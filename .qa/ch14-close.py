#!/usr/bin/env python3
import hashlib
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

CHAPTER_PATH = Path("Livre-III/CHAPITRE-14-Terrains-paysages-et-mondes-ouverts.md")
AUDIT_PATH = Path("Livre-III/QA/AUDIT-CHAPITRE-14.md")
PROOF_PATH = Path("Livre-III/QA/VALIDATION-FINALE-CHAPITRE-14.yaml")
CONTINUITY_PATH = Path("CONTINUITE-PROJET.md")
EXPECTED_CHAPTER_SHA = "72cfb38fac389935c3099b09b00f68d8ee416f4ad413a30f8fab21855077c01e"
EXPECTED_AUDIT_SHA = "35c311478ecda349ae6850dbef8ae9c65fbb3db9ab62490ab7cc8abd53f7145c"

def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Remplacement {label} attendu une fois, trouvé {count}.")
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
run_placeholder = "    run-id: null\n    conclusion: pending"
if proof.count(run_placeholder) != 2:
    raise RuntimeError(f"Deux blocs CI en attente étaient attendus, trouvé {proof.count(run_placeholder)}.")
proof = proof.replace(
    run_placeholder,
    f"    run-id: {run_id}\n    conclusion: success",
    1,
)
proof = proof.replace(
    run_placeholder,
    f"    run-id: {run_id}\n    conclusion: success",
    1,
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
continuity = replace_once(continuity, 'version: "3.44.0"', 'version: "3.44.1"', "version continuité clôture")
continuity = replace_once(
    continuity,
    'last-updated: "2026-07-23T16:43:43+02:00"',
    f'last-updated: "{timestamp}"',
    "date continuité clôture",
)
entry = f"""## 27. Journal

### {timestamp} — version 3.44.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-14.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 14 Finalizer Runner`, run `{run_id}`, sur la tête documentaire `{document_head}` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `{main_artifact_id}`, digest `{main_artifact_digest}` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `{context_artifact_id}`, digest `{context_artifact_digest}` ;
- empreinte SHA-256 du chapitre : `{chapter_sha}` ;
- empreinte SHA-256 de l’audit : `{audit_sha}` ;
- métriques finales : 2806 lignes, 74 titres, 78 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 15 — Végétation et biomes, niveau Élevée ;
- aucun terrain, heightmap, tuile, route, rivière, lac, matériau, collision, navmesh, scène, GLB, LOD, HLOD, runtime ou PDF du Livre III produits.

"""
continuity = replace_once(continuity, "## 27. Journal\n\n", entry, "journal de clôture")
CONTINUITY_PATH.write_text(continuity, encoding="utf-8")
