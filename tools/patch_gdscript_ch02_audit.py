from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md"
AUDIT = ROOT / "Livre-II/QA/AUDIT-CHAPITRES-01-02.md"
WORKFLOW = ROOT / ".github/workflows/validate-volume0.yml"
TEMP_WORKFLOW = ROOT / ".github/workflows/temp-patch-gdscript-ch02.yml"
SELF = Path(__file__)


def replace_section(text: str, heading: str, next_heading: str, body: str) -> str:
    start = text.find(heading)
    if start < 0:
        raise RuntimeError(f"Heading not found: {heading}")
    end = text.find(next_heading, start + len(heading))
    if end < 0:
        raise RuntimeError(f"Next heading not found: {next_heading}")
    return text[:start] + heading + "\n\n" + body.strip() + "\n\n" + text[end:]


text = CHAPTER.read_text(encoding="utf-8")
text = text.replace('version: "1.3.0"', 'version: "1.4.0"', 1)

if "### 2.2 Progression sans répétition" not in text:
    marker = "\n## 3. Un fichier GDScript est une classe\n"
    insertion = r'''
### 2.2 Progression sans répétition

Le chapitre distingue trois niveaux d’explication afin d’éviter les doublons :

1. **première apparition** : définition complète du mot-clé ou du symbole, lecture de gauche à droite et résultat concret ;
2. **réutilisation** : rappel bref et renvoi vers la première explication ;
3. **nouvelle combinaison** : explication uniquement de ce que la combinaison ajoute.

Par exemple, le formatage avec `%s` est décomposé entièrement à la section 17.3. La section 25 ne répète pas cette définition : elle ajoute les variantes `%d`, `%f` et `%%`.

De même, la section 10.3 montre comment le typage s’applique au contrat d’une fonction, tandis que la section 18 définit en détail fonction, méthode, paramètre, argument, valeur par défaut et valeur de retour.
'''
    if marker not in text:
        raise RuntimeError("Insertion marker for section 2.2 not found")
    text = text.replace(marker, "\n" + insertion.strip() + "\n\n## 3. Un fichier GDScript est une classe\n", 1)

text = replace_section(
    text,
    "### 10.3 Paramètres et valeur de retour",
    "### 10.4 Types natifs et classes personnalisées",
    r'''
Cette section montre le **contrat typé** d’une fonction. Le vocabulaire complet est défini à la section 18 pour éviter de répéter deux fois le même cours.

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** observer le contrat typé ; la section 18 détaille les paramètres, arguments et retours.

```gdscript
func clamp_health(value: int, maximum: int) -> int:
	return clampi(value, 0, maximum)
```

Lecture ciblée sur le typage :

- `value: int` impose un entier pour la valeur à limiter ;
- `maximum: int` impose un entier pour la limite haute ;
- `-> int` annonce que le résultat sera également un entier ;
- `clampi(value, 0, maximum)` appelle la fonction native de Godot qui borne `value` entre `0` et `maximum` ;
- l’appel `clamp_health(120, 100)` renvoie `100`, tandis que `clamp_health(-5, 100)` renvoie `0`.

Une fonction qui n’a pas de valeur utile à transmettre à l’appelant utilise `void` :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** observer une fonction qui effectue une action sans produire de valeur de retour.

```gdscript
func reset() -> void:
	print("Réinitialisation")
```

Ici, `reset()` affiche un message mais ne fournit aucune valeur utilisable dans une affectation. Écrire `var result = reset()` n’a donc pas de sens fonctionnel.
''',
)

