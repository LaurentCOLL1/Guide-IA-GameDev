---
title: "Livre II — Chapitre 6 : Entrées, contrôleurs, caméras et interactions"
id: "DOC-L2-CH06"
status: "reviewed"
version: "1.1.0"
lang: "fr-FR"
book: "Livre II"
chapter: 6
last-verified: "2026-07-19"
audit-status: "complete"
audit-date: "2026-07-19"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-06.md"
supplemental-audit: "Livre-II/QA/AUDIT-RETROACTIF-EXEMPLES-ERREURS-CH01-CH06.md"
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

# Entrées, contrôleurs, caméras et interactions

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir, **[LECTURE]** exemple à étudier. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH06`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  

> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-06.md`.

## 1. Rôle du chapitre

Les chapitres précédents ont défini les briques de Godot, GDScript, les scènes, l’architecture modulaire et l’assemblage des services.

Le jeu doit maintenant transformer des actions humaines en comportements 3D sans mélanger :

- les touches physiques ;
- les intentions du joueur ;
- les règles de déplacement ;
- la caméra ;
- la détection d’un objet interactif ;
- l’interface utilisateur ;
- les événements transversaux.

Une implémentation improvisée produit souvent :

- des touches codées en dur dans plusieurs scripts ;
- un contrôleur clavier différent du contrôleur manette ;
- un déplacement dépendant du nombre d’images par seconde ;
- une caméra qui traverse les murs ;
- des menus qui déclenchent aussi les actions de jeu ;
- des interactions qui connaissent directement les détails internes des objets ;
- des paramètres de sensibilité impossibles à remapper ;
- des scripts trop difficiles à tester.

À la fin du chapitre, le lecteur doit savoir :

- configurer des actions dans l’Input Map ;
- distinguer événement ponctuel et état maintenu ;
- utiliser `_unhandled_input()` sans concurrencer l’interface ;
- utiliser `Input.get_vector()` pour clavier et manette ;
- séparer lecture des entrées, intention, contrôleur et moteur physique ;
- déplacer un `CharacterBody3D` avec `move_and_slide()` ;
- orienter le déplacement selon la caméra ;
- construire une caméra à la troisième personne avec `SpringArm3D` ;
- capturer et libérer la souris ;
- détecter une cible avec `RayCast3D` ;
- proposer une interaction de proximité avec `Area3D` ;
- préparer le remappage des commandes ;
- intégrer accessibilité, zones mortes et variantes Solo/Studio.

## 2. Prérequis

Le lecteur doit connaître :

- les fonctions, types, variables et classes du chapitre 2 ;
- les scènes, nœuds, signaux et `Callable` du chapitre 3 ;
- les frontières de modules du chapitre 4 ;
- l’injection et le point de composition du chapitre 5.

Le chapitre réutilise :

- `AppBootstrap` ;
- `GameEventBus` ;
- `StatusBeacon` ;
- l’organisation feature-first ;
- la règle selon laquelle les dépendances sont fournies depuis `src/app`.

## 3. Périmètre et frontières

Ce chapitre définit :

- les actions du joueur ;
- une trame d’intention indépendante des périphériques ;
- un lecteur d’entrées ;
- un moteur de personnage 3D ;
- un contrôleur qui orchestre les composants ;
- une caméra à la troisième personne ;
- un système d’interaction par rayon ;
- une alternative par zone ;
- le remappage en mémoire ;
- les contrôles d’accessibilité de base.

Il ne définit pas encore :

- les statistiques et capacités complètes des personnages du chapitre 14 ;
- les animations avancées du Livre III ;
- les données persistantes de remappage des chapitres 7 et 9 ;
- le multijoueur du Livre IV ;
- les tests automatisés complets du chapitre 27 ;
- la localisation de l’interface du Livre IV.

> **Frontière essentielle :** le lecteur d’entrées produit une intention. Il ne déplace pas directement le personnage et ne décide pas des règles de gameplay.

## 4. Chaîne de traitement retenue

La chaîne de `Project Asteria` est :

> **[LECTURE] Architecture de l’entrée — Ne pas saisir.**

```text
Périphérique physique
    ↓
InputMap et InputEvent
    ↓
PlayerInputReader
    ↓
PlayerInputFrame
    ↓
PlayerController
    ├── ThirdPersonCameraRig
    ├── PlayerMotor
    └── PlayerInteractor
            ↓
      InteractionTarget
```

Chaque niveau possède une responsabilité :

| Niveau | Responsabilité |
|---|---|
| périphérique | touche, bouton, axe, mouvement de souris |
| Input Map | associer plusieurs périphériques à une action nommée |
| lecteur | convertir l’état des actions en intention |
| trame | transporter une intention pour une itération de physique |
| contrôleur | coordonner caméra, moteur et interaction |
| moteur | appliquer vitesse, gravité, saut et collisions |
| interactor | sélectionner et appeler une cible |
| cible | exposer une invite et accepter ou refuser l’interaction |

Cette séparation permet :

- de changer les touches sans modifier le moteur ;
- de remplacer le lecteur humain par un lecteur IA ;
- de rejouer une trame enregistrée ;
- de tester le moteur avec une intention synthétique ;
- de désactiver les entrées lorsque le jeu est en pause ;
- de conserver un flux compréhensible.

## 5. Configurer l’Input Map

### 5.1 Créer les actions

> **[APP] Godot — Ouvrir `Project > Project Settings > Input Map`.**

Créer les actions suivantes en `snake_case` :

| Action | Clavier/souris | Manette | Zone morte conseillée |
|---|---|---|---:|
| `move_left` | `A` ou `Q` | stick gauche X négatif | 0,20 |
| `move_right` | `D` | stick gauche X positif | 0,20 |
| `move_forward` | `W` ou `Z` | stick gauche Y négatif | 0,20 |
| `move_back` | `S` | stick gauche Y positif | 0,20 |
| `look_left` | aucune | stick droit X négatif | 0,20 |
| `look_right` | aucune | stick droit X positif | 0,20 |
| `look_up` | aucune | stick droit Y négatif | 0,20 |
| `look_down` | aucune | stick droit Y positif | 0,20 |
| `jump` | espace | bouton bas | 0,20 |
| `sprint` | Maj gauche | pression stick gauche | 0,20 |
| `interact` | `E` | bouton gauche | 0,20 |
| `pause` | Échap | bouton Start/Menu | 0,20 |

Les noms d’action décrivent une intention, pas une touche. Éviter `press_e` ou `keyboard_forward`.

### 5.2 Disposition AZERTY et QWERTY

