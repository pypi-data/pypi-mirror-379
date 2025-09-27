# (c) 2018 Mantas Mikulėnas <grawity@gmail.com>
# (c) 2024 E. Castedo Ellerman <castedo@castedo.com>
# Released under the MIT License (https://spdx.org/licenses/MIT)

from __future__ import annotations

import binascii
import hashlib
import io
from collections.abc import ByteString, Iterable
from typing import BinaryIO, ClassVar

from .binary_io import SshReader, SshWriter
from .ssh_public_key import PublicKey
from .unexceptional import cast_or_raise, unexceptional

# SSHSIG armored, blob, and signed data formats are documented in a file named
# `PROTOCOL.sshsig` which is archived from https://github.com/openssh/openssh-portable at
# https://archive.softwareheritage.org/swh:1:cnt:78457ddfc653519c056e36c79525712dafba4e6e


class InvalidSignature(Exception):
    pass


def ssh_enarmor_sshsig(raw: bytes) -> str:
    lines = ["-----BEGIN SSH SIGNATURE-----"]
    buf = binascii.b2a_base64(raw, newline=False).decode()
    for i in range(0, len(buf), 76):
        lines.append(buf[i : i + 76])
    lines += ["-----END SSH SIGNATURE-----", ""]
    return "\n".join(lines)


def ssh_dearmor_sshsig(buf: str | bytes) -> bytes:
    if isinstance(buf, bytes):
        buf = buf.decode('ascii')
    acc = ""
    match = False
    # TODO: stricter format check
    for line in buf.splitlines():
        if line == "-----BEGIN SSH SIGNATURE-----":
            match = True
        elif line == "-----END SSH SIGNATURE-----":
            break
        elif line and match:
            acc += line
    return binascii.a2b_base64(acc)


class SshsigWrapper:
    """The inner 'to-be-signed' data."""

    def __init__(
        self,
        *,
        namespace: bytes = b"",
        reserved: bytes = b"",
        hash_algo: bytes,
        hash: bytes,
    ) -> None:
        self.namespace = namespace
        self.reserved = reserved
        self.hash_algo = hash_algo
        self.hash = hash

    @staticmethod
    def from_bytes(buf: ByteString) -> SshsigWrapper:
        pkt = SshReader.from_bytes(buf)
        magic = pkt.read(6)
        if magic != b"SSHSIG":
            raise ValueError("magic preamble not found")
        return SshsigWrapper(
            namespace=pkt.read_string(),
            reserved=pkt.read_string(),
            hash_algo=pkt.read_string(),
            hash=pkt.read_string(),
        )

    def to_bytes(self) -> bytes:
        pkt = SshWriter(io.BytesIO())
        pkt.write(b"SSHSIG")
        pkt.write_string(self.namespace)
        pkt.write_string(self.reserved)
        pkt.write_string(self.hash_algo)
        pkt.write_string(self.hash)
        return pkt.output_fh.getvalue()

    def __bytes__(self) -> bytes:
        return self.to_bytes()


class SshsigSignature:
    VERSION: ClassVar[int] = 0x1

    public_key: bytes
    namespace: bytes
    hash_algo: bytes
    signature: bytes

    def __init__(self, buf: ByteString):
        pkt = SshReader.from_bytes(buf)
        if pkt.read(6) != b"SSHSIG":
            raise ValueError("SSH Signature magic preamble not found.")
        version = pkt.read_uint32()
        if version != SshsigSignature.VERSION:
            raise NotImplementedError(f"SSH Signature format version {version}.")
        self.public_key = pkt.read_string()
        self.namespace = pkt.read_string()
        pkt.read_string()  # reserved field to be ignored
        self.hash_algo = pkt.read_string()
        self.signature = pkt.read_string()

    def __bytes__(self) -> bytes:
        pkt = SshWriter(io.BytesIO())
        pkt.write(b"SSHSIG")
        pkt.write_uint32(SshsigSignature.VERSION)
        pkt.write_string(self.public_key)
        pkt.write_string(self.namespace)
        pkt.write_string(b"")  # reserved field to be ignored
        pkt.write_string(self.hash_algo)
        pkt.write_string(self.signature)
        return pkt.output_fh.getvalue()

    @staticmethod
    def from_armored(buf: str | bytes) -> SshsigSignature:
        return SshsigSignature(ssh_dearmor_sshsig(buf))

    def to_armored(self) -> str:
        return ssh_enarmor_sshsig(bytes(self))


def hash_file(msg_file: BinaryIO, hash_algo_name: str | bytes) -> bytes:
    return cast_or_raise(do_hash_file(msg_file, hash_algo_name))


def do_hash_file(
    msg_file: BinaryIO, hash_algo_name: str | bytes
) -> bytes | NotImplementedError:
    if isinstance(hash_algo_name, bytes):
        hash_algo_name = hash_algo_name.decode("ascii")
    hash_algo = hash_algo_name.lower()
    if hash_algo not in hashlib.algorithms_guaranteed:
        msg = "Signature hash algo '{}' not supported across platforms by Python."
        return unexceptional(NotImplementedError(msg.format(hash_algo)))
    hobj = hashlib.new(hash_algo)
    while data := msg_file.read(8192):
        hobj.update(data)
    return hobj.digest()