text = replace_section(
    text,
    "### 17.2 Parcourir un tableau",
    "### 17.3 Parcourir un dictionnaire",
    r'''
> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier le rôle de la collection, de la variable de boucle et de la fonction appelée.

```gdscript
for warning: String in warnings:
	push_warning(warning)
```

Lecture détaillée :

- `warnings` est un tableau de chaînes, par exemple `Array[String]` ;
- `for ... in warnings` demande de traiter ses éléments un par un, dans leur ordre courant ;
- `warning` est une variable locale créée pour la boucle ; à chaque tour, elle reçoit un élément différent ;
- `: String` confirme que chaque élément attendu est une chaîne de caractères ;
- `push_warning(warning)` transmet la chaîne courante au système de diagnostic de Godot ;
- si le tableau contient `"Pilote ancien"` puis `"Mode CPU"`, deux avertissements distincts sont produits.

Le nom singulier `warning` pour un élément et le nom pluriel `warnings` pour la collection rendent la relation immédiatement visible.
''',
)

text = replace_section(
    text,
    "### 17.4 Boucle `while`",
    "### 17.5 `break` et `continue`",
    r'''
> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** observer l’état initial, la condition et la progression qui empêchent une boucle infinie.

```gdscript
var attempts: int = 0

while attempts < 3:
	attempts += 1
```

Lecture détaillée :

- `attempts` mémorise le nombre de tentatives déjà effectuées ;
- la valeur initiale `0` signifie qu’aucune tentative n’a encore eu lieu ;
- `while` répète son bloc tant que l’expression qui suit vaut `true` ;
- `attempts < 3` autorise les passages correspondant aux valeurs `0`, `1` et `2` ;
- `attempts += 1` est une écriture abrégée de `attempts = attempts + 1` ;
- après le troisième passage, `attempts` vaut `3`, la condition devient fausse et la boucle s’arrête.

Une boucle `while` doit toujours posséder une progression observable vers sa condition de sortie. Oublier `attempts += 1` créerait ici une boucle infinie.
''',
)

text = replace_section(
    text,
    "### 17.5 `break` et `continue`",
    "## 18. Fonctions",
    r'''
> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** distinguer le saut vers l’itération suivante de l’arrêt complet de la boucle.

```gdscript
for value: int in values:
	if value < 0:
		continue
	if value > limit:
		break
	process_value(value)
```

Lecture détaillée :

- `values` est la collection parcourue ;
- `value` représente l’élément courant et n’existe que dans le bloc de la boucle ;
- `limit` est une valeur définie avant la boucle et utilisée comme seuil d’arrêt ;
- `continue` abandonne uniquement le tour courant : une valeur négative n’est pas traitée, mais la boucle examine l’élément suivant ;
- `break` quitte entièrement la boucle : dès qu’une valeur dépasse `limit`, aucun élément suivant n’est examiné ;
- `process_value(value)` est un appel de fonction ; la valeur courante devient l’argument transmis à son paramètre ;
- l’ordre des deux tests est important : les valeurs négatives sont ignorées avant la vérification de la limite.
''',
)

if "### 18.0 Vocabulaire indispensable" not in text:
    marker = "## 18. Fonctions\n\n### 18.1 Fonction simple"
    insertion = r'''## 18. Fonctions

### 18.0 Vocabulaire indispensable

| Terme | Définition | Exemple |
|---|---|---|
| fonction | bloc de code nommé que l’on peut appeler ; | `add` |
| méthode | fonction appartenant à une classe ou appelée sur un objet ; | `prefix.is_empty()` |
| paramètre | nom déclaré dans la définition et destiné à recevoir une donnée ; | `a: int` |
| argument | valeur réellement fournie lors d’un appel ; | `2` dans `add(2, 3)` |
| type du paramètre | contrat qui limite les valeurs acceptées ; | `int` |
| valeur par défaut | valeur utilisée lorsque l’argument correspondant est omis ; | `prefix: String = ""` |
| valeur de retour | résultat transmis à l’appelant par `return` ; | `5` renvoyé par `add(2, 3)` |
| type de retour | contrat placé après `->` ; | `-> int` |
| appelant | code qui déclenche la fonction ; | la ligne contenant `add(2, 3)` |
| portée locale | zone où un paramètre ou une variable locale existe ; | le bloc de la fonction |

Un **paramètre** appartient à la définition de la fonction. Un **argument** appartient à un appel précis. Dire « le paramètre vaut 2 » est un raccourci : plus exactement, l’argument `2` est affecté au paramètre `a` pendant cet appel.

### 18.1 Fonction simple'''
    if marker not in text:
        raise RuntimeError("Function section marker not found")
    text = text.replace(marker, insertion, 1)

