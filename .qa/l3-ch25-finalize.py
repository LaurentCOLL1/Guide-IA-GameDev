#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
from pathlib import Path
import zlib

ROOT = Path(__file__).resolve().parents[1]
PARTS = sorted((ROOT / ".qa").glob("l3-ch25-generator-part-*.txt"))
EXPECTED_PARTS = 6
EXPECTED_COMPRESSED = "9011c9bf077f9cae2c737b22dc65d5ad85b36db0c7d9ecbb7521995d0bedde9b"
EXPECTED_SCRIPT = "0d6baaef465abd5f9d957efbdae8b4ca3f49a314ba857257fecca4be2b88d993"

if len(PARTS) != EXPECTED_PARTS:
    raise SystemExit(f"Expected {EXPECTED_PARTS} fragments, found {len(PARTS)}")

encoded = "".join(path.read_text(encoding="utf-8").strip() for path in PARTS)
compressed = base64.b64decode(encoded, validate=True)
if hashlib.sha256(compressed).hexdigest() != EXPECTED_COMPRESSED:
    raise SystemExit("Compressed payload SHA-256 mismatch")

source = zlib.decompress(compressed)
if hashlib.sha256(source).hexdigest() != EXPECTED_SCRIPT:
    raise SystemExit("Generator script SHA-256 mismatch")

code = compile(source, "<l3-ch25-generator>", "exec")
exec(code, {"__name__": "__main__", "__file__": str(ROOT / ".qa/l3-ch25-generated.py")})

for path in PARTS:
    path.unlink()
