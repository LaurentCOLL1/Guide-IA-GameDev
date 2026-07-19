---
title: "Livre II — Chapitre 7 : Données avec Resources, JSON et configurations"
id: "DOC-L2-CH07"
status: "reviewed"
version: "1.0.0"
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
> **Niveau de raisonnement conseillé pour produire ou réviser ce chapitre :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-07.md`.

## 1. Rôle du chapitre

Les six premiers chapitres ont construit le projet, le langage, les scènes, l’architecture, les services et les interactions. Le projet doit maintenant organiser ses données sans les confondre avec les objets qui vivent dans le `SceneTree`.

Une architecture de données improvisée produit souvent :

- des valeurs de gameplay recopiées dans plusieurs scripts ;
- des `Dictionary` dont les clés ne sont vérifiées nulle part ;
- des Resources partagées modifiées accidentellement au runtime ;
- des identifiants qui changent avec le nom affiché ;
- un JSON accepté même lorsque sa structure est incohérente ;
- des fichiers de configuration mélangés aux sauvegardes du joueur ;
- des chemins de fichiers dispersés dans le code ;
- une dépendance directe à `ResourceLoader` ou `FileAccess` dans chaque fonctionnalité ;
- des erreurs silencieuses difficiles à diagnostiquer après export ;
- une migration vers SQLite ou les sauvegardes devenue coûteuse.

À la fin du chapitre, le lecteur doit savoir :

- distinguer données de conception, configuration, état runtime et données persistantes ;
- choisir entre `Resource`, JSON, `ConfigFile`, mémoire et future base SQLite ;
- créer un catalogue typé de Resources ;
- utiliser un identifiant stable indépendant du texte affiché ;
- valider un catalogue avant de l’injecter dans le jeu ;
- charger une Resource de manière synchrone et vérifier son type ;
- comprendre le cache de Resources ;
- éviter de modifier une Resource canonique partagée ;
- lire un JSON avec des messages d’erreur exploitables ;
- valider la forme et les types d’un document JSON ;
- fusionner des configurations par environnement ;
- séparer les valeurs par défaut embarquées de l’état utilisateur ;
- préparer un repository remplaçable au chapitre 8 ;
- différer le chargement lourd sans bloquer la boucle principale ;
- conserver des frontières claires avec SQLite et les sauvegardes.

## 2. Prérequis

Le lecteur doit connaître :

- les types, fonctions, collections et classes du chapitre 2 ;
- les Resources personnalisées et les signaux du chapitre 3 ;
- l’organisation feature-first du chapitre 4 ;
- l’injection de dépendances et le point de composition du chapitre 5 ;
- le remappage en mémoire introduit au chapitre 6.

Le chapitre réutilise :

- `BeaconProfile` ;
- `StatusBeacon` ;
- `AppBootstrap` ;
- le principe du repository ;
- le dossier `data/beacons` ;
- les conventions d’identifiants et de chemins du projet.

Le chapitre 3 expliquait comment créer une première Resource. Le présent chapitre ne répète pas cette initiation : il traite l’organisation d’un ensemble de données, sa validation, son chargement et ses frontières.

## 3. Périmètre et frontières

Ce chapitre définit :

- une taxonomie des données ;
- un catalogue `BeaconCatalog` ;
- des objets de rapport de validation ;
- un repository de catalogue injecté ;
- un chargeur JSON explicite ;
- une configuration runtime typée ;
- des fichiers de configuration par environnement ;
- des règles de priorité entre couches de configuration ;
- une politique de cache et d’immuabilité ;
- un exemple de chargement différé ;
- un contrat documentaire de données.

Il ne définit pas encore :

- une base SQLite, ses migrations ou ses transactions, réservées au chapitre 8 ;
- l’écriture d’une sauvegarde de partie, réservée au chapitre 9 ;
- la compatibilité complète des anciennes sauvegardes, réservée au chapitre 9 ;
- la mémoire vectorielle, réservée au chapitre 10 ;
- les appels HTTP vers les services IA, réservés aux chapitres 11 et 12 ;
- l’inventaire complet, réservé au chapitre 20 ;
- les outils d’édition avancés, réservés au chapitre 26 ;
- les tests automatisés complets, réservés au chapitre 27.

> **Frontière essentielle :** une définition de gameplay décrit ce qu’une chose est. Un état runtime décrit ce qui lui arrive pendant une session. Une sauvegarde décrit ce qui doit survivre à la fermeture du jeu.

## 4. Les quatre familles de données

### 4.1 Données de conception

Les données de conception sont créées par l’équipe et livrées avec le jeu.

Exemples :

- profil d’une balise ;
- définition d’un objet ;
- paramètres d’une compétence ;
- table de coûts ;
- courbe de progression ;
- catalogue de quêtes.

Elles sont généralement :

- versionnées dans Git ;
- placées sous `res://` ;
- modifiées dans Godot ou un outil de production ;
- considérées comme canoniques ;
- lues par le runtime sans être modifiées.

Dans ce chapitre, `BeaconProfile` et `BeaconCatalog` sont des données de conception.

### 4.2 Configuration d’exécution

Une configuration d’exécution choisit comment le programme se comporte dans un environnement donné.

Exemples :

- activer ou désactiver les services IA ;
- choisir une URL locale ;
- définir un délai maximal ;
- sélectionner un niveau de journalisation ;
- choisir un catalogue de démonstration.

Elle ne représente ni une règle de gameplay permanente ni la progression du joueur.

### 4.3 État runtime

L’état runtime change pendant la session.

Exemples :

- balise actuellement disponible ;
- temps restant avant la fin d’un cooldown ;
- cible regardée par le joueur ;
- requête IA en attente ;
- menu ouvert ou fermé.

Cet état appartient à des nœuds, des objets `RefCounted` ou des structures dédiées. Il ne doit pas être écrit dans la Resource canonique qui décrit la balise.

### 4.4 Données persistantes du joueur

Les données persistantes survivent à la fermeture du jeu.

Exemples :

- progression ;
- inventaire ;
- position sauvegardée ;
- réglages remappés ;
- historique de quêtes.

Le chapitre 7 prépare les formats et les responsabilités, mais n’implémente pas encore leur écriture. Le chapitre 9 prendra en charge la sauvegarde, le chargement et la migration.

## 5. Matrice de choix du format

| Besoin | Format principal | Pourquoi |
|---|---|---|
| données de conception typées et éditables dans Godot | `Resource` `.tres` | Inspector, types, références, sérialisation native |
| configuration lisible par d’autres outils | JSON | format textuel interopérable |
| petite configuration Godot de type sections/clés | `ConfigFile` | types `Variant`, API simple |
| état temporaire de session | objet runtime | aucune écriture inutile |
| données relationnelles persistantes | SQLite au chapitre 8 | requêtes, index, migrations |
| sauvegarde de partie | format versionné au chapitre 9 | compatibilité et contrôle du cycle de vie |

Aucun format n’est « meilleur » dans l’absolu. Le bon choix dépend :

- de qui produit les données ;
- de qui les lit ;
- du besoin de typage ;
- de la fréquence de modification ;
- de la taille ;
- du besoin de requêtes ;
- du besoin d’interopérabilité ;
- du niveau de confiance accordé à la source.

## 6. Architecture de données retenue

La chaîne de `Project Asteria` est la suivante :

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

Les dépendances suivent ces règles :

- le domaine ne connaît pas `FileAccess` ;
- les services de gameplay ne construisent pas eux-mêmes les chargeurs ;
- les chemins sont centralisés dans le point de composition ou une configuration ;
- les fichiers sont validés avant exposition ;
- une erreur de données devient un rapport explicite ;
- la Resource canonique reste une définition partagée et en lecture seule par convention.

## 7. Arborescence du chapitre

Depuis la racine de `Project Asteria`, créer les dossiers absents.

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

