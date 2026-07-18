from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md"
REPORT = ROOT / "dist/AUDIT-GDSCRIPT-CH02.md"

text = CHAPTER.read_text(encoding="utf-8")
errors: list[str] = []

# Remove front matter for content checks.
body = text
if body.startswith("---\n"):
    end = body.find("\n---\n", 4)
    if end >= 0:
        body = body[end + 5 :]

# Headings must be unique as complete headings.
headings = [line.strip() for line in body.splitlines() if re.match(r"^#{2,6} ", line)]
for heading, count in Counter(headings).items():
    if count > 1:
        errors.append(f"Titre dupliqué ({count} occurrences) : {heading}")

# Exact duplicate multi-line code blocks, excluding deliberately tiny syntax fragments.
blocks = re.findall(r"```[^\n]*\n(.*?)\n```", body, flags=re.S)
normalized_blocks: list[str] = []
for block in blocks:
    normalized = "\n".join(line.rstrip() for line in block.strip().splitlines())
    significant = [line for line in normalized.splitlines() if line.strip()]
    if len(significant) >= 3 and len(normalized) >= 60:
        normalized_blocks.append(normalized)
for block, count in Counter(normalized_blocks).items():
    if count > 1:
        preview = block.splitlines()[0][:80]
        errors.append(f"Bloc de code dupliqué ({count} occurrences) : {preview}")

# Exact duplicate prose paragraphs, ignoring standard context labels, lists and tables.
without_code = re.sub(r"```.*?```", "", body, flags=re.S)
paragraphs = re.split(r"\n\s*\n", without_code)
normalized_paragraphs: list[str] = []
for paragraph in paragraphs:
    compact = " ".join(line.strip() for line in paragraph.splitlines()).strip()
    if (
        len(compact) >= 140
        and not compact.startswith(("> **[", "|", "- ", "1. ", "2. ", "3. "))
        and not compact.startswith("#")
    ):
        normalized_paragraphs.append(compact.casefold())
for paragraph, count in Counter(normalized_paragraphs).items():
    if count > 1:
        errors.append(f"Paragraphe dupliqué ({count} occurrences) : {paragraph[:100]}…")

required_phrases = {
    "progression anti-doublon": "### 2.2 Progression sans répétition",
    "vocabulaire fonctionnel": "### 18.0 Vocabulaire indispensable",
    "distinction paramètre/argument": "Un **paramètre** appartient à la définition",
    "fonction privée détaillée": "_normalize_label(\"  Aster  \")",
    "fonction statique détaillée": "MathRules` n’est pas une variable",
    "await détaillé": "arrête temporairement cette fonction sans bloquer toute l’application",
    "delta rendu détaillé": "`delta` représente le nombre de secondes écoulées",
    "delta physique détaillé": "durée du pas physique",
    "formatage avancé": "`%%` produit le caractère `%` visible",
    "dictionnaire détaillé": "`metrics[key]` utilise la clé courante",
}
for label, phrase in required_phrases.items():
    if phrase not in text:
        errors.append(f"Explication pédagogique manquante : {label}")

sections_requiring_detail = [
    "### 10.3 Paramètres et valeur de retour",
    "### 17.2 Parcourir un tableau",
    "### 17.3 Parcourir un dictionnaire",
    "### 17.4 Boucle `while`",
    "### 17.5 `break` et `continue`",
    "### 18.1 Fonction simple",
    "### 18.2 Paramètre par défaut",
    "### 18.3 Fonction privée conventionnelle",
    "### 18.4 Fonction statique",
    "### 18.6 `await` et fonctions suspendues",
    "### 22.4 `_process(delta)`",
    "### 22.5 `_physics_process(delta)`",
]
for index, heading in enumerate(sections_requiring_detail):
    start = text.find(heading)
    if start < 0:
        errors.append(f"Section obligatoire absente : {heading}")
        continue
    next_start = len(text)
    for candidate in re.finditer(r"\n#{2,3} ", text[start + len(heading) :]):
        next_start = start + len(heading) + candidate.start()
        break
    section = text[start:next_start]
    if "Lecture détaillée" not in section and "Lecture ciblée" not in section:
        errors.append(f"Décomposition pédagogique absente : {heading}")

REPORT.parent.mkdir(parents=True, exist_ok=True)
lines = [
    "# Audit automatique — GDScript chapitre 2",
    "",
    f"- Titres contrôlés : **{len(headings)}**",
    f"- Blocs de code significatifs contrôlés : **{len(normalized_blocks)}**",
    f"- Paragraphes longs contrôlés : **{len(normalized_paragraphs)}**",
    f"- Erreurs : **{len(errors)}**",
    "",
    "## Résultat",
    "",
]
lines.extend([f"- {error}" for error in errors] or ["- Aucun doublon exact ni manque pédagogique détecté."])
REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(REPORT.read_text(encoding="utf-8"))
if errors:
    sys.exit(1)
