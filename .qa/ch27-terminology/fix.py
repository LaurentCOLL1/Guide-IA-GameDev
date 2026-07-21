#!/usr/bin/env python3
from pathlib import Path
import re

STAMP = "2026-07-22T01:40:00+02:00"
DATE = "2026-07-22"
CONTINUITY = Path("CONTINUITE-PROJET.md")
VALIDATOR = Path("tools/validate_chapters.py")

CHAPTERS = [
    {
        "number": 22,
        "path": Path("Livre-II/CHAPITRE-22-Monde-vivant-et-simulation-ecologique.md"),
        "audit": Path("Livre-II/QA/AUDIT-CHAPITRE-22.md"),
        "proof": Path("Livre-II/QA/VALIDATION-FINALE-CHAPITRE-22.yaml"),
        "old_version": "1.0.3",
        "new_version": "1.0.4",
        "old_audit_version": "1.0.3",
        "new_audit_version": "1.0.4",
    },
    {
        "number": 23,
        "path": Path("Livre-II/CHAPITRE-23-Politique-factions-et-justice.md"),
        "audit": Path("Livre-II/QA/AUDIT-CHAPITRE-23.md"),
        "proof": Path("Livre-II/QA/VALIDATION-FINALE-CHAPITRE-23.yaml"),
        "old_version": "1.0.2",
        "new_version": "1.0.3",
        "old_audit_version": "1.0.2",
        "new_audit_version": "1.0.3",
    },
    {
        "number": 27,
        "path": Path("Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md"),
        "audit": Path("Livre-II/QA/AUDIT-CHAPITRE-27.md"),
        "proof": Path("Livre-II/QA/VALIDATION-FINALE-CHAPITRE-27.yaml"),
        "old_version": "1.0.0",
        "new_version": "1.0.1",
        "old_audit_version": "1.0.1",
        "new_audit_version": "1.0.2",
    },
]

FORBIDDEN_TERMINOLOGY = {
    "durée murale": "durée réelle (durée de l’horloge système)",
    "temps mural": "durée réelle (durée de l’horloge système)",
    "temps mur": "durée réelle (durée de l’horloge système)",
    "temps horloge": "horloge système",
}


def sub_once(text: str, pattern: str, replacement: str, label: str, flags: int = 0) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return updated


def normalize_terms(text: str) -> tuple[str, int]:
    total = 0
    for forbidden, replacement in FORBIDDEN_TERMINOLOGY.items():
        pattern = rf"(?<!\w){re.escape(forbidden)}(?!\w)"
        text, count = re.subn(pattern, replacement, text, flags=re.IGNORECASE)
        total += count
    return text, total


def assert_terms_absent(text: str, label: str) -> None:
    for forbidden in FORBIDDEN_TERMINOLOGY:
        pattern = rf"(?<!\w){re.escape(forbidden)}(?!\w)"
        if re.search(pattern, text, flags=re.IGNORECASE):
            raise RuntimeError(f"Forbidden terminology remains in {label}: {forbidden}")


def reset_proof(path: Path, old_version: str, new_version: str) -> None:
    proof = path.read_text(encoding="utf-8")
    proof = sub_once(proof, r'^status: complete$', 'status: pending', f"{path} status", re.M)
    proof = sub_once(proof, r"^validation-date: '.+'$", f"validation-date: '{DATE}'", f"{path} date", re.M)
    proof = sub_once(proof, rf'^  version: {re.escape(old_version)}$', f'  version: {new_version}', f"{path} version", re.M)
    proof = sub_once(proof, r'^  blocking-errors: .+$', '  blocking-errors: pending', f"{path} errors", re.M)
    proof = sub_once(proof, r'^  warnings: .+$', '  warnings: pending', f"{path} warnings", re.M)
    proof = sub_once(
        proof,
        r'(  validate-chapters-without-pdf:\n)    run-id: .+\n    conclusion: .+',
        r'\1    run-id: pending\n    conclusion: pending',
        f"{path} chapter workflow",
    )
    proof = sub_once(
        proof,
        r'(  validate-usage-contexts:\n)    run-id: .+\n    conclusion: .+',
        r'\1    run-id: pending\n    conclusion: pending',
        f"{path} context workflow",
    )
    proof = sub_once(
        proof,
        r'(  artifact:\n)    id: .+\n    name: chapter-validation-without-pdf\n    digest: .+',
        r'\1    id: pending\n    name: chapter-validation-without-pdf\n    digest: pending',
        f"{path} artifact",
    )
    proof = sub_once(
        proof,
        r'(evidence-closure:\n)  commit: .+\n  conclusion: .+',
        r'\1  commit: pending\n  conclusion: pending',
        f"{path} closure",
    )
    path.write_text(proof, encoding="utf-8")


