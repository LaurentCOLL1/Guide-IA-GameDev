#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
from pathlib import Path
import zlib

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = [
    (4200, "52573109f58d6e728db634b250737e2b750e04f6"),
    (4200, "41aaa5bcdaeb974d9ac45fa663e519c3670784f6"),
    (4200, "29183d5da11e7c215bb57dbcf36f8d199f6cf95d"),
    (4200, "9d2114839daf598930744c9b3ae8612934101be5"),
    (4200, "bafe2e359c86044e55e42d0eab5dae26aebe40ac"),
    (4200, "31f3de024f91375fa58c9e2b2a60118e7af5a59c"),
    (4200, "eff689ff0ab5cb55edf0ee4f96e95d2c043ab524"),
    (4200, "3ace3bf3f7e45a37c672f1e61239ff3084d8a555"),
    (4200, "c7b4c41a70e67b5f0535cdddb2d298b55e7aaa47"),
    (4200, "32c372ed9537087292e03301cc83c8e0683135bd"),
    (4200, "7bb20ebfdb0942e45518bd24702dae77041b5147"),
    (3832, "5040d46659fe39903e2dde67f2566b78b246a9cd"),
]
COMPRESSED_SHA256 = "e181038387c9012a86cac292828dd79a5a44dae2ef8dd3ec451a26d5c5d368a3"
SOURCE_SHA256 = "8f59418da7d79940737cb62ce2de5520957aaaab9a7ec02881f0e40831316873"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="


def sha1(text: str) -> str:
    return hashlib.sha1(text.encode("ascii")).hexdigest()


def repair(text: str, expected_length: int, expected_sha1: str) -> str:
    if len(text) == expected_length and sha1(text) == expected_sha1:
        return text
    candidates: list[str] = []
    if len(text) == expected_length:
        for i, current in enumerate(text):
            for char in ALPHABET:
                if char == current:
                    continue
                candidate = text[:i] + char + text[i + 1:]
                if sha1(candidate) == expected_sha1:
                    candidates.append(candidate)
    elif len(text) == expected_length + 1:
        for i in range(len(text)):
            candidate = text[:i] + text[i + 1:]
            if sha1(candidate) == expected_sha1:
                candidates.append(candidate)
    elif len(text) == expected_length - 1:
        for i in range(len(text) + 1):
            for char in ALPHABET:
                candidate = text[:i] + char + text[i:]
                if sha1(candidate) == expected_sha1:
                    candidates.append(candidate)
    unique = list(dict.fromkeys(candidates))
    if len(unique) != 1:
        raise SystemExit(
            f"Fragment irreparable or ambiguous: length={len(text)}, expected={expected_length}, matches={len(unique)}"
        )
    return unique[0]


parts = sorted((ROOT / ".qa").glob("l3-ch27-generator-part-*.txt"))
if len(parts) != len(EXPECTED):
    raise SystemExit(f"Expected {len(EXPECTED)} fragments, found {len(parts)}")

repaired: list[str] = []
for path, (expected_length, expected_sha1) in zip(parts, EXPECTED, strict=True):
    text = "".join(path.read_text(encoding="utf-8").split())
    repaired.append(repair(text, expected_length, expected_sha1))

compressed = base64.b64decode("".join(repaired), validate=True)
if hashlib.sha256(compressed).hexdigest() != COMPRESSED_SHA256:
    raise SystemExit("Compressed payload SHA-256 mismatch")
source = zlib.decompress(compressed)
if hashlib.sha256(source).hexdigest() != SOURCE_SHA256:
    raise SystemExit("Generator source SHA-256 mismatch")
code = compile(source, "<l3-ch27-generator>", "exec")
exec(code, {"__name__": "__main__", "__file__": str(ROOT / ".qa/l3-ch27-generated.py")})
