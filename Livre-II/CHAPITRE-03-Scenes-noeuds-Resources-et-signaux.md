---
title: "Livre II — Chapitre 3 : Scènes, nœuds, Resources et signaux"
id: "DOC-L2-CH03"
status: "reviewed"
version: "1.1.0"
lang: "fr-FR"
book: "Livre II"
chapter: 3
last-verified: "2026-07-18"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-03.md"
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

# Scènes, nœuds, Resources et signaux

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir, **[LECTURE]** exemple à étudier. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH03`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Niveau de raisonnement conseillé pour produire ou réviser ce chapitre :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-03.md`.

## 1. Rôle du chapitre

Les chapitres précédents ont créé le projet Godot et introduit le langage GDScript. Le présent chapitre explique comment Godot organise réellement un jeu : des **nœuds** sont assemblés en **scènes**, ces scènes sont instanciées dans un **SceneTree**, leurs éléments communiquent avec des **signaux**, et leurs données réutilisables peuvent être placées dans des **Resources**.

À la fin du chapitre, le lecteur doit savoir :

- distinguer un nœud, une scène enregistrée et une instance en mémoire ;
- lire et construire un arbre de scène ;
- comprendre les relations parent, enfant, racine, branche et propriétaire ;
- récupérer une référence avec `get_node()`, `$`, `%NomUnique` ou une propriété exportée ;
- instancier une `PackedScene` et l’ajouter à l’arbre actif ;
- comprendre l’ordre de `_init()`, `_enter_tree()`, `_ready()` et `_exit_tree()` ;
- connecter un signal intégré et déclarer un signal personnalisé ;
- comprendre ce qu’est un `Callable` ;
- créer une `Resource` personnalisée éditable dans l’Inspector ;
- éviter les références fragiles et les connexions en double ;
- construire une petite fonctionnalité réutilisable pour `Project Asteria`.

## 2. Prérequis

Le lecteur doit avoir terminé :

- le chapitre 1 pour disposer d’un projet Godot fonctionnel ;
- le chapitre 2 pour comprendre variables, types, fonctions, paramètres, retours, classes, `@export`, `@onready`, `preload()` et `await`.

Ce chapitre rappelle brièvement ces notions lorsque leur combinaison crée un nouveau concept. Il ne répète pas leur cours complet.

## 3. Périmètre et frontières

Ce chapitre couvre les communications **locales** entre les éléments d’une scène ou entre quelques scènes directement liées.

Il ne définit pas encore :

- l’architecture modulaire complète du projet — chapitre 4 ;
- les services globaux, Autoloads, bus d’événements et injection de dépendances — chapitre 5 ;
- le contrôleur du joueur et les interactions physiques complètes — chapitre 6 ;
- la stratégie générale des données, catalogues JSON et Resources de conception — chapitre 7 ;
- la persistance et les migrations — chapitres 8 et 9.

Une bonne frontière pour ce chapitre est la suivante :

> Une scène peut exposer une petite interface publique et des signaux. Elle ne doit pas connaître toute l’application.

## 4. Vocabulaire fondamental

### 4.1 Nœud

Un `Node` est une unité active de l’arbre Godot. Selon son type, il peut :

- représenter une position 3D avec `Node3D` ;
- afficher une interface avec `Control` ;
- jouer un son avec `AudioStreamPlayer` ;
- attendre une durée avec `Timer` ;
- détecter une zone avec `Area3D` ;
- porter un script et du comportement personnalisé.

Chaque nœud possède notamment :

- un nom ;
- un type ;
- des propriétés ;
- éventuellement un parent ;
- zéro, un ou plusieurs enfants ;
- des fonctions de cycle de vie ;
- des signaux.

### 4.2 Arbre de scène

Des nœuds reliés par des relations parent-enfant forment un arbre.

> **[LECTURE] Structure conceptuelle - Ne pas saisir.**

```text
StatusBeacon                    ← racine de la scène
├── StatusLabel                 ← enfant direct
└── CooldownTimer               ← enfant direct
```

Dans cet exemple :

- `StatusBeacon` est le parent de `StatusLabel` et de `CooldownTimer` ;
- `StatusLabel` et `CooldownTimer` sont frères, car ils partagent le même parent ;
- l’ensemble forme une branche réutilisable ;
- le premier nœud est la racine de cette scène.

### 4.3 Scène

Une scène Godot est un arbre de nœuds enregistré comme une ressource, généralement dans un fichier `.tscn` lisible par Git ou un fichier `.scn` binaire.

Une scène :

- possède exactement une racine ;
- peut être enregistrée sur disque ;
- peut être ouverte et modifiée dans l’éditeur ;
- peut être instanciée plusieurs fois ;
- peut elle-même contenir des instances d’autres scènes.

Une scène n’est donc pas seulement un « niveau ». Elle peut représenter :

- un personnage ;
- une porte ;
- une caméra ;
- une interface ;
- une balise ;
- un projectile ;
- un effet ;
- une partie de niveau.

### 4.4 Instance

Une instance est une copie active créée à partir d’une scène enregistrée.

Si `status_beacon.tscn` est instanciée trois fois, le jeu contient trois arbres de nœuds distincts construits à partir du même modèle.

Les ressources lourdes peuvent rester partagées en mémoire, tandis que les propriétés propres aux nœuds appartiennent à chaque instance.

### 4.5 SceneTree

`SceneTree` est la boucle principale standard de Godot et contient l’arbre actif du jeu.

Une scène chargée avec `preload()` mais non ajoutée au `SceneTree` existe en mémoire, mais ses nœuds ne sont pas encore actifs. Les callbacks `_enter_tree()` et `_ready()` ne sont déclenchés qu’après l’ajout de l’instance à l’arbre.

### 4.6 Branche

Une branche est un nœud et tous ses descendants.

Déplacer ou instancier une branche permet de manipuler un ensemble cohérent sans traiter chaque enfant séparément.