Le guide accepte plusieurs événements pour une même action :

- `move_forward` peut contenir `W` et `Z` ;
- `move_left` peut contenir `A` et `Q`.

Cela fournit un démarrage immédiat. Le menu de remappage permettra ensuite au joueur de supprimer les liaisons inutiles.

### 5.3 Vérifier les actions requises

> **[VSC] Visual Studio Code — Créer : `src/features/player/input/player_input_actions.gd`.**

```gdscript
class_name PlayerInputActions
extends RefCounted

const MOVE_LEFT: StringName = &"move_left"
const MOVE_RIGHT: StringName = &"move_right"
const MOVE_FORWARD: StringName = &"move_forward"
const MOVE_BACK: StringName = &"move_back"
const LOOK_LEFT: StringName = &"look_left"
const LOOK_RIGHT: StringName = &"look_right"
const LOOK_UP: StringName = &"look_up"
const LOOK_DOWN: StringName = &"look_down"
const JUMP: StringName = &"jump"
const SPRINT: StringName = &"sprint"
const INTERACT: StringName = &"interact"
const PAUSE: StringName = &"pause"

const REQUIRED_ACTIONS: Array[StringName] = [
	MOVE_LEFT,
	MOVE_RIGHT,
	MOVE_FORWARD,
	MOVE_BACK,
	LOOK_LEFT,
	LOOK_RIGHT,
	LOOK_UP,
	LOOK_DOWN,
	JUMP,
	SPRINT,
	INTERACT,
	PAUSE,
]

static func validate_required_actions() -> bool:
	var valid := true

	for action: StringName in REQUIRED_ACTIONS:
		if InputMap.has_action(action):
			continue

		push_error("Action Input Map absente : %s" % action)
		valid = false

	return valid
```

Explication :

- `const` crée un identifiant qui ne sera pas réaffecté ;
- `StringName` est adapté aux noms d’actions répétés ;
- le préfixe `&` construit directement un `StringName` ;
- `REQUIRED_ACTIONS` est un tableau typé ;
- `static` permet d’appeler la fonction sans instancier la classe ;
- `InputMap.has_action(action)` vérifie la configuration du projet ;
- `continue` passe à l’action suivante lorsqu’elle existe ;
- `valid` reste `false` dès qu’une action manque ;
- le retour indique si le contrat d’entrée est complet.

Cette validation détecte tôt une faute de frappe entre le code et les paramètres du projet.

## 6. Événements contre interrogation continue

Godot fournit deux approches complémentaires.

### 6.1 Événement ponctuel

Un événement convient à une action déclenchée une fois :

- appuyer sur Interagir ;
- demander un saut ;
- ouvrir la pause ;
- déplacer la souris.

`_unhandled_input(event)` est généralement adapté au gameplay, car les nœuds `Control` ont auparavant l’occasion de consommer l’événement.

### 6.2 État maintenu

L’interrogation continue convient à une action maintenue :

- avancer ;
- reculer ;
- sprinter ;
- incliner un stick.

Le singleton `Input` est interrogé pendant `_physics_process()`.

### 6.3 Pourquoi ne pas tout lire dans `_input()`

`_input()` reçoit les événements avant l’interface. Un clic destiné à un bouton pourrait donc aussi déclencher une action de jeu.

La chaîne recommandée est :

> **[LECTURE] Ordre simplifié de propagation — Ne pas saisir.**

```text
_input()
    ↓
interface Control
    ↓
raccourcis
    ↓
_unhandled_key_input()
    ↓
_unhandled_input()
```

Lorsqu’un événement est traité, `get_viewport().set_input_as_handled()` empêche sa propagation ultérieure. Cette opération ne change pas l’état renvoyé par le singleton `Input`.

## 7. Définir une trame d’intention

Une **trame d’intention** est un objet éphémère contenant ce que le joueur souhaite pendant une itération.

> **[VSC] Visual Studio Code — Créer : `src/features/player/input/player_input_frame.gd`.**

```gdscript
class_name PlayerInputFrame
extends RefCounted

var move: Vector2 = Vector2.ZERO
var look_delta: Vector2 = Vector2.ZERO
var jump_pressed := false
var sprint_pressed := false
var interact_pressed := false
var pause_pressed := false

func is_idle() -> bool:
	return (
		move.is_zero_approx()
		and look_delta.is_zero_approx()
		and not jump_pressed
		and not sprint_pressed
		and not interact_pressed
		and not pause_pressed
	)
```

Explication :

- `move` contient une direction 2D : gauche/droite et avant/arrière ;
- `look_delta` contient une variation de lacet et de tangage ;
- `jump_pressed` vaut `true` uniquement pour une demande ponctuelle ;
- `sprint_pressed` représente ici un état maintenu ;
- `interact_pressed` représente une demande ponctuelle ;
- `pause_pressed` transporte la demande d’ouverture du menu ;
- `Vector2.ZERO` signifie aucune intention ;
- `is_zero_approx()` tolère de très petites valeurs analogiques ;
- `is_idle()` renvoie `true` si aucune intention utile n’existe.

La trame ne contient aucune touche. Elle peut provenir d’un clavier, d’une manette, d’un test ou d’une IA.

## 8. Lire clavier, souris et manette

### 8.1 Script complet

> **[VSC] Visual Studio Code — Créer : `src/features/player/input/player_input_reader.gd`.**

