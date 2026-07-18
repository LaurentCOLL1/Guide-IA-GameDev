---
title: "Livre II — Chapitre 2 : Fondamentaux de GDScript"
id: "DOC-L2-CH02"
status: "reviewed"
version: "1.3.0"
lang: "fr-FR"
book: "Livre II"
chapter: 2
last-verified: "2026-07-18"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Livre-II/QA/AUDIT-CHAPITRES-01-02.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Fondamentaux de GDScript

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH02`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **État technique vérifié le :** 18 juillet 2026  
> **Résultat attendu :** lire, écrire, tester et corriger un script GDScript typé simple, sans confondre GDScript avec Python et sans introduire prématurément une architecture globale.  
> **Audit post-création :** terminé — voir `Livre-II/QA/AUDIT-CHAPITRES-01-02.md`.

## 1. Rôle du chapitre

Le chapitre précédent a créé un projet Godot exécutable. Le présent chapitre explique le langage utilisé pour programmer ses comportements.

À la fin du chapitre, le lecteur doit savoir :

- reconnaître la structure d’un fichier GDScript ;
- déclarer des constantes, variables et types ;
- utiliser les principaux types intégrés ;
- écrire des conditions, boucles et fonctions ;
- manipuler des tableaux et dictionnaires ;
- créer une classe nommée simple ;
- comprendre les principales fonctions du cycle de vie d’un nœud ;
- exposer une propriété dans l’Inspector ;
- distinguer une erreur de syntaxe, une erreur de type et une erreur d’exécution ;
- produire un petit composant testable pour `Project Asteria`.

Ce chapitre ne traite pas encore en profondeur :

- les signaux ;
- la composition de scènes ;
- les Resources personnalisées ;
- les services globaux ;
- les bus d’événements ;
- la persistance ;
- les appels réseau ;
- les systèmes de gameplay.

Ces sujets possèdent leurs propres chapitres.

## 2. Nature de GDScript

GDScript est un langage :

- conçu pour Godot ;
- orienté objet ;
- impératif ;
- à typage progressif ;
- fondé sur l’indentation ;
- étroitement intégré aux nœuds, scènes, Resources et outils de l’éditeur.

Sa syntaxe peut rappeler Python, mais **GDScript n’est pas Python**.

Les différences importantes incluent :

- un système de types propre à Godot ;
- des classes natives comme `Node`, `Vector3`, `Transform3D` ou `Resource` ;
- des fonctions de cycle de vie comme `_ready()` et `_process()` ;
- des annotations comme `@export`, `@onready` et `@tool` ;
- les chemins `res://` et `user://` ;
- l’intégration directe à l’Inspector et à l’arbre de scène ;
- l’absence d’un mécanisme général d’exceptions comparable à celui de Python.

Une bibliothèque Python ne peut pas être importée directement dans un script GDScript.

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

## 3. Un fichier GDScript est une classe

Un fichier `.gd` décrit une classe.

Exemple minimal :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
extends Node


func _ready() -> void:
	print("Bonjour depuis Godot.")
```

Ce fichier :

1. étend la classe native `Node` ;
2. redéfinit la fonction virtuelle `_ready()` ;
3. exécute le bloc indenté lorsque le nœud entre dans l’état prêt.

Un script attaché à un nœud enrichit ce nœud avec :

- des propriétés ;
- des méthodes ;
- des signaux ;
- des constantes ;
- des états internes ;
- des réactions au cycle de vie.

## 4. Indentation et format des fichiers

### 4.1 Indentation

GDScript utilise l’indentation pour délimiter les blocs.

Correct :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func describe_health(health: int) -> String:
	if health <= 0:
		return "hors combat"
	return "actif"
```

Incorrect :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func describe_health(health: int) -> String:
if health <= 0:
return "hors combat"
```

Le guide suit le réglage par défaut de l’éditeur Godot : **tabulations pour l’indentation**.

### 4.2 Encodage et fins de ligne

Les scripts utilisent :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Encodage       UTF-8 sans BOM
Fin de ligne   LF
Fin de fichier une ligne vide finale
```

Git peut normaliser les fins de ligne. Dans Visual Studio Code, créer ou compléter `.gitattributes` à la racine du projet :

> **[VSC] Visual Studio Code - Créer ou modifier :** `.gitattributes` à la racine du projet.

```gitattributes
*.gd text eol=lf
*.tscn text eol=lf
*.tres text eol=lf
*.godot text eol=lf
```

### 4.3 Longueur et lisibilité

Règles du projet :

- viser moins de 100 caractères par ligne ;
- placer une instruction par ligne ;
- utiliser des parenthèses pour découper une expression longue ;
- préférer `and`, `or` et `not` à `&&`, `||` et `!` ;
- terminer les tableaux, dictionnaires et énumérations multilignes par une virgule ;
- séparer les étapes logiques d’une fonction par une ligne vide.

## 5. Ordre recommandé d’un script

Le projet suit cet ordre général :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
1. annotations de classe
2. class_name
3. extends
4. commentaire de documentation
5. signaux
6. énumérations
7. constantes
8. variables statiques
9. variables exportées
10. variables publiques
11. variables privées
12. variables @onready
13. initialisation et fonctions virtuelles
14. méthodes publiques
15. méthodes privées
16. classes internes
```

Exemple :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
class_name ExampleComponent
extends Node
## Composant d’exemple du guide.

signal state_changed(new_state: State)

enum State {
	IDLE,
	ACTIVE,
	DISABLED,
}

const MAX_VALUE: int = 100

@export var initial_value: int = 10

var value: int = 0
var _state: State = State.IDLE

@onready var _label: Label = $Label


func _ready() -> void:
	value = initial_value


func activate() -> void:
	_set_state(State.ACTIVE)


func _set_state(new_state: State) -> void:
	_state = new_state
	state_changed.emit(_state)
```

Les signaux seront étudiés dans le chapitre suivant. Ils figurent ici uniquement pour montrer l’ordre du fichier.

## 6. Commentaires et documentation