### 4.7 Parent et propriétaire ne signifient pas la même chose

Le **parent** décrit la position runtime dans l’arbre.

Le **propriétaire**, accessible par la propriété `owner`, indique quel nœud de scène est responsable de l’enregistrement du nœud dans une `PackedScene`.

Dans l’éditeur, Godot configure généralement le propriétaire des nœuds créés dans une scène. À l’exécution, un nœud ajouté par code n’a pas besoin d’un propriétaire pour fonctionner.

La propriété `owner` devient importante lorsque du code d’outil crée des nœuds destinés à être enregistrés dans une scène.

## 5. Les scènes comme composants réutilisables

Une scène bien conçue se comporte comme un composant :

- sa racine porte son identité ;
- ses enfants constituent son implémentation interne ;
- son script racine expose les propriétés et fonctions utiles ;
- ses signaux annoncent les événements ;
- les autres scènes n’accèdent pas arbitrairement à tous ses enfants.

Cette règle réduit les dépendances fragiles.

> **Mauvaise pratique :** une scène extérieure cherche directement `StatusBeacon/StatusLabel` et modifie le texte interne.

> **Meilleure pratique :** la scène extérieure appelle `StatusBeacon.activate()` et écoute le signal `activated`.

## 6. Créer l’arborescence de l’exercice

L’exercice construit une balise réutilisable appelée `StatusBeacon`.

### 6.1 Dossiers

Depuis la racine de `Project Asteria`, créer les dossiers nécessaires.

> **[PS] PowerShell 7 - Exécuter depuis la racine du projet Godot.**

```powershell
New-Item -ItemType Directory -Force -Path "src/features/beacons"
New-Item -ItemType Directory -Force -Path "scenes/learning"
New-Item -ItemType Directory -Force -Path "data/beacons"
```

Signification :

- `New-Item` demande à PowerShell de créer un élément ;
- `-ItemType Directory` précise qu’il s’agit d’un dossier ;
- `-Force` évite une erreur si le dossier existe déjà ;
- `-Path` fournit le chemin à créer.

Résultat attendu :

> **[SORTIE] Arborescence attendue - Ne pas saisir.**

```text
Project Asteria/
├── data/
│   └── beacons/
├── scenes/
│   └── learning/
└── src/
    └── features/
        └── beacons/
```

## 7. Créer une Resource personnalisée

### 7.1 Rôle de `Resource`

Un nœud fournit principalement du comportement dans l’arbre actif. Une `Resource` fournit principalement des données réutilisables et sérialisables.

Godot utilise déjà des Resources pour :

- les textures ;
- les maillages ;
- les scripts ;
- les sons ;
- les animations ;
- les scènes enregistrées.

Une scène enregistrée est elle-même une `PackedScene`, donc un type de `Resource`.

### 7.2 Script `BeaconProfile`

> **[VSC] Visual Studio Code - Créer :** `src/features/beacons/beacon_profile.gd`.

```gdscript
class_name BeaconProfile
extends Resource
## Données éditables d’une balise de statut.

@export var id: StringName = &"default_beacon"
@export var display_name: String = "Balise de statut"
@export_multiline var activation_message: String = "Signal reçu."
@export_range(0.1, 60.0, 0.1) var cooldown_seconds: float = 2.0
```

### 7.3 Décomposition ligne par ligne

#### `class_name BeaconProfile`

- `class_name` enregistre la classe dans le projet Godot ;
- `BeaconProfile` devient un type utilisable dans les annotations ;
- ce nom apparaît également dans le menu de création des Resources.

#### `extends Resource`

- `extends` indique la classe parente ;
- `Resource` fournit sérialisation, édition dans l’Inspector et comptage de références ;
- la classe n’est pas un nœud et n’entre pas dans le `SceneTree`.

#### `@export var id: StringName = &"default_beacon"`

- `@export` affiche la propriété dans l’Inspector ;
- `var` déclare une variable ;
- `id` est un identifiant stable choisi par le projet ;
- `: StringName` impose un type optimisé pour les noms répétés ;
- `=` affecte la valeur initiale ;
- `&"default_beacon"` construit un littéral `StringName`.

#### `@export_multiline`

Cette annotation affiche une zone de texte multiligne dans l’Inspector. Elle convient à un message plus long qu’un nom ou un identifiant.

#### `@export_range(0.1, 60.0, 0.1)`

Les trois nombres représentent :

1. la valeur minimale ;
2. la valeur maximale ;
3. le pas utilisé par l’Inspector.

La propriété reste un `float` et vaut ici `2.0` secondes par défaut.

### 7.4 Créer le fichier `.tres`

> **[APP] Godot Editor - Créer la Resource :** dans le dock FileSystem, effectuer un clic droit sur `data/beacons`, choisir **Create New > Resource**, sélectionner `BeaconProfile`, puis enregistrer sous `data/beacons/default_beacon.tres`.

Dans l’Inspector, définir :

> **[APP] Godot Editor - Modifier dans l’Inspector :** `data/beacons/default_beacon.tres`.

```text
Id                 default_beacon
Display Name       Balise Asteria
Activation Message Liaison locale confirmée.
Cooldown Seconds   2.0
```

Ce bloc décrit des valeurs à saisir dans l’Inspector, pas un fichier texte à recopier.

## 8. Créer la scène `StatusBeacon`

### 8.1 Arbre de scène

> **[APP] Godot Editor - Créer une scène 3D :** ajouter un nœud racine `Node3D`, le renommer `StatusBeacon`, puis ajouter deux enfants : `Label3D` nommé `StatusLabel` et `Timer` nommé `CooldownTimer`.

Arbre attendu :

> **[SORTIE] Dock Scene attendu - Ne pas saisir.**

```text
StatusBeacon (Node3D)
├── StatusLabel (Label3D)
└── CooldownTimer (Timer)
```

Enregistrer la scène :

