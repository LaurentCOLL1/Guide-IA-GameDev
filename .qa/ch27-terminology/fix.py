#!/usr/bin/env python3
from pathlib import Path

STAMP = "2026-07-22T01:40:00+02:00"
CHAPTER = Path("Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md")
AUDIT = Path("Livre-II/QA/AUDIT-CHAPITRE-27.md")
PROOF = Path("Livre-II/QA/VALIDATION-FINALE-CHAPITRE-27.yaml")
CONTINUITY = Path("CONTINUITE-PROJET.md")
VALIDATOR = Path("tools/validate_chapters.py")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


chapter = CHAPTER.read_text(encoding="utf-8")
chapter = replace_once(chapter, 'version: "1.0.0"', 'version: "1.0.1"', "chapter version")
chapter = replace_once(chapter, 'last-verified: "2026-07-21T21:00:05+02:00"', f'last-verified: "{STAMP}"', "chapter last-verified")
chapter = replace_once(chapter, 'audit-date: "2026-07-21T21:00:05+02:00"', f'audit-date: "{STAMP}"', "chapter audit-date")
chapter = replace_once(
    chapter,
    "Le harness ne saute aucun tick, n’en ajoute aucun et n’attend aucune durée murale.",
    "Le harness ne saute aucun tick, n’en ajoute aucun et ne dépend d’aucune durée réelle (durée de l’horloge système).",
    "wall-clock duration",
)
chapter = replace_once(
    chapter,
    "Le temps mur, la mémoire et le rendu exigent des benchmarks séparés sur la configuration de référence.",
    "La durée réelle (durée de l’horloge système), la mémoire et le rendu exigent des benchmarks séparés sur la configuration de référence.",
    "wall-clock time",
)
for forbidden in ("durée murale", "temps mur", "temps mural"):
    if forbidden in chapter.casefold():
        raise RuntimeError(f"Forbidden terminology remains in chapter: {forbidden}")
CHAPTER.write_text(chapter, encoding="utf-8")

audit = AUDIT.read_text(encoding="utf-8")
audit = replace_once(audit, 'version: "1.0.1"', 'version: "1.0.2"', "audit version")
audit = replace_once(audit, 'chapter-version: "1.0.0"', 'chapter-version: "1.0.1"', "audit chapter version")
audit = replace_once(audit, 'audit-date: "2026-07-21T21:00:05+02:00"', f'audit-date: "{STAMP}"', "audit date")
audit = replace_once(audit, 'last-verified: "2026-07-21T21:00:05+02:00"', f'last-verified: "{STAMP}"', "audit verified")
audit = replace_once(
    audit,
    "- les codes de sortie non nuls restent bloquants.",
    "- les codes de sortie non nuls restent bloquants ;\n- la terminologie emploie `durée réelle (durée de l’horloge système)` pour traduire le concept anglais de wall-clock time ou wall-clock duration.",
    "audit terminology note",
)
AUDIT.write_text(audit, encoding="utf-8")

proof = PROOF.read_text(encoding="utf-8")
proof = replace_once(proof, "status: complete", "status: pending", "proof status")
proof = replace_once(proof, "validation-date: '2026-07-21'", "validation-date: '2026-07-22'", "proof date")
proof = replace_once(proof, "  version: 1.0.0", "  version: 1.0.1", "proof chapter version")
proof = replace_once(proof, "  blocking-errors: 0", "  blocking-errors: pending", "proof errors")
proof = replace_once(proof, "  warnings: 1", "  warnings: pending", "proof warnings")
proof = replace_once(
    proof,
    "  validate-chapters-without-pdf:\n    run-id: 29862111418\n    conclusion: success",
    "  validate-chapters-without-pdf:\n    run-id: pending\n    conclusion: pending",
    "proof chapter workflow",
)
proof = replace_once(
    proof,
    "  validate-usage-contexts:\n    run-id: 29862111412\n    conclusion: success",
    "  validate-usage-contexts:\n    run-id: pending\n    conclusion: pending",
    "proof context workflow",
)
proof = replace_once(proof, "    id: 8507704291", "    id: pending", "proof artifact id")
proof = replace_once(proof, "    digest: sha256:678af704b617e916593159dacca254703150b390a6f1b4a367743925dd87b370", "    digest: pending", "proof artifact digest")
proof = replace_once(
    proof,
    "evidence-closure:\n  commit: 769b424af8312fa66676110cad97cb523a25bde8\n  conclusion: success",
    "evidence-closure:\n  commit: pending\n  conclusion: pending",
    "proof closure",
)
PROOF.write_text(proof, encoding="utf-8")

