---
title: "Livre II — Chapitre 7 : Données avec Resources, JSON et configurations"
id: "DOC-L2-CH07"
status: "reviewed"
version: "1.1.1"
lang: "fr-FR"
book: "Livre II"
chapter: 7
last-verified: "2026-07-19"
audit-status: "complete"
audit-date: "2026-07-19"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-07.md"
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
recommended-reasoning: "GPT-5.6 Sol — Élevée"
---

# Données avec Resources, JSON et configurations

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir, **[LECTURE]** exemple à étudier. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH07`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Niveau de raisonnement conseillé pour produire ou réviser ce chapitre :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-07.md`.

## 1. Rôle du chapitre

Les chapitres précédents ont créé le projet, présenté GDScript, structuré les scènes, défini l’architecture modulaire, construit les services et séparé les entrées du gameplay.

Le projet doit maintenant organiser ses données sans les disperser dans les scripts.

Une mauvaise organisation produit souvent :

- des nombres magiques répétés dans plusieurs classes ;
- des dictionnaires dont les clés sont mal orthographiées ;
- des `Resource` modifiées accidentellement par plusieurs instances ;
- du JSON accepté sans validation ;
- des identifiants basés sur des noms affichés et donc fragiles ;
- des fichiers de configuration qui mélangent secrets, préférences et règles de gameplay ;
- une dépendance prématurée à SQLite ou au système de sauvegarde ;
- des erreurs silencieuses lorsque les formats évoluent.

À la fin du chapitre, le lecteur doit savoir :

- distinguer donnée de conception, configuration, état runtime et sauvegarde ;
- créer une `Resource` personnalisée et l’éditer dans l’Inspector ;
- comprendre le cache des ressources et le partage des références ;
- choisir entre duplication superficielle et profonde ;
- utiliser `resource_local_to_scene` avec prudence ;
- créer un catalogue typé indexé par identifiant stable ;
- charger une ressource avec `preload()`, `load()` ou `ResourceLoader` ;
- lire un fichier JSON avec `FileAccess` et `JSON` ;
- vérifier types, champs obligatoires, plages et doublons ;
- versionner un format de données et préparer des migrations ;
- utiliser `ConfigFile` pour une configuration INI adaptée ;
- séparer `res://` et `user://` ;
- construire une configuration par défaut, locale et runtime ;
- injecter un catalogue dans un service sans créer de Service Locator.

## 2. Prérequis

Le lecteur doit connaître :

- les types, classes, fonctions, tableaux et dictionnaires du chapitre 2 ;
- les `Resource`, sous-ressources et signaux du chapitre 3 ;
- les frontières de modules du chapitre 4 ;
- l’injection de dépendances et le point de composition du chapitre 5 ;
- la différence entre intention, contrôleur et état runtime du chapitre 6.

Le chapitre réutilise l’organisation feature-first de `Project Asteria` et le point de composition situé dans `src/app`.

## 3. Périmètre et frontières

Ce chapitre définit :

- les données de conception éditables ;
- les ressources personnalisées ;
- les catalogues en mémoire ;
- les identifiants stables ;
- l’import manuel de JSON ;
- la validation explicite ;
- les configurations locales non secrètes ;
- le versionnement initial des formats ;
- les contrats nécessaires aux chapitres suivants.

Il ne définit pas encore :

- SQLite et les migrations SQL du chapitre 8 ;
- les fichiers de sauvegarde du joueur du chapitre 9 ;
- la mémoire vectorielle du chapitre 10 ;
- les API réseau des chapitres 11 et 12 ;
- les pipelines d’import automatisés du chapitre 26 ;
- les tests complets du chapitre 27 ;
- les scripts Python de génération massive du chapitre 29.

> **Frontière essentielle :** une donnée de conception décrit ce que le jeu peut utiliser. Un état runtime décrit ce qui se passe actuellement. Une sauvegarde décrit ce qui doit survivre à la fermeture du jeu.

## 4. Quatre catégories de données

### 4.1 Données de conception

Elles sont créées par les concepteurs et versionnées dans Git.

Exemples :

- profil d’un objet ;
- statistiques de base d’une créature ;
- définition d’une compétence ;
- paramètres d’un biome ;
- description d’une interaction.

Support conseillé dans ce chapitre : `Resource` externe en `.tres`.

### 4.2 Configuration technique

Elle adapte le comportement d’un environnement sans représenter la progression du joueur.

Exemples :

- niveau de journalisation ;
- activation d’un service local facultatif ;
- URL locale d’un serveur de développement ;
- taille maximale d’une file de tâches ;
- profil graphique de test.

Support possible : `ConfigFile`, JSON validé ou paramètres de projet selon le besoin.

### 4.3 État runtime

Il existe seulement pendant l’exécution.

Exemples :

- points de vie actuels ;
- cible sélectionnée ;
- position courante ;
- délai restant ;
- contenu temporaire d’une interaction.

Support conseillé : objets runtime dédiés, nœuds, `RefCounted` ou structures typées.

### 4.4 Données persistantes du joueur

Elles doivent survivre à la fermeture du jeu.

Exemples :

- progression ;
- inventaire courant ;
- quêtes actives ;
- options remappées ;
- monde modifié.

Elles seront traitées au chapitre 9. Elles ne doivent pas être écrites directement dans les `.tres` de conception.

## 5. Matrice de décision

> **[LECTURE] Matrice de choix — Ne pas saisir.**

```text
Besoin                                      Support principal
-----------------------------------------   ------------------------------
Donnée éditable dans l’Inspector            Resource externe .tres
Donnée imbriquée dans une scène             Sous-Resource avec prudence
Échange avec un outil externe               JSON validé
Configuration INI locale                    ConfigFile
État vivant pendant une partie              Objet runtime typé
Données relationnelles persistantes         SQLite, chapitre 8
Progression du joueur                       Sauvegarde versionnée, chapitre 9
Secret ou jeton d’accès                      Hors dépôt, mécanisme sécurisé
```

Cette matrice n’est pas une loi absolue. Elle évite surtout d’utiliser un même format pour tous les problèmes.

## 6. Pourquoi utiliser une Resource personnalisée

Une `Resource` est un conteneur de données reconnu par Godot. Elle bénéficie notamment :

- de propriétés typées ;
- de l’édition dans l’Inspector ;
- de la sérialisation native ;
- de références vers d’autres ressources ;
- du comptage de références ;
- d’un format texte `.tres` compatible avec Git ;
- de méthodes de validation ou de normalisation ;
- de signaux lorsqu’une réaction aux changements est réellement nécessaire.

Une `Resource` n’est pas un service et ne doit pas exécuter une boucle de gameplay permanente.

## 7. Premier modèle : `BeaconProfile`

Le chapitre 3 a introduit l’idée d’un profil de balise. Nous la transformons maintenant en contrat de données complet.

### 7.1 Emplacement du script

> **[VSC] Visual Studio Code - Créer :** `res://src/features/beacons/domain/beacon_profile.gd`.

```gdscript
class_name BeaconProfile
extends Resource

@export var id: StringName
@export var display_name: String = "Balise"
@export_multiline var description: String = ""
@export_range(0.0, 1000.0, 0.1) var activation_radius: float = 4.0
@export_range(0.0, 3600.0, 0.1) var cooldown_seconds: float = 2.0
@export var enabled_by_default: bool = true
@export var tags: Array[StringName] = []

func validate() -> PackedStringArray:
	var errors := PackedStringArray()

	if id.is_empty():
		errors.append("id est obligatoire")
	if display_name.strip_edges().is_empty():
		errors.append("display_name est obligatoire")
	if activation_radius <= 0.0:
		errors.append("activation_radius doit être supérieur à 0")
	if cooldown_seconds < 0.0:
		errors.append("cooldown_seconds ne peut pas être négatif")

	return errors
```

