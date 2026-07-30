from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class ConnectionOptions:
    busy_timeout_ms: int = 3000
    journal_mode: str = "WAL"
    synchronous: str = "FULL"


def open_database(
    path: str | Path,
    *,
    read_only: bool = False,
    options: ConnectionOptions | None = None,
) -> sqlite3.Connection:
    """Open and configure one SQLite connection.

    Parameters:
        path: Database file path.
        read_only: Open through SQLite URI mode=ro when true.
        options: Busy timeout, journal mode and synchronous policy.

    Returns:
        A configured sqlite3.Connection with sqlite3.Row rows.

    Raises:
        ValueError: An option is outside the allowlist.
        sqlite3.Error: SQLite cannot open or configure the database.
    """
    options = options or ConnectionOptions()
    database_path = Path(path)
    if options.busy_timeout_ms < 0 or options.busy_timeout_ms > 60_000:
        raise ValueError("busy_timeout_ms must be between 0 and 60000")
    if options.journal_mode.upper() not in {"DELETE", "TRUNCATE", "PERSIST", "MEMORY", "WAL", "OFF"}:
        raise ValueError("journal_mode is not allowlisted")
    if options.synchronous.upper() not in {"OFF", "NORMAL", "FULL", "EXTRA"}:
        raise ValueError("synchronous is not allowlisted")

    if not read_only:
        database_path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(
            database_path,
            timeout=options.busy_timeout_ms / 1000,
            isolation_level=None,
        )
    else:
        uri = f"{database_path.resolve().as_uri()}?mode=ro"
        connection = sqlite3.connect(
            uri,
            uri=True,
            timeout=options.busy_timeout_ms / 1000,
            isolation_level=None,
        )

    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute(f"PRAGMA busy_timeout = {options.busy_timeout_ms}")
    connection.execute("PRAGMA trusted_schema = OFF")
    if not read_only:
        row = connection.execute(
            f"PRAGMA journal_mode = {options.journal_mode.upper()}"
        ).fetchone()
        if row is None or str(row[0]).upper() != options.journal_mode.upper():
            connection.close()
            raise sqlite3.OperationalError(
                f"SQLite did not accept journal_mode={options.journal_mode}"
            )
        connection.execute(f"PRAGMA synchronous = {options.synchronous.upper()}")
    return connection