### 6.1 Commentaire ordinaire

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
# Explique pourquoi cette décision existe.
var gravity_scale: float = 1.0
```

Un commentaire ne doit pas répéter une instruction évidente.

Faible :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
# Ajoute 1 à count.
count += 1
```

Utile :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
# Le premier index est réservé à l’entrée inconnue pour préserver les sauvegardes anciennes.
count += 1
```

### 6.2 Commentaire de documentation

Les commentaires `##` alimentent la documentation intégrée de Godot.

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
class_name HealthPool
extends RefCounted
## Stocke une quantité de points de vie bornée.


## Retire [param amount] points et renvoie la valeur réellement retirée.
func apply_damage(amount: int) -> int:
	return 0
```

Utiliser notamment :

- `[param nom]` pour un paramètre ;
- `[method nom]` pour une méthode ;
- `[member nom]` pour une propriété ;
- `[code]...[/code]` pour un fragment court ;
- `[codeblock]...[/codeblock]` pour un bloc.

### 6.3 Code désactivé

Ne pas conserver de grandes portions de code commentées. Git conserve l’historique.

À supprimer :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
# func old_system():
# 	pass
```

## 7. Identifiants et conventions de nommage

| Élément | Convention | Exemple |
|---|---|---|
| fichier | `snake_case` | `health_pool.gd` |
| classe | `PascalCase` | `HealthPool` |
| nœud | `PascalCase` | `PlayerCamera` |
| fonction | `snake_case` | `apply_damage()` |
| variable | `snake_case` | `current_health` |
| constante | `CONSTANT_CASE` | `MAX_HEALTH` |
| énumération | `PascalCase` singulier | `CharacterState` |
| membre d’énumération | `CONSTANT_CASE` | `CharacterState.IDLE` |
| signal | `snake_case`, événement accompli | `health_changed` |
| membre privé conventionnel | préfixe `_` | `_recalculate()` |

Les noms de fichiers restent en minuscules afin d’éviter les erreurs de casse lors d’un export vers un système sensible à la casse.

## 8. Valeurs, expressions et instructions

### 8.1 Littéraux

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var lives: int = 3
var speed: float = 4.5
var enabled: bool = true
var title: String = "Project Asteria"
var empty_value: Variant = null
```

Les grands nombres peuvent utiliser `_` :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
const STARTING_CREDITS: int = 1_000
const WORLD_SEED: int = 2_147_483_647
```

### 8.2 Affectation

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var score: int = 0
score = 10
score += 5
score -= 2
score *= 3
score /= 2
```

Avec des entiers, vérifier la nature du calcul attendu. Pour une division décimale explicite :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var ratio: float = float(current_value) / float(max_value)
```

### 8.3 Comparaisons

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
health == 0
health != max_health
speed > 0.0
level >= minimum_level
name in known_names
```

### 8.4 Booléens

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
if is_alive and not is_stunned:
	move()
```

### 8.5 Expression conditionnelle

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var state_text := "vivant" if health > 0 else "hors combat"
```

L’expression conditionnelle est utile pour une valeur simple. Une logique complexe reste dans un bloc `if` lisible.

## 9. Types de base

### 9.1 Types scalaires

| Type | Usage |
|---|---|
| `bool` | vrai ou faux |
| `int` | entier signé |
| `float` | nombre à virgule flottante |
| `String` | chaîne de caractères Unicode |
| `StringName` | identifiant texte optimisé pour les comparaisons répétées |
| `NodePath` | chemin de nœud ou de propriété |
| `Callable` | référence vers une fonction appelable |
| `Signal` | valeur représentant un signal |
| `Variant` | valeur de type quelconque |

### 9.2 Types mathématiques

| Type | Usage |
|---|---|
| `Vector2` | position ou direction 2D |
| `Vector2i` | coordonnées entières 2D |
| `Vector3` | position, direction ou vitesse 3D |
| `Vector3i` | coordonnées entières 3D |
| `Quaternion` | rotation 3D |
| `Basis` | orientation et échelle 3D |
| `Transform3D` | transformation 3D complète |
| `Color` | couleur RGBA |
| `Rect2` | rectangle 2D |
| `AABB` | boîte englobante 3D |

Exemple :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var spawn_position := Vector3(0.0, 1.0, 0.0)
var move_direction := Vector3.FORWARD
var debug_color := Color(0.2, 0.8, 1.0, 1.0)
```

### 9.3 `StringName`

Un `StringName` convient aux identifiants répétés :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
const DEFAULT_FACTION: StringName = &"neutral"
const ACTION_INTERACT: StringName = &"interact"
```

Le préfixe `&` crée un littéral `StringName`.

Ne pas convertir chaque phrase utilisateur en `StringName`. Les descriptions et dialogues restent des `String`.

### 9.4 `NodePath`

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
@export var target_path: NodePath
```

Le préfixe `^` crée un littéral `NodePath` :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
const CAMERA_PATH: NodePath = ^"CameraRig/Camera3D"
```

Une référence directe typée est généralement préférable lorsqu’elle peut être obtenue de manière sûre avec `@onready`.

## 10. Typage progressif

### 10.1 Type explicite

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var health: int = 100
var speed: float = 5.0
var actor_name: String = "Aster"
```

### 10.2 Inférence avec `:=`

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var origin := Vector3.ZERO
var labels := ["alpha", "beta"]
```

Utiliser `:=` lorsque le type est évident et non ambigu.

Préférer un type explicite ici :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var health: int = 0
```

`0` pourrait représenter un entier, mais le domaine fonctionnel mérite d’être visible.

### 10.3 Paramètres et valeur de retour

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func clamp_health(value: int, maximum: int) -> int:
	return clampi(value, 0, maximum)
```

Une fonction qui ne renvoie rien utilise `void` :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func reset() -> void:
	print("Réinitialisation")
```

### 10.4 Types natifs et classes personnalisées

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
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

### 10.5 Pourquoi typer le code du guide

Le typage :

- détecte certaines erreurs avant l’exécution ;
- améliore l’autocomplétion ;
- documente les interfaces ;
- facilite les refactorings ;
- réduit les valeurs `Variant` inattendues ;
- rend les revues de code plus fiables.