- `$paths` est un tableau PowerShell contenant les dossiers ;
- `@(...)` construit ce tableau sur plusieurs lignes ;
- l’opérateur `|` transmet chaque élément à la commande suivante ;
- `ForEach-Object` exécute le bloc pour chaque chemin ;
- `$_` représente l’élément courant ;
- `New-Item` crée le dossier ;
- `-Force` accepte un dossier déjà présent ;
- `Out-Null` masque la sortie répétitive sans masquer une erreur.

Arborescence attendue :

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

### 8.1 Identifiant contre nom affiché

Un identifiant stable sert aux relations techniques.

Un nom affiché sert au joueur et peut être traduit ou reformulé.

> **[LECTURE] Comparaison conceptuelle — Ne pas saisir.**

```text
id technique       default_beacon
nom français       Balise Asteria
nom anglais        Asteria Beacon
```

Modifier le nom visible ne doit pas casser :

- une référence de catalogue ;
- une sauvegarde future ;
- une table SQLite ;
- un événement ;
- un test ;
- une traduction.

### 8.2 Convention retenue

Pour les définitions de gameplay :

- type `StringName` dans les Resources ;
- minuscules ASCII ;
- mots séparés par `_` ;
- aucune espace ;
- aucune traduction ;
- aucune donnée de version dans l’identifiant ;
- unicité dans le catalogue concerné.

Exemples valides :

- `default_beacon` ;
- `ancient_gate_beacon` ;
- `tutorial_signal_01`.

Exemples à éviter :

- `Balise Asteria` ;
- `Beacon-v2-final` ;
- `objet_énergie` ;
- `New Beacon`.

### 8.3 Validation minimale

Un identifiant est invalide lorsqu’il est vide, dupliqué ou incompatible avec la convention du projet.

Le catalogue effectuera ce contrôle avant de devenir disponible au reste du jeu.

## 9. Comprendre le partage des Resources

### 9.1 Le cache de chargement

Lorsque Godot charge plusieurs fois le même chemin de Resource, le mode de cache normal réutilise l’instance déjà chargée.

> **[LECTURE] Exemple de partage — Ne pas modifier les objets dans cet extrait.**

```gdscript
var first: BeaconProfile = load(
	"res://data/beacons/default_beacon.tres"
) as BeaconProfile

var second: BeaconProfile = load(
	"res://data/beacons/default_beacon.tres"
) as BeaconProfile

print(first == second)
```

La comparaison affiche normalement `true`, car `first` et `second` référencent la même Resource mise en cache.

Conséquence : cette instruction est dangereuse sur une définition canonique.

> **[LECTURE] Contre-exemple — Ne pas recopier.**

```gdscript
first.cooldown_seconds = 999.0
```

Tous les consommateurs qui partagent cette instance peuvent observer la nouvelle valeur.

### 9.2 Règle d’immuabilité par convention

GDScript ne transforme pas automatiquement une Resource en objet immuable. Le projet adopte donc une règle :

> **Une Resource de définition chargée depuis `res://data` n’est jamais modifiée par le gameplay.**

Pour changer une donnée de conception :

- modifier le `.tres` dans Godot ;
- faire relire la modification ;
- la versionner dans Git ;
- reconstruire les catalogues si nécessaire.

Pour stocker un changement runtime :

- utiliser un objet d’état séparé ;
- référencer l’identifiant de la définition ;
- ne pas modifier la définition.

### 9.3 `duplicate()` ne remplace pas un modèle d’état

Une copie peut être utile pour un outil ou un cas local, mais elle ne doit pas devenir la réponse automatique.

> **[LECTURE] Copie explicite — Étudier les limites.**

```gdscript
var runtime_copy: BeaconProfile = source_profile.duplicate(true) as BeaconProfile
```

Paramètres et résultat :

- `source_profile` est la Resource d’origine ;
- `duplicate(true)` demande une copie profonde des tableaux, dictionnaires et sous-ressources internes admissibles ;
- le booléen `true` est le paramètre `deep` ;
- le retour de `duplicate()` est typé `Resource` ;
- `as BeaconProfile` vérifie et précise le type attendu ;
- `runtime_copy` est une autre instance si le cast réussit.

Même avec `deep = true`, les Resources externes ne sont pas toutes dupliquées automatiquement. Une copie profonde peut aussi coûter de la mémoire. Un objet d’état dédié reste préférable pour les données qui changent souvent.

### 9.4 `resource_local_to_scene`

Lorsque `resource_local_to_scene` vaut `true`, Godot duplique la Resource pour chaque instance de scène qui l’utilise.

Cette propriété convient à une sous-Resource qui doit être unique par instance de scène. Elle ne doit pas être activée sur un catalogue global de définitions.

Points importants :

- la propriété doit être configurée avant l’instanciation ;
- la changer après coup ne modifie pas les copies déjà créées ;
- elle ne transforme pas une définition globale en sauvegarde ;
- elle augmente le nombre d’instances en mémoire.

## 10. Représenter une erreur de données

### 10.1 Créer `DataValidationIssue`

> **[VSC] Visual Studio Code — Créer :** `src/core/data/data_validation_issue.gd`.

```gdscript
class_name DataValidationIssue
extends RefCounted
## Décrit une non-conformité de données sans l’afficher directement.

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

### 10.2 Décomposition de la classe

`DataValidationIssue` hérite de `RefCounted` :

- elle n’a pas besoin d’être un nœud ;
- sa mémoire est libérée lorsqu’aucune référence ne la conserve ;
- elle transporte une information structurée ;
- elle ne dépend pas de l’interface ou du journal.

L’énumération `Severity` définit deux valeurs :

- `WARNING` signale une anomalie non bloquante ;
- `ERROR` signale une donnée qui empêche l’utilisation sûre du catalogue.

Les propriétés signifient :

- `severity` : gravité ;
- `code` : identifiant stable de l’erreur, par exemple `duplicate_id` ;
- `location` : chemin logique tel que `entries[2].id` ;
- `message` : explication lisible.

### 10.3 Paramètres du constructeur

La signature `_init(...) -> void` reçoit quatre paramètres :

- `p_severity` : valeur de l’énumération ;
- `p_code` : code technique ;
- `p_location` : endroit concerné ;
- `p_message` : description.

Le préfixe `p_` distingue les paramètres des propriétés de même sens.

La fonction ne renvoie aucune valeur. Elle affecte les arguments reçus aux propriétés de l’objet nouvellement créé.

## 11. Regrouper les erreurs dans un rapport

### 11.1 Créer `DataValidationReport`

> **[VSC] Visual Studio Code — Créer :** `src/core/data/data_validation_report.gd`.

```gdscript
class_name DataValidationReport
extends RefCounted
## Accumule les avertissements et erreurs d’une validation.

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

### 11.2 `issues`

`issues` est un `Array` typé :

- chaque élément doit être un `DataValidationIssue` ;
- le tableau commence vide ;
- l’ordre d’ajout est conservé ;
- avertissements et erreurs peuvent coexister.

### 11.3 `add_warning()` et `add_error()`

Les deux fonctions reçoivent :

- `code` : identifiant de la règle violée ;
- `location` : chemin de la valeur ;
- `message` : explication.

Elles construisent un objet avec `DataValidationIssue.new(...)`, puis l’ajoutent par `append()`.

Le premier argument de `new()` fixe la gravité. Les trois autres sont transmis sans modification au constructeur.

### 11.4 `has_errors()`

> **[LECTURE] Signature expliquée — Ne pas recopier isolément.**

```gdscript
func has_errors() -> bool:
```

- `has_errors` signifie « contient au moins une erreur » ;
- la fonction ne reçoit aucun paramètre ;
- `-> bool` garantit un retour booléen ;
- `true` est renvoyé dès la première erreur ;
- `false` est renvoyé après parcours complet si aucune erreur n’existe.

La boucle :

> **[LECTURE] Parcours typé — Étudier la syntaxe.**

```gdscript
for issue: DataValidationIssue in issues:
```

signifie :

