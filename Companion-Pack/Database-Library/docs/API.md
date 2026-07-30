# API publique

## Convention

Toutes les fonctions sont synchrones. Elles utilisent exclusivement la bibliothèque standard Python. Les erreurs contrôlées reçoivent une classe explicite ; les erreurs SQLite restent des sous-classes de `sqlite3.Error`.

## Connexion

### `open_database(path, *, read_only=False, options=None)`

- `path: str | Path` : fichier SQLite ;
- `read_only: bool` : utilise `mode=ro` ;
- `options: ConnectionOptions | None` : politiques de connexion ;
- retour : `sqlite3.Connection` ;
- effets : crée le dossier parent en écriture, configure les pragmas ;
- exceptions : `ValueError`, `sqlite3.Error`.

### `ConnectionOptions`

| Champ | Type | Défaut | Contrat |
|---|---|---:|---|
| `busy_timeout_ms` | `int` | `3000` | `0..60000` |
| `journal_mode` | `str` | `WAL` | liste fermée |
| `synchronous` | `str` | `FULL` | liste fermée |

## Migrations

### `load_manifest(path=None)`

Retourne `MigrationManifest`. Refuse séquences trouées, noms dupliqués et `latest_version` incohérente.

### `MigrationRunner.migrate(target_version=None)`

- `target_version: int | None` ;
- retour : version installée `int` ;
- refuse : base étrangère, version future, downgrade, checksum divergent ;
- transaction : une transaction `BEGIN IMMEDIATE` par migration.

### `MigrationRunner.verify_history(installed_version=None)`

Ne modifie pas le schéma. Compare noms et checksums attendus.

## Repositories

### `BeaconStateRepository`

- `save(BeaconState) -> None` ;
- `find(str) -> BeaconState | None` ;
- `list_all() -> tuple[BeaconState, ...]` ;
- `delete(str) -> bool` ;
- `add_event(...) -> int` ;
- `list_recent_events(str, limit=50) -> tuple[dict, ...]`.

### `ContentDocumentRepository`

- `save(ContentDocument) -> None` ;
- `upsert_tag(tag_id, label) -> None` ;
- `assign_tag(document_id, tag_id) -> None` ;
- `search_by_tag(tag_id) -> tuple[ContentDocument, ...]`.

### `put_derived_cache_entry(...)`

Stocke uniquement une donnée dérivée recréable. `source_checksum` doit contenir 64 caractères. `payload` doit être sérialisable en JSON strict.

## Sauvegarde et restauration

### `create_backup(source_path, destination_path) -> Path`

Refuse l’écrasement, utilise l’Online Backup API et valide la sortie.

### `restore_backup(backup_path, target_path) -> Path`

Valide, stage, synchronise, remplace et revalide. L’appelant ferme toutes les connexions de la cible.

## Validation

### `validate_database(path, *, require_latest=True) -> ValidationReport`

Effectue les portes d’identité, version, intégrité, relations et historique. Ne migre jamais.

## Fixtures

### `seed_synthetic_data(connection, fixture_path=None) -> dict[str, int]`

Charge une fixture fictive versionnée par les repositories publics.
