from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path
from typing import Iterable

from .errors import DatabaseIdentityError, FutureSchemaError, MigrationIntegrityError
from .models import Migration, MigrationManifest
from .util import pack_root, utc_now_text


def load_manifest(path: str | Path | None = None) -> MigrationManifest:
    manifest_path = Path(path) if path else pack_root() / "sql/migrations/manifest.json"
    raw = json.loads(manifest_path.read_text(encoding="utf-8"))
    migrations = tuple(
        Migration(
            version=int(item["version"]),
            name=str(item["name"]),
            path=str(item["path"]),
            sha256=str(item["sha256"]),
            minimum_sqlite_version=str(item["minimum_sqlite_version"]),
        )
        for item in raw["migrations"]
    )
    expected = list(range(1, len(migrations) + 1))
    actual = [migration.version for migration in migrations]
    if actual != expected:
        raise MigrationIntegrityError(
            f"migration versions must be contiguous from 1: {actual}"
        )
    if int(raw["latest_version"]) != len(migrations):
        raise MigrationIntegrityError("latest_version does not match the manifest")
    if len({migration.name for migration in migrations}) != len(migrations):
        raise MigrationIntegrityError("migration names must be unique")
    return MigrationManifest(
        database_id=str(raw["database_id"]),
        application_id=int(raw["application_id"]),
        latest_version=int(raw["latest_version"]),
        migrations=migrations,
    )


def split_sql_statements(sql_text: str) -> tuple[str, ...]:
    statements: list[str] = []
    buffer = ""
    for line in sql_text.splitlines(keepends=True):
        buffer += line
        if sqlite3.complete_statement(buffer):
            statement = buffer.strip()
            if statement:
                statements.append(statement)
            buffer = ""
    if buffer.strip():
        raise MigrationIntegrityError("incomplete SQL statement at end of migration")
    return tuple(statements)


class MigrationRunner:
    """Apply immutable, checksummed SQLite migrations in ascending order."""

    def __init__(
        self,
        connection: sqlite3.Connection,
        *,
        manifest: MigrationManifest | None = None,
        root: str | Path | None = None,
    ) -> None:
        self.connection = connection
        self.manifest = manifest or load_manifest()
        self.root = Path(root) if root else pack_root()

    def migrate(self, target_version: int | None = None) -> int:
        """Migrate the open database and return the installed user_version."""
        target = self.manifest.latest_version if target_version is None else int(target_version)
        if target < 0 or target > self.manifest.latest_version:
            raise ValueError("target_version is outside the manifest range")

        self._ensure_history_table()
        self._verify_or_initialize_identity()

        installed = self._user_version()
        if installed > self.manifest.latest_version:
            raise FutureSchemaError(
                f"database version {installed} is newer than supported "
                f"{self.manifest.latest_version}"
            )
        if installed > target:
            raise FutureSchemaError(
                f"automatic downgrade from {installed} to {target} is forbidden"
            )

        self.verify_history(installed)
        for migration in self.manifest.migrations:
            if installed < migration.version <= target:
                self._apply(migration)
                installed = migration.version
        self.verify_history(installed)
        return installed

    def verify_history(self, installed_version: int | None = None) -> None:
        installed = self._user_version() if installed_version is None else installed_version
        rows = self.connection.execute(
            """
            SELECT version, name, checksum
            FROM schema_migrations
            ORDER BY version
            """
        ).fetchall()
        by_version = {int(row["version"]): row for row in rows}
        if len(by_version) != len(rows):
            raise MigrationIntegrityError("duplicate versions in schema_migrations")
        for migration in self.manifest.migrations:
            if migration.version > installed:
                continue
            row = by_version.get(migration.version)
            if row is None:
                raise MigrationIntegrityError(
                    f"applied migration {migration.version} is missing from history"
                )
            if str(row["name"]) != migration.name:
                raise MigrationIntegrityError(
                    f"migration {migration.version} name diverged"
                )
            if str(row["checksum"]) != migration.sha256:
                raise MigrationIntegrityError(
                    f"migration {migration.version} checksum diverged"
                )
        unexpected = [version for version in by_version if version > installed]
        if unexpected:
            raise MigrationIntegrityError(
                f"history contains versions newer than user_version: {unexpected}"
            )

    def _ensure_history_table(self) -> None:
        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS schema_migrations (
                version INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                checksum TEXT NOT NULL CHECK (length(checksum) = 64),
                applied_at_utc TEXT NOT NULL
            ) STRICT
            """
        )

    def _verify_or_initialize_identity(self) -> None:
        application_id = int(
            self.connection.execute("PRAGMA application_id").fetchone()[0]
        )
        if application_id == self.manifest.application_id:
            return
        if application_id != 0:
            raise DatabaseIdentityError(
                f"application_id {application_id} does not match "
                f"{self.manifest.application_id}"
            )
        user_tables = self.connection.execute(
            """
            SELECT name
            FROM sqlite_schema
            WHERE type = 'table'
              AND name NOT LIKE 'sqlite_%'
              AND name <> 'schema_migrations'
            ORDER BY name
            """
        ).fetchall()
        if user_tables or self._user_version() != 0:
            raise DatabaseIdentityError(
                "unidentified non-empty database cannot be adopted automatically"
            )
        self.connection.execute(
            f"PRAGMA application_id = {self.manifest.application_id}"
        )

    def _user_version(self) -> int:
        return int(self.connection.execute("PRAGMA user_version").fetchone()[0])

    def _apply(self, migration: Migration) -> None:
        path = self.root / migration.path
        payload = path.read_bytes()
        checksum = hashlib.sha256(payload).hexdigest()
        if checksum != migration.sha256:
            raise MigrationIntegrityError(
                f"migration file checksum diverged: {migration.path}"
            )
        sql_text = payload.decode("utf-8")
        statements = split_sql_statements(sql_text)
        if not statements:
            raise MigrationIntegrityError(f"empty migration: {migration.path}")

        minimum = tuple(int(part) for part in migration.minimum_sqlite_version.split("."))
        if sqlite3.sqlite_version_info < minimum:
            raise MigrationIntegrityError(
                f"SQLite {sqlite3.sqlite_version} is older than "
                f"{migration.minimum_sqlite_version}"
            )

        try:
            self.connection.execute("BEGIN IMMEDIATE")
            for statement in statements:
                self.connection.execute(statement)
            self.connection.execute(
                """
                INSERT INTO schema_migrations(
                    version, name, checksum, applied_at_utc
                ) VALUES (?, ?, ?, ?)
                """,
                (
                    migration.version,
                    migration.name,
                    migration.sha256,
                    utc_now_text(),
                ),
            )
            self.connection.execute(
                f"PRAGMA user_version = {migration.version}"
            )
            self.connection.execute("COMMIT")
        except Exception:
            if self.connection.in_transaction:
                self.connection.execute("ROLLBACK")
            raise
