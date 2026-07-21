#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".qa/restore_semantic_error_sections.py"

spec = importlib.util.spec_from_file_location("semantic_restorer", SOURCE)
if spec is None or spec.loader is None:
    raise RuntimeError("Impossible de charger le restaurateur sémantique")
restorer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(restorer)

DETAILED = "**Explication détaillée du bloc :**"
FAULTY = re.compile(
    r".*?Pourquoi cet exemple est fautif\s*:\*\*\s*(.*)$",
    re.IGNORECASE,
)
CORRECTED = re.compile(
    r".*?Pourquoi la correction fonctionne\s*:\*\*\s*(.*)$",
    re.IGNORECASE,
)
CALLS = iter(restorer.CHAPTERS.keys())


def normalize_historical_error_section(section: str) -> str:
    normalized: list[str] = []
    for line in section.splitlines():
        stripped = line.strip()
        if stripped in {restorer.STRUCTURED, DETAILED}:
            continue
        faulty = FAULTY.match(line)
        if faulty:
            suffix = faulty.group(1).strip()
            normalized.append(
                "**Pourquoi cet exemple est fautif :**"
                + (f" {suffix}" if suffix else "")
            )
            continue
        corrected = CORRECTED.match(line)
        if corrected:
            suffix = corrected.group(1).strip()
            normalized.append(
                "**Pourquoi la correction fonctionne :**"
                + (f" {suffix}" if suffix else "")
            )
            continue
        normalized.append(line)

    text = "\n".join(normalized)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.rstrip() + "\n"


def restore_error_section(current: str, historical: str) -> str:
    chapter_number = next(CALLS)
    current_start, current_end = restorer.section_bounds(
        current, restorer.ERROR_MARKER
    )
    old_start, old_end = restorer.section_bounds(
        historical, restorer.ERROR_MARKER
    )
    restored = normalize_historical_error_section(
        historical[old_start:old_end]
    ).rstrip() + "\n\n"
    result = current[:current_start] + restored + current[current_end:]
    section = result[current_start : current_start + len(restored)]

    if restorer.STRUCTURED in section or DETAILED in section:
        raise RuntimeError(
            f"Chapitre {chapter_number}: un sous-titre d’explication subsiste "
            "dans la section restaurée"
        )
    if section.count("**Pourquoi cet exemple est fautif :**") < 1:
        labels = [
            line.strip()
            for line in section.splitlines()
            if "Pourquoi" in line
        ]
        raise RuntimeError(
            f"Chapitre {chapter_number}: explication fautive directe absente; "
            f"libellés rencontrés={labels[:8]}"
        )
    if section.count("**Pourquoi la correction fonctionne :**") < 1:
        labels = [
            line.strip()
            for line in section.splitlines()
            if "Pourquoi" in line
        ]
        raise RuntimeError(
            f"Chapitre {chapter_number}: explication corrigée directe absente; "
            f"libellés rencontrés={labels[:8]}"
        )
    return result


restorer.restore_error_section = restore_error_section
restorer.main()
