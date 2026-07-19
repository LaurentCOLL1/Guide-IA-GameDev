from __future__ import annotations

from pathlib import Path
import re
import unicodedata

TODAY = "2026-07-20"
MARKER = "<!-- qa:code-explanation -->"

CHAPTERS = {
    15: Path("Livre-II/CHAPITRE-15-Relations-sociales.md"),
    16: Path("Livre-II/CHAPITRE-16-Famille-et-generations.md"),
}
AUDITS = {
    15: Path("Livre-II/QA/AUDIT-CHAPITRE-15.md"),
    16: Path("Livre-II/QA/AUDIT-CHAPITRE-16.md"),
}
EVIDENCE = {
    15: Path("Livre-II/QA/VALIDATION-FINALE-CHAPITRE-15.yaml"),
    16: Path("Livre-II/QA/VALIDATION-FINALE-CHAPITRE-16.yaml"),
}

GENERIC_ROLE_PATTERNS = (
    "regroupe les opérations nécessaires à",
    "illustre la règle technique de",
    "illustre concrètement la règle présentée dans",
    "sert à illustrer concrètement",
    "sert à présenter la structure attendue pour",
    "présente les données attendues pour",
    "décrit la structure attendue pour",
)

SYNTAX_REMINDER = (
    " Les annotations après `:` typent les paramètres ; "
    "l’annotation après `->` impose le résultat que l’appelant doit gérer."
)

REFERENCE_RULES = {
    15: [
        (("nom affiché", "identité", "clé"), ("identifier une relation dirigée",)),
        (("symétr", "perception inverse"), ("une relation est dirigée",)),
        (("booléen", "amitié"), ("une vue mutuelle est calculée",)),
        (("borne", "delta", "axe"), ("représenter les axes sociaux",)),
        (("cause", "provenance"), ("cause", "changement social")),
        (("heure système", "tick"), ("tick", "horodatage logique")),
        (("historique",), ("historique",)),
        (("collection", "tableau interne"), ("dépôt", "repository")),
        (("voisin", "nœuds"), ("requête", "voisinage")),
        (("paires", "n²"), ("création", "à la demande")),
        (("décod", "conversion"), ("décoder", "codec")),
        (("validation complète", "appliquer avant"), ("restauration", "préparation")),
        (("ia",), ("ia", "service local")),
    ],
    16: [
        (("nom affiché", "identité"), ("identité", "characterid")),
        (("nœud actif", "scène"), ("architecture", "graphe familial")),
        (("filiation", "parent"), ("filiation dirigée",)),
        (("cycle", "ascendance"), ("cycle", "ascendance")),
        (("dépassement", "parcours"), ("parcours", "borné")),
        (("union", "paire"), ("union", "paire canonique")),
        (("heure système", "intervalle", "tick"), ("valeur temporelle", "intervalle logique")),
        (("collection", "tableau interne"), ("graphe", "lecture défensive")),
        (("charger", "validation complète", "appliquer"), ("restauration", "graphe candidat", "codec")),
        (("ia",), ("ia", "commande validée")),
        (("succession", "politique"), ("frontière", "succession")),
    ],
}


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one occurrence, got {count}")
    return text.replace(old, new, 1)


def set_frontmatter(text: str, key: str, value: str) -> str:
    pattern = re.compile(rf'(?m)^{re.escape(key)}: .+$')
    match = pattern.search(text)
    if not match:
        raise RuntimeError(f"front matter key missing: {key}")
    return text[: match.start()] + f'{key}: "{value}"' + text[match.end() :]


def sentence(text: str) -> str:
    value = text.strip()
    if not value:
        return value
    value = value[0].lower() + value[1:] if value[0].isupper() else value
    return value if value.endswith((".", "!", "?", ";")) else value + "."


def slugify(title: str) -> str:
    value = unicodedata.normalize("NFKD", title.lower())
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = re.sub(r"[`*_]", "", value)
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"\s+", "-", value).strip("-")
    return value


def headings_before(text: str, limit: int) -> list[tuple[int, str, str]]:
    result: list[tuple[int, str, str]] = []
    for match in re.finditer(r"(?m)^(#{2,4})\s+(.+)$", text[:limit]):
        title = match.group(2).strip()
        result.append((len(match.group(1)), title, slugify(title)))
    return result


