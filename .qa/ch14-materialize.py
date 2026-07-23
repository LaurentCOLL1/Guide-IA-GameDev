#!/usr/bin/env python3
import base64
import gzip
import hashlib
import json
from pathlib import Path

EXPECTED_PACKAGE_SHA = "e5f2ca87437f158be106a489433f7a4ec56db088e827879ee7953a825335d2da"
EXPECTED_FILE_SHAS = {
    "Livre-III/CHAPITRE-14-Terrains-paysages-et-mondes-ouverts.md": "72cfb38fac389935c3099b09b00f68d8ee416f4ad413a30f8fab21855077c01e",
    "Livre-III/QA/AUDIT-CHAPITRE-14.md": "35c311478ecda349ae6850dbef8ae9c65fbb3db9ab62490ab7cc8abd53f7145c",
    "Livre-III/QA/VALIDATION-FINALE-CHAPITRE-14.yaml": "a99990b4accac190f75b7ce1e19bee3b6cc2bd713e374bef6b17efa0d307e1f3",
    ".qa/ch14-governance.py": "a2fec5bb3516bb53e275cc265567566bcf26dbd2fe784e7fdb0b98e3b4677360",
    ".qa/ch14-close.py": "f7866c0d0b2a872f3227d2a1196c48f67a4e4c2e10b907bb14037738222077a3"
}

fragment_paths = sorted(Path(".qa").glob("ch14-package-*.txt"))
if len(fragment_paths) != 14:
    raise RuntimeError(f"Nombre de fragments invalide : {len(fragment_paths)} au lieu de 14.")

lengths = [len(path.read_text(encoding="utf-8").strip()) for path in fragment_paths]
expected_lengths = [4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 2976]
if lengths != expected_lengths:
    raise RuntimeError(f"Longueurs de fragments invalides : {lengths}.")

encoded = "".join(path.read_text(encoding="utf-8").strip() for path in fragment_paths)
compressed = base64.b64decode(encoded, validate=True)
actual_package_sha = hashlib.sha256(compressed).hexdigest()
if actual_package_sha != EXPECTED_PACKAGE_SHA:
    raise RuntimeError(f"Empreinte du paquet invalide : {actual_package_sha}.")

payload = json.loads(gzip.decompress(compressed).decode("utf-8"))
if payload.get("schema") != 1 or not isinstance(payload.get("files"), dict):
    raise RuntimeError("Schéma du paquet chapitre 14 invalide.")

if set(payload["files"]) != set(EXPECTED_FILE_SHAS):
    raise RuntimeError("Liste de fichiers du paquet chapitre 14 invalide.")

for raw_path, content in payload["files"].items():
    actual_sha = hashlib.sha256(content.encode("utf-8")).hexdigest()
    expected_sha = EXPECTED_FILE_SHAS[raw_path]
    if actual_sha != expected_sha:
        raise RuntimeError(f"Empreinte interne invalide pour {raw_path} : {actual_sha}.")
    target = Path(raw_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")

for raw_path, expected_sha in EXPECTED_FILE_SHAS.items():
    actual_sha = hashlib.sha256(Path(raw_path).read_bytes()).hexdigest()
    if actual_sha != expected_sha:
        raise RuntimeError(f"Empreinte matérialisée invalide pour {raw_path} : {actual_sha}.")

print("Paquet chapitre 14 matérialisé et vérifié.")
