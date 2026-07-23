from __future__ import annotations

import os
from pathlib import Path

PROOF = Path("Livre-III/QA/VALIDATION-FINALE-CHAPITRE-16.yaml")
CONTINUITY = Path("CONTINUITE-PROJET.md")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: attendu 1 occurrence, trouvé {count}")
    return text.replace(old, new, 1)


document_head = os.environ["DOCUMENT_HEAD"]
run_id = os.environ["VALIDATION_RUN_ID"]
main_artifact_id = os.environ["MAIN_ARTIFACT_ID"]
main_artifact_digest = os.environ["MAIN_ARTIFACT_DIGEST"]
context_artifact_id = os.environ["CONTEXT_ARTIFACT_ID"]
context_artifact_digest = os.environ["CONTEXT_ARTIFACT_DIGEST"]

text = PROOF.read_text(encoding="utf-8")
text = replace_once(text, "status: pending", "status: complete", "preuve statut")
text = replace_once(text, "validated-head-commit: null", f"validated-head-commit: {document_head}", "preuve tête")
text = replace_once(
    text,
    "  validate-chapters-without-pdf:\n    workflow-name: Chapter 16 Finalizer Runner\n    execution: embedded-command\n    run-id: null\n    conclusion: pending",
    f"  validate-chapters-without-pdf:\n    workflow-name: Chapter 16 Finalizer Runner\n    execution: embedded-command\n    run-id: {run_id}\n    conclusion: success",
    "CI chapitres",
)
text = replace_once(
    text,
    "  validate-usage-contexts:\n    workflow-name: Chapter 16 Finalizer Runner\n    execution: embedded-command\n    run-id: null\n    conclusion: pending",
    f"  validate-usage-contexts:\n    workflow-name: Chapter 16 Finalizer Runner\n    execution: embedded-command\n    run-id: {run_id}\n    conclusion: success",
    "CI contextes",
)
text = replace_once(text, "    id: null\n    name: chapter-validation-without-pdf\n    digest: null", f"    id: {main_artifact_id}\n    name: chapter-validation-without-pdf\n    digest: {main_artifact_digest}", "artefact principal")
text = replace_once(text, "    id: null\n    name: usage-context-audit\n    digest: null", f"    id: {context_artifact_id}\n    name: usage-context-audit\n    digest: {context_artifact_digest}", "artefact contextes")
PROOF.write_text(text, encoding="utf-8")

text = CONTINUITY.read_text(encoding="utf-8")
text = replace_once(text, 'version: "3.46.0"', 'version: "3.46.1"', "continuité version")
text = replace_once(text, 'last-updated: "2026-07-23T21:15:00+02:00"', 'last-updated: "2026-07-23T21:35:00+02:00"', "continuité date")
journal = f"""### 2026-07-23T21:35:00+02:00 — version 3.46.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-16.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 16 Finalizer Runner`, run `{run_id}`, sur la tête documentaire `{document_head}` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `{main_artifact_id}`, digest `{main_artifact_digest}` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `{context_artifact_id}`, digest `{context_artifact_digest}` ;
- empreinte SHA-256 du chapitre : `2c5d9182ff27921ee14905e5a516a73a054e3657a6d8e7394347c957044e105b` ;
- empreinte SHA-256 de l’audit : `55eb5d449c8fc79ecbda55ef66b2ed76de1c6a5fa3bf78d87efa3cf218d8d3e8` ;
- métriques finales : 1 654 lignes, 63 titres, 68 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 17 — UV, retopologie et baking, niveau Élevée ;
- aucune texture, matériau, ressource Godot, scène, capture, GLB, preset, benchmark, résultat runtime ou PDF du Livre III produit.

"""
text = replace_once(text, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal, "journal fermeture")
CONTINUITY.write_text(text, encoding="utf-8")