Le projet n’exige pas une annotation redondante lorsque l’inférence est parfaitement claire.

### 10.6 Vérifier et convertir un type

L’opérateur `is` vérifie un type avant utilisation :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func handle_body(body: Node) -> void:
	if body is not CharacterBody3D:
		push_warning("Le nœud reçu n’est pas un CharacterBody3D.")
		return

	var character: CharacterBody3D = body
	print(character.name)
```

L’opérateur `as` tente une conversion d’objet et renvoie `null` si elle échoue :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var character := body as CharacterBody3D
if character == null:
	return
```

Cette forme est pratique lorsque l’échec est attendu. Elle peut aussi masquer une erreur de conception, car une conversion incompatible échoue silencieusement. Utiliser `is` ou une assertion lorsque le type incorrect représente un défaut.

## 11. Constantes et variables

### 11.1 Constante

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
const MAX_PARTY_SIZE: int = 8
const DEFAULT_SCENE := preload("res://src/features/bootstrap/main.tscn")
```

Une constante doit représenter une valeur stable pour la durée du script.

### 11.2 Variable membre

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var current_health: int = 100
```

Chaque instance possède sa propre valeur.

### 11.3 Variable locale

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func calculate_ratio(current: float, maximum: float) -> float:
	var safe_maximum := maxf(maximum, 1.0)
	return current / safe_maximum
```

Limiter la portée d’une variable à la fonction lorsqu’elle n’a pas besoin d’être conservée.

### 11.4 Variable statique

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
static var instances_created: int = 0
```

Une variable statique appartient à la classe, pas à chaque instance.

Elle ne doit pas servir de raccourci pour créer des états globaux cachés. Les services globaux seront conçus explicitement plus tard.

## 12. Énumérations

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
enum BootstrapState {
	UNKNOWN,
	READY,
	DEGRADED,
	FAILED,
}
```

Usage :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var state: BootstrapState = BootstrapState.UNKNOWN
```

Une énumération améliore la lisibilité par rapport à des entiers magiques :

Faible :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
state = 2
```

Correct :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
state = BootstrapState.DEGRADED
```

Les valeurs d’énumération restent représentées par des entiers. Une donnée externe doit être validée avant conversion.

## 13. Tableaux

### 13.1 Tableau non typé

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var mixed_values: Array = ["actor", 10, true]
```

Il est autorisé, mais rarement souhaitable pour une interface métier.

### 13.2 Tableau typé

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var actor_names: Array[String] = [
	"Aster",
	"Boreal",
	"Cyra",
]
```

Ajouter et lire :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
actor_names.append("Darian")
var first_name: String = actor_names[0]
var last_name: String = actor_names[-1]
```

### 13.3 Itération

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
for actor_name: String in actor_names:
	print(actor_name)
```

Lecture détaillée :

- `for` ouvre une boucle ;
- `actor_name` est une variable locale créée pour l’itération courante ;
- `: String` indique que chaque élément attendu est une chaîne ;
- `in actor_names` demande de prendre successivement chaque élément du tableau `actor_names` ;
- `print(actor_name)` affiche l’élément courant ;
- à chaque tour, `actor_name` reçoit la valeur suivante jusqu’à la fin du tableau.

Avec index :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
for index: int in actor_names.size():
	print("%d : %s" % [index, actor_names[index]])
```

Lecture détaillée :

- `actor_names.size()` renvoie le nombre d’éléments du tableau ; dans une boucle `for`, cet entier produit les index de `0` à `size() - 1` ;
- `index` contient donc la position courante ;
- `%d` est un emplacement réservé pour un entier décimal ;
- `%s` est un emplacement réservé converti en texte ;
- l’opérateur `%` applique les valeurs du tableau `[index, actor_names[index]]` aux deux emplacements, dans le même ordre ;
- `actor_names[index]` lit l’élément situé à la position `index` ;
- avec `index == 0` et le premier nom `Aster`, le texte affiché est `0 : Aster`.

### 13.4 Références et duplication

Les tableaux sont des types par référence.

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var original: Array[String] = ["A", "B"]
var alias := original
alias.append("C")
```

`original` contient également `C`.

Pour une copie indépendante :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var copy: Array = original.duplicate(true)
```

Le paramètre `true` demande une duplication profonde des éléments compatibles.

### 13.5 Ne pas modifier pendant l’itération

Éviter de supprimer des éléments du tableau parcouru.

Préférer :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var retained: Array[String] = []

for value: String in actor_names:
	if not value.begins_with("B"):
		retained.append(value)

actor_names = retained
```

### 13.6 PackedArrays

Godot fournit des tableaux compacts spécialisés, notamment :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
PackedByteArray
PackedInt32Array
PackedInt64Array
PackedFloat32Array
PackedFloat64Array
PackedStringArray
PackedVector2Array
PackedVector3Array
PackedColorArray
```

Les PackedArrays réduisent généralement la mémoire et conviennent aux grandes séries homogènes, aux buffers et à certaines API du moteur. Les `Array[Type]` restent préférables pour la plupart des collections métier grâce à leur souplesse et à leurs méthodes de haut niveau.

## 14. Dictionnaires

### 14.1 Déclaration

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var actor_data: Dictionary = {
	&"name": "Aster",
	&"level": 1,
	&"active": true,
}
```

### 14.2 Dictionnaire typé

Lorsque les clés et valeurs suivent un contrat stable :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var metrics: Dictionary[StringName, float] = {
	&"marker_height": 1.0,
	&"load_time_ms": 12.5,
}
```

Une clé ou une valeur d’un autre type provoque une erreur. Utiliser `Variant` comme type de valeur uniquement lorsque la structure est volontairement hétérogène :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var metadata: Dictionary[StringName, Variant] = {}
```

Les dictionnaires, typés ou non, sont passés par référence. Utiliser `duplicate()` lorsqu’une copie indépendante est nécessaire.