text = replace_section(
    text,
    "### 18.3 Fonction privée conventionnelle",
    "### 18.4 Fonction statique",
    r'''
> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier le paramètre, la chaîne d’appels et la convention de nommage.

```gdscript
func _normalize_label(value: String) -> String:
	return value.strip_edges().to_lower()
```

Lecture détaillée :

- `_normalize_label` commence par `_` pour signaler qu’elle est destinée à l’usage interne de la classe ; GDScript n’empêche toutefois pas techniquement un autre script de l’appeler ;
- `value: String` est le paramètre obligatoire contenant le texte à normaliser ;
- `value.strip_edges()` crée une chaîne sans espaces inutiles au début ni à la fin ;
- le point `.` appelle une méthode sur la valeur située à gauche ;
- `.to_lower()` est ensuite appelé sur le résultat précédent et convertit les lettres en minuscules ;
- l’enchaînement se lit donc de gauche à droite : prendre `value`, retirer ses espaces externes, puis convertir le résultat en minuscules ;
- `return` transmet la chaîne finale à l’appelant ;
- `_normalize_label("  Aster  ")` renvoie `"aster"`.

Une variable intermédiaire peut rendre la même logique plus facile à déboguer :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** variante décomposée produisant le même résultat.

```gdscript
func _normalize_label(value: String) -> String:
	var trimmed: String = value.strip_edges()
	var normalized: String = trimmed.to_lower()
	return normalized
```
''',
)

text = replace_section(
    text,
    "### 18.4 Fonction statique",
    "### 18.5 Fonction récursive",
    r'''
Une fonction statique appartient à la classe elle-même. Elle ne dépend pas d’une instance ni de ses variables membres.

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** observer le paramètre, le booléen renvoyé et l’appel par le nom de classe.

```gdscript
static func is_valid_percentage(value: float) -> bool:
	return value >= 0.0 and value <= 1.0
```

Lecture détaillée :

- `static func` déclare une fonction appelable sans construire d’objet ;
- `is_valid_percentage` formule une question et son préfixe `is_` annonce naturellement un résultat booléen ;
- `value: float` reçoit le nombre à vérifier ;
- `-> bool` promet soit `true`, soit `false` ;
- `value >= 0.0` vérifie la borne basse ;
- `value <= 1.0` vérifie la borne haute ;
- `and` exige que les deux comparaisons soient vraies ;
- `is_valid_percentage(-0.2)` renvoie `false`, `is_valid_percentage(0.5)` renvoie `true`.

Appel par le nom de la classe :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** `MathRules` représente ici la classe qui déclare la fonction statique.

```gdscript
if MathRules.is_valid_percentage(0.5):
	print("Valeur valide")
```

`MathRules` n’est pas une variable. C’est le type global utilisé comme point d’accès à la fonction statique.
''',
)

text = replace_section(
    text,
    "### 18.6 `await` et fonctions suspendues",
    "## 19. Classes, héritage et `class_name`",
    r'''
`await` suspend la suite de la fonction jusqu’à ce que le signal ou l’objet attendu soit résolu :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** observer ce qui est exécuté avant et après la suspension.

```gdscript
func wait_one_frame() -> void:
	await get_tree().process_frame
	print("Image suivante")
```

Lecture détaillée :

- `wait_one_frame()` ne reçoit aucun paramètre : ses parenthèses sont vides ;
- `-> void` indique qu’elle ne renvoie pas de valeur métier ;
- `get_tree()` renvoie le `SceneTree` auquel appartient le nœud courant ;
- `.process_frame` désigne le signal émis au début de l’image de traitement suivante ;
- `await` arrête temporairement cette fonction sans bloquer toute l’application ;
- la ligne `print()` n’est exécutée qu’après l’émission du signal ;
- le code qui appelle `wait_one_frame()` ne doit pas supposer que les lignes situées après `await` ont déjà été exécutées.

Les temporisations, annulations, retours asynchrones et connexions de signaux seront approfondis au chapitre 3.
''',
)

