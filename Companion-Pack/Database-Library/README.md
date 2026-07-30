---
title: "Companion Pack — Database Library"
id: "CP-PACK-05-DATABASE-LIBRARY"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
validation-status: "runtime-tested-linux"
redistribution-status: "global-policy-defined"
reference-runtime:
  name: "CPython"
  version: "3.12"
  module: "sqlite3"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Database Library

Le Pack 5 fournit une bibliothèque SQLite réutilisable pour créer une base depuis zéro, appliquer des migrations ascendantes immuables, manipuler les données au moyen de repositories, charger des fixtures synthétiques, sauvegarder, restaurer et vérifier l’intégrité d’un fichier.

> **Repères d’utilisation :** **[PS]** PowerShell, **[CMD]** Invite de commandes Windows, **[WSL]** terminal Linux sous Windows, **[DCT]** terminal d’un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à comparer et **[LECTURE]** contenu à étudier.

## 1. Périmètre et frontières

Le Pack matérialise exactement l’entrée **Pack 5 — Database Library** du plan maître. Il contient :

- quatre migrations SQLite ascendantes ;
- un manifeste avec versions, noms, chemins, versions minimales et empreintes SHA-256 ;
- deux repositories métier ;
- une table de cache dérivé explicitement non autoritaire ;
- une fixture synthétique déterministe ;
- quatre outils CLI ;
- une sauvegarde fondée sur l’Online Backup API ;
- une restauration par staging et remplacement atomique ;
- un validateur d’identité, version, intégrité, clés étrangères et historique ;
- quatorze tests Python ;
- une documentation d’API et des diagrammes.

Il ne contient pas Godot-SQLite, de binaire tiers, de sauvegarde complète de partie, d’index vectoriel, de cache de fournisseur IA, de donnée personnelle, de secret, de promesse de performance, d’export ou de release.

La sauvegarde de partie reste propriétaire du Livre II, chapitre 9. La recherche vectorielle reste propriétaire du chapitre 10. Les files et caches de fournisseurs restent propriétaires de l’AI Library. Le repository mémoire reste dans la Code Library.

## 2. Prérequis

- Python `3.10+` ;
- module standard `sqlite3` ;
- SQLite `3.37.0+` pour les tables `STRICT` ;
- aucun paquet Python tiers pour l’exécution et les tests.

Le `pyproject.toml` décrit le paquet, mais les validations utilisent directement `PYTHONPATH`.

## 3. Arborescence

> **[LECTURE] Arborescence canonique — Ne pas saisir.**

```text
Database-Library/
├── README.md
├── VERSION
├── manifest.json
├── catalog.json
├── sql/
│   ├── migrations/
│   └── queries/
├── data/synthetic/
├── python/src/asteria_database/
├── python/tests/
├── tools/
├── docs/
└── qa/
```

Les fichiers `.sqlite3`, `.db`, `-wal`, `-shm` et `.restore.tmp` sont des sorties runtime exclues de Git.

## 4. Démarrage minimal

> **[PS] PowerShell 7 — Depuis `Companion-Pack/Database-Library`.**

```powershell
$env:PYTHONPATH = (Resolve-Path ".\python\src")
python .\tools\init_database.py `
  .\dist\demo.sqlite3 `
  --with-synthetic-data
```

Le paramètre `database: Path` désigne le fichier à créer ou migrer. L’option booléenne `--with-synthetic-data` charge uniquement la fixture fictive. `main() -> int` renvoie `0` après migration, insertion et validation réussies.

> **[SORTIE] Sortie minimale attendue — Le chemin peut différer.**

```json
{"database":"dist/demo.sqlite3","status":"success","synthetic_counts":{"beacons":2,"cache_entries":1,"documents":2,"events":1,"tags":1},"user_version":4}
```

> **[CMD] Invite de commandes Windows — Valider la base.**

```bat
set PYTHONPATH=python\src
python tools\validate_database.py dist\demo.sqlite3
```

> **[WSL] Bash — Lancer les tests.**

```bash
export PYTHONPATH="$PWD/python/src"
python3 -m unittest discover -s python/tests -v
```

`discover` recherche `test_*.py`. `-s` fixe le dossier de départ et `-v` affiche chaque cas.

> **[DCT] Terminal d’un conteneur — Parcours facultatif non utilisé comme preuve du lot.**

```bash
docker run --rm \
  -v "$PWD:/work" \
  -w /work \
  -e PYTHONPATH=/work/python/src \
  python:3.12-slim \
  python -m unittest discover -s python/tests -v
```

`--rm` supprime le conteneur arrêté ; `-v` monte le Pack ; `-w` sélectionne `/work`.

> **[DCK] Docker Desktop — Vérifier seulement que le conteneur s’arrête et qu’aucun volume anonyme persistant n’est créé.**

## 5. Identité et versions

Le manifeste fixe :

```text
database_id    = asteria-local-data
application_id = 1095980085
latest_version = 4
```