- `for` démarre une itération ;
- `issue` reçoit l’élément courant ;
- `: DataValidationIssue` documente et contrôle le type ;
- `in issues` indique la collection parcourue.

### 11.5 `is_valid()`

`is_valid()` inverse le résultat de `has_errors()` avec l’opérateur `not`.

Un rapport peut donc être valide tout en contenant des avertissements.

## 12. Construire un catalogue de balises

### 12.1 Créer `BeaconCatalog`

> **[VSC] Visual Studio Code — Créer :** `src/features/beacons/data/beacon_catalog.gd`.

```gdscript
class_name BeaconCatalog
extends Resource
## Catalogue canonique des profils de balise livrés avec le jeu.

const CURRENT_SCHEMA_VERSION: int = 1

@export var schema_version: int = CURRENT_SCHEMA_VERSION
@export var entries: Array[BeaconProfile] = []


func validate() -> DataValidationReport:
	var report := DataValidationReport.new()
	var seen_ids: Dictionary = {}

	if schema_version != CURRENT_SCHEMA_VERSION:
		report.add_error(
			&"unsupported_schema",
			"schema_version",
			"Version de catalogue non prise en charge : %d." % schema_version
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

		if entry.id == StringName():
			report.add_error(
				&"empty_id",
				location + ".id",
				"L’identifiant de la balise est vide."
			)
			continue

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

### 12.2 Constante de schéma

`CURRENT_SCHEMA_VERSION` indique la version comprise par le code.

La propriété exportée `schema_version` est enregistrée dans le fichier `.tres`. Lorsqu’une structure de catalogue évoluera, le code pourra :

- refuser une version inconnue ;
- migrer explicitement une ancienne version ;
- conserver une erreur compréhensible.

Ce mécanisme prépare la discipline de migration sans implémenter les migrations SQLite du chapitre 8.

### 12.3 Tableau `entries`

`entries` est un `Array[BeaconProfile]` :

- l’Inspector accepte uniquement des Resources compatibles ;
- chaque élément est une définition de balise ;
- l’ordre peut servir à l’affichage éditorial ;
- l’identifiant, et non l’index, sert aux références durables.

Ne pas utiliser l’index `0`, `1` ou `2` comme identifiant métier. Réordonner le catalogue casserait les relations.

### 12.4 Fonction `validate()`

`validate()` ne reçoit aucun paramètre, car elle vérifie l’instance courante.

Elle renvoie toujours un `DataValidationReport`, même si aucune erreur n’est détectée.

Variables locales :

- `report` accumule les résultats ;
- `seen_ids` mémorise les identifiants déjà rencontrés ;
- `index` représente la position courante ;
- `entry` est la Resource courante ;
- `location` produit un chemin lisible dans le rapport.

### 12.5 `range(entries.size())`

`entries.size()` renvoie le nombre d’éléments.

`range(nombre)` produit les entiers de `0` inclus à `nombre` exclu.

Pour trois entrées, les valeurs sont `0`, `1`, puis `2`.

L’index est utilisé uniquement pour localiser une erreur. Les relations métier continuent d’utiliser `entry.id`.

### 12.6 Dictionnaire `seen_ids`

> **[LECTURE] Index temporaire de validation — Ne pas recopier isolément.**

```gdscript
if seen_ids.has(entry.id):
```

- `seen_ids` est un dictionnaire en mémoire ;
- `has(key)` renvoie `true` lorsque la clé existe ;
- `entry.id` est la clé recherchée ;
- une clé déjà présente signifie que deux définitions partagent le même identifiant.

Après validation d’un identifiant, cette ligne l’enregistre :

> **[LECTURE] Affectation par clé — Étudier la syntaxe.**

```gdscript
seen_ids[entry.id] = true
```

Les crochets sélectionnent la clé `entry.id`. La valeur `true` sert seulement de marqueur de présence.

### 12.7 `continue`

`continue` arrête l’itération courante et passe à la suivante.

Après une entrée `null` ou un identifiant vide, le code ne tente pas de lire les propriétés restantes de cette entrée.

### 12.8 `find_by_id(id)`

La fonction reçoit un paramètre `id` de type `StringName`.

Elle renvoie :

- la première `BeaconProfile` correspondante ;
- `null` si aucune correspondance n’existe.

Le retour nullable est volontaire. Le consommateur doit gérer l’absence de définition au lieu de supposer que le catalogue est complet pour toutes les requêtes.

## 13. Créer la Resource de catalogue

### 13.1 Créer les profils supplémentaires

> **[APP] Godot Editor — Dans le dock FileSystem, dupliquer `data/beacons/default_beacon.tres` deux fois, puis renommer les copies.**

Créer :

- `data/beacons/gate_beacon.tres` ;
- `data/beacons/archive_beacon.tres`.

Modifier leurs identifiants et textes dans l’Inspector.

### 13.2 Créer `beacon_catalog.tres`

> **[APP] Godot Editor — Dans `data/beacons`, choisir `Create New > Resource`, sélectionner `BeaconCatalog`, puis enregistrer sous `data/beacons/beacon_catalog.tres`.**

Configurer :

> **[APP] Godot Editor — Modifier `data/beacons/beacon_catalog.tres` dans l’Inspector.**

```text
Schema Version  1
Entries         3 éléments
  0             default_beacon.tres
  1             gate_beacon.tres
  2             archive_beacon.tres
```

Le catalogue est une Resource externe. Les profils référencés sont également des Resources externes.

Cette organisation évite de recopier les mêmes données dans plusieurs scènes.

## 14. Valider le catalogue dans l’éditeur

Créer un petit script d’outil permet d’obtenir un diagnostic avant de lancer le jeu.

> **[VSC] Visual Studio Code — Créer :** `src/features/beacons/data/beacon_catalog_validator.gd`.

```gdscript
@tool
class_name BeaconCatalogValidator
extends Node
## Valide un catalogue depuis l’éditeur ou le runtime de démonstration.

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

### 14.1 Annotation `@tool`

`@tool` autorise l’exécution du script dans l’éditeur.

Cette capacité impose de la prudence :

- le `SceneTree` de l’éditeur n’est pas celui du jeu ;
- une erreur peut polluer la console de l’éditeur ;
- aucun fichier de production ne doit être réécrit automatiquement sans action claire ;
- une propriété de déclenchement doit revenir à `false`.

### 14.2 Setter de `validate_now`

Le setter reçoit `value`, la nouvelle valeur demandée par l’Inspector.

Il remet immédiatement la propriété à `false`, puis appelle `run_validation()` uniquement lorsque `value` vaut `true`.

Ce bouton booléen est une solution simple de chapitre. Le chapitre 26 présentera de vrais outils d’édition.

### 14.3 Rendu des erreurs

La chaîne :

> **[LECTURE] Format de diagnostic — Étudier les trois éléments.**

```gdscript
var rendered := "[%s] %s — %s" % [
	issue.code,
	issue.location,
	issue.message,
]
```

contient trois marqueurs `%s` :

1. le premier reçoit `issue.code` ;
2. le second reçoit `issue.location` ;
3. le troisième reçoit `issue.message`.

L’opérateur `%` applique le tableau d’arguments à la chaîne de format.

Le résultat peut ressembler à :

> **[SORTIE] Exemple de diagnostic — Ne pas saisir.**

```text
[duplicate_id] entries[2].id — Identifiant dupliqué : default_beacon.
```

## 15. Définir le contrat du repository

### 15.1 Pourquoi un repository

Le service qui cherche une balise n’a pas besoin de savoir si les données viennent :

- d’une Resource ;
- d’un JSON ;
- de SQLite ;
- d’un outil de test ;
- d’un service distant futur.

Il dépend d’un contrat minimal.

### 15.2 Créer `BeaconCatalogRepository`

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

GDScript n’impose pas ici une interface formelle. La classe de base fournit donc :

- les signatures ;
- les types de paramètres et de retours ;
- une erreur explicite si une implémentation manque ;
- une valeur de repli compatible avec la signature.

