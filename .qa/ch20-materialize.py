from __future__ import annotations
import base64, gzip, hashlib, json, os
from pathlib import Path

EXPECTED_PACKAGE_SHA256 = "c46c0c11c1c4da0962fd68b8741d0dcb850737d3a32ad384e416288e6a2005cc"
ROOT = Path(".")
parts = sorted((ROOT / ".qa").glob("ch20-package-*.txt"))
if not parts:
    raise RuntimeError("Aucun fragment du paquet chapitre 20.")
encoded = "".join(path.read_text(encoding="ascii").strip() for path in parts)
actual_package_sha = hashlib.sha256(encoded.encode("ascii")).hexdigest()
if actual_package_sha != EXPECTED_PACKAGE_SHA256:
    raise RuntimeError(f"Paquet chapitre 20 corrompu: {actual_package_sha}")
payload = json.loads(gzip.decompress(base64.b64decode(encoded)).decode("utf-8"))
if payload.get("schema") != 1 or not isinstance(payload.get("files"), dict):
    raise RuntimeError("Schéma du paquet chapitre 20 invalide.")
for relative, entry in payload["files"].items():
    destination = ROOT / relative
    data = base64.b64decode(entry["content_b64"])
    actual = hashlib.sha256(data).hexdigest()
    if actual != entry["sha256"]:
        raise RuntimeError(f"Empreinte invalide pour {relative}: {actual}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)

base_commit = os.environ["BASE_COMMIT"]
proof = ROOT / "Livre-III/QA/VALIDATION-FINALE-CHAPITRE-20.yaml"
proof_text = proof.read_text(encoding="utf-8")
old_base = "validated-base-commit: BASE_COMMIT_PLACEHOLDER"
new_base = f"validated-base-commit: {base_commit}"
if proof_text.count(old_base) != 1:
    raise RuntimeError("Base placeholder de la preuve absente ou dupliquée.")
proof.write_text(proof_text.replace(old_base, new_base, 1), encoding="utf-8")
print(f"Chapitre 20 matérialisé: {len(payload['files'])} fichiers vérifiés; base: {base_commit}.")
