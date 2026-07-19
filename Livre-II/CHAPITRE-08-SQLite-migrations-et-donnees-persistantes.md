---
title: "Livre II — Chapitre 8 : SQLite, migrations et données persistantes"
id: "DOC-L2-CH08"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
chapter: 8
last-verified: "2026-07-19"
audit-status: "complete"
audit-date: "2026-07-19"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-08.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
reference-addon:
  name: "Godot-SQLite"
  version: "4.7"
  license: "MIT"
  distribution: "Godot Asset Library"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
recommended-reasoning: "GPT-5.6 Sol — Élevée"
---

# SQLite, migrations et données persistantes

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir, **[LECTURE]** exemple à étudier. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH08`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Addon de référence :** Godot-SQLite `4.7`, licence MIT  
> **Niveau de raisonnement conseillé :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-08.md`.

## 1. Rôle du chapitre

Le chapitre 7 a séparé les données de conception, la configuration, l’état runtime et la persistance. Il a aussi créé des identifiants stables, des catalogues typés et des objets d’état vivants.

Le présent chapitre ajoute une base relationnelle locale pour les données qui doivent :

- survivre à la fermeture du jeu ;
- être recherchées ou filtrées efficacement ;
- conserver des relations entre plusieurs ensembles de données ;
- être modifiées de manière atomique ;
- évoluer avec un schéma versionné ;
- rester accessibles sans serveur externe.

À la fin du chapitre, le lecteur doit savoir :

- expliquer le rôle de SQLite dans `Project Asteria` ;
- distinguer base persistante et fichier de sauvegarde ;
- installer et qualifier une extension SQLite pour Godot ;
- concevoir des tables, contraintes, clés et index ;
- ouvrir une base sous `user://` ;
- exécuter des requêtes paramétrées ;
- grouper plusieurs écritures dans une transaction ;
- construire un contrat de dépôt indépendant de SQLite ;
- créer et appliquer des migrations numérotées ;
- vérifier le checksum des migrations déjà appliquées ;
- créer une copie de sécurité avant une migration ;
- diagnostiquer l’intégrité et les clés étrangères ;
- préparer le chapitre 9 sans définir prématurément son format de sauvegarde.

## 2. Prérequis

Le lecteur doit connaître :

- les classes, dictionnaires, tableaux, fonctions et codes `Error` du chapitre 2 ;
- les `Resource` et signaux du chapitre 3 ;
- l’architecture feature-first et les dépendances autorisées du chapitre 4 ;
- le bootstrap, les services et l’injection du chapitre 5 ;
- l’état runtime du chapitre 6 ;
- `BeaconProfile`, `BeaconRuntimeState`, `StableId` et les frontières de données du chapitre 7.

Le projet fil rouge conserve `src/app` comme point de composition. La couche métier ne connaît ni fichier `.sqlite3`, ni SQL, ni addon natif.

## 3. Périmètre et frontières

Ce chapitre définit :

- l’intégration SQLite locale ;
- le fichier de base principal ;
- une abstraction de connexion ;
- un schéma relationnel initial ;
- les requêtes paramétrées ;
- les transactions ;
- un dépôt persistant de l’état des balises ;
- les migrations de schéma ;
- la sauvegarde technique préalable à une migration ;
- les vérifications d’intégrité ;
- la préparation des exports Windows.

Il ne définit pas encore :

- les emplacements de sauvegarde visibles par le joueur ;
- les slots, miniatures et métadonnées de partie ;
- la capture atomique de l’état complet du monde ;
- la compatibilité entre versions de sauvegarde ;
- la stratégie de chargement partiel d’une partie ;
- la synchronisation cloud ;
- le chiffrement des sauvegardes ;
- la réplication multijoueur.

Ces sujets appartiennent au chapitre 9 ou aux Livres suivants.

> **Frontière essentielle :** SQLite fournit un moteur de stockage relationnel et transactionnel. Le système de sauvegarde décide quels états constituent une partie, quand les capturer, comment les versionner et comment les restaurer.

## 4. Pourquoi SQLite convient à `Project Asteria`

SQLite fonctionne sans serveur séparé. La base est stockée dans un fichier local et le moteur SQL s’exécute dans le processus du jeu par l’intermédiaire d’une bibliothèque native.

Cette approche convient aux besoins suivants :

- indexer de nombreux états persistants ;
- rechercher des lignes selon plusieurs critères ;
- relier des enregistrements par des clés étrangères ;
- garantir qu’un groupe de modifications est entièrement validé ou entièrement annulé ;
- faire évoluer le schéma par migrations ;
- inspecter la base avec des outils standards pendant le développement.

SQLite ne remplace pas automatiquement :

- les `Resource` éditables dans l’Inspector ;
- les fichiers JSON d’échange ;
- la configuration `ConfigFile` ;
- les objets runtime ;
- le format de sauvegarde complet du chapitre 9.

## 5. Matrice de décision

> **[LECTURE] Matrice de choix — Ne pas saisir.**

```text
Besoin                                             Support principal
------------------------------------------------  ---------------------------------
Définition d’une balise éditée par le concepteur   Resource .tres
État temporaire pendant une session                BeaconRuntimeState
Import ou échange avec un outil externe            JSON validé
Configuration locale non secrète                   ConfigFile
Recherche relationnelle persistante                SQLite
Historique d’événements persistant                  SQLite
Capture complète d’une partie                      Chapitre 9
Secret                                             Mécanisme externe sécurisé
```

La même donnée ne doit pas être dupliquée dans tous les supports. Par exemple, le nom affiché et le rayon d’activation restent dans `BeaconProfile`. La base conserve seulement les valeurs mutables qui doivent survivre.

## 6. Choisir l’intégration Godot

### 6.1 SQLite n’est pas intégré au cœur de Godot

Godot fournit `FileAccess`, `DirAccess`, des ressources et des mécanismes de sérialisation. Il ne fournit pas directement une classe SQLite dans l’édition Standard.

Une extension native est donc nécessaire pour le parcours GDScript.

### 6.2 Addon de référence

Le parcours principal utilise :

> **[LECTURE] Dépendance tierce de référence — Ne pas saisir.**

```text
Nom       : Godot-SQLite
Version   : 4.7
Licence   : MIT
Canal     : Godot Asset Library
Dépôt     : https://github.com/2shady4u/godot-sqlite
Plateforme de référence : Windows 11 x86_64
```

Le dépôt annonce une compatibilité Godot 4.x et fournit des bibliothèques précompilées pour Windows, Linux, macOS et plusieurs plateformes mobiles.

L’extension expose notamment :

- la classe `SQLite` ;
- `open_db()` et `close_db()` ;
- `query()` ;
- `query_with_bindings()` ;
- `query_with_named_bindings()` ;
- `query_result` ;
- `error_message` ;
- `last_insert_rowid` ;
- l’option `foreign_keys`.

### 6.3 Politique de dépendance

L’addon doit être :

- épinglé à une version précise ;
- conservé dans `addons/` ;
- accompagné de sa licence ;
- qualifié sur chaque plateforme exportée ;
- mis à jour dans une pull request dédiée ;
- caché derrière un adaptateur du projet.

Le code métier ne doit jamais instancier `SQLite.new()` directement.

### 6.4 Réserve de compatibilité

La version de référence du guide est Godot `4.7.1-stable`. L’entrée de l’Asset Library de Godot-SQLite `4.7` déclare Godot 4.5 comme version de soumission.

Cela ne constitue pas à lui seul une preuve d’exécution avec Godot 4.7.1. Le chapitre reste donc au niveau `static-review` jusqu’au test du Starter Kit sur Windows 11.

## 7. Installer et vérifier l’addon

### 7.1 Installation par l’éditeur

> **[APP] Godot — Installer l’addon depuis l’onglet AssetLib ou Asset Store selon le libellé de l’éditeur.**

1. ouvrir `Project Asteria` ;
2. ouvrir l’onglet de bibliothèque d’assets ;
3. rechercher `Godot-SQLite` ;
4. vérifier l’auteur `2shady4u` ;
5. sélectionner la version `4.7` ;
6. lire la licence MIT ;
7. télécharger puis installer le contenu dans `res://addons/` ;
8. ouvrir **Project > Project Settings > Plugins** ;
9. activer l’addon si l’installation fournit un plugin éditeur ;
10. redémarrer l’éditeur si la bibliothèque native n’est pas chargée immédiatement.

Certaines extensions runtime ne nécessitent pas de plugin éditeur actif. Le critère réel est la présence de la classe native et le chargement de la ressource `.gdextension`.

### 7.2 Vérifier les fichiers

> **[PS] PowerShell 7 — Depuis la racine du projet Godot matérialisé.**

```powershell
Get-ChildItem -Recurse .\addons | Where-Object {
    $_.Name -match 'sqlite|gdextension|dll'
} | Select-Object FullName, Length
```

Le résultat doit montrer :

- une ressource `.gdextension` ;
- une bibliothèque Windows x86_64 ;
- les scripts ou fichiers de documentation de l’addon ;
- le texte de licence fourni par l’auteur.

### 7.3 Test de présence de la classe

> **[VSC] Visual Studio Code — Créer temporairement dans le Starter Kit :** `res://scenes/learning/ch08_sqlite_smoke_test.gd`.

```gdscript
extends Node

func _ready() -> void:
	if not ClassDB.class_exists(&"SQLite"):
		push_error("La classe SQLite n’est pas chargée.")
		get_tree().quit(1)
		return

	print("SQLite GDExtension chargée.")
	get_tree().quit(0)
```

`ClassDB.class_exists()` reçoit le nom d’une classe enregistrée par le moteur ou une extension. Le préfixe `&` crée un `StringName`.

> **[PS] PowerShell 7 — Exécuter la scène de test depuis la racine du projet.**