### 7.2 Explication des propriétés

`class_name BeaconProfile` enregistre un nom global de script. La classe apparaît alors dans les sélecteurs de types et dans la fenêtre de création de ressources.

`extends Resource` indique que l’objet représente une ressource sérialisable et non un nœud de scène.

`id: StringName` contient l’identifiant technique stable. Il ne doit pas être traduit ni modifié pour améliorer l’affichage.

`display_name: String` contient le nom destiné à l’interface. Il peut évoluer ou être remplacé plus tard par une clé de traduction.

`@export_multiline` affiche un champ multiligne dans l’Inspector.

`@export_range(0.0, 1000.0, 0.1)` demande à l’Inspector une valeur comprise entre 0 et 1000, avec un pas visuel de 0,1. Cette indication améliore l’édition, mais la méthode `validate()` reste nécessaire pour contrôler les données chargées autrement.

`tags: Array[StringName]` contient une liste de catégories techniques. Un tableau typé empêche d’y placer accidentellement un entier ou un nœud.

`validate() -> PackedStringArray` retourne toutes les erreurs détectées au lieu de s’arrêter à la première. Cela facilite l’audit d’un catalogue entier.

## 8. Créer une ressource `.tres`

### 8.1 Depuis Godot

> **[APP] Godot - Créer :** dans le dock FileSystem, créer le dossier `res://data/beacons/`, puis utiliser **New Resource**, choisir `BeaconProfile` et enregistrer `beacon_training.tres`.

Renseigner :

- `id` : `beacon.training` ;
- `display_name` : `Balise d’entraînement` ;
- `description` : `Balise utilisée dans les scènes pédagogiques.` ;
- `activation_radius` : `4.0` ;
- `cooldown_seconds` : `2.0` ;
- `enabled_by_default` : activé ;
- `tags` : `training`, `interactive`.

### 8.2 Forme textuelle indicative

Le fichier doit normalement être créé et enregistré par Godot. La représentation suivante sert à comprendre le format.

> **[LECTURE] Exemple `.tres` — Ne pas recopier automatiquement.**

```ini
[gd_resource type="Resource" script_class="BeaconProfile" load_steps=2 format=3]

[ext_resource type="Script" path="res://src/features/beacons/domain/beacon_profile.gd" id="1_profile"]

[resource]
script = ExtResource("1_profile")
id = &"beacon.training"
display_name = "Balise d’entraînement"
description = "Balise utilisée dans les scènes pédagogiques."
activation_radius = 4.0
cooldown_seconds = 2.0
enabled_by_default = true
tags = Array[StringName]([&"training", &"interactive"])
```

Ne pas modifier manuellement les identifiants internes `ExtResource` sans comprendre le format. L’Inspector est le parcours principal du guide.

## 9. Ressource externe et sous-ressource

### 9.1 Ressource externe

Une ressource externe possède son propre fichier `.tres`.

Avantages :

- réutilisable par plusieurs scènes ;
- diff Git plus lisible ;
- validation et catalogage plus simples ;
- responsabilité claire.

### 9.2 Sous-ressource

Une sous-ressource est enregistrée à l’intérieur d’une scène ou d’une autre ressource.

Avantages :

- pratique pour une valeur locale courte ;
- limite le nombre de fichiers ;
- accompagne naturellement son propriétaire.

Risques :

- partage implicite entre instances ;
- diff de scène plus volumineux ;
- réutilisation difficile ;
- duplication involontaire de données.

### 9.3 Règle de `Project Asteria`

Utiliser une ressource externe lorsque la donnée :

- possède un identifiant métier ;
- doit être référencée depuis plusieurs scènes ;
- doit être cataloguée ;
- doit être révisée indépendamment ;
- peut être produite par un pipeline.

Utiliser une sous-ressource pour une donnée strictement locale et sans identité métier durable.

## 10. Cache et partage des Resources

Godot met en cache les ressources chargées. Charger plusieurs fois le même chemin retourne généralement la même instance en mémoire.

> **[LECTURE] Exemple GDScript — Étudier le partage de référence.**

```gdscript
var first: BeaconProfile = load("res://data/beacons/beacon_training.tres")
var second: BeaconProfile = load("res://data/beacons/beacon_training.tres")

print(first == second)
```

> **[SORTIE] Résultat attendu - Ne pas saisir :** les deux variables référencent normalement la même ressource mise en cache.

```text
true
```

Conséquence : modifier `first.activation_radius` modifie aussi la valeur observée par `second` pendant cette exécution.

Une donnée de conception chargée doit donc être considérée comme immuable pendant le gameplay, sauf décision explicite.

## 11. Dupliquer une Resource

### 11.1 Duplication superficielle

> **[LECTURE] Exemple GDScript — Étudier avant adaptation.**

```gdscript
var runtime_profile: BeaconProfile = source_profile.duplicate(false) as BeaconProfile
```

Le paramètre `false` demande une duplication non profonde. Les sous-ressources peuvent rester partagées.

### 11.2 Duplication profonde

> **[LECTURE] Exemple GDScript — Étudier avant adaptation.**

```gdscript
var runtime_profile: BeaconProfile = source_profile.duplicate(true) as BeaconProfile
```

Le paramètre `true` demande de dupliquer les sous-ressources internes lorsque Godot peut le faire.

### 11.3 Explication des éléments

`source_profile` est la ressource de conception d’origine.

`duplicate(true)` retourne une nouvelle ressource générique.

`as BeaconProfile` tente de la convertir vers le type attendu. Si la conversion échoue, le résultat vaut `null`.

Une vérification reste donc nécessaire :

> **[LECTURE] Exemple GDScript — Validation du résultat.**

```gdscript
var runtime_profile := source_profile.duplicate(true) as BeaconProfile
if runtime_profile == null:
	push_error("La duplication du BeaconProfile a échoué")
	return
```

## 12. `resource_local_to_scene`

Cette propriété demande à Godot de créer une copie locale de la ressource pour chaque instance de scène.

Elle peut être utile pour :

- un matériau modifiable par instance ;
- une courbe locale ;
- une petite donnée embarquée qui doit diverger entre instances.

Elle ne doit pas être activée par réflexe sur les profils de conception partagés.

Pour une ressource métier cataloguée, préférer :

- une ressource source immuable ;
- un objet d’état runtime séparé ;
- une duplication explicite lorsque cela est réellement nécessaire.

## 13. Séparer définition et état runtime

### 13.1 Définition immuable

`BeaconProfile` décrit les valeurs initiales et les règles configurables.

### 13.2 État vivant

> **[VSC] Visual Studio Code - Créer :** `res://src/features/beacons/domain/beacon_runtime_state.gd`.

```gdscript
class_name BeaconRuntimeState
extends RefCounted

var profile_id: StringName
var is_enabled: bool
var cooldown_remaining: float = 0.0
var activation_count: int = 0

func _init(profile: BeaconProfile) -> void:
	profile_id = profile.id
	is_enabled = profile.enabled_by_default

func tick(delta: float) -> void:
	cooldown_remaining = maxf(0.0, cooldown_remaining - delta)

func can_activate() -> bool:
	return is_enabled and is_zero_approx(cooldown_remaining)

func record_activation(cooldown_seconds: float) -> void:
	activation_count += 1
	cooldown_remaining = maxf(0.0, cooldown_seconds)
```

### 13.3 Explication des fonctions

`_init(profile: BeaconProfile)` est le constructeur. Le paramètre `profile` fournit la définition de conception. La fonction copie seulement les valeurs nécessaires à l’état initial.

