#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import platform
import sqlite3
import tempfile
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "dist/QA-LIVRE-V-CH14-SQLITE.json"
EXPECTED_CASES = 36
APPLICATION_ID = 0x41535452  # ASCII "ASTR"

CASES: list[tuple[str, Callable[[Path], None]]] = []


def case(name: str) -> Callable[[Callable[[Path], None]], Callable[[Path], None]]:
    def register(function: Callable[[Path], None]) -> Callable[[Path], None]:
        CASES.append((name, function))
        return function
    return register


def connect(path: Path, *, foreign_keys: bool = True) -> sqlite3.Connection:
    connection = sqlite3.connect(path, isolation_level=None)
    connection.row_factory = sqlite3.Row
    if foreign_keys:
        connection.execute("PRAGMA foreign_keys = ON;")
    connection.execute("PRAGMA trusted_schema = OFF;")
    connection.execute("PRAGMA busy_timeout = 1500;")
    return connection


def expect_raises(error_type: type[BaseException], action: Callable[[], object]) -> None:
    try:
        action()
    except error_type:
        return
    raise AssertionError(f"{error_type.__name__} was not raised")


REFERENCE_DDL = """
CREATE TABLE schema_migrations (
    version INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    checksum TEXT NOT NULL CHECK (length(checksum) = 64),
    applied_at_utc TEXT NOT NULL
) STRICT;

CREATE TABLE beacon_state (
    beacon_id TEXT PRIMARY KEY,
    is_enabled INTEGER NOT NULL DEFAULT 1
        CHECK (is_enabled IN (0, 1)),
    activation_count INTEGER NOT NULL DEFAULT 0
        CHECK (activation_count >= 0),
    updated_at_utc TEXT NOT NULL
) STRICT;

CREATE TABLE beacon_activation_event (
    event_id INTEGER PRIMARY KEY,
    beacon_id TEXT NOT NULL,
    actor_id TEXT NOT NULL,
    occurred_at_utc TEXT NOT NULL,
    FOREIGN KEY (beacon_id)
        REFERENCES beacon_state(beacon_id)
        ON DELETE CASCADE
) STRICT;

CREATE INDEX idx_beacon_event_beacon_time
    ON beacon_activation_event(beacon_id, occurred_at_utc);
""".strip()


def create_reference_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(REFERENCE_DDL)


def migration_checksum(sql: str) -> str:
    return hashlib.sha256(sql.encode("utf-8")).hexdigest()


def apply_v1(connection: sqlite3.Connection) -> str:
    checksum = migration_checksum(REFERENCE_DDL)
    connection.execute("BEGIN IMMEDIATE;")
    try:
        create_reference_schema(connection)
        connection.execute(
            """
            INSERT INTO schema_migrations(version, name, checksum, applied_at_utc)
            VALUES (?, ?, ?, ?);
            """,
            (1, "create_reference_schema", checksum, "2026-07-29T00:00:00Z"),
        )
        connection.execute("PRAGMA application_id = %d;" % APPLICATION_ID)
        connection.execute("PRAGMA user_version = 1;")
        connection.execute("COMMIT;")
    except Exception:
        connection.execute("ROLLBACK;")
        raise
    return checksum


def apply_v2(connection: sqlite3.Connection) -> str:
    sql = """
    ALTER TABLE beacon_state
        ADD COLUMN last_activated_at_utc TEXT;
    """.strip()
    checksum = migration_checksum(sql)
    connection.execute("BEGIN IMMEDIATE;")
    try:
        connection.execute(sql)
        connection.execute(
            """
            INSERT INTO schema_migrations(version, name, checksum, applied_at_utc)
            VALUES (?, ?, ?, ?);
            """,
            (2, "add_last_activated_at", checksum, "2026-07-29T00:01:00Z"),
        )
        connection.execute("PRAGMA user_version = 2;")
        connection.execute("COMMIT;")
    except Exception:
        connection.execute("ROLLBACK;")
        raise
    return checksum