```powershell
godot --headless --path . scenes/learning/ch08_sqlite_smoke_test.tscn
```

> **[SORTIE] Résultat attendu — Ne pas saisir.**

```text
SQLite GDExtension chargée.
```

Ce test sera réellement exécuté lors de la matérialisation du Starter Kit.

## 8. Arborescence cible

> **[LECTURE] Arborescence de référence — Ne pas saisir.**

```text
addons/
  godot-sqlite/
src/
  app/
    database_bootstrap.gd
  core/
    persistence/
      database_connection.gd
      sqlite_database_connection.gd
      database_backup_service.gd
      sql_migration_runner.gd
  features/
    beacons/
      application/
        beacon_state_record.gd
        beacon_state_repository.gd
        beacon_persistence_service.gd
      infrastructure/
        sqlite_beacon_state_repository.gd
data/
  sql/
    migrations/
      001_create_beacon_state.sql
      002_add_beacon_activation_event.sql
scenes/
  learning/
    ch08_sqlite_demo.gd
    ch08_sqlite_demo.tscn
```

Les fichiers `.sql` sont des données non natives de Godot. L’export Windows devra inclure `*.sql` dans le filtre des fichiers non-ressources.

## 9. Modéliser les données relationnelles

### 9.1 Une ligne par état de balise

La table `beacon_state` conserve :

- l’identifiant stable de la définition ;
- l’état actif ou inactif ;
- le nombre d’activations ;
- le délai restant ;
- la date de dernière activation ;
- la date de dernière mise à jour.

Elle ne conserve pas :

- `display_name` ;
- `description` ;
- `activation_radius` ;
- `cooldown_seconds` ;
- `tags`.

Ces valeurs restent dans les `BeaconProfile` versionnés.

### 9.2 Un historique dépendant

La table `beacon_activation_event` conserve plusieurs événements par balise. Sa clé étrangère référence `beacon_state.beacon_id`.

Cette relation illustre :

- une relation un-à-plusieurs ;
- l’intégrité référentielle ;
- la suppression en cascade ;
- l’intérêt d’un index sur la clé étrangère.

## 10. Types SQLite et types Godot

SQLite associe principalement un type à chaque valeur. Les colonnes possèdent une affinité plutôt qu’un type rigide dans les tables ordinaires.

> **[LECTURE] Correspondances utilisées dans ce chapitre — Ne pas saisir.**

```text
SQLite INTEGER  → GDScript int
SQLite REAL     → GDScript float
SQLite TEXT     → GDScript String ou StringName après conversion
SQLite BLOB     → GDScript PackedByteArray
SQLite NULL     → GDScript null
Booléen         → INTEGER avec CHECK (0 ou 1)
Date UTC        → TEXT ISO 8601
```

### 10.1 Booléens

SQLite ne possède pas une classe de stockage booléenne distincte. Le projet utilise `0` et `1`, puis impose :

> **[LECTURE] Fragment SQL de contrainte — Ne pas exécuter isolément.**

```sql
is_enabled INTEGER NOT NULL CHECK (is_enabled IN (0, 1))
```

### 10.2 Dates

Le projet stocke une chaîne UTC au format ISO 8601 :

> **[LECTURE] Exemple de valeur persistée — Ne pas saisir.**

```text
2026-07-19T10:15:30
```

> **[LECTURE] Exemple GDScript — Création d’une chaîne UTC.**

```gdscript
var utc_now := Time.get_datetime_string_from_system(true, false)
```

Le premier argument `true` demande l’UTC. Le second `false` conserve la lettre `T` entre date et heure.

L’horloge système peut être modifiée. Elle convient à une trace civile, pas à la mesure précise d’une durée de gameplay. Les durées courtes utilisent toujours `delta` ou les compteurs monotones.

### 10.3 Montants et précision

Un nombre `REAL` utilise une représentation flottante. Les monnaies exactes du système économique devront préférer un entier exprimé dans la plus petite unité, par exemple des centimes, lorsque les règles exigent une arithmétique exacte.

## 11. Première migration SQL

> **[VSC] Visual Studio Code — Créer :** `res://data/sql/migrations/001_create_beacon_state.sql`.

```sql
CREATE TABLE beacon_state (
    beacon_id TEXT PRIMARY KEY NOT NULL,
    is_enabled INTEGER NOT NULL DEFAULT 1
        CHECK (is_enabled IN (0, 1)),
    activation_count INTEGER NOT NULL DEFAULT 0
        CHECK (activation_count >= 0),
    cooldown_remaining REAL NOT NULL DEFAULT 0.0
        CHECK (cooldown_remaining >= 0.0),
    last_activated_at_utc TEXT,
    updated_at_utc TEXT NOT NULL
);

CREATE INDEX idx_beacon_state_updated_at
    ON beacon_state(updated_at_utc);
```

### 11.1 `PRIMARY KEY`

`beacon_id` est la clé primaire. Elle identifie une ligne de façon unique et reprend l’identifiant stable du `BeaconProfile`.

Le chemin de la ressource n’est pas utilisé comme clé. Une ressource peut être déplacée sans changer son identité métier.

### 11.2 `NOT NULL`

`NOT NULL` interdit l’absence d’une valeur indispensable.

Une chaîne vide reste toutefois une chaîne valide pour SQLite. Le projet contrôle aussi `StableId` avant l’écriture.

### 11.3 `CHECK`

`CHECK` protège les invariants simples directement dans la base :

- booléen limité à `0` ou `1` ;
- compteur non négatif ;
- délai non négatif.

Le modèle GDScript valide avant l’écriture, et la base valide une seconde fois à sa frontière.

### 11.4 Index de date

L’index `idx_beacon_state_updated_at` accélère les recherches ordonnées ou filtrées par date de mise à jour.

Un index a un coût :

- espace disque ;
- mise à jour supplémentaire à chaque écriture ;
- maintenance lors des migrations.

Ne pas indexer chaque colonne par réflexe.

## 12. Deuxième migration SQL

> **[VSC] Visual Studio Code — Créer :** `res://data/sql/migrations/002_add_beacon_activation_event.sql`.

```sql
CREATE TABLE beacon_activation_event (
    event_id INTEGER PRIMARY KEY,
    beacon_id TEXT NOT NULL,
    actor_id TEXT NOT NULL,
    occurred_at_utc TEXT NOT NULL,
    FOREIGN KEY (beacon_id)
        REFERENCES beacon_state(beacon_id)
        ON DELETE CASCADE
);

CREATE INDEX idx_beacon_activation_event_beacon_time
    ON beacon_activation_event(beacon_id, occurred_at_utc);
```

### 12.1 `INTEGER PRIMARY KEY`

Dans SQLite, une colonne déclarée exactement `INTEGER PRIMARY KEY` correspond à la clé entière interne de la ligne.

Le mot-clé `AUTOINCREMENT` n’est pas nécessaire ici. Il impose une politique plus stricte de non-réutilisation et ajoute un coût. Le projet n’en a pas besoin pour un identifiant technique d’événement.

### 12.2 Clé étrangère

La clé étrangère interdit un événement lié à une balise absente de `beacon_state`.

L’option `ON DELETE CASCADE` supprime les événements dépendants lorsque l’état parent est supprimé.

Cette décision doit être explicite. Pour un historique légal ou d’audit, une suppression en cascade pourrait être inacceptable.

### 12.3 Index composite

L’index commence par `beacon_id`, puis `occurred_at_utc`. Il convient à une requête qui recherche l’historique d’une balise et le trie par date.

L’ordre des colonnes d’un index composite influence les requêtes qui peuvent l’utiliser efficacement.

## 13. Contrat de connexion indépendant de l’addon

> **[VSC] Visual Studio Code — Créer :** `res://src/core/persistence/database_connection.gd`.

```gdscript
class_name DatabaseConnection
extends RefCounted

func open(_path: String) -> Error:
	push_error("DatabaseConnection.open() doit être redéfinie.")
	return ERR_UNAVAILABLE

func close() -> void:
	pass

func execute(_sql: String, _bindings: Array = []) -> Error:
	push_error("DatabaseConnection.execute() doit être redéfinie.")
	return ERR_UNAVAILABLE

func query(_sql: String, _bindings: Array = []) -> Array[Dictionary]:
	push_error("DatabaseConnection.query() doit être redéfinie.")
	var rows: Array[Dictionary] = []
	return rows

func last_error_code() -> Error:
	return ERR_UNAVAILABLE

func last_error_message() -> String:
	return "Connexion non configurée"
```

### 13.1 Pourquoi un contrat

Les consommateurs utilisent `DatabaseConnection`, pas `SQLite`.

Cela permet :

- de remplacer l’addon ;
- de créer une fausse connexion pour certains tests ;
- de centraliser les paramètres ;
- d’empêcher le SQL de se disperser dans toutes les scènes ;
- de limiter la dépendance native à l’infrastructure.

### 13.2 Paramètres préfixés par `_`

`_path`, `_sql` et `_bindings` indiquent que la classe de base ne les utilise pas. Les sous-classes les utilisent réellement.

`last_error_code()` distingue une requête réussie sans ligne d’une requête qui a échoué. `last_error_message()` fournit le diagnostic humain complémentaire. Un tableau vide ne doit jamais être interprété seul.

## 14. Adaptateur Godot-SQLite

> **[VSC] Visual Studio Code — Créer :** `res://src/core/persistence/sqlite_database_connection.gd`.

