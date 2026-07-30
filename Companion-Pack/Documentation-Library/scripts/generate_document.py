#!/usr/bin/env python3
"""Generate one document or a batch from explicit {{TOKEN}} templates."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

TOKEN_RE = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


def load_json(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return data


def render(template_text: str, values: dict[str, object]) -> str:
    required = set(TOKEN_RE.findall(template_text))
    missing = sorted(required - values.keys())
    if missing:
        raise ValueError("missing tokens: " + ", ".join(missing))
    unused = sorted(values.keys() - required)
    if unused:
        raise ValueError("unused values: " + ", ".join(unused))
    rendered = template_text
    for key in sorted(required, key=len, reverse=True):
        value = values[key]
        if not isinstance(value, (str, int, float, bool)) and value is not None:
            raise ValueError(f"{key}: scalar value required")
        rendered = rendered.replace("{{" + key + "}}", "" if value is None else str(value))
    unresolved = TOKEN_RE.findall(rendered)
    if unresolved:
        raise ValueError("unresolved tokens: " + ", ".join(sorted(set(unresolved))))
    return rendered.rstrip() + "\n"


def generate_one(root: Path, template: Path, data: Path, output: Path) -> None:
    template_path = root / template
    data_path = root / data
    output_path = root / output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    text = render(template_path.read_text(encoding="utf-8"), load_json(data_path))
    output_path.write_text(text, encoding="utf-8", newline="\n")


def generate_batch(root: Path, plan_path: Path, output_root: Path | None) -> int:
    plan = load_json(root / plan_path)
    jobs = plan.get("jobs")
    if not isinstance(jobs, list) or not jobs:
        raise ValueError("generation plan must contain a non-empty jobs list")
    for job in jobs:
        if not isinstance(job, dict):
            raise ValueError("each generation job must be an object")
        output = Path(str(job["output"]))
        if output_root is not None:
            output = output_root / output.name
            template = Path(str(job["template"]))
            data = Path(str(job["data"]))
            generate_one(root, template, data, output.relative_to(root) if output.is_relative_to(root) else output)
        else:
            generate_one(root, Path(str(job["template"])), Path(str(job["data"])), output)
    return len(jobs)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--template", type=Path)
    parser.add_argument("--data", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--plan", type=Path)
    parser.add_argument("--output-root", type=Path)
    args = parser.parse_args()

    root = args.root.resolve()
    if args.plan:
        count = generate_batch(root, args.plan, args.output_root.resolve() if args.output_root else None)
        print(json.dumps({"status": "success", "generated": count}))
        return 0
    if not (args.template and args.data and args.output):
        parser.error("provide --plan or --template, --data and --output")
    generate_one(root, args.template, args.data, args.output)
    print(json.dumps({"status": "success", "output": str(args.output)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
