from __future__ import annotations

import base64
import hashlib
import json
import os
import socket
import struct
from urllib.parse import urlparse

from .errors import ConfigurationError, ProtocolError, TransportError


class WebSocketTextClient:
    """Client RFC 6455 minimal, limité aux tests et événements textuels locaux."""

    def __init__(self, url: str, *, timeout_seconds: float = 2.0):
        parsed = urlparse(url)
        if parsed.scheme != "ws":
            raise ConfigurationError("Seul ws local est qualifié par ce client minimal.")
        if parsed.hostname not in {"127.0.0.1", "localhost", "::1"}:
            raise ConfigurationError("WebSocket distant refusé.")
        if parsed.port is None:
            raise ConfigurationError("Port WebSocket obligatoire.")
        self._host = parsed.hostname
        self._port = parsed.port
        self._path = parsed.path or "/"
        self._timeout = timeout_seconds
        self._socket: socket.socket | None = None

    def connect(self) -> None:
        sock = socket.create_connection((self._host, self._port), timeout=self._timeout)
        key = base64.b64encode(os.urandom(16)).decode("ascii")
        request = (
            f"GET {self._path} HTTP/1.1\r\n"
            f"Host: {self._host}:{self._port}\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\n"
            "Sec-WebSocket-Version: 13\r\n\r\n"
        )
        sock.sendall(request.encode("ascii"))
        response = self._read_http_headers(sock)
        if " 101 " not in response.split("\r\n", 1)[0]:
            sock.close()
            raise TransportError("Handshake WebSocket refusé.")
        expected = base64.b64encode(
            hashlib.sha1((key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode("ascii")).digest()
        ).decode("ascii")
        if f"Sec-WebSocket-Accept: {expected}".lower() not in response.lower():
            sock.close()
            raise ProtocolError("Sec-WebSocket-Accept invalide.")
        self._socket = sock

    def send_json(self, payload: dict) -> None:
        text = json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
        self._send_frame(0x1, text.encode("utf-8"))

    def receive_json(self) -> dict:
        opcode, payload = self._receive_frame()
        if opcode != 0x1:
            raise ProtocolError("Une trame texte était attendue.")
        try:
            value = json.loads(payload.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ProtocolError("Événement WebSocket JSON invalide.") from exc
        if not isinstance(value, dict) or not value.get("request_id"):
            raise ProtocolError("Événement WebSocket non corrélé.")
        return value

    def close(self) -> None:
        if self._socket is not None:
            try:
                self._send_frame(0x8, b"")
            except OSError:
                pass
            self._socket.close()
            self._socket = None

    @staticmethod
    def _read_http_headers(sock: socket.socket) -> str:
        data = bytearray()
        while b"\r\n\r\n" not in data:
            chunk = sock.recv(1024)
            if not chunk:
                raise TransportError("Handshake WebSocket interrompu.")
            data.extend(chunk)
            if len(data) > 16_384:
                raise ProtocolError("En-têtes WebSocket trop volumineux.")
        return data.decode("latin-1")

    def _send_frame(self, opcode: int, payload: bytes) -> None:
        if self._socket is None:
            raise TransportError("WebSocket non connecté.")
        if len(payload) >= 126:
            raise ProtocolError("Payload WebSocket de test trop volumineux.")
        mask = os.urandom(4)
        header = bytes([0x80 | opcode, 0x80 | len(payload)]) + mask
        masked = bytes(byte ^ mask[index % 4] for index, byte in enumerate(payload))
        self._socket.sendall(header + masked)

    def _receive_frame(self) -> tuple[int, bytes]:
        if self._socket is None:
            raise TransportError("WebSocket non connecté.")
        first = self._recv_exact(2)
        opcode = first[0] & 0x0F
        masked = bool(first[1] & 0x80)
        length = first[1] & 0x7F
        if length == 126:
            length = struct.unpack("!H", self._recv_exact(2))[0]
        elif length == 127:
            length = struct.unpack("!Q", self._recv_exact(8))[0]
        if length > 1_048_576:
            raise ProtocolError("Trame WebSocket trop volumineuse.")
        mask = self._recv_exact(4) if masked else b""
        payload = self._recv_exact(length)
        if masked:
            payload = bytes(byte ^ mask[index % 4] for index, byte in enumerate(payload))
        return opcode, payload

    def _recv_exact(self, size: int) -> bytes:
        assert self._socket is not None
        data = bytearray()
        while len(data) < size:
            chunk = self._socket.recv(size - len(data))
            if not chunk:
                raise TransportError("Connexion WebSocket interrompue.")
            data.extend(chunk)
        return bytes(data)