```gdscript
class_name SqliteDatabaseConnection
extends DatabaseConnection

const SQLITE_CLASS := &"SQLite"
const SQLITE_VERBOSITY_NORMAL := 1
const BUSY_TIMEOUT_MS := 3000

var _sqlite: Object
var _last_error_code: Error = OK
var _last_error_message: String = ""

func open(path: String) -> Error:
	if _sqlite != null:
		return _fail(ERR_ALREADY_IN_USE, "Une connexion est déjà ouverte.")

	if not ClassDB.class_exists(SQLITE_CLASS):
		return _fail(ERR_CANT_OPEN, "La classe SQLite est absente.")
	if not ClassDB.can_instantiate(SQLITE_CLASS):
		return _fail(ERR_CANT_OPEN, "La classe SQLite ne peut pas être instanciée.")

	var directory_error := DirAccess.make_dir_recursive_absolute(
		path.get_base_dir()
	)
	if directory_error != OK and directory_error != ERR_ALREADY_EXISTS:
		return _fail(
			directory_error,
			"Impossible de créer le dossier de la base."
		)

	var instance: Variant = ClassDB.instantiate(SQLITE_CLASS)
	if not instance is Object:
		return _fail(ERR_CANT_CREATE, "Instanciation SQLite impossible.")

	_sqlite = instance as Object
	_sqlite.set("path", path)
	_sqlite.set("foreign_keys", true)
	_sqlite.set("verbosity_level", SQLITE_VERBOSITY_NORMAL)

	if not bool(_sqlite.call("open_db")):
		var message := _read_native_error()
		_sqlite = null
		return _fail(ERR_CANT_OPEN, message)

	var error := execute(
		"PRAGMA busy_timeout = %d;" % BUSY_TIMEOUT_MS
	)
	if error != OK:
		close()
		return error

	var journal_rows := query("PRAGMA journal_mode = WAL;")
	if last_error_code() != OK:
		close()
		return _last_error_code
	if journal_rows.size() != 1 or not journal_rows[0].has("journal_mode"):
		close()
		return _fail(FAILED, "SQLite n’a pas confirmé le journal WAL.")
	if String(journal_rows[0]["journal_mode"]).to_lower() != "wal":
		close()
		return _fail(ERR_UNAVAILABLE, "Le mode WAL n’est pas disponible.")

	error = execute("PRAGMA synchronous = FULL;")
	if error != OK:
		close()
		return error

	error = execute("PRAGMA foreign_keys = ON;")
	if error != OK:
		close()
		return error

	var foreign_key_rows := query("PRAGMA foreign_keys;")
	if last_error_code() != OK:
		close()
		return _last_error_code
	if foreign_key_rows.size() != 1:
		close()
		return _fail(FAILED, "État des clés étrangères illisible.")
	if int(foreign_key_rows[0].get("foreign_keys", 0)) != 1:
		close()
		return _fail(FAILED, "Les clés étrangères ne sont pas actives.")

	_clear_error()
	return OK

func close() -> void:
	if _sqlite == null:
		return

	if not bool(_sqlite.call("close_db")):
		_last_error_code = FAILED
		_last_error_message = _read_native_error()
		push_warning(
			"Fermeture SQLite incomplète : %s" % _last_error_message
		)

	_sqlite = null

func execute(sql: String, bindings: Array = []) -> Error:
	if _sqlite == null:
		return _fail(ERR_UNCONFIGURED, "La base n’est pas ouverte.")

	var success := false
	if bindings.is_empty():
		success = bool(_sqlite.call("query", sql))
	else:
		success = bool(
			_sqlite.call("query_with_bindings", sql, bindings)
		)

	if not success:
		return _fail(FAILED, _read_native_error())

	_clear_error()
	return OK

func query(sql: String, bindings: Array = []) -> Array[Dictionary]:
	var rows: Array[Dictionary] = []
	var error := execute(sql, bindings)
	if error != OK:
		return rows

	var native_result: Variant = _sqlite.get("query_result")
	if not native_result is Array:
		_fail(ERR_INVALID_DATA, "Résultat SQLite non tabulaire.")
		return rows

	for value: Variant in native_result as Array:
		if value is Dictionary:
			rows.append((value as Dictionary).duplicate(true))
		else:
			_fail(ERR_INVALID_DATA, "Ligne SQLite non mappée.")
			return []

	_clear_error()
	return rows

func last_error_code() -> Error:
	return _last_error_code

func last_error_message() -> String:
	return _last_error_message

func _read_native_error() -> String:
	if _sqlite == null:
		return "Connexion SQLite absente."
	return String(_sqlite.get("error_message"))

func _fail(code: Error, message: String) -> Error:
	_last_error_code = code
	_last_error_message = message
	push_error("SQLite : %s" % message)
	return code

func _clear_error() -> void:
	_last_error_code = OK
	_last_error_message = ""
```

### 14.1 `foreign_keys` avant l’ouverture

L’addon demande d’activer `foreign_keys` avant `open_db()`. L’adaptateur crée la classe native par `ClassDB.instantiate()` afin de pouvoir diagnostiquer proprement son absence sans référencer statiquement le type tiers. Il exécute aussi `PRAGMA foreign_keys = ON` après l’ouverture et vérifie que la valeur lue vaut `1`.

SQLite active les clés étrangères par connexion. Une seconde connexion doit donc recevoir la même configuration.

### 14.2 `busy_timeout`

SQLite ne permet qu’un écrivain simultané. Une écriture peut rencontrer une base momentanément verrouillée.

`busy_timeout` demande à SQLite d’attendre jusqu’à trois secondes avant d’abandonner. Cette valeur est un point de départ, pas une garantie de performance.

### 14.3 Mode WAL

Le mode WAL utilise un journal d’écriture séparé. Il améliore généralement la coexistence entre lectures et écriture. L’adaptateur lit le résultat de `PRAGMA journal_mode = WAL` et refuse de poursuivre si SQLite ne confirme pas réellement `wal`.

Le projet conserve `synchronous = FULL` comme défaut prudent. Une réduction vers `NORMAL` doit être justifiée par des mesures et une politique explicite de durabilité.

### 14.4 `query_result`

L’addon expose le résultat de la dernière requête sous forme de tableau de dictionnaires. L’adaptateur duplique les dictionnaires valides dans un tableau typé et conserve séparément le dernier code d’erreur.

Aucun dictionnaire brut ne doit quitter l’infrastructure pour atteindre directement le gameplay.

## 15. Requêtes paramétrées

Une valeur provenant du joueur, d’un fichier, d’une API ou d’un système de jeu ne doit pas être concaténée dans une chaîne SQL.

> **[LECTURE] Forme correcte d’une requête paramétrée — Ne pas exécuter isolément.**

```gdscript
var rows := database.query(
	"SELECT * FROM beacon_state WHERE beacon_id = ?;",
	[String(profile_id)]
)
```

Le caractère `?` est un paramètre positionnel. Le tableau fournit sa valeur.

Les paramètres protègent :

- les apostrophes dans les chaînes ;
- les conversions de types ;
- les données binaires ;
- les requêtes contre l’injection de contenu dans la structure SQL.

Ils ne peuvent pas remplacer un nom de table ou de colonne. Les identifiants SQL dynamiques doivent provenir d’une liste fermée contrôlée par le programme.

## 16. Transaction explicite

Une transaction regroupe plusieurs modifications en une unité atomique.

> **[LECTURE] Séquence transactionnelle — Ne pas saisir.**

```sql
BEGIN IMMEDIATE;
-- écritures cohérentes
COMMIT;
```

En cas d’échec :

> **[LECTURE] Séquence d’annulation — Ne pas saisir.**

```sql
ROLLBACK;
```

`BEGIN IMMEDIATE` tente d’obtenir le droit d’écriture dès le début. Il échoue tôt si une autre connexion écrit déjà, plutôt que d’attendre une opération située au milieu de la migration.

Les transactions `BEGIN ... COMMIT` ne s’imbriquent pas. Pour des niveaux internes, SQLite utilise des `SAVEPOINT`. Le présent chapitre évite les transactions imbriquées afin de conserver un cycle de vie prévisible.

## 17. Historique des migrations

Le projet utilise deux sources complémentaires :

- `PRAGMA user_version` pour connaître rapidement la version courante ;
- `schema_migrations` pour conserver le nom, la date et le checksum de chaque migration.

La table d’historique est créée par le runner avant les migrations métier.

> **[LECTURE] Schéma géré par le runner — Ne pas exécuter manuellement.**

```sql
CREATE TABLE IF NOT EXISTS schema_migrations (
    version INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    checksum TEXT NOT NULL,
    applied_at_utc TEXT NOT NULL
);
```

### 17.1 Pourquoi conserver un checksum

Une migration appliquée ne doit plus être modifiée silencieusement.

Le checksum détecte :

- une modification du SQL après livraison ;
- un fichier remplacé par erreur ;
- une branche qui réécrit l’historique ;
- une divergence entre deux postes.

La correction d’une ancienne migration consiste à ajouter une nouvelle migration, pas à réécrire l’ancienne.

## 18. Runner de migrations

> **[VSC] Visual Studio Code — Créer :** `res://src/core/persistence/sql_migration_runner.gd`.

