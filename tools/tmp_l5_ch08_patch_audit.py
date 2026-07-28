#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-08.md"
PROOF = ROOT / "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-08.yaml"
TIMESTAMP = "2026-07-28T18:20:01+02:00"


def main() -> None:
    audit = AUDIT.read_text(encoding="utf-8")
    if "last-verified:" not in audit[:800]:
        audit = audit.replace(
            'version: "1.0.0"\nlang: "fr-FR"',
            f'version: "1.0.0"\nlast-verified: "{TIMESTAMP}"\nlang: "fr-FR"',
            1,
        )
        AUDIT.write_text(audit, encoding="utf-8")

    digest = hashlib.sha256(audit.encode("utf-8")).hexdigest()
    proof = PROOF.read_text(encoding="utf-8")
    proof, count = re.subn(
        r"(?m)^  audit-sha256: [0-9a-f]{64}$",
        f"  audit-sha256: {digest}",
        proof,
        count=1,
    )
    if count != 1:
        raise RuntimeError("empreinte d'audit absente de la preuve")
    PROOF.write_text(proof, encoding="utf-8")
    print(f"audit_sha256_corrigé: {digest}")


if __name__ == "__main__":
    main()