> **[APP] Godot Editor - Enregistrer :** `src/features/beacons/status_beacon.tscn`.

### 8.2 Noms uniques dans la scène

> **[APP] Godot Editor - Marquer comme noms uniques :** clic droit sur `StatusLabel` puis **Access as Unique Name** ; répéter pour `CooldownTimer`.

Le symbole `%` apparaît dans le dock Scene.

Un nom unique permet au script de la même scène d’utiliser :

> **[LECTURE] Exemple GDScript - Étudier la syntaxe.**

```gdscript
%StatusLabel
%CooldownTimer
```

Limite importante : un nom unique n’est résolu que depuis la même scène propriétaire. Une scène parente ne doit pas utiliser `%StatusLabel` pour atteindre l’intérieur d’une instance de `StatusBeacon`.

## 9. Référencer des nœuds

### 9.1 `get_node()`

> **[LECTURE] Exemple GDScript - Étudier la syntaxe.**

```gdscript
var timer: Timer = get_node("CooldownTimer")
```

Décomposition :

- `get_node()` cherche un nœud à partir du nœud courant ;
- la chaîne `"CooldownTimer"` est un chemin relatif ;
- la recherche utilise le nom et le chemin, pas uniquement le type ;
- le nœud doit être présent dans l’arbre attendu ;
- une erreur est produite si le chemin n’existe pas.

### 9.2 `$` comme raccourci

> **[LECTURE] Exemple GDScript - Étudier la syntaxe.**

```gdscript
var timer: Timer = $CooldownTimer
```

`$CooldownTimer` est une écriture courte de `get_node("CooldownTimer")`.

Ce raccourci est pratique pour un chemin stable et court.

### 9.3 `%NomUnique`

> **[LECTURE] Exemple GDScript - Étudier la syntaxe.**

```gdscript
var timer: Timer = %CooldownTimer
```

Le préfixe `%` demande à Godot de chercher un nœud marqué comme unique dans la même scène.

Cette forme résiste mieux au déplacement du nœud dans une autre branche interne, mais elle ne traverse pas librement les frontières d’instances.

### 9.4 `NodePath`

`NodePath` est un type qui représente un chemin de nœud ou de propriété.

> **[LECTURE] Exemple GDScript - Étudier la syntaxe.**

```gdscript
var timer_path: NodePath = ^"CooldownTimer"
var timer: Timer = get_node(timer_path)
```

- `^"CooldownTimer"` est un littéral `NodePath` ;
- `timer_path` stocke le chemin, pas le nœud lui-même ;
- `get_node(timer_path)` résout ce chemin en référence active.

Un `NodePath` peut être exporté lorsque le concepteur doit choisir une cible dans l’Inspector. Pour une dépendance forte et typée, une référence directe exportée peut être plus explicite.

### 9.5 `get_node_or_null()`

> **[LECTURE] Exemple GDScript - Étudier la syntaxe.**

```gdscript
var optional_label: Label3D = get_node_or_null("OptionalLabel") as Label3D
```

Cette fonction renvoie `null` au lieu de générer immédiatement une erreur si le chemin n’existe pas.

Elle convient à une dépendance réellement optionnelle. Elle ne doit pas masquer l’absence d’un nœud obligatoire.

### 9.6 `@onready`

> **[LECTURE] Exemple GDScript - Étudier la syntaxe.**

```gdscript
@onready var _status_label: Label3D = %StatusLabel
```

- `@onready` retarde l’évaluation jusqu’au moment précédant `_ready()` ;
- `_status_label` reçoit alors une référence au nœud ;
- `Label3D` impose le type attendu ;
- le préfixe `_` indique une variable interne au composant.

Cette forme garantit que les enfants de la scène ont été ajoutés avant la résolution de la référence.

## 10. Script de la balise

> **[VSC] Visual Studio Code - Créer :** `src/features/beacons/status_beacon.gd`.

```gdscript
class_name StatusBeacon
extends Node3D
## Balise réutilisable qui publie son activation par signaux.

signal activated(beacon_id: StringName, message: String)
signal availability_changed(is_available: bool)

@export var profile: BeaconProfile

@onready var _status_label: Label3D = %StatusLabel
@onready var _cooldown_timer: Timer = %CooldownTimer

var _is_available: bool = true


func _ready() -> void:
	if profile == null:
		push_error("StatusBeacon nécessite une Resource BeaconProfile.")
		return

	if not _cooldown_timer.timeout.is_connected(_on_cooldown_finished):
		_cooldown_timer.timeout.connect(_on_cooldown_finished)

	_cooldown_timer.wait_time = profile.cooldown_seconds
	_refresh_label()


func activate(actor_name: StringName) -> bool:
	if profile == null or not _is_available:
		return false

	_is_available = false
	var message: String = "%s active %s : %s" % [
		actor_name,
		profile.display_name,
		profile.activation_message,
	]

	_status_label.text = message
	activated.emit(profile.id, message)
	availability_changed.emit(false)
	_cooldown_timer.start()
	return true


func _on_cooldown_finished() -> void:
	_is_available = true
	_refresh_label()
	availability_changed.emit(true)


func _refresh_label() -> void:
	if profile == null:
		_status_label.text = "Profil manquant"
		return

	_status_label.text = profile.display_name if _is_available else "Indisponible"
```

### 10.1 Déclaration de la classe

`class_name StatusBeacon` permet aux autres scripts d’utiliser `StatusBeacon` comme type.

`extends Node3D` indique que la racine possède une transformation 3D et peut être placée dans l’espace.

### 10.2 Déclaration d’un signal personnalisé

> **[LECTURE] Extrait expliqué - Ne pas recopier isolément.**

```gdscript
signal activated(beacon_id: StringName, message: String)
```

- `signal` déclare un événement que l’objet pourra émettre ;
- `activated` est le nom choisi ;
- `beacon_id` est le premier paramètre transmis aux abonnés ;
- `StringName` est son type ;
- `message` est le second paramètre ;
- `String` est son type.