`get_by_id(id)` reçoit l’identifiant recherché.

`get_all()` ne reçoit aucun paramètre et renvoie une nouvelle liste de références.

Le repository expose des définitions. Il ne doit pas modifier le catalogue.

## 16. Implémenter le repository Resource

> **[VSC] Visual Studio Code — Créer :** `src/features/beacons/infrastructure/resource_beacon_catalog_repository.gd`.

```gdscript
class_name ResourceBeaconCatalogRepository
extends BeaconCatalogRepository
## Implémentation en lecture seule fondée sur BeaconCatalog.

var _catalog: BeaconCatalog


func _init(catalog: BeaconCatalog) -> void:
	assert(catalog != null, "Le catalogue de balises est obligatoire.")
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

### 16.1 Constructeur

`_init(catalog)` reçoit la dépendance au moment de la création.

`assert(condition, message)` arrête l’exécution de débogage si la condition est fausse. Cette assertion protège une erreur de programmation dans le point de composition.

Elle ne remplace pas la validation du contenu. Un catalogue non nul peut encore contenir des entrées incorrectes.

### 16.2 Copie de la liste

`get_all()` crée un nouveau tableau, puis y ajoute les références valides.

Le consommateur peut réordonner ou vider son tableau local sans modifier `BeaconCatalog.entries`.

Les `BeaconProfile` restent partagées. La règle d’immuabilité continue donc de s’appliquer à leurs propriétés.

## 17. Charger une Resource en vérifiant son type

### 17.1 Fonction de chargement

> **[VSC] Visual Studio Code — Ajouter au point de composition `src/app/app_bootstrap.gd`.**

```gdscript
const BEACON_CATALOG_PATH := \
	"res://data/beacons/beacon_catalog.tres"


func _load_beacon_catalog() -> BeaconCatalog:
	if not ResourceLoader.exists(
		BEACON_CATALOG_PATH,
		"BeaconCatalog"
	):
		push_error(
			"Catalogue absent : %s" % BEACON_CATALOG_PATH
		)
		return null

	var loaded: Resource = ResourceLoader.load(
		BEACON_CATALOG_PATH,
		"BeaconCatalog"
	)

	var catalog := loaded as BeaconCatalog
	if catalog == null:
		push_error(
			"Le fichier n’est pas un BeaconCatalog : %s"
			% BEACON_CATALOG_PATH
		)
		return null

	var report := catalog.validate()
	if report.has_errors():
		_print_data_issues(report)
		return null

	return catalog
```

### 17.2 Constante de chemin

`BEACON_CATALOG_PATH` centralise le chemin.

Le préfixe `res://` désigne la racine du projet importé. Ce chemin fonctionne dans l’éditeur et dans un export lorsque la ressource est incluse.

Le caractère `\` placé en fin de ligne continue l’expression sur la ligne suivante. Le style peut aussi utiliser des parenthèses.

### 17.3 `ResourceLoader.exists(path, type_hint)`

Paramètres :

- `path` : chemin de la ressource ;
- `type_hint` : nom de type attendu, utilisé comme indication.

Retour :

- `true` lorsque la ressource est reconnue ;
- `false` lorsqu’elle est absente ou non chargeable selon le type annoncé.

Ce contrôle ne remplace pas le cast après chargement.

### 17.4 `ResourceLoader.load(path, type_hint)`

La fonction reçoit le même chemin et le même indice de type.

Elle renvoie une `Resource` générale, ou `null` en cas d’échec.

Le cast :

> **[LECTURE] Cast contrôlé — Ne pas recopier isolément.**

```gdscript
var catalog := loaded as BeaconCatalog
```

renvoie :

- l’objet typé si `loaded` est compatible ;
- `null` dans le cas contraire.

### 17.5 Validation avant injection

La Resource n’est renvoyée qu’après `catalog.validate()`.

Le point de composition peut alors construire :

> **[LECTURE] Assemblage de dépendance — Étudier le flux.**

```gdscript
var catalog := _load_beacon_catalog()
if catalog == null:
	return false

var repository := ResourceBeaconCatalogRepository.new(catalog)
```

`return false` indique au bootstrap que l’étape de démarrage a échoué. Le chapitre 5 a défini la stratégie de nettoyage d’un démarrage partiel.

## 18. Afficher les problèmes sans coupler le validateur

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

Paramètre :

- `report` contient les problèmes structurés.

Retour :

- `-> void` indique que la fonction affiche les problèmes mais ne renvoie rien.

Cette séparation permet à un autre consommateur de :

- afficher les erreurs dans une fenêtre ;
- produire un rapport CI ;
- compter les erreurs ;
- traduire les messages ;
- refuser une publication.

Le catalogue ne choisit donc pas lui-même l’interface de diagnostic.

## 19. `preload()`, `load()` et `ResourceLoader`

### 19.1 `preload()`

Utiliser `preload()` lorsque :

- le chemin est constant ;
- la dépendance est obligatoire ;
- la ressource est raisonnablement petite ;
- son chargement doit être vérifié pendant l’analyse du script.

> **[LECTURE] Dépendance connue à l’avance — Ne pas recopier sans évaluer le coût.**

```gdscript
const DEFAULT_PROFILE: BeaconProfile = preload(
	"res://data/beacons/default_beacon.tres"
)
```

`preload()` ne peut pas recevoir un chemin calculé dans une variable runtime.

### 19.2 `load()`

Utiliser `load()` lorsque :

- le chemin n’est connu qu’à l’exécution ;
- le contenu choisi dépend d’une configuration ;
- le chargement peut être retardé ;
- le code peut gérer un échec.

`load()` est une forme concise de chargement synchrone et peut bloquer le thread appelant.

### 19.3 `ResourceLoader`

Utiliser directement `ResourceLoader` pour :

- vérifier l’existence ;
- fournir un indice de type ;
- choisir un mode de cache ;
- demander un chargement en arrière-plan ;
- inspecter la progression.

Le projet évite d’appeler ces API depuis les règles métier. Elles restent dans l’infrastructure et le point de composition.

## 20. JSON : rôle et limites

JSON convient lorsque les données doivent être :

- lisibles par Godot et d’autres outils ;
- générées par Python ;
- relues dans une revue de code ;
- transférées par HTTP au chapitre 12 ;
- représentées avec objets, tableaux, chaînes, booléens, nombres et `null`.

JSON ne connaît pas directement :

- `Vector3` ;
- `Color` ;
- `StringName` ;
- une classe `BeaconProfile` ;
- une référence de Resource ;
- un commentaire standard ;
- un entier distinct d’un nombre flottant au niveau du format.

Un JSON chargé devient d’abord un ensemble de `Variant`, `Dictionary` et `Array`. Le code doit ensuite vérifier la forme et convertir les valeurs.

## 21. Créer la configuration par défaut

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

- `schema_version` décrit la forme du document ;
- `environment` nomme l’environnement par défaut ;
- `logging` regroupe les options de journalisation ;
- `ai_services.enabled` permet un chemin déterministe sans IA ;
- `base_url` reste locale dans l’exemple ;
- `request_timeout_seconds` est un nombre ;
- `data.beacon_catalog` centralise le chemin du catalogue.

Ce fichier ne contient :

- ni mot de passe ;
- ni jeton API ;
- ni progression du joueur ;
- ni état de session.

## 22. Ajouter une surcharge d’environnement

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

Ce fichier ne répète pas toutes les clés. Il surcharge uniquement les valeurs différentes.

La configuration finale sera obtenue par fusion :

1. valeurs par défaut ;
2. surcharge d’environnement ;
3. futurs réglages utilisateur autorisés ;
4. futurs arguments de ligne de commande autorisés.

Le chapitre 7 implémente les deux premières couches. Les couches utilisateur persistantes attendront le chapitre 9.

## 23. Lire un fichier JSON avec des erreurs détaillées

### 23.1 Créer `JsonConfigLoader`

> **[VSC] Visual Studio Code — Créer :** `src/core/config/json_config_loader.gd`.

```gdscript
class_name JsonConfigLoader
extends RefCounted
## Lit et fusionne des objets JSON de configuration.


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
			"Ouverture impossible, code : %s."
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

