#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md"
AUDIT = ROOT / "Livre-II/QA/AUDIT-CHAPITRES-01-02.md"


def replace_once(text: str, old: str, new: str) -> str:
    if old not in text:
        raise RuntimeError(f"Passage introuvable: {old[:100]!r}")
    return text.replace(old, new, 1)


text = CHAPTER.read_text(encoding="utf-8")
text = replace_once(text, 'version: "1.2.0"', 'version: "1.3.0"')

anchor = "Une bibliothèque Python ne peut pas être importée directement dans un script GDScript.\n\n## 3. Un fichier GDScript est une classe"
insert = """Une bibliothèque Python ne peut pas être importée directement dans un script GDScript.

### 2.1 Méthode de lecture des exemples

Ce chapitre adopte désormais une règle stricte : lors de la première apparition d’une syntaxe, le texte explique **chaque mot-clé, symbole, nom et accès important**. Un exemple n’est pas seulement une recette à recopier ; il doit pouvoir être lu de gauche à droite.

Repères syntaxiques essentiels :

| Élément | Signification |
|---|---|
| `var` | déclare une variable, c’est-à-dire un nom associé à une valeur qui pourra évoluer ; |
| `const` | déclare une constante dont la référence ne doit pas être réaffectée ; |
| `nom: Type` | impose le type accepté par la variable ou le paramètre ; |
| `=` | affecte la valeur située à droite au nom situé à gauche ; |
| `:=` | affecte une valeur et demande à Godot d’en déduire le type statique ; |
| `func` | déclare une fonction ; |
| `(parametre: Type)` | déclare les données que la fonction attend lorsqu’elle est appelée ; |
| `-> Type` | indique le type de la valeur renvoyée par la fonction ; |
| `.` | accède à une propriété ou appelle une méthode d’un objet ; |
| `[index]` | lit ou modifie un élément d’un tableau ou la valeur associée à une clé de dictionnaire ; |
| `[]` | construit un tableau ; |
| `{}` | construit un dictionnaire ; |
| `%` après une chaîne | remplace les emplacements réservés d’une chaîne formatée ; |
| une ligne indentée | appartient au bloc ouvert par la ligne précédente terminée par `:`. |

Les noms comme `health`, `target`, `metrics` ou `key` ne sont pas des mots réservés de GDScript. Ce sont des noms choisis par le programmeur. Ils doivent décrire leur rôle.

## 3. Un fichier GDScript est une classe"""
text = replace_once(text, anchor, insert)

old = """```gdscript
var target: Node3D
var camera: Camera3D
var report: BootstrapReport
```

### 10.5 Pourquoi typer le code du guide"""
new = """```gdscript
var target: Node3D
var camera: Camera3D
var report: BootstrapReport
```

Lecture détaillée :

- `var` déclare une variable membre du script. Chaque instance de la classe possède son propre emplacement pour cette variable.
- `target`, `camera` et `report` sont les noms choisis pour ces variables. Ils pourraient être différents, mais des noms descriptifs facilitent la lecture.
- le caractère `:` introduit une **annotation de type** ; il signifie « cette variable ne pourra contenir qu’une valeur compatible avec le type qui suit » ;
- `Node3D` est une classe native de Godot représentant un nœud placé dans l’espace 3D. Une valeur assignée à `target` pourra donc fournir des propriétés comme `position`, `rotation` ou `scale` ;
- `Camera3D` est une classe native plus spécialisée. Elle hérite de `Node3D`, mais ajoute le comportement d’une caméra qui affiche un point de vue dans un `Viewport` ;
- `BootstrapReport` est une classe personnalisée créée plus loin dans le chapitre avec `class_name BootstrapReport`. Le type devient alors utilisable dans les annotations comme une classe native ;
- aucune valeur n’est placée après `=` dans ces trois déclarations. Comme ces types héritent d’`Object`, leur valeur initiale est `null` tant qu’une instance réelle ne leur a pas été affectée.

Exemple d’affectation ultérieure :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** observer comment une référence réelle remplace la valeur initiale `null`.

```gdscript
@onready var camera: Camera3D = $CameraRig/Camera3D
```

Dans cette ligne, `$CameraRig/Camera3D` recherche le nœud à ce chemin dans la scène. `@onready` reporte cette recherche jusqu’au moment où le nœud est entré dans l’arbre de scène et où ses enfants sont disponibles.

### 10.5 Pourquoi typer le code du guide"""
text = replace_once(text, old, new)