def nearest_heading(text: str, position: int) -> str:
    matches = list(re.finditer(r"(?m)^(#{2,4})\s+(.+)$", text[:position]))
    return matches[-1].group(2).strip() if matches else ""


def choose_reference(chapter: int, case_title: str, candidates: list[tuple[int, str, str]]) -> tuple[str, str] | None:
    lowered = case_title.lower()
    target_terms: tuple[str, ...] | None = None
    for triggers, targets in REFERENCE_RULES[chapter]:
        if any(trigger in lowered for trigger in triggers):
            target_terms = targets
            break
    if target_terms is None:
        return None
    for _level, title, slug in reversed(candidates):
        title_lower = title.lower()
        if any(term in title_lower for term in target_terms):
            return title, slug
    return None


def add_error_references(text: str, chapter: int) -> tuple[str, int]:
    error_heading = re.search(r"(?m)^##\s+.*(?:Erreurs fréquentes|Anti-patterns|Pièges).*$", text, re.IGNORECASE)
    if not error_heading:
        return text, 0
    candidates = headings_before(text, error_heading.start())
    pattern = re.compile(
        r"(?m)^(###\s+(?P<title>[^\n]+))\n\n(?!> \*\*À relire)(?=\*\*Symptôme ou risque :\*\*)"
    )
    added = 0

    def callback(match: re.Match[str]) -> str:
        nonlocal added
        reference = choose_reference(chapter, match.group("title"), candidates)
        if reference is None:
            return match.group(0)
        title, slug = reference
        added += 1
        return f'{match.group(1)}\n\n> **À relire :** [§ {title}](#{slug}).\n\n'

    return pattern.sub(callback, text), added


def extract_last(pattern: str, source: str) -> str:
    matches = list(re.finditer(pattern, source, re.MULTILINE))
    return matches[-1].group(1).strip() if matches else ""


def transform_explanations(text: str, chapter: int) -> tuple[str, dict[str, int]]:
    metrics = {
        "blocks": 0,
        "placements_removed": 0,
        "syntax_reminders_removed": 0,
        "generic_roles_removed": 0,
        "faulty_simplified": 0,
        "corrected_simplified": 0,
    }
    pattern = re.compile(
        r"(?P<code>```(?P<lang>[^\n]*)\n.*?\n```)\n"
        r"<!-- qa:code-explanation -->\n\n"
        r"\*\*Explication détaillée du bloc :\*\*\n\n"
        r"(?P<bullets>(?:- \*\*[^\n]+\n)+)",
        re.DOTALL,
    )

    def callback(match: re.Match[str]) -> str:
        metrics["blocks"] += 1
        before = text[max(0, match.start() - 2200) : match.start()]
        heading = nearest_heading(text, match.start())
        subsection_start = before.rfind("\n### ")
        local = before[subsection_start:] if subsection_start >= 0 else before
        label_window = before[-420:].lower()
        faulty = "exemple fautif" in label_window or "ne pas utiliser" in label_window
        corrected = "exemple corrigé" in label_window

        prefix = match.group("code") + "\n" + MARKER + "\n\n**Explication détaillée du bloc :**\n\n"

        if faulty:
            symptom = extract_last(r"\*\*Symptôme ou risque :\*\*\s*([^\n]+)", local)
            if not symptom:
                symptom = f"l’extrait viole la règle métier rappelée dans « {heading} »"
            metrics["faulty_simplified"] += 1
            return prefix + f"- **Pourquoi cet exemple est fautif :** {sentence(symptom)}\n"

        if corrected:
            correction = extract_last(r"\*\*Correction :\*\*\s*([^\n]+)", local)
            after = text[match.end() : match.end() + 900]
            difference_match = re.search(r"\*\*Différence :\*\*\s*([^\n]+)", after)
            difference = difference_match.group(1).strip() if difference_match else ""
            parts = [sentence(value) for value in (correction, difference) if value]
            explanation = " ".join(parts) or f"elle rétablit l’invariant présenté dans « {heading} »."
            metrics["corrected_simplified"] += 1
            return prefix + f"- **Pourquoi la correction fonctionne :** {explanation}\n"

        output: list[str] = []
        for line in match.group("bullets").splitlines():
            if line.startswith("- **Emplacement :**"):
                metrics["placements_removed"] += 1
                continue
            if SYNTAX_REMINDER in line:
                line = line.replace(SYNTAX_REMINDER, "")
                metrics["syntax_reminders_removed"] += 1
            if line.startswith("- **Rôle :**") and any(pattern_text in line for pattern_text in GENERIC_ROLE_PATTERNS):
                metrics["generic_roles_removed"] += 1
                continue
            output.append(line)
        if not output:
            raise RuntimeError(f"chapter {chapter}: explanation became empty near {heading}")
        return prefix + "\n".join(output) + "\n"

    transformed = pattern.sub(callback, text)
    marker_count = transformed.count(MARKER)
    if metrics["blocks"] != marker_count:
        raise RuntimeError(
            f"chapter {chapter}: parsed {metrics['blocks']} blocks but found {marker_count} markers"
        )
    return transformed, metrics