### 23.2 Paramètres de `load_object()`

La fonction reçoit :

- `path` : chemin Godot, par exemple `res://config/defaults/runtime.json` ;
- `report` : objet partagé qui accumule les erreurs.

Elle renvoie toujours un `Dictionary`.

En cas d’échec, elle renvoie `{}`, un dictionnaire vide, et ajoute une erreur au rapport. Le consommateur ne doit pas interpréter `{}` comme une réussite ; il doit consulter `report.has_errors()`.

### 23.3 `FileAccess.file_exists(path)`

Cette méthode statique reçoit un chemin et renvoie un booléen.

Le contrôle préalable distingue clairement :

- fichier absent ;
- fichier présent mais impossible à ouvrir ;
- fichier lisible mais JSON invalide.

### 23.4 `FileAccess.open(path, mode)`

Arguments :

- `path` : fichier à ouvrir ;
- `FileAccess.READ` : mode lecture seule.

Retour :

- un objet `FileAccess` en cas de réussite ;
- `null` en cas d’échec.

`FileAccess.get_open_error()` renvoie le dernier code d’ouverture du thread courant. `error_string(...)` convertit ce code en texte lisible.

### 23.5 `file.get_as_text()`

Cette méthode lit le contenu restant du fichier comme texte UTF-8.

Elle ne parse pas le JSON. Elle produit seulement une `String`.

### 23.6 `JSON.new()` et `parse()`

`JSON.new()` crée un parseur afin de conserver les détails d’erreur.

`parser.parse(source_text)` reçoit le texte complet et renvoie un code `Error`.

- `OK` signifie que le parseur a produit une valeur ;
- une autre valeur signale un échec.

Après un échec :

- `get_error_line()` fournit le numéro de ligne ;
- `get_error_message()` fournit le message.

La méthode statique `JSON.parse_string()` est plus courte, mais elle renvoie seulement `null` en cas d’échec et ne fournit pas ces détails. Le chargeur de production utilise donc l’instance `JSON`.

### 23.7 Vérifier la racine

Un document JSON valide peut contenir une chaîne, un tableau ou `null` à la racine.

La configuration attend un objet. Le test :

> **[LECTURE] Contrôle de type Variant — Étudier la constante.**

```gdscript
typeof(parser.data) != TYPE_DICTIONARY
```

compare le type runtime de la valeur à la constante globale représentant un dictionnaire.

Le cast final `as Dictionary` n’est effectué qu’après cette vérification.

## 24. Valider une valeur JSON

Un parse JSON réussi ne garantit pas que les clés et types conviennent au jeu.

Créer des fonctions de lecture strictes.

> **[VSC] Visual Studio Code — Ajouter à `src/core/config/json_config_loader.gd`.**

```gdscript
func read_int(
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

### 24.1 Pourquoi accepter `TYPE_FLOAT`

JSON ne distingue pas formellement entier et flottant. Godot convertit les nombres JSON selon son parseur numérique.

Le chargeur accepte donc `TYPE_FLOAT` ou `TYPE_INT`, puis vérifie que la valeur est mathématiquement entière.

### 24.2 Paramètres

- `source` : objet JSON courant ;
- `key` : clé recherchée ;
- `location` : chemin du parent pour le diagnostic ;
- `report` : accumulateur d’erreurs.

Retour :

- entier validé ;
- `0` en cas d’erreur, accompagné d’un problème dans le rapport.

Le `0` de repli ne doit pas être utilisé lorsque `report.has_errors()` vaut `true`.

### 24.3 `is_equal_approx()`

Les nombres flottants peuvent contenir de petites imprécisions.

`round(numeric_value)` calcule l’entier le plus proche sous forme numérique.

`is_equal_approx(a, b)` compare avec une tolérance adaptée au calcul flottant.

## 25. Fusionner deux objets JSON

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

### 25.1 Paramètres et retour

- `base` : dictionnaire de départ ;
- `override_values` : valeurs prioritaires ;
- retour : nouveau dictionnaire fusionné.

La fonction ne modifie pas intentionnellement `base`. Elle commence par `base.duplicate(true)`.

### 25.2 Fusion récursive

Lorsque la valeur existante et la surcharge sont toutes deux des dictionnaires, la fonction s’appelle elle-même.

Exemple :

- la base contient `ai_services.base_url` et `ai_services.enabled` ;
- la surcharge contient seulement `ai_services.enabled` ;
- le résultat conserve `base_url` et remplace `enabled`.

Si les types diffèrent, la surcharge remplace la valeur entière.

### 25.3 Limites de la politique

Cette politique :

- fusionne les objets ;
- remplace les tableaux entièrement ;
- remplace les valeurs scalaires ;
- ne supprime pas une clé avec `null` ;
- ne valide pas les types métier.

Ces choix doivent être documentés afin que les outils Python futurs produisent le même résultat.

## 26. Représenter la configuration runtime

### 26.1 Créer `RuntimeConfiguration`

> **[VSC] Visual Studio Code — Créer :** `src/core/config/runtime_configuration.gd`.

```gdscript
class_name RuntimeConfiguration
extends RefCounted
## Configuration validée utilisée par le runtime.

const CURRENT_SCHEMA_VERSION: int = 1

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

La classe `RuntimeConfiguration` n’est pas une Resource :

- elle représente le résultat validé du chargement ;
- elle n’est pas éditée dans l’Inspector ;
- elle n’est pas enregistrée dans un `.tres` ;
- elle peut être injectée dans les services ;
- elle reste séparée des dictionnaires bruts.

### 26.2 Fonction `apply()`

Paramètres :

- `data` : dictionnaire fusionné ;
- `report` : rapport partagé.

Retour :

- aucun ; les propriétés de l’instance sont mises à jour.

Les sous-fonctions séparent les groupes de clés afin d’éviter une fonction monolithique.

## 27. Lire les groupes de configuration

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

	schema_version = int(raw_version)

	if schema_version != CURRENT_SCHEMA_VERSION:
		report.add_error(
			&"unsupported_schema",
			"schema_version",
			"Version de configuration non prise en charge : %d."
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
			"Le nom d’environnement doit être une chaîne."
		)
		return

	var normalized := String(raw_environment).strip_edges()
	if normalized.is_empty():
		report.add_error(
			&"empty_environment",
			"environment",
			"Le nom d’environnement est vide."
		)
		return

	environment = StringName(normalized)
```

### 27.1 `Dictionary.get(key)`

`data.get("schema_version")` renvoie :

- la valeur associée ;
- `null` si la clé manque.

Une valeur absente échoue au contrôle de type et produit donc une erreur explicite.

### 27.2 Conversion en `int`

`int(raw_version)` convertit la valeur numérique.

Pour une validation stricte, la fonction pourrait aussi vérifier l’absence de partie décimale comme `read_int()`.

Ici, seules les versions exactes produites par les fichiers du projet sont attendues. L’audit signale néanmoins cette simplification comme point à renforcer avant une entrée externe non fiable.

### 27.3 Normalisation de l’environnement

`String(raw_environment)` convertit le `Variant` validé en chaîne.

`strip_edges()` retire les espaces de début et de fin.

`StringName(normalized)` crée l’identifiant optimisé utilisé au runtime.

## 28. Lire les sections imbriquées

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
			"Le niveau de journalisation doit être une chaîne."
		)
		return

	var candidate := StringName(
		String(raw_level).to_lower()
	)

	if candidate not in [&"debug", &"info", &"warning", &"error"]:
		report.add_error(
			&"unsupported_log_level",
			"logging.level",
			"Niveau de journalisation inconnu : %s."
			% candidate
		)
		return

	log_level = candidate
```

