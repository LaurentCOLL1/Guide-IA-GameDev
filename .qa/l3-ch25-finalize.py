#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
from pathlib import Path
import zlib

ROOT = Path(__file__).resolve().parents[1]
QA = ROOT / ".qa"
PARTS = sorted(QA.glob("l3-ch25-generator-part-*.txt"))
EXPECTED_PARTS = 6
EXPECTED_COMPRESSED = "9011c9bf077f9cae2c737b22dc65d5ad85b36db0c7d9ecbb7521995d0bedde9b"
EXPECTED_SCRIPT = "0d6baaef465abd5f9d957efbdae8b4ca3f49a314ba857257fecca4be2b88d993"
PART3_SHA1 = "22662579ac053852c637112c75f9607ba92b1187"

if len(PARTS) != EXPECTED_PARTS:
    raise SystemExit(f"Expected {EXPECTED_PARTS} fragments, found {len(PARTS)}")

part3 = PARTS[2]
content3 = part3.read_text(encoding="utf-8").strip()
if len(content3) == 9001:
    matches = []
    for index in range(len(content3)):
        candidate = content3[:index] + content3[index + 1:]
        if hashlib.sha1(candidate.encode("utf-8")).hexdigest() == PART3_SHA1:
            matches.append(candidate)
    if len(matches) != 1:
        raise SystemExit(f"Fragment 3 repair expected one match, found {len(matches)}")
    content3 = matches[0]
    part3.write_text(content3, encoding="utf-8")
elif len(content3) != 9000 or hashlib.sha1(content3.encode("utf-8")).hexdigest() != PART3_SHA1:
    raise SystemExit("Fragment 3 does not match expected length and SHA-1")

encoded = "".join(path.read_text(encoding="utf-8").strip() for path in PARTS)
compressed = base64.b64decode(encoded, validate=True)
if hashlib.sha256(compressed).hexdigest() != EXPECTED_COMPRESSED:
    raise SystemExit("Compressed payload SHA-256 mismatch")

source = zlib.decompress(compressed)
if hashlib.sha256(source).hexdigest() != EXPECTED_SCRIPT:
    raise SystemExit("Generator script SHA-256 mismatch")

code = compile(source, "<l3-ch25-generator>", "exec")
exec(code, {"__name__": "__main__", "__file__": str(QA / "l3-ch25-generated.py")})

(QA / "l3-ch25-error.txt").unlink(missing_ok=True)
for path in PARTS:
    path.unlink()
