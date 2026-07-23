#!/usr/bin/env python3
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import yaml

proof_path = Path("Livre-III/QA/VALIDATION-FINALE-CHAPITRE-10.yaml")
continuity_path = Path("CONTINUITE-PROJET.md")

document_head = os.environ["DOCUMENT_HEAD"]
run_id = int(os.environ["VALIDATION_RUN_ID"])
main_artifact_id = int(os.environ["MAIN_ARTIFACT_ID"])
main_artifact_digest = os.environ["MAIN_ARTIFACT_DIGEST"]
context_artifact_id = int(os.environ["CONTEXT_ARTIFACT_ID"])
context_artifact_digest = os.environ["CONTEXT_ARTIFACT_DIGEST"]
closed_at = datetime.now(ZoneInfo("Europe/Paris")).replace(microsecond=0).isoformat()

proof = yaml.safe_load(proof_path.read_text(encoding="utf-8"))
if proof.get("status") != "pending_ci":
    raise RuntimeError("La preuve du chapitre 10 n'est pas en attente de CI.")

proof["status"] = "complete"
proof["validated-head-commit"] = document_head
proof["ci"]["validate-chapters-without-pdf"]["run-id"] = run_id
proof["ci"]["validate-chapters-without-pdf"]["conclusion"] = "success"
proof["ci"]["validate-usage-contexts"]["run-id"] = run_id
proof["ci"]["validate-usage-contexts"]["conclusion"] = "success"
proof["ci"]["artifact"]["id"] = main_artifact_id
proof["ci"]["artifact"]["digest"] = main_artifact_digest
proof["ci"]["context-artifact"]["id"] = context_artifact_id
proof["ci"]["context-artifact"]["digest"] = context_artifact_digest
proof["evidence-closure"]["commit"] = None
proof["evidence-closure"]["conclusion"] = "pending"

proof_path.write_text(
    yaml.safe_dump(proof, allow_unicode=True, sort_keys=False, width=120),
    encoding="utf-8",
)

continuity = continuity_path.read_text(encoding="utf-8")
replacements = [
    ('version: "3.40.0"', 'version: "3.40.1"'),
    ('last-updated: "2026-07-23T10:56:17+02:00"', f'last-updated: "{closed_at}"'),
]
for old, new in replacements:
    if old not in continuity:
        raise RuntimeError(f"Motif de continuité introuvable: {old}")
    continuity = continuity.replace(old, new, 1)

journal = f"""### {closed_at} — version 3.40.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-10.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 10 Finalizer Runner`, run `{run_id}`, sur la tête documentaire `{document_head}` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `{main_artifact_id}`, digest `{main_artifact_digest}` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `{context_artifact_id}`, digest `{context_artifact_digest}` ;
- empreinte SHA-256 du chapitre : `a39df80e5f6a37d9290f87464f02b5804d0193b262db3c6209560cc10e3e375c` ;
- empreinte SHA-256 de l’audit : `cf9a9fa649b59b07c7a70b1193fa1340291cbf9a18ce6b02e268bdc88e082a7e` ;
- métriques finales : 1 978 lignes, 49 titres, 52 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 11 — Vêtements, armures et accessoires, niveau Élevée ;
- aucune tête, texture, matériau, œil, dentition, solution capillaire, blendshape, export GLB, scène Godot, runtime ou PDF du Livre III produits.

"""

marker = "## 27. Journal\n\n"
if marker not in continuity:
    raise RuntimeError("Section Journal introuvable dans la continuité.")
continuity = continuity.replace(marker, marker + journal, 1)
continuity_path.write_text(continuity, encoding="utf-8")

print("Chapter 10 evidence closed.")