text = replace_section(
    text,
    "### 22.4 `_process(delta)`",
    "### 22.5 `_physics_process(delta)`",
    r'''
Appelé à chaque image rendue lorsque le traitement est actif.

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** observer le paramètre temporel fourni automatiquement par Godot.

```gdscript
func _process(delta: float) -> void:
	rotation.y += delta
```

Lecture détaillée :

- Godot appelle `_process()` automatiquement ; le programmeur ne choisit pas directement son argument ;
- `delta` représente le nombre de secondes écoulées depuis l’image rendue précédente ;
- son type est `float` parce qu’une durée d’image est généralement une fraction de seconde ;
- à 60 images par seconde, `delta` est proche de `0.0167`, mais sa valeur varie avec les performances ;
- `rotation.y += delta` ajoute cette durée à la rotation autour de l’axe Y ; le mouvement dépend ainsi du temps écoulé plutôt que du nombre d’images ;
- sans multiplication ou addition fondée sur `delta`, une animation progresserait plus vite sur une machine affichant davantage d’images.

Utilisations :

- animation visuelle non physique ;
- interpolation d’interface ;
- effets dépendant du rendu.
''',
)

text = replace_section(
    text,
    "### 22.5 `_physics_process(delta)`",
    "### 22.6 Ordre simplifié",
    r'''
Appelé à fréquence physique fixe, indépendamment de la fréquence d’affichage.

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** transmettre explicitement le paramètre reçu à une fonction spécialisée.

```gdscript
func _physics_process(delta: float) -> void:
	_update_movement(delta)
```

Lecture détaillée :

- Godot fournit automatiquement `delta` à `_physics_process()` ;
- ce `delta` correspond à la durée du pas physique, par exemple environ `1 / 60` seconde avec 60 ticks physiques par seconde ;
- `_update_movement(delta)` appelle une méthode interne et lui transmet la même durée comme argument ;
- dans la définition de `_update_movement`, un paramètre — souvent également nommé `delta` — recevra cet argument ;
- transmettre la durée rend la méthode testable et évite qu’elle dépende implicitement d’une variable globale.

Utilisations :

- déplacement physique ;
- collisions ;
- contrôleurs de personnage ;
- logique devant suivre le pas physique.
''',
)

text = replace_section(
    text,
    "### 25.1 Interpolation avec `%`",
    "### 25.2 Conversion",
    r'''
La section 17.3 explique entièrement le mécanisme `"%s" % valeur`. Cette section ajoute les principaux marqueurs afin d’éviter de répéter la même définition.

| Marqueur | Valeur attendue | Exemple de résultat |
|---|---|---|
| `%s` | valeur convertie en texte | `Aster` |
| `%d` | entier décimal | `42` |
| `%f` | nombre flottant | `3.500000` |
| `%.2f` | flottant limité à deux décimales | `3.50` |
| `%%` | caractère `%` littéral | `75%` |

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** réutiliser le principe de la section 17.3 avec des marqueurs plus précis.

```gdscript
var message := "%s possède %d points et %.1f%% de progression." % [
	actor_name,
	score,
	progress_ratio * 100.0,
]
```

Lecture ciblée :

- `actor_name` remplace `%s` ;
- `score` remplace `%d` et doit être compatible avec un entier ;
- `progress_ratio * 100.0` transforme un ratio comme `0.75` en `75.0` ;
- `%.1f` affiche ce nombre avec une décimale ;
- `%%` produit le caractère `%` visible ;
- l’ordre des valeurs dans le tableau doit correspondre à l’ordre des marqueurs.
''',
)

CHAPTER.write_text(text, encoding="utf-8")

