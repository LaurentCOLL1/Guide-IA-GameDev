from __future__ import annotations
import argparse
from pathlib import Path
from png_utils import write_checkerboard

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    write_checkerboard(args.output)
    print(args.output)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
