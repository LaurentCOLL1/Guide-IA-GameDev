#!/usr/bin/env python3
from pathlib import Path
import base64
import bz2

parts = sorted(Path(".qa").glob("l3-ch23-payload-*.txt"))
if not parts:
    raise RuntimeError("Payload du chapitre 23 absent.")

payload = "".join(path.read_text(encoding="utf-8").strip() for path in parts)
source = bz2.decompress(base64.b64decode(payload))

for path in parts:
    path.unlink()

exec(compile(source, __file__, "exec"))
