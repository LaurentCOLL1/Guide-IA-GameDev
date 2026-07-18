from pathlib import Path
import re
from collections import Counter

path = Path('Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md')
text = path.read_text(encoding='utf-8')
text = text.replace('version: "1.3.0"', 'version: "1.4.0"', 1)
if 'pedagogical-audit-report:' not in text:
    text = text.replace('audit-level: "static-review"\n', 'audit-level: "static-review"\npedagogical-audit-report: "Livre-II/QA/AUDIT-CHAPITRE-02-PEDAGOGIQUE.md"\n', 1)

replacements = {
'''```gdscript
func clamp_health(value: int, maximum: int) -> int:
\treturn clampi(value, 0, maximum)
```

Une fonction qui ne renvoie rien utilise `void` :''': '''```gdscript
func clamp_health(value: int, maximum: int) -> int:
\treturn clampi(value, 0, maximum)
```

Lecture détaillée :

- `clamp_health` est le nom de la fonction : il annonce qu’elle limite une valeur de santé ;
- `value: int` reçoit la valeur à contrôler et `maximum: int` la borne supérieure ;
- ces paramètres sont locaux à la fonction et n’existent que pendant son appel ;
- `-> int` garantit un résultat entier ;
- `clampi(value, 0, maximum)` reçoit trois arguments : valeur, minimum et maximum ;
- `return` termine la fonction et transmet le résultat à l’appelant ;
- `clamp_health(-8, 100)` renvoie `0`, `clamp_health(45, 100)` renvoie `45` et `clamp_health(130, 100)` renvoie `100`.

Exemple d’appel : `var safe_health: int = clamp_health(130, 100)`. Après l’appel, `safe_health` vaut `100`.

Une fonction qui ne renvoie rien utilise `void` :''',
'''```gdscript
for warning: String in warnings:
\tpush_warning(warning)
```

### 17.3 Parcourir un dictionnaire''': '''```gdscript
for warning: String in warnings:
\tpush_warning(warning)
```

Lecture détaillée :

- `warnings` est la collection parcourue ;
- `warning` est une variable locale qui reçoit un élément différent à chaque tour ;
- `: String` impose une chaîne ;
- `in warnings` demande de prendre tous les éléments dans l’ordre ;
- `push_warning(warning)` envoie la chaîne courante au système d’avertissements de Godot ;
- la variable `warning` cesse d’exister à la fin de la boucle.

### 17.3 Parcourir un dictionnaire''',
'''```gdscript
func _normalize_label(value: String) -> String:
\treturn value.strip_edges().to_lower()
```

GDScript ne rend pas cette méthode strictement privée. Le préfixe `_` communique l’intention.''': '''```gdscript
func _normalize_label(value: String) -> String:
\treturn value.strip_edges().to_lower()
```

Lecture détaillée :

- `_normalize_label` commence par `_` pour signaler une méthode interne ;
- `value: String` reçoit le texte ;
- `strip_edges()` retire les espaces aux extrémités ;
- le point `.` appelle ensuite `to_lower()` sur le résultat précédent ;
- `to_lower()` convertit les lettres en minuscules ;
- `_normalize_label("  PLAYER  ")` renvoie `"player"`.

GDScript ne rend pas cette méthode strictement privée. Le préfixe `_` communique l’intention.''',
'''```gdscript
static func is_valid_percentage(value: float) -> bool:
\treturn value >= 0.0 and value <= 1.0
```

Appel :''': '''```gdscript
static func is_valid_percentage(value: float) -> bool:
\treturn value >= 0.0 and value <= 1.0
```

Lecture détaillée :

- `static` rattache la fonction à la classe plutôt qu’à une instance ;
- `value: float` est le nombre à vérifier ;
- `-> bool` annonce une réponse `true` ou `false` ;
- `>= 0.0` vérifie la borne basse et `<= 1.0` la borne haute ;
- `and` exige que les deux comparaisons soient vraies ;
- le résultat est vrai pour `0.5`, faux pour `-0.1` ou `1.2`.

Appel :''',
'''```gdscript
func wait_one_frame() -> void:
\tawait get_tree().process_frame
\tprint("Image suivante")
```

Une fonction utilisant `await` rend la suite de son exécution asynchrone.''': '''```gdscript
func wait_one_frame() -> void:
\tawait get_tree().process_frame
\tprint("Image suivante")
```

Lecture détaillée :

- `get_tree()` récupère le `SceneTree` ;
- `.process_frame` désigne son signal de prochaine image ;
- `await` suspend cette fonction sans bloquer tout le moteur ;
- `print()` s’exécute seulement après la reprise ;
- `-> void` indique qu’aucune valeur métier n’est renvoyée.

Une fonction utilisant `await` rend la suite de son exécution asynchrone.''',
'''```gdscript
class_name BootstrapReport
extends RefCounted
```

Godot enregistre `BootstrapReport` comme type global du projet.''': '''```gdscript
class_name BootstrapReport
extends RefCounted
```

Lecture détaillée :

- `class_name BootstrapReport` crée un nom global utilisable comme type ;
- `BootstrapReport` est un nom de projet en `PascalCase` ;
- `extends RefCounted` hérite d’un objet dont la durée de vie est gérée par comptage de références ;
- `RefCounted` n’est pas un nœud et ne doit pas être ajouté à l’arbre de scène ;
- ce choix convient à un objet de données temporaire.

Godot enregistre `BootstrapReport` comme type global du projet.''',
'''```gdscript
var health: int = 100:
\tset(value):
\t\thealth = clampi(value, 0, max_health)
\tget:
\t\treturn health

var max_health: int = 100
```

Un accesseur peut garantir un invariant, mais il doit rester léger.''': '''```gdscript
var health: int = 100:
\tset(value):
\t\thealth = clampi(value, 0, max_health)
\tget:
\t\treturn health

var max_health: int = 100
```

Lecture détaillée :

- `health` est une propriété entière initialisée à `100` ;
- le `:` ouvre ses accesseurs ;
- `set(value)` reçoit toute valeur affectée à `health` ;
- `clampi(value, 0, max_health)` applique les deux bornes ;
- l’affectation à `health` dans son propre setter utilise le stockage interne sans rappeler le setter ;
- `get` est exécuté lors d’une lecture et `return health` renvoie la valeur stockée ;
- après `health = 140` avec `max_health == 100`, une lecture renvoie `100`.

Un accesseur peut garantir un invariant, mais il doit rester léger.'''
}
for old, new in replacements.items():
    if old not in text:
        raise RuntimeError('Ancre absente: ' + old.splitlines()[1][:80])
    text = text.replace(old, new, 1)