### 14.3 Accès sûr

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var actor_name: String = actor_data.get(&"name", "Unknown")
```

Éviter de supposer qu’une clé externe existe.

### 14.4 Tester une clé

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
if actor_data.has(&"level"):
	print(actor_data[&"level"])
```

### 14.5 Ajouter ou modifier

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
actor_data[&"level"] = 2
actor_data[&"faction"] = &"neutral"
```

### 14.6 Retirer

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
actor_data.erase(&"active")
```

### 14.7 Choix entre dictionnaire et classe

Un dictionnaire convient pour :

- une charge JSON temporaire ;
- des métadonnées flexibles ;
- un petit résultat intermédiaire ;
- une interface externe encore non stabilisée.

Une classe ou une Resource convient mieux lorsque :

- les champs sont stables ;
- les types sont importants ;
- des invariants doivent être protégés ;
- plusieurs systèmes utilisent la structure ;
- l’Inspector doit éditer les données.

## 15. Conditions

### 15.1 `if`, `elif`, `else`

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func describe_temperature(value: float) -> String:
	if value < 0.0:
		return "gel"
	elif value < 20.0:
		return "frais"
	else:
		return "chaud"
```

Après un `return`, le bloc s’arrête. Un `else` final peut parfois être supprimé :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func can_act(health: int, stunned: bool) -> bool:
	if health <= 0:
		return false
	if stunned:
		return false
	return true
```

Cette forme réduit l’imbrication.

### 15.2 Valeurs évaluées comme booléens

Le projet préfère des comparaisons explicites lorsque l’intention pourrait être ambiguë.

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
if actor_names.is_empty():
	push_warning("Aucun acteur déclaré.")
```

Plutôt que :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
if not actor_names:
	push_warning("Aucun acteur déclaré.")
```

## 16. `match`

`match` compare une valeur à plusieurs motifs.

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func state_to_text(state: BootstrapState) -> String:
	match state:
		BootstrapState.UNKNOWN:
			return "inconnu"
		BootstrapState.READY:
			return "prêt"
		BootstrapState.DEGRADED:
			return "dégradé"
		BootstrapState.FAILED:
			return "échec"
		_:
			return "valeur invalide"
```

Le motif `_` couvre les autres valeurs.

Un `match` est particulièrement utile pour :

- un état ;
- un type d’ordre ;
- un identifiant d’action ;
- un résultat de validation ;
- une machine à états simple.

Ne pas l’utiliser pour remplacer arbitrairement toutes les conditions.

## 17. Boucles

### 17.1 Boucle `for`

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
for index: int in range(5):
	print(index)
```

Résultat : `0` à `4`.

### 17.2 Parcourir un tableau

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
for warning: String in warnings:
	push_warning(warning)
```

### 17.3 Parcourir un dictionnaire

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
for key: StringName in metrics:
	print("%s = %s" % [key, metrics[key]])
```

Lecture détaillée :

- `metrics` est le dictionnaire déclaré précédemment avec le type `Dictionary[StringName, float]` ; ses clés sont donc des `StringName` et ses valeurs des nombres `float` ;
- parcourir directement un dictionnaire avec `for ... in metrics` parcourt ses **clés** ;
- `key` est une variable locale. À chaque tour, elle contient une clé différente, par exemple `&"marker_height"` puis `&"load_time_ms"` ;
- `: StringName` rend explicite le type de cette clé ;
- `metrics[key]` utilise la clé courante entre crochets pour récupérer la valeur correspondante dans le dictionnaire ;
- la chaîne `"%s = %s"` est un modèle contenant deux emplacements `%s` ; chaque `%s` signifie « convertir la prochaine valeur en texte et l’insérer ici » ;
- l’opérateur `%` situé entre la chaîne et le tableau effectue le formatage ; il ne représente pas ici un pourcentage ni un reste de division ;
- `[key, metrics[key]]` fournit les deux valeurs dans l’ordre : la clé remplace le premier `%s`, puis sa valeur remplace le second ;
- si `key` vaut `&"load_time_ms"` et `metrics[key]` vaut `12.5`, `print()` affiche `load_time_ms = 12.5`.

Une forme plus longue, mais parfois plus claire pour débuter, produit le même résultat :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** même boucle décomposée en variables intermédiaires.

```gdscript
for key: StringName in metrics:
	var value: float = metrics[key]
	var line: String = "%s = %s" % [key, value]
	print(line)
```

### 17.4 Boucle `while`

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var attempts: int = 0

while attempts < 3:
	attempts += 1
```

Une boucle `while` doit posséder une condition de sortie observable.

### 17.5 `break` et `continue`

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
for value: int in values:
	if value < 0:
		continue
	if value > limit:
		break
	process_value(value)
```

## 18. Fonctions

### 18.1 Fonction simple

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func add(a: int, b: int) -> int:
	return a + b
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

### 18.2 Paramètre par défaut

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func format_actor_name(actor_name: String, prefix: String = "") -> String:
	if prefix.is_empty():
		return actor_name
	return "%s %s" % [prefix, actor_name]
```

Lecture détaillée :

- `actor_name` est obligatoire, car aucune valeur n’est indiquée après son type ;
- `prefix: String = ""` possède la valeur par défaut `""`, une chaîne vide ; l’appelant peut donc omettre ce second argument ;
- `prefix.is_empty()` appelle la méthode `is_empty()` de la chaîne stockée dans `prefix` ;
- si le préfixe est vide, la fonction renvoie directement `actor_name` ;
- sinon, `"%s %s" % [prefix, actor_name]` construit une chaîne contenant le préfixe, un espace et le nom ;
- `format_actor_name("Aster")` renvoie `Aster` ;
- `format_actor_name("Aster", "Capitaine")` renvoie `Capitaine Aster`.

Les paramètres possédant une valeur par défaut sont placés après les paramètres obligatoires.

### 18.3 Fonction privée conventionnelle

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func _normalize_label(value: String) -> String:
	return value.strip_edges().to_lower()
```

GDScript ne rend pas cette méthode strictement privée. Le préfixe `_` communique l’intention.

### 18.4 Fonction statique

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
static func is_valid_percentage(value: float) -> bool:
	return value >= 0.0 and value <= 1.0
