#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md"
text = CHAPTER.read_text(encoding="utf-8")


def replace_code_after(marker: str, language: str, replacement: str) -> None:
    global text
    marker_index = text.index(marker)
    opening = f"```{language}\n"
    start = text.index(opening, marker_index) + len(opening)
    end = text.index("\n```", start)
    text = text[:start] + replacement.rstrip() + text[end:]


def replace_once(old: str, new: str) -> None:
    global text
    if text.count(old) != 1:
        raise SystemExit(f"Replacement target count is {text.count(old)} instead of 1: {old[:100]!r}")
    text = text.replace(old, new, 1)


replace_code_after(
    "`res://src/core/persistence/database_connection.gd`",
    "gdscript",
    r'''class_name DatabaseConnection
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
	return "Connexion non configurée"''',
)

replace_once(
    "`_path`, `_sql` et `_bindings` indiquent que la classe de base ne les utilise pas. Les sous-classes les utilisent réellement.\n",
    "`_path`, `_sql` et `_bindings` indiquent que la classe de base ne les utilise pas. Les sous-classes les utilisent réellement.\n\n`last_error_code()` distingue une requête réussie sans ligne d’une requête qui a échoué. `last_error_message()` fournit le diagnostic humain complémentaire. Un tableau vide ne doit jamais être interprété seul.\n",
)

replace_code_after(
    "`res://src/core/persistence/sqlite_database_connection.gd`",
    "gdscript",
    r'''class_name SqliteDatabaseConnection
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
	_last_error_message = ""''',
)

replace_once(
    "L’addon demande d’activer `foreign_keys` avant `open_db()`. Le code exécute aussi `PRAGMA foreign_keys = ON` après l’ouverture pour rendre l’intention visible et vérifiable.\n",
    "L’addon demande d’activer `foreign_keys` avant `open_db()`. L’adaptateur crée la classe native par `ClassDB.instantiate()` afin de pouvoir diagnostiquer proprement son absence sans référencer statiquement le type tiers. Il exécute aussi `PRAGMA foreign_keys = ON` après l’ouverture et vérifie que la valeur lue vaut `1`.\n",
)
replace_once(
    "Le mode WAL utilise un journal d’écriture séparé. Il améliore généralement la coexistence entre lectures et écriture.\n\nLe projet conserve `synchronous = FULL` comme défaut prudent.",
    "Le mode WAL utilise un journal d’écriture séparé. Il améliore généralement la coexistence entre lectures et écriture. L’adaptateur lit le résultat de `PRAGMA journal_mode = WAL` et refuse de poursuivre si SQLite ne confirme pas réellement `wal`.\n\nLe projet conserve `synchronous = FULL` comme défaut prudent.",
)
replace_once(
    "L’addon expose le résultat de la dernière requête sous forme de tableau de dictionnaires. L’adaptateur copie les dictionnaires valides dans un tableau typé.\n",
    "L’addon expose le résultat de la dernière requête sous forme de tableau de dictionnaires. L’adaptateur duplique les dictionnaires valides dans un tableau typé et conserve séparément le dernier code d’erreur.\n",
)

replace_code_after(
    "`res://src/core/persistence/sql_migration_runner.gd`",
    "gdscript",
    r'''class_name SqlMigrationRunner
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

	error = _ensure_history_table()
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

	return context.finish().hex_encode()''',
)

replace_once(
    "L’adaptateur transmet le fichier complet à `query()`. Godot-SQLite utilise l’API SQLite capable d’exécuter une chaîne contenant plusieurs instructions.\n",
    "L’adaptateur transmet le fichier complet à `query()`. Dans l’implémentation relue de Godot-SQLite, `query_with_bindings()` prépare une première instruction avec `sqlite3_prepare_v2`, exécute celle-ci, puis traite récursivement la queue SQL `pzTail` tant qu’elle n’est pas vide. Une migration multi-instructions est donc prise en charge par cette version de l’addon.\n",
)
replace_once(
    "La liste est triée par version croissante. Une version ne doit jamais être réutilisée.\n",
    "La liste est triée par version croissante. `_validate_manifest()` impose ici une séquence continue à partir de `1`, ainsi que des noms uniques et des chemins non vides. Une version ne doit jamais être réutilisée.\n",
)

replace_code_after(
    "`res://src/core/persistence/database_backup_service.gd`",
    "gdscript",
    r'''class_name DatabaseBackupService
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

	return DirAccess.copy_absolute(backup_path, database_path)''',
)
replace_once(
    "Cette classe exige que toutes les connexions soient fermées. Le nom de méthode le rappelle explicitement.\n",
    "Cette classe exige que toutes les connexions soient fermées. Le nom de méthode le rappelle explicitement. La restauration supprime aussi les anciens fichiers auxiliaires `-wal` et `-shm` afin qu’ils ne soient jamais rejoués sur la copie restaurée.\n",
)
replace_once(
    "La copie simple d’un fichier ouvert en mode WAL n’est pas sûre. Le projet doit :\n",
    "La copie simple d’un fichier ouvert en mode WAL n’est pas sûre. Lorsqu’une migration est réellement nécessaire, le projet doit :\n",
)

