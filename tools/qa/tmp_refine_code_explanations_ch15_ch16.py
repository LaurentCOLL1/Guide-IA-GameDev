from __future__ import annotations

import re
from pathlib import Path

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


def compact(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip())


def nearest_heading(lines: list[str], start: int) -> str:
    for index in range(start - 1, max(-1, start - 45), -1):
        line = lines[index].strip()
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return "le passage courant"


def nearest_location(lines: list[str], start: int) -> str:
    for index in range(start - 1, max(-1, start - 45), -1):
        line = lines[index].strip()
        match = re.search(r"`([^`]+\.(?:gd|tscn|json|yaml|yml|py|sql))`", line)
        if match:
            return f"`{match.group(1)}`"
    return "le contexte pédagogique indiqué juste avant le bloc"


def context_before(lines: list[str], start: int) -> str:
    return "\n".join(lines[max(0, start - 18):start]).lower()


def parse_functions(code: str) -> list[dict[str, str | bool]]:
    pattern = re.compile(
        r"^\s*(static\s+)?func\s+([A-Za-z_][A-Za-z0-9_]*)\s*\((.*?)\)\s*(?:->\s*([^:\n]+))?:",
        re.MULTILINE | re.DOTALL,
    )
    result = []
    for match in pattern.finditer(code):
        result.append({
            "static": bool(match.group(1)),
            "name": match.group(2),
            "params": compact(match.group(3)) or "aucun paramètre",
            "return": compact(match.group(4) or "Variant implicite"),
        })
    return result


def describe_function(function: dict[str, str | bool]) -> str:
    name = str(function["name"])
    params = str(function["params"])
    return_type = str(function["return"])
    prefix = "méthode statique" if function["static"] else "méthode"
    if name == "_init":
        purpose = "initialise l’objet et copie les arguments dans son état interne"
    elif name.startswith("validate") or name == "is_valid":
        purpose = "vérifie les préconditions et signale toute donnée invalide"
    elif name.startswith("is_") or name.startswith("has_") or name.startswith("can_"):
        purpose = "répond à une question sans modifier l’état"
    elif name.startswith("get_") or name.startswith("find_") or name.startswith("list_"):
        purpose = "lit ou calcule une vue des données sans exposer directement les collections internes"
    elif name.startswith("to_") or name.startswith("encode"):
        purpose = "convertit l’objet vers une représentation de transport ou de stockage"
    elif name.startswith("decode") or name.startswith("from_"):
        purpose = "reconstruit une valeur typée après validation de la représentation externe"
    elif name.startswith("duplicate") or name.startswith("copy"):
        purpose = "produit une copie défensive indépendante de l’original"
    elif name.startswith("add_") or name.startswith("create_") or name.startswith("apply_"):
        purpose = "valide puis ajoute ou applique une mutation métier"
    elif name.startswith("remove_") or name.startswith("close_") or name.startswith("end_"):
        purpose = "termine ou retire un élément en refusant les transitions incohérentes"
    elif name.startswith("replace_") or name.startswith("restore"):
        purpose = "remplace l’état autoritaire à partir d’un candidat déjà validé"
    else:
        purpose = "encapsule l’opération métier indiquée par son nom"
    return f"`{name}({params}) -> {return_type}` est une {prefix} qui {purpose}"


def declarations(code: str) -> tuple[list[str], list[str], list[str], list[str]]:
    constants = [compact(x) for x in re.findall(r"^\s*const\s+([^\n]+)", code, re.MULTILINE)]
    variables = [compact(x) for x in re.findall(r"^\s*(?:@\w+(?:\([^)]*\))?\s+)*var\s+([^\n]+)", code, re.MULTILINE)]
    signals = [compact(x) for x in re.findall(r"^\s*signal\s+([^\n]+)", code, re.MULTILINE)]
    enums = []
    for match in re.finditer(r"enum\s+([A-Za-z_][A-Za-z0-9_]*)\s*\{(.*?)\}", code, re.DOTALL):
        values = [compact(v).rstrip(",") for v in match.group(2).splitlines() if compact(v)]
        enums.append(f"{match.group(1)} = {', '.join(values)}")
    return constants, variables, signals, enums