`tick(delta: float)` reçoit le temps écoulé depuis le dernier traitement. Elle réduit le délai restant sans le laisser devenir négatif.

`can_activate() -> bool` renvoie `true` uniquement si la balise est active et si son délai est terminé.

`record_activation(cooldown_seconds: float)` incrémente le compteur puis réinitialise le délai.

Cette séparation empêche l’état d’une partie de modifier le fichier de conception partagé.

## 14. Identifiants stables

### 14.1 Mauvais identifiant

> **[LECTURE] Exemple incorrect — Ne pas utiliser.**

```gdscript
var id := profile.display_name.to_lower().replace(" ", "_")
```

Le nom affiché peut changer, être traduit ou contenir des caractères différents.

### 14.2 Bon identifiant

> **[LECTURE] Exemple de convention — Ne pas saisir.**

```text
beacon.training
beacon.village.west
item.tool.hammer.iron
character.role.medic
```

La convention retenue :

- minuscules ASCII ;
- segments séparés par des points ;
- aucune espace ;
- identité indépendante du chemin de fichier ;
- aucun numéro de version dans l’identifiant métier ;
- identifiant jamais recyclé pour une autre signification.

### 14.3 Validation de syntaxe

> **[VSC] Visual Studio Code - Créer :** `res://src/core/data/stable_id.gd`.

```gdscript
class_name StableId
extends RefCounted

const PATTERN := "^[a-z][a-z0-9]*(\\.[a-z][a-z0-9_-]*)+$"

static func is_valid(value: StringName) -> bool:
	if value.is_empty():
		return false

	var regex := RegEx.new()
	var error := regex.compile(PATTERN)
	if error != OK:
		push_error("Le motif StableId est invalide")
		return false

	return regex.search(String(value)) != null
```

`PATTERN` impose au moins deux segments séparés par un point.

`RegEx.compile()` retourne un code `Error`. Il doit être contrôlé même lorsque le motif est constant.

`regex.search()` retourne un résultat ou `null`.

## 15. Catalogue typé

Un catalogue centralise les définitions chargées et interdit les doublons d’identifiants.

> **[VSC] Visual Studio Code - Créer :** `res://src/features/beacons/application/beacon_catalog.gd`.

```gdscript
class_name BeaconCatalog
extends RefCounted

var _profiles: Dictionary[StringName, BeaconProfile] = {}

func register(profile: BeaconProfile) -> Error:
	if profile == null:
		push_error("Impossible d’enregistrer un profil null")
		return ERR_INVALID_PARAMETER

	var validation_errors := profile.validate()
	if not validation_errors.is_empty():
		for message in validation_errors:
			push_error("%s : %s" % [profile.resource_path, message])
		return ERR_INVALID_DATA

	if not StableId.is_valid(profile.id):
		push_error("Identifiant invalide : %s" % profile.id)
		return ERR_INVALID_DATA

	if _profiles.has(profile.id):
		push_error("Identifiant dupliqué : %s" % profile.id)
		return ERR_ALREADY_EXISTS

	_profiles[profile.id] = profile
	return OK

func get_profile(id: StringName) -> BeaconProfile:
	return _profiles.get(id) as BeaconProfile

func has_profile(id: StringName) -> bool:
	return _profiles.has(id)

func get_ids() -> Array[StringName]:
	var ids: Array[StringName] = []
	ids.assign(_profiles.keys())
	ids.sort()
	return ids

func size() -> int:
	return _profiles.size()
```

### 15.1 Explication de `Dictionary[StringName, BeaconProfile]`

Le type placé avant la virgule est le type des clés.

Le type placé après la virgule est le type des valeurs.

Ici, chaque identifiant `StringName` pointe vers un `BeaconProfile`.

### 15.2 Explication de `register()`

Le paramètre `profile` est la donnée à enregistrer.

Le retour `Error` permet au code appelant de distinguer succès, paramètre invalide, donnée invalide et doublon.

La fonction :

1. refuse `null` ;
2. appelle la validation métier ;
3. contrôle la syntaxe de l’identifiant ;
4. refuse les doublons ;
5. ajoute la ressource ;
6. retourne `OK`.

### 15.3 Explication de `get_profile()`

`_profiles.get(id)` retourne la valeur associée ou `null`.

`as BeaconProfile` documente le type attendu et protège le reste du code.

Le code appelant doit vérifier le résultat lorsqu’un identifiant peut provenir d’une source externe.

## 16. Charger des ressources

### 16.1 `preload()`

> **[LECTURE] Exemple GDScript — Chemin connu à l’écriture du script.**

```gdscript
const TRAINING_BEACON: BeaconProfile = preload(
	"res://data/beacons/beacon_training.tres"
)
```

`preload()` exige un chemin constant. La ressource est résolue lors du chargement du script.

Utiliser ce choix pour une dépendance fixe et indispensable.

### 16.2 `load()`

> **[LECTURE] Exemple GDScript — Chargement dynamique simple.**

```gdscript
var resource := load(path)
var profile := resource as BeaconProfile
if profile == null:
	push_error("Le fichier n’est pas un BeaconProfile : %s" % path)
```

`path` peut être une variable. Le contrôle du type est obligatoire.

### 16.3 `ResourceLoader.load()`

> **[LECTURE] Exemple GDScript — Chargement avec indication de type.**

```gdscript
var resource := ResourceLoader.load(path, "BeaconProfile")
var profile := resource as BeaconProfile
```

L’indication de type aide le chargeur, mais ne remplace pas la conversion et la validation.

### 16.4 Chargement asynchrone préparatoire

Pour des ressources lourdes, `ResourceLoader` possède des fonctions de chargement en arrière-plan. Ce chapitre en présente seulement le contrat, car le pipeline complet sera traité lors de l’industrialisation.

> **[LECTURE] Exemple GDScript — Structure de référence.**

```gdscript
var error := ResourceLoader.load_threaded_request(path)
if error != OK:
	push_error("Impossible de démarrer le chargement : %s" % path)
	return
```

Le code doit ensuite suivre l’état puis récupérer la ressource. Ne pas lancer une requête en boucle à chaque image.

## 17. Construire le catalogue depuis une liste explicite

Le parcours initial utilise une liste de chemins versionnée. Il évite de dépendre de l’ordre non déterministe d’un parcours de dossier.

> **[VSC] Visual Studio Code - Créer :** `res://data/beacons/catalog_paths.gd`.

```gdscript
class_name BeaconCatalogPaths
extends RefCounted

const PATHS: PackedStringArray = [
	"res://data/beacons/beacon_training.tres",
]
```

> **[VSC] Visual Studio Code - Créer :** `res://src/features/beacons/infrastructure/beacon_catalog_loader.gd`.

```gdscript
class_name BeaconCatalogLoader
extends RefCounted

func load_catalog(paths: PackedStringArray) -> BeaconCatalog:
	var catalog := BeaconCatalog.new()

	for path in paths:
		var profile := ResourceLoader.load(path, "BeaconProfile") as BeaconProfile
		if profile == null:
			push_error("Profil absent ou invalide : %s" % path)
			continue

		var error := catalog.register(profile)
		if error != OK:
			push_error("Échec d’enregistrement pour %s : %s" % [path, error_string(error)])

	return catalog
```

### 17.1 Pourquoi retourner un catalogue même avec des erreurs

Dans un outil d’édition, il peut être utile de collecter toutes les erreurs en un passage.

Dans un build de production, une donnée obligatoire absente peut justifier l’arrêt du bootstrap.

La politique doit être explicite :

- mode audit : continuer et rapporter ;
- mode strict : interrompre dès qu’une donnée obligatoire échoue ;
- mode dégradé : utiliser une valeur de remplacement documentée.

## 18. JSON : rôle et limites