replace_code_after(
    "`res://src/features/beacons/application/beacon_state_repository.gd`",
    "gdscript",
    r'''class_name BeaconStateRepository
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
	return ERR_UNAVAILABLE''',
)
replace_once(
    "Le nom `Repository` désigne ici une collection persistante d’objets métier. Il ne désigne ni un dépôt Git, ni un Service Locator.\n",
    "Le nom `Repository` désigne ici une collection persistante d’objets métier. Il ne désigne ni un dépôt Git, ni un Service Locator. `last_error_code()` permet au service de distinguer `ERR_DOES_NOT_EXIST` d’une panne de lecture.\n",
)

replace_code_after(
    "`res://src/features/beacons/infrastructure/sqlite_beacon_state_repository.gd`",
    "gdscript",
    r'''class_name SqliteBeaconStateRepository
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
	)''',
)
replace_once(
    "- les bornes dans le constructeur du record.\n",
    "- les bornes dans le constructeur du record ;\n- le code d’erreur de la connexion, afin qu’un tableau vide valide ne masque jamais une panne SQL.\n",
)

old_restore = r'''func restore_runtime_state(state: BeaconRuntimeState) -> Error:
	if _repository == null or state == null:
		return ERR_UNCONFIGURED

	var record := _repository.find(state.profile_id)
	if record == null:
		return ERR_DOES_NOT_EXIST

	return record.apply_to(state)'''
new_restore = r'''func restore_runtime_state(state: BeaconRuntimeState) -> Error:
	if _repository == null or state == null:
		return ERR_UNCONFIGURED

	var record := _repository.find(state.profile_id)
	if record == null:
		return _repository.last_error_code()

	return record.apply_to(state)'''
replace_once(old_restore, new_restore)
replace_once(
    "Le service ignore SQL et SQLite. Il reçoit un dépôt injecté depuis le bootstrap.\n",
    "Le service ignore SQL et SQLite. Il reçoit un dépôt injecté depuis le bootstrap. Lorsqu’une recherche retourne `null`, il propage le code du dépôt : `ERR_DOES_NOT_EXIST` reste distinct d’une erreur de requête ou d’une ligne corrompue.\n",
)

replace_code_after(
    "`res://src/app/database_bootstrap.gd`",
    "gdscript",
    r'''class_name DatabaseBootstrap
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

	return OK''',
)
replace_once(
    "Si la base n’existe pas, aucune copie préalable n’est nécessaire. L’ouverture crée le fichier, puis les migrations créent le schéma.\n",
    "Si la base n’existe pas, aucune copie préalable n’est nécessaire. L’ouverture crée le fichier, puis les migrations créent le schéma. Le runner refuse aussi une base dont `user_version` est plus récent que la version maximale connue par l’application.\n",
)
replace_once(
    "Le bootstrap :\n\n1. ouvre la base pour permettre la récupération SQLite ;\n2. force un checkpoint WAL ;\n3. ferme la connexion ;\n4. crée une copie ;\n5. rouvre la base ;\n6. applique les migrations ;\n7. injecte le dépôt.\n",
    "Lorsqu’une migration est en attente, le bootstrap :\n\n1. ouvre la base pour permettre la récupération SQLite ;\n2. lit `PRAGMA user_version` ;\n3. force un checkpoint WAL ;\n4. ferme la connexion ;\n5. crée une copie et conserve son chemin ;\n6. rouvre la base ;\n7. applique les migrations ;\n8. exécute `quick_check` et `foreign_key_check` ;\n9. injecte le dépôt.\n\nSi le schéma est déjà à jour, aucune nouvelle copie n’est créée, mais les checksums historiques et l’intégrité sont tout de même vérifiés.\n",
)

insert_marker = "## 34. Parcours Solo\n"
new_case = r'''### 33.11 Confondre absence de ligne et erreur SQL

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

'''
if insert_marker not in text:
    raise SystemExit("Solo section marker missing")
text = text.replace(insert_marker, new_case + insert_marker, 1)

replace_once(
    "- [ ] Une copie fermée est créée avant migration.\n",
    "- [ ] Une copie fermée est créée uniquement lorsqu’une migration est en attente.\n",
)
replace_once(
    "- [ ] `quick_check` et `foreign_key_check` sont documentés.\n",
    "- [ ] `quick_check` et `foreign_key_check` sont exécutés après les migrations.\n- [ ] Une absence de ligne reste distincte d’une erreur de requête.\n",
)
replace_once(
    "- le dépôt mappe les lignes vers un type applicatif ;\n",
    "- le dépôt mappe les lignes vers un type applicatif et propage les erreurs de lecture ;\n",
)
replace_once(
    "- 2shady4u, **godot-sqlite**, dépôt et API primaire : <https://github.com/2shady4u/godot-sqlite>\n",
    "- 2shady4u, **godot-sqlite**, dépôt et API primaire : <https://github.com/2shady4u/godot-sqlite>\n- 2shady4u, **implémentation de `query_with_bindings()` relue au commit `019027732dc03d1a3b3ce4c3166d98961f4e066f`** : <https://github.com/2shady4u/godot-sqlite/blob/019027732dc03d1a3b3ce4c3166d98961f4e066f/src/gdsqlite.cpp>\n",
)

CHAPTER.write_text(text, encoding="utf-8")
print("Chapter 8 technical refinements applied.")