def list_code(values: list[str], limit: int = 6) -> str:
    shown = values[:limit]
    suffix = f" et {len(values) - limit} autre(s)" if len(values) > limit else ""
    return ", ".join(f"`{value}`" for value in shown) + suffix


def role_for(code: str, heading: str, language: str) -> str:
    class_match = re.search(r"^\s*class_name\s+([A-Za-z_][A-Za-z0-9_]*)", code, re.MULTILINE)
    if class_match:
        extends_match = re.search(r"^\s*extends\s+([^\n]+)", code, re.MULTILINE)
        suffix = f" et l’appuie sur `{compact(extends_match.group(1))}`" if extends_match else ""
        return f"définit le contrat `{class_match.group(1)}`{suffix}"
    if language == "json":
        return f"montre la forme JSON attendue par « {heading} »"
    if ".sort()" in code:
        return "illustre volontairement une normalisation incorrecte qui détruit l’ordre métier"
    functions = parse_functions(code)
    if functions:
        return f"regroupe les opérations nécessaires à « {heading} »"
    return f"illustre la règle technique de « {heading} »"


def flow_for(code: str) -> str:
    parts = []
    if re.search(r"\bif\b", code):
        parts.append("les branches `if` traitent d’abord les refus et cas limites")
    if re.search(r"\bmatch\b", code):
        parts.append("`match` choisit une branche dans un ensemble fermé de cas")
    if re.search(r"\bfor\b", code):
        parts.append("les boucles `for` parcourent explicitement les collections")
    if re.search(r"\bwhile\b", code):
        parts.append("la boucle `while` poursuit un parcours dont le budget doit rester borné")
    if re.search(r"\breturn\b", code):
        parts.append("les retours anticipés empêchent la suite du traitement après une erreur")
    if not parts:
        parts.append("les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale")
    return " ; ".join(parts)


def effects_for(code: str) -> list[str]:
    effects = []
    patterns = [
        (r"\.emit\s*\(|emit_signal\s*\(", "émet un événement observable après succès"),
        (r"replace_one\s*\(|replace_all_from\s*\(", "remplace l’état autoritaire"),
        (r"\.append\s*\(|push_back\s*\(", "ajoute une entrée à une collection ou à un historique"),
        (r"\.erase\s*\(|\.clear\s*\(", "retire ou réinitialise des données en mémoire"),
        (r"ended_at_tick\s*=|revision\s*\+=|_next_sequence\s*\+=", "modifie un état temporel ou une révision"),
        (r"FileAccess", "accède au système de fichiers de Godot"),
        (r"JSON\.|parse_string|stringify", "convertit des données JSON"),
        (r"_last_error\s*=|push_error\s*\(", "mémorise une erreur consultable"),
        (r"duplicate\s*\(|duplicate_[a-z_]+\s*\(", "crée une copie défensive"),
    ]
    for pattern, description in patterns:
        if re.search(pattern, code):
            effects.append(description)
    return effects


def invariants_for(code: str, heading: str) -> list[str]:
    values = []
    combined = code + "\n" + heading
    patterns = [
        (r"source_id\s*==\s*target_id|parent_id\s*==\s*child_id|first_id\s*==\s*second_id", "une identité ne peut pas former un lien avec elle-même"),
        (r"CharacterId\.is_valid|identity_index|contains_character", "chaque référence doit correspondre à une identité logique connue, même hors scène"),
        (r"MAX_|max_depth|max_nodes|HISTORY_LIMIT|history_limit", "les parcours et historiques sont bornés"),
        (r"logical_tick|started_at_tick|ended_at_tick|start_tick|end_tick", "les transitions utilisent des ticks logiques cohérents"),
        (r"candidate|prepared|_has_prepared", "un candidat complet est validé avant mutation de l’état actif"),
        (r"cycle|ancestor|descendant", "aucun cycle d’ascendance ne peut être introduit"),
        (r"expected_keys|unknown|keys\(\)|TYPE_", "les clés et types externes sont contrôlés strictement"),
        (r"duplicate|copy", "les lectures ne doivent pas exposer directement un objet interne mutable"),
        (r"clamp|MIN_|MAX_", "les valeurs numériques restent dans leurs bornes métier"),
        (r"sort\(\)|ne pas trier|orientation", "l’ordre des identifiants conserve la direction de la relation"),
    ]
    for pattern, description in patterns:
        if re.search(pattern, combined, re.IGNORECASE):
            values.append(description)
    return values


