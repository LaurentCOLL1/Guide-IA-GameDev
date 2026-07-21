#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE_COMMIT = "2dd2dc3d00b914a9199e200c00ff2bf463730e3e"
ERROR_MARKER = "<!-- qa:error-correction-section -->"
CODE_MARKER = "<!-- qa:code-explanation -->"
STRUCTURED = "**Explication structurée du bloc :**"

CHAPTERS = {
    17: "Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md",
    18: "Livre-II/CHAPITRE-18-Combat.md",
    19: "Livre-II/CHAPITRE-19-Competences-et-pouvoirs.md",
    20: "Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md",
    21: "Livre-II/CHAPITRE-21-Economie.md",
    22: "Livre-II/CHAPITRE-22-Monde-vivant-et-simulation-ecologique.md",
    23: "Livre-II/CHAPITRE-23-Politique-factions-et-justice.md",
    24: "Livre-II/CHAPITRE-24-Construction-et-gestion-de-domaines.md",
    25: "Livre-II/CHAPITRE-25-Narration-quetes-codex-et-connaissances.md",
    26: "Livre-II/CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md",
}

NOW = datetime.now(ZoneInfo("Europe/Paris")).replace(microsecond=0).isoformat()
TODAY = NOW[:10]


def git_show(path: str) -> str:
    result = subprocess.run(
        ["git", "show", f"{BASE_COMMIT}:{path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return result.stdout


def heading_match(line: str) -> tuple[int, str] | None:
    match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
    if not match:
        return None
    return len(match.group(1)), match.group(2)


def section_bounds(text: str, marker: str) -> tuple[int, int]:
    lines = text.splitlines(keepends=True)
    marker_index = next(
        (index for index, line in enumerate(lines) if line.strip() == marker),
        None,
    )
    if marker_index is None:
        raise RuntimeError(f"Marqueur absent: {marker}")

    start = None
    level = None
    in_fence = False
    fence_char = ""
    fence_len = 0
    for index, line in enumerate(lines[: marker_index + 1]):
        stripped = line.strip()
        fence = re.match(r"^(`{3,}|~{3,})", stripped)
        if fence:
            token = fence.group(1)
            if not in_fence:
                in_fence = True
                fence_char = token[0]
                fence_len = len(token)
            elif token[0] == fence_char and len(token) >= fence_len:
                in_fence = False
            continue
        if in_fence:
            continue
        match = heading_match(line.rstrip("\n"))
        if match and match[0] >= 2:
            start = index
            level = match[0]

    if start is None or level is None:
        raise RuntimeError(f"Titre parent introuvable pour {marker}")

    in_fence = False
    fence_char = ""
    fence_len = 0
    end = len(lines)
    for index in range(start + 1, len(lines)):
        stripped = lines[index].strip()
        fence = re.match(r"^(`{3,}|~{3,})", stripped)
        if fence:
            token = fence.group(1)
            if not in_fence:
                in_fence = True
                fence_char = token[0]
                fence_len = len(token)
            elif token[0] == fence_char and len(token) >= fence_len:
                in_fence = False
            continue
        if in_fence:
            continue
        match = heading_match(lines[index].rstrip("\n"))
        if match and match[0] <= level:
            end = index
            break

    return sum(len(line) for line in lines[:start]), sum(len(line) for line in lines[:end])


def restore_error_section(current: str, historical: str) -> str:
    current_start, current_end = section_bounds(current, ERROR_MARKER)
    old_start, old_end = section_bounds(historical, ERROR_MARKER)
    restored = historical[old_start:old_end].rstrip() + "\n\n"
    result = current[:current_start] + restored + current[current_end:]
    section = result[current_start : current_start + len(restored)]
    if STRUCTURED in section:
        raise RuntimeError("Une rubrique structurée subsiste dans la section restaurée")
    if section.count("**Pourquoi cet exemple est fautif :**") < 1:
        raise RuntimeError("Explication fautive absente après restauration")
    if section.count("**Pourquoi la correction fonctionne :**") < 1:
        raise RuntimeError("Explication corrigée absente après restauration")
    return result


def bump_patch(version: str) -> str:
    major, minor, patch = [int(value) for value in version.split(".")]
    return f"{major}.{minor}.{patch + 1}"


def replace_frontmatter_value(text: str, key: str, value: str) -> str:
    pattern = re.compile(rf'^({re.escape(key)}:\s*)"?([^"\n]+)"?\s*$', re.MULTILINE)
    match = pattern.search(text)
    if not match:
        raise RuntimeError(f"Clé front matter absente: {key}")
    rendered = f'{match.group(1)}"{value}"'
    return text[: match.start()] + rendered + text[match.end() :]


def chapter_version(text: str) -> str:
    match = re.search(r'^version:\s*"([^"]+)"\s*$', text, re.MULTILINE)
    if not match:
        raise RuntimeError("Version du chapitre absente")
    return match.group(1)


def extract_error_section(text: str) -> str:
    start, end = section_bounds(text, ERROR_MARKER)
    return text[start:end]


def metrics(text: str) -> dict[str, int]:
    section = extract_error_section(text)
    return {
        "lines": len(text.splitlines()),
        "headings": sum(1 for line in text.splitlines() if re.match(r"^#{1,6}\s+", line)),
        "blocks": text.count("```") // 2,
        "markers": text.count(CODE_MARKER),
        "cases": len(re.findall(r"^###\s+\d+\.\d+\s+", section, re.MULTILINE)),
        "faulty": section.count("**Pourquoi cet exemple est fautif :**"),
        "corrected": section.count("**Pourquoi la correction fonctionne :**"),
    }


def update_metric_line(text: str, labels: tuple[str, ...], value: int) -> str:
    for label in labels:
        pattern = re.compile(
            rf"(^-\s*{re.escape(label)}\s*:\s*\*\*)\d+(\*\*\s*;?)",
            re.MULTILINE | re.IGNORECASE,
        )
        if pattern.search(text):
            return pattern.sub(rf"\g<1>{value}\g<2>", text, count=1)
    return text


def update_audit(number: int, path: Path, version: str, data: dict[str, int]) -> None:
    text = path.read_text(encoding="utf-8")
    text = replace_frontmatter_value(text, "version", version)
    if re.search(r"^chapter-version:", text, re.MULTILINE):
        text = replace_frontmatter_value(text, "chapter-version", version)
    text = replace_frontmatter_value(text, "audit-date", NOW)
    text = replace_frontmatter_value(text, "last-verified", NOW)

    text = update_metric_line(text, ("lignes finales",), data["lines"])
    text = update_metric_line(text, ("titres Markdown",), data["headings"])
    text = update_metric_line(text, ("blocs de code ou de données",), data["blocks"])
    text = update_metric_line(text, ("marqueurs d’explication",), data["markers"])
    text = update_metric_line(text, ("cas d’erreurs détaillés",), data["cases"])
    text = update_metric_line(text, ("contre-exemples expliqués", "exemples fautifs expliqués"), data["faulty"])
    text = update_metric_line(text, ("corrections expliquées", "exemples corrigés expliqués"), data["corrected"])

    note = (
        "\nLes sections pédagogiques d’erreurs conservent leur séquence sémantique "
        "directe : symptôme, exemple fautif, explication du défaut, exemple corrigé "
        "et explication de la correction. Les rubriques générales de restructuration "
        "ne sont pas appliquées à ces deux explications, afin d’éviter répétitions, "
        "sous-titres intermédiaires et commentaires génériques.\n"
    )
    decision_heading = re.search(r"^##\s+\d+\.\s+Décision\s*$", text, re.MULTILINE)
    if note.strip() not in text:
        if decision_heading:
            text = text[: decision_heading.start()] + note + "\n" + text[decision_heading.start() :]
        else:
            text = text.rstrip() + "\n" + note

    path.write_text(text, encoding="utf-8")


def replace_yaml_scalar(text: str, key: str, value: str, indent: int = 0) -> str:
    prefix = " " * indent
    pattern = re.compile(rf"^{re.escape(prefix + key)}:\s*.*$", re.MULTILINE)
    rendered = f"{prefix}{key}: {value}"
    if pattern.search(text):
        return pattern.sub(rendered, text, count=1)
    return text


def update_proof(path: Path, version: str, data: dict[str, int]) -> None:
    text = path.read_text(encoding="utf-8")
    text = replace_yaml_scalar(text, "status", "pending")
    text = replace_yaml_scalar(text, "validation-date", f"'{TODAY}'")
    text = replace_yaml_scalar(text, "validated-base-commit", "4e0c7152a76aefc93ccf7a115ccbee23e5965385")
    text = replace_yaml_scalar(text, "validated-head-commit", "null")
    text = replace_yaml_scalar(text, "commit", "null", indent=2)
    text = replace_yaml_scalar(text, "conclusion", "pending", indent=2)

    chapter_pattern = re.compile(r"(^chapter:\n(?:^[ ]{2}.+\n)*?^[ ]{2}version:\s*).+$", re.MULTILINE)
    if chapter_pattern.search(text):
        text = chapter_pattern.sub(rf"\g<1>{version}", text, count=1)

    metric_map = {
        "chapter-lines": data["lines"],
        "chapter-headings": data["headings"],
        "chapter-code-and-data-blocks": data["blocks"],
        "code-explanation-markers": data["markers"],
        "detailed-error-cases": data["cases"],
        "faulty-examples-explained": data["faulty"],
        "corrected-examples-explained": data["corrected"],
    }
    for key, value in metric_map.items():
        text = replace_yaml_scalar(text, key, str(value), indent=2)

    text = replace_yaml_scalar(text, "blocking-errors", "null", indent=2)
    text = replace_yaml_scalar(text, "warnings", "null", indent=2)

    text = re.sub(r"(^  validate-chapters-without-pdf:\n    run-id:)\s*.*$", r"\1 null", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"(^  validate-chapters-without-pdf:\n    run-id: null\n    conclusion:)\s*.*$", r"\1 pending", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"(^  validate-usage-contexts:\n    run-id:)\s*.*$", r"\1 null", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"(^  validate-usage-contexts:\n    run-id: null\n    conclusion:)\s*.*$", r"\1 pending", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"(^    id:)\s*.*$", r"\1 null", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"(^    digest:)\s*.*$", r"\1 null", text, count=1, flags=re.MULTILINE)

    semantic_fields = (
        "  structured-non-error-code-explanations: true\n"
        "  semantic-error-correction-sequence: true\n"
        "  error-explanations-directly-after-markers: true\n"
        "  structured-error-explanation-wrapper-absent: true\n"
    )
    insertion_anchor = "  pdf-produced:"
    if "semantic-error-correction-sequence:" not in text and insertion_anchor in text:
        text = text.replace(insertion_anchor, semantic_fields + insertion_anchor, 1)

    path.write_text(text, encoding="utf-8")


def update_continuity(versions: dict[int, str]) -> None:
    path = ROOT / "CONTINUITE-PROJET.md"
    text = path.read_text(encoding="utf-8")
    text = re.sub(r'^version:\s*"[^"]+"', 'version: "3.26.2"', text, count=1, flags=re.MULTILINE)
    text = re.sub(r'^last-updated:\s*"[^"]+"', f'last-updated: "{NOW}"', text, count=1, flags=re.MULTILINE)

    rule_anchor = (
        "Les explications de code des chapitres 17 et suivants conservent toute "
        "information pédagogique déjà publiée, la reclassent sous un point explicite "
        "et créent un point technique supplémentaire lorsqu’aucune rubrique standard "
        "ne convient. Les sections Solo/Studio restent en Markdown ordinaire sauf "
        "représentation littérale d’un format."
    )
    exception = (
        "\n\nException obligatoire : dans une section sémantique d’erreurs, "
        "d’anti-patterns, de diagnostics ou de corrections, les marqueurs placés "
        "après les deux exemples sont suivis directement par `Pourquoi cet exemple "
        "est fautif` puis `Pourquoi la correction fonctionne`. La rubrique "
        "`Explication structurée du bloc`, les points génériques et toute répétition "
        "intermédiaire sont interdits dans ces sous-cas."
    )
    if exception.strip() not in text:
        if rule_anchor not in text:
            raise RuntimeError("Ancre de continuité introuvable")
        text = text.replace(rule_anchor, rule_anchor + exception, 1)

    for number, version in versions.items():
        pattern = re.compile(rf"(^-\s*chapitre\s+{number}\s*:\s*version\s+`)[^`]+(`\s*;)", re.MULTILINE | re.IGNORECASE)
        text = pattern.sub(rf"\g<1>{version}\g<2>", text, count=1)

    journal = (
        f"### {NOW} — correction sémantique des sections d’erreurs\n\n"
        "- chapitres 17 à 26 : sections d’erreurs restaurées depuis leur version "
        "antérieure à la restructuration générale ;\n"
        "- explications fautives et corrigées replacées directement après leur "
        "marqueur, sans sous-titre structuré ni rubrique parasite ;\n"
        "- formulations historiques conservées, sans perte de sens ;\n"
        "- protocole et contrôle automatique renforcés pour distinguer explication "
        "générale et séquence sémantique d’erreur/correction ;\n"
        "- audits et preuves QA remis en attente de validation ;\n"
        "- aucun test runtime revendiqué et aucun PDF construit.\n\n"
    )
    marker = "## 27. Journal\n\n"
    if marker not in text:
        raise RuntimeError("Journal de continuité introuvable")
    if "correction sémantique des sections d’erreurs" not in text:
        text = text.replace(marker, marker + journal, 1)

    path.write_text(text, encoding="utf-8")


def update_protocol() -> None:
    path = ROOT / "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
    text = path.read_text(encoding="utf-8")
    text = re.sub(r'^version:\s*"([^"]+)"', lambda m: f'version: "{bump_patch(m.group(1))}"', text, count=1, flags=re.MULTILINE)
    text = re.sub(r'^last-verified:\s*"[^"]+"', f'last-verified: "{NOW}"', text, count=1, flags=re.MULTILINE)

    anchor = (
        "Une ligne autonome `Correction` ou `Différence` n’est pas exigée lorsque "
        "son contenu est déjà intégré à ces deux explications. Le but est d’éviter "
        "la répétition sans supprimer l’analyse de l’invariant violé puis rétabli."
    )
    addition = (
        "\n\nDans ces sous-cas, Q1.1.3 ne s’applique pas sous la forme d’une rubrique "
        "`Explication structurée du bloc`. Après chaque marqueur "
        "`<!-- qa:code-explanation -->`, la première ligne non vide est directement "
        "`Pourquoi cet exemple est fautif` ou `Pourquoi la correction fonctionne`, "
        "selon le bloc. Aucun sous-titre intermédiaire, aucune liste de rubriques "
        "générales et aucune reformulation répétitive ne sont ajoutés. Les "
        "explications historiques pertinentes sont conservées telles quelles."
    )
    if addition.strip() not in text:
        if anchor not in text:
            raise RuntimeError("Ancre Q1.2 introuvable")
        text = text.replace(anchor, anchor + addition, 1)

    path.write_text(text, encoding="utf-8")


def main() -> None:
    versions: dict[int, str] = {}
    for number, relative in CHAPTERS.items():
        path = ROOT / relative
        current = path.read_text(encoding="utf-8")
        historical = git_show(relative)
        restored = restore_error_section(current, historical)

        old_version = chapter_version(restored)
        new_version = bump_patch(old_version)
        restored = replace_frontmatter_value(restored, "version", new_version)
        restored = replace_frontmatter_value(restored, "last-verified", NOW)
        restored = replace_frontmatter_value(restored, "audit-date", NOW)
        path.write_text(restored, encoding="utf-8")

        data = metrics(restored)
        if data["cases"] != data["faulty"] or data["cases"] != data["corrected"]:
            raise RuntimeError(f"Chapitre {number}: cas={data['cases']} fautifs={data['faulty']} corrigés={data['corrected']}")
        update_audit(number, ROOT / f"Livre-II/QA/AUDIT-CHAPITRE-{number}.md", new_version, data)
        update_proof(ROOT / f"Livre-II/QA/VALIDATION-FINALE-CHAPITRE-{number}.yaml", new_version, data)
        versions[number] = new_version

    update_continuity(versions)
    update_protocol()

    print("Sections d’erreurs restaurées et documents QA remis en attente.")
    for number, version in versions.items():
        print(f"chapitre {number}: {version}")


if __name__ == "__main__":
    main()
