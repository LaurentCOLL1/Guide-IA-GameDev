from __future__ import annotations

import sqlite3
import tempfile
import unittest
from pathlib import Path

from asteria_database import (
    DatabaseIdentityError,
    FutureSchemaError,
    MigrationIntegrityError,
    MigrationRunner,
    load_manifest,
    open_database,
    validate_database,
)


class MigrationTests(unittest.TestCase):
    def test_create_from_zero_to_latest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "asteria.sqlite3"
            connection = open_database(path)
            try:
                version = MigrationRunner(connection).migrate()
                self.assertEqual(version, 4)
                self.assertEqual(
                    connection.execute("PRAGMA user_version").fetchone()[0],
                    4,
                )
                tables = {
                    row[0]
                    for row in connection.execute(
                        """
                        SELECT name
                        FROM sqlite_schema
                        WHERE type = 'table'
                        """
                    )
                }
                self.assertTrue(
                    {
                        "schema_migrations",
                        "beacon_state",
                        "beacon_activation_event",
                        "content_document",
                        "content_tag",
                        "content_document_tag",
                        "derived_cache_entry",
                    }.issubset(tables)
                )
            finally:
                connection.close()
            report = validate_database(path)
            self.assertEqual(report.status, "success")
            self.assertEqual(report.migration_count, 4)

    def test_upgrade_each_prior_version_to_latest(self) -> None:
        for target in range(0, 4):
            with self.subTest(target=target):
                with tempfile.TemporaryDirectory() as directory:
                    path = Path(directory) / f"v{target}.sqlite3"
                    connection = open_database(path)
                    try:
                        runner = MigrationRunner(connection)
                        runner.migrate(target)
                        self.assertEqual(
                            connection.execute(
                                "PRAGMA user_version"
                            ).fetchone()[0],
                            target,
                        )
                        self.assertEqual(runner.migrate(), 4)
                    finally:
                        connection.close()
                    self.assertEqual(validate_database(path).user_version, 4)

    def test_future_schema_is_refused_without_downgrade(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "future.sqlite3"
            connection = open_database(path)
            try:
                MigrationRunner(connection).migrate()
                connection.execute("PRAGMA user_version = 99")
                with self.assertRaises(FutureSchemaError):
                    MigrationRunner(connection).migrate()
            finally:
                connection.close()

    def test_migration_checksum_divergence_is_refused(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tampered.sqlite3"
            connection = open_database(path)
            try:
                MigrationRunner(connection).migrate()
                connection.execute(
                    """
                    UPDATE schema_migrations
                    SET checksum = ?
                    WHERE version = 2
                    """,
                    ("0" * 64,),
                )
                with self.assertRaises(MigrationIntegrityError):
                    MigrationRunner(connection).verify_history()
            finally:
                connection.close()

    def test_unknown_non_empty_database_is_not_adopted(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "foreign.sqlite3"
            raw = sqlite3.connect(path)
            raw.execute("CREATE TABLE foreign_table(id INTEGER)")
            raw.commit()
            raw.close()

            connection = open_database(path)
            try:
                with self.assertRaises(DatabaseIdentityError):
                    MigrationRunner(connection).migrate()
            finally:
                connection.close()


if __name__ == "__main__":
    unittest.main()