def verify_manifest(connection: sqlite3.Connection, expected: dict[int, tuple[str, str]]) -> None:
    rows = connection.execute(
        "SELECT version, name, checksum FROM schema_migrations ORDER BY version;"
    ).fetchall()
    observed = {
        int(row["version"]): (str(row["name"]), str(row["checksum"]))
        for row in rows
    }
    if observed != expected:
        raise ValueError(f"migration history mismatch: {observed!r}")


def guard_identity(connection: sqlite3.Connection, *, latest_version: int) -> None:
    application_id = int(connection.execute("PRAGMA application_id;").fetchone()[0])
    user_version = int(connection.execute("PRAGMA user_version;").fetchone()[0])
    if application_id != APPLICATION_ID:
        raise ValueError("unexpected application_id")
    if user_version > latest_version:
        raise ValueError("future schema version")


@case("runtime.sqlite_version_supports_strict")
def _(root: Path) -> None:
    version = tuple(int(part) for part in sqlite3.sqlite_version.split(".")[:3])
    assert version >= (3, 37, 0)


@case("runtime.compile_options_available")
def _(root: Path) -> None:
    with connect(root / "compile.sqlite3") as connection:
        rows = connection.execute("PRAGMA compile_options;").fetchall()
        assert len(rows) > 0


@case("pragma.application_id_roundtrip")
def _(root: Path) -> None:
    with connect(root / "app-id.sqlite3") as connection:
        connection.execute("PRAGMA application_id = %d;" % APPLICATION_ID)
        assert int(connection.execute("PRAGMA application_id;").fetchone()[0]) == APPLICATION_ID


@case("pragma.user_version_roundtrip")
def _(root: Path) -> None:
    with connect(root / "user-version.sqlite3") as connection:
        connection.execute("PRAGMA user_version = 7;")
        assert int(connection.execute("PRAGMA user_version;").fetchone()[0]) == 7


@case("pragma.foreign_keys_enabled")
def _(root: Path) -> None:
    with connect(root / "foreign-keys.sqlite3") as connection:
        assert int(connection.execute("PRAGMA foreign_keys;").fetchone()[0]) == 1


@case("pragma.trusted_schema_disabled")
def _(root: Path) -> None:
    with connect(root / "trusted-schema.sqlite3") as connection:
        assert int(connection.execute("PRAGMA trusted_schema;").fetchone()[0]) == 0


@case("ddl.strict_tables_created")
def _(root: Path) -> None:
    with connect(root / "strict-schema.sqlite3") as connection:
        create_reference_schema(connection)
        rows = connection.execute("PRAGMA table_list;").fetchall()
        strict_by_name = {str(row[1]): int(row[5]) for row in rows}
        assert strict_by_name["beacon_state"] == 1
        assert strict_by_name["beacon_activation_event"] == 1


@case("strict.integer_rejects_text")
def _(root: Path) -> None:
    with connect(root / "strict-type.sqlite3") as connection:
        create_reference_schema(connection)
        expect_raises(
            sqlite3.IntegrityError,
            lambda: connection.execute(
                """
                INSERT INTO beacon_state(beacon_id, is_enabled, activation_count, updated_at_utc)
                VALUES ('beacon.a', 1, 'not-an-integer', '2026-07-29T00:00:00Z');
                """
            ),
        )


@case("constraint.boolean_check_rejects_two")
def _(root: Path) -> None:
    with connect(root / "check-bool.sqlite3") as connection:
        create_reference_schema(connection)
        expect_raises(
            sqlite3.IntegrityError,
            lambda: connection.execute(
                """
                INSERT INTO beacon_state(beacon_id, is_enabled, activation_count, updated_at_utc)
                VALUES ('beacon.a', 2, 0, '2026-07-29T00:00:00Z');
                """
            ),
        )


@case("constraint.not_null_rejects_null")
def _(root: Path) -> None:
    with connect(root / "not-null.sqlite3") as connection:
        create_reference_schema(connection)
        expect_raises(
            sqlite3.IntegrityError,
            lambda: connection.execute(
                "INSERT INTO beacon_state(beacon_id, updated_at_utc) VALUES ('beacon.a', NULL);"
            ),
        )