Le signal n’exécute rien seul. Il définit un canal auquel d’autres objets peuvent se connecter.

### 10.3 Propriété exportée

> **[LECTURE] Extrait expliqué - Ne pas recopier isolément.**

```gdscript
@export var profile: BeaconProfile
```

Cette ligne :

- crée une propriété visible dans l’Inspector ;
- exige une Resource de type `BeaconProfile` ;
- vaut `null` tant qu’aucune Resource n’est assignée ;
- permet de réutiliser la même scène avec plusieurs profils.

### 10.4 Signal intégré du `Timer`

> **[LECTURE] Extrait expliqué - Ne pas recopier isolément.**

```gdscript
_cooldown_timer.timeout.connect(_on_cooldown_finished)
```

- `_cooldown_timer.timeout` désigne le signal intégré `timeout` de l’objet `Timer` ;
- `.connect(...)` connecte ce signal à une fonction ;
- `_on_cooldown_finished` est transmis sans parenthèses, car il s’agit d’une référence de fonction ;
- cette référence de fonction est représentée par un `Callable`.

Écrire `_on_cooldown_finished()` appellerait immédiatement la fonction. Écrire `_on_cooldown_finished` transmet la fonction pour un appel futur.

### 10.5 Éviter une connexion en double

> **[LECTURE] Extrait expliqué - Ne pas recopier isolément.**

```gdscript
if not _cooldown_timer.timeout.is_connected(_on_cooldown_finished):
```

- `is_connected()` vérifie si le même signal connaît déjà le même `Callable` ;
- `not` inverse le résultat ;
- la connexion n’est créée que si elle n’existe pas.

Cette protection est utile lorsque l’initialisation peut être rejouée ou reconfigurée.

### 10.6 Fonction publique `activate()`

> **[LECTURE] Signature expliquée - Ne pas recopier isolément.**

```gdscript
func activate(actor_name: StringName) -> bool:
```

- `func` déclare une fonction ;
- `activate` est son nom public ;
- `actor_name` est le paramètre reçu ;
- `StringName` est le type de ce paramètre ;
- `-> bool` annonce que la fonction renvoie `true` ou `false` ;
- `true` signifie que l’activation a été acceptée ;
- `false` signifie qu’elle a été refusée.

### 10.7 Émettre un signal

> **[LECTURE] Extrait expliqué - Ne pas recopier isolément.**

```gdscript
activated.emit(profile.id, message)
```

- `activated` désigne le signal personnalisé ;
- `.emit(...)` déclenche le signal ;
- `profile.id` devient l’argument `beacon_id` reçu par les abonnés ;
- `message` devient l’argument `message` reçu par les abonnés ;
- toutes les fonctions connectées sont appelées.

L’émetteur ne connaît pas nécessairement les abonnés. C’est le principe de découplage.

### 10.8 Expression conditionnelle

> **[LECTURE] Extrait expliqué - Ne pas recopier isolément.**

```gdscript
_status_label.text = profile.display_name if _is_available else "Indisponible"
```

Cette expression affecte :

- `profile.display_name` lorsque `_is_available` vaut `true` ;
- `"Indisponible"` lorsque `_is_available` vaut `false`.

Elle équivaut à un bloc `if/else` plus long.

## 11. Attacher le script et configurer la scène

> **[APP] Godot Editor - Attacher un script :** sélectionner la racine `StatusBeacon`, attacher `src/features/beacons/status_beacon.gd`, puis enregistrer la scène.

> **[APP] Godot Editor - Assigner la Resource :** dans l’Inspector de la racine, glisser `data/beacons/default_beacon.tres` dans la propriété `Profile`.

Configurer le `Timer` :

> **[APP] Godot Editor - Modifier `CooldownTimer` dans l’Inspector.**

```text
One Shot  activé
Autostart désactivé
```

`wait_time` sera défini par le script à partir de la Resource.

## 12. Cycle de vie des nœuds

### 12.1 `_init()`

`_init()` est appelé lors de la création de l’objet scripté.

À ce moment :

- l’objet existe ;
- il n’est pas nécessairement dans le `SceneTree` ;
- ses enfants ne sont pas garantis disponibles ;
- les références `@onready` ne sont pas encore évaluées.

### 12.2 `_enter_tree()`

`_enter_tree()` est appelé chaque fois que le nœud entre dans le `SceneTree`.

Ordre d’entrée :

1. le parent reçoit `_enter_tree()` ;
2. ses enfants reçoivent ensuite `_enter_tree()`.

Cette fonction peut être appelée plusieurs fois si le nœud est retiré puis réinséré.

### 12.3 `_ready()`

`_ready()` est appelé lorsque le nœud et ses enfants sont entrés dans l’arbre.

Ordre de préparation :

1. les enfants reçoivent `_ready()` ;
2. le parent reçoit ensuite `_ready()`.

C’est pourquoi `_ready()` convient généralement à la récupération des enfants.

### 12.4 `_exit_tree()`

`_exit_tree()` est appelé lorsque le nœud quitte l’arbre.

Les enfants quittent l’arbre avant leur parent. Le callback du parent arrive donc après ceux de ses enfants.

### 12.5 Tableau récapitulatif

| Callback | Moment | Enfants garantis prêts ? | Peut se répéter ? |
|---|---|---:|---:|
| `_init()` | création de l’objet | non | une fois par objet |
| `_enter_tree()` | entrée dans le SceneTree | pas tous | oui |
| `_ready()` | nœud prêt après ses enfants | oui | généralement une fois ; voir `request_ready()` pour cas avancés |
| `_exit_tree()` | sortie du SceneTree | ils sortent avant le parent | oui |

## 13. Instancier une scène depuis le code

### 13.1 `PackedScene`

Une scène chargée depuis un fichier est représentée par une `PackedScene`.

> **[LECTURE] Exemple GDScript - Étudier la syntaxe.**

