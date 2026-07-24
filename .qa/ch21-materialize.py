#!/usr/bin/env python3
from __future__ import annotations

import base64
import zlib
from pathlib import Path

root = Path(__file__).resolve().parent
parts = sorted(root.glob("ch21-payload-*.txt"))
if len(parts) != 7:
    raise RuntimeError(f"Sept fragments attendus, trouvé {len(parts)}")
payload = "".join(path.read_text(encoding="utf-8").strip() for path in parts)
source = zlib.decompress(base64.b64decode(payload))
exec(compile(source, __file__, "exec"))
for path in parts:
    path.unlink()
