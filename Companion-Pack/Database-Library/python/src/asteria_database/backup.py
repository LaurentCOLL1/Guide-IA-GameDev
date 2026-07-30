from __future__ import annotations

import os
import shutil
import sqlite3
from pathlib import Path

from .connection import open_database
from .validation import validate_database


SIDE_CAR_SUFFIXES = ("-wal", "-shm")


def create_backup(
    source_path: str | Path,
    destination_path: str | Path,
) -> Path:
    """Create a consistent SQLite backup through the Online Backup API."""
    source = Path(source_path)
    destination = Path(destination_path)
    if not source.is_file():
        raise FileNotFoundError(source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        raise FileExistsError(destination)

    source_connection = open_database(source)
    destination_connection = sqlite3.connect(destination)
    try:
        source_connection.backup(destination_connection, pages=128, sleep=0.01)
    except Exception:
        destination_connection.close()
        source_connection.close()
        destination.unlink(missing_ok=True)
        raise
    else:
        destination_connection.close()
        source_connection.close()

    validate_database(destination)
    return destination


def restore_backup(
    backup_path: str | Path,
    target_path: str | Path,
) -> Path:
    """Validate a backup, stage it beside the target, then replace atomically."""
    backup = Path(backup_path)
    target = Path(target_path)
    validate_database(backup)
    target.parent.mkdir(parents=True, exist_ok=True)
    staged = target.with_name(target.name + ".restore.tmp")
    staged.unlink(missing_ok=True)

    shutil.copy2(backup, staged)
    with staged.open("rb") as handle:
        os.fsync(handle.fileno())
    validate_database(staged)

    for suffix in SIDE_CAR_SUFFIXES:
        target.with_name(target.name + suffix).unlink(missing_ok=True)
    os.replace(staged, target)
    validate_database(target)
    return target
