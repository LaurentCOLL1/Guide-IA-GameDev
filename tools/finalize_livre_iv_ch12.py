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


def join_verified(name: str, pieces: list[bytes], expected: str) -> bytes:
    rebuilt = b"".join(pieces)
    actual = hashlib.sha256(rebuilt).hexdigest()
    if actual != expected:
        raise SystemExit(f"Invalid rebuilt {name} SHA: {actual}")
    return rebuilt


def write_verified(name: str, pieces: list[bytes], expected: str) -> None:
    (payload_root / name).write_bytes(join_verified(name, pieces, expected))


def rebuild_b64_from_zlib(number: int, sha_a: str, sha_b: str, raw_sha: str, file_sha: str) -> None:
    raw = join_verified(
        f"ch12.{number:02d}.zlib",
        [
            read_verified(f"ch12.{number:02d}a.zlib", sha_a),
            read_verified(f"ch12.{number:02d}b.zlib", sha_b),
        ],
        raw_sha,
    )
    encoded = base64.b64encode(raw) + b"\n"
    actual = hashlib.sha256(encoded).hexdigest()
    if actual != file_sha:
        raise SystemExit(f"Invalid rebuilt ch12.{number:02d}.b64 SHA: {actual}")
    (payload_root / f"ch12.{number:02d}.b64").write_bytes(encoded)


write_verified(
    "ch12.02.b64",
    [
        read_verified("ch12.02a.part", "7c52b06aa85c0c6d27df8f952607eba6fb0df47b7d87bf30539f24aae9594e7e"),
        read_verified("ch12.02b.part", "20e323e178fa73878ab3342e68b02e674f9dee9d3b70345d6ec8546f996daa54"),
    ],
    "b862e7677f3473db558d55a5d1525743908d7cfd5f31dadb745f634168d0724f",
)
part_05b2 = join_verified(
    "ch12.05b2.part",
    [
        read_verified("ch12.05b2a.part", "e93e18d710edd28f39837552894661d1b39f6d019926bde58727a2ca38d9c7bc"),
        read_verified("ch12.05b2b.part", "1d3e12a4b7cb2865792bf7741d59275aa96ab763e93d9361a3b0b12e5aaed633"),
    ],
    "8e91300553112c785b4164bb863caba7485e08306159ef3622142d90ee0d8350",
)
part_05b = join_verified(
    "ch12.05b.part",
    [
        read_verified("ch12.05b1.part", "3a6f2af217f681cfcc8e3093cae37278280c501b6e3cebe05e96dd687952cc70"),
        part_05b2,
    ],
    "b6cd26f972c695151c3e6f9cb4534bf8219eb9b8f05e6c2d503020ab7816c7fe",
)
write_verified(
    "ch12.05.b64",
    [
        read_verified("ch12.05a.part", "9b556fee380d448b1d8b02f9cf1f0ae988d252a12bc1b4d6e9b8488d12949f3e"),
        part_05b,
    ],
    "6feb990c0a886287e5e950773274a7fc913c2a5712865b31be062723304d2e7a",
)
rebuild_b64_from_zlib(
    6,
    "fa89c32e743665770ecdeba07ffee4299469fb30c6853d74e1a2cb418830b2b3",
    "31848a931ee9e32801bf917948bdffcc7d73cdcfbc271d61802af4fe8b8e27ee",
    "b4e923ce1f70f25f9bf644934e68806ea1656800101ad3ec46cb6ceedc324e2d",
    "b553cb14d497219d9ac5d061a536be9b84bdda9f8fed304e907e86b424a791ea",
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