JSON est utile pour :

- échanger avec un outil externe ;
- recevoir une réponse d’API ;
- versionner un format simple indépendant de Godot ;
- importer des données générées ;
- produire des fixtures de test lisibles.

JSON ne fournit pas automatiquement :

- types Godot spécialisés ;
- validation de schéma ;
- commentaires standard ;
- références natives vers des ressources ;
- distinction entre entier et nombre à virgule après tous les traitements ;
- garantie sur les champs obligatoires.

Une lecture JSON réussie syntaxiquement ne signifie donc pas que la donnée est valide pour le jeu.

## 19. Exemple de fichier JSON

> **[VSC] Visual Studio Code - Créer :** `res://data/import/beacons.json`.

```json
{
  "format_version": 1,
  "beacons": [
    {
      "id": "beacon.training",
      "display_name": "Balise d’entraînement",
      "description": "Balise utilisée dans les scènes pédagogiques.",
      "activation_radius": 4.0,
      "cooldown_seconds": 2.0,
      "enabled_by_default": true,
      "tags": ["training", "interactive"]
    }
  ]
}
```

`format_version` versionne la structure du fichier, pas le contenu métier d’une balise.

## 20. Lire un fichier texte avec `FileAccess`

`ResourceLoader` charge des ressources reconnues. Pour un fichier JSON texte, utiliser `FileAccess`.

> **[VSC] Visual Studio Code - Créer :** `res://src/core/data/json_file_reader.gd`.

```gdscript
class_name JsonFileReader
extends RefCounted

func read_dictionary(path: String) -> Dictionary:
	if not FileAccess.file_exists(path):
		push_error("Fichier JSON absent : %s" % path)
		return {}

	var file := FileAccess.open(path, FileAccess.READ)
	if file == null:
		push_error(
			"Ouverture impossible : %s — %s"
			% [path, error_string(FileAccess.get_open_error())]
		)
		return {}

	var text := file.get_as_text()
	var json := JSON.new()
	var error := json.parse(text)
	if error != OK:
		push_error(
			"JSON invalide dans %s, ligne %d : %s"
			% [path, json.get_error_line(), json.get_error_message()]
		)
		return {}

	if not json.data is Dictionary:
		push_error("La racine JSON doit être un objet : %s" % path)
		return {}

	return json.data as Dictionary
```

### 20.1 Explication de `FileAccess.open()`

Le premier argument `path` est le chemin du fichier.

Le second argument `FileAccess.READ` indique une ouverture en lecture seule.

La fonction retourne un objet `FileAccess` ou `null`.

`FileAccess.get_open_error()` fournit le dernier code d’erreur d’ouverture.

### 20.2 Explication de `JSON.parse()`

`json.parse(text)` analyse la chaîne.

Le retour `Error` indique si la syntaxe est valide.

`json.data` contient la valeur décodée.

La racine peut techniquement être un tableau, un nombre ou une chaîne. Le contrat de ce projet exige un dictionnaire, donc le type est contrôlé explicitement.

## 21. Valider un dictionnaire JSON

### 21.1 Lire un champ obligatoire

> **[VSC] Visual Studio Code - Créer :** `res://src/core/data/dictionary_reader.gd`.

```gdscript
class_name DictionaryReader
extends RefCounted

static func require_string(
	data: Dictionary,
	key: StringName,
	errors: PackedStringArray
) -> String:
	if not data.has(key):
		errors.append("Champ obligatoire absent : %s" % key)
		return ""

	var value: Variant = data[key]
	if not value is String:
		errors.append("Le champ %s doit être une chaîne" % key)
		return ""

	var text := String(value).strip_edges()
	if text.is_empty():
		errors.append("Le champ %s ne peut pas être vide" % key)

	return text
```

### 21.2 Explication des paramètres

`data` est le dictionnaire source.

`key` est la clé recherchée.

`errors` est une collection partagée dans laquelle la fonction ajoute ses diagnostics.

La fonction retourne une chaîne normalisée. Une chaîne vide représente une absence ou une valeur invalide, mais les détails restent dans `errors`.

### 21.3 Lire un nombre

> **[VSC] Visual Studio Code - Ajouter :** dans `dictionary_reader.gd`.

```gdscript
static func require_float(
	data: Dictionary,
	key: StringName,
	minimum: float,
	maximum: float,
	errors: PackedStringArray
) -> float:
	if not data.has(key):
		errors.append("Champ obligatoire absent : %s" % key)
		return minimum

	var value: Variant = data[key]
	if not value is float and not value is int:
		errors.append("Le champ %s doit être numérique" % key)
		return minimum

	var number := float(value)
	if number < minimum or number > maximum:
		errors.append(
			"Le champ %s doit être compris entre %s et %s"
			% [key, minimum, maximum]
		)

	return clampf(number, minimum, maximum)
```

JSON peut représenter `4` ou `4.0`. La validation accepte donc `int` et `float`, puis convertit vers `float`.

## 22. Convertir JSON vers une Resource

> **[VSC] Visual Studio Code - Créer :** `res://src/features/beacons/infrastructure/beacon_json_mapper.gd`.

```gdscript
class_name BeaconJsonMapper
extends RefCounted

func from_dictionary(data: Dictionary) -> BeaconProfile:
	var errors := PackedStringArray()
	var profile := BeaconProfile.new()

	profile.id = StringName(
		DictionaryReader.require_string(data, &"id", errors)
	)
	profile.display_name = DictionaryReader.require_string(
		data,
		&"display_name",
		errors
	)
	profile.description = String(data.get(&"description", ""))
	profile.activation_radius = DictionaryReader.require_float(
		data,
		&"activation_radius",
		0.1,
		1000.0,
		errors
	)
	profile.cooldown_seconds = DictionaryReader.require_float(
		data,
		&"cooldown_seconds",
		0.0,
		3600.0,
		errors
	)
	profile.enabled_by_default = bool(data.get(&"enabled_by_default", true))
	profile.tags = _read_tags(data.get(&"tags", []), errors)

	errors.append_array(profile.validate())
	if not errors.is_empty():
		for message in errors:
			push_error("Beacon JSON : %s" % message)
		return null

	return profile

func _read_tags(value: Variant, errors: PackedStringArray) -> Array[StringName]:
	var tags: Array[StringName] = []
	if not value is Array:
		errors.append("tags doit être un tableau")
		return tags

	for index in value.size():
		var item: Variant = value[index]
		if not item is String:
			errors.append("tags[%d] doit être une chaîne" % index)
			continue
		tags.append(StringName(String(item)))

	return tags
```

### 22.1 Pourquoi retourner `null`

Le type de retour écrit `BeaconProfile`, mais GDScript autorise une référence nulle pour les objets.

Le code appelant doit vérifier le résultat.

### 22.2 Pourquoi valider deux fois

Le mapper vérifie la structure externe du JSON.

`profile.validate()` vérifie les invariants propres au modèle métier.

Les deux niveaux ont des responsabilités différentes et évitent de lier le domaine au format JSON.

## 23. Charger un document JSON versionné

> **[VSC] Visual Studio Code - Créer :** `res://src/features/beacons/infrastructure/beacon_json_importer.gd`.

