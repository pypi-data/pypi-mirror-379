import os
import struct
from http.client import HTTPConnection
from socket import socket as socket_cls
from typing import Optional, Callable, Any

from OpenSSL.SSL import Connection
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from urllib3.contrib.pyopenssl import WrappedSocket

from .tls import create_ssl_context, TeeInfo


def encrypt(cipher_key: bytes, nonce: bytes, plaintext: bytes) -> bytes:
    encryptor = Cipher(algorithms.AES(cipher_key), modes.GCM(nonce)).encryptor()
    ciphertext = nonce + encryptor.update(plaintext) + encryptor.finalize() + encryptor.tag
    return struct.pack(">I", len(ciphertext)) + ciphertext


def decrypt(cipher_key: bytes, nonce: bytes, ciphertext: bytes) -> bytes:
    decryptor = Cipher(algorithms.AES(cipher_key), modes.GCM(nonce, ciphertext[-16:])).decryptor()
    plaintext = decryptor.update(ciphertext[:-16]) + decryptor.finalize()
    return plaintext


class TeeSocket(WrappedSocket):
    def __init__(
        self,
        connection: Connection,
        socket: socket_cls,
        suppress_ragged_eofs: bool = True,
        send_callback: Optional[Callable[[bytes, bytes, bytes, bytes], None]] = None,
        recv_callback: Optional[Callable[[bytes, bytes, bytes, bytes], None]] = None,
    ):
        super().__init__(connection=connection, socket=socket, suppress_ragged_eofs=suppress_ragged_eofs)
        self.send_callback = send_callback
        self.recv_callback = recv_callback

        # ecdh handshake
        private_key = ec.generate_private_key(ec.SECP256R1())
        public_key_bytes = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.X962, format=serialization.PublicFormat.UncompressedPoint
        )
        super().sendall(b"Amanises: " + public_key_bytes)

        server_public_key = ec.EllipticCurvePublicKey.from_encoded_point(ec.SECP256R1(), super().recv(75))
        self.cipher_key = HKDF(algorithm=hashes.SHA256(), length=16, salt=None, info=b"ecdh-to-aes").derive(
            private_key.exchange(ec.ECDH(), server_public_key),
        )

    def send(self, plaintext: bytes) -> int:
        nonce = os.urandom(12)
        ciphertext = encrypt(self.cipher_key, nonce, plaintext)
        if self.send_callback is not None:
            self.send_callback(self.cipher_key, nonce, plaintext, ciphertext)
        return self._send_until_done(ciphertext)

    def sendall(self, data: bytes) -> None:
        total_sent = 0
        while total_sent < len(data):
            sent = self.send(data[total_sent : total_sent + 16384])
            total_sent += sent

    def recv(self, size: int) -> bytes:
        raise NotImplementedError

    def recv_into(self, buffer: Any) -> int:
        length = struct.unpack(">I", super().recv(4))[0] - 12
        assert length > 0
        nonce = super().recv(12)
        ciphertext = super().recv(length)
        plaintext = decrypt(self.cipher_key, nonce, ciphertext)
        if self.recv_callback is not None:
            self.recv_callback(self.cipher_key, nonce, plaintext, ciphertext)
        length = len(plaintext)
        buffer[:length] = memoryview(plaintext)
        return length


class TeeConnection(HTTPConnection):
    def __init__(
        self,
        host: str,
        port: Optional[int] = None,
        send_callback: Optional[Callable[[bytes, bytes, bytes, bytes], None]] = None,
        recv_callback: Optional[Callable[[bytes, bytes, bytes, bytes], None]] = None,
        **kwargs,
    ):
        self.cipher_key: Optional[bytes] = None
        self.ssl_context = create_ssl_context()
        self.send_callback = send_callback
        self.recv_callback = recv_callback
        super().__init__(host=host, port=port, **kwargs)

    def connect(self):
        super().connect()
        sock = self.ssl_context.wrap_socket(self.sock, server_hostname=self.host)
        self.sock = TeeSocket(
            connection=sock.connection,
            socket=sock.socket,
            suppress_ragged_eofs=sock.suppress_ragged_eofs,
            send_callback=self.send_callback,
            recv_callback=self.recv_callback,
        )

    def get_tee_info(self) -> Optional[TeeInfo]:
        if self.sock is None:
            return None
        return self.sock.connection.tee_info
