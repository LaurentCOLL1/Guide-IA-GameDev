#!/usr/bin/env python3
from pathlib import Path
import re

STAMP = "2026-07-22T01:40:00+02:00"
CHAPTER = Path("Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md")
AUDIT = Path("Livre-II/QA/AUDIT-CHAPITRE-27.md")
PROOF = Path("Livre-II/QA/VALIDATION-FINALE-CHAPITRE-27.yaml")
CONTINUITY = Path("CONTINUITE-PROJET.md")
VALIDATOR = Path("tools/validate_chapters.py")


def sub_once(text: str, pattern: str, replacement: str, label: str, flags: int = 0) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return updated


chapter = CHAPTER.read_text(encoding="utf-8")
chapter = sub_once(chapter, r'^version: "1\.0\.0"$', 'version: "1.0.1"', "chapter version", re.M)
chapter = sub_once(chapter, r'^last-verified: ".+"$', f'last-verified: "{STAMP}"', "chapter last-verified", re.M)
chapter = sub_once(chapter, r'^audit-date: ".+"$', f'audit-date: "{STAMP}"', "chapter audit-date", re.M)
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
normalizations = (
    (r"(?<!\w)durée murale(?!\w)", "durée réelle (durée de l’horloge système)"),
    (r"(?<!\w)temps mural(?!\w)", "durée réelle (durée de l’horloge système)"),
    (r"(?<!\w)temps mur(?!\w)", "durée réelle (durée de l’horloge système)"),
    (r"(?<!\w)temps horloge(?!\w)", "horloge système"),
)
for pattern, replacement in normalizations:
    chapter = re.sub(pattern, replacement, chapter, flags=re.IGNORECASE)
for forbidden in ("durée murale", "temps mur", "temps mural", "temps horloge"):
    if re.search(rf"(?<!\w){re.escape(forbidden)}(?!\w)", chapter, flags=re.IGNORECASE):
        raise RuntimeError(f"Forbidden terminology remains in chapter: {forbidden}")
CHAPTER.write_text(chapter, encoding="utf-8")

audit = AUDIT.read_text(encoding="utf-8")
audit = sub_once(audit, r'^version: "1\.0\.1"$', 'version: "1.0.2"', "audit version", re.M)
audit = sub_once(audit, r'^chapter-version: "1\.0\.0"$', 'chapter-version: "1.0.1"', "audit chapter version", re.M)
audit = sub_once(audit, r'^audit-date: ".+"$', f'audit-date: "{STAMP}"', "audit date", re.M)
audit = sub_once(audit, r'^last-verified: ".+"$', f'last-verified: "{STAMP}"', "audit verified", re.M)
audit = sub_once(
    audit,
    r'^- les codes de sortie non nuls restent bloquants\.$',
    '- les codes de sortie non nuls restent bloquants ;\n- la terminologie emploie `durée réelle (durée de l’horloge système)` pour traduire le concept anglais de wall-clock time ou wall-clock duration, et `horloge système` pour désigner la source temporelle réelle.',
    "audit terminology note",
    re.M,
)
AUDIT.write_text(audit, encoding="utf-8")

proof = PROOF.read_text(encoding="utf-8")
proof = sub_once(proof, r'^status: complete$', 'status: pending', "proof status", re.M)
proof = sub_once(proof, r"^validation-date: '.+'$", "validation-date: '2026-07-22'", "proof date", re.M)
proof = sub_once(proof, r'^  version: 1\.0\.0$', '  version: 1.0.1', "proof chapter version", re.M)
proof = sub_once(proof, r'^  blocking-errors: .+$', '  blocking-errors: pending', "proof errors", re.M)
proof = sub_once(proof, r'^  warnings: .+$', '  warnings: pending', "proof warnings", re.M)
proof = sub_once(proof, r'(  validate-chapters-without-pdf:\n)    run-id: .+\n    conclusion: .+', r'\1    run-id: pending\n    conclusion: pending', "proof chapter workflow")
proof = sub_once(proof, r'(  validate-usage-contexts:\n)    run-id: .+\n    conclusion: .+', r'\1    run-id: pending\n    conclusion: pending', "proof context workflow")
proof = sub_once(proof, r'(  artifact:\n)    id: .+\n    name: chapter-validation-without-pdf\n    digest: .+', r'\1    id: pending\n    name: chapter-validation-without-pdf\n    digest: pending', "proof artifact")
proof = sub_once(proof, r'(evidence-closure:\n)  commit: .+\n  conclusion: .+', r'\1  commit: pending\n  conclusion: pending', "proof closure")
PROOF.write_text(proof, encoding="utf-8")

continuity = CONTINUITY.read_text(encoding="utf-8")
continuity = sub_once(continuity, r'^version: "3\.27\.0"$', 'version: "3.27.1"', "continuity version", re.M)
continuity = sub_once(continuity, r'^last-updated: ".+"$', f'last-updated: "{STAMP}"', "continuity timestamp", re.M)
continuity = sub_once(continuity, r'^- chapitre 27 : version `1\.0\.0` ;$', '- chapitre 27 : version `1.0.1` ;', "continuity chapter version", re.M)
continuity = sub_once(
    continuity,
    r'^- ne pas considérer une couverture élevée comme preuve de qualité ou de correction métier ;$',
    '- ne pas considérer une couverture élevée comme preuve de qualité ou de correction métier ;\n- ne pas employer les calques `durée murale`, `temps mur`, `temps mural` ou `temps horloge` ; utiliser `durée réelle (durée de l’horloge système)` et `horloge système` ;',
    "continuity terminology rule",
    re.M,
)
journal = f'''### {STAMP} — version 3.27.1\n\n- chapitre 27 corrigé : les calques `durée murale`, `temps mur` et `temps horloge` sont remplacés par `durée réelle (durée de l’horloge système)` ou `horloge système` selon le contexte ;\n- règle terminologique permanente ajoutée au validateur des chapitres ;\n- version du chapitre portée à `1.0.1` et audit à `1.0.2` ;\n- preuve QA remise en attente de validation ;\n- aucun test runtime revendiqué et aucun PDF construit.\n\n'''
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

print("Chapter 27 terminology correction prepared.")