```gdscript
class_name PlayerInputReader
extends Node

@export_range(0.01, 1.0, 0.01)
var mouse_sensitivity := 0.12

@export_range(10.0, 360.0, 1.0)
var gamepad_look_speed := 140.0

var _mouse_look_accumulator := Vector2.ZERO
var _jump_requested := false
var _interact_requested := false
var _pause_requested := false
var _enabled := true

func _ready() -> void:
	if not PlayerInputActions.validate_required_actions():
		set_enabled(false)

func _unhandled_input(event: InputEvent) -> void:
	if not _enabled:
		return

	if event is InputEventMouseMotion:
		_accumulate_mouse_look(event as InputEventMouseMotion)
		return

	if event.is_action_pressed(PlayerInputActions.JUMP):
		_jump_requested = true
		get_viewport().set_input_as_handled()
		return

	if event.is_action_pressed(PlayerInputActions.INTERACT):
		_interact_requested = true
		get_viewport().set_input_as_handled()
		return

	if event.is_action_pressed(PlayerInputActions.PAUSE):
		_pause_requested = true
		get_viewport().set_input_as_handled()

func sample(delta: float) -> PlayerInputFrame:
	var frame := PlayerInputFrame.new()

	if not _enabled:
		return frame

	frame.move = Input.get_vector(
		PlayerInputActions.MOVE_LEFT,
		PlayerInputActions.MOVE_RIGHT,
		PlayerInputActions.MOVE_FORWARD,
		PlayerInputActions.MOVE_BACK,
	)

	var gamepad_look := Input.get_vector(
		PlayerInputActions.LOOK_LEFT,
		PlayerInputActions.LOOK_RIGHT,
		PlayerInputActions.LOOK_UP,
		PlayerInputActions.LOOK_DOWN,
	)

	frame.look_delta = (
		_mouse_look_accumulator
		+ gamepad_look * gamepad_look_speed * delta
	)
	frame.jump_pressed = _jump_requested
	frame.sprint_pressed = Input.is_action_pressed(
		PlayerInputActions.SPRINT
	)
	frame.interact_pressed = _interact_requested
	frame.pause_pressed = _pause_requested

	_mouse_look_accumulator = Vector2.ZERO
	_jump_requested = false
	_interact_requested = false
	_pause_requested = false

	return frame

func set_enabled(value: bool) -> void:
	_enabled = value
	if not _enabled:
		_mouse_look_accumulator = Vector2.ZERO
		_jump_requested = false
		_interact_requested = false
		_pause_requested = false

func _accumulate_mouse_look(event: InputEventMouseMotion) -> void:
	if Input.mouse_mode != Input.MOUSE_MODE_CAPTURED:
		return

	_mouse_look_accumulator += event.relative * mouse_sensitivity
```

### 8.2 Annotations exportées

`@export_range(minimum, maximum, pas)` :

- affiche un champ numérique dans l’Inspector ;
- limite les valeurs choisies dans l’éditeur ;
- documente une plage raisonnable ;
- ne remplace pas une validation de données chargées dynamiquement.

`mouse_sensitivity` multiplie les pixels relatifs de la souris.  
`gamepad_look_speed` exprime une vitesse angulaire approximative en degrés par seconde.

### 8.3 Accumulateur de souris

Une souris émet plusieurs `InputEventMouseMotion` entre deux itérations de physique. Le lecteur additionne `event.relative` dans `_mouse_look_accumulator`, puis remet l’accumulateur à zéro après `sample()`.

Le code ne lit pas `event.position`, car une souris capturée est verrouillée au centre. Godot recommande alors `event.relative`.

### 8.4 `Input.get_vector()`

`Input.get_vector()` reçoit quatre actions :

1. axe X négatif ;
2. axe X positif ;
3. axe Y négatif ;
4. axe Y positif.

Il renvoie un `Vector2` :

- de longueur maximale `1.0` ;
- compatible clavier, croix directionnelle et stick ;
- avec une zone morte circulaire ;
- sans vitesse supérieure en diagonale.

Dans `frame.move` :

- `x < 0` signifie gauche ;
- `x > 0` signifie droite ;
- `y < 0` signifie avant ;
- `y > 0` signifie arrière.

### 8.5 Souris et stick ne suivent pas exactement la même formule

La souris fournit déjà une variation entre deux événements. Elle ne doit pas être multipliée par `delta`.

Le stick fournit un état maintenu entre `-1.0` et `1.0`. Il est multiplié par une vitesse et par `delta` pour obtenir une variation par itération.

### 8.6 Consommer les demandes ponctuelles

Après la création de la trame :

- `_jump_requested` revient à `false` ;
- `_interact_requested` revient à `false` ;
- `_pause_requested` revient à `false` ;
- la même pression ne sera pas rejouée à l’itération suivante.

Le sprint reste interrogé directement, car il doit rester actif tant que l’action est maintenue.

## 9. Construire le moteur du personnage

### 9.1 Scène de base

> **[APP] Godot — Créer `src/features/player/presentation/player_character.tscn`.**

Arbre minimal :

> **[SORTIE] Arbre attendu dans le dock Scene — Ne pas saisir.**

```text
PlayerCharacter (CharacterBody3D)
├── CollisionShape3D
├── VisualRoot (Node3D)
├── PlayerInputReader (Node)
├── CameraRig (Node3D)
│   └── PitchPivot (Node3D)
│       └── SpringArm3D
│           └── Camera3D
│               └── PlayerInteractor (Node3D)
│                   └── InteractionRay (RayCast3D)
└── PlayerController (Node)
```

Le `CollisionShape3D` doit utiliser une capsule adaptée au modèle. La racine du personnage reste un `CharacterBody3D`.

### 9.2 Script du moteur

> **[VSC] Visual Studio Code — Créer : `src/features/player/movement/player_motor.gd`.**

```gdscript
class_name PlayerMotor
extends CharacterBody3D

@export_range(0.1, 20.0, 0.1)
var walk_speed := 5.0

@export_range(1.0, 3.0, 0.05)
var sprint_multiplier := 1.6

@export_range(0.1, 100.0, 0.1)
var ground_acceleration := 24.0

@export_range(0.1, 100.0, 0.1)
var air_acceleration := 8.0

@export_range(0.1, 30.0, 0.1)
var jump_velocity := 7.0

var gravity: float = float(
	ProjectSettings.get_setting("physics/3d/default_gravity")
)

func apply_input(
	frame: PlayerInputFrame,
	camera_basis: Basis,
	delta: float,
) -> void:
	if frame == null:
		push_error("PlayerMotor exige une PlayerInputFrame.")
		return

	var forward := -camera_basis.z
	var right := camera_basis.x

	forward.y = 0.0
	right.y = 0.0
	forward = forward.normalized()
	right = right.normalized()

	var desired_direction := (
		right * frame.move.x
		+ forward * -frame.move.y
	).normalized()

	var target_speed := walk_speed
	if frame.sprint_pressed:
		target_speed *= sprint_multiplier

	var target_velocity := desired_direction * target_speed
	var acceleration := (
		ground_acceleration
		if is_on_floor()
		else air_acceleration
	)

	velocity.x = move_toward(
		velocity.x,
		target_velocity.x,
		acceleration * delta,
	)
	velocity.z = move_toward(
		velocity.z,
		target_velocity.z,
		acceleration * delta,
	)

	if not is_on_floor():
		velocity.y -= gravity * delta
	elif frame.jump_pressed:
		velocity.y = jump_velocity

	move_and_slide()
```

### 9.3 `CharacterBody3D.velocity`

`velocity` appartient à `CharacterBody3D`.

Elle représente généralement une vitesse en mètres par seconde. Il ne faut pas multiplier toute la propriété par `delta` avant `move_and_slide()`. La méthode utilise déjà le pas de physique pour calculer le déplacement.

