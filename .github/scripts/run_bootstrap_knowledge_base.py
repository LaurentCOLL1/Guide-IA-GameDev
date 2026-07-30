#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib, io, os, subprocess, sys, tarfile
root=Path.cwd()
parts=[(root/f'.github/scripts/kb_payload_{i}.b64').read_text(encoding='utf-8').strip() for i in range(1,5)]
data=''.join(parts)
raw=base64.b64decode(data,validate=True)
expected='7963c5d73626f9beaa3ec8dc8f1c9071e846ea88c3d8dd2654b144d8e0bb3f30'
actual=hashlib.sha256(raw).hexdigest()
if len(data)!=17560 or actual!=expected:
    raise SystemExit(f'payload mismatch: chars={len(data)} sha256={actual}')
with tarfile.open(fileobj=io.BytesIO(raw),mode='r:gz') as tar:
    tar.extractall(root,filter='data')
pack=root/'Companion-Pack/Knowledge-Base'
env=os.environ.copy(); env['PYTHONPATH']=str(pack/'python/src'); env['PYTHONDONTWRITEBYTECODE']='1'
subprocess.run([sys.executable,'-m','unittest','discover','-s',str(pack/'python/tests'),'-v'],check=True,env=env)
report=root/'dist/knowledge-base-bootstrap.json'; report.parent.mkdir(parents=True,exist_ok=True)
subprocess.run([sys.executable,str(pack/'scripts/validate_knowledge_base.py'),'--report',str(report)],check=True,env=env)
for rel in ['.github/scripts/bootstrap_knowledge_base.py','.github/scripts/run_bootstrap_knowledge_base.py','.github/scripts/kb_payload_1.b64','.github/scripts/kb_payload_2.b64','.github/scripts/kb_payload_3.b64','.github/scripts/kb_payload_4.b64','.github/workflows/bootstrap-knowledge-base.yml']:
    p=root/rel
    if p.exists(): p.unlink()
subprocess.run(['git','config','user.name','github-actions[bot]'],check=True)
subprocess.run(['git','config','user.email','41898282+github-actions[bot]@users.noreply.github.com'],check=True)
subprocess.run(['git','add','-A'],check=True)
subprocess.run(['git','commit','-m','feat(companion-pack): matérialiser la Knowledge Base'],check=True)
subprocess.run(['git','push','origin','HEAD:feat/companion-pack-knowledge-base'],check=True)
