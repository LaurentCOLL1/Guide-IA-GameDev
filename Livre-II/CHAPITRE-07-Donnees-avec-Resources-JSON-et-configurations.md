---
title: "Livre II — Chapitre 7 : Données avec Resources, JSON et configurations"
id: "DOC-L2-CH07"
status: "reviewed"
version: "1.0.1"
lang: "fr-FR"
book: "Livre II"
chapter: 7
last-verified: "2026-07-19"
audit-status: "complete"
audit-date: "2026-07-19"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-07.md"
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
> **Niveau de raisonnement conseillé :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-07.md`.

## 1. Rôle du chapitre

Les chapitres précédents ont construit le projet, le langage, les scènes, l’architecture, les services et les interactions. Le projet doit maintenant organiser ses données sans les confondre avec les objets actifs du `SceneTree`.

Une architecture de données improvisée produit souvent :

- des valeurs recopiées dans plusieurs scripts ;
- des `Dictionary` dont les clés ne sont jamais contrôlées ;
- des Resources partagées modifiées accidentellement au runtime ;
- des identifiants liés au texte affiché ;
- un JSON accepté uniquement parce que sa syntaxe est valide ;
- des fichiers de configuration mélangés aux sauvegardes ;
- des chemins dispersés dans les fonctionnalités ;
- une dépendance directe à `FileAccess` ou `ResourceLoader` dans le code métier ;
- des erreurs silencieuses après export ;
- une migration future vers SQLite devenue coûteuse.

À la fin du chapitre, le lecteur doit savoir :

- distinguer données de conception, configuration, état runtime et persistance ;
- choisir entre `Resource`, JSON, `ConfigFile`, mémoire et future base SQLite ;
- créer et valider un catalogue typé ;
- utiliser des identifiants stables ;
- comprendre le cache et le partage des Resources ;
- lire un JSON avec des erreurs localisables ;
- convertir les dictionnaires bruts en objet typé ;
- fusionner une configuration par défaut avec une surcharge d’environnement ;
- charger une Resource en vérifiant son chemin et son type ;
- injecter un repository au lieu de charger depuis chaque service ;
- préparer le chargement différé ;
- respecter les frontières avec SQLite et les sauvegardes.

## 2. Prérequis et réutilisation

Le lecteur doit connaître :

- les types, fonctions, tableaux et dictionnaires du chapitre 2 ;
- les Resources personnalisées du chapitre 3 ;
- l’organisation feature-first du chapitre 4 ;
- l’injection et le point de composition du chapitre 5 ;
- le remappage temporaire du chapitre 6.

Le chapitre réutilise :

- `BeaconProfile` ;
- `StatusBeacon` ;
- `AppBootstrap` ;
- `ServiceRegistry` ;
- le dossier `data/beacons` ;
- la convention des identifiants stables.

Le chapitre 3 expliquait comment créer une première Resource. Le présent chapitre ne répète pas cette initiation : il traite un ensemble de données, sa validation, son chargement et son exposition aux services.

## 3. Périmètre et frontières

Ce chapitre définit :

- une taxonomie des données ;
- un catalogue `BeaconCatalog` ;
- des objets de diagnostic ;
- un repository de lecture ;
- un chargeur de Resource centralisé ;
- un chargeur JSON explicite ;
- une configuration runtime typée ;
- deux couches de configuration ;
- une politique de cache et d’immuabilité ;
- un exemple de chargement en arrière-plan ;
- un contrat documentaire de données.

Il ne définit pas encore :

- SQLite, les transactions et les migrations de base, réservés au chapitre 8 ;
- l’écriture d’une sauvegarde sous `user://`, réservée au chapitre 9 ;
- la migration complète des anciennes sauvegardes, réservée au chapitre 9 ;
- la mémoire vectorielle, réservée au chapitre 10 ;
- les appels HTTP et WebSocket, réservés aux chapitres 11 et 12 ;
- l’inventaire complet, réservé au chapitre 20 ;
- les outils d’édition avancés, réservés au chapitre 26 ;
- les tests automatisés complets, réservés au chapitre 27.

> **Frontière essentielle :** une définition décrit ce qu’une chose est. Un état runtime décrit ce qui lui arrive pendant une session. Une sauvegarde décrit ce qui doit survivre à la fermeture du jeu.

## 4. Les quatre familles de données

### 4.1 Données de conception

Les données de conception sont produites par l’équipe et livrées avec le jeu.

Exemples : profil de balise, définition d’objet, coût d’une compétence, courbe de progression ou catalogue de quêtes.

Elles sont généralement :

- versionnées dans Git ;
- placées sous `res://` ;
- éditées dans Godot ou un outil de production ;
- considérées comme canoniques ;
- lues sans être modifiées par le gameplay.

Dans l’exercice, `BeaconProfile` et `BeaconCatalog` sont des données de conception.

### 4.2 Configuration d’exécution

Une configuration d’exécution choisit comment le programme se comporte dans un environnement donné.

Exemples : niveau de journalisation, activation facultative des services IA, URL locale, délai maximal et chemin du catalogue.

Elle ne représente ni une règle de gameplay permanente ni la progression du joueur.

### 4.3 État runtime

L’état runtime change pendant la session : disponibilité actuelle d’une balise, cooldown restant, cible regardée, requête en attente ou menu ouvert.

Cet état appartient à un nœud, un objet `RefCounted` ou une structure dédiée. Il ne doit pas être écrit dans la Resource canonique.

### 4.4 Données persistantes du joueur

Les données persistantes survivent à la fermeture du jeu : progression, inventaire, position, réglages remappés et historique de quêtes.

Le chapitre 7 prépare les responsabilités. Le chapitre 9 implémentera l’écriture, le chargement et la migration des sauvegardes.

## 5. Matrice de choix du format

| Besoin | Format principal | Motif |
|---|---|---|
| données typées éditables dans Godot | `Resource` `.tres` | Inspector, types, références, sérialisation native |
| configuration interopérable | JSON | texte lisible par Godot, Python et d’autres outils |
| petite configuration propre à Godot | `ConfigFile` | sections, clés et valeurs `Variant` |
| état temporaire | objet runtime | aucune écriture inutile |
| données relationnelles persistantes | SQLite au chapitre 8 | requêtes, index, transactions, migrations |
| sauvegarde de partie | format versionné au chapitre 9 | contrôle de compatibilité |

Le choix dépend :

- du producteur et du consommateur ;
- du besoin de typage ;
- de la fréquence de modification ;
- de la taille ;
- des requêtes nécessaires ;
- de l’interopérabilité ;
- du niveau de confiance accordé à la source.

## 6. Architecture retenue

> **[LECTURE] Architecture de données — Ne pas saisir.**

```text
Resources et JSON sous res://
        ↓
chargeurs d’infrastructure
        ↓
validation de structure et de contenu
        ↓
objets typés et catalogues
        ↓
repositories injectés par AppBootstrap
        ↓
services et fonctionnalités
        ↓
état runtime séparé
```

Règles :

- le domaine ne connaît pas `FileAccess` ;
- les services ne construisent pas eux-mêmes les chargeurs ;
- les chemins sont centralisés ;
- les fichiers sont validés avant exposition ;
- les erreurs sont structurées ;
- les Resources canoniques sont traitées comme données en lecture seule.

## 7. Créer l’arborescence

> **[PS] PowerShell 7 — Exécuter depuis la racine du projet Godot.**

```powershell
$paths = @(
  "config/defaults",
  "config/environments",
  "docs/architecture",
  "src/core/config",
  "src/core/data",
  "src/features/beacons/application",
  "src/features/beacons/data",
  "src/features/beacons/infrastructure",
  "scenes/learning"
)

$paths | ForEach-Object {
  New-Item -ItemType Directory -Force -Path $_ | Out-Null
}
```

Explication :

- `$paths` est un tableau PowerShell ;
- `@(...)` permet de l’écrire sur plusieurs lignes ;
- `|` transmet chaque élément à `ForEach-Object` ;
- `$_` représente le chemin courant ;
- `New-Item` crée le dossier ;
- `-Force` accepte un dossier déjà présent ;
- `Out-Null` masque uniquement la sortie normale.