def refine_chapter(chapter: int, path: Path) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    text = set_frontmatter(text, "version", "1.2.0")
    text = set_frontmatter(text, "last-verified", TODAY)
    old_note = "> **Explications de code :** enrichies bloc par bloc selon la porte QA Q1.1."
    new_note = "> **Explications de code :** contextualisées bloc par bloc selon la porte QA Q1.1, sans répéter le chemin ou les rappels généraux de syntaxe."
    text = replace_once(text, old_note, new_note, f"chapter {chapter} explanation note")
    convention = (
        "\n> **Convention de lecture :** la consigne `[VSC]` placée avant un bloc porte déjà son chemin canonique ; "
        "l’explication ne le répète pas. Les annotations GDScript `:` et `->` sont présentées au "
        "[chapitre 2](CHAPITRE-02-Fondamentaux-de-GDScript.md) et ne sont rappelées ici que lorsqu’un choix "
        "de type ou de retour demande une attention particulière.\n"
    )
    text = text.replace(new_note + "\n", new_note + convention, 1)
    text, refs = add_error_references(text, chapter)
    text, metrics = transform_explanations(text, chapter)
    metrics["references_added"] = refs

    forbidden = [
        "- **Emplacement :**",
        "Les annotations après `:` typent les paramètres",
        "regroupe les opérations nécessaires à",
        "illustre la règle technique de",
    ]
    for phrase in forbidden:
        if phrase in text:
            raise RuntimeError(f"chapter {chapter}: forbidden repetitive phrase remains: {phrase}")

    path.write_text(text, encoding="utf-8")
    metrics["lines"] = len(text.splitlines())
    return metrics


def update_protocol() -> None:
    path = Path("Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md")
    text = path.read_text(encoding="utf-8")
    text = set_frontmatter(text, "version", "1.7.0")
    text = set_frontmatter(text, "last-verified", TODAY)
    old = """Pour chaque bloc significatif, vérifier explicitement :

1. son rôle et la raison de sa présence ;
2. le fichier et le chemin où le placer, ou le contexte dans lequel il est seulement lu ;
3. les entrées, paramètres, types, valeurs par défaut et dépendances utilisées ;
4. les sorties, valeurs de retour, erreurs, signaux et effets de bord ;
5. le déroulement des instructions importantes, ligne par ligne ou par groupes cohérents ;
6. les opérateurs, conversions, conditions et appels non évidents ;
7. les préconditions, invariants et postconditions protégés ;
8. le résultat attendu et la manière de le vérifier ;
9. les variantes raisonnables, limites et erreurs fréquentes pour un débutant ;
10. le lien avec le bloc précédent, le bloc suivant et l’architecture générale.

Une explication peut être placée avant ou après le bloc, mais elle doit être immédiatement identifiable. Pour un exemple fautif, elle doit aussi expliquer précisément pourquoi il échoue ou devient dangereux. Pour un exemple corrigé, elle doit montrer quelle modification rétablit l’invariant.
"""
    new = """Pour chaque bloc significatif, vérifier explicitement, selon ce que le bloc exige réellement :

1. son rôle uniquement lorsque cette formulation ajoute une information propre au code ;
2. son emplacement seulement lorsqu’il n’est pas déjà donné par la consigne `[VSC]` ou par le contexte adjacent ;
3. les entrées, paramètres, types, valeurs par défaut et dépendances qui demandent une explication ;
4. les sorties, valeurs de retour, erreurs, signaux et effets de bord ;
5. le déroulement des instructions importantes, ligne par ligne ou par groupes cohérents ;
6. les opérateurs, conversions, conditions et appels non évidents ;
7. les préconditions, invariants et postconditions protégés ;
8. le résultat attendu et la manière de le vérifier ;
9. les variantes raisonnables, limites et erreurs fréquentes pour un débutant ;
10. le lien avec l’architecture générale lorsqu’il éclaire réellement l’extrait.

Une explication peut être placée avant ou après le bloc, mais elle doit être immédiatement identifiable. Elle ne répète ni le chemin déjà affiché avant le code, ni une règle générale de syntaxe déjà présentée dans un chapitre de référence. Une rubrique `Rôle` qui reformule seulement le titre de la section est supprimée ; elle est conservée lorsqu’elle nomme un contrat, une fonction, une transformation ou une responsabilité concrète.

Dans une section d’erreurs, d’anti-patterns, de pièges ou de corrections, le format privilégié est plus court : `Pourquoi cet exemple est fautif` sous le contre-exemple et `Pourquoi la correction fonctionne` sous la version corrigée. Un renvoi vers une section ou un chapitre antérieur peut être placé avant le code fautif lorsqu’il évite de répéter une règle déjà établie.
"""
    text = replace_once(text, old, new, "protocol Q1.1")
    path.write_text(text, encoding="utf-8")