### 9.4 Base de caméra

Une `Basis` contient les trois axes d’une transformation 3D :

- `basis.x` : droite locale ;
- `basis.y` : haut local ;
- `basis.z` : arrière local dans la convention Godot ;
- `-basis.z` : avant local.

Le code retire la composante `y` pour empêcher la caméra inclinée vers le ciel de faire monter le personnage.

### 9.5 Pourquoi `-frame.move.y`

`Input.get_vector()` produit une valeur négative pour l’action `move_forward`. La direction avant du monde est déjà `-basis.z`.

La formule utilise donc `forward * -frame.move.y` :

- `frame.move.y == -1` ;
- `-frame.move.y == 1` ;
- le personnage avance dans la direction `forward`.

### 9.6 Accélération et `move_toward()`

`move_toward(valeur_actuelle, cible, variation_maximale)` rapproche progressivement la vitesse de la cible.

- sur le sol, `ground_acceleration` donne une réponse rapide ;
- dans l’air, `air_acceleration` réduit le contrôle ;
- multiplier l’accélération par `delta` rend le changement indépendant de la fréquence de physique.

### 9.7 Gravité et saut

- `is_on_floor()` décrit le résultat du dernier `move_and_slide()` ;
- lorsque le personnage est en l’air, la vitesse verticale diminue ;
- un saut est accepté seulement si le corps est au sol ;
- `jump_velocity` est positive, car `Vector3.UP` suit l’axe Y positif.

## 10. Construire la caméra à la troisième personne

### 10.1 Arbre de caméra

La caméra est enfant direct de `SpringArm3D`. Cette disposition permet au spring arm d’utiliser la forme de la caméra et de la rapprocher lorsqu’un obstacle se trouve derrière le joueur.

Configurer :

> **[APP] Godot — Sélectionner `SpringArm3D` dans `player_character.tscn`.**

- `spring_length` : `4.0` ;
- `margin` : `0.1` ;
- masque de collision : décor et obstacles ;
- exclure la couche du joueur si les couches suffisent.

> **[APP] Godot — Sélectionner `Camera3D`.**

- `current` : activé ;
- `fov` : `70` à `75` selon le confort ;
- `near` : conserver une valeur raisonnable afin d’éviter le clipping.

Une seule `Camera3D` est active par `Viewport`.

### 10.2 Script du rig

> **[VSC] Visual Studio Code — Créer : `src/features/player/camera/third_person_camera_rig.gd`.**

```gdscript
class_name ThirdPersonCameraRig
extends Node3D

@export_range(-89.0, -5.0, 1.0)
var minimum_pitch_degrees := -70.0

@export_range(5.0, 89.0, 1.0)
var maximum_pitch_degrees := 65.0

@onready var _pitch_pivot: Node3D = $PitchPivot
@onready var _spring_arm: SpringArm3D = $PitchPivot/SpringArm3D
@onready var _camera: Camera3D = $PitchPivot/SpringArm3D/Camera3D

var _pitch_radians := 0.0

func _ready() -> void:
	_camera.current = true

	var player_body := get_parent() as CollisionObject3D
	if player_body != null:
		_spring_arm.add_excluded_object(player_body.get_rid())

func apply_look(look_delta: Vector2) -> void:
	rotate_y(deg_to_rad(-look_delta.x))

	_pitch_radians = clamp(
		_pitch_radians + deg_to_rad(-look_delta.y),
		deg_to_rad(minimum_pitch_degrees),
		deg_to_rad(maximum_pitch_degrees),
	)
	_pitch_pivot.rotation.x = _pitch_radians

func get_movement_basis() -> Basis:
	return global_transform.basis

func get_camera() -> Camera3D:
	return _camera
```

### 10.3 Lacet et tangage

- le **lacet** ou yaw tourne autour de Y ;
- le **tangage** ou pitch tourne autour de X ;
- le rig racine gère le lacet ;
- `PitchPivot` gère le tangage ;
- cette séparation évite d’incliner tout le personnage.

### 10.4 Conversion en radians

Les angles visibles dans l’Inspector sont exprimés en degrés. Les propriétés de rotation de `Node3D` utilisent des radians.

`deg_to_rad()` réalise la conversion.

### 10.5 Limiter le tangage

`clamp(valeur, minimum, maximum)` empêche la caméra :

- de passer au-dessus de la verticale ;
- de se retourner ;
- de produire un contrôle désorientant.

Les limites doivent rester configurables pour l’accessibilité.

### 10.6 Exclure le personnage du spring arm

`get_rid()` renvoie l’identifiant du corps dans le serveur physique.  
`add_excluded_object()` empêche le spring arm de considérer ce corps comme un obstacle.

Cette exclusion complète, mais ne remplace pas, une bonne configuration des couches de collision.

## 11. Capturer et libérer la souris

### 11.1 Capture initiale

> **[VSC] Visual Studio Code — Ajouter au contrôleur joueur.**

```gdscript
func capture_mouse() -> void:
	Input.mouse_mode = Input.MOUSE_MODE_CAPTURED

func release_mouse() -> void:
	Input.mouse_mode = Input.MOUSE_MODE_VISIBLE
```

- `MOUSE_MODE_CAPTURED` masque le curseur et le verrouille au centre ;
- `MOUSE_MODE_VISIBLE` rend le curseur à l’interface ;
- le lecteur utilise `InputEventMouseMotion.relative` uniquement pendant la capture.

### 11.2 Pause

La pause doit :

1. désactiver le lecteur d’entrée de gameplay ;
2. libérer la souris ;
3. afficher le menu ;
4. donner le focus à un contrôle ;
5. restaurer la capture à la fermeture.

Le chapitre ne construit pas encore tout le menu de pause. Il définit le contrat requis.

## 12. Construire le contrôleur joueur

> **[VSC] Visual Studio Code — Créer : `src/features/player/presentation/player_controller.gd`.**