```

Appel :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
if MathRules.is_valid_percentage(0.5):
	print("Valeur valide")
```

### 18.5 Fonction récursive

La récursion est possible, mais une boucle est souvent plus sûre pour les parcours simples. Toute récursion doit posséder un cas terminal clair.

### 18.6 `await` et fonctions suspendues

`await` suspend la fonction courante jusqu’à la résolution d’un signal ou d’un objet attendu :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func wait_one_frame() -> void:
	await get_tree().process_frame
	print("Image suivante")
```

Une fonction utilisant `await` rend la suite de son exécution asynchrone. Le code appelant doit éviter de supposer que le résultat est disponible immédiatement. Les signaux, temporisations, annulations et chaînes asynchrones seront approfondis au chapitre 3.

## 19. Classes, héritage et `class_name`

### 19.1 Classe globale nommée

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
class_name BootstrapReport
extends RefCounted
```

Godot enregistre `BootstrapReport` comme type global du projet.

Instanciation :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var report := BootstrapReport.new()
```

### 19.2 Héritage

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
class_name SpecializedReport
extends BootstrapReport
```

Le projet privilégie la composition. L’héritage reste utile lorsque la relation « est un » est stable et simple.

### 19.3 Appeler le parent

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func reset() -> void:
	super.reset()
	print("Réinitialisation spécialisée")
```

### 19.4 Classe interne

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
class Metric:
	var key: StringName
	var value: float
```

Une classe interne convient à un détail d’implémentation local. Une classe réutilisée par plusieurs fonctionnalités reçoit son propre fichier.

## 20. Propriétés et accesseurs

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var health: int = 100:
	set(value):
		health = clampi(value, 0, max_health)
	get:
		return health

var max_health: int = 100
```

Un accesseur peut garantir un invariant, mais il doit rester léger.

Éviter dans un setter :

- un accès réseau ;
- un chargement de fichier lourd ;
- une longue recherche dans la scène ;
- une modification imprévisible de nombreux systèmes.

Pour une opération complexe, utiliser une méthode explicite comme `apply_damage()`.

## 21. Annotations principales

### 21.1 `@export`

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
@export var rotation_speed: float = 0.5
```

La propriété devient modifiable dans l’Inspector et enregistrée dans la scène ou la Resource.

### 21.2 Bornes et choix

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
@export_range(0.0, 10.0, 0.1) var movement_speed: float = 4.0
@export_enum("Peaceful", "Normal", "Hard") var difficulty: int = 1
@export_file("*.json") var configuration_file: String
@export_dir var export_directory: String
```

Un indice d’Inspector ne remplace pas la validation à l’exécution.

### 21.3 `@onready`

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
@onready var marker: MeshInstance3D = $Marker
```

La valeur est initialisée juste avant `_ready()`, lorsque les enfants attendus existent dans l’arbre.

### 21.4 `@tool`

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
@tool
extends Node3D
```

Le script peut s’exécuter dans l’éditeur.

Cette annotation est **optionnelle et avancée**. Un script `@tool` peut modifier une scène pendant l’édition. Il exige :

- une sauvegarde ;
- un comportement idempotent ;
- des gardes `Engine.is_editor_hint()` ;
- l’absence d’opération destructive implicite.

### 21.5 `@warning_ignore`

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
@warning_ignore("unused_parameter")
func _on_debug_event(_payload: Variant) -> void:
	pass
```

Ne masquer un avertissement qu’après l’avoir compris. Préférer le préfixe `_` pour un paramètre volontairement inutilisé lorsque cela suffit.

## 22. Cycle de vie d’un nœud

### 22.1 `_init()`

Appelé lors de la construction de l’objet.

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func _init() -> void:
	print("Objet construit")
```

Les enfants de scène ne sont pas encore nécessairement disponibles.

### 22.2 `_enter_tree()`

Appelé lorsque le nœud entre dans l’arbre de scène.

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func _enter_tree() -> void:
	print("Entrée dans l’arbre")
```

### 22.3 `_ready()`

Appelé lorsque le nœud et ses enfants sont prêts.

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func _ready() -> void:
	print("Nœud prêt")
```

C’est le point d’initialisation habituel pour les références `@onready`.

### 22.4 `_process(delta)`

Appelé à chaque image rendue lorsque le traitement est actif.

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func _process(delta: float) -> void:
	rotation.y += delta
```

Utilisations :

- animation visuelle non physique ;
- interpolation d’interface ;
- effets dépendant du rendu.

### 22.5 `_physics_process(delta)`

Appelé à fréquence physique fixe.

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func _physics_process(delta: float) -> void:
	_update_movement(delta)
```

Utilisations :

- déplacement physique ;
- collisions ;
- contrôleurs de personnage ;
- logique devant suivre le pas physique.

### 22.6 Ordre simplifié

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
construction
    ↓
_init()
    ↓
entrée dans l’arbre
    ↓
_enter_tree()
    ↓
enfants prêts
    ↓
_ready()
    ↓
_process() et/ou _physics_process()
    ↓
sortie de l’arbre
```

Le chapitre suivant approfondira l’ordre entre parents, enfants et scènes instanciées.

## 23. Références d’objets et validité

### 23.1 `null`

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var target: Node3D = null

if target == null:
	push_warning("Aucune cible")
```

### 23.2 Objet libéré

Une référence vers un objet peut exister alors que l’objet natif a été libéré.

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
if is_instance_valid(target):
	target.queue_free()
```

### 23.3 `queue_free()`

Pour un nœud :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
queue_free()
```

La suppression est planifiée de manière sûre à la fin de l’image courante.

Éviter de continuer à utiliser un nœud après avoir demandé sa suppression.

## 24. Chargement de ressources

### 24.1 `preload()`

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
const MAIN_SCENE := preload("res://src/features/bootstrap/main.tscn")
```

Le chemin doit être connu à l’analyse du script.

Utiliser pour :

- une dépendance fixe ;
- une petite Resource toujours requise ;
- une classe de script connue.