def collapse_duplicate_lines(text: str, phrase: str) -> str:
    lines = text.splitlines()
    seen = False
    output: list[str] = []
    for line in lines:
        if line.strip() == phrase:
            if seen:
                continue
            seen = True
        output.append(line)
    return "\n".join(output) + "\n"


def update_audit(chapter: int, metrics: dict[str, int]) -> None:
    path = AUDITS[chapter]
    text = path.read_text(encoding="utf-8")
    text = set_frontmatter(text, "version", "1.2.0")
    text = set_frontmatter(text, "chapter-version", "1.2.0")
    text = collapse_duplicate_lines(
        text,
        "La seconde lecture a aussi corrigé la détection des `static func`, les contre-exemples nommés « mauvaise pratique » et les formulations génériques de résultat attendu.",
    )
    text = re.sub(r"(?m)^- `version: 1\.0\.0` ;$", "- `version: 1.2.0` ;", text, count=1)
    addendum = f"""
## Addendum {TODAY} — concision et contextualisation des explications

La passe précédente était complète mais trop répétitive. Cette correction éditoriale applique les règles suivantes aux **{metrics['blocks']} blocs** du chapitre {chapter} :

- {metrics['placements_removed']} rubriques `Emplacement` supprimées parce que le chemin est déjà fourni avant le code ;
- {metrics['syntax_reminders_removed']} rappels généraux sur `:` et `->` supprimés des blocs et remplacés par une convention unique renvoyant au chapitre 2 ;
- {metrics['generic_roles_removed']} rubriques `Rôle` supprimées parce qu’elles reformulaient seulement le titre de la section ;
- {metrics['faulty_simplified']} contre-exemples réduits à une explication précise de leur faute ;
- {metrics['corrected_simplified']} corrections réduites à la raison concrète de leur fonctionnement ;
- {metrics['references_added']} renvois contextuels ajoutés avant des erreurs lorsque le chapitre avait déjà établi la règle concernée.

Les rôles qui nomment un contrat, une classe, une fonction ou une responsabilité concrète sont conservés. La décision reste `static-review` : aucune exécution Godot supplémentaire n’est revendiquée.
"""
    if "concision et contextualisation des explications" not in text:
        text = text.rstrip() + "\n" + addendum
    path.write_text(text, encoding="utf-8")


def update_evidence(chapter: int, metrics: dict[str, int]) -> None:
    path = EVIDENCE[chapter]
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"(?m)^status: complete$", "status: pending-ci", text, count=1)
    text = re.sub(r"(?m)^validation-date: .+$", f"validation-date: {TODAY}", text, count=1)
    text = re.sub(r"(?m)^  version: 1\.1\.0$", "  version: 1.2.0", text, count=1)
    text = re.sub(r"(?m)^  chapter-lines: \d+$", f"  chapter-lines: {metrics['lines']}", text, count=1)
    section = f"""
code-explanation-style-refinement:
  policy: QA-Q1.1-concise
  chapter: {chapter}
  explanation-blocks-reviewed: {metrics['blocks']}
  repeated-location-lines-removed: {metrics['placements_removed']}
  repeated-syntax-reminders-removed: {metrics['syntax_reminders_removed']}
  generic-role-lines-removed: {metrics['generic_roles_removed']}
  faulty-explanations-simplified: {metrics['faulty_simplified']}
  corrected-explanations-simplified: {metrics['corrected_simplified']}
  contextual-references-added: {metrics['references_added']}
  runtime-executed: false
  ci-status: pending
"""
    if "code-explanation-style-refinement:" in text:
        text = re.sub(r"\ncode-explanation-style-refinement:\n.*\Z", "\n" + section.lstrip(), text, flags=re.DOTALL)
    else:
        text = text.rstrip() + "\n\n" + section.lstrip()
    path.write_text(text, encoding="utf-8")


