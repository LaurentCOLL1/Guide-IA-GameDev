from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

EXPECTED = {
    "document_head": "12f949fcf53f53eaafb774b5d86b0d706b228191",
    "chapter_run_id": 29965382843,
    "chapter_artifact_id": 8547618141,
    "chapter_artifact_digest": "51ba9423ef5f80744ac63ee8d9a0ce880c058d24fe6f81bf52f02bcf14b7dd03",
    "context_run_id": 29965382828,
    "context_artifact_id": 8547616966,
    "context_artifact_digest": "5b4e2105ae83c656c5bcc0e08b797c9260da1a62ffc4f212bed08121403d178a",
    "chapter_sha256": "199af753e3c11117af44b8e8dac1911955654d734d5a64375b86af4238dcebeb",
    "audit_sha256": "13106867a157ad14d5ebcf2fae09263ccce2d039813a4bc856a23ace6bcbbd16",
}

result_path = Path(".qa/ch06-context-result.json")
result = json.loads(result_path.read_text(encoding="utf-8"))
expected_result = {
    "document_head": EXPECTED["document_head"],
    "context_run_id": EXPECTED["context_run_id"],
    "context_artifact_id": EXPECTED["context_artifact_id"],
    "context_artifact_digest": EXPECTED["context_artifact_digest"],
    "chapter_sha256": EXPECTED["chapter_sha256"],
    "audit_sha256": EXPECTED["audit_sha256"],
    "conclusion": "success",
}
if result != expected_result:
    raise RuntimeError("Les coordonnées de contextes ne correspondent pas au run approuvé.")

proof_path = Path("Livre-III/QA/VALIDATION-FINALE-CHAPITRE-06.yaml")
proof = yaml.safe_load(proof_path.read_text(encoding="utf-8"))
if proof.get("status") != "pending_ci":
    raise RuntimeError(f"Statut de preuve inattendu : {proof.get('status')}")
proof["status"] = "complete"
proof["validated-head-commit"] = EXPECTED["document_head"]
proof["results"].update({
    "blocking-errors": 0,
    "warnings": 1,
    "significant-code-and-data-blocks": 26,
    "duplicate-headings": 0,
    "duplicate-blocks": 0,
    "duplicate-paragraphs": 0,
})
proof["integrity"]["chapter-sha256"] = EXPECTED["chapter_sha256"]
proof["integrity"]["audit-sha256"] = EXPECTED["audit_sha256"]
proof["ci"]["validate-chapters-without-pdf"] = {
    "run-id": EXPECTED["chapter_run_id"],
    "conclusion": "success",
}
proof["ci"]["validate-usage-contexts"] = {
    "run-id": EXPECTED["context_run_id"],
    "conclusion": "success",
}
proof["ci"]["artifact"] = {
    "id": EXPECTED["chapter_artifact_id"],
    "name": "chapter-validation-without-pdf",
    "digest": EXPECTED["chapter_artifact_digest"],
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
if continuity.count('version: "3.36.0"') != 1:
    raise RuntimeError("La continuité 3.36.0 est attendue exactement une fois.")
continuity = continuity.replace('version: "3.36.0"', 'version: "3.36.1"', 1)
continuity = re.sub(
    r'last-updated: "[^"]+"',
    f'last-updated: "{timestamp}"',
    continuity,
    count=1,
)
journal = f'''### {timestamp} — version 3.36.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-06.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validation documentaire réussie au run `{EXPECTED["chapter_run_id"]}` sur la tête `{EXPECTED["document_head"]}` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `{EXPECTED["chapter_artifact_id"]}`, digest `{EXPECTED["chapter_artifact_digest"]}` ;
- validation des contextes réussie au run `{EXPECTED["context_run_id"]}` sur la même tête documentaire ;
- artefact `usage-context-audit` enregistré sous l’identifiant `{EXPECTED["context_artifact_id"]}`, digest `{EXPECTED["context_artifact_digest"]}` ;
- empreinte SHA-256 du chapitre : `{EXPECTED["chapter_sha256"]}` ;
- empreinte SHA-256 de l’audit : `{EXPECTED["audit_sha256"]}` ;
- métriques finales : 1 755 lignes, 68 titres, 26 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 7 — Création des humanoïdes, niveau Élevée ;
- aucun maillage humain, rig, animation, export GLB, scène Godot, runtime ou PDF du Livre III produits.

'''
marker = "## 27. Journal\n\n"
if continuity.count(marker) != 1:
    raise RuntimeError("Le marqueur du journal de continuité est introuvable ou dupliqué.")
continuity_path.write_text(
    continuity.replace(marker, marker + journal, 1),
    encoding="utf-8",
)

result_path.unlink()
print(timestamp)