### 24.2 `load()`

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var resource := load(path)
```

Le chemin peut être déterminé à l’exécution.

Utiliser pour :

- du contenu optionnel ;
- un chemin choisi par les données ;
- un catalogue de ressources.

Valider le résultat :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var resource := load(path)
if resource == null:
	push_error("Ressource introuvable : %s" % path)
	return
```

### 24.3 Ne pas charger à chaque image

Ne pas placer un `load()` répétitif dans `_process()` sans cache explicite.

## 25. Chaînes et formatage

### 25.1 Interpolation avec `%`

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var message := "%s possède %d points." % [actor_name, score]
```

### 25.2 Conversion

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var text_value := str(score)
var parsed_value := int("42")
```

Une entrée externe doit être validée avant conversion lorsque l’échec est possible.

### 25.3 Méthodes utiles

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
value.strip_edges()
value.to_lower()
value.to_upper()
value.begins_with("prefix")
value.ends_with(".json")
value.split(",")
value.replace("ancien", "nouveau")
```

### 25.4 Texte utilisateur

Les dialogues et textes d’interface seront externalisés pour la localisation. Ne pas disperser de longues chaînes de contenu dans les scripts de gameplay.

## 26. Mathématiques usuelles

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
clampi(value, minimum, maximum)
clampf(value, minimum, maximum)
mini(a, b)
maxi(a, b)
minf(a, b)
maxf(a, b)
lerpf(from, to, weight)
move_toward(from, to, delta)
absf(value)
signf(value)
```

Pour les vecteurs :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var direction := target_position - global_position
var distance := direction.length()
var normalized_direction := direction.normalized()
```

Ne pas normaliser un vecteur nul sans réfléchir au résultat attendu.

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
if not direction.is_zero_approx():
	direction = direction.normalized()
```

## 27. Aléatoire déterministe

Pour une simulation reproductible :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var rng := RandomNumberGenerator.new()
rng.seed = 12_345

var value := rng.randi_range(1, 100)
```

Conserver la graine lorsqu’un résultat doit être reproduit.

Pour une session non déterministe :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
rng.randomize()
```

Le système de sauvegarde devra enregistrer les graines importantes de la simulation.

## 28. Gestion des erreurs

GDScript n’utilise pas des exceptions générales comme Python pour le flux métier courant.

### 28.1 Retour explicite

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func divide_safe(a: float, b: float) -> float:
	if is_zero_approx(b):
		push_error("Division par zéro refusée.")
		return 0.0
	return a / b
```

### 28.2 Code `Error`

Certaines API renvoient un code `Error` :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var error := DirAccess.make_dir_recursive_absolute(path)
if error != OK:
	push_error("Création impossible : %s" % error_string(error))
```

### 28.3 Messages de diagnostic

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
print("Information")
push_warning("Situation inhabituelle")
push_error("Échec fonctionnel")
printerr("Erreur vers stderr")
```

### 28.4 Assertion

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
assert(max_health > 0, "max_health doit être supérieur à zéro")
```

Une assertion vérifie une hypothèse de développement. Elle ne remplace pas la validation d’une donnée utilisateur ou d’un fichier externe.

### 28.5 Échouer tôt

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
func initialize(configuration: Dictionary) -> bool:
	if not configuration.has(&"name"):
		push_error("Champ name absent")
		return false

	if String(configuration[&"name"]).is_empty():
		push_error("Champ name vide")
		return false

	return true
```

## 29. Avertissements du langage

L’éditeur peut signaler :

- une variable inutilisée ;
- un paramètre inutilisé ;
- une valeur potentiellement non sûre ;
- une conversion implicite ;
- une branche impossible ;
- une méthode qui masque une méthode parente ;
- un type Variant non sécurisé.

Le projet traite les avertissements selon trois catégories :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
corriger       défaut ou ambiguïté réelle
justifier      comportement intentionnel documenté
ignorer ciblé  cas rare avec annotation locale
```

Ne pas désactiver globalement un avertissement pour faire disparaître un problème isolé.

## 30. Débogueur intégré

### 30.1 Point d’arrêt

> **[APP] Godot - Débogueur :** placer le point d’arrêt dans l’éditeur de script.

Cliquer dans la marge de l’éditeur de script pour placer un point d’arrêt.

Lors de l’arrêt, examiner :

- la pile d’appels ;
- les variables locales ;
- les membres de l’objet ;
- le nœud courant ;
- la ligne exacte ;
- les erreurs précédentes dans Output.

### 30.2 Exécution pas à pas

Utiliser :

- entrer dans la fonction ;
- exécuter la ligne suivante ;
- sortir de la fonction ;
- reprendre l’exécution.

### 30.3 Moniteur distant

Pendant l’exécution, le dock **Remote** permet d’inspecter l’arbre de scène réellement instancié.

Ne pas confondre :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Local   scène telle qu’éditée
Remote  scène telle qu’exécutée
```

## 31. Exercice du projet fil rouge

L’exercice crée une classe indépendante qui résume l’état du bootstrap de `Project Asteria`.

### 31.1 Créer le dossier

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
New-Item -ItemType Directory -Force `
  C:\IA-GameDev\projects\project-asteria\src\core\diagnostics |
  Out-Null
```

### 31.2 Créer `bootstrap_report.gd`

Chemin :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
res://src/core/diagnostics/bootstrap_report.gd
```

Contenu :

> **[VSC] Visual Studio Code - Créer :** `res://src/core/diagnostics/bootstrap_report.gd`.