```gdscript
class_name BeaconJsonImporter
extends RefCounted

const CURRENT_FORMAT_VERSION := 1

var _reader := JsonFileReader.new()
var _mapper := BeaconJsonMapper.new()

func import_catalog(path: String) -> BeaconCatalog:
	var document := _reader.read_dictionary(path)
	if document.is_empty():
		return null

	var version := int(document.get(&"format_version", 0))
	if version != CURRENT_FORMAT_VERSION:
		push_error(
			"Version JSON non prise en charge : %d, attendue : %d"
			% [version, CURRENT_FORMAT_VERSION]
		)
		return null

	var entries: Variant = document.get(&"beacons", null)
	if not entries is Array:
		push_error("Le champ beacons doit être un tableau")
		return null

	var catalog := BeaconCatalog.new()
	for index in entries.size():
		var raw_entry: Variant = entries[index]
		if not raw_entry is Dictionary:
			push_error("beacons[%d] doit être un objet" % index)
			continue

		var profile := _mapper.from_dictionary(raw_entry as Dictionary)
		if profile == null:
			continue

		var error := catalog.register(profile)
		if error != OK:
			push_error("beacons[%d] refusé : %s" % [index, error_string(error)])

	return catalog
```

Le chapitre utilise une politique simple : une version inconnue est refusée. Les migrations automatiques apparaîtront aux chapitres 8 et 9.

## 24. Versionner les formats

### 24.1 Version de document

`format_version` décrit la structure sérialisée.

Exemple :

- version 1 : `activation_radius` est un nombre ;
- version 2 : le rayon est déplacé dans un objet `interaction` ;
- version 3 : les tags deviennent des objets enrichis.

### 24.2 Version de contenu

Une version métier ou un numéro de révision peut suivre une donnée précise. Elle ne remplace pas `format_version`.

### 24.3 Compatibilité

Chaque lecteur doit définir :

- version minimale acceptée ;
- version courante ;
- comportement face à une version future ;
- stratégie de migration ;
- politique de journalisation ;
- possibilité de retour arrière.

### 24.4 Ne jamais deviner silencieusement

Lorsqu’un champ change de sens, ne pas inventer une valeur sans trace.

Préférer :

- une erreur claire ;
- une migration explicite ;
- une valeur par défaut documentée ;
- un rapport d’import.

## 25. `res://` et `user://`

### 25.1 `res://`

`res://` pointe vers la racine du projet.

Utiliser ce préfixe pour :

- scripts ;
- scènes ;
- données de conception ;
- configurations par défaut versionnées ;
- fixtures de test.

Dans un jeu exporté, ce contenu n’est pas un espace général d’écriture utilisateur.

### 25.2 `user://`

`user://` pointe vers un dossier d’écriture propre à l’application et à l’utilisateur.

Utiliser ce préfixe pour :

- préférences locales ;
- caches ;
- journaux ;
- données temporaires ;
- sauvegardes futures.

Ne jamais construire un chemin `user://` en supposant son emplacement physique exact.

## 26. Utiliser `ConfigFile`

`ConfigFile` manipule un format de type INI organisé en sections et clés.

Il peut conserver des types Variant Godot, contrairement à un INI strictement universel.

### 26.1 Configuration par défaut

> **[VSC] Visual Studio Code - Créer :** `res://config/default.cfg`.

```ini
[diagnostics]
log_level="info"
show_fps=false

[local_ai]
enabled=false
base_url="http://127.0.0.1:11434"
request_timeout_seconds=30.0

[data]
strict_validation=true
```

Cette configuration ne contient aucun secret.

### 26.2 Lire une configuration

> **[VSC] Visual Studio Code - Créer :** `res://src/core/config/app_config.gd`.

```gdscript
class_name AppConfig
extends RefCounted

var log_level: StringName = &"info"
var show_fps: bool = false
var local_ai_enabled: bool = false
var local_ai_base_url: String = "http://127.0.0.1:11434"
var request_timeout_seconds: float = 30.0
var strict_data_validation: bool = true
```

> **[VSC] Visual Studio Code - Créer :** `res://src/core/config/app_config_loader.gd`.

```gdscript
class_name AppConfigLoader
extends RefCounted

func load_config(default_path: String, override_path: String) -> AppConfig:
	var merged := ConfigFile.new()
	var default_error := merged.load(default_path)
	if default_error != OK:
		push_error("Configuration par défaut illisible : %s" % default_path)
		return null

	if FileAccess.file_exists(override_path):
		var override := ConfigFile.new()
		var override_error := override.load(override_path)
		if override_error != OK:
			push_error("Configuration locale illisible : %s" % override_path)
			return null
		_merge(merged, override)

	return _map(merged)

func _merge(target: ConfigFile, source: ConfigFile) -> void:
	for section in source.get_sections():
		for key in source.get_section_keys(section):
			target.set_value(section, key, source.get_value(section, key))

func _map(config: ConfigFile) -> AppConfig:
	var result := AppConfig.new()
	result.log_level = StringName(
		String(config.get_value("diagnostics", "log_level", "info"))
	)
	result.show_fps = bool(
		config.get_value("diagnostics", "show_fps", false)
	)
	result.local_ai_enabled = bool(
		config.get_value("local_ai", "enabled", false)
	)
	result.local_ai_base_url = String(
		config.get_value("local_ai", "base_url", "http://127.0.0.1:11434")
	)
	result.request_timeout_seconds = float(
		config.get_value("local_ai", "request_timeout_seconds", 30.0)
	)
	result.strict_data_validation = bool(
		config.get_value("data", "strict_validation", true)
	)
	return result
```

### 26.3 Explication de la fusion

`target` contient les valeurs par défaut.

`source` contient les valeurs locales prioritaires.

La boucle parcourt les sections puis les clés et remplace seulement les valeurs présentes dans la surcharge.

Le résultat final est converti vers `AppConfig`, ce qui évite de propager `ConfigFile` dans tout le projet.

## 27. Configuration locale

Le fichier local peut être créé au premier démarrage dans :

> **[LECTURE] Chemin runtime — Ne pas créer dans le dépôt.**

```text
user://app.cfg
```

Exemple de surcharge :

> **[LECTURE] Exemple de configuration locale — Ne pas committer.**

```ini
[diagnostics]
show_fps=true

[local_ai]
enabled=true
```

Les valeurs absentes continuent de provenir de `res://config/default.cfg`.

## 28. Secrets et données sensibles

Ne pas stocker dans les `.tres`, JSON ou `.cfg` versionnés :

- mots de passe ;
- jetons d’API ;
- clés privées ;
- identifiants personnels ;
- données de production confidentielles.

Le Livre I a défini les principes de sécurité. Les services IA locaux des chapitres 11 à 13 préciseront les mécanismes adaptés.

Une URL locale comme `http://127.0.0.1:11434` n’est pas un secret. Un jeton donnant accès à un service distant en est un.

## 29. Configuration par environnement

### 29.1 Niveaux proposés

`Project Asteria` distingue :

1. valeurs par défaut versionnées ;
2. surcharge locale non versionnée ;
3. arguments de lancement ou variables d’environnement pour l’intégration ;
4. valeurs runtime fournies par le bootstrap.

### 29.2 Ordre de priorité

> **[LECTURE] Ordre de fusion — Ne pas saisir.**

```text
valeurs par défaut
    ↓ remplacées par
configuration locale
    ↓ remplacée par
arguments ou environnement autorisés
    ↓ normalisée en
AppConfig typée et immuable pour les consommateurs
```

Le dernier niveau ne doit pas réécrire silencieusement les fichiers sources.

## 30. Injecter les données dans les services

Le catalogue est construit dans le point de composition puis injecté.

> **[LECTURE] Exemple GDScript — Assemblage dans le bootstrap.**

```gdscript
var loader := BeaconCatalogLoader.new()
var catalog := loader.load_catalog(BeaconCatalogPaths.PATHS)

var activation_service := BeaconActivationService.new()
var error := activation_service.configure(event_bus, catalog)
if error != OK:
	push_error("Configuration du service de balises impossible")
	return error
```

Le service reçoit un catalogue prêt à l’emploi. Il ne parcourt pas lui-même le système de fichiers et ne connaît pas `ConfigFile`.

