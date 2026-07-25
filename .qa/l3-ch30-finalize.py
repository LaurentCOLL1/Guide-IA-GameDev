#!/usr/bin/env python3
from __future__ import annotations
import base64, gzip, hashlib, subprocess, sys, tempfile
from pathlib import Path

EXPECTED_LENGTHS = [4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 2244]
EXPECTED_SHA1 = ['361babdbd462d223af112d9bea4ed091f13746ae', 'eb2a807e046f53980b58c5a9e884e8bf191f353f', 'c5964ec462063ee946dc04baa850ff8f2feb452a', '508591f96926695bc64efb4b0943aa0d2f5577ef', 'b4526ecd88d2d46630d51da0545e2dc8c1b59a8a', '90420c279d042a163f61637268405ae4c6508e95', 'd4cfc2978b8b2dedad3d8c731509121988f19ecc', 'f2c3aed303687db9126b00bc161f6ff4f665b1f1', '68a1d666ab1c746140e158ca2f1e1c6ad94723e4', 'd5fd4d5e45db88c788a6fa62d6e31b3b752eeaf3', 'eb38f7fe4dc4048e77fb407df785bc7c2c611439', '2065dcdb37f09bd2e6fc2204dd38127f4b8ea656']
EXPECTED_GZIP_SHA256 = "1f41fd6544977f330c1edc18d5753f7a7002a7e3bf957b8d5411a2a470632434"
EXPECTED_RAW_SHA256 = "6ce8f55089fd9828366808b9c0f54f4b5798512bb1cdaa2be80dc303b10bdcc6"

parts = []
for index, (expected_len, expected_sha1) in enumerate(zip(EXPECTED_LENGTHS, EXPECTED_SHA1), start=1):
    path = Path(f".qa/l3-ch30-generator-part-{index:02d}.txt")
    text = "".join(path.read_text(encoding="utf-8").split())
    actual_sha1 = hashlib.sha1(text.encode("ascii")).hexdigest()
    if len(text) != expected_len or actual_sha1 != expected_sha1:
        raise SystemExit(f"Fragment {index} invalide: len={len(text)} sha1={actual_sha1}")
    parts.append(text)

payload = base64.b64decode("".join(parts), validate=True)
actual_gzip = hashlib.sha256(payload).hexdigest()
if actual_gzip != EXPECTED_GZIP_SHA256:
    raise SystemExit(f"Payload gzip invalide: {actual_gzip}")
raw = gzip.decompress(payload)
actual_raw = hashlib.sha256(raw).hexdigest()
if actual_raw != EXPECTED_RAW_SHA256:
    raise SystemExit(f"Générateur invalide: {actual_raw}")
compile(raw, "<l3-ch30-generator>", "exec")
with tempfile.NamedTemporaryFile(prefix="l3-ch30-generator-", suffix=".py", delete=False) as handle:
    handle.write(raw)
    temp_path = Path(handle.name)
try:
    subprocess.run([sys.executable, str(temp_path)], check=True)
finally:
    temp_path.unlink(missing_ok=True)
