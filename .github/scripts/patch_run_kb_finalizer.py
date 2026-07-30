#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys
R=Path.cwd()
if 'version: "4.24.0"' in (R/'CONTINUITE-PROJET.md').read_text(encoding='utf-8'):
    raise SystemExit(0)
p=R/'.github/scripts/finalize_knowledge_base_governance.py'
s=p.read_text(encoding='utf-8')
s=s.replace("s=one(s,a,b,'cont next')", "import re\ns,n=re.subn(r'(?s)(## 26\\. Prochaine action\\n\\n).*?(?=\\n## 27\\. Journal)', lambda m:m.group(1)+b+'\\n', s)\nif n!=1: raise RuntimeError(f'cont next regex: {n}')", 1)
anchor="E=os.environ.copy(); E['PYTHONDONTWRITEBYTECODE']='1'; E['PYTHONPATH']=str(R/'Companion-Pack/Knowledge-Base/python/src')"
code="""import hashlib, json
P=R/'Companion-Pack/Knowledge-Base'; F={}
for q in sorted(P.rglob('*')):
    if q.is_file() and q.name!='checksums.json':
        F[q.relative_to(P).as_posix()]=hashlib.sha256(q.read_bytes()).hexdigest()
(P/'checksums.json').write_text(json.dumps({'algorithm':'sha256','files':F,'schema_version':1},indent=2,ensure_ascii=False,sort_keys=True)+'\\n',encoding='utf-8')
"""
s=s.replace(anchor, code+anchor, 1)
s=s.replace("['git','add','ROADMAP.md','contents.txt','plans/COMPANION-PACK-PLAN-MAITRE.md','CONTINUITE-PROJET.md']", "['git','add','ROADMAP.md','contents.txt','plans/COMPANION-PACK-PLAN-MAITRE.md','CONTINUITE-PROJET.md','Companion-Pack/Knowledge-Base/checksums.json']", 1)
t=R/'.github/scripts/finalize_knowledge_base_governance.runtime.py'
t.write_text(s,encoding='utf-8')
subprocess.run([sys.executable,str(t)],check=True)