> **[SORTIE] Structure cible — Ne pas saisir.**

```text
Project Asteria/
├── config/
│   ├── defaults/
│   └── environments/
├── data/
│   └── beacons/
├── docs/
│   └── architecture/
├── scenes/
│   └── learning/
└── src/
    ├── core/
    │   ├── config/
    │   └── data/
    └── features/
        └── beacons/
            ├── application/
            ├── data/
            └── infrastructure/
```

## 8. Identifiants stables

### 8.1 Identifiant et nom affiché

> **[LECTURE] Comparaison conceptuelle — Ne pas saisir.**

```text
identifiant technique   default_beacon
nom français            Balise Asteria
nom anglais             Asteria Beacon
```

Le nom peut être traduit. L’identifiant doit rester stable afin de ne pas casser une référence de catalogue, une sauvegarde future, une table SQLite, un événement ou un test.

### 8.2 Convention du projet

Pour une définition de gameplay :

- type `StringName` dans les Resources ;
- minuscules ASCII ;
- mots séparés par `_` ;
- aucune espace ;
- aucune traduction ;
- aucune version dans l’identifiant ;
- unicité dans le catalogue.

Exemples valides : `default_beacon`, `ancient_gate_beacon`, `tutorial_signal_01`.

Exemples à éviter : `Balise Asteria`, `Beacon-v2-final`, `objet_énergie`, `New Beacon`.

## 9. Partage et cache des Resources

### 9.1 Une même ressource peut être partagée

> **[LECTURE] Exemple de partage — Ne pas modifier la Resource.**

```gdscript
var first := load(
	"res://data/beacons/default_beacon.tres"
) as BeaconProfile

var second := load(
	"res://data/beacons/default_beacon.tres"
) as BeaconProfile

print(first == second)
```

Dans le mode de cache normal, les deux variables référencent généralement la même Resource chargée.

Décomposition :

- `load(path)` charge synchroniquement une Resource ;
- `as BeaconProfile` renvoie l’objet typé ou `null` ;
- `first == second` compare les références ;
- une mutation effectuée par l’un des consommateurs peut être visible par les autres.

### 9.2 Règle d’immuabilité par convention

GDScript ne rend pas automatiquement une Resource immuable. Le projet adopte donc la règle suivante :

> **Une Resource chargée depuis `res://data` n’est jamais modifiée par le gameplay.**

Pour changer une définition, modifier son fichier, la relire et la versionner. Pour stocker un changement runtime, créer un objet d’état séparé qui conserve l’identifiant de la définition.

### 9.3 Limites de `duplicate()`

> **[LECTURE] Copie explicite — Étudier le paramètre.**

```gdscript
var runtime_copy := source_profile.duplicate(true) as BeaconProfile
```

- `source_profile` est l’origine ;
- `duplicate(deep)` crée une copie ;
- `true` est l’argument du paramètre `deep` ;
- les tableaux, dictionnaires et certaines sous-Resources internes peuvent être copiés profondément ;
- les Resources externes ne sont pas nécessairement dupliquées ;
- le retour général est casté en `BeaconProfile` ;
- `runtime_copy` vaut `null` si le type est incompatible.

Une copie ne remplace pas un véritable modèle d’état lorsque les valeurs changent souvent.

### 9.4 `resource_local_to_scene`

Lorsque `resource_local_to_scene` est activé avant l’instanciation, Godot peut créer une copie locale pour chaque instance de scène.

Cette propriété convient à une sous-Resource réellement propre à une instance. Elle ne convient pas à un catalogue global. Elle augmente également le nombre d’objets en mémoire et ne constitue pas un système de sauvegarde.

## 10. Décrire une erreur de données

> **[VSC] Visual Studio Code — Créer :** `src/core/data/data_validation_issue.gd`.

```gdscript
class_name DataValidationIssue
extends RefCounted
## Non-conformité structurée, indépendante de l’interface.

enum Severity {
	WARNING,
	ERROR,
}

var severity: Severity
var code: StringName
var location: String
var message: String


func _init(
	p_severity: Severity,
	p_code: StringName,
	p_location: String,
	p_message: String
) -> void:
	severity = p_severity
	code = p_code
	location = p_location
	message = p_message
```

Rôle des propriétés :

- `severity` indique si le problème bloque l’utilisation ;
- `code` est un identifiant stable comme `duplicate_id` ;
- `location` localise la valeur comme `entries[2].id` ;
- `message` explique le problème.

Paramètres du constructeur :

- `p_severity` reçoit une valeur de l’énumération ;
- `p_code` reçoit le code technique ;
- `p_location` reçoit le chemin logique ;
- `p_message` reçoit le texte lisible ;
- le préfixe `p_` distingue les paramètres des propriétés ;
- `-> void` indique qu’aucune valeur n’est renvoyée.

`RefCounted` convient car l’objet transporte des données et n’a pas besoin du `SceneTree`.

## 11. Accumuler les diagnostics

> **[VSC] Visual Studio Code — Créer :** `src/core/data/data_validation_report.gd`.

```gdscript
class_name DataValidationReport
extends RefCounted
## Accumule avertissements et erreurs.

var issues: Array[DataValidationIssue] = []


func add_warning(
	code: StringName,
	location: String,
	message: String
) -> void:
	issues.append(
		DataValidationIssue.new(
			DataValidationIssue.Severity.WARNING,
			code,
			location,
			message
		)
	)


func add_error(
	code: StringName,
	location: String,
	message: String
) -> void:
	issues.append(
		DataValidationIssue.new(
			DataValidationIssue.Severity.ERROR,
			code,
			location,
			message
		)
	)


func has_errors() -> bool:
	for issue: DataValidationIssue in issues:
		if issue.severity == DataValidationIssue.Severity.ERROR:
			return true
	return false


func is_valid() -> bool:
	return not has_errors()
```

Explication :

- `issues` est un tableau qui accepte uniquement `DataValidationIssue` ;
- `append(value)` ajoute un élément à la fin ;
- `add_warning()` et `add_error()` reçoivent code, emplacement et message ;
- `DataValidationIssue.new(...)` appelle le constructeur ;
- `has_errors()` parcourt les problèmes et renvoie `true` dès la première erreur ;
- `is_valid()` utilise `not` pour inverser le résultat ;
- un rapport peut être valide tout en contenant des avertissements.

> **[LECTURE] Parcours typé — Étudier la syntaxe.**

```gdscript
for issue: DataValidationIssue in issues:
```

- `for` démarre la boucle ;
- `issue` reçoit l’élément courant ;
- `: DataValidationIssue` impose son type ;
- `in issues` désigne la collection parcourue.

## 12. Créer le catalogue typé

> **[VSC] Visual Studio Code — Créer :** `src/features/beacons/data/beacon_catalog.gd`.

```gdscript
class_name BeaconCatalog
extends Resource
## Catalogue canonique des profils de balise.

const CURRENT_SCHEMA_VERSION: int = 1
const ID_PATTERN: String = "^[a-z0-9]+(?:_[a-z0-9]+)*$"

@export var schema_version: int = CURRENT_SCHEMA_VERSION
@export var entries: Array[BeaconProfile] = []


func validate() -> DataValidationReport:
	var report := DataValidationReport.new()
	var seen_ids: Dictionary = {}
	var id_regex := RegEx.new()

	var compile_error := id_regex.compile(ID_PATTERN)
	if compile_error != OK:
		report.add_error(
			&"validator_setup_failed",
			"id_pattern",
			"La règle interne des identifiants est invalide."
		)
		return report

	if schema_version != CURRENT_SCHEMA_VERSION:
		report.add_error(
			&"unsupported_schema",
			"schema_version",
			"Version de catalogue non prise en charge : %d."
			% schema_version
		)

	for index: int in range(entries.size()):
		var entry: BeaconProfile = entries[index]
		var location := "entries[%d]" % index

		if entry == null:
			report.add_error(
				&"null_entry",
				location,
				"Le catalogue contient une entrée vide."
			)
			continue

		if entry.id == &"":
			report.add_error(
				&"empty_id",
				location + ".id",
				"L’identifiant est vide."
			)
			continue

		if id_regex.search(String(entry.id)) == null:
			report.add_error(
				&"invalid_id_format",
				location + ".id",
				"Format d’identifiant invalide : %s." % entry.id
			)

		if seen_ids.has(entry.id):
			report.add_error(
				&"duplicate_id",
				location + ".id",
				"Identifiant dupliqué : %s." % entry.id
			)
			continue

		seen_ids[entry.id] = true

		if entry.display_name.strip_edges().is_empty():
			report.add_warning(
				&"empty_display_name",
				location + ".display_name",
				"Le nom affiché est vide."
			)

		if entry.cooldown_seconds <= 0.0:
			report.add_error(
				&"invalid_cooldown",
				location + ".cooldown_seconds",
				"Le cooldown doit être strictement positif."
			)

	return report


func find_by_id(id: StringName) -> BeaconProfile:
	for entry: BeaconProfile in entries:
		if entry != null and entry.id == id:
			return entry
	return null
```

