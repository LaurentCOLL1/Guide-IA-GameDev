#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sqlite3
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("tmp_l5_ch14_validate_sqlite.py")
SPEC = importlib.util.spec_from_file_location("l5_ch14_sqlite_fixtures", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Impossible de charger les fixtures SQLite.")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


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
