#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise RuntimeError(f"Replacement expected once in {path}, found {text.count(old)}: {old!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


def main() -> None:
    replace_once(
        "tools/check_code_explanation_structure.py",
        "def check(path: Path) -> list[str]:\n    chapter = number(path)\n",
        "def check(path: Path) -> list[str]:\n    if path.parent.name == \"Livre-V\":\n        return []\n    chapter = number(path)\n",
    )

    replace_once(
        "tools/audit_contextes_utilisation.py",
        '"""Apply and audit normative usage-context markers through Livre IV."""',
        '"""Apply and audit normative usage-context markers through Livre V."""',
    )
    replace_once(
        "tools/audit_contextes_utilisation.py",
        'for base in (ROOT / "Volume-0", ROOT / "Livre-I", ROOT / "Livre-II", ROOT / "Livre-III", ROOT / "Livre-IV"):',
        'for base in (ROOT / "Volume-0", ROOT / "Livre-I", ROOT / "Livre-II", ROOT / "Livre-III", ROOT / "Livre-IV", ROOT / "Livre-V"):',
    )

    replace_once(
        "tools/audit_contextes_semantiques.py",
        'for base in (ROOT / "Volume-0", ROOT / "Livre-I", ROOT / "Livre-II", ROOT / "Livre-III", ROOT / "Livre-IV"):',
        'for base in (ROOT / "Volume-0", ROOT / "Livre-I", ROOT / "Livre-II", ROOT / "Livre-III", ROOT / "Livre-IV", ROOT / "Livre-V"):',
    )

    replace_once(
        "tools/report_contextes_utilisation.py",
        '    if rel.startswith("Livre-IV/"):\n        return "Livre IV"\n    return "Racine"',
        '    if rel.startswith("Livre-IV/"):\n        return "Livre IV"\n    if rel.startswith("Livre-V/"):\n        return "Livre V"\n    return "Racine"',
    )
    replace_once(
        "tools/report_contextes_utilisation.py",
        'for group in ("Volume 0", "Livre I", "Livre II", "Livre III", "Livre IV", "Racine"):',
        'for group in ("Volume 0", "Livre I", "Livre II", "Livre III", "Livre IV", "Livre V", "Racine"):',
    )
    replace_once(
        "tools/report_contextes_utilisation.py",
        'print("## Chapitres des Livres II à IV")',
        'print("## Chapitres des Livres II à V")',
    )
    replace_once(
        "tools/report_contextes_utilisation.py",
        'if not path.startswith(("Livre-II/", "Livre-III/", "Livre-IV/")):',
        'if not path.startswith(("Livre-II/", "Livre-III/", "Livre-IV/", "Livre-V/")):',
    )


if __name__ == "__main__":
    main()
