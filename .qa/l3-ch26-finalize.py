#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
from pathlib import Path
import zlib

ROOT = Path(__file__).resolve().parents[1]
PARTS = sorted((ROOT / ".qa").glob("l3-ch26-generator-part-*.txt"))
EXPECTED_PARTS = 9
EXPECTED_COMPRESSED = "a83c4bc1ef6c003eb59b3ed33cb0af9be3297c1c3a83379526d1ca18934ae52e"
EXPECTED_SCRIPT = "6fb13f63e59f369559c0e0a1f70d8f41c5791bb15e311018198dc8926cead711"

if len(PARTS) != EXPECTED_PARTS:
    raise SystemExit(f"Expected {EXPECTED_PARTS} fragments, found {len(PARTS)}")

# Les espaces et retours ajoutés par le transport ne font pas partie de Base64.
encoded = "".join("".join(path.read_text(encoding="utf-8").split()) for path in PARTS)
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
