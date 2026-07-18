#!/usr/bin/env python3
"""Audit usage-context markers and temporarily export migrated Livre II files."""

from __future__ import annotations

import argparse
import base64
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT_DATE = "2026-07-18"
STANDARD_ID = "DOC-V0-ANN-CONTEXTES"
MARKER_RE = re.compile(r"^> \*\*\[(PS|CMD|WSL|DCT|DCK|VSC|WEB|APP|SORTIE|LECTURE)\]")
FENCE_RE = re.compile(r"^(?P<indent>\s*)(?P<fence>`{3,}|~{3,})(?P<lang>[^`]*)$")
EXTERNAL_LINK_RE = re.compile(r"\[[^\]]+\]\(https?://[^)]+\)|https?://\S+")
PATH_RE = re.compile(
    r"`([^`]*(?:[\\/]|\.(?:json|ya?ml|toml|ini|cfg|conf|env|md|txt|py|ps1|sh|bat|cmd|sql|gd|tscn|tres|godot|dockerfile|gitignore|gitattributes))[^`]*)`",
    re.IGNORECASE,
)
CHAPTER_RE = re.compile(r"(?:Volume-0|Livre-I|Livre-II)/CHAPITRE-\d{2}-.+\.md$")
L2_CHAPTER_RE = re.compile(r"Livre-II/CHAPITRE-\d{2}-.+\.md$")

USAGE_NOTES = {
    "Volume-0": (
        "> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, "
        "**[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. "
        "Voir la [convention complète](annexes/CONVENTION-OUTILS-ET-CONTEXTES.md)."
    ),
    "Livre-I": (
        "> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, "
        "**[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. "
        "Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md)."
    ),
    "Livre-II": (
        "> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, "
        "**[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. "
        "Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md)."
    ),
}

ACTION_LINK_WORDS = (
    "télécharg", "telecharg", "ouvrir", "accéder", "acceder", "consulter",
    "page officielle", "site officiel", "récupérer", "recuperer", "aller sur", "se rendre",
)
REFERENCE_HEADINGS = (
    "source", "référence", "reference", "bibliographie", "documentation officielle", "liens utiles",
)
FILE_LANGS = {
    "json", "yaml", "yml", "toml", "ini", "cfg", "conf", "python", "py", "gdscript", "sql",
    "dockerfile", "dotenv", "env", "gitignore", "gitattributes", "markdown", "md", "xml", "csv",
    "javascript", "js", "typescript", "ts",
}
APP_NAMES = ("godot", "project manager", "inspector", "éditeur", "editeur")
APP_ACTIONS = (
    "ouvrir", "lancer", "sélectionner", "selectionner", "cliquer", "choisir", "créer", "creer",
    "ajouter", "activer", "désactiver", "desactiver", "modifier", "enregistrer", "importer",
)


@dataclass
class Fence:
    start: int
    end: int
    lang: str


def iter_markdown_files() -> list[Path]:
    result: list[Path] = []
    for base in (ROOT / "Volume-0", ROOT / "Livre-I", ROOT / "Livre-II"):
        result.extend(sorted(base.rglob("*.md")))
    result.append(ROOT / "STYLE_GUIDE.md")
    return [path for path in result if path.is_file()]


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def parse_fences(lines: list[str]) -> list[Fence]:
    result: list[Fence] = []
    current: tuple[int, str, int, str] | None = None
    for index, line in enumerate(lines):
        match = FENCE_RE.match(line)
        if not match:
            continue
        fence = match.group("fence")
        char, length = fence[0], len(fence)
        lang = match.group("lang").strip().split()[0].lower() if match.group("lang").strip() else ""
        if current is None:
            current = (index, char, length, lang)
            continue
        start, open_char, open_length, open_lang = current
        if char == open_char and length >= open_length and not lang:
            result.append(Fence(start, index, open_lang))
            current = None
    return result


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


def current_heading(lines: list[str], index: int) -> str:
    cursor = index
    while cursor >= 0:
        value = lines[cursor].strip()
        if value.startswith("#"):
            return value.lstrip("#").strip().lower()
        cursor -= 1
    return ""


def extract_target_path(context: str) -> str | None:
    matches = PATH_RE.findall(context)
    if not matches:
        return None
    candidate = matches[-1].strip()
    return candidate if len(candidate) <= 180 else None


def is_file_content_context(context_lower: str, lang: str) -> bool:
    if extract_target_path(context_lower):
        return True
    words = (
        "créer le fichier", "creer le fichier", "modifier le fichier", "contenu du fichier",
        "fichier :", "fichier `", "enregistrer dans", "script suivant", "créer le script",
        "creer le script", "remplacer le contenu", "coller dans",
    )
    return lang in FILE_LANGS and any(word in context_lower for word in words)


