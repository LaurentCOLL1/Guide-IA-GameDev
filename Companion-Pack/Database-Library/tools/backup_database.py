from __future__ import annotations

import argparse
import json
from pathlib import Path

from asteria_database import create_backup, validate_database


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a validated SQLite backup through the Backup API."
    )
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()

    result = create_backup(args.source, args.destination)
    report = validate_database(result)
    print(
        json.dumps(
            {
                "status": report.status,
                "backup": str(result),
                "user_version": report.user_version,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