def update_governance(metrics: dict[int, dict[str, int]]) -> None:
    index_path = Path("Livre-II/index.md")
    index = index_path.read_text(encoding="utf-8")
    index = set_frontmatter(index, "version", "1.11.0")
    index = index.replace(
        "expliqué bloc par bloc et audité au niveau static-review",
        "expliqué bloc par bloc sans répétitions éditoriales et audité au niveau static-review",
    )
    index_path.write_text(index, encoding="utf-8")

    roadmap_path = Path("ROADMAP.md")
    roadmap = roadmap_path.read_text(encoding="utf-8")
    anchor = "- [x] Audits et preuves QA corrigés des chapitres 15 et 16 fermés avant le chapitre 17."
    item = "- [x] Explications des chapitres 15 et 16 rendues concises : chemins et syntaxe non répétés, rôles spécifiques, erreurs au format fautif/correction."
    if item not in roadmap:
        roadmap = replace_once(roadmap, anchor, anchor + "\n" + item, "roadmap explanation style")
    roadmap_path.write_text(roadmap, encoding="utf-8")

    continuity_path = Path("CONTINUITE-PROJET.md")
    continuity = continuity_path.read_text(encoding="utf-8")
    continuity = set_frontmatter(continuity, "version", "3.17.4")
    continuity = continuity.replace("- chapitre 15 : version `1.1.0` ;", "- chapitre 15 : version `1.2.0` ;", 1)
    continuity = continuity.replace("- chapitre 16 : version `1.1.0` ;", "- chapitre 16 : version `1.2.0` ;", 1)
    old = "- audits et preuves QA révisés en version `1.1.0` ;"
    new = "- audits et preuves QA révisés en version `1.2.0` ;\n- chemins, rappels généraux de syntaxe et rôles purement redondants retirés des explications ;\n- sections d’erreurs simplifiées autour de la faute et de la correction, avec renvois contextuels lorsque pertinents ;"
    continuity = replace_once(continuity, old, new, "continuity explanation summary")
    journal_anchor = "## 27. Journal\n"
    entry = f"""## 27. Journal

### {TODAY} — version 3.17.4

- correction éditoriale des explications de code des chapitres 15 et 16 ;
- suppression des rubriques `Emplacement` lorsque le chemin précède déjà le bloc ;
- suppression des rappels répétés sur les annotations `:` et `->` ;
- conservation des rôles uniquement lorsqu’ils apportent une responsabilité concrète ;
- simplification des exemples fautifs et corrigés ;
- ajout de renvois contextuels avant certaines erreurs ;
- chapitres, audits et preuves QA portés en version `1.2.0` ;
- aucun PDF construit et aucun test runtime revendiqué.
"""
    continuity = replace_once(continuity, journal_anchor, entry, "continuity journal")
    continuity_path.write_text(continuity, encoding="utf-8")


metrics_by_chapter: dict[int, dict[str, int]] = {}
for chapter, chapter_path in CHAPTERS.items():
    metrics_by_chapter[chapter] = refine_chapter(chapter, chapter_path)

update_protocol()
for chapter in CHAPTERS:
    update_audit(chapter, metrics_by_chapter[chapter])
    update_evidence(chapter, metrics_by_chapter[chapter])
update_governance(metrics_by_chapter)

metrics_path = Path("tmp_ch15_ch16_explanation_style_metrics.txt")
metrics_path.write_text(
    "\n".join(
        f"chapter {chapter}: " + ", ".join(f"{key}={value}" for key, value in metrics.items())
        for chapter, metrics in metrics_by_chapter.items()
    )
    + "\n",
    encoding="utf-8",
)