- `PRAGMA application_id` identifie la famille du fichier ;
- `PRAGMA user_version` indique la dernière migration appliquée ;
- `schema_migrations` conserve version, nom, empreinte et date ;
- la version du Pack décrit l’ensemble distribué ;
- `sqlite3.sqlite_version` décrit le moteur réellement utilisé.

Une base future est refusée. Aucun downgrade automatique n’est tenté.

## 6. Connexion

`open_database(path, *, read_only=False, options=None) -> sqlite3.Connection` reçoit :

- `path: str | Path`, chemin de la base ;
- `read_only: bool`, ouverture via `mode=ro` ;
- `options: ConnectionOptions | None`, politiques de connexion.

La fonction applique `foreign_keys=ON`, un `busy_timeout` borné, `trusted_schema=OFF`, `journal_mode=WAL` et `synchronous=FULL` en écriture. Elle renvoie une connexion dont les lignes sont des `sqlite3.Row`.

`ConnectionOptions` contient :

- `busy_timeout_ms: int = 3000`, borné entre `0` et `60000` ;
- `journal_mode: str = "WAL"`, contrôlé par liste fermée ;
- `synchronous: str = "FULL"`, contrôlé par liste fermée.

## 7. Migrations

`load_manifest(path=None) -> MigrationManifest` lit le JSON et vérifie une séquence continue à partir de `1`, des noms uniques et la cohérence de `latest_version`.

`MigrationRunner(connection, manifest=None, root=None)` reçoit une connexion configurée, un manifeste optionnel et la racine des chemins relatifs.

`migrate(target_version=None) -> int` :

1. crée `schema_migrations` si nécessaire ;
2. initialise `application_id` uniquement sur une base réellement vide ;
3. refuse une base étrangère, une version future ou un downgrade ;
4. vérifie les migrations déjà appliquées ;
5. recalcule l’empreinte du SQL ;
6. ouvre `BEGIN IMMEDIATE` ;
7. exécute chaque instruction ;
8. insère l’historique avec paramètres liés ;
9. met à jour `user_version` ;
10. effectue `COMMIT` ou `ROLLBACK` après échec.

Le retour est la version installée. Les fichiers SQL ne contiennent pas leurs propres `BEGIN`, `COMMIT` ou `ROLLBACK`, car le runner possède la frontière transactionnelle.

Une migration publiée est immuable. Une correction reçoit un nouveau numéro.

## 8. Repositories

### `BeaconStateRepository`

- `save(record: BeaconState) -> None` valide les nombres et effectue un UPSERT paramétré ;
- `find(beacon_id: str) -> BeaconState | None` renvoie un record ou `None` ;
- `list_all() -> tuple[BeaconState, ...]` renvoie une collection triée ;
- `delete(beacon_id: str) -> bool` indique si une ligne a été supprimée ;
- `add_event(...) -> int` renvoie la clé technique créée ;
- `list_recent_events(beacon_id, limit=50) -> tuple[dict, ...]` borne `limit` entre `1` et `500`.

### `ContentDocumentRepository`

- `save(document: ContentDocument) -> None` effectue un UPSERT ;
- `upsert_tag(tag_id, label) -> None` crée ou renomme un tag ;
- `assign_tag(document_id, tag_id) -> None` crée la relation ;
- `search_by_tag(tag_id) -> tuple[ContentDocument, ...]` renvoie les documents triés.

Le Pack n’implémente aucun embedding ni index vectoriel.

`put_derived_cache_entry(...) -> None` stocke uniquement une donnée dérivée recréable. Il ne fournit ni LRU, ni file, ni retry, ni cache de fournisseur.

## 9. Données synthétiques

`seed_synthetic_data(connection, fixture_path=None) -> dict[str, int]` charge `data/synthetic/asteria-fixture.json`.

La fixture porte une version de schéma, annonce l’absence de données personnelles, utilise des identifiants fictifs et contient deux balises, un événement, deux documents, un tag et une entrée dérivée.

Le dictionnaire retourné expose les nombres d’objets insérés. Les données autoritaires utilisent des UPSERT ou relations sans doublon. L’événement d’exemple reste un historique ajoutable et n’est pas présenté comme idempotent.

## 10. Sauvegarde

`create_backup(source_path, destination_path) -> Path` :

1. refuse une source absente ;
2. refuse d’écraser une destination ;
3. utilise `sqlite3.Connection.backup()` ;
4. supprime une destination incomplète après échec ;
5. valide la copie ;
6. renvoie son chemin.

> **[PS] PowerShell 7 — Créer une sauvegarde validée.**

```powershell
python .\tools\backup_database.py `
  .\dist\demo.sqlite3 `
  .\dist\backups\demo-001.sqlite3
```

La sauvegarde n’est ni chiffrée ni signée.

## 11. Restauration

`restore_backup(backup_path, target_path) -> Path` valide la source, copie vers `<cible>.restore.tmp`, synchronise et valide le staging, retire les anciens sidecars, remplace la cible avec `os.replace()`, puis valide la cible finale.

> **[WSL] Bash — Restaurer dans une cible isolée.**

```bash
python3 tools/restore_database.py \
  dist/backups/demo-001.sqlite3 \
  dist/restored/demo.sqlite3
```