```gdscript
const BEACON_SCENE: PackedScene = preload(
	"res://src/features/beacons/status_beacon.tscn"
)
```

- `const` déclare une référence qui ne sera pas réaffectée ;
- `BEACON_SCENE` est un nom de constante ;
- `PackedScene` est le type de la ressource chargée ;
- `preload()` charge le fichier lors de l’analyse du script ;
- le chemin doit être connu à l’avance.

### 13.2 Fonction d’instanciation

> **[LECTURE] Exemple GDScript - Étudier et adapter.**

```gdscript
const BEACON_SCENE: PackedScene = preload(
	"res://src/features/beacons/status_beacon.tscn"
)


func spawn_beacon(parent: Node, profile: BeaconProfile) -> StatusBeacon:
	var beacon: StatusBeacon = BEACON_SCENE.instantiate() as StatusBeacon
	if beacon == null:
		push_error("La scène instanciée n’est pas un StatusBeacon.")
		return null

	beacon.profile = profile
	parent.add_child(beacon)
	return beacon
```

Décomposition :

- `parent: Node` est le nœud qui recevra la nouvelle instance ;
- `profile: BeaconProfile` est la Resource à assigner ;
- `-> StatusBeacon` annonce le type de retour ;
- `instantiate()` construit l’arbre décrit par la `PackedScene` ;
- `as StatusBeacon` tente de convertir la racine vers le type attendu ;
- la conversion renvoie `null` si le type ne correspond pas ;
- `beacon.profile = profile` configure l’instance avant son entrée dans l’arbre ;
- `parent.add_child(beacon)` l’ajoute au `SceneTree` si `parent` y appartient ;
- l’ajout déclenche ensuite `_enter_tree()` puis `_ready()` ;
- `return beacon` rend la référence disponible à l’appelant.

L’ordre est important : assigner `profile` avant `add_child()` garantit que `_ready()` peut l’utiliser.

### 13.3 `load()` contre `preload()`

Utiliser `preload()` lorsque :

- le chemin est fixe ;
- la ressource est indispensable ;
- une erreur de chemin doit être détectée tôt.

Utiliser `load()` lorsque :

- le chemin est choisi à l’exécution ;
- un catalogue décide de la ressource ;
- le chargement doit être différé.

Le chapitre 7 définira la stratégie générale des catalogues et configurations.

## 14. Créer la scène de démonstration

### 14.1 Nouvelle scène

> **[APP] Godot Editor - Créer une scène 3D :** racine `Node3D` nommée `Chapter03Demo`, puis enregistrer sous `scenes/learning/ch03_scene_signals_demo.tscn`.

> **[APP] Godot Editor - Instancier une scène enfant :** glisser `src/features/beacons/status_beacon.tscn` dans le dock Scene sous `Chapter03Demo`.

Arbre attendu :

> **[SORTIE] Dock Scene attendu - Ne pas saisir.**

```text
Chapter03Demo (Node3D)
└── StatusBeacon (instance)
    ├── StatusLabel
    └── CooldownTimer
```

La scène parente voit l’instance `StatusBeacon` comme un composant. Elle ne doit pas modifier directement `StatusLabel` ou `CooldownTimer`.

### 14.2 Script de démonstration

> **[VSC] Visual Studio Code - Créer :** `scenes/learning/chapter03_demo.gd`.

```gdscript
extends Node3D
## Démonstration locale des scènes, Resources et signaux.

@onready var _beacon: StatusBeacon = $StatusBeacon


func _ready() -> void:
	if not _beacon.activated.is_connected(_on_beacon_activated):
		_beacon.activated.connect(_on_beacon_activated)

	if not _beacon.availability_changed.is_connected(
		_on_beacon_availability_changed
	):
		_beacon.availability_changed.connect(
			_on_beacon_availability_changed
		)

	var accepted: bool = _beacon.activate(&"Explorateur")
	print("Activation acceptée : %s" % accepted)


func _on_beacon_activated(
	beacon_id: StringName,
	message: String,
) -> void:
	print("[%s] %s" % [beacon_id, message])


func _on_beacon_availability_changed(is_available: bool) -> void:
	print("Balise disponible : %s" % is_available)
```

Attacher ce script :

> **[APP] Godot Editor - Attacher un script :** sélectionner `Chapter03Demo`, attacher `scenes/learning/chapter03_demo.gd`, puis enregistrer.

### 14.3 Signature du récepteur

La fonction :

> **[LECTURE] Signature expliquée - Ne pas recopier isolément.**

```gdscript
func _on_beacon_activated(
	beacon_id: StringName,
	message: String,
) -> void:
```

reçoit deux arguments, car le signal `activated` en émet deux dans le même ordre.

Une incompatibilité entre les arguments du signal et les paramètres du récepteur provoque une erreur à l’exécution.

## 15. Connecter un signal dans l’éditeur

Godot peut enregistrer certaines connexions directement dans le fichier `.tscn`.

Procédure :

1. sélectionner le nœud émetteur ;
2. ouvrir l’onglet **Node** à côté de l’Inspector ;
3. choisir le signal ;
4. cliquer sur **Connect** ;
5. sélectionner le nœud récepteur ;
6. confirmer ou adapter le nom de la méthode.

> **[APP] Godot Editor - Observer sans modifier l’exercice principal :** ouvrir l’onglet Node du `CooldownTimer` et repérer le signal `timeout`.

Dans ce chapitre, la connexion est effectuée par code afin d’expliquer explicitement l’émetteur, le signal et le `Callable`.

### Choisir entre éditeur et code

Connexion dans l’éditeur :

- utile pour une relation fixe et visible entre deux nœuds d’une même scène ;
- enregistrée dans la scène ;
- facile à découvrir dans le dock Node.

Connexion dans le code :

- utile pour une instance créée dynamiquement ;
- permet des conditions et des paramètres liés ;
- facilite certaines fabriques et certains tests ;
- doit être protégée contre les doubles connexions.

