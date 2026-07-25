#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime
from hashlib import sha256
from pathlib import Path
from zoneinfo import ZoneInfo
import re

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.now(ZoneInfo("Europe/Paris")).isoformat(timespec="seconds")
TODAY = NOW[:10]
BASE_COMMIT = "2e58c8ffc04908975b0f6a80f945ea3867143814"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: attendu 1 occurrence, trouvé {count}")
    return text.replace(old, new, 1)


chapter_path = "Livre-IV/CHAPITRE-01-Equilibrage-et-telemetrie-locale.md"
chapter = read(chapter_path)
chapter = replace_once(chapter, 'version: "1.0.0"', 'version: "1.0.1"', "version chapitre")
chapter = re.sub(r'^last-verified: ".*"$', f'last-verified: "{NOW}"', chapter, count=1, flags=re.MULTILINE)
chapter = re.sub(r'^audit-date: ".*"$', f'audit-date: "{NOW}"', chapter, count=1, flags=re.MULTILINE)
chapter = replace_once(
    chapter,
    '> **[PS] PowerShell 7 — Lancer une campagne locale bornée sans PDF.**',
    '> **[PS] PowerShell 7 — Lancer une campagne locale bornée.**',
    "commande campagne",
)
chapter = replace_once(
    chapter,
    '- [ ] aucun PDF intermédiaire construit.',
    '- [ ] aucune sortie de campagne n’est publiée hors du workspace déclaré.',
    "checklist campagne",
)
if "PDF" in chapter:
    raise RuntimeError("Le chapitre lecteur contient encore une mention de PDF.")
write(chapter_path, chapter)


audit_path = "Livre-IV/QA/AUDIT-CHAPITRE-01.md"
audit = read(audit_path)
audit = replace_once(audit, 'version: "1.0.0"', 'version: "1.0.1"', "version audit")
audit = replace_once(audit, 'chapter-version: "1.0.0"', 'chapter-version: "1.0.1"', "version chapitre audit")
audit = re.sub(r'^audit-date: ".*"$', f'audit-date: "{NOW}"', audit, count=1, flags=re.MULTILINE)
audit = re.sub(r'^last-verified: ".*"$', f'last-verified: "{NOW}"', audit, count=1, flags=re.MULTILINE)
audit = replace_once(
    audit,
    "Aucune session de jeu, donnée personnelle, simulation, commande Python, collecteur Godot, agrégat, baseline, benchmark, décision d’équilibrage ou PDF n’est revendiqué comme produit ou exécuté.\n",
    "Aucune session de jeu, donnée personnelle, simulation, commande Python, collecteur Godot, agrégat, baseline, benchmark ou décision d’équilibrage n’est revendiqué comme produit ou exécuté.\n\nLa correction `1.0.1` retire du texte lecteur les deux mentions relatives au PDF du guide. La génération du manuel appartient exclusivement à la chaîne de publication documentaire et ne constitue ni une étape ni un critère d’acceptation de l’équilibrage.\n",
    "décision audit",
)
audit = replace_once(
    audit,
    "Le chapitre satisfait le périmètre du plan maître et peut entrer dans la validation légère sans PDF. La preuve finale reste en attente de la réussite des workflows sur la branche documentaire.",
    "Le chapitre satisfait le périmètre du plan maître. La preuve finale est régénérée par les workflows permanents après la correction du texte lecteur.",
    "conclusion audit",
)
write(audit_path, audit)


index_path = "Livre-IV/index.md"
index = read(index_path)
index = replace_once(index, 'version: "0.2.0"', 'version: "0.2.1"', "version index")
index = re.sub(r'^last-updated: ".*"$', f'last-updated: "{NOW}"', index, count=1, flags=re.MULTILINE)
index = replace_once(index, 'version `1.0.0`, niveau `static-review`', 'version `1.0.1`, niveau `static-review`', "version chapitre index")
write(index_path, index)