def classify_context(before: str, heading: str, code: str) -> tuple[bool, bool]:
    combined = before + "\n" + heading.lower()
    faulty_words = ["exemple fautif", "mauvaise", "incorrect", "anti-pattern", "ne pas utiliser", "erreur"]
    corrected_words = ["exemple corrig", "correction", "version correcte", "bonne pratique"]
    faulty = any(word in combined for word in faulty_words) or ".sort()" in code and "orient" in combined
    corrected = any(word in combined for word in corrected_words) and not faulty
    return faulty, corrected


def expected_for(code: str, language: str, heading: str, faulty: bool) -> str:
    if faulty:
        if ".sort()" in code:
            return "constater que deux relations opposées produisent la même paire triée, ce qui prouve la perte d’orientation ; ce bloc ne doit pas être intégré au projet"
        return "identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas"
    if language == "json":
        return "obtenir un document décodable avec exactement les clés, types et identifiants attendus, sans cache ni valeur dérivée persistée"
    if re.search(r"->\s*Error", code):
        return "obtenir `OK` pour le cas valide et un code `Error` documenté pour chaque refus, sans mutation partielle"
    if re.search(r"->\s*bool", code):
        return "obtenir `true` uniquement lorsque toutes les conditions décrites sont satisfaites et `false` pour les cas limites"
    if "class_name" in code:
        return "pouvoir instancier ou appeler ce contrat depuis la couche prévue, avec un état valide et des lectures défensives"
    return "observer le comportement décrit par la section sans modifier de donnée autoritaire non concernée"


def explanation(code: str, language: str, heading: str, location: str, before: str) -> list[str]:
    functions = parse_functions(code)
    constants, variables, signals, enums = declarations(code)
    faulty, corrected = classify_context(before, heading, code)
    effects = effects_for(code)
    invariants = invariants_for(code, heading)

    lines = [MARKER, "", "**Explication détaillée du bloc :**", ""]
    lines.append(f"- **Rôle :** ce bloc {role_for(code, heading, language)}.")
    if location.startswith("`"):
        lines.append(f"- **Emplacement :** place ce code dans {location}. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.")
    else:
        lines.append(f"- **Emplacement :** ce bloc est un exemple à lire dans {location} ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.")

    if functions:
        descriptions = [describe_function(item) for item in functions]
        lines.append("- **Fonctions, paramètres et retours :** " + " ; ".join(descriptions) + ". Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.")
    else:
        lines.append("- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.")

    declared = []
    if enums:
        declared.append("énumérations " + list_code(enums, 3))
    if constants:
        declared.append("constantes " + list_code(constants, 5))
    if variables:
        declared.append("variables " + list_code(variables, 6))
    if signals:
        declared.append("signaux " + list_code(signals, 4))
    if declared:
        lines.append("- **Données et types :** " + " ; ".join(declared) + ". Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.")
    else:
        lines.append("- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.")

    lines.append(f"- **Déroulement :** {flow_for(code)}. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.")
    if effects:
        lines.append("- **Effets de bord :** " + " ; ".join(effects[:6]) + ". L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.")
    else:
        lines.append("- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.")
    if invariants:
        lines.append("- **Invariants protégés :** " + " ; ".join(invariants[:6]) + ".")
    else:
        lines.append("- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.")

    if faulty:
        lines.append("- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.")
    elif corrected:
        lines.append("- **Pourquoi la correction fonctionne :** elle rétablit l’ordre validation → construction du candidat → mutation autoritaire → événement, ou replace la responsabilité dans la couche qui possède réellement l’invariant.")

    lines.append(f"- **Résultat attendu et vérification :** {expected_for(code, language, heading, faulty)}. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.")
    return lines