## 16. Comprendre `Callable`

Un `Callable` représente une opération pouvant être appelée plus tard.

> **[LECTURE] Exemple GDScript - Étudier la syntaxe.**

```gdscript
var callback: Callable = _on_beacon_activated
_beacon.activated.connect(callback)
```

Ici :

- `callback` est une variable ;
- `Callable` est son type ;
- `_on_beacon_activated` est la fonction référencée ;
- aucune parenthèse n’est utilisée, donc la fonction n’est pas exécutée immédiatement ;
- `connect(callback)` conserve la référence pour l’appeler lors d’une émission.

### 16.1 Lier des arguments supplémentaires

> **[LECTURE] Exemple avancé - Étudier sans l’intégrer obligatoirement.**

```gdscript
button.pressed.connect(_on_button_pressed.bind(button))
```

`bind(button)` construit un nouveau `Callable` qui ajoutera `button` aux arguments transmis lors de l’appel.

Ce mécanisme est utile lorsqu’une même fonction reçoit les événements de plusieurs objets.

## 17. Déconnexion et durée de vie

Une connexion vers un objet libéré est supprimée lorsque sa cible n’existe plus. Une déconnexion manuelle reste utile lorsque :

- l’écoute doit être suspendue temporairement ;
- le récepteur change d’émetteur ;
- un objet persistant se reconnecte plusieurs fois ;
- une logique de configuration doit être inversée proprement.

> **[LECTURE] Exemple GDScript - Étudier la syntaxe.**

```gdscript
if _beacon.activated.is_connected(_on_beacon_activated):
	_beacon.activated.disconnect(_on_beacon_activated)
```

Ne pas appeler `disconnect()` sans vérifier la connexion, car une connexion inexistante produit une erreur.

## 18. Partage des Resources entre instances

Lorsqu’une même Resource est assignée à plusieurs instances, elles peuvent partager le même objet en mémoire.

Conséquence : modifier une propriété mutable de cette Resource pendant le jeu peut affecter plusieurs instances.

Pour des données de conception immuables, ce partage est généralement souhaitable.

Pour un état propre à chaque instance :

- stocker l’état dans le nœud ;
- dupliquer explicitement la Resource ;
- ou utiliser `resource_local_to_scene` lorsque le cas est maîtrisé.

Dans l’exercice :

- `BeaconProfile` décrit la configuration ;
- `_is_available` décrit l’état runtime de chaque balise ;
- le cooldown n’est pas écrit dans la Resource.

Cette séparation évite qu’une balise rende toutes les autres indisponibles.

## 19. Créer un nœud directement par code

Une scène n’est pas obligatoire pour chaque nœud temporaire.

> **[LECTURE] Exemple GDScript - Étudier la syntaxe.**

```gdscript
var marker: Marker3D = Marker3D.new()
marker.name = "RuntimeMarker"
add_child(marker)
```

- `Marker3D.new()` crée un objet ;
- il n’est pas encore dans l’arbre ;
- `marker.name` définit son nom ;
- `add_child(marker)` l’ajoute comme enfant ;
- ses callbacks d’entrée et de préparation sont alors déclenchés.

À l’exécution, aucun `owner` n’est nécessaire pour que ce nœud fonctionne.

Dans un outil d’éditeur qui doit enregistrer le nœud dans une scène, son `owner` doit être configuré vers un ancêtre appartenant à cette scène.

## 20. Supprimer un nœud

> **[LECTURE] Exemple GDScript - Étudier la syntaxe.**

```gdscript
marker.queue_free()
```

`queue_free()` programme la libération du nœud à la fin de la trame courante.

Cette méthode est généralement plus sûre qu’une suppression immédiate pendant qu’un callback ou une boucle utilise encore le nœud.

Après la libération, ne pas conserver ni utiliser la référence comme si l’objet existait encore.

## 21. Erreurs fréquentes et diagnostics

<!-- qa:error-correction-section -->

Le diagnostic reste associé à une correction concrète. Les exemples utilisent les contrats introduits dans le chapitre.

### 21.1 `Node not found`

**Symptôme ou risque :** un chemin exige un enfant qui n’existe pas à cet emplacement.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
@onready var label: Label = $Panel/StatusLabel
```

**Correction :** rendre le chemin cohérent avec la scène ou traiter explicitement une dépendance optionnelle.

> **[VSC] Visual Studio Code — Exemple corrigé avec contrôle nullable.**

```gdscript
@onready var label := get_node_or_null('Panel/StatusLabel') as Label

func _ready() -> void:
	if label == null:
		push_error('StatusLabel est absent.')
```

**Différence :** `$...` échoue immédiatement ; `get_node_or_null()` permet de produire un diagnostic adapté avant l’usage.

### 21.2 `Invalid access to property` sur `null`

**Symptôme ou risque :** le résultat d’un cast est utilisé sans vérifier qu’il a réussi.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
var beacon := node as StatusBeacon
beacon.activate(&'player')
```

**Correction :** tester la référence avant d’accéder à ses propriétés ou méthodes.

> **[VSC] Visual Studio Code — Exemple corrigé après le cast.**

```gdscript
var beacon := node as StatusBeacon
if beacon == null:
	push_error('La racine instanciée doit être un StatusBeacon.')
	return
beacon.activate(&'player')
```

**Différence :** la version corrigée traite le résultat nullable du cast et rapproche l’erreur de sa cause.

### 21.3 Signal connecté deux fois

**Symptôme ou risque :** la même connexion est créée à chaque réactivation de la scène.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
func enable() -> void:
	beacon.activated.connect(_on_beacon_activated)
```

**Correction :** vérifier la connexion avant de l’ajouter.

> **[VSC] Visual Studio Code — Exemple corrigé idempotent.**

```gdscript
func enable() -> void:
	if not beacon.activated.is_connected(_on_beacon_activated):
		beacon.activated.connect(_on_beacon_activated)
