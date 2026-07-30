from __future__ import annotations

import sqlite3
from pathlib import Path

from .connection import open_database
from .errors import (
    DatabaseIdentityError,
    DatabaseValidationError,
    FutureSchemaError,
    MigrationIntegrityError,
)
from .migrations import MigrationRunner, load_manifest
from .models import ValidationReport


def validate_database(
    path: str | Path,
    *,
    require_latest: bool = True,
) -> ValidationReport:
    """Validate identity, version, integrity, foreign keys and migration history."""
    manifest = load_manifest()
    database_path = Path(path)
    if not database_path.is_file():
        raise DatabaseValidationError(f"database file does not exist: {database_path}")

    connection = open_database(database_path, read_only=True)
    try:
        application_id = int(
            connection.execute("PRAGMA application_id").fetchone()[0]
        )
        if application_id != manifest.application_id:
            raise DatabaseIdentityError(
                f"application_id {application_id} does not match "
                f"{manifest.application_id}"
            )

        user_version = int(connection.execute("PRAGMA user_version").fetchone()[0])
        if user_version > manifest.latest_version:
            raise FutureSchemaError(
                f"database version {user_version} is newer than "
                f"{manifest.latest_version}"
            )
        if require_latest and user_version != manifest.latest_version:
            raise DatabaseValidationError(
                f"database version {user_version} is not latest "
                f"{manifest.latest_version}"
            )

        quick_rows = connection.execute("PRAGMA quick_check").fetchall()
        quick_messages = tuple(str(row[0]) for row in quick_rows)
        if quick_messages != ("ok",):
            raise DatabaseValidationError(
                "quick_check failed: " + "; ".join(quick_messages)
            )

        foreign_rows = connection.execute("PRAGMA foreign_key_check").fetchall()
        violations = tuple(dict(row) for row in foreign_rows)
        if violations:
            raise DatabaseValidationError(
                f"foreign_key_check found {len(violations)} violation(s)"
            )

        runner = MigrationRunner(connection, manifest=manifest)
        runner.verify_history(user_version)
        migration_count = int(
            connection.execute(
                "SELECT COUNT(*) FROM schema_migrations"
            ).fetchone()[0]
        )
        if migration_count != user_version:
            raise MigrationIntegrityError(
                f"migration history count {migration_count} "
                f"does not match user_version {user_version}"
            )

        return ValidationReport(
            database_path=str(database_path),
            application_id=application_id,
            user_version=user_version,
            quick_check="ok",
            foreign_key_violations=violations,
            migration_count=migration_count,
            status="success",
        )
    finally:
        connection.close()
