from __future__ import annotations


class DatabaseLibraryError(RuntimeError):
    """Base class for controlled Database Library failures."""


class DatabaseIdentityError(DatabaseLibraryError):
    """The SQLite application_id does not match the expected database family."""


class FutureSchemaError(DatabaseLibraryError):
    """The database schema version is newer than this library understands."""


class MigrationIntegrityError(DatabaseLibraryError):
    """An applied migration is missing, reordered, renamed, or has a divergent checksum."""


class DatabaseValidationError(DatabaseLibraryError):
    """The database failed a structural or integrity validation gate."""