## 31. Contrat du service consommateur

> **[VSC] Visual Studio Code - Modifier :** `res://src/features/beacons/application/beacon_activation_service.gd`.

```gdscript
var _event_bus: GameEventBus
var _catalog: BeaconCatalog

func configure(event_bus: GameEventBus, catalog: BeaconCatalog) -> Error:
	if event_bus == null or catalog == null:
		return ERR_INVALID_PARAMETER
	if catalog.size() == 0:
		return ERR_DOES_NOT_EXIST

	_event_bus = event_bus
	_catalog = catalog
	return OK

func get_profile(id: StringName) -> BeaconProfile:
	if _catalog == null:
		push_error("BeaconActivationService n’est pas configuré")
		return null
	return _catalog.get_profile(id)
```

Le service ne conserve pas une référence vers le chargeur. Il dépend du résultat abstrait : le catalogue.

## 32. Mode strict et mode dégradé

### 32.1 Mode strict

Utiliser pour :

- CI ;
- builds de développement ;
- outils de production ;
- données obligatoires.

Une erreur de donnée bloque le démarrage ou le pipeline.

### 32.2 Mode dégradé

Utiliser seulement lorsque :

- la fonctionnalité est optionnelle ;
- une valeur de remplacement sûre existe ;
- l’erreur est journalisée ;
- l’utilisateur comprend la perte de fonctionnalité.

### 32.3 Null Object de donnée

Une valeur de remplacement doit posséder un identifiant explicite, par exemple `beacon.missing`, et ne jamais masquer silencieusement une corruption.

## 33. Rapport de validation

Un import de données doit pouvoir produire :

- chemin source ;
- version du format ;
- nombre d’entrées lues ;
- nombre d’entrées acceptées ;
- erreurs par index ou identifiant ;
- doublons ;
- avertissements ;
- durée de traitement.

Le renvoi au chapitre 28 est volontaire. Le chapitre 7 se limite à un **rapport d’import local**, destiné à expliquer pourquoi un catalogue a été accepté ou refusé.

Le chapitre 27 ajoutera les tests automatisés et les assertions capables de vérifier ces rapports. Le chapitre 28, intitulé **« Journalisation, diagnostic et reproductibilité »**, généralisera ensuite cette discipline à l’ensemble du projet : niveaux de journal, contexte d’exécution, identifiants de corrélation, graines aléatoires, versions, durées et informations nécessaires pour reproduire une anomalie.

La frontière est donc :

> **[LECTURE] Répartition des responsabilités — Ne pas saisir.**

```text
chapitre 7  : rapport d’import de données
chapitre 27 : vérification automatisée du résultat
chapitre 28 : journalisation et reproductibilité de tout le runtime
```

## 34. Exercice guidé

### 34.1 Objectif

Créer un mini-catalogue de balises chargé depuis deux `Resource`, puis vérifier un document JSON d’import sans l’utiliser comme sauvegarde.

### 34.2 Fichiers à créer

> **[LECTURE] Arborescence cible — Ne pas saisir.**

```text
res://
├── config/
│   └── default.cfg
├── data/
│   ├── beacons/
│   │   ├── beacon_training.tres
│   │   ├── beacon_village_west.tres
│   │   └── catalog_paths.gd
│   └── import/
│       └── beacons.json
└── src/
    ├── core/
    │   ├── config/
    │   │   ├── app_config.gd
    │   │   └── app_config_loader.gd
    │   └── data/
    │       ├── dictionary_reader.gd
    │       ├── json_file_reader.gd
    │       └── stable_id.gd
    └── features/
        └── beacons/
            ├── application/
            │   └── beacon_catalog.gd
            ├── domain/
            │   ├── beacon_profile.gd
            │   └── beacon_runtime_state.gd
            └── infrastructure/
                ├── beacon_catalog_loader.gd
                ├── beacon_json_importer.gd
                └── beacon_json_mapper.gd
```

### 34.3 Deuxième balise

> **[APP] Godot - Créer :** une ressource `BeaconProfile` nommée `res://data/beacons/beacon_village_west.tres`.

Dans la boîte de dialogue **Create New Resource**, choisir `BeaconProfile`, puis renseigner dans l’Inspector :

- `id` : `beacon.village.west` ;
- `display_name` : `Balise ouest du village` ;
- `activation_radius` : `6.0` ;
- `cooldown_seconds` : `5.0` ;
- tags : `village`, `navigation`.

Godot génère le fichier `.tres`. Son contenu textuel doit être équivalent à l’exemple suivant ; les identifiants internes peuvent différer sans modifier le résultat.

> **[LECTURE] Contenu sérialisé attendu de `res://data/beacons/beacon_village_west.tres` — Ne pas recopier si la ressource a été créée dans Godot.**

```ini
[gd_resource type="Resource" script_class="BeaconProfile" load_steps=2 format=3]

[ext_resource type="Script" path="res://src/features/beacons/domain/beacon_profile.gd" id="1_profile"]

[resource]
script = ExtResource("1_profile")
id = &"beacon.village.west"
display_name = "Balise ouest du village"
activation_radius = 6.0
cooldown_seconds = 5.0
tags = Array[StringName]([&"village", &"navigation"])
```

Explication :

- `[gd_resource ...]` déclare un fichier de ressource texte Godot ;
- `script_class="BeaconProfile"` indique la classe personnalisée ;
- `[ext_resource ...]` référence le script qui définit cette classe ;
- `script = ExtResource("1_profile")` associe le script à l’instance ;
- `&"beacon.village.west"` est un littéral `StringName` stable ;
- `Array[StringName](...)` conserve le type des tags ;
- les valeurs appartiennent à la définition de conception, pas à l’état runtime.

Ajouter ensuite les deux chemins au catalogue.

> **[VSC] Visual Studio Code - Modifier :** `res://data/beacons/catalog_paths.gd`.

```gdscript
class_name BeaconCatalogPaths
extends RefCounted

const PATHS: Array[String] = [
	"res://data/beacons/beacon_training.tres",
	"res://data/beacons/beacon_village_west.tres",
]
```

`PATHS` est un tableau constant de chemins de ressources. L’ordre est explicite et versionné ; le chargeur ne dépend donc pas de l’ordre variable d’un parcours de dossier.

### 34.4 Scène de vérification

> **[VSC] Visual Studio Code - Créer :** `res://scenes/learning/ch07_data_demo.gd`.

```gdscript
extends Node

func _ready() -> void:
	var loader := BeaconCatalogLoader.new()
	var catalog := loader.load_catalog(BeaconCatalogPaths.PATHS)
	if catalog == null:
		push_error("Le catalogue de balises n’a pas pu être chargé.")
		return

	print("Profils chargés : %d" % catalog.size())
	for id: StringName in catalog.get_ids():
		var profile := catalog.get_profile(id)
		if profile == null:
			push_warning("Profil absent pour l’identifiant : %s" % id)
			continue
		print("%s — %s" % [id, profile.display_name])

	var importer := BeaconJsonImporter.new()
	var imported := importer.import_catalog("res://data/import/beacons.json")
	if imported != null:
		print("Profils JSON valides : %d" % imported.size())

	var config_loader := AppConfigLoader.new()
	var config := config_loader.load_config(
		"res://config/default.cfg",
		"user://app.cfg"
	)
	if config != null:
		print("Validation stricte : %s" % config.strict_data_validation)
```

#### 34.4.1 Déclaration et point d’entrée

- `extends Node` fait du script un nœud pouvant être attaché à une scène ;
- `_ready()` est appelé lorsque le nœud entre dans l’arbre et que ses enfants sont prêts ;
- `-> void` indique que la fonction ne renvoie aucune valeur.

#### 34.4.2 Chargement du catalogue de Resources