def do_sshsig_verify(
    sshsig_outer: SshsigSignature,
    msg_file: BinaryIO,
    namespace: str,
) -> PublicKey | InvalidSignature | NotImplementedError:
    """Verify the SSHSIG signature is for the input message and namespace.

    The SSHSIG signature is verified to be for the namespace and the embedded
    public key signature is valid for the provided input message.

    Returns:
      If no error, the cryptographic PublicKey embedded inside the SSHSIG signature.
      ValueError: If the input string is not a valid format or encoding.
      NotImplementedError: If a signature encoding feature is not supported.
    """
    # The intention of this implementation is to reproduce (approximately)
    # the behaviour of the sshsig_verify_fd function of the ssh-keygen C file:
    # sshsig.c
    # https://archive.softwareheritage.org/
    # swh:1:cnt:470b286a3a982875a48a5262b7057c4710b17fed

    _namespace = namespace.encode("ascii")
    if _namespace != sshsig_outer.namespace:
        errmsg = "Namespace of signature {} != {}"
        return unexceptional(
            InvalidSignature(errmsg.format(sshsig_outer.namespace, _namespace))
        )

    msg_hash = do_hash_file(msg_file, sshsig_outer.hash_algo)
    if isinstance(msg_hash, NotImplementedError):
        return msg_hash

    toverify = SshsigWrapper(
        namespace=_namespace, hash_algo=sshsig_outer.hash_algo, hash=msg_hash
    ).to_bytes()

    pub_key = PublicKey.do_from_ssh_encoding(sshsig_outer.public_key)
    if isinstance(pub_key, NotImplementedError):
        return pub_key
    if isinstance(pub_key, ValueError):
        return unexceptional(InvalidSignature(pub_key))
    if err := pub_key.do_verify(sshsig_outer.signature, toverify):
        return unexceptional(InvalidSignature(err))
    return pub_key


def check_signature(
    msg_in: str | bytes | BinaryIO,
    armored_signature: str | bytes,
    namespace: str = "git",
) -> PublicKey:
    """Check that an ssh-keygen signature is a digital signature of the input message.

    This function implements functionality provided by:
    ```
    ssh-keygen -Y check-novalidate -n namespace -s armored_signature_file < msg_in
    ```

    Returns:
      The cryptographic PublicKey embedded inside the SSHSIG signature.

    Raises:
      InvalidSignature: If signature is not valid for the input message.
      NotImplementedError: If a signature encoding feature is not supported.
    """
    return cast_or_raise(do_check_signature(msg_in, armored_signature, namespace))


def do_check_signature(
    msg_in: str | bytes | BinaryIO,
    armored_signature: str | bytes,
    namespace: str = "git",
) -> PublicKey | InvalidSignature | NotImplementedError:
    """Implementation of check_signature returning unexceptional Exception objects."""

    if isinstance(msg_in, str):
        msg_in = msg_in.encode()
    msg_file = io.BytesIO(msg_in) if isinstance(msg_in, bytes) else msg_in
    try:
        sshsig_outer = SshsigSignature.from_armored(armored_signature)
    except ValueError as ex:
        return unexceptional(InvalidSignature(ex))
    return do_sshsig_verify(sshsig_outer, msg_file, namespace)


def verify(
    msg_in: str | bytes | BinaryIO,
    armored_signature: str | bytes,
    allowed_signers: Iterable[PublicKey],
    namespace: str = "git",
) -> PublicKey:
    r"""Verify a signature generated by ssh-keygen, the OpenSSH authentication key utility.

    This function implements a _SUBSET_ of functionality provided by:
    ```sh
    ssh-keygen -Y verify \
        -f allowed_signers_file \
        -I '*' \
        -n namespace \
        -s armored_signature_file \
        < msg_in
    ```
    when the allowed_signers_file is in a sub-format with only lines starting:
    `* namespaces="X" ...`
    where X equals the namespace argument.

    Returns:
      The cryptographic PublicKey embedded inside the SSHSIG signature.

    Raises:
      InvalidSignature: If signature is not valid for the input message.
      NotImplementedError: If a signature encoding feature is not supported.
    """
    return cast_or_raise(
        do_verify(msg_in, armored_signature, allowed_signers, namespace)
    )


def do_verify(
    msg_in: str | bytes | BinaryIO,
    armored_signature: str | bytes,
    allowed_signers: Iterable[PublicKey],
    namespace: str = "git",
) -> PublicKey | InvalidSignature | NotImplementedError:
    """Implementation of verify returning unexceptional Exception objects."""
    ret = do_check_signature(msg_in, armored_signature, namespace)
    if not isinstance(ret, PublicKey):
        return ret
    if all(key != ret for key in allowed_signers):
        msg = "Signature public key not of allowed signer."
        return unexceptional(InvalidSignature(msg))
    return ret
