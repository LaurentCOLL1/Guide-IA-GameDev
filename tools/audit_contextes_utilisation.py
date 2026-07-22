#!/usr/bin/env python3
"""Apply and audit normative usage-context markers through Livre III."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT_DATE = "2026-07-18"
STANDARD_ID = "DOC-V0-ANN-CONTEXTES"
MARKER_RE = re.compile(r"^> \*\*\[(PS|CMD|WSL|DCT|DCK|VSC|WEB|APP|SORTIE|LECTURE)\]")
FENCE_RE = re.compile(r"^(?P<fence>`{3,}|~{3,})(?P<lang>[^`]*)$")
EXTERNAL_LINK_RE = re.compile(r"\[[^\]]+\]\(https?://[^)]+\)|https?://\S+")
L2_CHAPTER_RE = re.compile(r"Livre-II/CHAPITRE-\d{2}-.+\.md$")
ACTION_LINK_WORDS = (
    "télécharg", "telecharg", "ouvrir", "accéder", "acceder", "consulter",
    "page officielle", "site officiel", "récupérer", "recuperer", "aller sur", "se rendre",
)
REFERENCE_HEADINGS = (
    "source", "référence", "reference", "bibliographie", "documentation officielle", "liens utiles",
)
USAGE_NOTE = (
    "> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, "
    "**[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. "
    "Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md)."
)


@dataclass
class Fence:
    start: int
    end: int
    lang: str
    h2: str
    h3: str


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def all_markdown_files() -> list[Path]:
    files: list[Path] = []
    for base in (ROOT / "Volume-0", ROOT / "Livre-I", ROOT / "Livre-II", ROOT / "Livre-III"):
        files.extend(sorted(base.rglob("*.md")))
    files.append(ROOT / "STYLE_GUIDE.md")
    return [path for path in files if path.is_file()]


def l2_markdown_files() -> list[Path]:
    return sorted((ROOT / "Livre-II").rglob("*.md"))


def previous_nonempty(lines: list[str], index: int) -> int | None:
    cursor = index - 1
    while cursor >= 0:
        if lines[cursor].strip():
            return cursor
        cursor -= 1
    return None


def parse_fences(lines: list[str]) -> list[Fence]:
    result: list[Fence] = []
    current: tuple[int, str, int, str, str, str] | None = None
    h2 = ""
    h3 = ""
    in_front_matter = bool(lines and lines[0].strip() == "---")
    for index, line in enumerate(lines):
        stripped = line.strip()
        if index > 0 and in_front_matter and stripped == "---":
            in_front_matter = False
            continue
        if not in_front_matter:
            if line.startswith("## ") and not line.startswith("### "):
                h2 = line[3:].strip()
                h3 = ""
            elif line.startswith("### "):
                h3 = line[4:].strip()
        match = FENCE_RE.match(stripped)
        if not match:
            continue
        fence = match.group("fence")
        lang = match.group("lang").strip().split()[0].lower() if match.group("lang").strip() else ""
        if current is None:
            current = (index, fence[0], len(fence), lang, h2, h3)
            continue
        start, open_char, open_length, open_lang, open_h2, open_h3 = current
        if fence[0] == open_char and len(fence) >= open_length and not lang:
            result.append(Fence(start, index, open_lang, open_h2, open_h3))
            current = None
    return result


def current_heading(lines: list[str], index: int) -> str:
    cursor = index
    while cursor >= 0:
        value = lines[cursor].strip()
        if value.startswith("#"):
            return value.lstrip("#").strip().lower()
        cursor -= 1
    return ""


def set_marker(lines: list[str], fence_start: int, marker: str) -> None:
    previous = previous_nonempty(lines, fence_start)
    if previous is not None and MARKER_RE.match(lines[previous].strip()):
        lines[previous] = marker
    else:
        lines[fence_start:fence_start] = [marker, ""]


def marker_for(path: Path, fence: Fence) -> str:
    name = path.name
    lang = fence.lang
    h2 = fence.h2.lower()
    h3 = fence.h3.lower()

    if lang in {"powershell", "pwsh"}:
        return "> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows."
    if lang in {"cmd", "bat", "batch"}:
        return "> **[CMD] Invite de commandes Windows - Exécuter :** utiliser `cmd.exe`."
    if lang in {"bash", "sh", "shell", "zsh"}:
        return "> **[WSL] Terminal WSL/Bash - Exécuter :** utiliser la distribution Linux indiquée."

    if lang == "gdscript":
        if name.startswith("CHAPITRE-01-") and h3 == "15.1 créer le fichier":
            return "> **[VSC] Visual Studio Code - Créer :** `res://src/features/bootstrap/main.gd`."
        if name.startswith("CHAPITRE-02-") and h3 == "31.2 créer `bootstrap_report.gd`":
            return "> **[VSC] Visual Studio Code - Créer :** `res://src/core/diagnostics/bootstrap_report.gd`."
        if name.startswith("CHAPITRE-02-") and h3 == "31.3 utiliser la classe dans `main.gd`":
            return "> **[VSC] Visual Studio Code - Modifier :** `res://src/features/bootstrap/main.gd`."
        return "> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande."

    if lang in {"yaml", "yml"}:
        if name.startswith("CHAPITRE-01-") and h3 == "3.3 politique de version":
            return "> **[VSC] Visual Studio Code - Créer :** `docs/environment/godot-reference.yaml` à la racine du projet."
        return "> **[LECTURE] Exemple YAML - Ne pas créer de fichier sans chemin explicitement indiqué.**"

    if lang == "gitignore":
        return "> **[VSC] Visual Studio Code - Créer ou modifier :** `.gitignore` à la racine du projet."
    if lang == "gitattributes":
        return "> **[VSC] Visual Studio Code - Créer ou modifier :** `.gitattributes` à la racine du projet."
    if lang in {"markdown", "md"} and name.startswith("CHAPITRE-01-") and h3 == "8.3 readme initial":
        return "> **[VSC] Visual Studio Code - Créer :** `README.md` à la racine du projet."

    if lang in {"text", "plaintext", ""} and name.startswith("CHAPITRE-01-"):
        if h3 == "9.2 paramètres de création":
            return "> **[APP] Godot Project Manager - Configurer :** renseigner les paramètres ci-dessous dans **Create New Project**."
        if h3 == "9.3 vérifier les fichiers initiaux":
            return "> **[SORTIE] Résultat attendu - Ne pas saisir :** comparer cette liste avec les fichiers réellement créés."
        if h3 == "14.1 nœud racine":
            return "> **[APP] Godot - Enregistrer :** sauvegarder la scène sous le chemin ci-dessous."
        if h2 == "14. créer la scène principale":
            return "> **[APP] Godot - Créer ou configurer :** utiliser l’arbre de scène et l’Inspector avec les valeurs ci-dessous."
        if h2 == "16. définir la scène principale":
            return "> **[APP] Godot - Configurer :** utiliser **Project Settings > Application > Run > Main Scene** avec la valeur ci-dessous."
        if h3 == "17.1 scène courante":
            return "> **[APP] Godot - Exécuter :** utiliser le raccourci ci-dessous pour lancer la scène courante."
        if h3 == "17.2 projet complet":
            return "> **[APP] Godot - Exécuter :** utiliser le raccourci ci-dessous pour lancer le projet complet."
        if h3 == "17.3 résultat attendu":
            return "> **[SORTIE] Résultat attendu - Ne pas saisir :** comparer avec le panneau **Output** de Godot."
        if h3 == "17.4 arrêter":
            return "> **[APP] Godot - Arrêter :** utiliser le raccourci ci-dessous pour arrêter l’exécution."

    if lang in {"text", "plaintext", "", "console", "output"}:
        if "résultat attendu" in h3 or "résultat attendu" in h2:
            return "> **[SORTIE] Résultat attendu - Ne pas saisir :** comparer avec le résultat obtenu."
        return "> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**"

    if lang == "mermaid":
        return "> **[LECTURE] Diagramme de référence - Ne pas exécuter :** lire le flux représenté."

    return f"> **[LECTURE] Exemple {lang or 'de code'} - Ne pas créer ni exécuter sans instruction explicite.**"


def add_usage_note(lines: list[str]) -> bool:
    if any("Repères d’utilisation" in line for line in lines[:100]):
        return False
    for index, line in enumerate(lines):
        if line.startswith("# "):
            lines[index + 1:index + 1] = ["", USAGE_NOTE]
            return True
    return False


def add_front_matter_field(lines: list[str], key: str, rendered: str) -> bool:
    if not lines or lines[0].strip() != "---":
        return False
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return False
    prefix = f"{key}:"
    for index in range(1, end):
        if lines[index].startswith(prefix):
            if lines[index] != rendered:
                lines[index] = rendered
                return True
            return False
    lines.insert(end, rendered)
    return True


def bump_l2_version(lines: list[str]) -> bool:
    if not lines or lines[0].strip() != "---":
        return False
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return False
    for index in range(1, end):
        if lines[index].startswith("version:"):
            raw = lines[index].split(":", 1)[1].strip().strip('"')
            match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", raw)
            if not match:
                return False
            major, minor, _patch = map(int, match.groups())
            desired = f"{major}.{max(minor, 2)}.0"
            if raw != desired:
                lines[index] = f'version: "{desired}"'
                return True
            return False
    return False


def insert_app_marker(lines: list[str], phrase: str, marker: str) -> bool:
    for index, line in enumerate(lines):
        if phrase not in line:
            continue
        previous = previous_nonempty(lines, index)
        if previous is not None and MARKER_RE.match(lines[previous].strip()):
            return False
        lines[index:index] = [marker, ""]
        return True
    return False


def apply_l2_file(path: Path) -> int:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()
    changed = 0

    if L2_CHAPTER_RE.fullmatch(relative(path)):
        changed += int(add_front_matter_field(lines, "audit-status", 'audit-status: "complete"'))
        changed += int(add_front_matter_field(lines, "audit-date", f'audit-date: "{AUDIT_DATE}"'))
        changed += int(add_front_matter_field(lines, "audit-level", 'audit-level: "static-review"'))
        changed += int(add_front_matter_field(lines, "usage-context-standard", f'usage-context-standard: "{STANDARD_ID}"'))
        changed += int(bump_l2_version(lines))

    changed += int(add_usage_note(lines))

    if path.name.startswith("CHAPITRE-01-"):
        for index, line in enumerate(lines):
            if line.strip() == "Pour chaque projet Godot, enregistrer :":
                lines[index] = "Pour chaque projet Godot, créer le fichier `docs/environment/godot-reference.yaml` et y enregistrer :"
                changed += 1
                break
    if path.name.startswith("CHAPITRE-02-"):
        for index, line in enumerate(lines):
            if line.strip() == "Git peut normaliser les fins de ligne avec `.gitattributes` :":
                lines[index] = "Git peut normaliser les fins de ligne. Dans Visual Studio Code, créer ou compléter `.gitattributes` à la racine du projet :"
                changed += 1
                break

    # Insert or replace markers from the end to avoid shifting subsequent fences.
    for fence in reversed(parse_fences(lines)):
        marker = marker_for(path, fence)
        previous = previous_nonempty(lines, fence.start)
        if previous is not None and MARKER_RE.match(lines[previous].strip()):
            if lines[previous] != marker:
                lines[previous] = marker
                changed += 1
        else:
            lines[fence.start:fence.start] = [marker, ""]
            changed += 1

    if path.name.startswith("CHAPITRE-01-"):
        actions = (
            ("Lorsque le dossier ne contient pas encore `project.godot`", "> **[APP] Godot Project Manager - Interface :** ouvrir le gestionnaire de projets et effectuer l’action décrite."),
            ("Laisser le projet créer le fichier `project.godot`.", "> **[APP] Godot Project Manager - Créer :** valider la création du projet avec les paramètres précédents."),
            ("Créer une nouvelle ressource `Environment`", "> **[APP] Godot - Inspector :** créer et affecter la ressource décrite."),
            ("Créer un `StandardMaterial3D`", "> **[APP] Godot - Inspector :** créer le matériau et régler sa couleur."),
            ("Utiliser les ancres et marges", "> **[APP] Godot - Interface :** régler les ancres et marges dans l’éditeur 2D."),
            ("Déplacer les ressources depuis le dock FileSystem de Godot", "> **[APP] Godot - FileSystem :** effectuer le déplacement depuis le dock de l’éditeur."),
            ("Lancer l’éditeur, exécuter la scène", "> **[APP] Godot - Exécuter :** lancer la scène et vérifier visuellement le résultat."),
        )
        for phrase, marker in actions:
            changed += int(insert_app_marker(lines, phrase, marker))
    elif path.name.startswith("CHAPITRE-02-"):
        changed += int(insert_app_marker(
            lines,
            "Cliquer dans la marge de l’éditeur de script",
            "> **[APP] Godot - Débogueur :** placer le point d’arrêt dans l’éditeur de script.",
        ))

    # Procedural external links need [WEB], except bibliographies/reference lists.
    index = 0
    while index < len(lines):
        line = lines[index]
        if EXTERNAL_LINK_RE.search(line):
            heading = current_heading(lines, index)
            context = " ".join(lines[max(0, index - 4):index + 1]).lower()
            if not any(word in heading for word in REFERENCE_HEADINGS) and any(word in context for word in ACTION_LINK_WORDS):
                previous = previous_nonempty(lines, index)
                if previous is None or not MARKER_RE.match(lines[previous].strip()):
                    lines[index:index] = ["> **[WEB] Navigateur internet - Ouvrir :** utiliser la page officielle indiquée ci-dessous.", ""]
                    changed += 1
                    index += 2
        index += 1

    migrated = "\n".join(lines).rstrip() + "\n"
    if migrated != original:
        path.write_text(migrated, encoding="utf-8", newline="\n")
    return changed


def audit_file(path: Path) -> list[str]:
    rel = relative(path)
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    for fence in parse_fences(lines):
        previous = previous_nonempty(lines, fence.start)
        if previous is None or not MARKER_RE.match(lines[previous].strip()):
            errors.append(f"{rel}:{fence.start + 1}: bloc `{fence.lang or 'text'}` sans repère d’utilisation")
    if L2_CHAPTER_RE.fullmatch(rel):
        front = "\n".join(lines[:100])
        for expected in (
            'audit-status: "complete"',
            f'audit-date: "{AUDIT_DATE}"',
            'audit-level: "static-review"',
            f'usage-context-standard: "{STANDARD_ID}"',
        ):
            if expected not in front:
                errors.append(f"{rel}: métadonnée absente ou incorrecte : {expected}")
        if "Repères d’utilisation" not in "\n".join(lines[:120]):
            errors.append(f"{rel}: légende des repères absente")
    return errors


def apply() -> int:
    total = 0
    changed_files = 0
    for path in l2_markdown_files():
        changes = apply_l2_file(path)
        total += changes
        changed_files += int(changes > 0)
    print(f"Fichiers Livre II modifiés : {changed_files}")
    print(f"Corrections appliquées : {total}")
    return 0


def check() -> int:
    errors: list[str] = []
    files = all_markdown_files()
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
