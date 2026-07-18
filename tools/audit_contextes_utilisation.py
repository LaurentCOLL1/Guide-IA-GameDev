#!/usr/bin/env python3
"""Audit and migrate usage-context markers in Volume 0 and Livre I.

The script has two modes:
- --apply: add the normative markers and chapter audit metadata;
- --check: fail when a procedural fenced block or actionable web link has no marker.

It intentionally uses only the Python standard library so it can run in CI.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT_DATE = "2026-07-18"
AUDIT_REPORT = "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
STANDARD_ID = "DOC-V0-ANN-CONTEXTES"
MARKER_CODES = {
    "PS",
    "CMD",
    "WSL",
    "DCT",
    "DCK",
    "VSC",
    "WEB",
    "APP",
    "SORTIE",
    "LECTURE",
}
MARKER_RE = re.compile(
    r"^> \*\*\[(PS|CMD|WSL|DCT|DCK|VSC|WEB|APP|SORTIE|LECTURE)\]"
)
FENCE_RE = re.compile(r"^(?P<indent>\s*)(?P<fence>`{3,}|~{3,})(?P<lang>[^`]*)$")
EXTERNAL_LINK_RE = re.compile(r"\[[^\]]+\]\(https?://[^)]+\)|https?://\S+")
PATH_RE = re.compile(
    r"`([^`]*(?:[\\/]|\.(?:json|ya?ml|toml|ini|cfg|conf|env|md|txt|py|ps1|sh|bat|cmd|sql|gd|tscn|tres|godot|dockerfile|gitignore|gitattributes))[^`]*)`",
    re.IGNORECASE,
)

CHAPTER_RE = re.compile(r"(?:Volume-0|Livre-I)/CHAPITRE-\d{2}-.+\.md$")

USAGE_NOTE_VOLUME0 = (
    "> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, "
    "**[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. "
    "Voir la [convention complète](annexes/CONVENTION-OUTILS-ET-CONTEXTES.md)."
)
USAGE_NOTE_LIVRE1 = (
    "> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, "
    "**[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. "
    "Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md)."
)

ACTION_LINK_WORDS = (
    "télécharg",
    "telecharg",
    "ouvrir",
    "accéder",
    "acceder",
    "consulter",
    "page officielle",
    "site officiel",
    "récupérer",
    "recuperer",
    "aller sur",
    "se rendre",
)
REFERENCE_HEADINGS = (
    "source",
    "référence",
    "reference",
    "bibliographie",
    "documentation officielle",
    "liens utiles",
)

FILE_LANGS = {
    "json",
    "yaml",
    "yml",
    "toml",
    "ini",
    "cfg",
    "conf",
    "python",
    "py",
    "gdscript",
    "sql",
    "dockerfile",
    "gitignore",
    "gitattributes",
    "markdown",
    "md",
    "xml",
    "csv",
    "javascript",
    "js",
    "typescript",
    "ts",
}


@dataclass
class Fence:
    start: int
    end: int
    lang: str


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for base in (ROOT / "Volume-0", ROOT / "Livre-I"):
        files.extend(sorted(base.rglob("*.md")))
    # The root style guide is normative and belongs to this migration.
    files.append(ROOT / "STYLE_GUIDE.md")
    return [path for path in files if path.is_file()]


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def parse_fences(lines: list[str]) -> list[Fence]:
    fences: list[Fence] = []
    current: tuple[int, str, int, str] | None = None
    for index, line in enumerate(lines):
        match = FENCE_RE.match(line)
        if not match:
            continue
        fence = match.group("fence")
        char = fence[0]
        length = len(fence)
        lang = match.group("lang").strip().split()[0].lower() if match.group("lang").strip() else ""
        if current is None:
            current = (index, char, length, lang)
            continue
        start, open_char, open_length, open_lang = current
        if char == open_char and length >= open_length and not lang:
            fences.append(Fence(start=start, end=index, lang=open_lang))
            current = None
    return fences


def previous_nonempty(lines: list[str], index: int) -> tuple[int, str] | None:
    cursor = index - 1
    while cursor >= 0:
        value = lines[cursor].strip()
        if value:
            return cursor, value
        cursor -= 1
    return None


def context_before(lines: list[str], index: int, count: int = 10) -> str:
    values: list[str] = []
    cursor = index - 1
    while cursor >= 0 and len(values) < count:
        value = lines[cursor].strip()
        if value:
            values.append(value)
        cursor -= 1
    return " ".join(reversed(values))


def extract_target_path(context: str) -> str | None:
    matches = PATH_RE.findall(context)
    if not matches:
        return None
    candidate = matches[-1].strip()
    if len(candidate) > 140:
        return None
    return candidate


def is_file_content_context(context_lower: str, lang: str) -> bool:
    path = extract_target_path(context_lower)
    if path:
        return True
    keywords = (
        "créer le fichier",
        "creer le fichier",
        "modifier le fichier",
        "contenu du fichier",
        "fichier :",
        "fichier `",
        "enregistrer dans",
        "compose.yaml",
        "dockerfile",
        ".vscode/settings.json",
        ".gitignore",
        ".gitattributes",
        "script suivant",
        "créer le script",
        "creer le script",
    )
    return lang in FILE_LANGS and any(word in context_lower for word in keywords)


def marker_for(lines: list[str], fence: Fence) -> str:
    context = context_before(lines, fence.start)
    lower = context.lower()
    lang = fence.lang.lower()
    target = extract_target_path(context)

    output_words = (
        "résultat attendu",
        "resultat attendu",
        "sortie attendue",
        "doit afficher",
        "affiche :",
        "exemple de sortie",
        "journal doit contenir",
    )
    if lang in {"text", "console", "output"} and any(word in lower for word in output_words):
        return "> **[SORTIE] Résultat attendu - Ne pas saisir :** comparer avec la sortie obtenue."

    if lang in {"powershell", "pwsh"}:
        if is_file_content_context(lower, lang) and not any(
            word in lower for word in ("exécuter", "executer", "commande", "vérifier", "verifier")
        ):
            suffix = f" `{target}`." if target else " le script indiqué dans l’étape."
            return f"> **[VSC] Visual Studio Code - Créer ou modifier :**{suffix}"
        return "> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows."

    if lang in {"cmd", "bat", "batch"}:
        if is_file_content_context(lower, lang):
            suffix = f" `{target}`." if target else " le fichier de commandes indiqué."
            return f"> **[VSC] Visual Studio Code - Créer ou modifier :**{suffix}"
        return "> **[CMD] Invite de commandes Windows - Exécuter :** utiliser `cmd.exe`."

    if lang in {"bash", "sh", "shell", "zsh"}:
        if is_file_content_context(lower, lang) and any(
            ext in lower for ext in (".sh", "dockerfile", "script")
        ):
            suffix = f" `{target}`." if target else " le script indiqué dans l’étape."
            return f"> **[VSC] Visual Studio Code - Créer ou modifier :**{suffix}"
        if any(word in lower for word in ("dans le conteneur", "terminal du conteneur", "docker exec", "shell du conteneur")):
            return "> **[DCT] Terminal du conteneur - Exécuter :** utiliser le shell du conteneur concerné."
        return "> **[WSL] Terminal WSL/Bash - Exécuter :** utiliser la distribution Linux indiquée."

    if lang in FILE_LANGS and is_file_content_context(lower, lang):
        suffix = f" `{target}`." if target else " le fichier indiqué dans l’étape."
        return f"> **[VSC] Visual Studio Code - Créer ou modifier :**{suffix}"

    if lang in {"mermaid"}:
        if is_file_content_context(lower, lang):
            suffix = f" `{target}`." if target else " le fichier Markdown indiqué."
            return f"> **[VSC] Visual Studio Code - Créer ou modifier :**{suffix}"
        return "> **[LECTURE] Diagramme de référence - Ne pas exécuter :** lire le flux représenté."

    if lang in {"text", "", "plaintext"}:
        if any(word in lower for word in ("arborescence", "structure", "architecture", "organisation", "flux", "principe", "schéma", "schema")):
            return "> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel."
        return "> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**"

    return "> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède."


def add_markers(lines: list[str]) -> tuple[list[str], int]:
    fences = parse_fences(lines)
    insertions: dict[int, str] = {}
    for fence in fences:
        previous = previous_nonempty(lines, fence.start)
        if previous and MARKER_RE.match(previous[1]):
            continue
        insertions[fence.start] = marker_for(lines, fence)

    if not insertions:
        return lines, 0

    output: list[str] = []
    for index, line in enumerate(lines):
        marker = insertions.get(index)
        if marker:
            if output and output[-1].strip():
                output.append("")
            output.append(marker)
            output.append("")
        output.append(line)
    return output, len(insertions)


def current_heading(lines: list[str], index: int) -> str:
    cursor = index
    while cursor >= 0:
        stripped = lines[cursor].strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip().lower()
        cursor -= 1
    return ""


def add_web_markers(lines: list[str]) -> tuple[list[str], int]:
    insertions: dict[int, str] = {}
    for index, line in enumerate(lines):
        if not EXTERNAL_LINK_RE.search(line):
            continue
        heading = current_heading(lines, index)
        if any(word in heading for word in REFERENCE_HEADINGS):
            continue
        context = context_before(lines, index, count=4).lower() + " " + line.lower()
        if not any(word in context for word in ACTION_LINK_WORDS):
            continue
        previous = previous_nonempty(lines, index)
        if previous and MARKER_RE.match(previous[1]):
            continue
        # One marker can cover a contiguous list of links.
        if index > 0 and lines[index - 1].lstrip().startswith(("- ", "* ")):
            continue
        insertions[index] = (
            "> **[WEB] Navigateur internet - Ouvrir :** utiliser la page officielle indiquée ci-dessous."
        )

    if not insertions:
        return lines, 0

    output: list[str] = []
    for index, line in enumerate(lines):
        marker = insertions.get(index)
        if marker:
            if output and output[-1].strip():
                output.append("")
            output.append(marker)
            output.append("")
        output.append(line)
    return output, len(insertions)


def add_usage_note(path: Path, lines: list[str]) -> tuple[list[str], bool]:
    if any("Repères d’utilisation" in line for line in lines[:80]):
        return lines, False
    if relative(path) in {
        "Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md",
        "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md",
    }:
        return lines, False

    note = USAGE_NOTE_VOLUME0 if relative(path).startswith("Volume-0/") else USAGE_NOTE_LIVRE1
    for index, line in enumerate(lines):
        if line.startswith("# "):
            return lines[: index + 1] + ["", note] + lines[index + 1 :], True
    return lines, False


def bump_version(value: str) -> str:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", value.strip())
    if not match:
        return value
    major, minor, _patch = map(int, match.groups())
    return f"{major}.{minor + 1}.0"


def add_audit_metadata(path: Path, text: str) -> tuple[str, bool]:
    rel = relative(path)
    if not CHAPTER_RE.fullmatch(rel):
        return text, False
    if not text.startswith("---\n"):
        return text, False
    end = text.find("\n---\n", 4)
    if end == -1:
        return text, False
    front = text[4:end]
    body = text[end + 5 :]
    lines = front.splitlines()
    changed = False

    fields = {line.split(":", 1)[0].strip(): index for index, line in enumerate(lines) if ":" in line}
    required = {
        "audit-status": 'audit-status: "complete"',
        "audit-date": f'audit-date: "{AUDIT_DATE}"',
        "audit-report": f'audit-report: "{AUDIT_REPORT}"',
        "audit-level": 'audit-level: "static-review"',
        "usage-context-standard": f'usage-context-standard: "{STANDARD_ID}"',
    }
    insertion_index = len(lines)
    for key, rendered in required.items():
        if key in fields:
            if lines[fields[key]] != rendered:
                lines[fields[key]] = rendered
                changed = True
        else:
            lines.insert(insertion_index, rendered)
            insertion_index += 1
            changed = True

    for index, line in enumerate(lines):
        if line.startswith("version:"):
            raw = line.split(":", 1)[1].strip().strip('"')
            bumped = bump_version(raw)
            if bumped != raw:
                lines[index] = f'version: "{bumped}"'
                changed = True
            break

    if not changed:
        return text, False
    return "---\n" + "\n".join(lines) + "\n---\n" + body, True


def migrate_file(path: Path) -> dict[str, int | bool]:
    original = path.read_text(encoding="utf-8")
    with_metadata, metadata_changed = add_audit_metadata(path, original)
    lines = with_metadata.splitlines()
    lines, note_added = add_usage_note(path, lines)
    lines, fence_markers = add_markers(lines)
    lines, web_markers = add_web_markers(lines)
    migrated = "\n".join(lines).rstrip() + "\n"
    changed = migrated != original
    if changed:
        path.write_text(migrated, encoding="utf-8", newline="\n")
    return {
        "changed": changed,
        "metadata": metadata_changed,
        "usage_note": note_added,
        "fence_markers": fence_markers,
        "web_markers": web_markers,
    }


def audit_file(path: Path) -> list[str]:
    rel = relative(path)
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    for fence in parse_fences(lines):
        previous = previous_nonempty(lines, fence.start)
        if not previous or not MARKER_RE.match(previous[1]):
            errors.append(f"{rel}:{fence.start + 1}: bloc `{fence.lang or 'text'}` sans repère d’utilisation")

    for index, line in enumerate(lines):
        if not EXTERNAL_LINK_RE.search(line):
            continue
        heading = current_heading(lines, index)
        if any(word in heading for word in REFERENCE_HEADINGS):
            continue
        context = context_before(lines, index, count=4).lower() + " " + line.lower()
        if not any(word in context for word in ACTION_LINK_WORDS):
            continue
        previous = previous_nonempty(lines, index)
        if not previous or not MARKER_RE.match(previous[1]):
            errors.append(f"{rel}:{index + 1}: lien procédural sans repère [WEB]")

    if CHAPTER_RE.fullmatch(rel):
        text = "\n".join(lines)
        for field in (
            'audit-status: "complete"',
            f'audit-date: "{AUDIT_DATE}"',
            f'audit-report: "{AUDIT_REPORT}"',
            'audit-level: "static-review"',
            f'usage-context-standard: "{STANDARD_ID}"',
        ):
            if field not in text[:1600]:
                errors.append(f"{rel}: métadonnée absente ou incorrecte : {field}")
    return errors


def apply() -> int:
    totals = {
        "files_changed": 0,
        "metadata": 0,
        "usage_notes": 0,
        "fence_markers": 0,
        "web_markers": 0,
    }
    for path in iter_markdown_files():
        result = migrate_file(path)
        totals["files_changed"] += int(bool(result["changed"]))
        totals["metadata"] += int(bool(result["metadata"]))
        totals["usage_notes"] += int(bool(result["usage_note"]))
        totals["fence_markers"] += int(result["fence_markers"])
        totals["web_markers"] += int(result["web_markers"])

    print("Migration des contextes d’utilisation terminée")
    for key, value in totals.items():
        print(f"- {key}: {value}")
    return 0


def check() -> int:
    errors: list[str] = []
    files = iter_markdown_files()
    for path in files:
        errors.extend(audit_file(path))

    print(f"Fichiers contrôlés : {len(files)}")
    print(f"Non-conformités : {len(errors)}")
    for error in errors:
        print(f"- {error}")
    return 1 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--apply", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    return apply() if args.apply else check()


if __name__ == "__main__":
    sys.exit(main())