```

**Différence :** le second appel corrigé ne crée pas une nouvelle liaison et ne duplique pas le callback.

### 21.4 Signal émis avant la connexion

**Symptôme ou risque :** l’action est lancée avant que l’abonné soit enregistré.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
beacon.activate(&'player')
beacon.activated.connect(_on_beacon_activated)
```

**Correction :** connecter d’abord, puis déclencher l’action.

> **[VSC] Visual Studio Code — Exemple corrigé dans l’ordre observable.**

```gdscript
beacon.activated.connect(_on_beacon_activated)
beacon.activate(&'player')
```

**Différence :** un signal ne conserve pas l’historique ; seul l’ordre corrigé permet au récepteur d’observer cette émission.

### 21.5 Signature incompatible

**Symptôme ou risque :** le callback ne reçoit pas le même nombre de paramètres que le signal.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
signal activated(beacon_id: StringName, message: String)

func _on_activated(beacon_id: StringName) -> void:
	print(beacon_id)
```

**Correction :** aligner la signature du callback sur la déclaration du signal.

> **[VSC] Visual Studio Code — Exemple corrigé avec les deux paramètres.**

```gdscript
func _on_activated(beacon_id: StringName, message: String) -> void:
	print('%s : %s' % [beacon_id, message])
```

**Différence :** la version corrigée accepte exactement les valeurs envoyées par `emit()`.

### 21.6 Resource partagée modifiée par erreur

**Symptôme ou risque :** le cooldown courant est écrit dans la définition partagée.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
profile.cooldown_seconds -= delta
```

**Correction :** conserver la configuration dans la Resource et l’état courant dans le nœud.

> **[VSC] Visual Studio Code — Exemple corrigé avec une variable runtime.**

```gdscript
_remaining_cooldown = maxf(_remaining_cooldown - delta, 0.0)
```

**Différence :** la Resource reste identique pour toutes les instances ; seule la variable propre au nœud évolue.

### 21.7 Mauvaise scène exécutée

**Symptôme ou risque :** `F6` lance l’onglet courant alors que le test attendu concerne la scène principale.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```text
Onglet actif : status_beacon.tscn
F6 → seule la balise est exécutée
```

**Correction :** lancer explicitement la scène de démonstration ou utiliser `F5` pour la scène principale.

> **[PS] PowerShell 7 — Exemple corrigé avec une cible explicite.**

```powershell
godot --headless --path . --scene 'res://scenes/learning/ch03_scene_signals_demo.tscn' --quit-after 180
```

**Différence :** la commande corrigée nomme la scène testée et rend le résultat reproductible.

### 21.8 Nœud ajouté mais absent après enregistrement