@case("constraint.primary_key_rejects_duplicate")
def _(root: Path) -> None:
    with connect(root / "primary-key.sqlite3") as connection:
        create_reference_schema(connection)
        connection.execute(
            "INSERT INTO beacon_state(beacon_id, updated_at_utc) VALUES (?, ?);",
            ("beacon.a", "2026-07-29T00:00:00Z"),
        )
        expect_raises(
            sqlite3.IntegrityError,
            lambda: connection.execute(
                "INSERT INTO beacon_state(beacon_id, updated_at_utc) VALUES (?, ?);",
                ("beacon.a", "2026-07-29T00:00:01Z"),
            ),
        )


@case("foreign_key.orphan_rejected")
def _(root: Path) -> None:
    with connect(root / "fk-orphan.sqlite3") as connection:
        create_reference_schema(connection)
        expect_raises(
            sqlite3.IntegrityError,
            lambda: connection.execute(
                """
                INSERT INTO beacon_activation_event(beacon_id, actor_id, occurred_at_utc)
                VALUES ('beacon.missing', 'actor.a', '2026-07-29T00:00:00Z');
                """
            ),
        )


@case("foreign_key.cascade_deletes_child")
def _(root: Path) -> None:
    with connect(root / "fk-cascade.sqlite3") as connection:
        create_reference_schema(connection)
        connection.execute(
            "INSERT INTO beacon_state(beacon_id, updated_at_utc) VALUES (?, ?);",
            ("beacon.a", "2026-07-29T00:00:00Z"),
        )
        connection.execute(
            """
            INSERT INTO beacon_activation_event(beacon_id, actor_id, occurred_at_utc)
            VALUES (?, ?, ?);
            """,
            ("beacon.a", "actor.a", "2026-07-29T00:00:01Z"),
        )
        connection.execute("DELETE FROM beacon_state WHERE beacon_id = ?;", ("beacon.a",))
        count = int(connection.execute("SELECT count(*) FROM beacon_activation_event;").fetchone()[0])
        assert count == 0


@case("foreign_key.deferred_commit_after_parent")
def _(root: Path) -> None:
    with connect(root / "fk-deferred.sqlite3") as connection:
        connection.executescript(
            """
            CREATE TABLE parent(id INTEGER PRIMARY KEY) STRICT;
            CREATE TABLE child(
                id INTEGER PRIMARY KEY,
                parent_id INTEGER NOT NULL,
                FOREIGN KEY(parent_id) REFERENCES parent(id)
                    DEFERRABLE INITIALLY DEFERRED
            ) STRICT;
            """
        )
        connection.execute("BEGIN;")
        connection.execute("INSERT INTO child(id, parent_id) VALUES (1, 7);")
        connection.execute("INSERT INTO parent(id) VALUES (7);")
        connection.execute("COMMIT;")
        assert int(connection.execute("SELECT count(*) FROM child;").fetchone()[0]) == 1


@case("transaction.rollback_reverts_insert")
def _(root: Path) -> None:
    with connect(root / "rollback.sqlite3") as connection:
        create_reference_schema(connection)
        connection.execute("BEGIN IMMEDIATE;")
        connection.execute(
            "INSERT INTO beacon_state(beacon_id, updated_at_utc) VALUES (?, ?);",
            ("beacon.a", "2026-07-29T00:00:00Z"),
        )
        connection.execute("ROLLBACK;")
        assert int(connection.execute("SELECT count(*) FROM beacon_state;").fetchone()[0]) == 0


