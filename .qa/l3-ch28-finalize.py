#!/usr/bin/env python3
from __future__ import annotations
import base64, gzip, hashlib, subprocess, sys, tempfile
from pathlib import Path

EXPECTED_LENGTHS = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 1312]
EXPECTED_SHA1 = ['1be30677a8b4ac3d09bbfc4cd73b22359ac3b0e9', '554d24ee3a7dbf34de9bf618a06067daef0c7643', '63d311572259de6e3ad69226397040ab558f083f', '133a0f5879edf3914b8207cda5dafddf7366d743', 'e1785099f413c81e03ee3e34c6ca535709887581', 'f6498bc717d4caf42724a134beb75266d1aeba55', 'c294830179b7fe999eee6d221cab05f24f18e9e0', 'd1674d65a601c333de1d9ca7a3e08439b2958ec4', '5b7edbcbf5b424d5ea1177a9437eeebaef6874fe']
EXPECTED_GZIP_SHA256 = "68e2aaca426c81e35a58f2ffa7efd32715f4fc3e55968c39cfe2837963ff309e"
EXPECTED_RAW_SHA256 = "c4626eefccf49e2087b478b7d25cd64280c5290989ae81f2b0abaa36f3905f0f"

parts = []
for index, (expected_len, expected_sha1) in enumerate(zip(EXPECTED_LENGTHS, EXPECTED_SHA1), start=1):
    path = Path(f".qa/l3-ch28-generator-part-{index:02d}.txt")
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
compile(raw, "<l3-ch28-generator>", "exec")
with tempfile.NamedTemporaryFile(prefix="l3-ch28-generator-", suffix=".py", delete=False) as handle:
    handle.write(raw)
    temp_path = Path(handle.name)
try:
    subprocess.run([sys.executable, str(temp_path)], check=True)
finally:
    temp_path.unlink(missing_ok=True)
