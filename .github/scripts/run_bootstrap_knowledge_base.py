#!/usr/bin/env python3
from pathlib import Path
import ast, base64, io, os, re, subprocess, sys, tarfile
root=Path.cwd()
source=(root/'.github/scripts/bootstrap_knowledge_base.py').read_text(encoding='utf-8')
match=re.search(r'^DATA=(.+)$', source, re.MULTILINE)
if not match:
    raise SystemExit('DATA block not found')
data=ast.literal_eval(match.group(1))
data=''.join(data.split())
data += '=' * (-len(data) % 4)
with tarfile.open(fileobj=io.BytesIO(base64.b64decode(data)),mode='r:gz') as tar:
    tar.extractall(root)
pack=root/'Companion-Pack/Knowledge-Base'
env=os.environ.copy(); env['PYTHONPATH']=str(pack/'python/src'); env['PYTHONDONTWRITEBYTECODE']='1'
subprocess.run([sys.executable,'-m','unittest','discover','-s',str(pack/'python/tests'),'-v'],check=True,env=env)
report=root/'dist/knowledge-base-bootstrap.json'; report.parent.mkdir(parents=True,exist_ok=True)
subprocess.run([sys.executable,str(pack/'scripts/validate_knowledge_base.py'),'--report',str(report)],check=True,env=env)
for rel in ['.github/scripts/bootstrap_knowledge_base.py','.github/scripts/run_bootstrap_knowledge_base.py','.github/workflows/bootstrap-knowledge-base.yml']:
    p=root/rel
    if p.exists(): p.unlink()
subprocess.run(['git','config','user.name','github-actions[bot]'],check=True)
subprocess.run(['git','config','user.email','41898282+github-actions[bot]@users.noreply.github.com'],check=True)
subprocess.run(['git','add','-A'],check=True)
subprocess.run(['git','commit','-m','feat(companion-pack): matérialiser la Knowledge Base'],check=True)
subprocess.run(['git','push','origin','HEAD:feat/companion-pack-knowledge-base'],check=True)