@case("savepoint.rollback_to_reverts_subunit")
def _(root: Path) -> None:
    with connect(root / "savepoint.sqlite3") as connection:
        create_reference_schema(connection)
        connection.execute("BEGIN;")
        connection.execute(
            "INSERT INTO beacon_state(beacon_id, updated_at_utc) VALUES (?, ?);",
            ("beacon.a", "2026-07-29T00:00:00Z"),
        )
        connection.execute("SAVEPOINT optional_event;")
        connection.execute(
            """
            INSERT INTO beacon_activation_event(beacon_id, actor_id, occurred_at_utc)
            VALUES (?, ?, ?);
            """,
            ("beacon.a", "actor.a", "2026-07-29T00:00:01Z"),
        )
        connection.execute("ROLLBACK TO optional_event;")
        connection.execute("RELEASE optional_event;")
        connection.execute("COMMIT;")
        assert int(connection.execute("SELECT count(*) FROM beacon_state;").fetchone()[0]) == 1
        assert int(connection.execute("SELECT count(*) FROM beacon_activation_event;").fetchone()[0]) == 0


@case("binding.apostrophe_preserved")
def _(root: Path) -> None:
    with connect(root / "binding.sqlite3") as connection:
        connection.execute("CREATE TABLE note(value TEXT NOT NULL) STRICT;")
        value = "l'objet d'Ariane"
        connection.execute("INSERT INTO note(value) VALUES (?);", (value,))
        assert str(connection.execute("SELECT value FROM note;").fetchone()[0]) == value


@case("migration.v1_applies")
def _(root: Path) -> None:
    with connect(root / "migration-v1.sqlite3") as connection:
        apply_v1(connection)
        guard_identity(connection, latest_version=2)
        assert int(connection.execute("PRAGMA user_version;").fetchone()[0]) == 1


@case("migration.history_checksum_matches")
def _(root: Path) -> None:
    with connect(root / "migration-checksum.sqlite3") as connection:
        checksum = apply_v1(connection)
        verify_manifest(connection, {1: ("create_reference_schema", checksum)})


@case("migration.checksum_divergence_detected")
def _(root: Path) -> None:
    with connect(root / "migration-divergence.sqlite3") as connection:
        checksum = apply_v1(connection)
        connection.execute(
            "UPDATE schema_migrations SET checksum = ? WHERE version = 1;",
            ("0" * 64,),
        )
        expect_raises(
            ValueError,
            lambda: verify_manifest(connection, {1: ("create_reference_schema", checksum)}),
        )


@case("migration.future_version_rejected")
def _(root: Path) -> None:
    with connect(root / "future-version.sqlite3") as connection:
        connection.execute("PRAGMA application_id = %d;" % APPLICATION_ID)
        connection.execute("PRAGMA user_version = 99;")
        expect_raises(ValueError, lambda: guard_identity(connection, latest_version=2))


@case("migration.v2_applies_after_v1")
def _(root: Path) -> None:
    with connect(root / "migration-v2.sqlite3") as connection:
        checksum_v1 = apply_v1(connection)
        checksum_v2 = apply_v2(connection)
        verify_manifest(
            connection,
            {
                1: ("create_reference_schema", checksum_v1),
                2: ("add_last_activated_at", checksum_v2),
            },
        )
        columns = {str(row[1]) for row in connection.execute("PRAGMA table_xinfo('beacon_state');")}
        assert "last_activated_at_utc" in columns


@case("alter.add_column_default_backfills_old_rows")
def _(root: Path) -> None:
    with connect(root / "alter-add.sqlite3") as connection:
        connection.execute("CREATE TABLE sample(id INTEGER PRIMARY KEY) STRICT;")
        connection.execute("INSERT INTO sample DEFAULT VALUES;")
        connection.execute("ALTER TABLE sample ADD COLUMN enabled INTEGER NOT NULL DEFAULT 1;")
        assert int(connection.execute("SELECT enabled FROM sample;").fetchone()[0]) == 1