### 12.1 Version de schéma

`CURRENT_SCHEMA_VERSION` est la version comprise par le code. `schema_version` est enregistrée dans le `.tres`.

Une version inconnue est refusée explicitement. Le chapitre 8 appliquera cette discipline aux migrations SQLite et le chapitre 9 aux sauvegardes.

### 12.2 Expression régulière

`ID_PATTERN` autorise des groupes ASCII minuscules séparés par un seul `_`.

`RegEx.new()` crée le moteur. `compile(pattern)` renvoie un code `Error`. La validation s’arrête si sa propre règle interne ne peut pas être compilée.

`search(text)` renvoie un résultat lorsqu’une correspondance existe, sinon `null`.

### 12.3 Validation des entrées

Variables locales :

- `report` accumule les problèmes ;
- `seen_ids` mémorise les identifiants déjà vus ;
- `index` est la position éditoriale ;
- `entry` est le profil courant ;
- `location` construit un chemin de diagnostic.

`range(entries.size())` produit les indices de `0` inclus jusqu’à la taille exclue.

`continue` abandonne uniquement l’itération courante. Il évite de lire les propriétés d’une entrée `null` ou sans identifiant.

> **[LECTURE] Enregistrement d’une clé — Étudier les crochets.**

```gdscript
seen_ids[entry.id] = true
```

- `seen_ids` est le dictionnaire ;
- les crochets sélectionnent la clé `entry.id` ;
- `true` sert de marqueur de présence ;
- la position du tableau ne devient jamais un identifiant métier.

### 12.4 Recherche par identifiant

`find_by_id(id)` reçoit un `StringName` et renvoie :

- la première `BeaconProfile` correspondante ;
- `null` si aucune définition n’existe.

Le consommateur doit traiter ce retour nullable.

## 13. Créer les Resources du catalogue

> **[APP] Godot Editor — Dans le dock FileSystem, dupliquer `data/beacons/default_beacon.tres` deux fois, puis renommer les copies.**

Créer :

- `data/beacons/gate_beacon.tres` ;
- `data/beacons/archive_beacon.tres`.

Modifier les identifiants, noms et messages dans l’Inspector.

> **[APP] Godot Editor — Créer une Resource `BeaconCatalog` sous `data/beacons/beacon_catalog.tres`.**

> **[APP] Godot Editor — Configurer le catalogue dans l’Inspector avec les valeurs suivantes.**

```text
Schema Version  1
Entries         3 éléments
  0             default_beacon.tres
  1             gate_beacon.tres
  2             archive_beacon.tres
```

Le catalogue et ses profils sont des Resources externes. Ils ne sont pas recopiés dans chaque scène.

## 14. Ajouter une validation dans l’éditeur

> **[VSC] Visual Studio Code — Créer :** `src/features/beacons/data/beacon_catalog_validator.gd`.

```gdscript
@tool
class_name BeaconCatalogValidator
extends Node
## Lance une validation depuis l’Inspector.

@export var catalog: BeaconCatalog
@export var validate_now: bool:
	set(value):
		validate_now = false
		if value:
			run_validation()


func run_validation() -> void:
	if catalog == null:
		push_error("BeaconCatalogValidator : catalogue absent.")
		return

	var report := catalog.validate()

	for issue: DataValidationIssue in report.issues:
		var rendered := "[%s] %s — %s" % [
			issue.code,
			issue.location,
			issue.message,
		]

		if issue.severity == DataValidationIssue.Severity.ERROR:
			push_error(rendered)
		else:
			push_warning(rendered)

	if report.is_valid():
		print("Catalogue de balises valide.")
```

Explication :

- `@tool` autorise le script dans l’éditeur ;
- `catalog` est assigné dans l’Inspector ;
- le setter reçoit la nouvelle valeur `value` ;
- la propriété revient à `false` pour agir comme un bouton ;
- `run_validation()` ne reçoit aucun paramètre et ne renvoie rien ;
- `rendered` assemble code, emplacement et message ;
- `push_error()` et `push_warning()` choisissent le niveau d’affichage.

> **[SORTIE] Exemple de diagnostic — Ne pas saisir.**

```text
[duplicate_id] entries[2].id — Identifiant dupliqué : default_beacon.
```

La chaîne contient trois `%s`. L’opérateur `%` remplace chacun d’eux par l’élément de même position dans le tableau.

## 15. Définir le contrat du repository

> **[VSC] Visual Studio Code — Créer :** `src/features/beacons/application/beacon_catalog_repository.gd`.

```gdscript
class_name BeaconCatalogRepository
extends RefCounted
## Contrat de lecture des définitions de balise.


func get_by_id(id: StringName) -> BeaconProfile:
	push_error(
		"BeaconCatalogRepository.get_by_id() doit être redéfini."
	)
	return null


func get_all() -> Array[BeaconProfile]:
	push_error(
		"BeaconCatalogRepository.get_all() doit être redéfini."
	)
	return []
```

`get_by_id(id)` reçoit l’identifiant et renvoie un profil ou `null`.

`get_all()` ne reçoit aucun argument et renvoie un tableau typé. Les erreurs rappellent qu’une sous-classe doit redéfinir ces fonctions.

GDScript ne fournit pas ici une interface formelle distincte. La classe de base fixe donc les signatures et les valeurs de repli.

## 16. Implémenter le repository Resource

> **[VSC] Visual Studio Code — Créer :** `src/features/beacons/infrastructure/resource_beacon_catalog_repository.gd`.

```gdscript
class_name ResourceBeaconCatalogRepository
extends BeaconCatalogRepository
## Lecture seule depuis un BeaconCatalog validé.

var _catalog: BeaconCatalog


func _init(catalog: BeaconCatalog) -> void:
	assert(catalog != null, "Le catalogue est obligatoire.")
	_catalog = catalog


func get_by_id(id: StringName) -> BeaconProfile:
	return _catalog.find_by_id(id)


func get_all() -> Array[BeaconProfile]:
	var result: Array[BeaconProfile] = []
	for entry: BeaconProfile in _catalog.entries:
		if entry != null:
			result.append(entry)
	return result
```

Le constructeur `_init(catalog)` reçoit la dépendance. `assert()` protège une erreur de programmation dans le point de composition ; il ne remplace pas la validation du contenu.

`get_all()` crée un nouveau tableau. Le consommateur peut modifier ce tableau local sans modifier `BeaconCatalog.entries`. Les profils restent partagés et doivent rester en lecture seule.

## 17. Charger le catalogue depuis un chemin contrôlé

> **[VSC] Visual Studio Code — Ajouter à `src/app/app_bootstrap.gd`.**

```gdscript
func _is_allowed_catalog_path(path: String) -> bool:
	if not path.begins_with("res://data/beacons/"):
		return false

	var extension := path.get_extension().to_lower()
	return extension in ["tres", "res"]


func _load_catalog_at(path: String) -> BeaconCatalog:
	if not _is_allowed_catalog_path(path):
		push_error("Chemin de catalogue refusé : %s." % path)
		return null

	if not ResourceLoader.exists(path, "BeaconCatalog"):
		push_error("Catalogue absent ou incompatible : %s." % path)
		return null

	var loaded: Resource = ResourceLoader.load(
		path,
		"BeaconCatalog",
		ResourceLoader.CACHE_MODE_REUSE
	)

	var catalog := loaded as BeaconCatalog
	if catalog == null:
		push_error("Le fichier n’est pas un BeaconCatalog : %s." % path)
		return null

	var report := catalog.validate()
	if report.has_errors():
		_print_data_issues(report)
		return null

	return catalog
```