replacement_counts: dict[int, int] = {}
for item in CHAPTERS:
    number = item["number"]
    old_version = item["old_version"]
    new_version = item["new_version"]
    old_audit_version = item["old_audit_version"]
    new_audit_version = item["new_audit_version"]

    chapter = item["path"].read_text(encoding="utf-8")
    chapter = sub_once(
        chapter,
        rf'^version: "{re.escape(old_version)}"$',
        f'version: "{new_version}"',
        f"chapter {number} version",
        re.M,
    )
    chapter = sub_once(chapter, r'^last-verified: ".+"$', f'last-verified: "{STAMP}"', f"chapter {number} verified", re.M)
    chapter = sub_once(chapter, r'^audit-date: ".+"$', f'audit-date: "{STAMP}"', f"chapter {number} audit date", re.M)

    if number == 27:
        chapter = chapter.replace(
            "Le harness ne saute aucun tick, n’en ajoute aucun et n’attend aucune durée murale.",
            "Le harness ne saute aucun tick, n’en ajoute aucun et ne dépend d’aucune durée réelle (durée de l’horloge système).",
        )
        chapter = chapter.replace(
            "Le temps mur, la mémoire et le rendu exigent des benchmarks séparés sur la configuration de référence.",
            "La durée réelle (durée de l’horloge système), la mémoire et le rendu exigent des benchmarks séparés sur la configuration de référence.",
        )
        chapter = chapter.replace(
            "Le temps horloge et un délai réel introduisent une dépendance externe sans rapport avec la règle métier.",
            "L’horloge système et une attente réelle introduisent une dépendance externe sans rapport avec la règle métier.",
        )
        chapter = chapter.replace(
            "Le test contrôle exactement l’état initial et l’avancement de l’horloge logique, sans attendre de durée murale.",
            "Le test contrôle exactement l’état initial et l’avancement de l’horloge logique, sans dépendre d’une durée réelle (durée de l’horloge système).",
        )

    chapter, count = normalize_terms(chapter)
    replacement_counts[number] = count
    assert_terms_absent(chapter, f"chapter {number}")
    item["path"].write_text(chapter, encoding="utf-8")

    audit = item["audit"].read_text(encoding="utf-8")
    audit = sub_once(
        audit,
        rf'^version: "{re.escape(old_audit_version)}"$',
        f'version: "{new_audit_version}"',
        f"audit {number} version",
        re.M,
    )
    audit = sub_once(
        audit,
        rf'^chapter-version: "{re.escape(old_version)}"$',
        f'chapter-version: "{new_version}"',
        f"audit {number} chapter version",
        re.M,
    )
    audit = sub_once(audit, r'^audit-date: ".+"$', f'audit-date: "{STAMP}"', f"audit {number} date", re.M)
    audit = sub_once(audit, r'^last-verified: ".+"$', f'last-verified: "{STAMP}"', f"audit {number} verified", re.M)
    decision_match = re.search(r'^## \d+\. Décision$', audit, flags=re.M)
    if decision_match is None:
        raise RuntimeError(f"audit {number}: decision heading not found")
    note = (
        "## Correction terminologique du 22 juillet 2026\n\n"
        "Les calques anglais relatifs à `wall-clock time` ou `wall-clock duration` ont été remplacés par "
        "`durée réelle (durée de l’horloge système)` ; `horloge système` désigne la source temporelle réelle. "
        "Le validateur documentaire refuse désormais les anciennes formulations.\n\n"
    )
    audit = audit[:decision_match.start()] + note + audit[decision_match.start():]
    item["audit"].write_text(audit, encoding="utf-8")

    reset_proof(item["proof"], old_version, new_version)