```gdscript
class_name BootstrapReport
extends RefCounted
## Résume les validations de démarrage de Project Asteria.

enum Status {
	UNKNOWN,
	READY,
	DEGRADED,
	FAILED,
}

const MAX_MESSAGES: int = 32

var status: Status = Status.UNKNOWN
var messages: Array[String] = []
var metrics: Dictionary[StringName, float] = {}


func add_message(message: String) -> void:
	var normalized := message.strip_edges()
	if normalized.is_empty():
		return
	if messages.size() >= MAX_MESSAGES:
		push_warning("La limite de messages du rapport est atteinte.")
		return
	messages.append(normalized)


func set_metric(key: StringName, value: float) -> void:
	metrics[key] = value


func mark_ready() -> void:
	status = Status.READY


func mark_degraded(reason: String) -> void:
	status = Status.DEGRADED
	add_message(reason)


func mark_failed(reason: String) -> void:
	status = Status.FAILED
	add_message(reason)


func is_usable() -> bool:
	return status == Status.READY or status == Status.DEGRADED


func status_text() -> String:
	match status:
		Status.UNKNOWN:
			return "unknown"
		Status.READY:
			return "ready"
		Status.DEGRADED:
			return "degraded"
		Status.FAILED:
			return "failed"
		_:
			return "invalid"


func summary() -> String:
	return "status=%s messages=%d metrics=%d" % [
		status_text(),
		messages.size(),
		metrics.size(),
	]
```

### 31.3 Utiliser la classe dans `main.gd`

Compléter le script principal :

> **[VSC] Visual Studio Code - Modifier :** `res://src/features/bootstrap/main.gd`.

```gdscript
extends Node3D

const VALIDATION_ID: StringName = &"DOC-L2-CH02"
const ROTATION_SPEED: float = 0.5

@onready var marker: MeshInstance3D = $Marker

var _report := BootstrapReport.new()


func _ready() -> void:
	_run_bootstrap_validation()
	print("%s : %s" % [VALIDATION_ID, _report.summary()])


func _process(delta: float) -> void:
	marker.rotate_y(ROTATION_SPEED * delta)


func _run_bootstrap_validation() -> void:
	if marker == null:
		_report.mark_failed("Le marqueur est absent.")
		return

	_report.set_metric(&"marker_height", marker.position.y)
	_report.add_message("Scène principale chargée.")
	_report.mark_ready()
```

### 31.4 Résultat attendu

Dans **Output** :

> **[SORTIE] Résultat attendu - Ne pas saisir :** comparer avec le résultat obtenu.

```text
DOC-L2-CH02 : status=ready messages=1 metrics=1
```

Le marqueur continue de tourner.

## 32. Tests manuels de l’exercice

### Test 1 — Cas nominal

- conserver le nœud `Marker` ;
- exécuter le projet ;
- vérifier `status=ready`.

### Test 2 — Message vide

Ajouter temporairement :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
_report.add_message("   ")
```

Le nombre de messages ne doit pas augmenter.

### Test 3 — État dégradé

Remplacer temporairement :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
_report.mark_ready()
```

par :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
_report.mark_degraded("Mode graphique réduit.")
```

Résultat attendu :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
status=degraded messages=2 metrics=1
```

### Test 4 — Erreur de type

Essayer temporairement :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
_report.set_metric(&"marker_height", "haut")
```

L’éditeur doit signaler que `String` ne correspond pas au paramètre `float`.

Annuler ensuite la modification.

### Test 5 — Erreur de syntaxe

Retirer temporairement le `:` d’une déclaration de fonction. L’éditeur doit empêcher une exécution normale et indiquer la ligne concernée.

Annuler ensuite la modification.

## 33. Validation sans interface

Godot peut vérifier le projet depuis PowerShell.

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Set-Location C:\IA-GameDev\projects\project-asteria

& $env:GODOT_EXE `
  --headless `
  --path . `
  --editor `
  --quit `
  --verbose `
  *> logs\gdscript-import-check.log

if ($LASTEXITCODE -ne 0) {
  throw "La vérification Godot a échoué."
}
```

Cette commande :

- ouvre le projet sans fenêtre ;
- importe les ressources nécessaires ;
- analyse les scripts chargés par le projet ;
- écrit un journal ;
- quitte ensuite.

Elle ne remplace pas les tests d’exécution du gameplay.

Rechercher les erreurs :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Select-String `
  -Path logs\gdscript-import-check.log `
  -Pattern "ERROR|SCRIPT ERROR|Parse Error"
```

Une recherche vide est attendue.

## 34. Tests déterministes

Une fonction déterministe renvoie le même résultat pour les mêmes entrées.

Exemple :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
static func compute_damage(base_damage: int, armor: int) -> int:
	return maxi(base_damage - armor, 0)
```

Test simple :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
assert(compute_damage(10, 3) == 7)
assert(compute_damage(3, 10) == 0)
```

Les calculs métiers importants seront progressivement déplacés vers des classes sans dépendance à l’arbre de scène afin de faciliter leurs tests.

## 35. Erreurs fréquentes

### 35.1 Confondre `=` et `==`

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
health = 0   # affectation
health == 0  # comparaison
```

### 35.2 Mauvaise indentation

Symptômes :

- erreur d’analyse ;
- bloc exécuté au mauvais niveau ;
- `return` placé hors de la fonction.

Utiliser l’indentation automatique de l’éditeur.

### 35.3 Type trop vague

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var data
```

Préférer :

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var data: Dictionary = {}
```

ou une classe métier dédiée.

### 35.4 Dépendance cachée à un nœud

> **[LECTURE] Exemple GDScript - Ne pas recopier automatiquement :** étudier la syntaxe et l’adapter uniquement lorsque l’étape le demande.

```gdscript
var player = get_node("/root/Main/World/Player")
```

Ce chemin absolu fragilise la scène. Le chapitre 3 montrera les références, scènes instanciées et signaux ; le chapitre 4 définira les frontières architecturales.

### 35.5 Travail lourd dans `_process()`

Éviter à chaque image :

- lecture de fichier ;
- requête réseau ;
- recherche complète de l’arbre ;
- chargement de Resource ;
- reconstruction d’un grand tableau ;
- sérialisation JSON complète.

### 35.6 Utiliser `Variant` partout

Le typage dynamique reste utile aux frontières externes, mais il ne doit pas effacer les contrats internes du projet.

### 35.7 Modifier un tableau partagé sans le savoir

Utiliser `duplicate()` lorsqu’une copie indépendante est nécessaire.

### 35.8 Masquer tous les avertissements

Un projet silencieux n’est pas forcément correct. Corriger la cause avant de désactiver un contrôle.