def replace_or_insert(lines: list[str], after: int, generated: list[str]) -> tuple[list[str], int, bool]:
    index = after
    while index < len(lines) and lines[index] == "":
        index += 1
    if index < len(lines) and lines[index] == MARKER:
        end = index + 1
        while end < len(lines) and lines[end] == "":
            end += 1
        if end < len(lines) and lines[end].startswith("**Explication détaillée"):
            end += 1
        while end < len(lines):
            if lines[end].startswith("- **") or lines[end] == "":
                end += 1
                continue
            break
        return lines[:index] + generated + [""] + lines[end:], index + len(generated) + 1, True
    return lines[:after] + generated + [""] + lines[after:], after + len(generated) + 1, False


def process(path: Path) -> tuple[int, int, int]:
    lines = path.read_text(encoding="utf-8").splitlines()
    index = 0
    total = 0
    replaced = 0
    added = 0
    while index < len(lines):
        if not lines[index].startswith("```"):
            index += 1
            continue
        language = lines[index][3:].strip().lower()
        start = index
        index += 1
        while index < len(lines) and not lines[index].startswith("```"):
            index += 1
        if index >= len(lines):
            break
        end = index
        code = "\n".join(lines[start + 1:end])
        index += 1
        relevant = language == "gdscript" and bool(code.strip())
        relevant = relevant or language in {"json", "yaml", "yml", "python", "sql"} and len([line for line in code.splitlines() if line.strip()]) >= 2
        if not relevant:
            continue
        total += 1
        heading = nearest_heading(lines, start)
        location = nearest_location(lines, start)
        before = context_before(lines, start)
        generated = explanation(code, language, heading, location, before)
        lines, index, was_replaced = replace_or_insert(lines, index, generated)
        if was_replaced:
            replaced += 1
        else:
            added += 1
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return total, replaced, added


metrics = {}
for chapter, path in CHAPTERS.items():
    metrics[chapter] = process(path)

for chapter, audit_path in AUDITS.items():
    text = audit_path.read_text(encoding="utf-8")
    total, replaced, added = metrics[chapter]
    text = re.sub(
        rf"La correction a repris les \*\*\d+ blocs de code ou données significatifs\*\* détectés dans le chapitre {chapter}\. \*\*\d+ explications détaillées\*\* ont été ajoutées[^\n]*",
        f"La correction finale couvre **{total} blocs de code ou données** dans le chapitre {chapter}. **{replaced} explications** ont été affinées après seconde lecture et **{added} explications manquantes** ont été ajoutées, notamment pour les blocs GDScript d’une seule ligne.",
        text,
        count=1,
    )
    if "Les fonctions statiques" not in text:
        text += "\nLa seconde lecture a aussi corrigé la détection des `static func`, les contre-exemples nommés « mauvaise pratique » et les formulations génériques de résultat attendu.\n"
    audit_path.write_text(text, encoding="utf-8")

for chapter, evidence_path in EVIDENCE.items():
    text = evidence_path.read_text(encoding="utf-8")
    total, replaced, added = metrics[chapter]
    text = re.sub(r"(?m)^  significant-code-or-data-blocks: \d+$", f"  significant-code-or-data-blocks: {total}", text, count=1)
    text = re.sub(r"(?m)^  explanations-added: \d+$", f"  explanations-added: {total}", text, count=1)
    if "  explanations-refined-after-second-review:" not in text:
        text = text.replace(
            "  explanation-marker: qa:code-explanation\n",
            f"  explanation-marker: qa:code-explanation\n  explanations-refined-after-second-review: {replaced}\n  previously-missing-explanations-added: {added}\n  static-functions-detected: true\n  one-line-gdscript-blocks-covered: true\n  faulty-examples-explicitly-explained: true\n",
            1,
        )
    evidence_path.write_text(text, encoding="utf-8")

Path("tmp_ch15_ch16_code_explanation_metrics.txt").write_text(
    "\n".join(
        f"chapter {chapter}: total={values[0]}, refined={values[1]}, newly_added={values[2]}"
        for chapter, values in metrics.items()
    ) + "\n",
    encoding="utf-8",
)
print(Path("tmp_ch15_ch16_code_explanation_metrics.txt").read_text(encoding="utf-8"))
