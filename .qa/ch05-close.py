from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

EXPECTED = {
    "document_head": "ea8f6a6b9c6cd66b9c3a7922d801274e2405f5e7",
    "context_run_id": 29961125128,
    "context_artifact_id": 8545999556,
    "context_artifact_digest": "f701349af7c1e7694d736925e30153a6419b4f32fcf1656d2f3f601b13825d84",
    "chapter_sha256": "652cdf06964e9354e310fdbb152f9e34dff1f4062b3af313b976901d3ec9d4ec",
    "audit_sha256": "b2a7782ead143c01ef1fe4e040365bb1cd4cfeab982e570ea09ac75bedd3ef1f",
    "conclusion": "success",
}

result_path = Path(".qa/ch05-context-result.json")
result = json.loads(result_path.read_text(encoding="utf-8"))
if result != EXPECTED:
    raise RuntimeError("Les coordonnées de preuve ne correspondent pas au résultat approuvé.")

proof_path = Path("Livre-III/QA/VALIDATION-FINALE-CHAPITRE-05.yaml")
proof = yaml.safe_load(proof_path.read_text(encoding="utf-8"))
proof["status"] = "complete"
proof["validated-head-commit"] = EXPECTED["document_head"]
proof["results"].update(
    {
        "blocking-errors": 0,
        "warnings": 1,
        "significant-code-and-data-blocks": 26,
        "duplicate-headings": 0,
        "duplicate-blocks": 0,
        "duplicate-paragraphs": 0,
    }
)
proof["integrity"]["chapter-sha256"] = EXPECTED["chapter_sha256"]
proof["integrity"]["audit-sha256"] = EXPECTED["audit_sha256"]
proof["ci"]["validate-chapters-without-pdf"] = {
    "run-id": 29960812166,
    "conclusion": "success",
}
proof["ci"]["validate-usage-contexts"] = {
    "run-id": EXPECTED["context_run_id"],
    "conclusion": "success",
}
proof["ci"]["artifact"] = {
    "id": 8545871720,
    "name": "chapter-validation-without-pdf",
    "digest": "b4ae05177e0fc97a7d79cac93c7610046a84db483b0bd8a134032dad9c13083f",
}
proof["ci"]["context-artifact"] = {
    "id": EXPECTED["context_artifact_id"],
    "name": "usage-context-audit",
    "digest": EXPECTED["context_artifact_digest"],
}
proof["evidence-closure"] = {"commit": None, "conclusion": "pending"}
proof_path.write_text(
    yaml.safe_dump(proof, sort_keys=False, allow_unicode=True, width=120),
    encoding="utf-8",
)

timestamp = datetime.now(ZoneInfo("Europe/Paris")).isoformat(timespec="seconds")
continuity_path = Path("CONTINUITE-PROJET.md")
continuity = continuity_path.read_text(encoding="utf-8")
if continuity.count('version: "3.35.0"') != 1:
    raise RuntimeError("La continuité 3.35.0 est attendue.")
continuity = continuity.replace('version: "3.35.0"', 'version: "3.35.1"', 1)
continuity = re.sub(
    r'last-updated: "[^"]+"',
    f'last-updated: "{timestamp}"',
    continuity,
    count=1,
)
journal = f"""### {timestamp} — version 3.35.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-05.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validation documentaire réussie au run `29960812166` sur la tête `{EXPECTED['document_head']}` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8545871720`, digest `b4ae05177e0fc97a7d79cac93c7610046a84db483b0bd8a134032dad9c13083f` ;
- validation des contextes réussie au run `{EXPECTED['context_run_id']}` sur la même tête documentaire ;
- artefact `usage-context-audit` enregistré sous l’identifiant `{EXPECTED['context_artifact_id']}`, digest `{EXPECTED['context_artifact_digest']}` ;
- empreinte SHA-256 du chapitre : `{EXPECTED['chapter_sha256']}` ;
- empreinte SHA-256 de l’audit : `{EXPECTED['audit_sha256']}` ;
- métriques finales : 1 555 lignes, 63 titres, 26 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 6 — Création des humains, niveau Élevée ;
- aucun registre réel, contrat, consentement, runtime ou PDF du Livre III produits.

"""
marker = "## 27. Journal\n\n"
if continuity.count(marker) != 1:
    raise RuntimeError("Le journal de continuité est introuvable.")
continuity_path.write_text(
    continuity.replace(marker, marker + journal, 1),
    encoding="utf-8",
)

for path in (
    Path(".qa/ch05-context-result.json"),
    Path(".qa/ch05-close-trigger.txt"),
):
    path.unlink(missing_ok=True)

print("CH05_EVIDENCE_CLOSED")
