#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json
REQUIRED=['README.md','VERSION','manifest.json','catalog.json','DEPENDENCIES.json','PROVENANCE.json','LICENSE-STATUS.md','checksums.json','python/src/production_toolkit/toolkit.py','scripts/toolkit_cli.py','blender/obj_to_glb.py','godot/project.godot','godot/check_import.gd']
def digest(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
p=argparse.ArgumentParser(); p.add_argument('--root',default=str(Path(__file__).parents[1])); p.add_argument('--report'); a=p.parse_args(); root=Path(a.root); failures=[]
for rel in REQUIRED:
 if not (root/rel).is_file(): failures.append('missing:'+rel)
files=[x for x in root.rglob('*') if x.is_file()]
for path in files:
 if path.suffix.lower() in {'.pdf','.docx','.epub','.blend','.glb','.png','.wav','.zip'}: failures.append('binary-source:'+path.relative_to(root).as_posix())
readme=(root/'README.md').read_text(encoding='utf-8')
for token in ['--dry-run','checkpoint','source']:
 if token not in readme: failures.append('readme-token:'+token)
try:
 checks=json.loads((root/'checksums.json').read_text())['files']; expected={p.relative_to(root).as_posix() for p in files if p.name!='checksums.json'}
 if set(checks)!=expected: failures.append('checksums-coverage')
 for rel,sha in checks.items():
  if not (root/rel).is_file() or digest(root/rel)!=sha: failures.append('checksum:'+rel)
except Exception as e: failures.append('checksums-invalid:'+str(e))
try:
 catalog=json.loads((root/'catalog.json').read_text())['entries']; ids=[x['id'] for x in catalog]
 if len(ids)!=len(set(ids)): failures.append('catalog-duplicate-id')
except Exception as e: failures.append('catalog-invalid:'+str(e))
payload={'status':'success' if not failures else 'failure','files':len(files),'catalog_entries':len(catalog) if 'catalog' in locals() else 0,'failures':failures}
if a.report: Path(a.report).parent.mkdir(parents=True,exist_ok=True); Path(a.report).write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
print(json.dumps(payload,sort_keys=True)); raise SystemExit(0 if not failures else 1)
