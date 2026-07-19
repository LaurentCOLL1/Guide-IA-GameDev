#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / "Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md"
text = path.read_text(encoding="utf-8")

old = '''\tvar error := _validate_manifest()
\tif error != OK:
\t\treturn error

\terror = _ensure_history_table()
\tif error != OK:
\t\treturn error

\tvar installed_version := current_version()
\tif installed_version < 0:
\t\treturn FAILED
\tif installed_version > latest_version():
\t\tpush_error(
\t\t\t"Schéma plus récent que l’application : %d > %d"
\t\t\t% [installed_version, latest_version()]
\t\t)
\t\treturn ERR_INVALID_DATA

\terror = _verify_applied_migrations(installed_version)
'''
new = '''\tvar error := _validate_manifest()
\tif error != OK:
\t\treturn error

\tvar installed_version := current_version()
\tif installed_version < 0:
\t\treturn FAILED
\tif installed_version > latest_version():
\t\tpush_error(
\t\t\t"Schéma plus récent que l’application : %d > %d"
\t\t\t% [installed_version, latest_version()]
\t\t)
\t\treturn ERR_INVALID_DATA

\terror = _ensure_history_table()
\tif error != OK:
\t\treturn error

\terror = _verify_applied_migrations(installed_version)
'''
if text.count(old) != 1:
    raise SystemExit("Migration ordering block not found exactly once")
text = text.replace(old, new, 1)

old = '''\tfor row: Dictionary in rows:
\t\tif not row.has("version"):
\t\t\treturn ERR_FILE_CORRUPT
\t\tvar version := int(row["version"])
\t\tif applied_by_version.has(version):
\t\t\treturn ERR_FILE_CORRUPT
\t\tapplied_by_version[version] = row
'''
new = '''\tfor row: Dictionary in rows:
\t\tif not row.has("version"):
\t\t\treturn ERR_FILE_CORRUPT
\t\tvar version := int(row["version"])
\t\tif version < 1 or version > installed_version:
\t\t\tpush_error("Historique incohérent pour la version %d" % version)
\t\t\treturn ERR_FILE_CORRUPT
\t\tif applied_by_version.has(version):
\t\t\treturn ERR_FILE_CORRUPT
\t\tapplied_by_version[version] = row
'''
if text.count(old) != 1:
    raise SystemExit("Applied migration loop not found exactly once")
text = text.replace(old, new, 1)

old = '''func record_activation(
\trecord: BeaconStateRecord,
\tactor_id: StringName
) -> Error:
\tvar error := _database.execute("BEGIN IMMEDIATE;")
'''
new = '''func record_activation(
\trecord: BeaconStateRecord,
\tactor_id: StringName
) -> Error:
\tif record == null:
\t\treturn ERR_INVALID_PARAMETER
\tif not StableId.is_valid(record.profile_id):
\t\treturn ERR_INVALID_PARAMETER
\tif not StableId.is_valid(actor_id):
\t\treturn ERR_INVALID_PARAMETER
\tif record.last_activated_at_utc.is_empty():
\t\treturn ERR_INVALID_PARAMETER

\tvar error := _database.execute("BEGIN IMMEDIATE;")
'''
if text.count(old) != 1:
    raise SystemExit("record_activation block not found exactly once")
text = text.replace(old, new, 1)

old = '''Le dépôt orchestre la transaction, car il connaît les deux opérations SQL. Le service applicatif demande une intention métier unique : enregistrer une activation.
'''
new = '''Le dépôt orchestre la transaction, car il connaît les deux opérations SQL. Il valide les deux identifiants et la date avant `BEGIN IMMEDIATE`, afin qu’une erreur de paramètre ne démarre aucune transaction. Le service applicatif demande une intention métier unique : enregistrer une activation.
'''
if text.count(old) != 1:
    raise SystemExit("record_activation prose not found exactly once")
text = text.replace(old, new, 1)

old = '''Le runner refuse aussi une base dont `user_version` est plus récent que la version maximale connue par l’application.
'''
new = '''Le runner lit `user_version` avant de créer ou modifier sa table d’historique. Il refuse ainsi une base dont le schéma est plus récent que la version maximale connue, sans écrire quoi que ce soit dans ce fichier futur.
'''
if text.count(old) != 1:
    raise SystemExit("Future schema prose not found exactly once")
text = text.replace(old, new, 1)

path.write_text(text, encoding="utf-8")
print("Final Chapter 8 code corrections applied.")