@case("alter.rebuild_table_preserves_rows")
def _(root: Path) -> None:
    with connect(root / "alter-rebuild.sqlite3") as connection:
        connection.execute("CREATE TABLE item(id INTEGER PRIMARY KEY, value INTEGER) STRICT;")
        connection.executemany("INSERT INTO item(value) VALUES (?);", [(1,), (2,), (3,)])
        connection.execute("BEGIN IMMEDIATE;")
        try:
            connection.execute(
                "CREATE TABLE item_new(id INTEGER PRIMARY KEY, value INTEGER NOT NULL CHECK(value >= 0)) STRICT;"
            )
            connection.execute("INSERT INTO item_new(id, value) SELECT id, value FROM item;")
            connection.execute("DROP TABLE item;")
            connection.execute("ALTER TABLE item_new RENAME TO item;")
            connection.execute("COMMIT;")
        except Exception:
            connection.execute("ROLLBACK;")
            raise
        assert int(connection.execute("SELECT count(*) FROM item;").fetchone()[0]) == 3


@case("index.composite_exists")
def _(root: Path) -> None:
    with connect(root / "index-list.sqlite3") as connection:
        create_reference_schema(connection)
        names = {str(row[1]) for row in connection.execute("PRAGMA index_list('beacon_activation_event');")}
        assert "idx_beacon_event_beacon_time" in names


@case("plan.uses_composite_index")
def _(root: Path) -> None:
    with connect(root / "query-plan.sqlite3") as connection:
        create_reference_schema(connection)
        connection.execute(
            "INSERT INTO beacon_state(beacon_id, updated_at_utc) VALUES (?, ?);",
            ("beacon.a", "2026-07-29T00:00:00Z"),
        )
        connection.executemany(
            """
            INSERT INTO beacon_activation_event(beacon_id, actor_id, occurred_at_utc)
            VALUES (?, ?, ?);
            """,
            [
                ("beacon.a", f"actor.{index}", f"2026-07-29T00:00:{index:02d}Z")
                for index in range(10)
            ],
        )
        rows = connection.execute(
            """
            EXPLAIN QUERY PLAN
            SELECT event_id, occurred_at_utc
            FROM beacon_activation_event
            WHERE beacon_id = ?
            ORDER BY occurred_at_utc;
            """,
            ("beacon.a",),
        ).fetchall()
        details = "\n".join(str(row[3]) for row in rows)
        assert "idx_beacon_event_beacon_time" in details


@case("diagnostic.quick_check_ok")
def _(root: Path) -> None:
    with connect(root / "quick-check.sqlite3") as connection:
        create_reference_schema(connection)
        assert str(connection.execute("PRAGMA quick_check;").fetchone()[0]) == "ok"


@case("diagnostic.integrity_check_ok")
def _(root: Path) -> None:
    with connect(root / "integrity-check.sqlite3") as connection:
        create_reference_schema(connection)
        assert str(connection.execute("PRAGMA integrity_check;").fetchone()[0]) == "ok"


@case("diagnostic.foreign_key_check_empty")
def _(root: Path) -> None:
    with connect(root / "foreign-key-check.sqlite3") as connection:
        create_reference_schema(connection)
        assert connection.execute("PRAGMA foreign_key_check;").fetchall() == []


@case("backup.online_snapshot_preserves_state")
def _(root: Path) -> None:
    source_path = root / "backup-source.sqlite3"
    backup_path = root / "backup-destination.sqlite3"
    source = connect(source_path)
    try:
        create_reference_schema(source)
        source.execute(
            "INSERT INTO beacon_state(beacon_id, updated_at_utc) VALUES (?, ?);",
            ("beacon.a", "2026-07-29T00:00:00Z"),
        )
        destination = connect(backup_path)
        try:
            source.backup(destination)
        finally:
            destination.close()
        source.execute(
            "INSERT INTO beacon_state(beacon_id, updated_at_utc) VALUES (?, ?);",
            ("beacon.b", "2026-07-29T00:00:01Z"),
        )
    finally:
        source.close()
    with connect(backup_path) as backup:
        assert int(backup.execute("SELECT count(*) FROM beacon_state;").fetchone()[0]) == 1
        assert str(backup.execute("PRAGMA quick_check;").fetchone()[0]) == "ok"