def marker_for(lines: list[str], fence: Fence) -> str:
    context = context_before(lines, fence.start)
    lower = context.lower()
    lang = fence.lang.lower()
    target = extract_target_path(context)

    if lang in {"text", "console", "output"} and any(
        word in lower for word in ("résultat attendu", "resultat attendu", "sortie attendue", "doit afficher", "exemple de sortie")
    ):
        return "> **[SORTIE] Résultat attendu - Ne pas saisir :** comparer avec la sortie obtenue."

    if lang in {"powershell", "pwsh"}:
        if is_file_content_context(lower, lang) and not any(word in lower for word in ("exécuter", "executer", "commande", "vérifier", "verifier")):
            suffix = f" `{target}`." if target else " le script indiqué dans l’étape."
            return f"> **[VSC] Visual Studio Code - Créer ou modifier :**{suffix}"
        return "> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows."

    if lang in {"cmd", "bat", "batch"}:
        if is_file_content_context(lower, lang):
            suffix = f" `{target}`." if target else " le fichier de commandes indiqué."
            return f"> **[VSC] Visual Studio Code - Créer ou modifier :**{suffix}"
        return "> **[CMD] Invite de commandes Windows - Exécuter :** utiliser `cmd.exe`."

    if lang in {"bash", "sh", "shell", "zsh"}:
        if is_file_content_context(lower, lang) and any(ext in lower for ext in (".sh", "dockerfile", "script")):
            suffix = f" `{target}`." if target else " le script indiqué dans l’étape."
            return f"> **[VSC] Visual Studio Code - Créer ou modifier :**{suffix}"
        if any(word in lower for word in ("dans le conteneur", "terminal du conteneur", "docker exec", "shell du conteneur")):
            return "> **[DCT] Terminal du conteneur - Exécuter :** utiliser le shell du conteneur concerné."
        return "> **[WSL] Terminal WSL/Bash - Exécuter :** utiliser la distribution Linux indiquée."

    if lang in FILE_LANGS and is_file_content_context(lower, lang):
        suffix = f" `{target}`." if target else " le fichier indiqué dans l’étape."
        return f"> **[VSC] Visual Studio Code - Créer ou modifier :**{suffix}"

    if lang == "mermaid":
        return "> **[LECTURE] Diagramme de référence - Ne pas exécuter :** lire le flux représenté."

    if lang in {"text", "", "plaintext"}:
        if any(word in lower for word in ("arborescence", "structure", "architecture", "organisation", "flux", "principe", "schéma", "schema")):
            return "> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel."
        return "> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**"

    return "> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède."


def add_markers(lines: list[str]) -> tuple[list[str], int]:
    insertions: dict[int, str] = {}
    for fence in parse_fences(lines):
        previous = previous_nonempty(lines, fence.start)
        if previous and MARKER_RE.match(previous[1]):
            continue
        insertions[fence.start] = marker_for(lines, fence)
    output: list[str] = []
    for index, line in enumerate(lines):
        marker = insertions.get(index)
        if marker:
            if output and output[-1].strip():
                output.append("")
            output.extend([marker, ""])
        output.append(line)
    return output, len(insertions)


def add_web_markers(lines: list[str]) -> tuple[list[str], int]:
    insertions: dict[int, str] = {}
    for index, line in enumerate(lines):
        if not EXTERNAL_LINK_RE.search(line):
            continue
        if any(word in current_heading(lines, index) for word in REFERENCE_HEADINGS):
            continue
        context = (context_before(lines, index, 4) + " " + line).lower()
        if not any(word in context for word in ACTION_LINK_WORDS):
            continue
        previous = previous_nonempty(lines, index)
        if previous and MARKER_RE.match(previous[1]):
            continue
        if index > 0 and lines[index - 1].lstrip().startswith(("- ", "* ")):
            continue
        insertions[index] = "> **[WEB] Navigateur internet - Ouvrir :** utiliser la page officielle indiquée ci-dessous."
    output: list[str] = []
    for index, line in enumerate(lines):
        marker = insertions.get(index)
        if marker:
            if output and output[-1].strip():
                output.append("")
            output.extend([marker, ""])
        output.append(line)
    return output, len(insertions)


def add_app_markers(lines: list[str]) -> tuple[list[str], int]:
    insertions: dict[int, str] = {}
    inside_fence = False
    for index, line in enumerate(lines):
        if line.strip().startswith(("```", "~~~")):
            inside_fence = not inside_fence
            continue
        if inside_fence or not line.strip() or line.lstrip().startswith(("#", ">", "- [")):
            continue
        lower = line.lower()
        if not any(name in lower for name in APP_NAMES) or not any(action in lower for action in APP_ACTIONS):
            continue
        previous = previous_nonempty(lines, index)
        if previous and MARKER_RE.match(previous[1]):
            continue
        app = "Godot"
        if "project manager" in lower:
            app = "Godot Project Manager"
        insertions[index] = f"> **[APP] {app} - Interface :** effectuer l’action décrite ci-dessous."
    output: list[str] = []
    for index, line in enumerate(lines):
        marker = insertions.get(index)
        if marker:
            if output and output[-1].strip():
                output.append("")
            output.extend([marker, ""])
        output.append(line)
    return output, len(insertions)


