from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path('.')
AUDIT_PATH = ROOT / 'Livre-V/QA/AUDIT-CHAPITRE-18.md'
PROOF_PATH = ROOT / 'Livre-V/QA/VALIDATION-FINALE-CHAPITRE-18.yaml'
OLD = 'Temporary Livre V Chapter 18 Finalizer'
NEW = 'Temporary Livre V Chapter 18 Script Runner'


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: remplacement attendu une fois, trouvé {count}')
    return text.replace(old, new, 1)


audit = AUDIT_PATH.read_text(encoding='utf-8')
audit = replace_once(audit, OLD, NEW, str(AUDIT_PATH))
AUDIT_PATH.write_text(audit, encoding='utf-8')
audit_sha = hashlib.sha256(AUDIT_PATH.read_bytes()).hexdigest()

proof = PROOF_PATH.read_text(encoding='utf-8')
proof = replace_once(proof, OLD, NEW, str(PROOF_PATH))
proof = replace_once(
    proof,
    'audit-sha256: 68ed543591281dc66f57e8977fd7c287314404264bbd73d722289ddac4e91979',
    f'audit-sha256: {audit_sha}',
    str(PROOF_PATH),
)
PROOF_PATH.write_text(proof, encoding='utf-8')
print(f'audit_sha256={audit_sha}')