old = """```gdscript
for actor_name: String in actor_names:
\tprint(actor_name)
```

Avec index :"""
new = """```gdscript
for actor_name: String in actor_names:
\tprint(actor_name)
```

Lecture détaillée :

- `for` ouvre une boucle ;
- `actor_name` est une variable locale créée pour l’itération courante ;
- `: String` indique que chaque élément attendu est une chaîne ;
- `in actor_names` demande de prendre successivement chaque élément du tableau `actor_names` ;
- `print(actor_name)` affiche l’élément courant ;
- à chaque tour, `actor_name` reçoit la valeur suivante jusqu’à la fin du tableau.

Avec index :"""
text = replace_once(text, old, new)

old = """```gdscript
for index: int in actor_names.size():
\tprint(\"%d : %s\" % [index, actor_names[index]])
```

### 13.4 Références et duplication"""
new = """```gdscript
for index: int in actor_names.size():
\tprint(\"%d : %s\" % [index, actor_names[index]])
```

Lecture détaillée :

- `actor_names.size()` renvoie le nombre d’éléments du tableau ; dans une boucle `for`, cet entier produit les index de `0` à `size() - 1` ;
- `index` contient donc la position courante ;
- `%d` est un emplacement réservé pour un entier décimal ;
- `%s` est un emplacement réservé converti en texte ;
- l’opérateur `%` applique les valeurs du tableau `[index, actor_names[index]]` aux deux emplacements, dans le même ordre ;
- `actor_names[index]` lit l’élément situé à la position `index` ;
- avec `index == 0` et le premier nom `Aster`, le texte affiché est `0 : Aster`.

### 13.4 Références et duplication"""
text = replace_once(text, old, new)

old = """```gdscript
for key: StringName in metrics:
\tprint(\"%s = %s\" % [key, metrics[key]])
```

### 17.4 Boucle `while`"""
new = """```gdscript
for key: StringName in metrics:
\tprint(\"%s = %s\" % [key, metrics[key]])
```

Lecture détaillée :

- `metrics` est le dictionnaire déclaré précédemment avec le type `Dictionary[StringName, float]` ; ses clés sont donc des `StringName` et ses valeurs des nombres `float` ;
- parcourir directement un dictionnaire avec `for ... in metrics` parcourt ses **clés** ;
- `key` est une variable locale. À chaque tour, elle contient une clé différente, par exemple `&\"marker_height\"` puis `&\"load_time_ms\"` ;
- `: StringName` rend explicite le type de cette clé ;
- `metrics[key]` utilise la clé courante entre crochets pour récupérer la valeur correspondante dans le dictionnaire ;
- la chaîne `\"%s = %s\"` est un modèle contenant deux emplacements `%s` ; chaque `%s` signifie « convertir la prochaine valeur en texte et l’insérer ici » ;
- l’opérateur `%` situé entre la chaîne et le tableau effectue le formatage ; il ne représente pas ici un pourcentage ni un reste de division ;
- `[key, metrics[key]]` fournit les deux valeurs dans l’ordre : la clé remplace le premier `%s`, puis sa valeur remplace le second ;
- si `key` vaut `&\"load_time_ms\"` et `metrics[key]` vaut `12.5`, `print()` affiche `load_time_ms = 12.5`.

Une forme plus longue, mais parfois plus claire pour débuter, produit le même résultat :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** même boucle décomposée en variables intermédiaires.

```gdscript
for key: StringName in metrics:
\tvar value: float = metrics[key]
\tvar line: String = \"%s = %s\" % [key, value]
\tprint(line)
```

### 17.4 Boucle `while`"""
text = replace_once(text, old, new)