```gdscript
class_name PlayerController
extends Node

signal pause_requested

@export var motor_path: NodePath = ^".."
@export var input_reader_path: NodePath = ^"../PlayerInputReader"
@export var camera_rig_path: NodePath = ^"../CameraRig"
@export var interactor_path: NodePath = ^"../CameraRig/PitchPivot/SpringArm3D/Camera3D/PlayerInteractor"

@onready var _motor := get_node_or_null(motor_path) as PlayerMotor
@onready var _input_reader := (
	get_node_or_null(input_reader_path) as PlayerInputReader
)
@onready var _camera_rig := (
	get_node_or_null(camera_rig_path) as ThirdPersonCameraRig
)
@onready var _interactor := (
	get_node_or_null(interactor_path) as PlayerInteractor
)

func _ready() -> void:
	if not _validate_dependencies():
		set_physics_process(false)
		return

	_input_reader.set_enabled(true)
	Input.mouse_mode = Input.MOUSE_MODE_CAPTURED

func _physics_process(delta: float) -> void:
	var frame := _input_reader.sample(delta)

	if frame.pause_pressed:
		pause_requested.emit()
		return

	_camera_rig.apply_look(frame.look_delta)
	_motor.apply_input(
		frame,
		_camera_rig.get_movement_basis(),
		delta,
	)

	if frame.interact_pressed:
		_interactor.try_interact(_motor)

func set_gameplay_enabled(value: bool) -> void:
	_input_reader.set_enabled(value)
	set_physics_process(value)

func _validate_dependencies() -> bool:
	var valid := true

	if _motor == null:
		push_error("PlayerController : PlayerMotor absent.")
		valid = false
	if _input_reader == null:
		push_error("PlayerController : PlayerInputReader absent.")
		valid = false
	if _camera_rig == null:
		push_error("PlayerController : ThirdPersonCameraRig absent.")
		valid = false
	if _interactor == null:
		push_error("PlayerController : PlayerInteractor absent.")
		valid = false

	return valid
```

### 12.1 Chemins exportés

Les `NodePath` sont exportés afin que la scène puisse être réorganisée sans coder chaque chemin dans plusieurs fonctions.

Un chemin exporté reste une dépendance forte. `_validate_dependencies()` transforme une mauvaise configuration en erreur claire au démarrage.

### 12.2 Ordre de l’itération

À chaque `_physics_process(delta)` :

1. le lecteur produit une trame ;
2. une demande de pause est émise avant le gameplay ;
3. la caméra applique le regard ;
4. le moteur utilise la nouvelle orientation ;
5. l’interaction ponctuelle est traitée.

Le déplacement est ainsi relatif à la caméra de la même itération.

### 12.3 Pourquoi le contrôleur ne lit pas directement `Input`

Le contrôleur reçoit une `PlayerInputFrame`. Il pourra donc plus tard recevoir :

- une trame de test ;
- une trame enregistrée ;
- une intention issue d’un réseau ;
- une intention issue d’un agent IA.

## 13. Définir une cible d’interaction

### 13.1 Composant `InteractionTarget`

> **[VSC] Visual Studio Code — Créer : `src/features/interactions/domain/interaction_target.gd`.**

```gdscript
class_name InteractionTarget
extends Area3D

signal interaction_accepted(actor: Node3D)

@export_multiline var prompt := "Interagir"
@export var enabled := true

func get_prompt() -> String:
	return prompt if enabled else ""

func interact(actor: Node3D) -> bool:
	if not enabled:
		return false

	if actor == null:
		push_warning("Interaction refusée : acteur absent.")
		return false

	interaction_accepted.emit(actor)
	return true
```

Explication :

- `Area3D` permet de posséder une forme de collision détectable ;
- `interaction_accepted` confirme une interaction réellement acceptée ;
- `@export_multiline` facilite l’édition d’un texte plus long ;
- `enabled` permet de désactiver la cible sans supprimer le nœud ;
- `get_prompt()` renvoie une chaîne vide si l’action est indisponible ;
- `interact(actor)` reçoit l’acteur responsable ;
- le retour `bool` distingue acceptation et refus ;
- le signal transmet l’acteur aux détails internes de l’objet.

La cible ne connaît pas le contrôleur joueur. Elle expose un contrat limité.

### 13.2 Couches de collision

Réserver une couche physique nommée `Interactable`.

Configurer la cible :

> **[APP] Godot — Dans l’Inspector de `InteractionTarget`.**

- `monitorable` : activé ;
- couche : `Interactable` ;
- masque : selon les besoins de proximité ;
- ajouter un `CollisionShape3D`.

Le rayon du joueur doit activer `collide_with_areas` et viser la couche `Interactable`.

## 14. Interaction par `RayCast3D`

### 14.1 Configurer le rayon

> **[APP] Godot — Sélectionner `InteractionRay` dans `player_character.tscn`.**

- `enabled` : activé ;
- `target_position` : `(0, 0, -3)` ;
- `collide_with_areas` : activé ;
- `collide_with_bodies` : désactivé si seules les cibles `Area3D` comptent ;
- masque : couche `Interactable`.

Dans l’arbre proposé, `PlayerInteractor` et `InteractionRay` sont des descendants de `Camera3D`. Le rayon suit donc automatiquement la position et l’orientation de la caméra.

### 14.2 Script de l’interactor

> **[VSC] Visual Studio Code — Créer : `src/features/interactions/presentation/player_interactor.gd`.**

```gdscript
class_name PlayerInteractor
extends Node3D

signal focus_changed(prompt: String)
signal interaction_completed(target: InteractionTarget)

@onready var _ray: RayCast3D = $InteractionRay

var _current_target: InteractionTarget

func _physics_process(_delta: float) -> void:
	_refresh_target()

func try_interact(actor: Node3D) -> bool:
	if _current_target == null:
		return false

	var accepted := _current_target.interact(actor)
	if accepted:
		interaction_completed.emit(_current_target)

	return accepted

func _refresh_target() -> void:
	var next_target: InteractionTarget

	if _ray.is_colliding():
		next_target = _ray.get_collider() as InteractionTarget

	if next_target == _current_target:
		return

	_current_target = next_target
	var prompt := ""

	if _current_target != null:
		prompt = _current_target.get_prompt()

	focus_changed.emit(prompt)
```

### 14.3 Résultat du rayon

`RayCast3D` calcule son résultat à chaque itération de physique et le conserve jusqu’à l’itération suivante.

- `is_colliding()` indique si le rayon touche quelque chose ;
- `get_collider()` renvoie un type général ;
- `as InteractionTarget` tente un cast ;
- le résultat est `null` si le collider n’est pas une cible compatible.

### 14.4 Changement de focus

Le signal `focus_changed(prompt)` n’est émis que lorsque la cible change.

Cela évite :

- de mettre l’interface à jour à chaque frame ;
- d’émettre le même texte en continu ;
- de multiplier les allocations inutiles.

Une chaîne vide signifie qu’aucune invite ne doit être affichée.

### 14.5 Appel pendant la physique

Le contrôleur appelle `try_interact()` depuis `_physics_process()`. Le résultat du rayon est donc cohérent avec l’état physique courant.

Pour une reconfiguration du rayon plusieurs fois dans la même itération, `force_raycast_update()` existe, mais il n’est pas nécessaire dans l’exercice normal.