### 17.1 Validation du chemin

`_is_allowed_catalog_path(path)` reçoit une chaîne et renvoie un booléen.

Elle exige :

- le préfixe `res://data/beacons/` ;
- l’extension `.tres` ou `.res`.

`begins_with(prefix)` teste le début. `get_extension()` renvoie l’extension sans point. `to_lower()` normalise la casse. `in` teste l’appartenance au tableau autorisé.

### 17.2 Existence, type et cache

`ResourceLoader.exists(path, type_hint)` vérifie le chemin avec un indice de type.

`ResourceLoader.load(path, type_hint, cache_mode)` reçoit :

1. le chemin ;
2. le type attendu sous forme de texte ;
3. le mode de cache.

Le mode `CACHE_MODE_REUSE` réutilise une Resource déjà mise en cache. Le retour général `Resource` est ensuite casté en `BeaconCatalog`.

La fonction renvoie uniquement un catalogue dont le chemin, le type et le contenu ont été validés.

## 18. Afficher les problèmes au point de composition

> **[VSC] Visual Studio Code — Ajouter à `src/app/app_bootstrap.gd`.**

```gdscript
func _print_data_issues(report: DataValidationReport) -> void:
	for issue: DataValidationIssue in report.issues:
		var rendered := "[%s] %s : %s" % [
			issue.code,
			issue.location,
			issue.message,
		]

		if issue.severity == DataValidationIssue.Severity.ERROR:
			push_error(rendered)
		else:
			push_warning(rendered)
```

Le paramètre `report` contient les diagnostics. La fonction ne renvoie rien.

Le catalogue reste indépendant de l’affichage : un autre consommateur pourrait produire une fenêtre, un rapport CI ou un fichier de diagnostic.

## 19. Comparer les modes de chargement

### 19.1 `preload()`

Utiliser `preload()` lorsque le chemin est constant, la dépendance obligatoire, la Resource raisonnablement petite et son chargement vérifiable pendant l’analyse du script.

> **[LECTURE] Dépendance connue à l’avance — Ne pas recopier sans évaluer le coût.**

```gdscript
const DEFAULT_PROFILE: BeaconProfile = preload(
	"res://data/beacons/default_beacon.tres"
)
```

`preload()` ne reçoit pas un chemin calculé au runtime.

### 19.2 `load()`

Utiliser `load()` lorsque le chemin est choisi à l’exécution et que le code peut gérer un échec. Le chargement reste synchrone et peut bloquer le thread appelant.

### 19.3 `ResourceLoader`

Utiliser directement `ResourceLoader` pour contrôler l’existence, le type, le cache ou un chargement en arrière-plan.

Ces API restent dans l’infrastructure et le point de composition, pas dans les règles métier.

## 20. Rôle et limites de JSON

JSON convient lorsque les données doivent être lisibles par Godot, Python, un outil de production ou une future API.

Il représente objets, tableaux, chaînes, booléens, nombres et `null`.

Il ne représente pas directement :

- `Vector3` ;
- `Color` ;
- `StringName` ;
- une classe `BeaconProfile` ;
- une référence de Resource ;
- des commentaires standard.

Après parsing, le code reçoit d’abord des `Variant`, `Dictionary` et `Array`. Il doit contrôler la forme et convertir vers des objets typés.

## 21. Créer les fichiers de configuration

> **[VSC] Visual Studio Code — Créer :** `config/defaults/runtime.json`.

```json
{
  "schema_version": 1,
  "environment": "development",
  "logging": {
    "level": "debug"
  },
  "ai_services": {
    "enabled": false,
    "base_url": "http://127.0.0.1:11434",
    "request_timeout_seconds": 10.0
  },
  "data": {
    "beacon_catalog": "res://data/beacons/beacon_catalog.tres"
  }
}
```

Signification :

- `schema_version` décrit la structure ;
- `environment` nomme le profil ;
- `logging.level` règle le journal ;
- `ai_services.enabled` conserve un chemin sans IA ;
- `base_url` est locale dans l’exemple ;
- `request_timeout_seconds` fixe un délai ;
- `data.beacon_catalog` centralise le chemin.

> **[VSC] Visual Studio Code — Créer :** `config/environments/studio.json`.

```json
{
  "schema_version": 1,
  "environment": "studio",
  "logging": {
    "level": "info"
  },
  "ai_services": {
    "enabled": true,
    "request_timeout_seconds": 20.0
  }
}
```

La configuration finale applique :

1. les valeurs par défaut ;
2. la surcharge d’environnement ;
3. plus tard, des réglages utilisateur autorisés ;
4. plus tard, des arguments de lancement autorisés.

Le chapitre 7 implémente uniquement les deux premières couches.

Aucun fichier versionné ne doit contenir mot de passe, clé privée, jeton, secret ou donnée personnelle.

## 22. Lire un objet JSON avec des erreurs détaillées

> **[VSC] Visual Studio Code — Créer :** `src/core/config/json_config_loader.gd`.

```gdscript
class_name JsonConfigLoader
extends RefCounted
## Lit, contrôle et fusionne des objets JSON.


func load_object(
	path: String,
	report: DataValidationReport
) -> Dictionary:
	if not FileAccess.file_exists(path):
		report.add_error(
			&"file_not_found",
			path,
			"Le fichier de configuration est absent."
		)
		return {}

	var file := FileAccess.open(path, FileAccess.READ)
	if file == null:
		report.add_error(
			&"file_open_failed",
			path,
			"Ouverture impossible : %s."
			% error_string(FileAccess.get_open_error())
		)
		return {}

	var source_text: String = file.get_as_text()
	var parser := JSON.new()
	var parse_error: Error = parser.parse(source_text)

	if parse_error != OK:
		report.add_error(
			&"json_parse_failed",
			"%s:%d" % [path, parser.get_error_line()],
			parser.get_error_message()
		)
		return {}

	if typeof(parser.data) != TYPE_DICTIONARY:
		report.add_error(
			&"invalid_root_type",
			path,
			"La racine JSON doit être un objet."
		)
		return {}

	return parser.data as Dictionary
```

Paramètres :

- `path` est un chemin Godot ;
- `report` accumule les erreurs sans les afficher lui-même.

Retour :

- dictionnaire racine lorsque la lecture réussit ;
- `{}` en cas d’échec, avec une erreur ajoutée.

Le consommateur doit toujours consulter `report.has_errors()`.

Détails :

- `file_exists(path)` distingue un fichier absent ;
- `FileAccess.open(path, FileAccess.READ)` ouvre en lecture seule ;
- `get_open_error()` fournit le code d’échec du dernier appel ;
- `error_string(code)` le convertit en texte ;
- `get_as_text()` lit la chaîne UTF-8 ;
- `JSON.new()` conserve les détails du parseur ;
- `parse(text)` renvoie un code `Error` ;
- `get_error_line()` et `get_error_message()` localisent l’échec ;
- `typeof(parser.data)` vérifie le type de la racine.

`JSON.parse_string()` est plus court, mais ne fournit pas ces informations détaillées lorsqu’il échoue.

## 23. Ajouter des lecteurs de valeurs stricts

> **[VSC] Visual Studio Code — Ajouter à `src/core/config/json_config_loader.gd`.**

```gdscript
func read_integer(
	source: Dictionary,
	key: String,
	location: String,
	report: DataValidationReport
) -> int:
	if not source.has(key):
		report.add_error(
			&"missing_key",
			location + "." + key,
			"Clé entière obligatoire absente."
		)
		return 0

	var value: Variant = source[key]
	if typeof(value) != TYPE_FLOAT and typeof(value) != TYPE_INT:
		report.add_error(
			&"invalid_integer_type",
			location + "." + key,
			"Un nombre entier est attendu."
		)
		return 0

	var numeric_value := float(value)
	if not is_equal_approx(numeric_value, round(numeric_value)):
		report.add_error(
			&"non_integral_number",
			location + "." + key,
			"Le nombre doit être sans partie décimale."
		)
		return 0

	return int(numeric_value)
```