- `BeaconCatalogLoader.new()` construit le chargeur ;
- `BeaconCatalogPaths.PATHS` fournit les deux chemins déclarés à la section précédente ;
- `load_catalog()` renvoie un `BeaconCatalog` valide ou `null` en cas d’échec ;
- le test `catalog == null` empêche d’appeler `size()` sur une référence absente ;
- `push_error()` consigne la cause dans le débogueur ;
- `return` arrête `_ready()` puisque les vérifications suivantes dépendent du catalogue.

#### 34.4.3 Affichage des profils

- `catalog.size()` renvoie le nombre de profils acceptés ;
- `%d` réserve un emplacement pour un entier ;
- l’opérateur `%` remplace cet emplacement par la valeur fournie ;
- `catalog.get_ids()` renvoie les identifiants triés ;
- `id: StringName` type la variable locale de boucle ;
- `get_profile(id)` récupère le profil associé à la clé courante ;
- `continue` passe à l’identifiant suivant lorsqu’un profil manque ;
- `"%s — %s"` contient deux emplacements textuels ;
- `[id, profile.display_name]` fournit les deux valeurs dans le même ordre.

#### 34.4.4 Vérification du JSON

- `BeaconJsonImporter.new()` crée l’importeur ;
- `import_catalog(path)` lit, analyse, valide et convertit le document ;
- le chemin appartient à `res://`, donc au projet versionné ;
- `imported != null` distingue un catalogue valide d’un import refusé ;
- le nombre affiché correspond uniquement aux profils ayant franchi toutes les validations.

#### 34.4.5 Chargement de la configuration

- `AppConfigLoader.new()` crée le chargeur de configuration ;
- le premier argument est la configuration par défaut obligatoire ;
- le second est la surcharge locale facultative ;
- les parenthèses réparties sur plusieurs lignes ne changent pas l’appel ;
- `config != null` protège l’accès à la propriété ;
- `strict_data_validation` indique si les données invalides doivent bloquer le démarrage.

Cette scène vérifie trois frontières différentes : Resources typées, JSON externe validé et configuration locale fusionnée. Elle n’écrit aucune sauvegarde.

### 34.5 Résultat attendu

> **[SORTIE] Résultat attendu - Ne pas saisir :** l’ordre des identifiants est trié par `get_ids()`.

```text
Profils chargés : 2
beacon.training — Balise d’entraînement
beacon.village.west — Balise ouest du village
Profils JSON valides : 1
Validation stricte : true
```

### 34.6 Vérifications négatives

Modifier temporairement une copie de test pour vérifier que le système détecte :

- identifiant vide ;
- identifiant dupliqué ;
- rayon négatif ;
- champ JSON absent ;
- tableau `tags` contenant un nombre ;
- `format_version` inconnue ;
- fichier absent ;
- configuration locale invalide.

Restaurer ensuite les fichiers valides.

## 35. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

Chaque erreur ci-dessous comporte un exemple fautif et un exemple corrigé. Les fragments sont volontairement courts afin d’isoler la différence importante.

### 35.1 Modifier une Resource partagée pendant le gameplay

**Symptôme :** plusieurs instances changent en même temps, car elles référencent la même Resource chargée depuis le même chemin.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
func update_cooldown(delta: float) -> void:
	profile.cooldown_seconds -= delta
```

Le code modifie la définition de conception `profile`. Toute autre balise utilisant cette même instance voit aussi la nouvelle valeur.

**Correction :** conserver la durée configurée dans `BeaconProfile` et l’évolution courante dans `BeaconRuntimeState`.

> **[VSC] Visual Studio Code - Exemple corrigé à adapter dans le composant runtime.**

```gdscript
func update_cooldown(delta: float) -> void:
	runtime_state.tick(delta)
```

`delta` représente le temps écoulé. La méthode `tick()` soustrait cette durée de `cooldown_remaining` et utilise `maxf()` pour empêcher une valeur négative. La Resource reste inchangée.

### 35.2 Utiliser le nom affiché comme identifiant

**Symptôme :** une traduction ou une correction éditoriale casse les références.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
profile.id = StringName(profile.display_name)
```

Après traduction, `Balise ouest du village` pourrait devenir `West village beacon`, ce qui changerait la clé.

**Correction :** utiliser une clé technique stable et conserver le texte visible séparément.

> **[VSC] Visual Studio Code - Exemple corrigé dans une Resource de conception.**

```gdscript
profile.id = &"beacon.village.west"
profile.display_name = "Balise ouest du village"
```

L’identifiant sert aux relations métier ; `display_name` peut être traduit sans modifier ces relations.

### 35.3 Accepter tout JSON syntaxiquement valide

**Symptôme :** le parseur accepte le document, puis le gameplay échoue sur un champ absent ou du mauvais type.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
var data = JSON.parse_string(text)
var radius: float = data["activation_radius"]
```

Un JSON peut être syntaxiquement valide tout en ayant une racine tableau, un champ absent ou une chaîne à la place d’un nombre.

**Correction :** vérifier successivement la racine, les champs, leurs types et les règles métier.

> **[VSC] Visual Studio Code - Exemple corrigé à la frontière JSON.**

```gdscript
var data = JSON.parse_string(text)
if not data is Dictionary:
	push_error("La racine JSON doit être un objet.")
	return null

var row: Dictionary = data
if not row.has("activation_radius"):
	push_error("Champ activation_radius absent.")
	return null

var raw_radius: Variant = row["activation_radius"]
if not (raw_radius is float or raw_radius is int):
	push_error("activation_radius doit être numérique.")
	return null

var radius := float(raw_radius)
if radius < 0.0:
	push_error("activation_radius ne peut pas être négatif.")
	return null
```

Chaque contrôle produit une erreur proche de sa cause au lieu d’attendre un échec tardif.

### 35.4 Lire un fichier texte avec `ResourceLoader`

**Symptôme :** chargement impossible d’un JSON brut qui n’est pas pris en charge par un chargeur de ressource enregistré.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
var document = ResourceLoader.load("res://data/import/beacons.json")
```

`ResourceLoader` charge les formats reconnus comme ressources. Un fichier texte ordinaire doit être lu comme texte.

**Correction :** utiliser `FileAccess`, puis analyser le contenu avec `JSON`.

> **[VSC] Visual Studio Code - Exemple corrigé dans un lecteur JSON.**

```gdscript
var file := FileAccess.open(
	"res://data/import/beacons.json",
	FileAccess.READ
)
if file == null:
	push_error("Impossible d’ouvrir le document JSON.")
	return null

var parser := JSON.new()
var error := parser.parse(file.get_as_text())
if error != OK:
	push_error(parser.get_error_message())
	return null

var document: Variant = parser.data
```

`FileAccess.READ` ouvre le fichier en lecture. `parser.data` n’est utilisé qu’après un retour `OK`.

### 35.5 Enregistrer l’état du joueur dans une `.tres` de conception

**Symptôme :** les données sources sont modifiées dans l’éditeur ou l’écriture échoue dans un export où `res://` est en lecture seule.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
profile.enabled_by_default = false
ResourceSaver.save(profile, "res://data/beacons/beacon_training.tres")
```

La définition versionnée est utilisée comme sauvegarde et reçoit en plus une propriété runtime qui ne lui appartient pas.

**Correction :** conserver l’état vivant dans un objet runtime et transmettre plus tard un instantané au système de sauvegarde du chapitre 9.

> **[VSC] Visual Studio Code - Exemple corrigé pour le chapitre 7.**

```gdscript
var runtime_state := BeaconRuntimeState.new(profile)
runtime_state.record_activation(profile.cooldown_seconds)
```

Ce chapitre ne persiste pas encore cet objet. Le chapitre 9 créera un format versionné sous `user://` et une procédure de migration.

