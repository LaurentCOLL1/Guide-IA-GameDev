#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("tmp_l5_ch14_validate_sqlite.py")
SPEC = importlib.util.spec_from_file_location("l5_ch14_sqlite_fixtures", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Impossible de charger les fixtures SQLite.")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


def create_reference_schema_transactionally(connection) -> None:
    statements = (
        """
        CREATE TABLE schema_migrations (
            version INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            checksum TEXT NOT NULL CHECK (length(checksum) = 64),
            applied_at_utc TEXT NOT NULL
        ) STRICT;
        """,
        """
        CREATE TABLE beacon_state (
            beacon_id TEXT PRIMARY KEY,
            is_enabled INTEGER NOT NULL DEFAULT 1
                CHECK (is_enabled IN (0, 1)),
            activation_count INTEGER NOT NULL DEFAULT 0
                CHECK (activation_count >= 0),
            updated_at_utc TEXT NOT NULL
        ) STRICT;
        """,
        """
        CREATE TABLE beacon_activation_event (
            event_id INTEGER PRIMARY KEY,
            beacon_id TEXT NOT NULL,
            actor_id TEXT NOT NULL,
            occurred_at_utc TEXT NOT NULL,
            FOREIGN KEY (beacon_id)
                REFERENCES beacon_state(beacon_id)
                ON DELETE CASCADE
        ) STRICT;
        """,
        """
        CREATE INDEX idx_beacon_event_beacon_time
            ON beacon_activation_event(beacon_id, occurred_at_utc);
        """,
    )
    for statement in statements:
        connection.execute(statement)


module.create_reference_schema = create_reference_schema_transactionally


@module.case("pragma.schema_version_changes_without_user_version")
def _(root: Path) -> None:
    with module.connect(root / "schema-version.sqlite3") as connection:
        before_schema = int(connection.execute("PRAGMA schema_version;").fetchone()[0])
        before_user = int(connection.execute("PRAGMA user_version;").fetchone()[0])
        connection.execute("CREATE TABLE sample(id INTEGER PRIMARY KEY) STRICT;")
        after_schema = int(connection.execute("PRAGMA schema_version;").fetchone()[0])
        after_user = int(connection.execute("PRAGMA user_version;").fetchone()[0])
        assert after_schema > before_schema
        assert after_user == before_user == 0


if __name__ == "__main__":
    raise SystemExit(module.main())