## 15. Alternative : interaction de proximité avec `Area3D`

Une zone convient mieux lorsque :

- le joueur n’a pas besoin de viser précisément ;
- plusieurs objets proches peuvent être sélectionnés ;
- une interaction doit s’activer dès l’entrée ;
- l’accessibilité exige une zone généreuse.

Un `Area3D` joueur peut écouter :

- `area_entered(area)` ;
- `area_exited(area)`.

Le signal exige `monitoring == true`.

> **[VSC] Visual Studio Code — Exemple de registre de proximité à adapter.**

```gdscript
var nearby_targets: Array[InteractionTarget] = []

func _on_area_entered(area: Area3D) -> void:
	var target := area as InteractionTarget
	if target == null or nearby_targets.has(target):
		return

	nearby_targets.append(target)

func _on_area_exited(area: Area3D) -> void:
	var target := area as InteractionTarget
	if target == null:
		return

	nearby_targets.erase(target)
```

Cette alternative doit ensuite définir une règle de sélection :

- plus proche ;
- au centre de l’écran ;
- priorité explicite ;
- dernier objet entré.

Le présent chapitre ne combine pas automatiquement rayon et proximité afin de garder une règle prévisible.

## 16. Relier une balise à l’interaction

Ajouter un enfant `InteractionTarget` à la scène `StatusBeacon`, puis connecter son signal.

> **[VSC] Visual Studio Code — Ajouter au script de la scène de démonstration.**

```gdscript
func _on_beacon_interaction_accepted(actor: Node3D) -> void:
	var actor_name := StringName(actor.name)
	var accepted := demo_beacon.activate(actor_name)

	if not accepted:
		result_label.text = "Balise indisponible"
```

- `actor.name` est une chaîne de nœud ;
- `StringName(actor.name)` convertit cette valeur pour la signature de `activate()` ;
- `accepted` reçoit le retour du chapitre 3 ;
- l’interface affiche un refus sans modifier directement l’état interne de la balise.

Le bus global du chapitre 5 n’est pas obligatoire pour une interaction locale entre composants de la même scène.

## 17. Remappage des commandes

### 17.1 Modifier l’Input Map en mémoire

> **[VSC] Visual Studio Code — Créer : `src/features/settings/input/input_rebinder.gd`.**

```gdscript
class_name InputRebinder
extends RefCounted

func replace_events(
	action: StringName,
	events: Array[InputEvent],
) -> bool:
	if not InputMap.has_action(action):
		push_error("Action inconnue : %s" % action)
		return false

	if events.is_empty():
		push_warning("Aucune liaison fournie pour : %s" % action)
		return false

	InputMap.action_erase_events(action)

	for event: InputEvent in events:
		InputMap.action_add_event(action, event)

	return true

func get_events(action: StringName) -> Array[InputEvent]:
	if not InputMap.has_action(action):
		return []

	return InputMap.action_get_events(action)
```

Explication :

- `replace_events()` remplace toutes les liaisons d’une action ;
- `Array[InputEvent]` accepte clavier, souris, bouton ou axe ;
- la fonction refuse de rendre une action vide ;
- `action_erase_events()` supprime les anciennes liaisons ;
- `action_add_event()` ajoute chaque nouvel événement ;
- la modification concerne l’Input Map chargée en mémoire.

La sauvegarde sur disque et la migration des préférences appartiennent aux chapitres 7 et 9.

### 17.2 Capturer une nouvelle touche

Un écran de remappage doit :

1. entrer dans un mode d’écoute ;
2. recevoir un `InputEventKey`, `InputEventMouseButton` ou `InputEventJoypadButton` ;
3. ignorer les événements de relâchement et les répétitions ;
4. détecter les conflits ;
5. demander confirmation ;
6. appliquer la nouvelle liaison ;
7. permettre l’annulation au clavier et à la manette.

Ne pas supprimer la seule action permettant de fermer ou confirmer le menu sans proposer une voie de secours.

## 18. Zones mortes et manettes

Godot prend en charge clavier et manette à travers les mêmes actions. Depuis Godot 4.5, les plateformes de bureau utilisent SDL 3 pour la prise en charge des contrôleurs.

### 18.1 Zone morte

Un stick physique ne revient pas toujours exactement à zéro. Une petite valeur persistante s’appelle le **drift**.

Une zone morte :

- ignore les faibles valeurs ;
- évite un déplacement involontaire ;
- ne doit pas être si haute qu’elle masque une intention réelle.

`Input.get_vector()` applique une zone morte circulaire. Une valeur initiale de `0.20` est un point de départ, pas une constante universelle.

### 18.2 Connexion et déconnexion

Le signal `Input.joy_connection_changed(device, connected)` permet d’informer l’interface lorsqu’une manette change d’état.

Le jeu doit :

- conserver le clavier comme voie de secours ;
- ne pas supposer qu’une manette particulière est disponible ;
- afficher les glyphes adaptés lorsque cette fonction sera développée ;
- ne pas rendre la vibration obligatoire.

### 18.3 Vibration

La vibration est facultative et doit disposer :

- d’un interrupteur ;
- d’une intensité réglable ;
- d’une durée limitée ;
- d’une valeur par défaut prudente.

Le présent chapitre ne l’active pas dans l’exercice.

## 19. Accessibilité et confort

Prévoir dès maintenant :

- remappage clavier et manette ;
- inversion séparée de l’axe vertical ;
- sensibilité souris et manette séparées ;
- zone morte réglable ;
- marche et sprint en maintien ou bascule ;
- interaction par pression ou maintien configurable ;
- assistance de ciblage facultative ;
- taille et contraste de l’invite ;
- réduction ou désactivation de la vibration ;
- FOV réglable dans une plage testée ;
- vitesse de caméra plafonnée ;
- possibilité de libérer la souris ;
- commandes navigables sans souris.

Une option d’accessibilité ne doit pas modifier silencieusement la difficulté sans l’expliquer.

## 20. Assemblage par `AppBootstrap`

Le bootstrap du chapitre 5 doit injecter les services transversaux. Les dépendances internes à la scène peuvent rester des références de scène validées.

Exemple de responsabilité du bootstrap :

> **[LECTURE] Pseudo-code d’assemblage — Ne pas recopier tel quel.**

```text
créer PlayerCharacter
obtenir PlayerController
injecter éventuellement GameEventBus
ajouter le personnage à la scène de jeu
activer le gameplay après chargement
```

Le contrôleur ne doit pas appeler `AppRuntime` à chaque frame. Toute dépendance globale nécessaire est fournie une seule fois lors de l’assemblage.

