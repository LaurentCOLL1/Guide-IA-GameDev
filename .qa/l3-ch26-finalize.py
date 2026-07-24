#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
from pathlib import Path
import zlib

ROOT = Path(__file__).resolve().parents[1]
PARTS = sorted((ROOT / ".qa").glob("l3-ch26-generator-part-*.txt"))
EXPECTED = [
    (6000, "b869749131e7551754de0f46296601b941741329"),
    (6000, "1de8698e30dc0ac70c03bf04ace43e050f9d9b80"),
    (6000, "e55b2d1fb52f57f43036f743c943bcdfaaacaecb"),
    (6000, "aee54775771fee1502862bda504c6a66b9ede882"),
    (6000, "f129d58eb5bb35ad6bd8ab4ac42accfd0f47ef3f"),
    (6000, "35859118f276f1ff3c24b81ff89031d47c4e0bb5"),
    (6000, "066af475c75ed5c6a0e10ddbfc5f88878e61e03e"),
    (6000, "2edefe06a2e35b9bdda91e10a631057dda12dc49"),
    (1516, "41fda277e6ca3cc9b47a988e4744cb378791b7e0"),
]
EXPECTED_COMPRESSED = "a83c4bc1ef6c003eb59b3ed33cb0af9be3297c1c3a83379526d1ca18934ae52e"
EXPECTED_SCRIPT = "6fb13f63e59f369559c0e0a1f70d8f41c5791bb15e311018198dc8926cead711"
ALPHABET = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

if len(PARTS) != len(EXPECTED):
    raise SystemExit(f"Expected {len(EXPECTED)} fragments, found {len(PARTS)}")

clean_parts: list[bytes] = []
for path, (expected_length, expected_sha1) in zip(PARTS, EXPECTED):
    clean = "".join(path.read_text(encoding="utf-8").split()).encode("ascii")
    if len(clean) != expected_length:
        raise SystemExit(f"Unexpected fragment length: {path.name}")
    if hashlib.sha1(clean).hexdigest() != expected_sha1:
        matches: list[bytes] = []
        work = bytearray(clean)
        for position, original in enumerate(work):
            for replacement in ALPHABET:
                if replacement == original:
                    continue
                work[position] = replacement
                candidate = bytes(work)
                if hashlib.sha1(candidate).hexdigest() == expected_sha1:
                    matches.append(candidate)
                work[position] = original
        if len(matches) != 1:
            raise SystemExit(f"Fragment repair is not unique: {path.name}, matches={len(matches)}")
        clean = matches[0]
    clean_parts.append(clean)

encoded = b"".join(clean_parts)
compressed = base64.b64decode(encoded, validate=True)
if hashlib.sha256(compressed).hexdigest() != EXPECTED_COMPRESSED:
    raise SystemExit("Compressed payload SHA-256 mismatch")
source = zlib.decompress(compressed)
if hashlib.sha256(source).hexdigest() != EXPECTED_SCRIPT:
    raise SystemExit("Generator script SHA-256 mismatch")

code = compile(source, "<l3-ch26-generator>", "exec")
exec(code, {"__name__": "__main__", "__file__": str(ROOT / ".qa/l3-ch26-generated.py")})

for path in PARTS:
    path.unlink()
diagnostic = ROOT / ".qa/l3-ch26-diagnostic.txt"
if diagnostic.exists():
    diagnostic.unlink()