```gdscript
class_name SqlMigrationRunner
extends RefCounted

const MIGRATIONS: Array[Dictionary] = [
	{
		"version": 1,
		"name": "create_beacon_state",
		"path": "res://data/sql/migrations/001_create_beacon_state.sql",
	},
	{
		"version": 2,
		"name": "add_beacon_activation_event",
		"path": "res://data/sql/migrations/002_add_beacon_activation_event.sql",
	},
]

var _database: DatabaseConnection

func configure(database: DatabaseConnection) -> void:
	_database = database

func latest_version() -> int:
	if MIGRATIONS.is_empty():
		return 0
	return int(MIGRATIONS[MIGRATIONS.size() - 1]["version"])

func current_version() -> int:
	if _database == null:
		return -1

	var rows := _database.query("PRAGMA user_version;")
	if _database.last_error_code() != OK:
		return -1
	if rows.size() != 1 or not rows[0].has("user_version"):
		push_error("PRAGMA user_version n’a pas retourné une ligne valide.")
		return -1

	return int(rows[0]["user_version"])

func migrate() -> Error:
	if _database == null:
		return ERR_UNCONFIGURED

	var error := _validate_manifest()
	if error != OK:
		return error

	var installed_version := current_version()
	if installed_version < 0:
		return FAILED
	if installed_version > latest_version():
		push_error(
			"Schéma plus récent que l’application : %d > %d"
			% [installed_version, latest_version()]
		)
		return ERR_INVALID_DATA

	error = _ensure_history_table()
	if error != OK:
		return error

	error = _verify_applied_migrations(installed_version)
	if error != OK:
		return error

	for migration: Dictionary in MIGRATIONS:
		var version := int(migration["version"])
		if version <= installed_version:
			continue

		error = _apply_migration(migration)
		if error != OK:
			return error

		installed_version = version

	return OK

func _validate_manifest() -> Error:
	var expected_version := 1
	var known_names: Dictionary[String, bool] = {}
	for migration: Dictionary in MIGRATIONS:
		var version := int(migration.get("version", -1))
		var name := String(migration.get("name", ""))
		var path := String(migration.get("path", ""))
		if version != expected_version:
			push_error("Version de migration attendue : %d" % expected_version)
			return ERR_INVALID_DATA
		if name.is_empty() or known_names.has(name):
			push_error("Nom de migration vide ou dupliqué : %s" % name)
			return ERR_INVALID_DATA
		if path.is_empty():
			push_error("Chemin de migration vide pour la version %d" % version)
			return ERR_INVALID_DATA

		known_names[name] = true
		expected_version += 1

	return OK

func _ensure_history_table() -> Error:
	return _database.execute(
		"""
		CREATE TABLE IF NOT EXISTS schema_migrations (
			version INTEGER PRIMARY KEY,
			name TEXT NOT NULL UNIQUE,
			checksum TEXT NOT NULL CHECK (length(checksum) = 64),
			applied_at_utc TEXT NOT NULL
		);
		"""
	)

func _verify_applied_migrations(installed_version: int) -> Error:
	var rows := _database.query(
		"""
		SELECT version, name, checksum
		FROM schema_migrations
		ORDER BY version;
		"""
	)
	if _database.last_error_code() != OK:
		return _database.last_error_code()

	var applied_by_version: Dictionary[int, Dictionary] = {}
	for row: Dictionary in rows:
		if not row.has("version"):
			return ERR_FILE_CORRUPT
		var version := int(row["version"])
		if version < 1 or version > installed_version:
			push_error("Historique incohérent pour la version %d" % version)
			return ERR_FILE_CORRUPT
		if applied_by_version.has(version):
			return ERR_FILE_CORRUPT
		applied_by_version[version] = row

	for migration: Dictionary in MIGRATIONS:
		var version := int(migration["version"])
		if version > installed_version:
			continue

		if not applied_by_version.has(version):
			push_error("Migration appliquée absente de l’historique : %d" % version)
			return ERR_FILE_CORRUPT

		var sql := _read_sql(String(migration["path"]))
		if sql.is_empty():
			return ERR_FILE_CANT_READ

		var expected_checksum := _sha256(sql)
		if expected_checksum.is_empty():
			return ERR_CANT_CREATE

		var stored := applied_by_version[version]
		if String(stored.get("name", "")) != String(migration["name"]):
			push_error("Nom divergent pour la migration %d" % version)
			return ERR_FILE_CORRUPT
		if String(stored.get("checksum", "")) != expected_checksum:
			push_error("Checksum divergent pour la migration %d" % version)
			return ERR_FILE_CORRUPT

	return OK

func _apply_migration(migration: Dictionary) -> Error:
	var version := int(migration["version"])
	var name := String(migration["name"])
	var path := String(migration["path"])
	var sql := _read_sql(path)
	if sql.is_empty():
		return ERR_FILE_CANT_READ

	var checksum := _sha256(sql)
	if checksum.is_empty():
		return ERR_CANT_CREATE

	var error := _database.execute("BEGIN IMMEDIATE;")
	if error != OK:
		return error

	error = _database.execute(sql)
	if error == OK:
		error = _database.execute(
			"""
			INSERT INTO schema_migrations(
				version,
				name,
				checksum,
				applied_at_utc
			)
			VALUES (?, ?, ?, ?);
			""",
			[
				version,
				name,
				checksum,
				Time.get_datetime_string_from_system(true, false),
			]
		)

	if error == OK:
		error = _database.execute(
			"PRAGMA user_version = %d;" % version
		)

	if error == OK:
		error = _database.execute("COMMIT;")
		if error == OK:
			return OK

	var rollback_error := _database.execute("ROLLBACK;")
	if rollback_error != OK:
		push_error("ROLLBACK impossible après l’échec de migration.")

	return error if error != OK else FAILED

func _read_sql(path: String) -> String:
	if not FileAccess.file_exists(path):
		push_error("Migration absente : %s" % path)
		return ""

	var file := FileAccess.open(path, FileAccess.READ)
	if file == null:
		push_error("Migration illisible : %s" % path)
		return ""

	var sql := file.get_as_text().strip_edges()
	file.close()
	return sql

func _sha256(text: String) -> String:
	var context := HashingContext.new()
	var error := context.start(HashingContext.HASH_SHA256)
	if error != OK:
		push_error("Initialisation SHA-256 impossible.")
		return ""

	error = context.update(text.to_utf8_buffer())
	if error != OK:
		push_error("Calcul SHA-256 impossible.")
		return ""

	return context.finish().hex_encode()
```

### 18.1 Ordre des migrations

La liste est triée par version croissante. `_validate_manifest()` impose ici une séquence continue à partir de `1`, ainsi que des noms uniques et des chemins non vides. Une version ne doit jamais être réutilisée.

Convention :

> **[LECTURE] Convention de nommage — Ne pas saisir.**

```text
NNN_verbe_objet.sql
001_create_beacon_state.sql
002_add_beacon_activation_event.sql
003_add_world_region.sql
```

### 18.2 SQL multiligne

L’adaptateur transmet le fichier complet à `query()`. Dans l’implémentation relue de Godot-SQLite, `query_with_bindings()` prépare une première instruction avec `sqlite3_prepare_v2`, exécute celle-ci, puis traite récursivement la queue SQL `pzTail` tant qu’elle n’est pas vide. Une migration multi-instructions est donc prise en charge par cette version de l’addon.

Une migration ne reçoit aucune donnée utilisateur. Les valeurs dynamiques de l’historique utilisent toutefois des paramètres liés.

### 18.3 Échec et rollback

Si une étape échoue :

1. aucune nouvelle version n’est enregistrée ;
2. le runner demande `ROLLBACK` ;
3. l’erreur remonte au bootstrap ;
4. le gameplay ne démarre pas avec un schéma partiellement migré.

## 19. Copie de sécurité avant migration

Une transaction protège les changements SQL de la migration. Une copie séparée protège contre :

- une migration destructrice pourtant valide ;
- une erreur logique non détectée ;
- un addon ou disque défaillant ;
- un besoin de retour à la version précédente de l’application.

La copie simple d’un fichier ouvert en mode WAL n’est pas sûre. Lorsqu’une migration est réellement nécessaire, le projet doit :

1. ouvrir la base ;
2. demander un checkpoint ;
3. fermer toutes les connexions ;
4. copier le fichier principal ;
5. rouvrir la base ;
6. appliquer les migrations.

> **[VSC] Visual Studio Code — Créer :** `res://src/core/persistence/database_backup_service.gd`.

```gdscript
class_name DatabaseBackupService
extends RefCounted

const SIDE_CAR_SUFFIXES: PackedStringArray = ["-wal", "-shm"]

func create_closed_copy(database_path: String) -> String:
	if not FileAccess.file_exists(database_path):
		return ""

	var backup_dir := "user://backups/database"
	var directory_error := DirAccess.make_dir_recursive_absolute(backup_dir)
	if directory_error != OK and directory_error != ERR_ALREADY_EXISTS:
		push_error("Impossible de créer le dossier de sauvegarde technique.")
		return ""

	var unix_seconds := int(Time.get_unix_time_from_system())
	var millisecond_part := Time.get_ticks_msec() % 1000
	var backup_path := "%s/asteria-pre-migration-%d-%03d.sqlite3" % [
		backup_dir,
		unix_seconds,
		millisecond_part,
	]
	var copy_error := DirAccess.copy_absolute(database_path, backup_path)
	if copy_error != OK:
		push_error("Copie de sécurité impossible : %s" % error_string(copy_error))
		return ""

	return backup_path

func restore_closed_copy(backup_path: String, database_path: String) -> Error:
	if not FileAccess.file_exists(backup_path):
		return ERR_FILE_NOT_FOUND

	for suffix: String in SIDE_CAR_SUFFIXES:
		var side_car_path := database_path + suffix
		if FileAccess.file_exists(side_car_path):
			var remove_error := DirAccess.remove_absolute(side_car_path)
			if remove_error != OK:
				return remove_error

	return DirAccess.copy_absolute(backup_path, database_path)
```

`DirAccess.copy_absolute()` accepte `user://` comme chemin absolu dans la portée Godot.

Cette classe exige que toutes les connexions soient fermées. Le nom de méthode le rappelle explicitement. La restauration supprime aussi les anciens fichiers auxiliaires `-wal` et `-shm` afin qu’ils ne soient jamais rejoués sur la copie restaurée.

## 20. Objet typé persistant

> **[VSC] Visual Studio Code — Créer :** `res://src/features/beacons/application/beacon_state_record.gd`.

