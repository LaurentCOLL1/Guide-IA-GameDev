#!/usr/bin/env python3
"""Contrôles documentaires légers, sans génération PDF."""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote

import yaml

CHAPTER_RE = re.compile(r"Livre-(I|II)/CHAPITRE-(\d{2})-.+\.md$")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
INLINE_CODE_RE = re.compile(r"(`+)([^\n]*?)\1")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^(?P<fence>`{3,}|~{3,})(?P<lang>.*)$")
CONFLICT_MARKERS = ("<<<<<<<", "=======", ">>>>>>>")
VALID_AUDIT_LEVELS = {"static-review", "runtime-tested"}
VALID_REASONING = {"GPT-5.6 Sol — Moyenne", "GPT-5.6 Sol — Élevée"}
ERROR_SECTION_MARKER = "<!-- qa:error-correction-section -->"
ERROR_INDEX_MARKER = "<!-- qa:error-correction-index -->"
ERROR_HEADING_RE = re.compile(r"(?:erreurs? fréquentes|anti[- ]patterns?|symptômes fréquents|pièges(?: fréquents)?|mauvaises pratiques|problèmes fréquents|diagnostics et corrections)", re.IGNORECASE)


@dataclass
class ChapterStats:
    path: str
    lines: int = 0
    headings: int = 0
    code_blocks: int = 0
    duplicate_headings: list[str] = field(default_factory=list)
    duplicate_blocks: int = 0
    duplicate_paragraphs: int = 0


def parse_front_matter(text: str, rel: str, errors: list[str]) -> dict[str, object]:
    if not text.startswith("---\n"):
        if rel != "README.md":
            errors.append(f"Front matter YAML absent : {rel}")
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        errors.append(f"Front matter YAML non fermé : {rel}")
        return {}
    try:
        loaded = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError as exc:
        errors.append(f"YAML invalide dans {rel} : {exc}")
        return {}
    if not isinstance(loaded, dict):
        errors.append(f"Front matter YAML non mappé : {rel}")
        return {}
    return loaded


def normalize_heading(value: str) -> str:
    value = re.sub(r"`([^`]*)`", r"\1", value)
    value = re.sub(r"[*_~]", "", value)
    return re.sub(r"\s+", " ", value.strip().casefold())


def normalize_block(lines: list[str]) -> str:
    stripped = [line.rstrip() for line in lines]
    while stripped and not stripped[0]:
        stripped.pop(0)
    while stripped and not stripped[-1]:
        stripped.pop()
    return "\n".join(stripped)


def normalize_paragraph(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().casefold())


def text_without_fenced_code(text: str) -> str:
    """Remplace le contenu des blocs clôturés par des lignes vides.

    Les exemples de code peuvent contenir une séquence ``](`` qui ressemble à
    un lien Markdown. Les liens locaux ne doivent être contrôlés que dans le
    texte Markdown interprétable, pas dans les exemples littéraux.
    """
    result: list[str] = []
    in_fence = False
    fence_char = ""
    fence_length = 0

    for line in text.splitlines():
        match = FENCE_RE.match(line.strip())
        if match:
            fence = match.group("fence")
            if not in_fence:
                in_fence = True
                fence_char = fence[0]
                fence_length = len(fence)
            elif fence[0] == fence_char and len(fence) >= fence_length:
                in_fence = False
            result.append("")
            continue
        result.append("" if in_fence else line)

    return "\n".join(result)


def validate_error_correction_sections(text: str, rel: str, errors: list[str]) -> None:
    """Valide les sections pédagogiques d'erreurs indépendamment de leur titre."""
    lines = text.splitlines()
    headings: list[tuple[int, int, str]] = []
    in_fence = False
    fence_char = ""
    fence_length = 0
    for index, line in enumerate(lines):
        fence_match = FENCE_RE.match(line.strip())
        if fence_match:
            fence = fence_match.group("fence")
            if not in_fence:
                in_fence = True
                fence_char = fence[0]
                fence_length = len(fence)
            elif fence[0] == fence_char and len(fence) >= fence_length:
                in_fence = False
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(line)
        if match:
            headings.append((index, len(match.group(1)), match.group(2).strip()))

    for position, (start, level, title) in enumerate(headings):
        if level < 2 or not ERROR_HEADING_RE.search(title):
            continue
        end = len(lines)
        for next_start, next_level, _ in headings[position + 1:]:
            if next_level <= level:
                end = next_start
                break
        body = "\n".join(lines[start + 1:end])
        has_detail = ERROR_SECTION_MARKER in body
        has_index = ERROR_INDEX_MARKER in body
        if not has_detail and not has_index:
            errors.append(
                f"Section d’erreurs non qualifiée dans {rel} : {title}. "
                "Ajouter un marqueur détaillé ou d’index."
            )
            continue
        if has_index:
            normalized = body.casefold()
            if "exemples" not in normalized or "section" not in normalized:
                errors.append(f"Index de diagnostic sans renvoi explicite dans {rel} : {title}")
            continue

        children = [
            (child_start, child_title)
            for child_start, child_level, child_title in headings[position + 1:]
            if child_start < end and child_level == level + 1
        ]
        if not children:
            errors.append(f"Section détaillée sans sous-cas dans {rel} : {title}")
            continue
        for child_index, (child_start, child_title) in enumerate(children):
            child_end = children[child_index + 1][0] if child_index + 1 < len(children) else end
            child_body = "\n".join(lines[child_start + 1:child_end])
            missing: list[str] = []
            if "Exemple fautif" not in child_body:
                missing.append("exemple fautif")
            corrected_match = re.search(
                r"(?:exemple|structure|organisation|chemin|dépendances?|arbre|lot)[^\n]{0,100}corrig(?:é|ée|és|ées)",
                child_body,
                re.IGNORECASE,
            )
            if corrected_match is None:
                missing.append("exemple corrigé")
            has_labeled_difference = "**Différence :**" in child_body
            trailing_prose = ""
            if corrected_match is not None:
                corrected_part = child_body[corrected_match.end():]
                outside_fence: list[str] = []
                current_after_fence: list[str] = []
                in_fence = False
                saw_closed_fence = False
                fence_char = ""
                fence_length = 0
                for line in corrected_part.splitlines():
                    fence_match = FENCE_RE.match(line.strip())
                    if fence_match:
                        fence = fence_match.group("fence")
                        if not in_fence:
                            in_fence = True
                            fence_char = fence[0]
                            fence_length = len(fence)
                        elif fence[0] == fence_char and len(fence) >= fence_length:
                            in_fence = False
                            saw_closed_fence = True
                            current_after_fence = []
                        continue
                    if saw_closed_fence and not in_fence:
                        current_after_fence.append(line)
                outside_fence = [
                    line.strip()
                    for line in current_after_fence
                    if line.strip() and not line.lstrip().startswith((">", "<!--"))
                ]
                trailing_prose = normalize_paragraph(" ".join(outside_fence))
            if not has_labeled_difference and len(trailing_prose) < 45:
                missing.append("explication de la différence")
            if missing:
                errors.append(
                    f"Cas pédagogique incomplet dans {rel} — {child_title} : "
                    + ", ".join(missing)
                )


def inspect_duplicates(text: str, rel: str) -> ChapterStats:
    lines = text.splitlines()
    headings: list[str] = []
    blocks: list[str] = []
    paragraphs: list[str] = []
    in_fence = False
    fence_char = ""
    fence_length = 0
    block_lines: list[str] = []
    paragraph_lines: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph_lines
        if paragraph_lines:
            value = normalize_paragraph(" ".join(paragraph_lines))
            if len(value) >= 180:
                paragraphs.append(value)
            paragraph_lines = []

    for line in lines:
        match_fence = FENCE_RE.match(line.strip())
        if match_fence:
            flush_paragraph()
            fence = match_fence.group("fence")
            if in_fence and fence[0] == fence_char and len(fence) >= fence_length:
                normalized = normalize_block(block_lines)
                meaningful = [item for item in normalized.splitlines() if item.strip()]
                if len(meaningful) >= 4 or len(normalized) >= 180:
                    blocks.append(normalized)
                block_lines = []
                in_fence = False
            elif not in_fence:
                in_fence = True
                fence_char = fence[0]
                fence_length = len(fence)
            continue
        if in_fence:
            block_lines.append(line)
            continue

        match_heading = HEADING_RE.match(line)
        if match_heading:
            flush_paragraph()
            headings.append(normalize_heading(match_heading.group(2)))
            continue
        if not line.strip() or line.lstrip().startswith((">", "- ", "* ", "|")):
            flush_paragraph()
            continue
        paragraph_lines.append(line.strip())

    flush_paragraph()
    heading_counts = Counter(headings)
    block_counts = Counter(blocks)
    paragraph_counts = Counter(paragraphs)
    return ChapterStats(
        path=rel,
        lines=len(lines),
        headings=len(headings),
        code_blocks=len(blocks),
        duplicate_headings=sorted(k for k, v in heading_counts.items() if v > 1),
        duplicate_blocks=sum(v - 1 for v in block_counts.values() if v > 1),
        duplicate_paragraphs=sum(v - 1 for v in paragraph_counts.values() if v > 1),
    )


def validate_local_links(
    text: str,
    source: Path,
    root: Path,
    rel: str,
    errors: list[str],
) -> None:
    markdown_text = text_without_fenced_code(text)
    markdown_text = INLINE_CODE_RE.sub("", markdown_text)
    for raw_target in LINK_RE.findall(markdown_text):
        target = unquote(raw_target.strip().split()[0].strip("<>"))
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target_path = target.split("#", 1)[0]
        if not target_path:
            continue
        resolved = (source.parent / target_path).resolve()
        try:
            resolved.relative_to(root)
        except ValueError:
            errors.append(f"Lien sortant du dépôt dans {rel} : {target}")
            continue
        if not resolved.exists():
            errors.append(f"Lien local cassé dans {rel} : {target}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--report", default="dist/QA-CHAPTERS.md")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    report_path = root / args.report
    report_path.parent.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []
    warnings: list[str] = []

    contents_path = root / "contents.txt"
    if not contents_path.is_file():
        errors.append("contents.txt est absent.")
        entries: list[str] = []
    else:
        entries = [
            line.strip()
            for line in contents_path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]
        if len(entries) != len(set(entries)):
            errors.append("Une ou plusieurs sources sont dupliquées dans contents.txt.")

    sources = [root / entry for entry in entries]
    for entry, source in zip(entries, sources):
        if not source.is_file():
            errors.append(f"Source absente dans contents.txt : {entry}")

    chapter_entries: dict[str, list[tuple[str, int]]] = {"I": [], "II": []}
    for entry in entries:
        match = CHAPTER_RE.fullmatch(entry)
        if match:
            chapter_entries[match.group(1)].append((entry, int(match.group(2))))

    actual_i = [number for _, number in chapter_entries["I"]]
    if actual_i != list(range(1, 11)):
        errors.append(f"Le Livre I doit déclarer les chapitres 01 à 10 dans l’ordre ; détectés : {actual_i}.")

    actual_ii = [number for _, number in chapter_entries["II"]]
    if actual_ii != list(range(1, len(actual_ii) + 1)):
        errors.append(f"Les chapitres présents du Livre II doivent être continus depuis 01 ; détectés : {actual_ii}.")

    ids: dict[str, str] = {}
    stats: list[ChapterStats] = []
    expected_livre_i_ids = {
        1: "DOC-L1-CH01", 2: "DOC-L1-ENV-TERMINAL", 3: "DOC-L1-ENV-GIT",
        4: "DOC-L1-ENV-PYTHON", 5: "DOC-L1-CH02", 6: "DOC-L1-CH03",
        7: "DOC-L1-CH04", 8: "DOC-L1-CH05", 9: "DOC-L1-CH06",
        10: "DOC-L1-ENV-SECURITY",
    }

    for source in sources:
        if not source.is_file() or source.suffix.lower() != ".md":
            continue
        rel = source.relative_to(root).as_posix()
        text = source.read_text(encoding="utf-8")
        if any(marker in text for marker in CONFLICT_MARKERS):
            errors.append(f"Marqueur de conflit Git détecté : {rel}")

        metadata = parse_front_matter(text, rel, errors)
        if metadata:
            for field_name in ("title", "status", "version"):
                if not metadata.get(field_name):
                    errors.append(f"Métadonnée obligatoire absente ({field_name}) : {rel}")
            doc_id = metadata.get("id") or metadata.get("identifier")
            if not doc_id:
                errors.append(f"Métadonnée obligatoire absente (id ou identifier) : {rel}")
            elif str(doc_id) in ids:
                errors.append(f"Identifiant dupliqué {doc_id} : {ids[str(doc_id)]} et {rel}")
            else:
                ids[str(doc_id)] = rel

        chapter_match = CHAPTER_RE.fullmatch(rel)
        if chapter_match:
            book_code, number_text = chapter_match.groups()
            number = int(number_text)
            expected_book = "Livre I" if book_code == "I" else "Livre II"
            if metadata.get("book") != expected_book:
                errors.append(f"Métadonnée book incorrecte pour {rel}.")
            if metadata.get("chapter") != number:
                errors.append(f"Numéro de chapitre incohérent dans {rel} : attendu {number}, reçu {metadata.get('chapter')}.")
            if not metadata.get("last-verified"):
                errors.append(f"Métadonnée last-verified absente : {rel}")
            actual_id = metadata.get("id") or metadata.get("identifier")
            expected_id = expected_livre_i_ids[number] if book_code == "I" else f"DOC-L2-CH{number:02d}"
            if actual_id != expected_id:
                errors.append(f"Identifiant stable incorrect pour {rel} : attendu {expected_id}, reçu {actual_id}.")

            if book_code == "II":
                if metadata.get("audit-status") != "complete":
                    errors.append(f"Audit post-création incomplet : {rel}")
                if not metadata.get("audit-date"):
                    errors.append(f"Métadonnée audit-date absente : {rel}")
                if metadata.get("audit-level") not in VALID_AUDIT_LEVELS:
                    errors.append(f"Métadonnée audit-level invalide : {rel}")
                if metadata.get("usage-context-standard") != "DOC-V0-ANN-CONTEXTES":
                    errors.append(f"Convention de contexte absente ou incorrecte : {rel}")
                if number >= 3 and metadata.get("recommended-reasoning") not in VALID_REASONING:
                    errors.append(f"Niveau GPT-5.6 Sol absent ou invalide : {rel}")
                audit_report = metadata.get("audit-report")
                if not audit_report:
                    errors.append(f"Métadonnée audit-report absente : {rel}")
                elif not (root / str(audit_report)).is_file():
                    errors.append(f"Rapport d’audit absent pour {rel} : {audit_report}")

                validate_error_correction_sections(text, rel, errors)
                chapter_stats = inspect_duplicates(text, rel)
                stats.append(chapter_stats)
                if chapter_stats.duplicate_headings:
                    errors.append(f"Titres dupliqués dans {rel} : {chapter_stats.duplicate_headings}")
                if chapter_stats.duplicate_blocks:
                    errors.append(f"Blocs significatifs dupliqués dans {rel} : {chapter_stats.duplicate_blocks}")
                if chapter_stats.duplicate_paragraphs:
                    errors.append(f"Paragraphes longs dupliqués dans {rel} : {chapter_stats.duplicate_paragraphs}")

        validate_local_links(text, source, root, rel, errors)

    metadata_file = root / "metadata.yaml"
    if not metadata_file.is_file():
        errors.append("metadata.yaml est absent.")
    else:
        try:
            global_metadata = yaml.safe_load(metadata_file.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            errors.append(f"metadata.yaml invalide : {exc}")
            global_metadata = {}
        if global_metadata.get("license") in (None, "", "À définir avant publication"):
            warnings.append("La licence globale reste à définir avant publication officielle.")

    lines = [
        "# Validation automatique légère des chapitres", "",
        "Cette validation ne construit aucun PDF.", "",
        f"- Sources déclarées : **{len(sources)}**",
        f"- Chapitres du Livre I : **{len(chapter_entries['I'])}**",
        f"- Chapitres du Livre II : **{len(chapter_entries['II'])}**",
        f"- Identifiants uniques : **{len(ids)}**",
        f"- Erreurs bloquantes : **{len(errors)}**",
        f"- Avertissements : **{len(warnings)}**", "",
        "## Doublons par chapitre du Livre II", "",
        "| Chapitre | Lignes | Titres | Blocs significatifs | Titres dupliqués | Blocs dupliqués | Paragraphes dupliqués |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for item in stats:
        lines.append(
            f"| `{item.path}` | {item.lines} | {item.headings} | {item.code_blocks} | "
            f"{len(item.duplicate_headings)} | {item.duplicate_blocks} | {item.duplicate_paragraphs} |"
        )
    lines.extend(["", "## Erreurs", ""])
    lines.extend([f"- {item}" for item in errors] or ["- Aucune."])
    lines.extend(["", "## Avertissements", ""])
    lines.extend([f"- {item}" for item in warnings] or ["- Aucun."])
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(report_path.read_text(encoding="utf-8"))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
