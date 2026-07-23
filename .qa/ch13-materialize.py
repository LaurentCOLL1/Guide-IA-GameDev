#!/usr/bin/env python3
import base64
import gzip
import hashlib
import json
from pathlib import Path

EXPECTED_PACKAGE_SHA = "2d70d119a36bf61e6cdb6bb38b24abb79adc5cee48806149083ce5393e6fc494"
EXPECTED_CHAPTER_SHA = "fb9835f62e40f33091db48662ed16bb629002ca396b7e5972ce4767b6b3d54c9"
EXPECTED_AUDIT_SHA = "1eaa54f65360d61d2268e6037892b0be671a4f1cdc49957c6f9c31263f17b6dc"
BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

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
prefix_hash = hashlib.sha256()
prefix_hash.update(prefix_bytes)
recovered_tail = None
recovered_position = None
recovered_character = None
recovered_tail_bytes = None

for position in range(len(corrupted_tail) + 1):
    before = corrupted_tail[:position]
    after = corrupted_tail[position:]
    for character in BASE64_ALPHABET:
        candidate_tail = before + character + after
        try:
            candidate_tail_bytes = base64.b64decode(candidate_tail, validate=True)
        except Exception:
            continue
        candidate_hash = prefix_hash.copy()
        candidate_hash.update(candidate_tail_bytes)
        if candidate_hash.hexdigest() == EXPECTED_PACKAGE_SHA:
            recovered_tail = candidate_tail
            recovered_position = position
            recovered_character = character
            recovered_tail_bytes = candidate_tail_bytes
            break
    if recovered_tail is not None:
        break

if recovered_tail is None or recovered_tail_bytes is None:
    raise RuntimeError("Aucune insertion unique ne reconstitue l’empreinte du paquet chapitre 13.")

compressed = prefix_bytes + recovered_tail_bytes
if hashlib.sha256(compressed).hexdigest() != EXPECTED_PACKAGE_SHA:
    raise RuntimeError("Empreinte finale du paquet incohérente après récupération.")

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
    raise RuntimeError(f"Empreinte du chapitre 13 invalide : {actual_chapter_sha}.")
if actual_audit_sha != EXPECTED_AUDIT_SHA:
    raise RuntimeError(f"Empreinte de l’audit du chapitre 13 invalide : {actual_audit_sha}.")

Path(".qa/ch13-diagnostic.json").unlink(missing_ok=True)
print(
    "Caractère Base64 restauré avec preuve cryptographique : "
    f"position={recovered_position}, caractère={recovered_character}"
)