### 28.1 Section intermédiaire

La clé `logging` doit contenir un dictionnaire.

Le cast `(section as Dictionary)` n’est effectué qu’après contrôle avec `typeof()`.

### 28.2 Opérateur `not in`

> **[LECTURE] Test d’appartenance — Étudier la liste autorisée.**

```gdscript
candidate not in [&"debug", &"info", &"warning", &"error"]
```

- `candidate` est la valeur vérifiée ;
- `in` teste l’appartenance ;
- `not` inverse le résultat ;
- le tableau contient les valeurs autorisées.

Cette liste fermée empêche une faute comme `verbsoe` de devenir silencieusement un nouveau niveau.

## 29. Charger et construire la configuration finale

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

### 29.1 Pourquoi un dictionnaire de résultat

GDScript ne définit pas ici un type générique `Result<T>`.

La fonction renvoie donc un dictionnaire avec deux clés stables :

- `configuration` : objet typé ou `null` ;
- `report` : rapport toujours présent.

Le consommateur doit extraire et vérifier les deux.

Dans un projet plus avancé, une classe `ConfigurationLoadResult` dédiée serait préférable. Elle est volontairement évitée ici pour ne pas multiplier les abstractions avant un second besoin.

### 29.2 Arrêt après une erreur de lecture

Une fusion n’est pas tentée lorsque le fichier par défaut est invalide.

La surcharge d’environnement n’est pas autorisée à réparer silencieusement un document de base corrompu.

### 29.3 Expression conditionnelle

L’expression :

> **[LECTURE] Valeur conditionnelle — Ne pas recopier isolément.**

```gdscript
configuration if report.is_valid() else null
```

renvoie l’objet seulement lorsque le rapport ne contient aucune erreur.

Les avertissements n’empêchent pas la configuration d’être utilisée.

## 30. Choisir l’environnement

Le choix de l’environnement doit être explicite et centralisé.

Pour ce chapitre :

- `development` utilise uniquement le fichier par défaut ;
- `studio` ajoute `config/environments/studio.json`.

Le bootstrap peut recevoir ce choix depuis une constante temporaire.

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

### 30.1 `match`

`match` compare `ACTIVE_ENVIRONMENT` aux cas déclarés.

- `development` renvoie une chaîne vide, donc aucune surcharge ;
- `studio` renvoie le chemin de surcharge ;
- `_` représente tous les autres cas.

Une chaîne vide signifie ici « pas de fichier de surcharge ». Cette convention est limitée à cette fonction et doit rester documentée.

### 30.2 Pourquoi ne pas utiliser une variable d’environnement secrète

Le choix de profil n’est pas un secret.

Les secrets ne doivent pas être stockés dans Git ni dans un JSON embarqué. Les chapitres 11 à 13 préciseront les moyens sûrs de fournir des informations sensibles aux services locaux.

## 31. Assembler la configuration et le repository

> **[VSC] Visual Studio Code — Ajouter au démarrage de `src/app/app_bootstrap.gd`.**

```gdscript
func _build_data_services() -> bool:
	var loader := JsonConfigLoader.new()
	var result := loader.load_runtime_configuration(
		DEFAULT_CONFIG_PATH,
		_resolve_environment_path()
	)

	var report := result["report"] as DataValidationReport
	if report == null:
		push_error("Rapport de configuration absent.")
		return false

	if report.has_errors():
		_print_data_issues(report)
		return false

	var configuration := \
		result["configuration"] as RuntimeConfiguration

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

### 31.1 Responsabilité de la fonction

`_build_data_services()` :

1. charge les JSON ;
2. vérifie le rapport ;
3. obtient une configuration typée ;
4. charge le catalogue indiqué ;
5. construit le repository ;
6. enregistre les services au point de composition.

Elle renvoie `true` lorsque toute la chaîne est prête.

### 31.2 Accès aux clés du résultat

> **[LECTURE] Extraction typée — Étudier le cast après accès par clé.**

```gdscript
var report := result["report"] as DataValidationReport
```

- `result["report"]` lit la valeur associée à la clé ;
- le type statique d’une valeur de dictionnaire est `Variant` ;
- `as DataValidationReport` réalise un cast sûr ;
- `report` vaut `null` si le type ne correspond pas.

Le contrôle `report == null` protège une modification future du contrat.

### 31.3 Registre limité au point de composition

Le registre du chapitre 5 est utilisé ici uniquement pour publier les dépendances construites.

Un service de gameplay ne doit pas appeler directement :

> **[LECTURE] Contre-exemple de Service Locator — Ne pas recopier.**

```gdscript
ServiceRegistry.get(&"beacon_catalog_repository")
```

Il reçoit le repository par constructeur ou par méthode `configure()`.

## 32. `res://`, `user://` et chemins absolus

### 32.1 `res://`

`res://` pointe vers les ressources du projet.

Utilisation :

- scripts ;
- scènes ;
- Resources ;
- configurations embarquées ;
- données de conception.

Dans un export, le contenu peut se trouver dans le paquet de ressources. Il ne faut pas supposer qu’il s’agit d’un dossier Windows modifiable.

### 32.2 `user://`

`user://` pointe vers le dossier de données de l’application pour l’utilisateur courant.

Utilisation future :

- réglages utilisateur ;
- sauvegardes ;
- caches ;
- journaux selon la politique du projet.

Le chemin réel dépend du système et de la configuration du projet.

Le chapitre 7 ne crée pas encore de fichier persistant sous `user://`. Cette écriture appartient au chapitre 9.

### 32.3 Chemins absolus

Un chemin absolu Windows comme `C:\Asteria\data.json` ne doit pas être codé dans le gameplay.

Il dépend :

- de la machine ;
- du compte ;
- du disque ;
- de l’installation ;
- des permissions.

Les outils d’import du chapitre 26 pourront recevoir un chemin choisi par l’utilisateur, mais le runtime livré doit utiliser des chemins portables.

## 33. Inclure les JSON dans un export

Godot reconnaît les Resources natives et les ressources importées. Un fichier arbitraire peut nécessiter un filtre d’export.

> **[APP] Godot Editor — Ouvrir `Project > Export`, sélectionner le preset, puis vérifier les filtres de ressources.**

Pour les fichiers JSON chargés directement au runtime, ajouter si nécessaire :

> **[APP] Godot Editor — Dans le preset d’export, configurer le filtre des fichiers non-ressources.**

```text
config/**/*.json
```

Ne pas ajouter `**/*.json` sans raison : cela pourrait embarquer des fichiers de travail ou des données sensibles placées par erreur dans le dépôt.

Après export, tester réellement :

- présence du fichier ;
- lecture par `FileAccess` ;
- chargement du catalogue ;
- messages d’erreur ;
- absence de chemin local de développement.

## 34. `ConfigFile` comme alternative ciblée

`ConfigFile` gère un format par sections et clés.

> **[LECTURE] Exemple de format `ConfigFile` — Ne pas créer dans ce chapitre.**

```ini
[logging]
level="info"

[ai_services]
enabled=false
request_timeout_seconds=10.0
```

Avantages :

- API Godot simple ;
- conservation de plusieurs types `Variant` ;
- structure adaptée aux petites configurations.

Limites :

- format moins interopérable que JSON ;
- commentaires perdus lors d’une réécriture ;
- conventions `.cfg` et `.ini` non parfaitement standardisées ;
- moins adapté aux tableaux d’objets complexes.

Choix de `Project Asteria` :

- JSON pour les configurations interopérables ;
- `ConfigFile` possible pour un outil purement Godot ;
- aucune coexistence de deux formats pour la même responsabilité sans justification.

## 35. Chargement en arrière-plan

### 35.1 Quand le chargement synchrone suffit

Le catalogue de démonstration est petit et chargé au démarrage. Un chargement synchrone est acceptable.

### 35.2 Quand différer

Un chargement en arrière-plan devient utile pour :

