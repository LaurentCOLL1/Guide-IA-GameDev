from __future__ import annotations
import binascii
import json
import struct
import zlib
from pathlib import Path

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"

def _chunk(kind: bytes, payload: bytes) -> bytes:
    return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", binascii.crc32(kind + payload) & 0xFFFFFFFF)

def write_checkerboard(path: Path, width: int = 64, height: int = 64) -> None:
    if width <= 0 or height <= 0 or width > 512 or height > 512:
        raise ValueError("invalid image dimensions")
    rows = []
    for y in range(height):
        row = bytearray([0])
        for x in range(width):
            light = ((x // 16) + (y // 16)) % 2 == 0
            value = 208 if light else 32
            row.extend((value, value, value))
        rows.append(bytes(row))
    payload = b"".join(rows)
    png = (
        PNG_SIGNATURE
        + _chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
        + _chunk(b"IDAT", zlib.compress(payload, level=9))
        + _chunk(b"IEND", b"")
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(png)

def text_chunks(path: Path) -> dict[str, str]:
    data = path.read_bytes()
    if not data.startswith(PNG_SIGNATURE):
        raise ValueError("not a PNG file")
    offset = len(PNG_SIGNATURE)
    result: dict[str, str] = {}
    while offset < len(data):
        if offset + 12 > len(data):
            raise ValueError("truncated PNG")
        size = struct.unpack(">I", data[offset:offset+4])[0]
        kind = data[offset+4:offset+8]
        payload = data[offset+8:offset+8+size]
        crc_expected = struct.unpack(">I", data[offset+8+size:offset+12+size])[0]
        if (binascii.crc32(kind + payload) & 0xFFFFFFFF) != crc_expected:
            raise ValueError("invalid PNG CRC")
        if kind == b"tEXt" and b"\x00" in payload:
            key, value = payload.split(b"\x00", 1)
            result[key.decode("latin-1")] = value.decode("latin-1")
        elif kind == b"iTXt":
            parts = payload.split(b"\x00", 5)
            if len(parts) == 6:
                key, compressed, _, _, _, value = parts
                if compressed == b"\x01":
                    value = zlib.decompress(value)
                result[key.decode("utf-8")] = value.decode("utf-8")
        offset += 12 + size
        if kind == b"IEND":
            break
    return result

def assert_comfy_metadata(path: Path) -> dict[str, object]:
    chunks = text_chunks(path)
    missing = [name for name in ("prompt", "workflow") if name not in chunks]
    if missing:
        raise ValueError("missing PNG metadata: " + ", ".join(missing))
    parsed = {}
    for name in ("prompt", "workflow"):
        parsed[name] = json.loads(chunks[name])
    return parsed