continuity = CONTINUITY.read_text(encoding="utf-8")
continuity = sub_once(continuity, r'^version: "3\.27\.0"$', 'version: "3.27.1"', "continuity version", re.M)
continuity = sub_once(continuity, r'^last-updated: ".+"$', f'last-updated: "{STAMP}"', "continuity timestamp", re.M)
for item in CHAPTERS:
    number = item["number"]
    old_version = item["old_version"]
    new_version = item["new_version"]
    continuity = sub_once(
        continuity,
        rf'^- chapitre {number} : version `{re.escape(old_version)}` ;$',
        f'- chapitre {number} : version `{new_version}` ;',
        f"continuity chapter {number} version",
        re.M,
    )
continuity = sub_once(
    continuity,
    r'^- ne pas considérer une couverture élevée comme preuve de qualité ou de correction métier ;$',
    '- ne pas considérer une couverture élevée comme preuve de qualité ou de correction métier ;\n- ne pas employer les calques `durée murale`, `temps mur`, `temps mural` ou `temps horloge` ; utiliser `durée réelle (durée de l’horloge système)` et `horloge système` ;',
    "continuity terminology rule",
    re.M,
)
journal = f'''### {STAMP} — version 3.27.1\n\n- chapitres 22, 23 et 27 corrigés : les calques liés à `wall-clock time` et `wall-clock duration` sont remplacés par `durée réelle (durée de l’horloge système)` ou `horloge système` selon le contexte ;\n- versions portées à `1.0.4`, `1.0.3` et `1.0.1` ; audits portés à `1.0.4`, `1.0.3` et `1.0.2` ;\n- règle terminologique permanente ajoutée au validateur des chapitres ;\n- preuves QA des trois chapitres remises en attente de validation ;\n- aucun test runtime revendiqué et aucun PDF construit.\n\n'''
continuity = sub_once(continuity, r'^## 27\. Journal\n\n', '## 27. Journal\n\n' + journal, "continuity journal", re.M)
CONTINUITY.write_text(continuity, encoding="utf-8")

validator = VALIDATOR.read_text(encoding="utf-8")
if "FORBIDDEN_TERMINOLOGY" not in validator:
    validator = sub_once(
        validator,
        r'^(ERROR_HEADING_RE = .+\n)',
        r'\1FORBIDDEN_TERMINOLOGY = {\n    "durée murale": "durée réelle (durée de l’horloge système)",\n    "temps mural": "durée réelle (durée de l’horloge système)",\n    "temps mur": "durée réelle (durée de l’horloge système)",\n    "temps horloge": "horloge système",\n}\n',
        "validator constants",
        re.M,
    )
    validator = sub_once(
        validator,
        r'(        if any\(marker in text for marker in CONFLICT_MARKERS\):\n            errors\.append\(f"Marqueur de conflit Git détecté : \{rel\}"\)\n)',
        r'\1\n        normalized_text = text.casefold()\n        for forbidden, replacement in FORBIDDEN_TERMINOLOGY.items():\n            pattern = rf"(?<!\\w){re.escape(forbidden)}(?!\\w)"\n            if re.search(pattern, normalized_text):\n                errors.append(\n                    f"Calque terminologique interdit dans {rel} : {forbidden!r}. "\n                    f"Employer {replacement!r}."\n                )\n',
        "validator terminology check",
    )
VALIDATOR.write_text(validator, encoding="utf-8")

if sum(replacement_counts.values()) < 2:
    raise RuntimeError(f"Expected historical terminology replacements, got {replacement_counts}")
print(f"Terminology correction prepared: {replacement_counts}")