- une grande scène ;
- un gros catalogue de ressources ;
- un ensemble de textures ou modèles ;
- un changement de zone ;
- un écran de chargement.

### 35.3 Demander un chargement

> **[LECTURE] Exemple de chargement différé — Étudier avant intégration.**

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

Paramètres :

- chemin de la ressource ;
- indice de type.

Retour :

- `OK` si la demande est acceptée ;
- autre code `Error` si elle ne démarre pas.

### 35.4 Vérifier le statut sur plusieurs images

> **[LECTURE] Exemple de suivi — Ne pas utiliser dans une boucle bloquante.**

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

`progress` reçoit un élément entre `0.0` et `1.0`.

Le statut doit être interrogé dans `_process()` ou un mécanisme réparti sur plusieurs images. Une boucle `while` serrée bloquerait la boucle principale et annulerait le bénéfice du chargement différé.

`load_threaded_get()` peut bloquer s’il est appelé avant le statut `THREAD_LOAD_LOADED`.

## 36. Politique de cache

Le mode normal de `ResourceLoader` réutilise le cache.

Conséquences positives :

- pas de chargement disque répété ;
- références cohérentes ;
- économie de mémoire pour les définitions partagées.

Risques :

- une mutation accidentelle devient globale ;
- un rechargement de fichier ne crée pas forcément une nouvelle instance ;
- un test peut observer une Resource déjà modifiée par un autre test.

Règles du projet :

1. définitions canoniques en lecture seule ;
2. état runtime séparé ;
3. chemins centralisés ;
4. modes de cache avancés confinés à l’infrastructure ;
5. aucun rechargement forcé dispersé dans le gameplay ;
6. tests futurs réinitialisant leurs dépendances.

Les modes `CACHE_MODE_IGNORE`, `REUSE` et `REPLACE` existent, mais ils ne sont pas utilisés sans besoin mesuré. Leur propagation aux sous-ressources et dépendances exige une revue spécifique.

## 37. Versionner les formats

### 37.1 Version de document

Chaque racine de données durable possède `schema_version`.

Cette version décrit la structure, pas la version du jeu.

Exemple :

> **[LECTURE] Évolution de schéma — Ne pas saisir.**

```text
schéma 1  ai_services.request_timeout_seconds
schéma 2  ai_services.timeouts.request_seconds
```

### 37.2 Compatibilité

Le lecteur de données doit choisir explicitement :

- accepter la version courante ;
- migrer une version ancienne ;
- refuser une version future inconnue.

Il ne doit pas ignorer silencieusement `schema_version`.

### 37.3 Identifiants et migration

Une migration de structure ne doit pas changer les identifiants métier sans table de correspondance.

Un renommage d’identifiant peut casser :

- sauvegardes ;
- références de quêtes ;
- relations SQLite ;
- événements ;
- métriques.

### 37.4 Portée de ce chapitre

Le chapitre 7 détecte une version inconnue et la refuse.

Le chapitre 8 appliquera cette discipline aux migrations de base.

Le chapitre 9 l’appliquera aux sauvegardes et aux conversions entre versions.

## 38. Sécurité des données

### 38.1 Ne jamais faire confiance au format seul

Un JSON valide peut contenir :

- une URL inattendue ;
- un délai négatif ;
- un tableau énorme ;
- une chaîne vide ;
- un chemin hors du projet ;
- une valeur d’un type incorrect.

La validation sémantique reste obligatoire.

### 38.2 Chemins fournis par configuration

Avant de charger un chemin provenant d’un JSON :

- vérifier le préfixe autorisé ;
- vérifier l’extension ;
- vérifier l’existence ;
- vérifier le type de Resource ;
- refuser les chemins absolus non autorisés.

> **[VSC] Visual Studio Code — Ajouter une validation avant `_load_catalog_at()`.**

```gdscript
func _is_allowed_catalog_path(path: String) -> bool:
	if not path.begins_with("res://data/beacons/"):
		return false

	if path.get_extension().to_lower() not in ["tres", "res"]:
		return false

	return true
```

Paramètre :

- `path` : chemin candidat.

Retour :

- `true` si le chemin reste dans le dossier autorisé et utilise une extension native ;
- `false` sinon.

Cette validation n’est pas une protection universelle contre toutes les entrées hostiles. Elle limite le périmètre de la configuration de ce projet.

### 38.3 Objets JSON

Par défaut, ne pas activer la désérialisation arbitraire d’objets provenant d’une source non fiable.

Le projet utilise des dictionnaires simples, puis construit explicitement des objets typés.

### 38.4 Secrets

Ne jamais placer dans les JSON versionnés :

- mot de passe ;
- clé privée ;
- jeton d’accès ;
- secret de service ;
- donnée personnelle.

## 39. Exercice intégré

### 39.1 Objectif

Créer une scène de démonstration qui :

1. reçoit un `BeaconCatalogRepository` ;
2. demande une définition par identifiant ;
3. affiche ses propriétés ;
4. signale proprement un identifiant absent ;
5. ne charge aucun fichier directement.

### 39.2 Créer le script

> **[VSC] Visual Studio Code — Créer :** `scenes/learning/ch07_data_demo.gd`.

```gdscript
class_name Ch07DataDemo
extends Node
## Démonstration sans dépendance directe à ResourceLoader.

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

### 39.3 `configure(repository)`

Le paramètre `repository` fournit la dépendance.

L’assertion protège une erreur d’assemblage. La propriété privée `_repository` conserve la référence pour les appels suivants.

### 39.4 `run_demo(id)`

Le paramètre `id` désigne la définition demandée.

La fonction renvoie :

- `true` lorsqu’une définition est trouvée et affichée ;
- `false` si le composant n’est pas configuré ou si l’identifiant est absent.

Elle ne connaît :

- ni chemin de fichier ;
- ni `ResourceLoader` ;
- ni JSON ;
- ni registre global.

### 39.5 Créer la scène

> **[APP] Godot Editor — Créer une scène avec un nœud racine `Node`, le renommer `Ch07DataDemo`, attacher `scenes/learning/ch07_data_demo.gd`, puis enregistrer sous `scenes/learning/ch07_data_demo.tscn`.**

Le bootstrap instanciera ou référencera cette scène, appellera `configure(repository)`, puis :

> **[LECTURE] Appel de démonstration — Adapter au bootstrap existant.**

```gdscript
data_demo.run_demo(&"default_beacon")
```

Résultat attendu :

> **[SORTIE] Exemple de sortie Godot — Ne pas saisir.**

```text
Balise default_beacon — Balise Asteria — cooldown 2.0 s
```

## 40. Vérifications manuelles

### 40.1 Catalogue valide

- lancer la validation ;
- vérifier l’absence d’erreur ;
- démarrer la scène ;
- demander `default_beacon` ;
- vérifier le nom et le cooldown.

### 40.2 Identifiant dupliqué

- dupliquer temporairement un identifiant dans l’Inspector ;
- relancer la validation ;
- vérifier `duplicate_id` ;
- rétablir l’identifiant correct.

### 40.3 JSON invalide

- sur une branche de test, retirer une virgule ou une accolade ;
- lancer le projet ;
- vérifier le numéro de ligne et le message ;
- restaurer immédiatement le fichier.

### 40.4 Mauvais type

- remplacer temporairement `request_timeout_seconds` par une chaîne ;
- vérifier que la validation refuse la configuration ;
- restaurer le nombre.

### 40.5 Fichier d’environnement absent

- choisir un chemin absent ;
- vérifier `file_not_found` ;
- confirmer que le bootstrap s’arrête proprement.

### 40.6 Export

À la fin du Livre II, lors de la campagne runtime :

- exporter une construction de test ;
- vérifier l’inclusion des JSON ;
- charger le catalogue ;
- confirmer les chemins `res://` ;
- confirmer qu’aucun chemin de poste de travail n’apparaît.

## 41. Erreurs fréquentes et corrections

### 41.1 Modifier une Resource partagée

