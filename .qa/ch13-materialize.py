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
    raise RuntimeError(f"Nombre de fragments invalide : {len(fragment_paths)} au lieu de 14.")

parts = [path.read_text(encoding="utf-8").strip() for path in fragment_paths]
if len(parts[12]) == 6263 and len(parts[13]) == 20:
    parts[13] = parts[12][4000:] + parts[13]
    parts[12] = parts[12][:4000]

if len("".join(parts)) % 4 == 3 and parts[-1].endswith("="):
    parts[-1] += "="

lengths = [len(part) for part in parts]
if lengths[:13] != [4000] * 13 or lengths[13] != 2284:
    raise RuntimeError(f"Découpage corrigé invalide : {lengths}")

encoded = "".join(parts)
compressed = base64.b64decode(encoded, validate=True)
actual_package_sha = hashlib.sha256(compressed).hexdigest()
if actual_package_sha != EXPECTED_PACKAGE_SHA:
    raise RuntimeError(
        f"Empreinte du paquet chapitre 13 invalide : {actual_package_sha}."
    )

payload = json.loads(gzip.decompress(compressed).decode("utf-8"))
if payload.get("schema") != 1 or not isinstance(payload.get("files"), dict):
    raise RuntimeError("Schéma du paquet chapitre 13 invalide.")

for raw_path, content in payload["files"].items():
    target = Path(raw_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")

chapter = Path("Livre-III/CHAPITRE-13-Architecture-batiments-et-kits-modulaires.md")
audit = Path("Livre-III/QA/AUDIT-CHAPITRE-13.md")
actual_chapter_sha = hashlib.sha256(chapter.read_bytes()).hexdigest()
actual_audit_sha = hashlib.sha256(audit.read_bytes()).hexdigest()
if actual_chapter_sha != EXPECTED_CHAPTER_SHA:
    raise RuntimeError(
        f"Chapitre 13 reconstruit avec une empreinte invalide : {actual_chapter_sha}."
    )
if actual_audit_sha != EXPECTED_AUDIT_SHA:
    raise RuntimeError(
        f"Audit du chapitre 13 reconstruit avec une empreinte invalide : {actual_audit_sha}."
    )

Path(".qa/ch13-diagnostic.json").unlink(missing_ok=True)