## 21. Vérifications et diagnostic

### 21.1 Validation dans Godot

> **[APP] Godot — Exécuter `player_character.tscn` dans une scène de test.**

Vérifier :

1. déplacement identique au clavier et au stick ;
2. diagonale non accélérée ;
3. saut uniquement au sol ;
4. gravité stable ;
5. caméra limitée verticalement ;
6. spring arm qui évite un mur ;
7. souris capturée pendant le gameplay ;
8. interface capable de consommer les clics ;
9. invite d’interaction affichée seulement sur une cible ;
10. interaction refusée lorsque la cible est désactivée ;
11. absence de double connexion ;
12. aucune erreur après la fermeture de la scène.

### 21.2 Vérification headless future

> **[PS] PowerShell 7 — Depuis la racine du projet Godot matérialisé.**

```powershell
godot --headless --path . --editor --quit-after 2
```

Cette commande peut détecter :

- erreur d’analyse GDScript ;
- chemin de ressource invalide ;
- classe globale manquante ;
- scène non chargeable.

Elle ne valide pas :

- la sensation du déplacement ;
- la zone morte réelle d’une manette ;
- le confort de la caméra ;
- la collision du spring arm ;
- l’ergonomie du remappage.

### 21.3 Symptômes fréquents

<!-- qa:error-correction-index -->

Ce tableau constitue un index de diagnostic rapide. Les exemples fautifs et corrigés détaillés se trouvent dans la section 22 ; les lignes propres au confort de caméra, aux couches physiques ou au matériel renvoient aussi aux sections techniques correspondantes du chapitre.

| Symptôme | Cause probable | Vérification |
|---|---|---|
| le personnage avance quand on recule | signe Y inversé deux fois | inspecter `-frame.move.y` |
| déplacement diagonal trop rapide | vecteurs additionnés sans limite | utiliser `Input.get_vector()` |
| vitesse dépendante du FPS | logique dans `_process()` | déplacer la physique dans `_physics_process()` |
| chute trop lente | gravité multipliée deux fois par `delta` | vérifier `velocity.y -= gravity * delta` |
| caméra retournée | tangage non limité | vérifier `clamp()` |
| caméra touche le joueur | corps non exclu | vérifier couches et `add_excluded_object()` |
| clic UI déclenche Interagir | lecture dans `_input()` | utiliser `_unhandled_input()` |
| drift de manette | zone morte trop faible | ajuster l’Input Map |
| aucun objet ciblé | mauvais masque de collision | vérifier couche `Interactable` |
| interaction répétée | événement maintenu utilisé comme ponctuel | consommer la demande dans la trame |

## 22. Anti-patterns et corrections

<!-- qa:error-correction-section -->

La section 21.3 reste un index de symptômes. Les cas ci-dessous constituent les explications détaillées exigées par la règle pédagogique.

### 22.1 Touches codées en dur

**Symptôme ou risque :** le gameplay dépend directement d’une touche physique et ne peut pas être remappé.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
if event is InputEventKey and event.keycode == KEY_E:
	try_interact()
```

**Correction :** interroger une action logique définie dans l’Input Map.

> **[VSC] Visual Studio Code — Exemple corrigé dans `_unhandled_input()`.**

```gdscript
if event.is_action_pressed(&'interact'):
	try_interact()
```

**Différence :** l’action corrigée peut recevoir plusieurs touches ou boutons et être remappée sans modifier le gameplay.

### 22.2 Déplacement dans `_input()`

**Symptôme ou risque :** la position change une fois par événement reçu, donc selon le périphérique et sa fréquence.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
func _input(event: InputEvent) -> void:
	if event.is_action(&'move_forward'):
		position.z -= speed
```

**Correction :** lire l’intention puis appliquer le mouvement pendant le pas physique.

> **[VSC] Visual Studio Code — Exemple corrigé avec séparation des responsabilités.**

```gdscript
func _physics_process(delta: float) -> void:
	var frame := input_reader.sample(delta)
	motor.apply_input(frame, delta)
```

**Différence :** la version corrigée produit une vitesse stable à chaque tick physique au lieu de dépendre du nombre d’événements.

### 22.3 Multiplier `velocity` par `delta`

**Symptôme ou risque :** la vitesse finale est transformée en déplacement avant `move_and_slide()`.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
velocity = direction * speed * delta
move_and_slide()
```

**Correction :** conserver une vitesse en unités par seconde et multiplier seulement les accélérations par `delta`.

> **[VSC] Visual Studio Code — Exemple corrigé pour `CharacterBody3D`.**

```gdscript
velocity.x = direction.x * speed
velocity.z = direction.z * speed
velocity.y -= gravity * delta
move_and_slide()
```

**Différence :** `move_and_slide()` utilise déjà le pas physique pour la vitesse ; seul le changement de vitesse dû à la gravité dépend ici de `delta`.

### 22.4 Une classe qui lit les entrées et modifie tout

**Symptôme ou risque :** un seul script interroge les touches, tourne la caméra, déplace le corps et déclenche les interactions.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
func _physics_process(delta: float) -> void:
	read_keyboard()
	rotate_camera()
	move_character(delta)
	check_interaction()
	update_ui()
```

**Correction :** déléguer à des composants spécialisés reliés par un contrôleur.

> **[VSC] Visual Studio Code — Exemple corrigé dans `PlayerController`.**

```gdscript
func _physics_process(delta: float) -> void:
	var frame := input_reader.sample(delta)
	camera_rig.apply_look(frame.look, delta)
	motor.apply_input(frame, delta)
	interactor.try_interact(frame.interact_pressed)
```

**Différence :** le contrôleur corrigé orchestre des contrats séparés ; chaque composant peut évoluer et être testé indépendamment.

### 22.5 Bus global pour une interaction locale

**Symptôme ou risque :** une balise et son contrôleur de scène communiquent par un événement transversal.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
_events.event_published.emit('local_beacon_clicked', {'id': id})
```

**Correction :** utiliser un signal direct ou un appel entre composants de la même fonctionnalité.

> **[VSC] Visual Studio Code — Exemple corrigé avec signal local typé.**

```gdscript
interaction_target.accepted.connect(_on_beacon_interaction_accepted)
```

**Différence :** la connexion corrigée rend l’émetteur et le récepteur visibles dans la scène ; le bus n’ajoute aucune valeur pour ce trajet local.

### 22.6 Interaction par nom de méthode libre

**Symptôme ou risque :** n’importe quel objet possédant une méthode du même nom est appelé sans contrat de signature.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
if collider.has_method('interact'):
	collider.call('interact', player)
```

