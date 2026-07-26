#!/usr/bin/env python3
from __future__ import annotations
import base64, hashlib, zlib
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
payload_root = ROOT / ".chapter12"
part_a = (payload_root / "ch12.02a.part").read_bytes()
part_b = (payload_root / "ch12.02b.part").read_bytes()
if hashlib.sha256(part_a).hexdigest() != "7c52b06aa85c0c6d27df8f952607eba6fb0df47b7d87bf30539f24aae9594e7e":
    raise SystemExit("Invalid ch12.02a.part SHA")
if hashlib.sha256(part_b).hexdigest() != "20e323e178fa73878ab3342e68b02e674f9dee9d3b70345d6ec8546f996daa54":
    raise SystemExit("Invalid ch12.02b.part SHA")
rebuilt_payload = part_a + part_b
if hashlib.sha256(rebuilt_payload).hexdigest() != "b862e7677f3473db558d55a5d1525743908d7cfd5f31dadb745f634168d0724f":
    raise SystemExit("Invalid rebuilt ch12.02.b64 SHA")
(payload_root / "ch12.02.b64").write_bytes(rebuilt_payload)
parts = []
for path in sorted(payload_root.glob("finalizer.*.b64")):
    parts.append(zlib.decompress(base64.b64decode(path.read_bytes())))
source = b"".join(parts)
expected = "d42a4b126d44bb60821fa9eb9d4ec30d0f33319ff37a6bc70b149b46a8d7944b"
actual = hashlib.sha256(source).hexdigest()
if actual != expected:
    raise SystemExit(f"Finalizer SHA mismatch: {actual}")
exec(compile(source, str(Path(__file__)), "exec"), {"__name__": "__main__", "__file__": str(Path(__file__))})