Paramètres :

- `source` est l’objet courant ;
- `key` est la clé recherchée ;
- `location` est le chemin du parent ;
- `report` reçoit les erreurs.

Retour : entier validé, ou `0` accompagné d’une erreur.

JSON représente les nombres sans imposer la distinction métier entier/flottant. Le code accepte donc `TYPE_FLOAT` et `TYPE_INT`, puis contrôle l’absence de partie décimale.

`round()` calcule l’entier le plus proche. `is_equal_approx()` évite qu’une petite imprécision flottante déclenche une fausse erreur.

## 24. Fusionner les couches de configuration

> **[VSC] Visual Studio Code — Ajouter à `src/core/config/json_config_loader.gd`.**

```gdscript
func merge_objects(
	base: Dictionary,
	override_values: Dictionary
) -> Dictionary:
	var result: Dictionary = base.duplicate(true)

	for key: Variant in override_values:
		var override_value: Variant = override_values[key]

		if (
			result.has(key)
			and typeof(result[key]) == TYPE_DICTIONARY
			and typeof(override_value) == TYPE_DICTIONARY
		):
			result[key] = merge_objects(
				result[key] as Dictionary,
				override_value as Dictionary
			)
		else:
			result[key] = override_value

	return result
```

Paramètres et retour :

- `base` est le dictionnaire de départ ;
- `override_values` contient les valeurs prioritaires ;
- le retour est un nouveau dictionnaire ;
- `base.duplicate(true)` évite de modifier directement la base.

La fonction est récursive lorsque les deux valeurs sont des dictionnaires. Les tableaux et valeurs scalaires sont remplacés entièrement.

Cette politique doit être identique dans les futurs outils Python. Elle ne supprime pas une clé lorsque la surcharge contient `null`.

## 25. Représenter la configuration runtime

> **[VSC] Visual Studio Code — Créer :** `src/core/config/runtime_configuration.gd`.

```gdscript
class_name RuntimeConfiguration
extends RefCounted
## Configuration validée et injectée au runtime.

const CURRENT_SCHEMA_VERSION: int = 1
const ALLOWED_LOG_LEVELS: Array[StringName] = [
	&"debug",
	&"info",
	&"warning",
	&"error",
]

var schema_version: int = CURRENT_SCHEMA_VERSION
var environment: StringName = &"development"
var log_level: StringName = &"info"
var ai_services_enabled: bool = false
var ai_base_url: String = "http://127.0.0.1:11434"
var ai_request_timeout_seconds: float = 10.0
var beacon_catalog_path: String = \
	"res://data/beacons/beacon_catalog.tres"


func apply(
	data: Dictionary,
	report: DataValidationReport
) -> void:
	_read_schema(data, report)
	_read_environment(data, report)
	_read_logging(data, report)
	_read_ai_services(data, report)
	_read_data_paths(data, report)
```

La classe n’est pas une Resource : elle représente le résultat validé du chargement. Elle n’est ni éditée dans l’Inspector ni enregistrée dans un `.tres`.

`apply(data, report)` reçoit le dictionnaire fusionné et le rapport. Elle appelle cinq fonctions, toutes définies dans les sections suivantes.

## 26. Lire la version et l’environnement

> **[VSC] Visual Studio Code — Ajouter à `src/core/config/runtime_configuration.gd`.**

```gdscript
func _read_schema(
	data: Dictionary,
	report: DataValidationReport
) -> void:
	var raw_version: Variant = data.get("schema_version")

	if typeof(raw_version) != TYPE_FLOAT \
	and typeof(raw_version) != TYPE_INT:
		report.add_error(
			&"invalid_schema_type",
			"schema_version",
			"La version de schéma doit être numérique."
		)
		return

	var numeric_version := float(raw_version)
	if not is_equal_approx(numeric_version, round(numeric_version)):
		report.add_error(
			&"non_integral_schema",
			"schema_version",
			"La version doit être entière."
		)
		return

	schema_version = int(numeric_version)
	if schema_version != CURRENT_SCHEMA_VERSION:
		report.add_error(
			&"unsupported_schema",
			"schema_version",
			"Version non prise en charge : %d."
			% schema_version
		)


func _read_environment(
	data: Dictionary,
	report: DataValidationReport
) -> void:
	var raw_environment: Variant = data.get("environment")

	if typeof(raw_environment) != TYPE_STRING:
		report.add_error(
			&"invalid_environment",
			"environment",
			"L’environnement doit être une chaîne."
		)
		return

	var normalized := String(raw_environment).strip_edges()
	if normalized.is_empty():
		report.add_error(
			&"empty_environment",
			"environment",
			"L’environnement est vide."
		)
		return

	environment = StringName(normalized)
```

`Dictionary.get(key)` renvoie la valeur ou `null` lorsque la clé manque. Une clé absente échoue donc au contrôle de type.

La version est vérifiée comme nombre mathématiquement entier. L’environnement est converti en `String`, nettoyé avec `strip_edges()`, puis converti en `StringName`.

## 27. Lire la journalisation

> **[VSC] Visual Studio Code — Ajouter à `src/core/config/runtime_configuration.gd`.**

```gdscript
func _read_logging(
	data: Dictionary,
	report: DataValidationReport
) -> void:
	var section: Variant = data.get("logging")
	if typeof(section) != TYPE_DICTIONARY:
		report.add_error(
			&"invalid_logging_section",
			"logging",
			"La section logging doit être un objet."
		)
		return

	var raw_level: Variant = (section as Dictionary).get("level")
	if typeof(raw_level) != TYPE_STRING:
		report.add_error(
			&"invalid_log_level",
			"logging.level",
			"Le niveau doit être une chaîne."
		)
		return

	var candidate := StringName(
		String(raw_level).strip_edges().to_lower()
	)

	if candidate not in ALLOWED_LOG_LEVELS:
		report.add_error(
			&"unsupported_log_level",
			"logging.level",
			"Niveau inconnu : %s." % candidate
		)
		return

	log_level = candidate
```

La section intermédiaire est contrôlée avant le cast en `Dictionary`.

`candidate not in ALLOWED_LOG_LEVELS` teste que la valeur normalisée appartient à la liste fermée. Une faute de frappe ne devient donc pas un niveau silencieusement accepté.

## 28. Lire la configuration des services IA

> **[VSC] Visual Studio Code — Ajouter à `src/core/config/runtime_configuration.gd`.**

```gdscript
func _read_ai_services(
	data: Dictionary,
	report: DataValidationReport
) -> void:
	var section: Variant = data.get("ai_services")
	if typeof(section) != TYPE_DICTIONARY:
		report.add_error(
			&"invalid_ai_section",
			"ai_services",
			"La section ai_services doit être un objet."
		)
		return

	var values := section as Dictionary
	var raw_enabled: Variant = values.get("enabled")
	var raw_url: Variant = values.get("base_url")
	var raw_timeout: Variant = values.get(
		"request_timeout_seconds"
	)

	if typeof(raw_enabled) != TYPE_BOOL:
		report.add_error(
			&"invalid_ai_enabled",
			"ai_services.enabled",
			"La valeur enabled doit être booléenne."
		)
	else:
		ai_services_enabled = bool(raw_enabled)

	if typeof(raw_url) != TYPE_STRING:
		report.add_error(
			&"invalid_ai_url",
			"ai_services.base_url",
			"L’URL doit être une chaîne."
		)
	else:
		var candidate_url := String(raw_url).strip_edges()
		if not candidate_url.begins_with("http://127.0.0.1") \
		and not candidate_url.begins_with("http://localhost"):
			report.add_error(
				&"non_local_ai_url",
				"ai_services.base_url",
				"Le profil local doit utiliser localhost."
			)
		else:
			ai_base_url = candidate_url.trim_suffix("/")

	if typeof(raw_timeout) != TYPE_FLOAT \
	and typeof(raw_timeout) != TYPE_INT:
		report.add_error(
			&"invalid_ai_timeout",
			"ai_services.request_timeout_seconds",
			"Le délai doit être numérique."
		)
		return

	var timeout := float(raw_timeout)
	if timeout <= 0.0 or timeout > 120.0:
		report.add_error(
			&"ai_timeout_out_of_range",
			"ai_services.request_timeout_seconds",
			"Le délai doit être dans ]0, 120] secondes."
		)
		return

	ai_request_timeout_seconds = timeout
```

