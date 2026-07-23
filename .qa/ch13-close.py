#!/usr/bin/env python3
import hashlib
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

CHAPTER_PATH = Path("Livre-III/CHAPITRE-13-Architecture-batiments-et-kits-modulaires.md")
AUDIT_PATH = Path("Livre-III/QA/AUDIT-CHAPITRE-13.md")
PROOF_PATH = Path("Livre-III/QA/VALIDATION-FINALE-CHAPITRE-13.yaml")
CONTINUITY_PATH = Path("CONTINUITE-PROJET.md")
EXPECTED_CHAPTER_SHA = "fb9835f62e40f33091db48662ed16bb629002ca396b7e5972ce4767b6b3d54c9"
EXPECTED_AUDIT_SHA = "48defcdb19887a51643c87d3ad2aa02d37792c5d42409d1d9508b511d255af0e"

def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise RuntimeError(f"Remplacement {label} attendu une fois, trouvé {text.count(old)}.")
    return text.replace(old, new, 1)

chapter_sha = hashlib.sha256(CHAPTER_PATH.read_bytes()).hexdigest()
audit_sha = hashlib.sha256(AUDIT_PATH.read_bytes()).hexdigest()
if chapter_sha != EXPECTED_CHAPTER_SHA or audit_sha != EXPECTED_AUDIT_SHA:
    raise RuntimeError("Empreintes chapitre/audit invalides lors de la clôture.")

document_head = os.environ["DOCUMENT_HEAD"]
run_id = os.environ["VALIDATION_RUN_ID"]
main_artifact_id = os.environ["MAIN_ARTIFACT_ID"]
main_artifact_digest = os.environ["MAIN_ARTIFACT_DIGEST"]
context_artifact_id = os.environ["CONTEXT_ARTIFACT_ID"]
context_artifact_digest = os.environ["CONTEXT_ARTIFACT_DIGEST"]
timestamp = datetime.now(ZoneInfo("Europe/Paris")).replace(microsecond=0).isoformat()

proof = PROOF_PATH.read_text(encoding="utf-8")
proof = replace_once(proof, "status: pending_ci", "status: complete", "statut preuve")
proof = replace_once(
    proof,
    "validated-head-commit: null",
    f"validated-head-commit: {document_head}",
    "tête validée",
)
proof = replace_once(proof, "  blocking-errors: null", "  blocking-errors: 0", "erreurs bloquantes")
proof = replace_once(proof, "  warnings: null", "  warnings: 1", "avertissements")
proof = replace_once(
    proof,
    "    run-id: null\n    conclusion: pending",
    f"    run-id: {run_id}\n    conclusion: success",
    "validation chapitres",
)
proof = replace_once(
    proof,
    "    run-id: null\n    conclusion: pending",
    f"    run-id: {run_id}\n    conclusion: success",
    "validation contextes",
)
proof = replace_once(
    proof,
    "  artifact:\n    id: null\n    name: chapter-validation-without-pdf\n    digest: null",
    f"  artifact:\n    id: {main_artifact_id}\n    name: chapter-validation-without-pdf\n    digest: {main_artifact_digest}",
    "artefact principal",
)
proof = replace_once(
    proof,
    "  context-artifact:\n    id: null\n    name: usage-context-audit\n    digest: null",
    f"  context-artifact:\n    id: {context_artifact_id}\n    name: usage-context-audit\n    digest: {context_artifact_digest}",
    "artefact contextes",
)
PROOF_PATH.write_text(proof, encoding="utf-8")

continuity = CONTINUITY_PATH.read_text(encoding="utf-8")
continuity = replace_once(continuity, 'version: "3.43.0"', 'version: "3.43.1"', "version continuité clôture")
continuity = replace_once(
    continuity,
    'last-updated: "2026-07-23T14:35:47+02:00"',
    f'last-updated: "{timestamp}"',
    "date continuité clôture",
)
entry = f"""## 27. Journal

### {timestamp} — version 3.43.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-13.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 13 Finalizer Runner`, run `{run_id}`, sur la tête documentaire `{document_head}` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `{main_artifact_id}`, digest `{main_artifact_digest}` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `{context_artifact_id}`, digest `{context_artifact_digest}` ;
- empreinte SHA-256 du chapitre : `{chapter_sha}` ;
- empreinte SHA-256 de l’audit : `{audit_sha}` ;
- métriques finales : 2 381 lignes, 63 titres, 69 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 14 — Terrains, paysages et mondes ouverts, niveau Élevée ;
- aucun module, bâtiment, collision, navigation, occluder, matériau, atlas, LOD, HLOD, GLB, scène Godot, runtime ou PDF du Livre III produits.

"""
continuity = replace_once(continuity, "## 27. Journal\n\n", entry, "journal de clôture")
CONTINUITY_PATH.write_text(continuity, encoding="utf-8")