continuity = CONTINUITY.read_text(encoding="utf-8")
continuity = replace_once(continuity, 'version: "3.27.0"', 'version: "3.27.1"', "continuity version")
continuity = replace_once(continuity, 'last-updated: "2026-07-21T21:00:05+02:00"', f'last-updated: "{STAMP}"', "continuity timestamp")
continuity = replace_once(continuity, '- chapitre 27 : version `1.0.0` ;', '- chapitre 27 : version `1.0.1` ;', "continuity chapter version")
continuity = replace_once(
    continuity,
    "- ne pas considérer une couverture élevée comme preuve de qualité ou de correction métier ;",
    "- ne pas considérer une couverture élevée comme preuve de qualité ou de correction métier ;\n- ne pas employer les calques `durée murale`, `temps mur` ou `temps mural` ; utiliser `durée réelle (durée de l’horloge système)` ;",
    "continuity terminology rule",
)
journal = f'''### {STAMP} — version 3.27.1\n\n- chapitre 27 corrigé : `durée murale` et `temps mur` remplacés par `durée réelle (durée de l’horloge système)` ;\n- règle terminologique permanente ajoutée au validateur des chapitres ;\n- version du chapitre portée à `1.0.1` et audit à `1.0.2` ;\n- preuve QA remise en attente de validation ;\n- aucun test runtime revendiqué et aucun PDF construit.\n\n'''
continuity = replace_once(continuity, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal, "continuity journal")
CONTINUITY.write_text(continuity, encoding="utf-8")

validator = VALIDATOR.read_text(encoding="utf-8")
validator = replace_once(
    validator,
    'ERROR_HEADING_RE = re.compile(r"(?:erreurs? fréquentes|anti[- ]patterns?|symptômes fréquents|pièges(?: fréquents)?|mauvaises pratiques|problèmes fréquents|diagnostics et corrections)", re.IGNORECASE)\n',
    'ERROR_HEADING_RE = re.compile(r"(?:erreurs? fréquentes|anti[- ]patterns?|symptômes fréquents|pièges(?: fréquents)?|mauvaises pratiques|problèmes fréquents|diagnostics et corrections)", re.IGNORECASE)\nFORBIDDEN_TERMINOLOGY = {\n    "durée murale": "durée réelle (durée de l’horloge système)",\n    "temps mural": "durée réelle (durée de l’horloge système)",\n    "temps mur": "durée réelle (durée de l’horloge système)",\n}\n',
    "validator constants",
)
validator = replace_once(
    validator,
    '        if any(marker in text for marker in CONFLICT_MARKERS):\n            errors.append(f"Marqueur de conflit Git détecté : {rel}")\n\n        metadata = parse_front_matter(text, rel, errors)\n',
    '        if any(marker in text for marker in CONFLICT_MARKERS):\n            errors.append(f"Marqueur de conflit Git détecté : {rel}")\n\n        normalized_text = text.casefold()\n        for forbidden, replacement in FORBIDDEN_TERMINOLOGY.items():\n            pattern = rf"(?<!\\w){re.escape(forbidden)}(?!\\w)"\n            if re.search(pattern, normalized_text):\n                errors.append(\n                    f"Calque terminologique interdit dans {rel} : {forbidden!r}. "\n                    f"Employer {replacement!r}."\n                )\n\n        metadata = parse_front_matter(text, rel, errors)\n',
    "validator terminology check",
)
VALIDATOR.write_text(validator, encoding="utf-8")

print("Chapter 27 terminology correction prepared.")