```gdscript
class_name BeaconStateRecord
extends RefCounted

var profile_id: StringName
var is_enabled: bool
var activation_count: int
var cooldown_remaining: float
var last_activated_at_utc: String
var updated_at_utc: String

func _init(
	p_profile_id: StringName = &"",
	p_is_enabled: bool = true,
	p_activation_count: int = 0,
	p_cooldown_remaining: float = 0.0,
	p_last_activated_at_utc: String = "",
	p_updated_at_utc: String = ""
) -> void:
	profile_id = p_profile_id
	is_enabled = p_is_enabled
	activation_count = maxi(0, p_activation_count)
	cooldown_remaining = maxf(0.0, p_cooldown_remaining)
	last_activated_at_utc = p_last_activated_at_utc
	updated_at_utc = p_updated_at_utc

static func from_runtime(
	state: BeaconRuntimeState,
	last_activated_at_utc: String = ""
) -> BeaconStateRecord:
	return BeaconStateRecord.new(
		state.profile_id,
		state.is_enabled,
		state.activation_count,
		state.cooldown_remaining,
		last_activated_at_utc,
		Time.get_datetime_string_from_system(true, false)
	)

func apply_to(state: BeaconRuntimeState) -> Error:
	if state.profile_id != profile_id:
		return ERR_INVALID_PARAMETER

	state.is_enabled = is_enabled
	state.activation_count = maxi(0, activation_count)
	state.cooldown_remaining = maxf(0.0, cooldown_remaining)
	return OK
```

Le record représente le contrat de persistance de la fonctionnalité. Il ne contient aucun dictionnaire SQLite.

`from_runtime()` capture les valeurs nécessaires. `apply_to()` refuse d’appliquer une ligne à une balise d’un autre identifiant.

## 21. Contrat du dépôt

> **[VSC] Visual Studio Code — Créer :** `res://src/features/beacons/application/beacon_state_repository.gd`.

```gdscript
class_name BeaconStateRepository
extends RefCounted

func save(_record: BeaconStateRecord) -> Error:
	return ERR_UNAVAILABLE

func find(_profile_id: StringName) -> BeaconStateRecord:
	return null

func list_all() -> Array[BeaconStateRecord]:
	var records: Array[BeaconStateRecord] = []
	return records

func delete(_profile_id: StringName) -> Error:
	return ERR_UNAVAILABLE

func last_error_code() -> Error:
	return ERR_UNAVAILABLE
```

Le contrat appartient à la fonctionnalité `beacons`. L’implémentation SQLite appartient à son infrastructure.

Le nom `Repository` désigne ici une collection persistante d’objets métier. Il ne désigne ni un dépôt Git, ni un Service Locator. `last_error_code()` permet au service de distinguer `ERR_DOES_NOT_EXIST` d’une panne de lecture.

## 22. Dépôt SQLite des balises

> **[VSC] Visual Studio Code — Créer :** `res://src/features/beacons/infrastructure/sqlite_beacon_state_repository.gd`.

```gdscript
class_name SqliteBeaconStateRepository
extends BeaconStateRepository

const UPSERT_SQL := """
INSERT INTO beacon_state(
	beacon_id,
	is_enabled,
	activation_count,
	cooldown_remaining,
	last_activated_at_utc,
	updated_at_utc
)
VALUES (?, ?, ?, ?, ?, ?)
ON CONFLICT(beacon_id) DO UPDATE SET
	is_enabled = excluded.is_enabled,
	activation_count = excluded.activation_count,
	cooldown_remaining = excluded.cooldown_remaining,
	last_activated_at_utc = excluded.last_activated_at_utc,
	updated_at_utc = excluded.updated_at_utc;
"""

var _database: DatabaseConnection
var _last_error_code: Error = OK

func configure(database: DatabaseConnection) -> void:
	_database = database
	_last_error_code = OK if database != null else ERR_UNCONFIGURED

func save(record: BeaconStateRecord) -> Error:
	if _database == null:
		return _set_error(ERR_UNCONFIGURED)
	if record == null or not StableId.is_valid(record.profile_id):
		return _set_error(ERR_INVALID_PARAMETER)

	return _set_error(
		_database.execute(
			UPSERT_SQL,
			[
				String(record.profile_id),
				int(record.is_enabled),
				record.activation_count,
				record.cooldown_remaining,
				record.last_activated_at_utc,
				record.updated_at_utc,
			]
		)
	)

func find(profile_id: StringName) -> BeaconStateRecord:
	if _database == null:
		_set_error(ERR_UNCONFIGURED)
		return null
	if not StableId.is_valid(profile_id):
		_set_error(ERR_INVALID_PARAMETER)
		return null

	var rows := _database.query(
		"""
		SELECT
			beacon_id,
			is_enabled,
			activation_count,
			cooldown_remaining,
			last_activated_at_utc,
			updated_at_utc
		FROM beacon_state
		WHERE beacon_id = ?;
		""",
		[String(profile_id)]
	)
	if _database.last_error_code() != OK:
		_set_error(_database.last_error_code())
		return null
	if rows.is_empty():
		_set_error(ERR_DOES_NOT_EXIST)
		return null
	if rows.size() != 1:
		_set_error(ERR_FILE_CORRUPT)
		return null

	var record := _map_row(rows[0])
	_set_error(OK if record != null else ERR_FILE_CORRUPT)
	return record

func list_all() -> Array[BeaconStateRecord]:
	var records: Array[BeaconStateRecord] = []
	if _database == null:
		_set_error(ERR_UNCONFIGURED)
		return records

	var rows := _database.query(
		"""
		SELECT
			beacon_id,
			is_enabled,
			activation_count,
			cooldown_remaining,
			last_activated_at_utc,
			updated_at_utc
		FROM beacon_state
		ORDER BY beacon_id;
		"""
	)
	if _database.last_error_code() != OK:
		_set_error(_database.last_error_code())
		return records

	for row: Dictionary in rows:
		var record := _map_row(row)
		if record == null:
			_set_error(ERR_FILE_CORRUPT)
			return []
		records.append(record)

	_set_error(OK)
	return records

func delete(profile_id: StringName) -> Error:
	if _database == null:
		return _set_error(ERR_UNCONFIGURED)
	if not StableId.is_valid(profile_id):
		return _set_error(ERR_INVALID_PARAMETER)

	return _set_error(
		_database.execute(
			"DELETE FROM beacon_state WHERE beacon_id = ?;",
			[String(profile_id)]
		)
	)

func last_error_code() -> Error:
	return _last_error_code

func _set_error(code: Error) -> Error:
	_last_error_code = code
	return code

func _map_row(row: Dictionary) -> BeaconStateRecord:
	var required: PackedStringArray = [
		"beacon_id",
		"is_enabled",
		"activation_count",
		"cooldown_remaining",
		"updated_at_utc",
	]
	for key: String in required:
		if not row.has(key):
			push_error("Colonne SQLite absente : %s" % key)
			return null

	var profile_id := StringName(String(row["beacon_id"]))
	if not StableId.is_valid(profile_id):
		push_error("Identifiant persistant invalide : %s" % profile_id)
		return null

	return BeaconStateRecord.new(
		profile_id,
		int(row["is_enabled"]) != 0,
		int(row["activation_count"]),
		float(row["cooldown_remaining"]),
		String(row.get("last_activated_at_utc", "")),
		String(row["updated_at_utc"])
	)
```

### 22.1 `UPSERT`

`INSERT ... ON CONFLICT ... DO UPDATE` crée la ligne si elle n’existe pas et met à jour les colonnes mutables sinon.

`excluded` représente les valeurs proposées par l’insertion qui a rencontré le conflit.

### 22.2 Conversion du booléen

`int(record.is_enabled)` produit `1` ou `0`.

Lors de la lecture, `int(row["is_enabled"]) != 0` produit un `bool`.

### 22.3 Validation à la lecture

La base peut provenir d’une ancienne version ou avoir été modifiée par un outil externe. Le mapper vérifie donc :

- la présence des colonnes obligatoires ;
- la syntaxe de l’identifiant ;
- les conversions de types ;
- les bornes dans le constructeur du record ;
- le code d’erreur de la connexion, afin qu’un tableau vide valide ne masque jamais une panne SQL.

## 23. Service applicatif

> **[VSC] Visual Studio Code — Créer :** `res://src/features/beacons/application/beacon_persistence_service.gd`.

```gdscript
class_name BeaconPersistenceService
extends RefCounted

var _repository: BeaconStateRepository

func configure(repository: BeaconStateRepository) -> void:
	_repository = repository

func persist_runtime_state(
	state: BeaconRuntimeState,
	last_activated_at_utc: String = ""
) -> Error:
	if _repository == null or state == null:
		return ERR_UNCONFIGURED

	var record := BeaconStateRecord.from_runtime(
		state,
		last_activated_at_utc
	)
	return _repository.save(record)

func restore_runtime_state(state: BeaconRuntimeState) -> Error:
	if _repository == null or state == null:
		return ERR_UNCONFIGURED

	var record := _repository.find(state.profile_id)
	if record == null:
		return _repository.last_error_code()

	return record.apply_to(state)
```

Le service ignore SQL et SQLite. Il reçoit un dépôt injecté depuis le bootstrap. Lorsqu’une recherche retourne `null`, il propage le code du dépôt : `ERR_DOES_NOT_EXIST` reste distinct d’une erreur de requête ou d’une ligne corrompue.

Il ne sauvegarde pas à chaque image. L’application choisit des points cohérents :

- activation acceptée ;
- changement durable d’état ;
- checkpoint de simulation ;
- fermeture propre ;
- future capture de sauvegarde du chapitre 9.

## 24. Bootstrap de la base

> **[VSC] Visual Studio Code — Créer :** `res://src/app/database_bootstrap.gd`.