L’appelant doit fermer toutes les connexions de la cible avant restauration.

## 12. Validation

`validate_database(path, *, require_latest=True) -> ValidationReport` vérifie :

- présence du fichier ;
- `application_id` ;
- `user_version` ;
- `PRAGMA quick_check` ;
- `PRAGMA foreign_key_check` ;
- noms et empreintes des migrations ;
- égalité entre nombre de migrations et `user_version`.

`require_latest=False` permet d’inspecter une ancienne version supportée sans la migrer. Le rapport contient chemin, identifiant, version, résultat d’intégrité, violations de clés étrangères, nombre de migrations et statut.

## 13. Intégration Godot

Le Pack ne distribue pas Godot-SQLite. Une intégration Godot doit qualifier séparément l’addon, cacher la classe native derrière un adaptateur, reproduire l’identité, la version, l’historique, les checksums, les paramètres liés et les tests de restauration.

> **[VSC] Visual Studio Code — Lire et adapter :** `docs/INTEGRATION.md`.

> **[WEB] Navigateur — Vérifier les documentations officielles SQLite sur les transactions, WAL, les tables `STRICT` et l’Online Backup API avant de modifier ces politiques.**

> **[APP] DB Browser for SQLite ou outil équivalent — Inspecter uniquement une copie de développement et ne pas enregistrer une modification dans une preuve de référence.**

## 14. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 14.1 Copier seulement le fichier principal en WAL

**Symptôme ou risque :** des écritures récentes manquent dans la copie.

**Exemple fautif**

```python
shutil.copy2("game.sqlite3", "backup.sqlite3")
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** une base ouverte peut dépendre de `game.sqlite3-wal`. Copier le fichier principal ne constitue pas un snapshot cohérent.

**Exemple corrigé**

```python
create_backup("game.sqlite3", "backup.sqlite3")
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’Online Backup API produit un snapshot, puis la copie franchit les contrôles d’identité, version, intégrité, relations et historique.

### 14.2 Concaténer une valeur SQL

**Symptôme ou risque :** une quote modifie la syntaxe ou permet une injection.

**Exemple fautif**

```python
sql = "SELECT * FROM beacon_state WHERE beacon_id = '" + beacon_id + "'"
connection.execute(sql)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la valeur devient une partie du programme SQL.

**Exemple corrigé**

```python
connection.execute(
    "SELECT * FROM beacon_state WHERE beacon_id = ?",
    (beacon_id,),
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le texte SQL et la valeur suivent deux canaux distincts ; `?` représente un paramètre.

### 14.3 Réécrire une migration publiée

**Symptôme ou risque :** deux bases portant la même version obtiennent des schémas différents.

**Exemple fautif**

```text
Modifier 002_add_beacon_activation_event.sql après publication.
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** l’empreinte stockée diverge et la reproductibilité est rompue.

**Exemple corrigé**

```text
Créer 005_correct_beacon_activation_event.sql.
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la correction devient une nouvelle transition ascendante, traçable et testable.

### 14.4 Restaurer sans validation

**Symptôme ou risque :** une cible saine est remplacée par une base étrangère, future ou corrompue.

**Exemple fautif**

```python
os.replace("downloaded.sqlite3", "game.sqlite3")
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** aucune porte n’est vérifiée avant destruction de la cible.

**Exemple corrigé**

```python
restore_backup("backup.sqlite3", "game.sqlite3")
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la source et le staging sont validés avant le remplacement, puis la cible finale est revalidée.

### 14.5 Employer `REAL` pour un montant exact

**Symptôme ou risque :** les additions monétaires accumulent des écarts binaires.

**Exemple fautif**

```sql
price_eur REAL NOT NULL
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** `REAL` est un flottant binaire et ne garantit pas une arithmétique décimale exacte.

**Exemple corrigé**

```sql
price_cents INTEGER NOT NULL CHECK (price_cents >= 0),
currency_code TEXT NOT NULL CHECK (length(currency_code) = 3)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le montant utilise l’unité entière minimale et la devise est explicite. `1 299` représente `12,99 €` pour `EUR`.

## 15. Solo, Studio et nettoyage

En Solo, utiliser une base par workspace, des bases temporaires pour les tests et une copie avant toute migration destructive.

En Studio, faire relire chaque migration, interdire la réécriture des versions publiées, conserver la preuve de restauration, comparer les manifestes en CI et enregistrer les versions Python et SQLite.

> **[PS] PowerShell 7 — Supprimer uniquement les sorties locales.**

```powershell
Remove-Item -Recurse -Force .\dist -ErrorAction SilentlyContinue
Get-ChildItem -Recurse -Directory -Filter __pycache__ |
  Remove-Item -Recurse -Force
```

## 16. Validation du Pack

Les validations légères couvrent la structure, les manifestes, les migrations, les tests Python, la création depuis zéro, les montées depuis les versions antérieures, les repositories, la sauvegarde, la restauration, l’intégrité, les clés étrangères et l’absence de PDF.

Aucune mesure de débit, latence, concurrence, charge ou contention n’est déduite de ces tests.
