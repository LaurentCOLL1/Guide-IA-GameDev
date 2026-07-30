from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from asteria_database import validate_database


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate an Asteria Database Library database."
    )
    parser.add_argument("database", type=Path)
    parser.add_argument(
        "--allow-prior-version",
        action="store_true",
        help="Accept a supported version below the current manifest.",
    )
    args = parser.parse_args()
    report = validate_database(
        args.database,
        require_latest=not args.allow_prior_version,
    )
    print(json.dumps(asdict(report), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