Paramètres :

- `data` est l’objet racine ;
- `report` reçoit toutes les erreurs ;
- la fonction ne renvoie aucune valeur.

Valeurs lues :

- `enabled` doit être un booléen ;
- `base_url` doit être une chaîne locale dans ce profil ;
- `request_timeout_seconds` doit être numérique et compris dans l’intervalle autorisé.

`trim_suffix("/")` retire un slash terminal afin de produire des URLs de requête cohérentes plus tard.

Cette validation locale ne remplace pas la politique de sécurité complète du chapitre 13.

## 29. Lire le chemin du catalogue

> **[VSC] Visual Studio Code — Ajouter à `src/core/config/runtime_configuration.gd`.**

```gdscript
func _read_data_paths(
	data: Dictionary,
	report: DataValidationReport
) -> void:
	var section: Variant = data.get("data")
	if typeof(section) != TYPE_DICTIONARY:
		report.add_error(
			&"invalid_data_section",
			"data",
			"La section data doit être un objet."
		)
		return

	var raw_path: Variant = (
		section as Dictionary
	).get("beacon_catalog")

	if typeof(raw_path) != TYPE_STRING:
		report.add_error(
			&"invalid_catalog_path",
			"data.beacon_catalog",
			"Le chemin doit être une chaîne."
		)
		return

	var candidate := String(raw_path).strip_edges()
	if not candidate.begins_with("res://data/beacons/"):
		report.add_error(
			&"catalog_path_outside_scope",
			"data.beacon_catalog",
			"Le catalogue doit rester sous res://data/beacons/."
		)
		return

	if candidate.get_extension().to_lower() \
	not in ["tres", "res"]:
		report.add_error(
			&"invalid_catalog_extension",
			"data.beacon_catalog",
			"Extension attendue : .tres ou .res."
		)
		return

	beacon_catalog_path = candidate
```

La fonction reçoit le même couple `data` et `report` que les autres lecteurs.

Elle contrôle le type, le dossier autorisé et l’extension avant d’affecter `beacon_catalog_path`.

La validation est répétée par `_load_catalog_at()` au moment du chargement. Cette défense en profondeur empêche qu’un futur appel contourne l’objet de configuration.

## 30. Construire la configuration finale

> **[VSC] Visual Studio Code — Ajouter à `src/core/config/json_config_loader.gd`.**

```gdscript
func load_runtime_configuration(
	default_path: String,
	environment_path: String
) -> Dictionary:
	var report := DataValidationReport.new()
	var defaults := load_object(default_path, report)

	if report.has_errors():
		return {
			"configuration": null,
			"report": report,
		}

	var environment_values: Dictionary = {}
	if not environment_path.is_empty():
		environment_values = load_object(
			environment_path,
			report
		)

	if report.has_errors():
		return {
			"configuration": null,
			"report": report,
		}

	var merged := merge_objects(
		defaults,
		environment_values
	)

	var configuration := RuntimeConfiguration.new()
	configuration.apply(merged, report)

	return {
		"configuration": (
			configuration if report.is_valid() else null
		),
		"report": report,
	}
```

Paramètres :

- `default_path` est obligatoire ;
- `environment_path` peut être vide pour désigner l’absence de surcharge.

Retour : dictionnaire contenant deux clés stables :

- `configuration` : `RuntimeConfiguration` ou `null` ;
- `report` : `DataValidationReport` toujours présent.

Le chargeur s’arrête après une erreur de lecture. Une surcharge ne répare pas silencieusement un fichier de base corrompu.

L’expression conditionnelle renvoie la configuration uniquement lorsque le rapport ne contient aucune erreur.

## 31. Choisir explicitement l’environnement

> **[VSC] Visual Studio Code — Ajouter temporairement à `src/app/app_bootstrap.gd`.**

```gdscript
const DEFAULT_CONFIG_PATH := \
	"res://config/defaults/runtime.json"
const STUDIO_CONFIG_PATH := \
	"res://config/environments/studio.json"
const ACTIVE_ENVIRONMENT: StringName = &"development"


func _resolve_environment_path() -> String:
	match ACTIVE_ENVIRONMENT:
		&"development":
			return ""
		&"studio":
			return STUDIO_CONFIG_PATH
		_:
			push_error(
				"Environnement inconnu : %s."
				% ACTIVE_ENVIRONMENT
			)
			return ""
```

`match` compare la valeur aux cas déclarés. `_` capture tous les autres cas.

La chaîne vide signifie ici « aucune surcharge ». Cette convention reste locale à la fonction.

Le choix d’environnement n’est pas un secret. Les secrets ne doivent jamais être placés dans ces fichiers.

## 32. Assembler les services de données

> **[VSC] Visual Studio Code — Ajouter au démarrage de `src/app/app_bootstrap.gd`.**

```gdscript
func _build_data_services() -> bool:
	var loader := JsonConfigLoader.new()
	var result := loader.load_runtime_configuration(
		DEFAULT_CONFIG_PATH,
		_resolve_environment_path()
	)

	var report := result.get("report") as DataValidationReport
	if report == null:
		push_error("Rapport de configuration absent.")
		return false

	if report.has_errors():
		_print_data_issues(report)
		return false

	var configuration := result.get(
		"configuration"
	) as RuntimeConfiguration
	if configuration == null:
		push_error("Configuration runtime absente.")
		return false

	var catalog := _load_catalog_at(
		configuration.beacon_catalog_path
	)
	if catalog == null:
		return false

	var repository := \
		ResourceBeaconCatalogRepository.new(catalog)

	_service_registry.register(
		&"runtime_configuration",
		configuration
	)
	_service_registry.register(
		&"beacon_catalog_repository",
		repository
	)

	return true
```

Responsabilité :

1. charger et fusionner les JSON ;
2. examiner le rapport ;
3. obtenir la configuration typée ;
4. charger le catalogue validé ;
5. construire le repository ;
6. publier les dépendances au point de composition.

`result.get("report")` renvoie un `Variant`, puis `as DataValidationReport` réalise un cast sûr. Le contrôle `report == null` protège une évolution accidentelle du contrat.

Le registre reste limité au point de composition. Un service de gameplay reçoit le repository par constructeur ou `configure()` ; il ne cherche pas lui-même un service global.

## 33. `res://`, `user://` et chemins absolus

### 33.1 `res://`

`res://` désigne la racine des ressources du projet. Il convient aux scripts, scènes, Resources, configurations embarquées et données de conception.

Après export, il ne faut pas supposer que ce contenu est un dossier Windows librement modifiable.

### 33.2 `user://`

`user://` désigne le dossier de données de l’application pour l’utilisateur courant.

Il accueillera plus tard les réglages, sauvegardes, caches et journaux selon la politique du projet.

Le chapitre 7 n’écrit encore aucun fichier sous `user://`. Cette responsabilité appartient au chapitre 9.

### 33.3 Chemins absolus

Un chemin comme `C:\Asteria\data.json` ne doit pas être codé dans le gameplay. Il dépend de la machine, du compte, du disque et des permissions.

Les outils d’import du chapitre 26 pourront recevoir un chemin choisi par l’utilisateur. Le runtime livré doit conserver des chemins portables.

## 34. Inclure les JSON dans un export

> **[APP] Godot Editor — Ouvrir `Project > Export`, sélectionner le preset, puis vérifier les filtres de ressources.**

Pour les JSON lus directement au runtime, ajouter si nécessaire :

> **[APP] Godot Editor — Configurer le filtre des fichiers non-ressources avec la valeur suivante.**

```text
config/**/*.json
```

Ne pas ajouter `**/*.json` sans raison : cela pourrait embarquer un fichier de travail ou une donnée sensible.

À la campagne de fin de Livre, tester :