old = """```gdscript
func add(a: int, b: int) -> int:
\treturn a + b
```

### 18.2 Paramètre par défaut"""
new = """```gdscript
func add(a: int, b: int) -> int:
\treturn a + b
```

Lecture détaillée :

- `func` annonce une fonction ;
- `add` est son nom ;
- les parenthèses contiennent les paramètres reçus par la fonction ;
- `a: int` et `b: int` déclarent deux paramètres entiers ; ces noms n’existent que pendant l’appel de la fonction ;
- `-> int` promet que la fonction renverra un entier ;
- le caractère `:` final ouvre le bloc indenté de la fonction ;
- `return` arrête la fonction et renvoie la valeur située à sa droite ;
- `a + b` additionne les deux arguments reçus.

Ainsi, `add(2, 3)` associe `2` à `a`, `3` à `b` et renvoie `5`.

### 18.2 Paramètre par défaut"""
text = replace_once(text, old, new)

old = """```gdscript
func format_actor_name(actor_name: String, prefix: String = \"\") -> String:
\tif prefix.is_empty():"""
new = """```gdscript
func format_actor_name(actor_name: String, prefix: String = \"\") -> String:
\tif prefix.is_empty():"""
# Keep code, append explanation after complete block via next replacement.
text = replace_once(text, old, new)

anchor2 = """\treturn \"%s %s\" % [prefix, actor_name]
```

### 18.3 Paramètres nommés"""
insert2 = """\treturn \"%s %s\" % [prefix, actor_name]
```

Lecture détaillée :

- `actor_name` est obligatoire, car aucune valeur n’est indiquée après son type ;
- `prefix: String = \"\"` possède la valeur par défaut `\"\"`, une chaîne vide ; l’appelant peut donc omettre ce second argument ;
- `prefix.is_empty()` appelle la méthode `is_empty()` de la chaîne stockée dans `prefix` ;
- si le préfixe est vide, la fonction renvoie directement `actor_name` ;
- sinon, `\"%s %s\" % [prefix, actor_name]` construit une chaîne contenant le préfixe, un espace et le nom ;
- `format_actor_name(\"Aster\")` renvoie `Aster` ;
- `format_actor_name(\"Aster\", \"Capitaine\")` renvoie `Capitaine Aster`.

### 18.3 Paramètres nommés"""
text = replace_once(text, anchor2, insert2)

CHAPTER.write_text(text, encoding="utf-8", newline="\n")

audit = AUDIT.read_text(encoding="utf-8")
audit = replace_once(audit, 'version: "2.0.0"', 'version: "2.1.0"')
audit_anchor = "| L2-AUD-021 | majeure | Le vérificateur sémantique et le rapporteur de couverture ne contrôlaient pas encore le Livre II. | Extension des deux outils et ajout de métriques par chapitre. |"
audit_new = audit_anchor + "\n| L2-AUD-022 | majeure | Plusieurs exemples introduisaient des symboles, types ou accès sans les expliquer suffisamment pour un débutant. | Ajout d’une méthode de lecture syntaxique et de décompositions ligne par ligne. |\n| L2-AUD-023 | majeure | Les exemples de classes natives/personnalisées et de parcours de dictionnaire supposaient des connaissances préalables. | Explication détaillée de `Node3D`, `Camera3D`, `BootstrapReport`, `%s`, `%`, `key` et `metrics[key]`. |"
audit = replace_once(audit, audit_anchor, audit_new)
audit = replace_once(audit, "Le chapitre couvre toujours correctement la syntaxe, le typage, les collections, fonctions, classes, annotations, cycle de vie, erreurs, débogage et l’exercice `BootstrapReport`.", "Le chapitre couvre la syntaxe, le typage, les collections, fonctions, classes, annotations, cycle de vie, erreurs, débogage et l’exercice `BootstrapReport`. La nouvelle lecture a renforcé l’explication de chaque symbole et de chaque rôle au moment de sa première utilisation.")
AUDIT.write_text(audit, encoding="utf-8", newline="\n")

print("Chapitre 2 approfondi et audit mis à jour.")
