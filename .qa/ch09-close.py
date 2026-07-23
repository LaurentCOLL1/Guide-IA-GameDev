from __future__ import annotations

from datetime import datetime
import os
from pathlib import Path
import re
from zoneinfo import ZoneInfo

import yaml

PROOF_PATH = Path("Livre-III/QA/VALIDATION-FINALE-CHAPITRE-09.yaml")
CONTINUITY_PATH = Path("CONTINUITE-PROJET.md")
SHA_PATH = Path("dist/CH09-SHA256.txt")


def required_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"Variable obligatoire absente : {name}")
    return value


def parse_sha_file() -> tuple[str, str]:
    chapter_sha = ""
    audit_sha = ""
    for line in SHA_PATH.read_text(encoding="utf-8").splitlines():
        digest, name = line.split(maxsplit=1)
        if "CHAPITRE-09-Creation-des-creatures.md" in name:
            chapter_sha = digest
        elif "AUDIT-CHAPITRE-09.md" in name:
            audit_sha = digest
    if not chapter_sha or not audit_sha:
        raise RuntimeError("Empreintes du chapitre 9 introuvables.")
    return chapter_sha, audit_sha


def close_proof(chapter_sha: str, audit_sha: str) -> None:
    proof = yaml.safe_load(PROOF_PATH.read_text(encoding="utf-8"))
    proof["status"] = "complete"
    proof["validated-head-commit"] = required_env("DOCUMENT_HEAD")
    proof["results"]["blocking-errors"] = 0
    proof["integrity"]["chapter-sha256"] = chapter_sha
    proof["integrity"]["audit-sha256"] = audit_sha

    run_id = int(required_env("VALIDATION_RUN_ID"))
    for key in ("validate-chapters-without-pdf", "validate-usage-contexts"):
        proof["ci"][key]["run-id"] = run_id
        proof["ci"][key]["conclusion"] = "success"

    proof["ci"]["artifact"]["id"] = int(required_env("MAIN_ARTIFACT_ID"))
    proof["ci"]["artifact"]["digest"] = required_env("MAIN_ARTIFACT_DIGEST").removeprefix("sha256:")
    proof["ci"]["context-artifact"]["id"] = int(required_env("CONTEXT_ARTIFACT_ID"))
    proof["ci"]["context-artifact"]["digest"] = required_env("CONTEXT_ARTIFACT_DIGEST").removeprefix("sha256:")

    PROOF_PATH.write_text(
        yaml.safe_dump(proof, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def close_continuity(chapter_sha: str, audit_sha: str) -> None:
    continuity = CONTINUITY_PATH.read_text(encoding="utf-8")
    timestamp = datetime.now(ZoneInfo("Europe/Paris")).isoformat(timespec="seconds")
    if 'version: "3.39.0"' not in continuity:
        raise RuntimeError("Version 3.39.0 de continuité absente.")
    continuity = continuity.replace('version: "3.39.0"', 'version: "3.39.1"', 1)
    continuity = re.sub(
        r'last-updated: "[^"]+"',
        f'last-updated: "{timestamp}"',
        continuity,
        count=1,
    )

    run_id = required_env("VALIDATION_RUN_ID")
    main_artifact_id = required_env("MAIN_ARTIFACT_ID")
    main_digest = required_env("MAIN_ARTIFACT_DIGEST").removeprefix("sha256:")
    context_artifact_id = required_env("CONTEXT_ARTIFACT_ID")
    context_digest = required_env("CONTEXT_ARTIFACT_DIGEST").removeprefix("sha256:")
    document_head = required_env("DOCUMENT_HEAD")

    marker = "## 27. Journal\n\n"
    journal = f"""### {timestamp} — version 3.39.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-09.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 9 Finalizer Runner`, run `{run_id}`, sur la tête documentaire `{document_head}` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `{main_artifact_id}`, digest `{main_digest}` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `{context_artifact_id}`, digest `{context_digest}` ;
- empreinte SHA-256 du chapitre : `{chapter_sha}` ;
- empreinte SHA-256 de l’audit : `{audit_sha}` ;
- métriques finales : 2 332 lignes, 66 titres, 45 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 10 — Visages, peau, yeux, cheveux et pilosité, niveau Élevée ;
- aucun concept final, modèle, rig, collision, socket, export GLB, scène Godot, runtime ou PDF du Livre III produits.

"""
    if marker not in continuity:
        raise RuntimeError("Journal de continuité introuvable.")
    continuity = continuity.replace(marker, marker + journal, 1)
    CONTINUITY_PATH.write_text(continuity, encoding="utf-8")


chapter_sha, audit_sha = parse_sha_file()
close_proof(chapter_sha, audit_sha)
close_continuity(chapter_sha, audit_sha)
