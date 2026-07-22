from __future__ import annotations

import base64
import json
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHUNKS = [ROOT / ".qa" / f"l3-ch01-{index:02d}.b64" for index in range(5)]

missing = [path.as_posix() for path in CHUNKS if not path.is_file()]
if missing:
    raise RuntimeError(f"Fragments absents : {missing}")

encoded = "".join(path.read_text(encoding="ascii").strip() for path in CHUNKS)
data = json.loads(zlib.decompress(base64.b64decode(encoded)).decode("utf-8"))

for relative, content in data["new_files"].items():
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")

for operation in data["ops"]:
    path = ROOT / operation["path"]
    text = path.read_text(encoding="utf-8")
    count = text.count(operation["old"])
    if count != 1:
        raise RuntimeError(
            f"{operation['label']}: attendu une occurrence, trouvé {count} dans {operation['path']}"
        )
    path.write_text(
        text.replace(operation["old"], operation["new"], 1),
        encoding="utf-8",
        newline="\n",
    )

for path in CHUNKS:
    path.unlink(missing_ok=True)
Path(__file__).unlink(missing_ok=True)

print("Chapitre 1 du Livre III, audit, preuve et gouvernance matérialisés.")
