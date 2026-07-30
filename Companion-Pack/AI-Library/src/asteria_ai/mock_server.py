from __future__ import annotations

import argparse
import base64
from dataclasses import dataclass
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import socket
import socketserver
import struct
import threading
import time
from typing import Any


@dataclass
class MockState:
    failures_remaining: int = 0
    chat_calls: int = 0
    models_calls: int = 0


class MockHttpHandler(BaseHTTPRequestHandler):
    server_version = "AsteriaMock/1"
    state: MockState

    def log_message(self, format: str, *args: Any) -> None:
        return

    def do_GET(self) -> None:
        if self.path == "/health":
            self._json(200, {"status": "ok", "provider": "mock-provider"})
            return
        if self.path == "/v1/models":
            self.state.models_calls += 1
            self._json(200, {
                "object": "list",
                "data": [{"id": "mock-model", "object": "model", "owned_by": "mock-provider"}],
            })
            return
        self._json(404, {"error": {"code": "not_found"}})

    def do_POST(self) -> None:
        if self.path != "/v1/chat/completions":
            self._json(404, {"error": {"code": "not_found"}})
            return
        self.state.chat_calls += 1
        if self.state.failures_remaining > 0:
            self.state.failures_remaining -= 1
            self._json(503, {"error": {"code": "mock_transient"}})
            return
        length = int(self.headers.get("Content-Length", "0"))
        if length > 1_048_576:
            self._json(413, {"error": {"code": "too_large"}})
            return
        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            messages = payload["messages"]
            last = next(
                message["content"]
                for message in reversed(messages)
                if message.get("role") == "user"
            )
        except Exception:
            self._json(400, {"error": {"code": "invalid_request"}})
            return
        request_id = self.headers.get("X-Asteria-Request-Id", "missing")
        self._json(200, {
            "id": "chatcmpl-mock",
            "object": "chat.completion",
            "model": payload.get("model", "mock-model"),
            "choices": [{
                "index": 0,
                "message": {"role": "assistant", "content": f"mock:{last}"},
                "finish_reason": "stop",
            }],
            "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2},
            "asteria_request_id": request_id,
        })

    def _json(self, status: int, payload: dict) -> None:
        encoded = json.dumps(payload, separators=(",", ":")).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)


class _ReusableHttpServer(ThreadingHTTPServer):
    allow_reuse_address = True


class MockWebSocketHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        headers = self._read_headers()
        key = ""
        for line in headers.split("\r\n"):
            if line.lower().startswith("sec-websocket-key:"):
                key = line.split(":", 1)[1].strip()
        if not key:
            return
        accept = base64.b64encode(
            hashlib.sha1((key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode("ascii")).digest()
        ).decode("ascii")
        response = (
            "HTTP/1.1 101 Switching Protocols\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            f"Sec-WebSocket-Accept: {accept}\r\n\r\n"
        )
        self.request.sendall(response.encode("ascii"))
        opcode, payload = self._read_frame()
        if opcode != 0x1:
            return
        try:
            subscription = json.loads(payload.decode("utf-8"))
            request_id = str(subscription["request_id"])
        except Exception:
            return
        event = {
            "event": "task.progress",
            "request_id": request_id,
            "sequence": 1,
            "payload": {"progress": 0.5, "provider": "mock-provider"},
        }
        self._send_text(json.dumps(event, separators=(",", ":")))
        # Keep the TCP stream open long enough for event-loop clients such as
        # Godot WebSocketPeer to poll and consume the frame before teardown.
        time.sleep(0.25)

    def _read_headers(self) -> str:
        data = bytearray()
        while b"\r\n\r\n" not in data and len(data) <= 16_384:
            chunk = self.request.recv(1024)
            if not chunk:
                break
            data.extend(chunk)
        return data.decode("latin-1")

    def _read_frame(self) -> tuple[int, bytes]:
        first = self._recv_exact(2)
        opcode = first[0] & 0x0F
        masked = bool(first[1] & 0x80)
        length = first[1] & 0x7F
        if length == 126:
            length = struct.unpack("!H", self._recv_exact(2))[0]
        mask = self._recv_exact(4) if masked else b""
        payload = self._recv_exact(length)
        if masked:
            payload = bytes(byte ^ mask[index % 4] for index, byte in enumerate(payload))
        return opcode, payload

    def _send_text(self, text: str) -> None:
        payload = text.encode("utf-8")
        if len(payload) < 126:
            header = bytes([0x81, len(payload)])
        else:
            header = bytes([0x81, 126]) + struct.pack("!H", len(payload))
        self.request.sendall(header + payload)

    def _recv_exact(self, size: int) -> bytes:
        data = bytearray()
        while len(data) < size:
            chunk = self.request.recv(size - len(data))
            if not chunk:
                raise ConnectionError("Connexion interrompue.")
            data.extend(chunk)
        return bytes(data)


class _ReusableWebSocketServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


class MockServers:
    def __init__(self, *, http_port: int = 0, ws_port: int = 0, failures: int = 0):
        self.state = MockState(failures_remaining=failures)
        handler = type("BoundMockHttpHandler", (MockHttpHandler,), {"state": self.state})
        self.http = _ReusableHttpServer(("127.0.0.1", http_port), handler)
        self.ws = _ReusableWebSocketServer(("127.0.0.1", ws_port), MockWebSocketHandler)
        self._threads: list[threading.Thread] = []

    @property
    def http_url(self) -> str:
        return f"http://127.0.0.1:{self.http.server_address[1]}"

    @property
    def websocket_url(self) -> str:
        return f"ws://127.0.0.1:{self.ws.server_address[1]}/events"

    def start(self) -> "MockServers":
        for server in (self.http, self.ws):
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            self._threads.append(thread)
        return self

    def close(self) -> None:
        for server in (self.http, self.ws):
            server.shutdown()
            server.server_close()
        for thread in self._threads:
            thread.join(timeout=2.0)

    def __enter__(self) -> "MockServers":
        return self.start()

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--http-port", type=int, default=8765)
    parser.add_argument("--ws-port", type=int, default=8766)
    parser.add_argument("--failures", type=int, default=0)
    args = parser.parse_args()
    servers = MockServers(
        http_port=args.http_port, ws_port=args.ws_port, failures=args.failures
    ).start()
    print(
        json.dumps(
            {
                "status": "ready",
                "http_url": servers.http_url,
                "websocket_url": servers.websocket_url,
                "provider": "mock-provider",
            }
        ),
        flush=True,
    )
    try:
        while True:
            time.sleep(1.0)
    except KeyboardInterrupt:
        servers.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
