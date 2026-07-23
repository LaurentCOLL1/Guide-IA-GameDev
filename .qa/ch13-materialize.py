#!/usr/bin/env python3
import base64
import gzip
import hashlib
import json
from pathlib import Path

EXPECTED_CHAPTER_SHA = "fb9835f62e40f33091db48662ed16bb629002ca396b7e5972ce4767b6b3d54c9"
EXPECTED_AUDIT_SHA = "1eaa54f65360d61d2268e6037892b0be671a4f1cdc49957c6f9c31263f17b6dc"
BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
CHAPTER_KEY = "Livre-III/CHAPITRE-13-Architecture-batiments-et-kits-modulaires.md"
AUDIT_KEY = "Livre-III/QA/AUDIT-CHAPITRE-13.md"

fragment_paths = sorted(Path(".qa").glob("ch13-package-*.txt"))
if len(fragment_paths) != 14:
    raise RuntimeError(f"Nombre de fragments invalide : {len(fragment_paths)} au lieu de 14.")

parts = [path.read_text(encoding="utf-8").strip() for path in fragment_paths]
if [len(part) for part in parts[:12]] != [4000] * 12:
    raise RuntimeError("Les douze premiers fragments ne respectent pas le contrat de 4 000 caractères.")
if len(parts[12]) != 6263 or len(parts[13]) != 20:
    raise RuntimeError(f"Forme finale inattendue : {[len(part) for part in parts]}")

prefix_encoded = "".join(parts[:12]) + parts[12][:4000]
corrupted_tail = parts[12][4000:] + parts[13]
if len(prefix_encoded) != 52000 or len(corrupted_tail) != 2283:
    raise RuntimeError("Longueur du préfixe ou de la queue corrompue invalide.")

prefix_bytes = base64.b64decode(prefix_encoded, validate=True)
recovered = None

for position in range(len(corrupted_tail) + 1):
    before = corrupted_tail[:position]
    after = corrupted_tail[position:]
    for character in BASE64_ALPHABET:
        candidate_tail = before + character + after
        try:
            tail_bytes = base64.b64decode(candidate_tail, validate=True)
            compressed = prefix_bytes + tail_bytes
            raw = gzip.decompress(compressed)
            payload = json.loads(raw.decode("utf-8"))
        except Exception:
            continue
        if payload.get("schema") != 1 or not isinstance(payload.get("files"), dict):
            continue
        files = payload["files"]
        chapter = files.get(CHAPTER_KEY)
        audit = files.get(AUDIT_KEY)
        if not isinstance(chapter, str) or not isinstance(audit, str):
            continue
        chapter_sha = hashlib.sha256(chapter.encode("utf-8")).hexdigest()
        audit_sha = hashlib.sha256(audit.encode("utf-8")).hexdigest()
        if chapter_sha == EXPECTED_CHAPTER_SHA and audit_sha == EXPECTED_AUDIT_SHA:
            recovered = {
                "position": position,
                "character": character,
                "compressed": compressed,
                "payload": payload,
                "package_sha": hashlib.sha256(compressed).hexdigest(),
            }
            break
    if recovered is not None:
        break

if recovered is None:
    raise RuntimeError(
        "Aucune insertion unique ne reconstitue un paquet gzip/JSON portant les empreintes exactes du chapitre et de l’audit."
    )

for raw_path, content in recovered["payload"]["files"].items():
    target = Path(raw_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")

chapter_path = Path(CHAPTER_KEY)
audit_path = Path(AUDIT_KEY)
if hashlib.sha256(chapter_path.read_bytes()).hexdigest() != EXPECTED_CHAPTER_SHA:
    raise RuntimeError("Empreinte du chapitre matérialisé invalide.")
if hashlib.sha256(audit_path.read_bytes()).hexdigest() != EXPECTED_AUDIT_SHA:
    raise RuntimeError("Empreinte de l’audit matérialisé invalide.")

Path(".qa/ch13-diagnostic.json").unlink(missing_ok=True)
print(
    "Paquet restauré par les empreintes permanentes : "
    f"position={recovered['position']}, caractère={recovered['character']}, "
    f"sha256={recovered['package_sha']}"
)
