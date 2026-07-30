from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from asteria_database import (
    BeaconState,
    BeaconStateRepository,
    ContentDocument,
    ContentDocumentRepository,
    MigrationRunner,
    open_database,
)


class RepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.path = Path(self.directory.name) / "repository.sqlite3"
        self.connection = open_database(self.path)
        MigrationRunner(self.connection).migrate()

    def tearDown(self) -> None:
        self.connection.close()
        self.directory.cleanup()

    def test_beacon_round_trip_and_cascade(self) -> None:
        repository = BeaconStateRepository(self.connection)
        record = BeaconState(
            beacon_id="beacon-alpha",
            is_enabled=True,
            activation_count=3,
            cooldown_remaining=1.5,
            last_activated_at_utc="2042-01-01T00:00:00Z",
            updated_at_utc="2042-01-01T00:00:01Z",
        )
        repository.save(record)
        self.assertEqual(repository.find("beacon-alpha"), record)
        event_id = repository.add_event(
            beacon_id="beacon-alpha",
            actor_id="actor-synthetic",
            occurred_at_utc="2042-01-01T00:00:02Z",
        )
        self.assertGreater(event_id, 0)
        self.assertEqual(len(repository.list_recent_events("beacon-alpha")), 1)
        self.assertTrue(repository.delete("beacon-alpha"))
        count = self.connection.execute(
            "SELECT COUNT(*) FROM beacon_activation_event"
        ).fetchone()[0]
        self.assertEqual(count, 0)

    def test_sql_injection_payload_is_only_a_value(self) -> None:
        repository = BeaconStateRepository(self.connection)
        payload = "x'; DROP TABLE beacon_state; --"
        self.assertIsNone(repository.find(payload))
        self.connection.execute("SELECT COUNT(*) FROM beacon_state").fetchone()

    def test_repository_rejects_invalid_numbers(self) -> None:
        repository = BeaconStateRepository(self.connection)
        with self.assertRaises(ValueError):
            repository.save(
                BeaconState(
                    beacon_id="bad",
                    is_enabled=True,
                    activation_count=-1,
                    cooldown_remaining=0.0,
                    last_activated_at_utc=None,
                    updated_at_utc="2042-01-01T00:00:00Z",
                )
            )

    def test_content_tags_are_normalized(self) -> None:
        repository = ContentDocumentRepository(self.connection)
        document = ContentDocument(
            document_id="doc-alpha",
            title="Document Alpha",
            body="Texte synthétique.",
            language_code="fr-FR",
            content_version=1,
            updated_at_utc="2042-01-01T00:00:00Z",
        )
        repository.save(document)
        repository.upsert_tag("tag-lore", "Lore")
        repository.assign_tag(document.document_id, "tag-lore")
        self.assertEqual(repository.search_by_tag("tag-lore"), (document,))


if __name__ == "__main__":
    unittest.main()
