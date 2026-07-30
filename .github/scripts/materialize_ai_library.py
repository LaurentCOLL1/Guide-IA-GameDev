from __future__ import annotations

import base64
import json
from pathlib import Path
import zlib

PAYLOAD_SHA256 = "TODO"
PAYLOAD = """TODO"""

root = Path.cwd()
decoded = zlib.decompress(base64.b64decode(PAYLOAD.encode("ascii")))
if hashlib_sha := __import__("hashlib").sha256(decoded).hexdigest():
    if hashlib_sha != PAYLOAD_SHA256:
        raise SystemExit("AI Library payload checksum mismatch.")

files = json.loads(decoded.decode("utf-8"))
for relative, content in sorted(files.items()):
    target = root / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8", newline="\n")

Path(__file__).unlink()
print(f"AI Library materialized: {len(files)} files.")
