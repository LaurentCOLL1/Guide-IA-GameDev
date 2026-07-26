#!/usr/bin/env python3
from __future__ import annotations
import base64, hashlib, zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
payload_root = ROOT / ".chapter12"


def read_verified(path: str, expected: str) -> bytes:
    data = (payload_root / path).read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    if actual != expected:
        raise SystemExit(f"Invalid {path} SHA: {actual}")
    return data


def write_verified(name: str, pieces: list[bytes], expected: str) -> None:
    rebuilt = b"".join(pieces)
    actual = hashlib.sha256(rebuilt).hexdigest()
    if actual != expected:
        raise SystemExit(f"Invalid rebuilt {name} SHA: {actual}")
    (payload_root / name).write_bytes(rebuilt)


write_verified(
    "ch12.02.b64",
    [
        read_verified("ch12.02a.part", "7c52b06aa85c0c6d27df8f952607eba6fb0df47b7d87bf30539f24aae9594e7e"),
        read_verified("ch12.02b.part", "20e323e178fa73878ab3342e68b02e674f9dee9d3b70345d6ec8546f996daa54"),
    ],
    "b862e7677f3473db558d55a5d1525743908d7cfd5f31dadb745f634168d0724f",
)
part_05b = b"".join(
    [
        read_verified("ch12.05b1.part", "3a6f2af217f681cfcc8e3093cae37278280c501b6e3cebe05e96dd687952cc70"),
        read_verified("ch12.05b2.part", "8e91300553112c785b4164bb863caba7485e08306159ef3622142d90ee0d8350"),
    ]
)
if hashlib.sha256(part_05b).hexdigest() != "b6cd26f972c695151c3e6f9cb4534bf8219eb9b8f05e6c2d503020ab7816c7fe":
    raise SystemExit("Invalid rebuilt ch12.05b.part SHA")
write_verified(
    "ch12.05.b64",
    [
        read_verified("ch12.05a.part", "9b556fee380d448b1d8b02f9cf1f0ae988d252a12bc1b4d6e9b8488d12949f3e"),
        part_05b,
    ],
    "6feb990c0a886287e5e950773274a7fc913c2a5712865b31be062723304d2e7a",
)

parts: list[bytes] = []
for path in sorted(payload_root.glob("finalizer.*.b64")):
    parts.append(zlib.decompress(base64.b64decode(path.read_bytes())))
source = b"".join(parts)
expected = "d42a4b126d44bb60821fa9eb9d4ec30d0f33319ff37a6bc70b149b46a8d7944b"
actual = hashlib.sha256(source).hexdigest()
if actual != expected:
    raise SystemExit(f"Finalizer SHA mismatch: {actual}")
exec(
    compile(source, str(Path(__file__)), "exec"),
    {"__name__": "__main__", "__file__": str(Path(__file__))},
)
