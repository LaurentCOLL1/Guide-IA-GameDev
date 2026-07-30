from __future__ import annotations
import argparse, shutil
from pathlib import Path

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    source = root / "godot/addons/asteria_code"
    target = root / "godot-example/addons/asteria_code"
    if target.exists():
        shutil.rmtree(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target)
    print(f"Prepared Godot example: {target}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
