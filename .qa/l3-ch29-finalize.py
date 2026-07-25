#!/usr/bin/env python3
from __future__ import annotations
import base64, gzip, hashlib, subprocess, sys, tempfile
from pathlib import Path

EXPECTED_LENGTHS = [4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 2904]
EXPECTED_SHA1 = ['270c6c898b8cba19f8ec978ec4b25157c3b6e8fd', 'dc827f43182384724d998bf0b5a1383b714480c2', '4b8d1d02fe49b359eb16df9ced00b46f5231a94d', 'accc0c2da42695db12dbc730d8fe4c40b0d6da59', 'c98ede6dcee98a8fda35f19556fa1b97cc57c3d0', '0a260b87024e36e2894456eb59db66a25855fb26', 'cb87dc5c621c083170d163d21c0af4727b51bce8', '3fef25084837c3e7b961c54892148c0354c727ac', '1080a1e4506d382f0a491a21fbf590ff6102efb5', 'af492f7402d833282776d4a72c6e41b66b4f2d93', '1d06ff750eef88818487233be06ce144ddc7589a', '17879c167425a4bec94db8a20e6c98f50f85803b']
EXPECTED_GZIP_SHA256 = "84fc14bb9400d101b7be8bbaf09d8e987e1094fcf7c9a0dd1a7111e04df5d1b6"
EXPECTED_RAW_SHA256 = "93451134b56000f23e2f9fa1dfd6ac19c6200ec9ef32d1656b6532fa4d45aa52"

parts = []
for index, (expected_len, expected_sha1) in enumerate(zip(EXPECTED_LENGTHS, EXPECTED_SHA1), start=1):
    path = Path(f".qa/l3-ch29-generator-part-{index:02d}.txt")
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
compile(raw, "<l3-ch29-generator>", "exec")
with tempfile.NamedTemporaryFile(prefix="l3-ch29-generator-", suffix=".py", delete=False) as handle:
    handle.write(raw)
    temp_path = Path(handle.name)
try:
    subprocess.run([sys.executable, str(temp_path)], check=True)
finally:
    temp_path.unlink(missing_ok=True)
