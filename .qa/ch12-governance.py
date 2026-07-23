#!/usr/bin/env python3
import base64
import gzip
import runpy
from pathlib import Path

chapter_path = Path("Livre-III/CHAPITRE-12-Objets-equipements-et-armes.md")
package_parts = [Path(f".qa/ch12-package-{index:02d}.txt") for index in range(1, 10)]
missing = [str(path) for path in package_parts if not path.is_file()]
if missing:
    raise RuntimeError("Paquet exact du chapitre 12 incomplet : " + ", ".join(missing))

encoded = "".join(path.read_text(encoding="utf-8").strip() for path in package_parts)
chapter_path.write_bytes(gzip.decompress(base64.b64decode(encoded)))

for path in package_parts:
    path.unlink()
for index in range(1, 6):
    old_part = Path(f".qa/ch12-chapter-{index:02d}.txt")
    if old_part.exists():
        old_part.unlink()

core = Path(".qa/ch12-governance-core.py")
runpy.run_path(str(core), run_name="__main__")
core.unlink()
