from __future__ import annotations

import base64
import hashlib
import json
import zlib
from pathlib import Path

ROOT = Path.cwd()
PACK = ROOT / "Companion-Pack/Database-Library"
PAYLOAD_SHA256 = "de8e68176c6f0f29a118683193f5b470b3d8426c79852887668845859d7e9a5a"


def main() -> int:
    encoded = (
        (ROOT / ".github/scripts/database_library_payload_1.txt").read_text(encoding="ascii").strip()
        + (ROOT / ".github/scripts/database_library_payload_2.txt").read_text(encoding="ascii").strip()
    )
    payload_bytes = zlib.decompress(base64.b64decode(encoded))
    if hashlib.sha256(payload_bytes).hexdigest() != PAYLOAD_SHA256:
        raise RuntimeError("materialization payload checksum mismatch")
    payload = json.loads(payload_bytes.decode("utf-8"))
    if not isinstance(payload, dict) or len(payload) != 30:
        raise RuntimeError("unexpected materialization payload")
    for relative, content in sorted(payload.items()):
        path = (PACK / relative).resolve()
        path.relative_to(PACK.resolve())
        if not isinstance(content, str):
            raise RuntimeError(f"non-text payload: {relative}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    trigger = PACK / ".materialization-trigger"
    if trigger.exists():
        trigger.unlink()
    print(f"Database Library materialized: {len(payload)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
