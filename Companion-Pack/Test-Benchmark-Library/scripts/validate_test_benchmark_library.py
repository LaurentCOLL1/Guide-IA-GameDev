#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

PACK = Path(__file__).resolve().parents[1]
ID_RE = re.compile(r"^(BMK|CP)-[A-Z0-9-]+$")


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser=argparse.ArgumentParser(); parser.add_argument("--report",type=Path); args=parser.parse_args()
    errors=[]
    required=["README.md","VERSION","manifest.json","catalog.json","checksums.json","fixtures/seeds.json","godot/project.godot","scripts/run_python_suite.py"]
    for rel in required:
        if not (PACK/rel).is_file(): errors.append(f"missing:{rel}")
    manifest=load(PACK/"manifest.json")
    catalog=load(PACK/"catalog.json")
    ids=[]
    for item in catalog["entries"]:
        ids.append(item["id"])
        if not ID_RE.match(item["id"]): errors.append(f"invalid-id:{item['id']}")
        if not (PACK/item["path"]).is_file(): errors.append(f"missing-catalog-path:{item['path']}")
    if len(ids)!=len(set(ids)): errors.append("duplicate-catalog-id")
    contracts=list((PACK/"contracts").glob("*.json"))
    if len(contracts)!=6: errors.append(f"contract-count:{len(contracts)}")
    for path in contracts:
        value=load(path)
        if value.get("repetitions",0)<2: errors.append(f"repetitions:{path.name}")
        if "variance" in value: errors.append(f"contract-must-not-contain-results:{path.name}")
    corpus=list((PACK/"fixtures/corpus").glob("*.jsonl"))
    if len(corpus)!=2: errors.append("corpus-files")
    forbidden=(".pdf",".docx",".epub",".safetensors",".ckpt",".pt",".pth",".bin")
    files=[p for p in PACK.rglob("*") if p.is_file() and "__pycache__" not in p.parts]
    for path in files:
        if path.suffix.lower() in forbidden: errors.append(f"forbidden:{path.relative_to(PACK)}")
        if path.stat().st_size>500_000: errors.append(f"large:{path.relative_to(PACK)}")
    checks=load(PACK/"checksums.json")["files"]
    for rel,digest in checks.items():
        path=PACK/rel
        if not path.is_file(): errors.append(f"checksum-missing:{rel}")
        elif hashlib.sha256(path.read_bytes()).hexdigest()!=digest: errors.append(f"checksum-mismatch:{rel}")
    result={"status":"pass" if not errors else "fail","source_files":len(files),"contracts":len(contracts),"catalog_entries":len(catalog["entries"]),"errors":errors,"manifest_version":manifest["version"]}
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True); args.report.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2,sort_keys=True))
    print(f"TEST_BENCHMARK_LIBRARY_STATIC: {'PASS' if not errors else 'FAIL'} ({len(files)} files)")
    return 1 if errors else 0

if __name__=="__main__": raise SystemExit(main())