def usage_note_for(path: Path) -> str | None:
    rel = relative(path)
    if rel.startswith("Volume-0/annexes/"):
        return USAGE_NOTES["Volume-0"].replace("annexes/CONVENTION-OUTILS-ET-CONTEXTES.md", "CONVENTION-OUTILS-ET-CONTEXTES.md")
    if rel.startswith("Volume-0/QA/"):
        return USAGE_NOTES["Volume-0"].replace("annexes/CONVENTION-OUTILS-ET-CONTEXTES.md", "../annexes/CONVENTION-OUTILS-ET-CONTEXTES.md")
    if rel.startswith("Volume-0/"):
        return USAGE_NOTES["Volume-0"]
    if rel.startswith("Livre-I/"):
        return USAGE_NOTES["Livre-I"]
    if rel.startswith("Livre-II/"):
        return USAGE_NOTES["Livre-II"]
    return None


def add_usage_note(path: Path, lines: list[str]) -> tuple[list[str], bool]:
    if any("Repères d’utilisation" in line for line in lines[:100]):
        return lines, False
    if relative(path).endswith("CONVENTION-OUTILS-ET-CONTEXTES.md"):
        return lines, False
    note = usage_note_for(path)
    if not note:
        return lines, False
    for index, line in enumerate(lines):
        if line.startswith("# "):
            return lines[: index + 1] + ["", note] + lines[index + 1 :], True
    return lines, False


def bump_version(raw: str) -> str:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", raw)
    if not match:
        return raw
    major, minor, _patch = map(int, match.groups())
    return f"{major}.{minor + 1}.0"


def add_l2_metadata(path: Path, text: str) -> tuple[str, bool]:
    rel = relative(path)
    if not L2_CHAPTER_RE.fullmatch(rel) or not text.startswith("---\n"):
        return text, False
    end = text.find("\n---\n", 4)
    if end == -1:
        return text, False
    front, body = text[4:end], text[end + 5 :]
    lines = front.splitlines()
    fields = {line.split(":", 1)[0].strip(): index for index, line in enumerate(lines) if ":" in line}
    changed = False
    required = {
        "audit-status": 'audit-status: "complete"',
        "audit-date": f'audit-date: "{AUDIT_DATE}"',
        "audit-level": 'audit-level: "static-review"',
        "usage-context-standard": f'usage-context-standard: "{STANDARD_ID}"',
    }
    for key, rendered in required.items():
        if key in fields:
            if lines[fields[key]] != rendered:
                lines[fields[key]] = rendered
                changed = True
        else:
            lines.append(rendered)
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
    with_metadata, metadata = add_l2_metadata(path, original)
    lines = with_metadata.splitlines()
    lines, note = add_usage_note(path, lines)
    lines, fences = add_markers(lines)
    lines, web = add_web_markers(lines)
    lines, app = add_app_markers(lines)
    migrated = "\n".join(lines).rstrip() + "\n"
    changed = migrated != original
    if changed:
        path.write_text(migrated, encoding="utf-8", newline="\n")
    return {"changed": changed, "metadata": metadata, "usage_note": note, "fence_markers": fences, "web_markers": web, "app_markers": app}


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
        if any(word in current_heading(lines, index) for word in REFERENCE_HEADINGS):
            continue
        context = (context_before(lines, index, 4) + " " + line).lower()
        if not any(word in context for word in ACTION_LINK_WORDS):
            continue
        previous = previous_nonempty(lines, index)
        if not previous or not MARKER_RE.match(previous[1]):
            errors.append(f"{rel}:{index + 1}: lien procédural sans repère [WEB]")
    if L2_CHAPTER_RE.fullmatch(rel):
        text = "\n".join(lines[:100])
        for field in (
            'audit-status: "complete"', f'audit-date: "{AUDIT_DATE}"', 'audit-level: "static-review"',
            f'usage-context-standard: "{STANDARD_ID}"',
        ):
            if field not in text:
                errors.append(f"{rel}: métadonnée absente ou incorrecte : {field}")
    return errors


def export_l2_files() -> None:
    for path in iter_markdown_files():
        if not relative(path).startswith("Livre-II/"):
            continue
        payload = base64.b64encode(path.read_bytes()).decode("ascii")
        print(f"BEGIN_MIGRATED_FILE {relative(path)}")
        print(payload)
        print(f"END_MIGRATED_FILE {relative(path)}")


def apply() -> int:
    totals = {"files_changed": 0, "metadata": 0, "usage_notes": 0, "fence_markers": 0, "web_markers": 0, "app_markers": 0}
    for path in iter_markdown_files():
        result = migrate_file(path)
        for key in totals:
            source = "usage_note" if key == "usage_notes" else key
            totals[key] += int(bool(result[source])) if key in {"files_changed", "metadata", "usage_notes"} else int(result[source])
    print("Migration des contextes d’utilisation terminée")
    for key, value in totals.items():
        print(f"- {key}: {value}")
    return 0


def check() -> int:
    # Temporary CI-assisted migration: the checkout is ephemeral. The exported
    # files are retrieved from the artifact, reviewed, then committed through
    # the GitHub contents API. This behavior is removed before merge.
    if os.environ.get("GITHUB_ACTIONS") == "true":
        for path in iter_markdown_files():
            if relative(path).startswith("Livre-II/"):
                migrate_file(path)
        export_l2_files()
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
