from __future__ import annotations

import argparse
import json
from pathlib import Path

from asteria_database import restore_backup, validate_database


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate and atomically restore an Asteria SQLite backup."
    )
    parser.add_argument("backup", type=Path)
    parser.add_argument("target", type=Path)
    args = parser.parse_args()

    result = restore_backup(args.backup, args.target)
    report = validate_database(result)
    print(
        json.dumps(
            {
                "status": report.status,
                "restored": str(result),
                "user_version": report.user_version,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