@case("backup.vacuum_into_creates_valid_copy")
def _(root: Path) -> None:
    source_path = root / "vacuum-source.sqlite3"
    copy_path = root / "vacuum-copy.sqlite3"
    with connect(source_path) as source:
        create_reference_schema(source)
        source.execute(
            "INSERT INTO beacon_state(beacon_id, updated_at_utc) VALUES (?, ?);",
            ("beacon.a", "2026-07-29T00:00:00Z"),
        )
        escaped = str(copy_path).replace("'", "''")
        source.execute(f"VACUUM INTO '{escaped}';")
    with connect(copy_path) as copied:
        assert int(copied.execute("SELECT count(*) FROM beacon_state;").fetchone()[0]) == 1
        assert str(copied.execute("PRAGMA integrity_check;").fetchone()[0]) == "ok"


@case("wal.mode_confirmed")
def _(root: Path) -> None:
    with connect(root / "wal.sqlite3") as connection:
        mode = str(connection.execute("PRAGMA journal_mode = WAL;").fetchone()[0]).lower()
        assert mode == "wal"


@case("pragma.busy_timeout_roundtrip")
def _(root: Path) -> None:
    with connect(root / "busy-timeout.sqlite3") as connection:
        connection.execute("PRAGMA busy_timeout = 2345;")
        assert int(connection.execute("PRAGMA busy_timeout;").fetchone()[0]) == 2345


@case("without_rowid.rowid_is_unavailable")
def _(root: Path) -> None:
    with connect(root / "without-rowid.sqlite3") as connection:
        connection.execute(
            "CREATE TABLE catalog(key TEXT PRIMARY KEY, value TEXT NOT NULL) WITHOUT ROWID;"
        )
        connection.execute("INSERT INTO catalog(key, value) VALUES ('a', 'A');")
        expect_raises(sqlite3.OperationalError, lambda: connection.execute("SELECT rowid FROM catalog;").fetchall())


@case("identity.application_id_mismatch_rejected")
def _(root: Path) -> None:
    with connect(root / "identity-mismatch.sqlite3") as connection:
        connection.execute("PRAGMA application_id = 123;")
        connection.execute("PRAGMA user_version = 1;")
        expect_raises(ValueError, lambda: guard_identity(connection, latest_version=2))


def main() -> int:
    if len(CASES) != EXPECTED_CASES:
        raise RuntimeError(f"Expected {EXPECTED_CASES} cases, found {len(CASES)}")

    results: list[dict[str, str]] = []
    failed = 0
    with tempfile.TemporaryDirectory(prefix="l5-ch14-sqlite-") as directory:
        root = Path(directory)
        for name, action in CASES:
            try:
                action(root)
            except Exception as exc:  # bounded test report
                failed += 1
                results.append(
                    {
                        "name": name,
                        "status": "failed",
                        "detail": f"{type(exc).__name__}: {exc}",
                    }
                )
            else:
                results.append({"name": name, "status": "passed", "detail": ""})

    with sqlite3.connect(":memory:") as probe:
        compile_options = [str(row[0]) for row in probe.execute("PRAGMA compile_options;")]

    report = {
        "schema_version": 1,
        "scope": "temporary-synthetic-sqlite-databases",
        "python_version": platform.python_version(),
        "sqlite_module_version": sqlite3.version,
        "sqlite_runtime_version": sqlite3.sqlite_version,
        "platform": platform.platform(),
        "compile_options": compile_options,
        "total": len(results),
        "passed": len(results) - failed,
        "failed": failed,
        "cases": results,
        "reservations": [
            "No Godot binary, GDExtension, addon or project was loaded.",
            "Only synthetic temporary SQLite databases were created.",
            "No user, production, network, secret, personal or Companion Pack data was processed.",
            "No multi-process contention, load, fuzzing or adversarial campaign was executed.",
            "The results qualify only the recorded Python sqlite3 runtime and fixture scope.",
        ],
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "sqlite": report["sqlite_runtime_version"],
                "total": report["total"],
                "passed": report["passed"],
                "failed": report["failed"],
            }
        )
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
