#!/usr/bin/env python3
import base64
import gzip
import hashlib
import json
from pathlib import Path

EXPECTED_PACKAGE_SHA = "2d70d119a36bf61e6cdb6bb38b24abb79adc5cee48806149083ce5393e6fc494"
EXPECTED_CHAPTER_SHA = "fb9835f62e40f33091db48662ed16bb629002ca396b7e5972ce4767b6b3d54c9"
EXPECTED_AUDIT_SHA = "1eaa54f65360d61d2268e6037892b0be671a4f1cdc49957c6f9c31263f17b6dc"

fragment_paths = sorted(Path(".qa").glob("ch13-package-*.txt"))
if len(fragment_paths) != 14:
    raise RuntimeError(
        f"Nombre de fragments invalide : {len(fragment_paths)} au lieu de 14."
    )

encoded = "".join(path.read_text(encoding="utf-8").strip() for path in fragment_paths)
compressed = base64.b64decode(encoded, validate=True)
if hashlib.sha256(compressed).hexdigest() != EXPECTED_PACKAGE_SHA:
    raise RuntimeError("Empreinte du paquet chapitre 13 invalide.")

payload = json.loads(gzip.decompress(compressed).decode("utf-8"))
if payload.get("schema") != 1 or not isinstance(payload.get("files"), dict):
    raise RuntimeError("Schéma du paquet chapitre 13 invalide.")

for raw_path, content in payload["files"].items():
    target = Path(raw_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")

chapter = Path("Livre-III/CHAPITRE-13-Architecture-batiments-et-kits-modulaires.md")
audit = Path("Livre-III/QA/AUDIT-CHAPITRE-13.md")
if hashlib.sha256(chapter.read_bytes()).hexdigest() != EXPECTED_CHAPTER_SHA:
    raise RuntimeError("Chapitre 13 reconstruit avec une empreinte invalide.")
if hashlib.sha256(audit.read_bytes()).hexdigest() != EXPECTED_AUDIT_SHA:
    raise RuntimeError("Audit du chapitre 13 reconstruit avec une empreinte invalide.")
