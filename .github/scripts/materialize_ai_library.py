from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path
import zlib

EXPECTED_SHA256 = "61aa5ec33c827ea4d395dff7f7fee56368e93b3ccc813bb0cc71d104788c0944"
root = Path.cwd()
payload_dir = root / ".github/ai-library-payload"
encoded = "".join(
    part.read_text(encoding="ascii").strip()
    for part in sorted(payload_dir.glob("part-*.txt"))
)
decoded = zlib.decompress(base64.b64decode(encoded, validate=True))
actual = hashlib.sha256(decoded).hexdigest()
if actual != EXPECTED_SHA256:
    raise SystemExit(f"AI Library payload checksum mismatch: {actual}")

files = json.loads(decoded.decode("utf-8"))
for relative, content in sorted(files.items()):
    target = root / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8", newline="\n")

for part in payload_dir.glob("part-*.txt"):
    part.unlink()
payload_dir.rmdir()
for temporary in [
    root / ".github/scripts/materialize_ai_library.py",
    root / ".github/ai-library-materialize.trigger",
]:
    if temporary.exists():
        temporary.unlink()

print(f"AI Library materialized: {len(files)} files; payload {actual}.")
