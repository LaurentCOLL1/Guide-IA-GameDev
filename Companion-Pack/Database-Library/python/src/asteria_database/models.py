from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class Migration:
    version: int
    name: str
    path: str
    sha256: str
    minimum_sqlite_version: str


@dataclass(frozen=True, slots=True)
class MigrationManifest:
    database_id: str
    application_id: int
    latest_version: int
    migrations: tuple[Migration, ...]


@dataclass(frozen=True, slots=True)
class BeaconState:
    beacon_id: str
    is_enabled: bool
    activation_count: int
    cooldown_remaining: float
    last_activated_at_utc: str | None
    updated_at_utc: str


@dataclass(frozen=True, slots=True)
class ContentDocument:
    document_id: str
    title: str
    body: str
    language_code: str
    content_version: int
    updated_at_utc: str


@dataclass(frozen=True, slots=True)
class ValidationReport:
    database_path: str
    application_id: int
    user_version: int
    quick_check: str
    foreign_key_violations: tuple[dict[str, Any], ...]
    migration_count: int
    status: str
