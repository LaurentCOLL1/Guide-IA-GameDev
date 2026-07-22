from __future__ import annotations

import base64
import json
import traceback
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHUNKS = [ROOT / ".qa" / f"l3-ch01-{index:02d}.b64" for index in range(5)]
DIAGNOSTIC = ROOT / "dist" / "QA-CHAPTERS.log"


def indented_workflow_block(value: str) -> str:
    return "\n".join(("      " + line) if line else "" for line in value.splitlines()) + "\n"


try:
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
        print(f"Application : {operation['label']} -> {operation['path']}")
        path = ROOT / operation["path"]
        text = path.read_text(encoding="utf-8")
        old = operation["old"]
        new = operation["new"]
        count = text.count(old)

        if count == 0 and operation["label"] == "jalon M4":
            old = """## M4 — Livre III : Production des contenus et assets

- [ ] Préproduction et direction artistique.
- [ ] Êtres vivants, objets et environnements.
- [ ] Animation, audio, VFX, UI et UX.
- [ ] Automatisation et validation artistique.
"""
            new = """## M4 — Livre III : Production des contenus et assets

- [x] Chapitre 1 — Préproduction et cahier des charges artistique.
- [ ] Préproduction et direction artistique — 1 chapitre sur 5.
- [ ] Êtres vivants, objets et environnements.
- [ ] Animation, audio, VFX, UI et UX.
- [ ] Automatisation et validation artistique.

**Statut M4 : en cours — 1 chapitre rédigé, repéré et audité sur 30.**
"""
            count = text.count(old)

        if count == 0 and operation["label"] == "restore workflow hook":
            old = indented_workflow_block(old)
            new = indented_workflow_block(new)
            count = text.count(old)

        if count != 1:
            raise RuntimeError(
                f"{operation['label']}: attendu une occurrence, trouvé {count} dans {operation['path']}"
            )
        path.write_text(
            text.replace(old, new, 1),
            encoding="utf-8",
            newline="\n",
        )

    for path in CHUNKS:
        path.unlink(missing_ok=True)
    Path(__file__).unlink(missing_ok=True)

    print("Chapitre 1 du Livre III, audit, preuve et gouvernance matérialisés.")
except Exception:
    DIAGNOSTIC.parent.mkdir(parents=True, exist_ok=True)
    DIAGNOSTIC.write_text(traceback.format_exc(), encoding="utf-8")
    raise
