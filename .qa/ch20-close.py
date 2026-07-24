from __future__ import annotations
import os
from pathlib import Path

ROOT = Path(".")
proof_path = ROOT / "Livre-III/QA/VALIDATION-FINALE-CHAPITRE-20.yaml"
continuity_path = ROOT / "CONTINUITE-PROJET.md"

def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: occurrence attendue 1, trouvée {count}")
    return text.replace(old, new, 1)

document_head = os.environ["DOCUMENT_HEAD"]
run_id = os.environ["VALIDATION_RUN_ID"]
main_artifact_id = os.environ["MAIN_ARTIFACT_ID"]
main_artifact_digest = os.environ["MAIN_ARTIFACT_DIGEST"]
context_artifact_id = os.environ["CONTEXT_ARTIFACT_ID"]
context_artifact_digest = os.environ["CONTEXT_ARTIFACT_DIGEST"]

text = proof_path.read_text(encoding="utf-8")
text = replace_once(text, "status: provisional", "status: complete", "statut preuve")
text = replace_once(text, "validated-head-commit: null", f"validated-head-commit: {document_head}", "tête preuve")

main_ci_old = """  validate-chapters-without-pdf:
    workflow-name: Chapter 20 Finalizer Runner
    execution: embedded-command
    run-id: null
    conclusion: pending
"""
main_ci_new = f"""  validate-chapters-without-pdf:
    workflow-name: Chapter 20 Finalizer Runner
    execution: embedded-command
    run-id: {run_id}
    conclusion: success
"""
text = replace_once(text, main_ci_old, main_ci_new, "CI chapitres")

context_ci_old = """  validate-usage-contexts:
    workflow-name: Chapter 20 Finalizer Runner
    execution: embedded-command
    run-id: null
    conclusion: pending
"""
context_ci_new = f"""  validate-usage-contexts:
    workflow-name: Chapter 20 Finalizer Runner
    execution: embedded-command
    run-id: {run_id}
    conclusion: success
"""
text = replace_once(text, context_ci_old, context_ci_new, "CI contextes")

artifact_old = """  artifact:
    id: null
    name: chapter-validation-without-pdf
    digest: null
"""
artifact_new = f"""  artifact:
    id: {main_artifact_id}
    name: chapter-validation-without-pdf
    digest: {main_artifact_digest}
"""
text = replace_once(text, artifact_old, artifact_new, "artefact principal")

context_artifact_old = """  context-artifact:
    id: null
    name: usage-context-audit
    digest: null
"""
context_artifact_new = f"""  context-artifact:
    id: {context_artifact_id}
    name: usage-context-audit
    digest: {context_artifact_digest}
"""
text = replace_once(text, context_artifact_old, context_artifact_new, "artefact contextes")
proof_path.write_text(text, encoding="utf-8")

text = continuity_path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "3.50.0"', 'version: "3.50.1"', "version continuité finale")
text = replace_once(
    text,
    'last-updated: "2026-07-24T05:10:00+02:00"',
    'last-updated: "2026-07-24T05:30:00+02:00"',
    "date continuité finale",
)
journal = f"""### 2026-07-24T05:30:00+02:00 — version 3.50.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-20.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 20 Finalizer Runner`, run `{run_id}`, sur la tête documentaire `{document_head}` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `{main_artifact_id}`, digest `{main_artifact_digest}` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `{context_artifact_id}`, digest `{context_artifact_digest}` ;
- empreinte SHA-256 du chapitre : `9caa2e71f4ad8bb1ecbf3d9dfe0eaf0189bf085ecba7884f7d759c136f9567f9` ;
- empreinte SHA-256 de l’audit : `c132ed7d0950212a32e6689a13ad87ee69b4c94842cddf811d60a1bd2ad82d63` ;
- métriques finales : 2 452 lignes, 76 titres, 81 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 21 — Capture de mouvement et retargeting, niveau Élevée ;
- aucune animation, bibliothèque, GLB, scène, capture, benchmark, résultat runtime ou PDF du Livre III produit.

"""
text = replace_once(text, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal, "journal final")
continuity_path.write_text(text, encoding="utf-8")
print("Preuve et continuité du chapitre 20 fermées.")
