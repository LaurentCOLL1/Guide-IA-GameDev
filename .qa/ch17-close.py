from __future__ import annotations

import os
from pathlib import Path

PROOF = Path("Livre-III/QA/VALIDATION-FINALE-CHAPITRE-17.yaml")
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
main_ci_old = """  validate-chapters-without-pdf:
    workflow-name: Chapter 17 Finalizer Runner
    execution: embedded-command
    run-id: null
    conclusion: pending"""
main_ci_new = f"""  validate-chapters-without-pdf:
    workflow-name: Chapter 17 Finalizer Runner
    execution: embedded-command
    run-id: {run_id}
    conclusion: success"""
text = replace_once(text, main_ci_old, main_ci_new, "CI chapitres")
context_ci_old = """  validate-usage-contexts:
    workflow-name: Chapter 17 Finalizer Runner
    execution: embedded-command
    run-id: null
    conclusion: pending"""
context_ci_new = f"""  validate-usage-contexts:
    workflow-name: Chapter 17 Finalizer Runner
    execution: embedded-command
    run-id: {run_id}
    conclusion: success"""
text = replace_once(text, context_ci_old, context_ci_new, "CI contextes")
text = replace_once(
    text,
    "    id: null\n    name: chapter-validation-without-pdf\n    digest: null",
    f"    id: {main_artifact_id}\n    name: chapter-validation-without-pdf\n    digest: {main_artifact_digest}",
    "artefact principal",
)
text = replace_once(
    text,
    "    id: null\n    name: usage-context-audit\n    digest: null",
    f"    id: {context_artifact_id}\n    name: usage-context-audit\n    digest: {context_artifact_digest}",
    "artefact contextes",
)
PROOF.write_text(text, encoding="utf-8")

text = CONTINUITY.read_text(encoding="utf-8")
text = replace_once(text, 'version: "3.47.0"', 'version: "3.47.1"', "continuité version")
text = replace_once(
    text,
    'last-updated: "2026-07-23T23:15:00+02:00"',
    'last-updated: "2026-07-23T23:35:00+02:00"',
    "continuité date",
)
journal = f"""### 2026-07-23T23:35:00+02:00 — version 3.47.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-17.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 17 Finalizer Runner`, run `{run_id}`, sur la tête documentaire `{document_head}` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `{main_artifact_id}`, digest `{main_artifact_digest}` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `{context_artifact_id}`, digest `{context_artifact_digest}` ;
- empreinte SHA-256 du chapitre : `127d06c2bc9bbd28c606088e303ea74d447b91c57f8a906c5b8e1da046f58a2d` ;
- empreinte SHA-256 de l’audit : `35eeabea1cdd67cc858a7dcceb4abeab9f436c182fc206177f4b2511864b3d86` ;
- métriques finales : 2 890 lignes, 82 titres, 84 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 18 — LOD, imposteurs et optimisation géométrique, niveau Élevée ;
- aucun maillage, UV, cage, texture bakée, GLB, scène, capture, rapport, benchmark, résultat runtime ou PDF du Livre III produit.

"""
text = replace_once(text, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal, "journal fermeture")
CONTINUITY.write_text(text, encoding="utf-8")