**Symptôme :** plusieurs instances changent ensemble.

**Cause :** la définition mise en cache a été utilisée comme état runtime.

**Correction :** déplacer les propriétés changeantes dans un objet d’état.

### 41.2 Utiliser le nom affiché comme clé

**Symptôme :** une traduction casse une recherche.

**Cause :** identité et présentation sont confondues.

**Correction :** conserver un `StringName` stable.

### 41.3 Accepter un JSON seulement parce qu’il se parse

**Symptôme :** une clé absente produit une erreur plus loin.

**Cause :** aucune validation de schéma et de type.

**Correction :** vérifier chaque section avant construction de l’objet typé.

### 41.4 Appeler `JSON.parse_string()` sans diagnostic

**Symptôme :** le chargeur sait seulement que le résultat vaut `null`.

**Cause :** méthode courte utilisée dans un chemin de production.

**Correction :** utiliser `JSON.new()`, `parse()`, `get_error_line()` et `get_error_message()`.

### 41.5 Charger depuis chaque service

**Symptôme :** chemins dupliqués, cache mal compris et tests difficiles.

**Cause :** infrastructure dispersée.

**Correction :** charger au point de composition et injecter un repository.

### 41.6 Utiliser un index de tableau comme identifiant

**Symptôme :** réordonner le catalogue modifie le sens des références.

**Cause :** position éditoriale confondue avec identité.

**Correction :** rechercher par identifiant stable.

### 41.7 Écrire une sauvegarde dans `res://`

**Symptôme :** l’écriture échoue après export.

**Cause :** ressources embarquées traitées comme dossier utilisateur.

**Correction :** utiliser `user://` au chapitre 9.

### 41.8 Embarquer un secret

**Symptôme :** un jeton est visible dans Git ou dans le paquet.

**Cause :** configuration et secret confondus.

**Correction :** retirer le secret, le révoquer et utiliser un mécanisme externe approprié.

### 41.9 Boucler sur le statut de chargement

**Symptôme :** l’application se fige malgré le chargement en arrière-plan.

**Cause :** boucle bloquante dans la même image.

**Correction :** interroger le statut sur plusieurs appels de `_process()`.

### 41.10 Multiplier les formats

**Symptôme :** une même option existe dans `.tres`, JSON et `.cfg`.

**Cause :** absence de source de vérité.

**Correction :** attribuer une responsabilité unique à chaque format.

## 42. Parcours Solo et Studio

### 42.1 Mode Solo

Le parcours Solo peut conserver :

- un catalogue `.tres` ;
- un JSON par défaut ;
- une surcharge locale de développement ;
- un repository Resource ;
- une validation au démarrage ;
- une revue Git simple.

Priorité : lisibilité et faible coût opérationnel.

### 42.2 Mode Studio

Le parcours Studio ajoute :

- propriétaire désigné pour chaque schéma ;
- revue obligatoire des identifiants ;
- catalogue généré ou contrôlé en CI ;
- règles de compatibilité documentées ;
- fichiers d’environnement approuvés ;
- validation de taille et de plage ;
- artefact de rapport ;
- séparation des secrets ;
- tests d’export ;
- politique de dépréciation des identifiants.

### 42.3 Contrat commun

Les deux parcours conservent :

- une source de vérité ;
- des identifiants stables ;
- une validation avant usage ;
- des objets typés après parsing ;
- un repository injecté ;
- l’absence de mutation des définitions canoniques.

## 43. Contrat documentaire

> **[VSC] Visual Studio Code — Créer :** `docs/architecture/data-contract.md`.

Le document doit contenir :

- les quatre familles de données ;
- le propriétaire de chaque format ;
- les dossiers autorisés ;
- la convention d’identifiants ;
- les versions de schéma ;
- l’ordre des couches de configuration ;
- la politique de fusion ;
- les plages et valeurs autorisées ;
- les erreurs bloquantes ;
- les données sensibles interdites ;
- la frontière avec SQLite ;
- la frontière avec les sauvegardes ;
- la stratégie de dépréciation.

Exemple de tableau :

> **[VSC] Visual Studio Code — Ajouter dans `docs/architecture/data-contract.md`.**

```markdown
| Source | Propriétaire | Mutée au runtime | Versionnée Git |
|---|---|---:|---:|
| `data/**/*.tres` | conception | non | oui |
| `config/defaults/*.json` | architecture | non | oui |
| configuration typée en mémoire | bootstrap | oui, avant injection | non |
| état de session | fonctionnalité | oui | non |
| `user://` | chapitre 9 | oui | non |
```

## 44. Livrables du chapitre

À l’issue du chapitre, le projet doit documenter ou créer :

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

Les chemins de code sont des livrables guidés du projet fil rouge. Ils ne signifient pas que le Starter Kit du Companion Pack est déjà matérialisé dans le dépôt documentaire.

## 45. Checklist de revue

### 45.1 Modèle de données

- [ ] Les définitions sont séparées de l’état runtime.
- [ ] Chaque définition possède un identifiant stable.
- [ ] Le nom affiché n’est pas utilisé comme clé.
- [ ] Le catalogue possède une version de schéma.
- [ ] Les entrées `null` sont détectées.
- [ ] Les doublons d’identifiant sont refusés.
- [ ] Les valeurs métier sont validées.

### 45.2 Resources

- [ ] Les définitions canoniques ne sont pas modifiées au runtime.
- [ ] Le partage par cache est compris.
- [ ] `resource_local_to_scene` n’est utilisé que pour un besoin local.
- [ ] Les casts après chargement sont contrôlés.
- [ ] Le chemin de catalogue est centralisé.

### 45.3 JSON

- [ ] Le fichier est ouvert avec un contrôle d’erreur.
- [ ] Le parseur fournit ligne et message.
- [ ] La racine est un dictionnaire.
- [ ] Les sections imbriquées sont vérifiées.
- [ ] Les types numériques sont normalisés.
- [ ] Les valeurs autorisées sont bornées.
- [ ] La version de schéma est vérifiée.
- [ ] La politique de fusion est documentée.

### 45.4 Architecture

- [ ] Le domaine ne dépend pas de `FileAccess`.
- [ ] Le gameplay ne dépend pas de `ResourceLoader`.
- [ ] Le repository est injecté.
- [ ] Le registre reste limité au point de composition.
- [ ] Les erreurs sont structurées.
- [ ] Les frontières SQLite et sauvegarde sont respectées.
- [ ] Aucun secret n’est embarqué.

### 45.5 Publication

- [ ] Les JSON nécessaires seront inclus dans l’export.
- [ ] Aucun chemin absolu de développement n’est utilisé.
- [ ] La validation automatique légère est verte.
- [ ] Aucun PDF intermédiaire n’est produit.
- [ ] Le test runtime reste déclaré comme réserve tant qu’il n’est pas exécuté.

## 46. Résumé

Le chapitre établit une chaîne de données contrôlée :

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
3. une Resource chargée peut être partagée par le cache ;
4. une définition canonique reste en lecture seule par convention ;
5. un JSON valide syntaxiquement peut être invalide pour le jeu ;
6. le parseur doit produire des erreurs localisables ;
7. une configuration brute devient un objet typé avant usage ;
8. les couches de configuration suivent un ordre documenté ;
9. les chemins et chargeurs restent dans l’infrastructure ;
10. le repository prépare le remplacement par SQLite ;
11. les secrets ne sont jamais versionnés dans les données ;
12. les sauvegardes et migrations complètes restent aux chapitres suivants.

## 47. Passage au chapitre suivant

Le chapitre 8 utilisera ces fondations pour introduire :

- SQLite ;
- schéma relationnel ;
- migrations ;
- transactions ;
- index ;
- repositories persistants ;
- séparation lecture/écriture ;
- import contrôlé depuis les données de conception.

Avant de continuer, le projet doit pouvoir charger une configuration validée et exposer le catalogue de balises par un repository sans modifier les Resources canoniques.
