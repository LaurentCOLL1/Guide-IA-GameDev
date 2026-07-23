from __future__ import annotations

import base64
import gzip
import hashlib
import json
from pathlib import Path

CHAPTER = Path("Livre-III/CHAPITRE-16-Textures-materiaux-et-pipeline-PBR.md")
AUDIT = Path("Livre-III/QA/AUDIT-CHAPITRE-16.md")
EXPECTED_CHAPTER = "2c5d9182ff27921ee14905e5a516a73a054e3657a6d8e7394347c957044e105b"
EXPECTED_AUDIT = "55eb5d449c8fc79ecbda55ef66b2ed76de1c6a5fa3bf78d87efa3cf218d8d3e8"

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load_package() -> dict[str, str]:
    parts = sorted(Path(".qa").glob("ch16-package-*.txt"))
    if not parts:
        raise RuntimeError("Fragments du paquet du chapitre 16 absents.")
    encoded = "".join(path.read_text(encoding="ascii").strip() for path in parts)
    payload = json.loads(gzip.decompress(base64.b64decode(encoded)).decode("utf-8"))
    required = {"chapter", "audit", "governance", "close"}
    if set(payload) != required:
        raise RuntimeError(f"Clés de paquet inattendues: {sorted(payload)}")
    return payload

payload = load_package()
CHAPTER.parent.mkdir(parents=True, exist_ok=True)
AUDIT.parent.mkdir(parents=True, exist_ok=True)
Path(".qa").mkdir(parents=True, exist_ok=True)

CHAPTER.write_text(payload["chapter"], encoding="utf-8")
AUDIT.write_text(payload["audit"], encoding="utf-8")
Path(".qa/ch16-governance.py").write_text(payload["governance"], encoding="utf-8")
Path(".qa/ch16-close.py").write_text(payload["close"], encoding="utf-8")

if sha256(CHAPTER) != EXPECTED_CHAPTER:
    raise RuntimeError("Empreinte du chapitre 16 invalide après matérialisation.")
if sha256(AUDIT) != EXPECTED_AUDIT:
    raise RuntimeError("Empreinte de l'audit du chapitre 16 invalide après matérialisation.")