### 35.6 Mettre un secret dans `default.cfg`

**Symptôme :** le secret apparaît dans Git, dans les archives et éventuellement dans le paquet exporté.

> **[LECTURE] Exemple fautif — Ne pas recopier et ne jamais utiliser de valeur réelle.**

```ini
[remote_service]
api_token="secret-reel-a-ne-jamais-committer"
```

**Correction :** ne versionner que les options non sensibles et recevoir le secret depuis un mécanisme externe autorisé.

> **[VSC] Visual Studio Code - Exemple corrigé de configuration versionnée.**

```ini
[remote_service]
enabled=false
base_url="https://example.invalid"
```

> **[VSC] Visual Studio Code - Exemple de lecture runtime à traiter avec la politique de sécurité des chapitres 11 à 13.**

```gdscript
var api_token := OS.get_environment("ASTERIA_API_TOKEN")
if api_token.is_empty():
	push_warning("ASTERIA_API_TOKEN n’est pas défini.")
```

Cet exemple ne constitue pas à lui seul un gestionnaire de secrets. Il montre seulement que la valeur ne doit pas être écrite dans le dépôt.

### 35.7 Parcourir un dossier sans trier ni valider

**Symptôme :** l’ordre varie selon le système ou l’historique du dossier, ce qui rend les résultats difficiles à reproduire.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
for file_name in DirAccess.get_files_at("res://data/beacons"):
	catalog.add_profile(load("res://data/beacons/" + file_name))
```

Le code ne trie pas, ne filtre pas l’extension, ne vérifie ni le type ni le résultat de `load()`.

**Correction :** utiliser une liste explicite ou construire une liste filtrée, triée et validée.

> **[VSC] Visual Studio Code - Exemple corrigé pour un parcours déterministe.**

```gdscript
var paths: Array[String] = []
for file_name: String in DirAccess.get_files_at("res://data/beacons"):
	if file_name.get_extension() == "tres":
		paths.append("res://data/beacons/" + file_name)
paths.sort()

for path: String in paths:
	var profile := load(path) as BeaconProfile
	if profile == null:
		push_error("Resource BeaconProfile invalide : %s" % path)
		continue
	catalog.add_profile(profile)
```

Le chapitre privilégie malgré tout `BeaconCatalogPaths.PATHS` tant que la collection reste petite, car cette liste rend les changements explicites dans Git.

### 35.8 Propager des dictionnaires partout

**Symptôme :** les consommateurs répètent des clés magiques et découvrent les erreurs trop tard.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
func activate_beacon(data: Dictionary) -> void:
	print(data["display_name"])
	start_cooldown(float(data["cooldown_seconds"]))
```

Chaque appelant doit connaître l’orthographe des clés et les conversions attendues.

**Correction :** convertir le dictionnaire à la frontière puis transmettre un objet typé.

> **[VSC] Visual Studio Code - Exemple corrigé dans le mapper puis le service.**

```gdscript
var mapper := BeaconJsonMapper.new()
var profile := mapper.from_dictionary(data)
if profile == null:
	return

catalog.register(profile)
activation_service.configure(event_bus, catalog)
```

`BeaconJsonMapper` concentre les clés et validations. `BeaconCatalog` et `BeaconProfile` fournissent ensuite des méthodes et propriétés connues par le moteur et l’éditeur.

## 36. Checklist de fin de chapitre

- [ ] Les données de conception sont séparées de l’état runtime.
- [ ] Chaque définition possède un identifiant stable.
- [ ] Les noms affichés ne servent pas de clés métier.
- [ ] Les `Resource` partagées ne sont pas modifiées implicitement.
- [ ] Les duplications sont explicites.
- [ ] Le catalogue refuse les doublons.
- [ ] Le chargement vérifie les types.
- [ ] Le JSON vérifie syntaxe, structure et métier.
- [ ] Le format JSON possède une version.
- [ ] `res://` et `user://` sont utilisés correctement.
- [ ] La configuration par défaut ne contient aucun secret.
- [ ] La surcharge locale ne remplace que les clés prévues.
- [ ] Les services reçoivent des objets typés par injection.
- [ ] Les erreurs ne sont pas masquées.
- [ ] Les chemins et actions possèdent leurs repères d’utilisation.
- [ ] Aucun PDF intermédiaire n’a été construit.

## 37. Parcours Solo

Le parcours Solo peut conserver :

- des catalogues de taille modérée ;
- une liste explicite de chemins ;
- des `.tres` éditées dans Godot ;
- un import JSON manuel ;
- une configuration par défaut et une surcharge `user://` ;
- une validation au démarrage.

L’objectif est la lisibilité et la sécurité, pas la création immédiate d’un pipeline complexe.

## 38. Parcours Studio

Le parcours Studio ajoute :

- propriétaire de chaque schéma ;
- conventions d’identifiants partagées ;
- génération de rapports d’import ;
- validation en CI ;
- revue des changements de format ;
- jeux de fixtures valides et invalides ;
- politique de dépréciation ;
- outils d’édition ;
- migration documentée ;
- séparation des données de développement, test et production.

Toute évolution de format doit être accompagnée d’un exemple, d’une stratégie de compatibilité et d’un test.

## 39. Audit rapide après modification de données

Après chaque lot de données :

1. vérifier les identifiants ;
2. rechercher les doublons ;
3. lancer les méthodes `validate()` ;
4. contrôler les types issus du JSON ;
5. vérifier la version du format ;
6. confirmer les chemins `res://` et `user://` ;
7. inspecter le diff Git ;
8. exécuter la validation légère sans PDF ;
9. enregistrer les réserves runtime.

## 40. Sources officielles vérifiées

Les concepts du chapitre ont été confrontés aux pages officielles de Godot 4.7 concernant :

- Resources : `https://docs.godotengine.org/en/4.7/tutorials/scripting/resources.html` ;
- système de fichiers : `https://docs.godotengine.org/en/4.7/tutorials/scripting/filesystem.html` ;
- `ConfigFile` : `https://docs.godotengine.org/en/4.7/classes/class_configfile.html` ;
- `ResourceLoader` : `https://docs.godotengine.org/en/4.7/classes/class_resourceloader.html` ;
- `FileAccess` : `https://docs.godotengine.org/en/4.7/classes/class_fileaccess.html` ;
- `JSON` : `https://docs.godotengine.org/en/4.7/classes/class_json.html` ;
- `Resource.duplicate()` et `resource_local_to_scene` : `https://docs.godotengine.org/en/4.7/classes/class_resource.html`.

## 41. Frontière avec le chapitre suivant

Le chapitre 7 fournit :

- données de conception typées ;
- catalogues en mémoire ;
- import JSON validé ;
- configuration locale ;
- identifiants et versions de format.

Le chapitre 8 ajoutera :

- SQLite ;
- schéma relationnel ;
- migrations SQL ;
- transactions ;
- repositories persistants ;
- intégrité référentielle ;
- sauvegardes de bases de développement ;
- diagnostic des requêtes.

Il ne devra pas remplacer les `Resource` lorsqu’elles restent le meilleur support pour les données de conception éditables.

## 42. Résultat du chapitre

Le projet dispose maintenant d’une stratégie de données explicite :

- `Resource` pour les définitions intégrées à Godot ;
- objets runtime pour l’état vivant ;
- JSON pour les échanges contrôlés ;
- `ConfigFile` pour les configurations INI locales ;
- identifiants stables pour relier les systèmes ;
- validation et versionnement à chaque frontière ;
- injection des catalogues dans les services.

Cette base prépare SQLite et les sauvegardes sans confondre données de conception, configuration technique et progression du joueur.