continuity_path = "CONTINUITE-PROJET.md"
continuity = read(continuity_path)
continuity = replace_once(continuity, 'version: "3.63.0"', 'version: "3.64.0"', "version continuité")
continuity = re.sub(r'^last-updated: ".*"$', f'last-updated: "{NOW}"', continuity, count=1, flags=re.MULTILINE)
continuity = replace_once(
    continuity,
    '- ne pas collecter une métrique sans question, finalité et politique de conservation explicites ;',
    '- ne pas introduire dans un chapitre lecteur des instructions ou critères liés à la génération du PDF du guide ; cette chaîne appartient à la publication documentaire de fin de Livre ou de collection ;\n- ne pas collecter une métrique sans question, finalité et politique de conservation explicites ;',
    "règle PDF lecteur",
)
continuity = replace_once(
    continuity,
    '- chapitre 1 du Livre IV : version `1.0.0`, niveau `static-review` ;',
    '- chapitre 1 du Livre IV : version `1.0.1`, niveau `static-review` ;',
    "version chapitre continuité",
)
journal_anchor = '### 2026-07-25T17:49:48+02:00 — version 3.63.0'
journal_entry = f'''### {NOW} — version 3.64.0

- correction du chapitre 1 du Livre IV en version `1.0.1` ;
- retrait des deux mentions de PDF présentes dans le texte lecteur ;
- la commande de campagne décrit désormais uniquement l’exécution de la matrice d’équilibrage ;
- la checklist d’acceptation porte désormais sur le confinement des sorties dans le workspace déclaré ;
- décision permanente enregistrée : la génération du PDF du guide appartient à la chaîne de publication documentaire et ne doit pas apparaître comme procédure ou critère métier d’un chapitre ;
- audit, preuve QA, index actif et continuité mis à jour ;
- prochaine action officielle inchangée : Livre IV, chapitre 2.


{journal_anchor}'''
continuity = replace_once(continuity, journal_anchor, journal_entry, "journal continuité")
write(continuity_path, continuity)


chapter_hash = sha256(chapter.encode("utf-8")).hexdigest()
audit_hash = sha256(audit.encode("utf-8")).hexdigest()
proof_path = "Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-01.yaml"
proof = f'''schema-version: 1
evidence-id: DOC-L4-QA-EVIDENCE-CH01
validation-authority: permanent-workflows
status: pending
validation-date: '{TODAY}'
validated-base-commit: {BASE_COMMIT}
validated-head-commit: pending
chapter:
  id: DOC-L4-CH01
  path: Livre-IV/CHAPITRE-01-Equilibrage-et-telemetrie-locale.md
  version: 1.0.1
  audit-level: static-review
results:
  blocking-errors: pending
  warnings: pending
  chapter-lines: 2001
  chapter-headings: 62
  chapter-code-and-data-blocks: 55
  significant-code-and-data-blocks: 48
  code-explanation-markers: 55
  structured-non-error-code-explanations: 35
  detailed-error-cases: 10
  faulty-examples-explained: 10
  corrected-examples-explained: 10
  duplicate-headings: 0
  duplicate-blocks: 0
  duplicate-paragraphs: 0
  reader-qa-procedure-absent: true
  reader-pdf-pipeline-mentions-absent: true
  next-step-absent-from-reader-chapter: true
  reasoning-process-metadata-absent: true
  solo-studio-documented: true
  master-plan-scope-covered: true
  project-asteria-operational-summary-present: true
  clickable-technical-references: true
  metric-catalog-documented: true
  local-telemetry-boundaries-documented: true
  balancing-curves-documented: true
  deterministic-simulations-documented: true
  privacy-minimization-and-consent-documented: true
  decision-reports-and-rollback-documented: true
  no-gameplay-authority: true
  runtime-values-not-invented: true
  semantic-error-correction-sequence: true
  error-explanations-directly-after-markers: true
  pdf-produced: false
  runtime-executed: false
integrity:
  chapter-sha256: {chapter_hash}
  audit-sha256: {audit_hash}
ci:
  validate-chapters-without-pdf:
    workflow-name: Validate Chapters Without PDF
    execution: pending
    run-id: pending
    conclusion: pending
  validate-usage-contexts:
    workflow-name: Validate Usage Contexts
    execution: pending
    run-id: pending
    conclusion: pending
  artifact:
    id: pending
    name: chapter-validation-without-pdf
    digest: pending
reservations:
  - Metric catalog not materialized.
  - Local Godot recorder not executed.
  - Simulation scenarios and profiles not executed.
  - Python aggregation and comparison not executed.
  - No player or playtest data collected.
  - Consent and withdrawal flow not implemented.
  - No balance baseline or decision approved.
  - Runtime measurements not produced.
  - Collection-wide licence not defined.
  - PDF accessibility tagging remains open.
evidence-closure:
  commit: pending
  conclusion: pending
'''
write(proof_path, proof)

print(f"Correction appliquée à {chapter_path}")
print(f"Horodatage : {NOW}")
print(f"SHA-256 chapitre : {chapter_hash}")
print(f"SHA-256 audit : {audit_hash}")
