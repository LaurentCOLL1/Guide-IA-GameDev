from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from asteria_database import (
    BeaconState,
    BeaconStateRepository,
    MigrationRunner,
    create_backup,
    open_database,
    restore_backup,
    validate_database,
)


class BackupRestoreTests(unittest.TestCase):
    def test_backup_and_restore_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            source = base / "source.sqlite3"
            backup = base / "backups" / "source-backup.sqlite3"
            restored = base / "restored.sqlite3"

            connection = open_database(source)
            try:
                MigrationRunner(connection).migrate()
                BeaconStateRepository(connection).save(
                    BeaconState(
                        beacon_id="beacon-backup",
                        is_enabled=True,
                        activation_count=7,
                        cooldown_remaining=0.0,
                        last_activated_at_utc=None,
                        updated_at_utc="2042-01-01T00:00:00Z",
                    )
                )
            finally:
                connection.close()

            self.assertEqual(create_backup(source, backup), backup)
            self.assertEqual(validate_database(backup).status, "success")
            self.assertEqual(restore_backup(backup, restored), restored)

            restored_connection = open_database(restored)
            try:
                restored_record = BeaconStateRepository(
                    restored_connection
                ).find("beacon-backup")
                self.assertIsNotNone(restored_record)
                self.assertEqual(restored_record.activation_count, 7)
            finally:
                restored_connection.close()

    def test_existing_backup_is_not_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            source = base / "source.sqlite3"
            backup = base / "backup.sqlite3"
            connection = open_database(source)
            try:
                MigrationRunner(connection).migrate()
            finally:
                connection.close()
            create_backup(source, backup)
            with self.assertRaises(FileExistsError):
                create_backup(source, backup)


if __name__ == "__main__":
    unittest.main()