```gdscript
class_name DatabaseBootstrap
extends RefCounted

const DATABASE_PATH := "user://data/asteria.sqlite3"

var database := SqliteDatabaseConnection.new()
var migration_runner := SqlMigrationRunner.new()
var backup_service := DatabaseBackupService.new()
var beacon_repository := SqliteBeaconStateRepository.new()
var beacon_persistence := BeaconPersistenceService.new()
var last_backup_path: String = ""

func start() -> Error:
	var database_exists := FileAccess.file_exists(DATABASE_PATH)

	var error := database.open(DATABASE_PATH)
	if error != OK:
		return error

	migration_runner.configure(database)
	var installed_version := migration_runner.current_version()
	if installed_version < 0:
		database.close()
		return FAILED

	var migration_pending := (
		installed_version < migration_runner.latest_version()
	)
	if database_exists and migration_pending:
		error = database.execute("PRAGMA wal_checkpoint(TRUNCATE);")
		if error != OK:
			database.close()
			return error

		database.close()
		last_backup_path = backup_service.create_closed_copy(DATABASE_PATH)
		if last_backup_path.is_empty():
			return ERR_CANT_CREATE

		error = database.open(DATABASE_PATH)
		if error != OK:
			return error
		migration_runner.configure(database)

	error = migration_runner.migrate()
	if error != OK:
		database.close()
		return error

	error = _validate_integrity()
	if error != OK:
		database.close()
		return error

	beacon_repository.configure(database)
	beacon_persistence.configure(beacon_repository)
	return OK

func stop() -> void:
	database.close()

func _validate_integrity() -> Error:
	var quick_rows := database.query("PRAGMA quick_check;")
	if database.last_error_code() != OK:
		return database.last_error_code()
	if quick_rows.size() != 1:
		return ERR_FILE_CORRUPT
	if String(quick_rows[0].get("quick_check", "")) != "ok":
		return ERR_FILE_CORRUPT

	var foreign_key_rows := database.query("PRAGMA foreign_key_check;")
	if database.last_error_code() != OK:
		return database.last_error_code()
	if not foreign_key_rows.is_empty():
		push_error("Violation de clé étrangère détectée.")
		return ERR_FILE_CORRUPT

	return OK
```

### 24.1 Première création

Si la base n’existe pas, aucune copie préalable n’est nécessaire. L’ouverture crée le fichier, puis les migrations créent le schéma. Le runner lit `user_version` avant de créer ou modifier sa table d’historique. Il refuse ainsi une base dont le schéma est plus récent que la version maximale connue, sans écrire quoi que ce soit dans ce fichier futur.

### 24.2 Base existante

Lorsqu’une migration est en attente, le bootstrap :

1. ouvre la base pour permettre la récupération SQLite ;
2. lit `PRAGMA user_version` ;
3. force un checkpoint WAL ;
4. ferme la connexion ;
5. crée une copie et conserve son chemin ;
6. rouvre la base ;
7. applique les migrations ;
8. exécute `quick_check` et `foreign_key_check` ;
9. injecte le dépôt.

Si le schéma est déjà à jour, aucune nouvelle copie n’est créée, mais les checksums historiques et l’intégrité sont tout de même vérifiés.

### 24.3 Échec de démarrage

Le gameplay ne doit pas démarrer si :

- l’extension native est absente ;
- la base est illisible ;
- la copie préalable échoue ;
- une migration échoue ;
- un checksum diverge ;
- l’intégrité est invalide.

Un écran de diagnostic peut proposer de consulter les journaux ou de restaurer une copie. Il ne doit pas écraser automatiquement la seule base disponible.

## 25. Scène de démonstration

> **[VSC] Visual Studio Code — Créer :** `res://scenes/learning/ch08_sqlite_demo.gd`.

```gdscript
extends Node

const PROFILE_PATH := "res://data/beacons/beacon_training.tres"

var _bootstrap := DatabaseBootstrap.new()

func _ready() -> void:
	var error := _bootstrap.start()
	if error != OK:
		push_error("Démarrage SQLite impossible : %s" % error_string(error))
		get_tree().quit(1)
		return

	var profile := load(PROFILE_PATH) as BeaconProfile
	if profile == null:
		push_error("BeaconProfile de démonstration absent.")
		_bootstrap.stop()
		get_tree().quit(1)
		return

	var runtime_state := BeaconRuntimeState.new(profile)
	var restore_error := _bootstrap.beacon_persistence.restore_runtime_state(
		runtime_state
	)
	if restore_error == ERR_DOES_NOT_EXIST:
		error = _bootstrap.beacon_persistence.persist_runtime_state(
			runtime_state
		)
	elif restore_error != OK:
		error = restore_error

	if error == OK and runtime_state.can_activate():
		runtime_state.record_activation(profile.cooldown_seconds)
		error = _bootstrap.beacon_persistence.persist_runtime_state(
			runtime_state,
			Time.get_datetime_string_from_system(true, false)
		)

	if error == OK:
		print(
			"État persistant : %s, activations=%d"
			% [runtime_state.profile_id, runtime_state.activation_count]
		)
	else:
		push_error("Persistance impossible : %s" % error_string(error))

	_bootstrap.stop()
	get_tree().quit(0 if error == OK else 1)
```

> **[SORTIE] Exemple de sortie attendue — Ne pas saisir.**

```text
État persistant : beacon.training, activations=1
```

Au second lancement, le compteur doit augmenter à partir de la valeur précédente.

Cette observation reste une attente documentaire tant que le Starter Kit n’est pas matérialisé.

## 26. Ajouter un événement dans la même transaction

Une activation peut mettre à jour l’état courant et ajouter une ligne d’historique. Les deux écritures doivent réussir ensemble.

> **[LECTURE] Exemple de méthode infrastructure à adapter — Ne pas recopier sans l’intégrer au dépôt.**

```gdscript
func record_activation(
	record: BeaconStateRecord,
	actor_id: StringName
) -> Error:
	if record == null:
		return ERR_INVALID_PARAMETER
	if not StableId.is_valid(record.profile_id):
		return ERR_INVALID_PARAMETER
	if not StableId.is_valid(actor_id):
		return ERR_INVALID_PARAMETER
	if record.last_activated_at_utc.is_empty():
		return ERR_INVALID_PARAMETER

	var error := _database.execute("BEGIN IMMEDIATE;")
	if error != OK:
		return error

	error = save(record)
	if error == OK:
		error = _database.execute(
			"""
			INSERT INTO beacon_activation_event(
				beacon_id,
				actor_id,
				occurred_at_utc
			)
			VALUES (?, ?, ?);
			""",
			[
				String(record.profile_id),
				String(actor_id),
				record.last_activated_at_utc,
			]
		)

	if error == OK:
		error = _database.execute("COMMIT;")
		if error == OK:
			return OK

	_database.execute("ROLLBACK;")
	return error if error != OK else FAILED
```

Le dépôt orchestre la transaction, car il connaît les deux opérations SQL. Il valide les deux identifiants et la date avant `BEGIN IMMEDIATE`, afin qu’une erreur de paramètre ne démarre aucune transaction. Le service applicatif demande une intention métier unique : enregistrer une activation.

## 27. Intégrité et diagnostic

### 27.1 Vérification rapide

> **[LECTURE] Requête de diagnostic — À exécuter uniquement par un outil de diagnostic contrôlé.**

```sql
PRAGMA quick_check;
```

Le résultat normal contient une ligne `ok`.

### 27.2 Vérification complète

> **[LECTURE] Requête de diagnostic — À exécuter hors boucle de gameplay.**

```sql
PRAGMA integrity_check;
```

Cette vérification examine notamment la structure des tables, index et pages. Elle peut être plus coûteuse.

### 27.3 Clés étrangères

`integrity_check` ne remplace pas la vérification des clés étrangères.

> **[LECTURE] Requête complémentaire — À exécuter par le diagnostic.**

```sql
PRAGMA foreign_key_check;
```

Un résultat vide signifie qu’aucune violation n’a été trouvée.

### 27.4 Vérifier l’activation

> **[LECTURE] Requête de contrôle de connexion — Ne pas saisir dans le gameplay.**

```sql
PRAGMA foreign_keys;
```

La valeur attendue est `1` pour chaque connexion.

### 27.5 Version SQLite

> **[LECTURE] Requête de qualification — Ne pas saisir dans une boucle.**

```sql
SELECT sqlite_version() AS sqlite_version;
```

La version réellement embarquée doit être enregistrée dans le rapport de qualification runtime du Starter Kit.

## 28. Concurrence et performance

### 28.1 Un seul écrivain

SQLite accepte plusieurs lecteurs, mais une seule transaction d’écriture à la fois.

Le projet Solo utilise une seule connexion principale sur le thread qui orchestre la persistance. Cette règle évite de partager une connexion native entre plusieurs threads sans contrat clair.

### 28.2 Ne pas écrire à chaque frame

Une écriture à chaque `_process()` ou `_physics_process()` provoque :

- beaucoup de transactions ;
- une usure inutile du stockage ;
- des risques de contention ;
- des ralentissements ;
- des états difficiles à grouper de manière cohérente.

Utiliser des événements métier et des checkpoints.

### 28.3 Grouper les écritures

Plusieurs insertions cohérentes sont plus efficaces et plus sûres dans une transaction explicite que dans une série de transactions implicites indépendantes.

### 28.4 Mesurer avant d’ajouter des index

Pour une requête lente :

1. reproduire la charge ;
2. mesurer ;
3. examiner la requête ;
4. ajouter un index ciblé ;
5. mesurer de nouveau ;
6. vérifier le coût en écriture et en espace.

Le chapitre 28 développera la journalisation et la reproductibilité des diagnostics.

## 29. Évolution du schéma

### 29.1 Ajouter une colonne