# Create permanent duplicate/pedagogy audit tool.
audit_tool = ROOT / "tools/audit_gdscript_ch02.py"
audit_tool.write_text(r'''from __future__ import annotations

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
''', encoding="utf-8")

# Update audit report.
audit = AUDIT.read_text(encoding="utf-8")
audit = audit.replace('version: "2.1.0"', 'version: "2.2.0"', 1)
if "L2-AUD-024" not in audit:
    audit = audit.replace(
        "| L2-AUD-023 | majeure | Les exemples de classes natives/personnalisées et de parcours de dictionnaire supposaient des connaissances préalables. | Explication détaillée de `Node3D`, `Camera3D`, `BootstrapReport`, `%s`, `%`, `key` et `metrics[key]`. |",
        "| L2-AUD-023 | majeure | Les exemples de classes natives/personnalisées et de parcours de dictionnaire supposaient des connaissances préalables. | Explication détaillée de `Node3D`, `Camera3D`, `BootstrapReport`, `%s`, `%`, `key` et `metrics[key]`. |\n"
        "| L2-AUD-024 | majeure | Le chapitre ne distinguait pas formellement répétition pédagogique et progression. | Ajout d’une règle de première définition, rappel bref et nouvelle combinaison. |\n"
        "| L2-AUD-025 | majeure | Plusieurs fonctions secondaires et paramètres (`value`, `delta`, fonctions statiques ou privées) restaient trop peu décomposés. | Ajout de lectures ligne par ligne, exemples d’appels et résultats concrets. |\n"
        "| L2-AUD-026 | majeure | L’absence de doublons n’était pas démontrée par un contrôle dédié. | Ajout de `tools/audit_gdscript_ch02.py` et exécution permanente dans la CI. |",
        1,
    )
if "### Contrôle dédié des doublons" not in audit:
    audit = audit.replace(
        "### Décision\n\n**Accepté avec réserve runtime.** Les exemples pédagogiques ne sont plus confondus avec les fichiers que le lecteur doit réellement créer.",
        "### Contrôle dédié des doublons\n\nLe chapitre est désormais contrôlé automatiquement pour les titres identiques, les paragraphes longs identiques et les blocs de code multilignes identiques. Les répétitions nécessaires sont remplacées par un renvoi vers la première définition complète.\n\n### Décision\n\n**Accepté avec réserve runtime.** Les fonctions, méthodes, paramètres, arguments, valeurs par défaut et retours sont explicités au niveau débutant ; aucun doublon exact significatif n’est accepté par la CI.",
        1,
    )
AUDIT.write_text(audit, encoding="utf-8")

# Add audit tool to the permanent documentation workflow.
workflow = WORKFLOW.read_text(encoding="utf-8")
if '"tools/audit_gdscript_ch02.py"' not in workflow:
    workflow = workflow.replace(
        '      - ".github/workflows/validate-volume0.yml"\n',
        '      - ".github/workflows/validate-volume0.yml"\n      - "tools/audit_gdscript_ch02.py"\n',
        1,
    )
if "Audit GDScript chapter 2 pedagogy" not in workflow:
    workflow = workflow.replace(
        "      - name: Compile PDF with Pandoc\n",
        "      - name: Audit GDScript chapter 2 pedagogy\n        run: python3 tools/audit_gdscript_ch02.py\n\n      - name: Compile PDF with Pandoc\n",
        1,
    )
if "dist/AUDIT-GDSCRIPT-CH02.md" not in workflow:
    workflow = workflow.replace(
        "            dist/QA-DOCUMENTATION.md\n",
        "            dist/QA-DOCUMENTATION.md\n            dist/AUDIT-GDSCRIPT-CH02.md\n",
        1,
    )
WORKFLOW.write_text(workflow, encoding="utf-8")

# Remove temporary automation from the branch before it is merged.
if TEMP_WORKFLOW.exists():
    TEMP_WORKFLOW.unlink()
if SELF.exists():
    SELF.unlink()
