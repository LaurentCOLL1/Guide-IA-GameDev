from __future__ import annotations

import sqlite3
import tempfile
import unittest
from pathlib import Path

from asteria_database import (
    DatabaseIdentityError,
    DatabaseValidationError,
    MigrationRunner,
    open_database,
    seed_synthetic_data,
    validate_database,
)


class ValidationSyntheticTests(unittest.TestCase):
    def test_synthetic_fixture_is_deterministic_and_non_empty(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "synthetic.sqlite3"
            connection = open_database(path)
            try:
                MigrationRunner(connection).migrate()
                first = seed_synthetic_data(connection)
                second = seed_synthetic_data(connection)
                self.assertEqual(first, second)
                self.assertEqual(first["beacons"], 2)
                self.assertEqual(
                    connection.execute(
                        "SELECT COUNT(*) FROM beacon_state"
                    ).fetchone()[0],
                    2,
                )
                self.assertEqual(
                    connection.execute(
                        "SELECT COUNT(*) FROM content_document"
                    ).fetchone()[0],
                    2,
                )
            finally:
                connection.close()
            self.assertEqual(validate_database(path).status, "success")

    def test_wrong_application_id_is_refused(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "wrong.sqlite3"
            connection = open_database(path)
            try:
                MigrationRunner(connection).migrate()
                connection.execute("PRAGMA application_id = 1234")
            finally:
                connection.close()
            with self.assertRaises(DatabaseIdentityError):
                validate_database(path)

    def test_old_version_can_be_validated_only_when_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "old.sqlite3"
            connection = open_database(path)
            try:
                MigrationRunner(connection).migrate(2)
            finally:
                connection.close()
            with self.assertRaises(DatabaseValidationError):
                validate_database(path)
            report = validate_database(path, require_latest=False)
            self.assertEqual(report.user_version, 2)


if __name__ == "__main__":
    unittest.main()
