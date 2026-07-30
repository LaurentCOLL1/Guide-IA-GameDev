from __future__ import annotations

import argparse
import json
from pathlib import Path

from asteria_database import (
    MigrationRunner,
    open_database,
    seed_synthetic_data,
    validate_database,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create or migrate an Asteria Database Library database."
    )
    parser.add_argument("database", type=Path)
    parser.add_argument(
        "--with-synthetic-data",
        action="store_true",
        help="Insert deterministic fictional fixtures.",
    )
    args = parser.parse_args()

    connection = open_database(args.database)
    try:
        version = MigrationRunner(connection).migrate()
        counts = (
            seed_synthetic_data(connection)
            if args.with_synthetic_data
            else {}
        )
    finally:
        connection.close()

    report = validate_database(args.database)
    print(
        json.dumps(
            {
                "status": report.status,
                "database": str(args.database),
                "user_version": version,
                "synthetic_counts": counts,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