**Correction :** utiliser un composant ou une classe typée représentant une cible interactive.

> **[VSC] Visual Studio Code — Exemple corrigé avec cast.**

```gdscript
var target := collider as InteractionTarget
if target != null:
	target.interact(player)
```

**Différence :** le cast corrigé vérifie le type attendu et l’éditeur connaît la méthode publique et ses paramètres.

### 22.7 Caméra enfant directe du personnage sans pivot

**Symptôme ou risque :** le même transform mélange rotation horizontale, verticale et déplacement du corps.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```text
PlayerCharacter
└── Camera3D
```

**Correction :** séparer le lacet, le tangage et l’évitement d’obstacles dans un rig.

> **[LECTURE] Arbre corrigé de caméra — Ne pas saisir.**

```text
PlayerCharacter
└── CameraYaw
    └── CameraPitch
        └── SpringArm3D
            └── Camera3D
```

**Différence :** chaque nœud corrigé porte un axe ou une responsabilité, ce qui permet de limiter le tangage sans incliner le personnage.

### 22.8 Remappage destructif sans voie de secours

**Symptôme ou risque :** les événements existants sont effacés avant de vérifier la nouvelle liste.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
InputMap.action_erase_events(action)
for event in events:
	InputMap.action_add_event(action, event)
```

**Correction :** valider l’action et conserver au moins une liaison avant toute suppression.

> **[VSC] Visual Studio Code — Exemple corrigé avec garde préalable.**

```gdscript
if not InputMap.has_action(action) or events.is_empty():
	return false

InputMap.action_erase_events(action)
for event: InputEvent in events:
	InputMap.action_add_event(action, event)
return true
```

**Différence :** la version corrigée ne détruit jamais la dernière commande lorsque la proposition est vide ou l’action inconnue.

## 23. Parcours Solo

Le parcours Solo utilise :

- une seule scène joueur ;
- un `PlayerInputReader` ;
- un `PlayerInputFrame` ;
- un `PlayerMotor` ;
- un rig de caméra ;
- un `PlayerInteractor` ;
- une cible typée ;
- une page de configuration simple ;
- des chemins exportés validés.

Les réglages peuvent rester dans les paramètres du projet jusqu’au chapitre 7.

## 24. Parcours Studio

Le parcours Studio ajoute :

- une matrice de périphériques pris en charge ;
- des propriétaires de modules ;
- une convention de nommage des actions ;
- des profils de commandes ;
- une stratégie de glyphes ;
- une campagne manettes ;
- des tests de clavier ghosting ;
- des tests de focus de fenêtre ;
- des critères d’accessibilité ;
- une scène laboratoire pour caméra et interactions ;
- des métriques de confort documentées ;
- une revue de collision layers/masks.

> **[VSC] Visual Studio Code — Créer : `docs/architecture/input-contract.md`.**

Le document doit lister :

- action ;
- intention ;
- périphériques par défaut ;
- état maintenu ou événement ponctuel ;
- consommateur ;
- contexte actif ;
- possibilité de remappage ;
- comportement pendant la pause ;
- exigence d’accessibilité.

## 25. Checklist d’audit

- [ ] Toutes les actions existent dans l’Input Map.
- [ ] Aucun code de gameplay ne dépend d’une touche physique.
- [ ] Les événements ponctuels sont consommés une fois.
- [ ] Le mouvement est interrogé pendant la physique.
- [ ] `Input.get_vector()` gère les diagonales et zones mortes.
- [ ] La souris et le stick utilisent des formules adaptées.
- [ ] Le moteur ne multiplie pas sa vitesse finale par `delta`.
- [ ] Les dépendances du contrôleur sont validées.
- [ ] La caméra limite le tangage.
- [ ] Le spring arm exclut le personnage.
- [ ] Les interactions utilisent une cible typée.
- [ ] Les couches et masques sont documentés.
- [ ] Le remappage conserve une voie de secours.
- [ ] Les paramètres d’accessibilité sont identifiés.
- [ ] Les fonctions et paramètres nouveaux sont expliqués.
- [ ] Les repères d’utilisation sont présents.
- [ ] Les frontières des chapitres suivants sont respectées.
- [ ] Le rapport `Livre-II/QA/AUDIT-CHAPITRE-06.md` est à jour.
- [ ] Aucun PDF intermédiaire n’a été construit.

## 26. Résultat attendu

À la fin du chapitre, `Project Asteria` dispose d’une architecture documentée pour :

- lire clavier, souris et manette ;
- produire une intention indépendante du périphérique ;
- déplacer un personnage 3D avec une physique stable ;
- orienter la caméra et le déplacement de façon cohérente ;
- éviter les obstacles de caméra ;
- sélectionner et activer une cible ;
- préparer le remappage ;
- intégrer les besoins d’accessibilité ;
- injecter les dépendances depuis le composition root.

Le statut reste `static-review` tant que les scènes et scripts ne sont pas matérialisés dans le Starter Kit et testés avec de vrais périphériques.

## 27. Sources officielles

- Godot Engine, **Input examples**, documentation 4.7 : <https://docs.godotengine.org/en/4.7/tutorials/inputs/input_examples.html>
- Godot Engine, **Using InputEvent**, documentation 4.x : <https://docs.godotengine.org/fr/4.x/tutorials/inputs/inputevent.html>
- Godot Engine, **Controllers, gamepads, and joysticks**, documentation 4.7 : <https://docs.godotengine.org/en/4.7/tutorials/inputs/controllers_gamepads_joysticks.html>
- Godot Engine, **InputMap**, référence 4.x : <https://docs.godotengine.org/fr/4.x/classes/class_inputmap.html>
- Godot Engine, **Input**, référence 4.x : <https://docs.godotengine.org/fr/4.x/classes/class_input.html>
- Godot Engine, **CharacterBody3D**, référence 4.x : <https://docs.godotengine.org/fr/4.x/classes/class_characterbody3d.html>
- Godot Engine, **Camera3D**, référence 4.7 : <https://docs.godotengine.org/en/4.7/classes/class_camera3d.html>
- Godot Engine, **Third-person camera with spring arm**, documentation 4.7 : <https://docs.godotengine.org/en/4.7/tutorials/3d/spring_arm.html>
- Godot Engine, **Ray-casting**, documentation 4.x : <https://docs.godotengine.org/fr/4.x/tutorials/physics/ray-casting.html>
- Godot Engine, **Area3D**, référence 4.x : <https://docs.godotengine.org/fr/4.x/classes/class_area3d.html>