**Symptôme ou risque :** un outil d’éditeur ajoute un enfant sans propriétaire de scène.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
var marker := Marker3D.new()
scene_root.add_child(marker)
ResourceSaver.save(packed_scene, path)
```

**Correction :** dans un outil d’éditeur, définir `owner` vers la racine enregistrée avant le conditionnement de la scène.

> **[VSC] Visual Studio Code — Exemple corrigé réservé à un outil d’éditeur.**

```gdscript
var marker := Marker3D.new()
scene_root.add_child(marker)
marker.owner = scene_root
ResourceSaver.save(packed_scene, path)
```

**Différence :** `add_child()` suffit au runtime, mais `owner` indique au sérialiseur que l’enfant appartient à la scène enregistrée.

## 22. Validation dans Godot

### 22.1 Exécution graphique

> **[APP] Godot Editor - Exécuter la scène courante :** ouvrir `scenes/learning/ch03_scene_signals_demo.tscn`, puis appuyer sur `F6`.

Sortie attendue dans le panneau Output :

> **[SORTIE] Exemple de sortie - Ne pas saisir.**

```text
[default_beacon] Explorateur active Balise Asteria : Liaison locale confirmée.
Balise disponible : false
Activation acceptée : true
Balise disponible : true
```

L’ordre précis des premières lignes dépend de l’ordre d’émission et des appels `print()`, mais chaque événement doit apparaître une seule fois.

### 22.2 Import et analyse headless

Fermer l’éditeur Godot avant cette vérification si le projet utilise des fichiers verrouillés par un plugin.

> **[PS] PowerShell 7 - Exécuter depuis la racine de `Project Asteria`.**

```powershell
godot --headless --path . --import
```

Cette commande :

- active le mode sans fenêtre ;
- ouvre le projet situé dans le dossier courant ;
- attend l’importation des ressources ;
- quitte ensuite automatiquement.

### 22.3 Exécuter la scène précise en mode headless

> **[PS] PowerShell 7 - Exécuter depuis la racine de `Project Asteria`.**

```powershell
godot --headless --path . --scene "res://scenes/learning/ch03_scene_signals_demo.tscn" --quit-after 180
```

- `--scene` choisit la scène à lancer ;
- `--quit-after 180` arrête le moteur après 180 itérations ;
- la durée réelle dépend de la cadence et du mode headless ;
- les erreurs GDScript restent visibles dans PowerShell.

Pour une validation déterministe future, le Companion Pack ajoutera un script de test qui quittera explicitement après observation des signaux attendus.

## 23. Vérification avec Git

> **[PS] PowerShell 7 - Vérifier les fichiers modifiés.**

```powershell
git status --short
```

Fichiers attendus pour l’exercice :

> **[SORTIE] Liste de référence - Les préfixes Git peuvent varier.**

```text
src/features/beacons/beacon_profile.gd
src/features/beacons/status_beacon.gd
src/features/beacons/status_beacon.tscn
data/beacons/default_beacon.tres
scenes/learning/chapter03_demo.gd
scenes/learning/ch03_scene_signals_demo.tscn
```

Avant le commit, ouvrir les fichiers `.tscn` et `.tres` uniquement pour inspection. Leur structure est gérée par Godot ; éviter les modifications manuelles inutiles.

## 24. Mode Solo et Mode Studio

### 24.1 Mode Solo

Le parcours Solo peut :

- connecter les relations locales directement dans le script racine ;
- utiliser des scènes petites et explicites ;
- conserver une seule Resource de profil pour commencer ;
- documenter les frontières dans le README de la fonctionnalité.

Le développeur Solo ne doit pas créer un bus global pour chaque événement.

### 24.2 Mode Studio

Le parcours Studio ajoute :

- revue des interfaces publiques des scènes ;
- conventions de noms de signaux et callbacks ;
- ownership clair des fonctionnalités ;
- scènes de test isolées ;
- Resources validées par schéma ou outils ;
- tests de connexions et de cycles de vie ;
- documentation des dépendances entre équipes.

Même en Studio, les communications locales simples peuvent rester des signaux directs.

## 25. Règles de conception retenues pour `Project Asteria`

1. La racine d’une scène porte son interface publique.
2. Les enfants internes ne sont pas manipulés directement depuis l’extérieur.
3. Les références obligatoires échouent clairement lorsqu’elles manquent.
4. Les références optionnelles sont explicitement traitées comme telles.
5. Les noms uniques restent dans la frontière de leur scène.
6. Les scènes réutilisables sont instanciées plutôt que copiées.
7. Les données de conception vivent dans des Resources ou catalogues appropriés.
8. L’état runtime propre à une instance reste dans ses nœuds.
9. Les signaux annoncent des événements ; ils ne remplacent pas toutes les fonctions directes.
10. Une connexion doit avoir un propriétaire logique et une durée de vie compréhensible.
11. Les services globaux ne sont introduits qu’au chapitre 5.
12. Les scènes et Resources de l’exercice devront être matérialisées dans le Starter Kit.

## 26. Checklist de fin de chapitre

- [ ] Je sais distinguer un nœud, une scène enregistrée et une instance.
- [ ] Je peux expliquer parent, enfant, branche, racine et propriétaire.
- [ ] Je comprends la différence entre `owner` et `get_parent()`.
- [ ] Je peux choisir entre `get_node()`, `$`, `%NomUnique` et `get_node_or_null()`.
- [ ] Je sais pourquoi `@onready` est utilisé pour les enfants.
- [ ] Je peux expliquer l’ordre de `_enter_tree()` et `_ready()`.
- [ ] Je sais charger une `PackedScene` et appeler `instantiate()`.
- [ ] Je configure les propriétés indispensables avant `add_child()`.
- [ ] Je sais déclarer, connecter et émettre un signal.
- [ ] Je comprends ce qu’est un `Callable`.
- [ ] Je vérifie les connexions avant de les dupliquer ou les déconnecter.
- [ ] Je sais créer et assigner une Resource personnalisée.
- [ ] Je distingue données partagées et état runtime par instance.
- [ ] La scène de démonstration s’exécute sans erreur visible.
- [ ] Les commandes et fichiers sont associés au bon outil.

## 27. Critères d’acceptation

Le chapitre est réussi lorsque :

1. `BeaconProfile` apparaît comme type de Resource dans Godot ;
2. `default_beacon.tres` peut être créé et édité ;
3. `StatusBeacon` affiche son nom initial ;
4. l’appel `activate()` renvoie `true` lors de la première activation ;
5. le signal `activated` transmet l’identifiant et le message ;
6. le signal `availability_changed` transmet `false`, puis `true` après le cooldown ;
7. chaque message n’est reçu qu’une fois ;
8. aucune scène extérieure ne modifie directement les enfants internes de la balise ;
9. l’analyse headless ne signale pas d’erreur de syntaxe ;
10. la réserve runtime reste clairement déclarée tant que le Starter Kit n’a pas matérialisé et exécuté ces fichiers.

## 28. Ce que le chapitre suivant ajoutera

Le chapitre 4 définira l’architecture modulaire complète :

- couches ;
- modules ;
- dépendances autorisées ;
- séparation domaine, présentation, données et infrastructure ;
- conventions de dossiers ;
- décisions d’architecture.

Il réutilisera les scènes, Resources et signaux du présent chapitre sans réexpliquer intégralement leur syntaxe.

## 29. Sources officielles vérifiées

- [Godot 4.7 — Nodes and Scenes](https://docs.godotengine.org/en/4.7/getting_started/step_by_step/nodes_and_scenes.html)
- [Godot 4.7 — Nodes and scene instances](https://docs.godotengine.org/en/4.7/tutorials/scripting/nodes_and_scene_instances.html)
- [Godot 4.7 — Resources](https://docs.godotengine.org/en/4.7/tutorials/scripting/resources.html)
- [Godot 4.7 — Instancing with signals](https://docs.godotengine.org/en/4.7/tutorials/scripting/instancing_with_signals.html)
- [Godot 4.7 — Signal class](https://docs.godotengine.org/en/4.7/classes/class_signal.html)
- [Godot 4.x — Scene unique nodes](https://docs.godotengine.org/fr/4.x/tutorials/scripting/scene_unique_nodes.html)
- [Godot 4.x — Overridable functions](https://docs.godotengine.org/fr/4.x/tutorials/scripting/overridable_functions.html)
- [Godot 4.7 — Command line tutorial](https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html)

## 30. Résumé

Une scène est un arbre de nœuds enregistré comme une `PackedScene`. Une instance est l’arbre actif créé à partir de cette ressource. Les nœuds entrent dans le `SceneTree`, reçoivent leurs callbacks dans un ordre déterminé et communiquent localement grâce aux fonctions et aux signaux. Les Resources stockent des données réutilisables sans devenir des nœuds actifs.

L’exercice `StatusBeacon` applique ces principes sans introduire prématurément une architecture globale. Il constitue la première fonctionnalité réutilisable de `Project Asteria` fondée sur une scène, une Resource et des signaux typés.
