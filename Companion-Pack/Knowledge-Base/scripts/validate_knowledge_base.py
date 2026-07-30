#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--report",required=True); a=ap.parse_args()
    root=Path(__file__).resolve().parents[1]; errors=[]
    required=["README.md","VERSION","CHANGELOG.md","LICENSE-STATUS.md","PROVENANCE.json","DEPENDENCIES.json","manifest.json","catalog.json","checksums.json","python/src/knowledge_base/core.py","python/tests/test_knowledge_base.py","scripts/knowledge_base_cli.py"]
    for rel in required:
        if not (root/rel).is_file(): errors.append("missing:"+rel)
    checks=json.loads((root/"checksums.json").read_text())
    for rel,digest in checks["files"].items():
        p=root/rel
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest: errors.append("checksum:"+rel)
    corpus=list((root/"corpus").rglob("*.json"))
    if len(corpus)!=8: errors.append("corpus-count:"+str(len(corpus)))
    report={"status":"success" if not errors else "failure","pack_files":sum(1 for p in root.rglob("*") if p.is_file()),"corpus_documents":len(corpus),"errors":errors}
    Path(a.report).parent.mkdir(parents=True,exist_ok=True); Path(a.report).write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print(json.dumps(report,sort_keys=True)); return 0 if not errors else 1
if __name__=="__main__": raise SystemExit(main())
