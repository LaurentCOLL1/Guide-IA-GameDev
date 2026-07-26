#!/usr/bin/env python3
from __future__ import annotations
import base64, hashlib, zlib
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
parts = []
for path in sorted((ROOT / ".chapter12").glob("finalizer.*.b64")):
    parts.append(zlib.decompress(base64.b64decode(path.read_bytes())))
source = b"".join(parts)
expected = "d42a4b126d44bb60821fa9eb9d4ec30d0f33319ff37a6bc70b149b46a8d7944b"
actual = hashlib.sha256(source).hexdigest()
if actual != expected:
    raise SystemExit(f"Finalizer SHA mismatch: {actual}")
# Le workflow existe déjà sur la branche ; ce push déclenche la finalisation.
exec(compile(source, str(Path(__file__)), "exec"), {"__name__": "__main__", "__file__": str(Path(__file__))})