- l’inclusion du fichier ;
- sa lecture par `FileAccess` ;
- le chargement du catalogue ;
- l’absence de chemin propre au poste de développement.

## 35. `ConfigFile` comme alternative ciblée

> **[LECTURE] Exemple de format par sections — Ne pas créer dans ce chapitre.**

```ini
[logging]
level="info"

[ai_services]
enabled=false
request_timeout_seconds=10.0
```

`ConfigFile` convient à une petite configuration propre à Godot et conserve des valeurs `Variant`.

JSON reste retenu ici pour l’interopérabilité avec Python et les futurs services. Deux formats ne doivent pas représenter la même source de vérité sans justification.

## 36. Préparer un chargement en arrière-plan

Un petit catalogue chargé au démarrage peut rester synchrone. Un grand ensemble de scènes ou d’assets peut justifier un chargement différé.

> **[LECTURE] Démarrer une demande — Étudier le code d’erreur.**

```gdscript
var request_error := ResourceLoader.load_threaded_request(
	"res://data/large_catalog.tres",
	"Resource"
)

if request_error != OK:
	push_error(
		"Impossible de démarrer le chargement : %s."
		% error_string(request_error)
	)
```

`load_threaded_request(path, type_hint)` reçoit le chemin et l’indice de type. Il renvoie `OK` si la demande est acceptée.

> **[LECTURE] Interroger le statut sur plusieurs images — Ne pas placer dans une boucle bloquante.**

```gdscript
var progress: Array = []
var status := ResourceLoader.load_threaded_get_status(
	"res://data/large_catalog.tres",
	progress
)

match status:
	ResourceLoader.THREAD_LOAD_IN_PROGRESS:
		var ratio := float(progress[0])
		print("Progression : %.0f %%" % (ratio * 100.0))
	ResourceLoader.THREAD_LOAD_LOADED:
		var loaded := ResourceLoader.load_threaded_get(
			"res://data/large_catalog.tres"
		)
	ResourceLoader.THREAD_LOAD_FAILED:
		push_error("Chargement différé échoué.")
```

`progress` reçoit une progression entre `0.0` et `1.0`.

Le statut doit être interrogé dans `_process()` ou un mécanisme réparti sur plusieurs images. Une boucle `while` serrée bloquerait la boucle principale. `load_threaded_get()` peut également bloquer s’il est appelé avant l’état `THREAD_LOAD_LOADED`.

## 37. Politique de cache

Le cache normal évite de relire plusieurs fois la même Resource et permet de partager les définitions.

Risques :

- une mutation accidentelle devient globale ;
- un test peut observer une instance déjà modifiée ;
- forcer un rechargement sans politique crée des références incohérentes.

Règles de `Project Asteria` :

1. définitions canoniques en lecture seule ;
2. état runtime séparé ;
3. chemins centralisés ;
4. modes de cache confinés à l’infrastructure ;
5. aucun rechargement forcé dispersé dans le gameplay ;
6. tests futurs construisant des dépendances propres.

Les modes de cache avancés ne sont utilisés qu’après une revue spécifique de leurs effets sur les dépendances et sous-Resources.

## 38. Versionner les formats

Chaque racine durable possède un `schema_version`.

Cette version décrit la structure du document, pas la version commerciale du jeu.

> **[LECTURE] Exemple d’évolution — Ne pas saisir.**

```text
schéma 1  ai_services.request_timeout_seconds
schéma 2  ai_services.timeouts.request_seconds
```

Le lecteur doit choisir explicitement entre :

- accepter la version courante ;
- migrer une ancienne version ;
- refuser une version future inconnue.

Une migration de structure ne doit pas changer un identifiant métier sans table de correspondance. Le chapitre 8 appliquera cette discipline à la base et le chapitre 9 aux sauvegardes.

## 39. Sécurité des données

Un JSON syntaxiquement valide peut encore contenir une URL inattendue, un délai négatif, un tableau énorme, un chemin interdit ou un type incorrect.

Règles :

- vérifier les types ;
- borner les nombres et les tailles ;
- limiter les chemins autorisés ;
- vérifier l’extension et le type de Resource ;
- ne jamais désérialiser arbitrairement un objet provenant d’une source non fiable ;
- ne jamais versionner de secret ;
- conserver un fonctionnement déterministe lorsque les services IA sont désactivés.

## 40. Exercice intégré

> **[VSC] Visual Studio Code — Créer :** `scenes/learning/ch07_data_demo.gd`.

```gdscript
class_name Ch07DataDemo
extends Node
## Démonstration sans dépendance directe aux fichiers.

var _repository: BeaconCatalogRepository


func configure(
	repository: BeaconCatalogRepository
) -> void:
	assert(repository != null)
	_repository = repository


func run_demo(id: StringName) -> bool:
	if _repository == null:
		push_error("Ch07DataDemo n’est pas configuré.")
		return false

	var profile := _repository.get_by_id(id)
	if profile == null:
		push_warning("Balise inconnue : %s." % id)
		return false

	print(
		"Balise %s — %s — cooldown %.1f s"
		% [
			profile.id,
			profile.display_name,
			profile.cooldown_seconds,
		]
	)
	return true
```

`configure(repository)` reçoit la dépendance et ne renvoie rien. L’assertion protège une erreur d’assemblage.

`run_demo(id)` reçoit l’identifiant et renvoie :

- `true` si la définition est trouvée et affichée ;
- `false` si le composant n’est pas configuré ou si l’identifiant est absent.

Le script ne connaît ni chemin, ni JSON, ni `ResourceLoader`, ni registre global.

> **[APP] Godot Editor — Créer une scène avec une racine `Node` nommée `Ch07DataDemo`, attacher le script, puis enregistrer sous `scenes/learning/ch07_data_demo.tscn`.**

> **[LECTURE] Appel depuis le bootstrap — Adapter à l’assemblage existant.**

```gdscript
data_demo.run_demo(&"default_beacon")
```

> **[SORTIE] Exemple de sortie Godot — Ne pas saisir.**

```text
Balise default_beacon — Balise Asteria — cooldown 2.0 s
```

## 41. Vérifications manuelles prévues

### 41.1 Catalogue correct

- lancer la validation ;
- vérifier l’absence d’erreur ;
- demander `default_beacon` ;
- contrôler le nom et le cooldown.

### 41.2 Identifiant dupliqué

- dupliquer temporairement un identifiant ;
- vérifier `duplicate_id` ;
- restaurer la valeur correcte.

### 41.3 JSON mal formé

- sur une branche de test, retirer une virgule ;
- vérifier le numéro de ligne et le message ;
- restaurer le fichier.

### 41.4 Type incorrect

- remplacer temporairement le délai par une chaîne ;
- vérifier le refus de la configuration ;
- restaurer le nombre.

### 41.5 Chemin interdit

- remplacer le catalogue par un chemin hors de `res://data/beacons/` ;
- vérifier le diagnostic ;
- restaurer le chemin.

### 41.6 Export de fin de Livre

- vérifier l’inclusion des JSON ;
- confirmer les chemins `res://` ;
- confirmer qu’aucun chemin absolu local n’est présent ;
- conserver ces contrôles comme réserves tant qu’ils ne sont pas exécutés.

## 42. Erreurs fréquentes et corrections

### 42.1 Modifier une Resource partagée

**Symptôme :** plusieurs instances changent ensemble.  
**Cause :** la définition mise en cache sert d’état runtime.  
**Correction :** déplacer les valeurs changeantes dans un objet d’état.

### 42.2 Utiliser le nom visible comme clé

**Symptôme :** une traduction casse une recherche.  
**Cause :** identité et présentation sont confondues.  
**Correction :** conserver un `StringName` stable.

### 42.3 Accepter un JSON uniquement parce qu’il se parse

**Symptôme :** une clé absente échoue beaucoup plus loin.  
**Cause :** aucune validation de structure ou de type.  
**Correction :** valider chaque section avant de construire l’objet typé.

### 42.4 Utiliser `parse_string()` sans diagnostic

**Symptôme :** seul un résultat `null` est disponible.  
**Cause :** méthode courte utilisée sur un chemin de production.  
**Correction :** utiliser une instance `JSON` et ses détails d’erreur.

### 42.5 Charger depuis chaque service