Ne pas modifier `001_create_beacon_state.sql` après sa livraison.

Créer par exemple :

> **[LECTURE] Nom d’une future migration — Ne pas créer dans ce chapitre.**

```text
003_add_beacon_damage_state.sql
```

### 29.2 Migration destructive

Pour supprimer ou transformer une colonne :

1. créer une nouvelle table ;
2. copier et convertir les lignes ;
3. vérifier les comptes et contraintes ;
4. supprimer l’ancienne table ;
5. renommer la nouvelle ;
6. reconstruire les index ;
7. laisser la transaction annuler l’ensemble en cas d’échec.

### 29.3 Données et schéma

Une migration peut modifier le schéma et transformer les données nécessaires à ce schéma.

Elle ne doit pas devenir un script de gameplay général ou une importation massive non liée à la compatibilité.

### 29.4 Compatibilité vers l’arrière

Une ancienne version du jeu ne saura généralement pas lire un schéma futur. La politique de retour à une ancienne version doit donc restaurer la copie créée avant migration.

Ne jamais promettre un downgrade automatique sans migrations inverses testées.

## 30. Exporter les migrations et l’extension

### 30.1 Fichiers SQL

Godot n’inclut pas nécessairement les fichiers non-ressources dans le paquet exporté.

> **[APP] Godot — Dans Project > Export > Windows Desktop > Resources.**

Ajouter au filtre des fichiers non-ressources :

> **[LECTURE] Filtre d’export — Saisir dans le champ approprié de Godot, pas dans un terminal.**

```text
*.sql
```

Vérifier l’export en exécutant le build dans un dossier vide et en lançant une base neuve.

### 30.2 Bibliothèques natives

La ressource `.gdextension` doit référencer la bibliothèque Windows x86_64 livrée avec l’addon.

L’export doit être testé sur une machine sans l’éditeur Godot installé. Une réussite dans l’éditeur ne prouve pas que la DLL a été empaquetée.

### 30.3 Licence

Conserver :

- le fichier de licence de l’addon ;
- le nom et la version ;
- l’URL du dépôt ;
- les obligations d’attribution ;
- la date de qualification.

La licence globale du guide reste à définir, mais la licence de chaque dépendance tierce doit déjà être respectée.

## 31. Procédure de validation graphique

> **[APP] Godot — Exécuter `ch08_sqlite_demo.tscn`.**

Vérifier :

1. absence d’erreur de chargement GDExtension ;
2. création de `user://data/asteria.sqlite3` ;
3. création de la copie avant migration lorsqu’une base existe ;
4. présence de `schema_migrations` ;
5. `PRAGMA user_version` égal à `2` ;
6. présence des deux tables métier ;
7. clés étrangères actives ;
8. compteur d’activation conservé entre deux lancements ;
9. aucune écriture dans `res://` ;
10. fermeture propre de la connexion.

## 32. Validation headless future

> **[PS] PowerShell 7 — Depuis la racine du projet Godot matérialisé.**

```powershell
godot --headless --path . scenes/learning/ch08_sqlite_demo.tscn
if ($LASTEXITCODE -ne 0) {
    throw "La démonstration SQLite a échoué."
}
```

Cette commande pourra détecter :

- classe `SQLite` absente ;
- erreur d’analyse GDScript ;
- migration manquante ;
- ouverture de base impossible ;
- checksum divergent ;
- requête SQL invalide ;
- erreur de persistance.

Elle ne qualifiera pas à elle seule :

- une coupure électrique ;
- l’usure du stockage ;
- les performances à grande échelle ;
- toutes les plateformes exportées ;
- la restauration complète d’une partie ;
- la compatibilité des sauvegardes du chapitre 9.

## 33. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

Chaque cas présente un comportement fautif, une correction et la différence observable.

### 33.1 Écrire la base dans `res://`

**Symptôme ou risque :** l’écriture fonctionne dans l’éditeur, puis échoue dans un export où les ressources empaquetées sont en lecture seule.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
var database_path := "res://data/asteria.sqlite3"
```

**Correction :** écrire la base mutable dans le dossier utilisateur.

> **[VSC] Visual Studio Code — Exemple corrigé dans le bootstrap.**

```gdscript
const DATABASE_PATH := "user://data/asteria.sqlite3"
```

**Différence :** `res://` décrit les ressources du projet ; `user://` fournit un emplacement persistant et inscriptible propre à l’application.

### 33.2 Concaténer une valeur dans SQL

**Symptôme ou risque :** une apostrophe casse la requête et une donnée non fiable peut modifier sa structure.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
var sql := "SELECT * FROM beacon_state WHERE beacon_id = '%s';" % user_value
var rows := database.query(sql)
```

**Correction :** utiliser un paramètre lié.

> **[VSC] Visual Studio Code — Exemple corrigé dans le dépôt.**

```gdscript
var rows := database.query(
	"SELECT * FROM beacon_state WHERE beacon_id = ?;",
	[user_value]
)
```

**Différence :** la valeur corrigée reste une donnée ; elle ne peut plus être interprétée comme une partie de la syntaxe SQL.

### 33.3 Modifier une migration déjà appliquée

**Symptôme ou risque :** deux installations portant la même version possèdent des schémas différents.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```text
Modifier 001_create_beacon_state.sql après sa livraison.
Conserver PRAGMA user_version = 1.
```

**Correction :** conserver la migration historique et ajouter une nouvelle version.

> **[LECTURE] Organisation corrigée — Ne pas saisir.**

```text
001_create_beacon_state.sql       inchangée
002_add_beacon_activation_event.sql
003_fix_beacon_state_constraint.sql
```

**Différence :** l’historique corrigé est append-only et vérifiable par checksum ; l’exemple fautif réécrit silencieusement le passé.

### 33.4 Appliquer plusieurs écritures sans transaction

**Symptôme ou risque :** l’état courant est mis à jour, mais l’événement associé échoue, laissant deux tables incohérentes.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
database.execute(update_state_sql, state_bindings)
database.execute(insert_event_sql, event_bindings)
```

**Correction :** entourer les deux opérations d’une transaction et annuler au premier échec.

> **[VSC] Visual Studio Code — Exemple corrigé dans le dépôt.**

```gdscript
var error := database.execute("BEGIN IMMEDIATE;")
if error == OK:
	error = database.execute(update_state_sql, state_bindings)
if error == OK:
	error = database.execute(insert_event_sql, event_bindings)
if error == OK:
	error = database.execute("COMMIT;")
else:
	database.execute("ROLLBACK;")
```

**Différence :** la version corrigée valide l’ensemble ou n’en conserve aucune partie ; la version fautive peut enregistrer seulement la première écriture.

### 33.5 Activer les clés étrangères trop tard

**Symptôme ou risque :** les clauses `FOREIGN KEY` existent dans le schéma, mais des lignes orphelines sont acceptées.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
sqlite.open_db()
sqlite.foreign_keys = true
```

**Correction :** configurer la connexion avant son ouverture et vérifier le PRAGMA.

> **[VSC] Visual Studio Code — Exemple corrigé dans l’adaptateur.**

```gdscript
sqlite.foreign_keys = true
sqlite.open_db()
sqlite.query("PRAGMA foreign_keys = ON;")
```

**Différence :** la version corrigée active l’intégrité sur la connexion avant les écritures ; l’ordre fautif peut laisser l’option inactive.

### 33.6 Copier une base WAL encore ouverte

**Symptôme ou risque :** la copie du fichier principal ne contient pas les dernières transactions présentes dans le journal `-wal`.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
DirAccess.copy_absolute(
	"user://data/asteria.sqlite3",
	"user://backups/asteria.sqlite3"
)
```

**Correction :** effectuer un checkpoint, fermer toutes les connexions, puis copier.

> **[VSC] Visual Studio Code — Exemple corrigé dans le bootstrap.**

```gdscript
database.execute("PRAGMA wal_checkpoint(TRUNCATE);")
database.close()
var backup_path := backup_service.create_closed_copy(DATABASE_PATH)
```

**Différence :** la copie corrigée part d’un fichier stabilisé et fermé ; la copie fautive peut ignorer des pages encore présentes dans le WAL.

### 33.7 Créer un index sur chaque colonne

**Symptôme ou risque :** le fichier grossit et chaque écriture met à jour de nombreux index peu utiles.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```sql
CREATE INDEX idx_enabled ON beacon_state(is_enabled);
CREATE INDEX idx_count ON beacon_state(activation_count);
CREATE INDEX idx_cooldown ON beacon_state(cooldown_remaining);
CREATE INDEX idx_updated ON beacon_state(updated_at_utc);
```

**Correction :** indexer une requête mesurée et fréquente.

> **[VSC] Visual Studio Code — Exemple corrigé dans la migration.**

```sql
CREATE INDEX idx_beacon_state_updated_at
    ON beacon_state(updated_at_utc);
```

**Différence :** la version corrigée répond à un accès identifié ; l’exemple fautif paie le coût de quatre index sans preuve d’utilité.

### 33.8 Partager la connexion native entre plusieurs threads

