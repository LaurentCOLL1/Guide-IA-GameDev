from __future__ import annotations
import base64, gzip, hashlib, json, os
from pathlib import Path

EXPECTED_PACKAGE_SHA256 = "c51301f26e4647cc68b2a6ac6db142748a15dd609b89bac6f8566ba6f16df4b0"
ROOT = Path('.')
parts = sorted((ROOT / '.qa').glob('ch19-package-*.txt'))
if not parts:
    raise RuntimeError('Aucun fragment du paquet chapitre 19.')
encoded = ''.join(path.read_text(encoding='ascii').strip() for path in parts)
actual = hashlib.sha256(encoded.encode('ascii')).hexdigest()
if actual != EXPECTED_PACKAGE_SHA256:
    raise RuntimeError(f'Paquet chapitre 19 corrompu: {actual}')
payload = json.loads(gzip.decompress(base64.b64decode(encoded)).decode('utf-8'))
if payload.get('schema') != 1 or not isinstance(payload.get('files'), dict):
    raise RuntimeError('Schéma du paquet chapitre 19 invalide.')
for relative, entry in payload['files'].items():
    destination = ROOT / relative
    data = base64.b64decode(entry['content_b64'])
    digest = hashlib.sha256(data).hexdigest()
    if digest != entry['sha256']:
        raise RuntimeError(f'Empreinte invalide pour {relative}: {digest}')
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)
proof = ROOT / 'Livre-III/QA/VALIDATION-FINALE-CHAPITRE-19.yaml'
text = proof.read_text(encoding='utf-8')
base = os.environ['BASE_COMMIT']
if text.count('BASE_COMMIT_PLACEHOLDER') != 1:
    raise RuntimeError('Placeholder de base absent ou dupliqué.')
proof.write_text(text.replace('BASE_COMMIT_PLACEHOLDER', base, 1), encoding='utf-8')
print(f"Chapitre 19 matérialisé: {len(payload['files'])} fichiers vérifiés; base: {base}.")