**Symptôme :** chemins dupliqués et tests difficiles.  
**Cause :** infrastructure dispersée.  
**Correction :** charger au point de composition et injecter un repository.

### 42.6 Utiliser l’index comme identité

**Symptôme :** réordonner le catalogue change le sens des références.  
**Cause :** position éditoriale et identité sont confondues.  
**Correction :** rechercher par identifiant stable.

### 42.7 Écrire une sauvegarde dans `res://`

**Symptôme :** l’écriture échoue après export.  
**Cause :** ressources embarquées traitées comme dossier utilisateur.  
**Correction :** attendre le chapitre 9 et utiliser `user://`.

### 42.8 Embarquer un secret

**Symptôme :** une clé apparaît dans Git ou dans le paquet.  
**Cause :** configuration et secret sont confondus.  
**Correction :** retirer et révoquer le secret, puis utiliser un mécanisme externe.

### 42.9 Bloquer en attendant un chargement différé

**Symptôme :** le jeu se fige.  
**Cause :** boucle serrée sur le statut.  
**Correction :** interroger le statut sur plusieurs images.

### 42.10 Multiplier les formats

**Symptôme :** la même option existe en `.tres`, JSON et `.cfg`.  
**Cause :** aucune source de vérité.  
**Correction :** attribuer une responsabilité unique à chaque format.

## 43. Parcours Solo et Studio

### 43.1 Mode Solo

Le parcours Solo peut conserver :

- un catalogue `.tres` ;
- un JSON par défaut ;
- une surcharge de développement ;
- un repository Resource ;
- une validation au démarrage ;
- une revue Git simple.

### 43.2 Mode Studio

Le parcours Studio ajoute :

- un propriétaire pour chaque schéma ;
- une revue des identifiants ;
- une validation automatisée des catalogues ;
- des règles de compatibilité ;
- des fichiers d’environnement approuvés ;
- des bornes de taille et de plage ;
- des tests d’export ;
- une politique de dépréciation ;
- une séparation formelle des secrets.

### 43.3 Contrat commun des deux parcours

Les deux parcours conservent une source de vérité, des identifiants stables, une validation avant usage, des objets typés après parsing, un repository injecté et l’absence de mutation des définitions canoniques.

## 44. Créer le contrat documentaire

> **[VSC] Visual Studio Code — Créer :** `docs/architecture/data-contract.md`.

Le document doit contenir :

- les quatre familles de données ;
- le propriétaire de chaque format ;
- les dossiers autorisés ;
- la convention d’identifiants ;
- les versions de schéma ;
- l’ordre des couches ;
- la politique de fusion ;
- les plages autorisées ;
- les erreurs bloquantes ;
- les données sensibles interdites ;
- les frontières SQLite et sauvegarde ;
- la stratégie de dépréciation.

> **[VSC] Visual Studio Code — Ajouter dans `docs/architecture/data-contract.md`.**

```markdown
| Source | Propriétaire | Mutée au runtime | Versionnée Git |
|---|---|---:|---:|
| `data/**/*.tres` | conception | non | oui |
| `config/defaults/*.json` | architecture | non | oui |
| configuration typée en mémoire | bootstrap | avant injection | non |
| état de session | fonctionnalité | oui | non |
| `user://` | chapitre 9 | oui | non |
```

## 45. Livrables guidés

- `src/core/data/data_validation_issue.gd` ;
- `src/core/data/data_validation_report.gd` ;
- `src/core/config/json_config_loader.gd` ;
- `src/core/config/runtime_configuration.gd` ;
- `src/features/beacons/data/beacon_catalog.gd` ;
- `src/features/beacons/data/beacon_catalog_validator.gd` ;
- `src/features/beacons/application/beacon_catalog_repository.gd` ;
- `src/features/beacons/infrastructure/resource_beacon_catalog_repository.gd` ;
- `data/beacons/beacon_catalog.tres` ;
- `config/defaults/runtime.json` ;
- `config/environments/studio.json` ;
- `scenes/learning/ch07_data_demo.gd` ;
- `scenes/learning/ch07_data_demo.tscn` ;
- `docs/architecture/data-contract.md`.

Ces fichiers sont des livrables guidés du projet fil rouge. Le Starter Kit du Companion Pack n’est pas encore matérialisé dans le dépôt documentaire.

## 46. Checklist de revue

### 46.1 Modèle et identité

- [ ] Définitions et état runtime sont séparés.
- [ ] Chaque définition possède un identifiant stable.
- [ ] Le nom affiché n’est pas utilisé comme clé.
- [ ] Le catalogue possède une version de schéma.
- [ ] Les entrées `null`, identifiants invalides et doublons sont détectés.

### 46.2 Resources et chargement

- [ ] Les définitions canoniques ne sont pas modifiées.
- [ ] Le partage par cache est compris.
- [ ] `resource_local_to_scene` répond à un besoin local réel.
- [ ] Le chemin et le type sont vérifiés.
- [ ] Le repository est injecté.

### 46.3 JSON et configuration

- [ ] Les erreurs d’ouverture et de parsing sont localisées.
- [ ] La racine est un dictionnaire.
- [ ] Les sections imbriquées sont contrôlées.
- [ ] Les types et bornes sont validés.
- [ ] La version de schéma est contrôlée.
- [ ] La fusion est documentée.
- [ ] La configuration brute devient un objet typé.

### 46.4 Architecture et sécurité

- [ ] Le domaine ne dépend pas de `FileAccess`.
- [ ] Le gameplay ne dépend pas de `ResourceLoader`.
- [ ] Le registre reste limité au point de composition.
- [ ] Aucun secret n’est embarqué.
- [ ] SQLite et sauvegarde restent hors périmètre.

### 46.5 Validation et publication

- [ ] Le contrôle automatique léger est vert.
- [ ] Aucun doublon documentaire n’est détecté.
- [ ] Les réserves runtime sont déclarées.
- [ ] Aucun PDF intermédiaire n’est produit.

## 47. Résumé

> **[LECTURE] Synthèse de l’architecture — Ne pas saisir.**

```text
définition versionnée
    ↓
chargement centralisé
    ↓
validation structurée
    ↓
configuration ou catalogue typé
    ↓
repository injecté
    ↓
service de gameplay
```

Principes à retenir :

1. une définition n’est pas un état runtime ;
2. un nom visible n’est pas un identifiant ;
3. une Resource peut être partagée par le cache ;
4. une définition canonique reste en lecture seule par convention ;
5. un JSON valide syntaxiquement peut être invalide pour le jeu ;
6. le parseur doit produire des erreurs localisables ;
7. la configuration brute devient un objet typé ;
8. les couches suivent un ordre documenté ;
9. chemins et chargeurs restent dans l’infrastructure ;
10. le repository prépare le remplacement par SQLite ;
11. les secrets ne sont jamais versionnés ;
12. sauvegardes et migrations complètes restent aux chapitres suivants.

## 48. Passage au chapitre suivant

Le chapitre 8 introduira :

- SQLite ;
- schéma relationnel ;
- migrations ;
- transactions ;
- index ;
- repositories persistants ;
- séparation lecture/écriture ;
- import contrôlé depuis les données de conception.

Avant de continuer, le projet doit pouvoir charger une configuration validée et exposer le catalogue de balises par un repository sans modifier les Resources canoniques.

## 49. Sources officielles de vérification

- [Documentation Godot — Resources](https://docs.godotengine.org/en/4.7/tutorials/scripting/resources.html)
- [Référence Godot — Resource](https://docs.godotengine.org/en/4.7/classes/class_resource.html)
- [Référence Godot — ResourceLoader](https://docs.godotengine.org/en/4.7/classes/class_resourceloader.html)
- [Référence Godot — JSON](https://docs.godotengine.org/en/4.7/classes/class_json.html)
- [Référence Godot — FileAccess](https://docs.godotengine.org/en/4.7/classes/class_fileaccess.html)
- [Référence Godot — ConfigFile](https://docs.godotengine.org/en/4.7/classes/class_configfile.html)
- [Documentation Godot — Exporter les projets](https://docs.godotengine.org/en/4.7/tutorials/export/exporting_projects.html)
