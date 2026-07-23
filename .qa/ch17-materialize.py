from __future__ import annotations
import base64, gzip, hashlib, json
from pathlib import Path

EXPECTED_PACKAGE_SHA256 = "62185242fd9d0c41b4cff6c2439465610491305fd7943785a512a9731ed48dd0"
ROOT = Path(".")
parts = sorted((ROOT / ".qa").glob("ch17-package-*.txt"))
if not parts:
    raise RuntimeError("Aucun fragment du paquet chapitre 17.")
encoded = "".join(path.read_text(encoding="ascii").strip() for path in parts)
actual_package_sha = hashlib.sha256(encoded.encode("ascii")).hexdigest()
if actual_package_sha != EXPECTED_PACKAGE_SHA256:
    raise RuntimeError(f"Paquet chapitre 17 corrompu: {actual_package_sha}")
payload = json.loads(gzip.decompress(base64.b64decode(encoded)).decode("utf-8"))
if payload.get("schema") != 1 or not isinstance(payload.get("files"), dict):
    raise RuntimeError("Schéma du paquet chapitre 17 invalide.")
for relative, entry in payload["files"].items():
    destination = ROOT / relative
    data = base64.b64decode(entry["content_b64"])
    actual = hashlib.sha256(data).hexdigest()
    if actual != entry["sha256"]:
        raise RuntimeError(f"Empreinte invalide pour {relative}: {actual}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)
print(f"Chapitre 17 matérialisé: {len(payload['files'])} fichiers vérifiés.")