### 35.9 Utiliser `@tool` trop tôt

Un script éditeur peut modifier les données pendant la conception. Il reste optionnel jusqu’au chapitre consacré aux outils internes.

## 36. Principes de conception retenus

| Décision | Statut |
|---|---|
| GDScript comme langage principal | retenu |
| Typage progressif dans le code de production | obligatoire |
| `Variant` aux frontières réellement dynamiques | autorisé |
| Classes nommées pour les concepts réutilisables | recommandé |
| Dictionnaires comme modèle métier universel | écarté |
| Tabulations pour l’indentation | retenu |
| Noms de fichiers en `snake_case` | obligatoire |
| Noms de classes en `PascalCase` | obligatoire |
| Logique lourde dans `_process()` | interdit |
| État global caché dans des variables statiques | interdit |
| Scripts `@tool` dans le parcours débutant | optionnel |
| Validation headless après modification importante | recommandé |

## 37. Mode Solo

Le développeur Solo :

- utilise l’éditeur de script intégré au début ;
- active le typage sur les interfaces importantes ;
- conserve des classes courtes ;
- évite les abstractions sans besoin concret ;
- traite les avertissements avant chaque commit ;
- ajoute un test manuel reproductible par composant ;
- privilégie une fonction pure pour les calculs métier.

Règle Solo :

> Une fonction lisible et testable vaut mieux qu’une hiérarchie de classes anticipant des besoins inexistants.

## 38. Mode Studio

Le Mode Studio ajoute :

- une convention GDScript versionnée ;
- des règles de revue sur les types publics ;
- un seuil d’avertissements accepté égal à zéro pour le code nouveau ;
- une validation headless en CI ;
- des propriétaires de modules ;
- des commentaires de documentation pour les interfaces partagées ;
- des tests automatisés des fonctions déterministes ;
- une procédure d’évolution des classes globales `class_name`.

Une classe publique modifiée doit identifier les scènes, Resources et sauvegardes susceptibles d’être affectées.

## 39. Checklist obligatoire

- [ ] Je sais distinguer GDScript et Python.
- [ ] Je comprends qu’un fichier `.gd` représente une classe.
- [ ] Mes scripts utilisent UTF-8, LF et une indentation cohérente.
- [ ] Les fichiers et symboles respectent les conventions de nommage.
- [ ] Les paramètres et valeurs de retour importants sont typés.
- [ ] Je sais utiliser `if`, `match`, `for` et `while`.
- [ ] Je sais créer et parcourir un `Array` typé et reconnaître un PackedArray.
- [ ] Je sais utiliser un `Dictionary` typé et accéder prudemment à ses valeurs.
- [ ] Je sais vérifier un type avec `is` et utiliser `as` uniquement lorsque l’échec nullable est voulu.
- [ ] Je comprends la différence entre copie et référence pour un tableau.
- [ ] Je sais écrire une classe `class_name` simple.
- [ ] Je comprends `_init()`, `_enter_tree()`, `_ready()`, `_process()` et `_physics_process()`.
- [ ] Je sais utiliser `@export` et `@onready`.
- [ ] Je sais utiliser `preload()` et `load()` dans leurs cas respectifs.
- [ ] Je comprends que `await` suspend la suite d’une fonction.
- [ ] Je sais lire une erreur dans Output et le débogueur.
- [ ] `BootstrapReport` fonctionne dans `Project Asteria`.
- [ ] La vérification headless ne rapporte aucune erreur de script.
- [ ] Les changements sont enregistrés dans Git.

## 40. Critère d’acceptation

Le chapitre est validé lorsque :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Godot 4.7.1-stable ouvre le projet
        ↓
bootstrap_report.gd est reconnu comme classe globale
        ↓
main.gd compile avec typage
        ↓
le projet affiche la scène de bootstrap
        ↓
Output contient status=ready
        ↓
les tests manuels réussissent
        ↓
la vérification headless se termine avec le code 0
        ↓
aucune erreur de script ne reste dans le journal
        ↓
le commit Git est propre
```

## 41. Commit de validation

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Set-Location C:\IA-GameDev\projects\project-asteria

git status --short
git add .
git diff --cached --check
git commit -m "feat(core): add typed GDScript bootstrap report"
```

Vérifier :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git status --short
git log -1 --oneline
```

Le statut doit être vide après le commit.

## 42. Sources officielles vérifiées

- [Godot 4.7 — documentation GDScript](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/index.html)
- [Référence GDScript](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/gdscript_basics.html)
- [Typage statique en GDScript](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/static_typing.html)
- [Guide de style GDScript](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/gdscript_styleguide.html)
- [Commentaires de documentation](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/gdscript_documentation_comments.html)
- [Propriétés exportées](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/gdscript_exports.html)
- [Système d’avertissements GDScript](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/warning_system.html)
- [Utilisation de l’éditeur de script](https://docs.godotengine.org/en/4.7/tutorials/scripting/script_editor/index.html)
- [Ligne de commande de Godot](https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html)
- [Classe Array](https://docs.godotengine.org/en/4.7/classes/class_array.html)
- [Classe Dictionary](https://docs.godotengine.org/en/4.7/classes/class_dictionary.html)
- [Liste des annotations GDScript](https://docs.godotengine.org/en/4.7/classes/class_%40gdscript.html)

## 43. Résumé

GDScript est le langage principal de `Project Asteria`. Le projet adopte un typage progressif, des conventions cohérentes et des classes courtes afin de rendre le code lisible, testable et compatible avec les outils de Godot.

Les fondations retenues sont :

- un fichier `.gd` représente une classe ;
- les nœuds fournissent le cycle de vie ;
- les types décrivent les contrats ;
- les tableaux et dictionnaires sont utilisés avec prudence ;
- les fonctions courtes portent une responsabilité claire ;
- les erreurs sont traitées explicitement ;
- la logique métier déterministe reste séparée autant que possible de l’arbre de scène ;
- le projet reste exécutable après chaque modification.

Le chapitre suivant approfondira les scènes, les nœuds, les Resources, les instances et les signaux.