path.write_text(text, encoding='utf-8')

headings = [re.sub(r'^#{2,6}\s+', '', line).strip() for line in text.splitlines() if re.match(r'^#{2,6}\s+', line)]
dup_headings = [x for x, c in Counter(headings).items() if c > 1]
paragraphs = []
for block in re.split(r'\n\s*\n', text):
    n = re.sub(r'\s+', ' ', block.strip())
    if len(n) >= 140 and not n.startswith('> **[') and not n.startswith('```'):
        paragraphs.append(n)
dup_paragraphs = [x for x, c in Counter(paragraphs).items() if c > 1]
code = []
for m in re.finditer(r'```(?:gdscript|text|bash|powershell|json|yaml|gitattributes)?\n(.*?)\n```', text, re.S):
    n = re.sub(r'[ \t]+$', '', m.group(1), flags=re.M).strip()
    if len(n.splitlines()) >= 5:
        code.append(n)
dup_code = [x for x, c in Counter(code).items() if c > 1]
if dup_headings or dup_paragraphs or dup_code:
    raise RuntimeError(f'Doublons: headings={dup_headings}, paragraphs={len(dup_paragraphs)}, code={len(dup_code)}')

required = ['`metrics[key]` utilise la clé courante', 'l’opérateur `%` situé entre la chaîne et le tableau', '`Node3D` est une classe native de Godot', '`Camera3D` est une classe native plus spécialisée', '`BootstrapReport` est une classe personnalisée', '`clamp_health` est le nom de la fonction', '`static` rattache la fonction à la classe', '`await` suspend cette fonction', '`set(value)` reçoit toute valeur']
missing = [x for x in required if x not in text]
if missing:
    raise RuntimeError('Explications absentes: ' + repr(missing))

Path('Livre-II/QA/AUDIT-CHAPITRE-02-PEDAGOGIQUE.md').write_text('''---
title: "Audit pédagogique — Livre II, chapitre 2"
id: "DOC-L2-QA-CH02-PEDAGOGIE"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
audit-date: "2026-07-18"
audit-level: "static-review"
---

# Audit pédagogique du chapitre 2

## Périmètre

L’audit vérifie les doublons et la profondeur des explications consacrées aux variables, types, paramètres, arguments, valeurs de retour, opérateurs, accès aux collections et fonctions.

## Résultats

- aucun titre de section dupliqué ;
- aucun paragraphe explicatif long dupliqué ;
- aucun bloc de code non trivial dupliqué ;
- les rappels courts restent admis lorsqu’ils accompagnent un exemple différent ;
- les sections sur `Node3D`, `Camera3D`, `BootstrapReport`, les dictionnaires, `%s`, `%`, `key`, `metrics[key]`, les paramètres, les retours, `static`, `await` et les accesseurs possèdent une décomposition détaillée ;
- chaque notion nouvelle est reliée à un exemple d’appel ou à un résultat observable ;
- la validation reste statique jusqu’à l’exécution des extraits dans le projet fil rouge matérialisé.

## Critère permanent

Un exemple introduisant une syntaxe nouvelle doit expliquer les mots-clés, les noms choisis, les types, les opérateurs, la portée, les valeurs reçues, les valeurs renvoyées et le résultat observable.
''', encoding='utf-8')