**Symptôme ou risque :** les appels se chevauchent, les résultats de requête sont remplacés et les erreurs deviennent non déterministes.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
WorkerThreadPool.add_task(func(): sqlite.query(query_a))
WorkerThreadPool.add_task(func(): sqlite.query(query_b))
```

**Correction :** sérialiser les opérations sur une connexion possédée par un service, ou créer des connexions indépendantes avec un contrat de concurrence explicite.

> **[LECTURE] Architecture corrigée — Ne pas saisir.**

```text
Gameplay → file de requêtes → propriétaire unique de DatabaseConnection
```

**Différence :** l’architecture corrigée possède un ordre d’exécution et un propriétaire ; l’exemple fautif partage un objet natif sans synchronisation documentée.

### 33.9 Utiliser SQLite comme `Resource` de conception

**Symptôme ou risque :** les concepteurs doivent modifier des lignes SQL pour changer le rayon ou le texte d’une balise, et les diffs Git deviennent opaques.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```sql
UPDATE beacon_definition
SET display_name = 'Balise ouest', activation_radius = 6.0
WHERE beacon_id = 'beacon.village.west';
```

**Correction :** conserver la définition dans une `Resource` et seulement l’état mutable dans SQLite.

> **[LECTURE] Organisation corrigée — Ne pas saisir.**

```text
res://data/beacons/beacon_village_west.tres
user://data/asteria.sqlite3 → beacon_state
```

**Différence :** la version corrigée garde les données éditoriales lisibles et versionnées, tandis que la base ne contient que l’état persistant de la partie.

### 33.10 Confondre base persistante et sauvegarde complète

**Symptôme ou risque :** le jeu considère tout le fichier SQLite comme un slot sans définir de point de capture cohérent, de métadonnées ou de compatibilité.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```text
Bouton Sauvegarder → copier immédiatement asteria.sqlite3 pendant le gameplay
Bouton Charger → remplacer le fichier ouvert
```

**Correction :** utiliser ce chapitre pour les dépôts persistants et laisser le chapitre 9 définir la capture complète, les slots, l’atomicité et les migrations de sauvegarde.

> **[LECTURE] Flux corrigé — Ne pas saisir.**

```text
État runtime
   ↓ point de sauvegarde cohérent défini au chapitre 9
Snapshot versionné
   ↓ écriture atomique et métadonnées
Slot de sauvegarde
```

**Différence :** le flux corrigé définit ce qui constitue une partie et quand la capturer ; l’exemple fautif manipule un fichier ouvert sans contrat de cohérence.

### 33.11 Confondre absence de ligne et erreur SQL

**Symptôme ou risque :** une requête échoue, retourne un tableau vide par convention, puis le service annonce à tort que l’objet n’existe pas.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
var rows := database.query(sql, bindings)
if rows.is_empty():
	return ERR_DOES_NOT_EXIST
```

**Correction :** vérifier d’abord le code d’erreur, puis seulement la cardinalité du résultat.

> **[VSC] Visual Studio Code — Exemple corrigé dans le dépôt.**

```gdscript
var rows := database.query(sql, bindings)
if database.last_error_code() != OK:
	return database.last_error_code()
if rows.is_empty():
	return ERR_DOES_NOT_EXIST
```

**Différence :** la version corrigée conserve deux états distincts — lecture réussie sans ligne et lecture impossible — alors que l’exemple fautif masque une panne de base derrière un résultat métier normal.

## 34. Parcours Solo

Le parcours Solo retient :

- un seul fichier `user://data/asteria.sqlite3` ;
- une connexion principale ;
- Godot-SQLite épinglé ;
- deux migrations initiales ;
- un backup avant migration ;
- des requêtes paramétrées ;
- un dépôt par fonctionnalité persistante ;
- des écritures sur événements ;
- `quick_check` au diagnostic ;
- une procédure manuelle de restauration documentée.

Le but est la fiabilité avec un nombre limité de composants.

## 35. Parcours Studio

Le parcours Studio ajoute :

- un propriétaire de schéma ;
- une revue obligatoire de chaque migration ;
- des checksums vérifiés en CI ;
- une base fixture par version supportée ;
- des tests d’upgrade depuis chaque version publiée ;
- des tests d’échec au milieu d’une migration ;
- un inventaire des index et de leur justification ;
- une qualification par plateforme ;
- une politique de rétention des copies ;
- des métriques de durée et de taille ;
- une procédure de restauration répétée ;
- une matrice de compatibilité addon, Godot et SQLite embarqué ;
- une validation de l’export sur machine propre.

Une migration relue uniquement sur une base vide ne suffit pas. Elle doit être testée sur des données représentatives et sur les versions réellement distribuées.

## 36. Checklist d’audit

- [ ] Godot-SQLite est épinglé à la version approuvée.
- [ ] Sa licence MIT est conservée.
- [ ] La classe `SQLite` est vérifiée avant l’ouverture.
- [ ] La base mutable est sous `user://`.
- [ ] Le dossier est créé avant l’ouverture.
- [ ] Les clés étrangères sont activées pour chaque connexion.
- [ ] Le timeout d’attente est explicite.
- [ ] Le mode de journal et la synchronisation sont documentés.
- [ ] Les valeurs dynamiques utilisent des bindings.
- [ ] Les noms SQL dynamiques proviennent d’une liste fermée.
- [ ] Les contraintes protègent les invariants simples.
- [ ] Les index correspondent à des requêtes identifiées.
- [ ] Les écritures cohérentes utilisent une transaction.
- [ ] Les migrations sont numérotées et append-only.
- [ ] `PRAGMA user_version` est mis à jour dans la transaction.
- [ ] `schema_migrations` conserve le checksum.
- [ ] Une copie fermée est créée uniquement lorsqu’une migration est en attente.
- [ ] Un échec déclenche un rollback.
- [ ] Le gameplay ne démarre pas après une migration incomplète.
- [ ] `quick_check` et `foreign_key_check` sont exécutés après les migrations.
- [ ] Une absence de ligne reste distincte d’une erreur de requête.
- [ ] Les fichiers `*.sql` sont inclus dans l’export.
- [ ] Les DLL de l’extension sont testées hors éditeur.
- [ ] La base ne duplique pas les `Resource` de conception.
- [ ] La frontière avec le chapitre 9 est respectée.
- [ ] Chaque cas d’erreur contient exemple fautif, exemple corrigé et différence.
- [ ] Les repères d’utilisation sont cohérents.
- [ ] Aucun PDF intermédiaire n’a été construit.

## 37. Critères d’acceptation

Le chapitre est accepté au niveau `static-review` lorsque :

- le choix d’intégration est qualifié et licencié ;
- l’architecture ne fait pas dépendre le domaine de SQLite ;
- le schéma et les deux migrations sont cohérents ;
- les requêtes utilisent des bindings ;
- le runner gère version, historique, checksum, transaction et rollback ;
- la copie préalable respecte le mode WAL ;
- le dépôt mappe les lignes vers un type applicatif et propage les erreurs de lecture ;
- les diagnostics d’intégrité sont fournis ;
- les procédures d’export sont expliquées ;
- les erreurs fréquentes respectent la règle sémantique ;
- l’index, la roadmap, `contents.txt` et la continuité sont mis à jour ;
- le workflow léger réussit sans produire de PDF.

Le statut `runtime-tested` exige en plus :

- installation réelle de l’addon ;
- chargement de la DLL Windows x86_64 ;
- exécution des migrations ;
- création et réouverture de la base ;
- vérification de la persistance entre deux lancements ;
- simulation d’un échec de migration ;
- restauration d’une copie ;
- test d’un export Windows sur machine propre.

## 38. Résultat attendu

À la fin du chapitre, `Project Asteria` possède une architecture documentée pour :

- ouvrir une base SQLite locale ;
- versionner son schéma ;
- détecter une migration historique modifiée ;
- protéger les migrations par transaction ;
- créer une copie préalable ;
- persister et restaurer un état de balise ;
- conserver un historique relié ;
- diagnostiquer l’intégrité ;
- exporter les fichiers SQL et l’extension native ;
- préparer le système de sauvegarde du chapitre 9.

La base et les scripts ne sont pas encore matérialisés dans le Starter Kit. Le niveau reste donc `static-review`.

## 39. Sources officielles et primaires vérifiées

- Godot Engine, **Installing plugins**, documentation stable : <https://docs.godotengine.org/en/stable/tutorials/plugins/editor/installing_plugins.html>
- Godot Engine, **GDExtension**, documentation 4.7 : <https://docs.godotengine.org/en/4.7/engine_details/engine_api/gdextension/index.html>
- Godot Engine, **Exporting projects**, documentation stable : <https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html>
- Godot Engine, **FileAccess**, référence stable : <https://docs.godotengine.org/en/stable/classes/class_fileaccess.html>
- Godot Engine, **DirAccess**, référence 4.x : <https://docs.godotengine.org/fr/4.x/classes/class_diraccess.html>
- Godot Engine, **Time**, référence 4.x : <https://docs.godotengine.org/fr/4.x/classes/class_time.html>
- Godot Engine, **HashingContext**, référence 4.x : <https://docs.godotengine.org/fr/4.x/classes/class_hashingcontext.html>
- Godot Asset Library, **Godot-SQLite 4.7** : <https://godotengine.org/asset-library/asset?user=2shady4u>
- 2shady4u, **godot-sqlite**, dépôt et API primaire : <https://github.com/2shady4u/godot-sqlite>
- 2shady4u, **implémentation de `query_with_bindings()` relue au commit `019027732dc03d1a3b3ce4c3166d98961f4e066f`** : <https://github.com/2shady4u/godot-sqlite/blob/019027732dc03d1a3b3ce4c3166d98961f4e066f/src/gdsqlite.cpp>
- SQLite, **Datatypes in SQLite** : <https://www.sqlite.org/datatype3.html>
- SQLite, **Transaction** : <https://www.sqlite.org/lang_transaction.html>
- SQLite, **Foreign Key Support** : <https://www.sqlite.org/foreignkeys.html>
- SQLite, **Binding Values To Prepared Statements** : <https://www.sqlite.org/c3ref/bind_blob.html>
- SQLite, **PRAGMA statements** : <https://www.sqlite.org/pragma.html>
- SQLite, **VACUUM and VACUUM INTO** : <https://www.sqlite.org/lang_vacuum.html>
- SQLite, **SQLite Is Transactional** : <https://www.sqlite.org/transactional.html>
