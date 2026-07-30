#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import os, subprocess, sys
R=Path.cwd(); now=datetime.now(ZoneInfo('Europe/Paris')).replace(microsecond=0).isoformat()
def rw(p): return (R/p).read_text(encoding='utf-8')
def wr(p,s): (R/p).write_text(s,encoding='utf-8')
def one(s,a,b,n):
 c=s.count(a)
 if c!=1: raise RuntimeError(f'{n}: {c}')
 return s.replace(a,b,1)
p='ROADMAP.md'; s=rw(p)
s=one(s,'**Statut M7 : actif — 9 packs validés sur 10 ; Pack 10, Knowledge Base, suivant.**','**Statut M7 : terminé — 10 packs matérialisés et validés sur 10 dans leur périmètre Linux.**','roadmap status')
s=one(s,'- [ ] Knowledge Base.','- [x] Knowledge Base — version `1.0.0`, validation Linux `runtime-tested` avec corpus synthétique, index local déterministe, recherche et suppression vérifiée.','roadmap pack')
wr(p,s)
p='contents.txt'; s=rw(p); e='Companion-Pack/Knowledge-Base/README.md'
if e not in s.splitlines(): s=s.rstrip()+'\n'+e+'\n'
wr(p,s)
p='plans/COMPANION-PACK-PLAN-MAITRE.md'; s=rw(p)
s=one(s,'version: "1.9.0"','version: "1.10.0"','plan version')
s=one(s,'> **Statut :** en cours — Pack 9 sur 10 validé','> **Statut :** terminé — 10 Packs sur 10 matérialisés et validés','plan status')
s=one(s,'## Pack 10 — Knowledge Base\n\n**Objectifs**','## Pack 10 — Knowledge Base\n\n**État :** matérialisé en version `1.0.0`, validé sur Linux x86_64 par le run `30551507215` avec corpus synthétique, index local déterministe, 32 tests de recherche et suppression complète vérifiée ; réserves embeddings réels, service RAG distant, base vectorielle externe, volumétrie, publication et licence globale maintenues.\n\n**Objectifs**','plan state')
wr(p,s)
p='CONTINUITE-PROJET.md'; s=rw(p)
s=one(s,'version: "4.23.0"','version: "4.24.0"','cont version')
s=one(s,'last-updated: "2026-07-30T15:10:10+02:00"',f'last-updated: "{now}"','cont date')
s=one(s,'- jalon : M7 — Companion Pack ;','- jalon : M8 — Publications ;','cont jalon')
s=one(s,'- progression du Companion Pack : 9 packs validés sur 10 ;','- progression du Companion Pack : 10 packs validés sur 10, M7 terminé ;','cont progress')
s=one(s,'- Production Toolkit : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec Python, Blender et import Godot ;','- Production Toolkit : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec Python, Blender et import Godot ;\n- Knowledge Base : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec corpus synthétique, index local déterministe, recherche et suppression vérifiée ;','cont pack')
a='''M7 — Companion Pack est actif. Les Packs 1 à 9 sont matérialisés en version `1.0.0` et validés dans leur périmètre Linux. Production Toolkit a validé 28 fichiers, neuf familles, 29 tests Python, le dry-run, les codes de sortie, l'échec injecté et la reprise, les conversions synthétiques, deux ZIP déterministes, Blender OBJ vers GLB, l'import Godot et la préservation des sources. Les formats propriétaires, la qualité artistique, les bakes complexes, la compression GPU, les exports de jeu, les plateformes non Linux et la licence globale restent réservés.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Companion-Pack/Knowledge-Base/README.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le Pack 10 doit matérialiser une base de connaissances synthétique : lore, codex, documents RAG, schémas de métadonnées, corpus de test, scripts de découpage, index reproductibles et outils de suppression/réindexation. Les droits devront être clairs, le corpus synthétique ou autorisé, l'index recréable depuis les sources, les tests de recherche exécutés et la suppression complète d'un document vérifiée.'''
b='''M7 — Companion Pack est terminé. Les dix Packs sont matérialisés en version `1.0.0` et validés dans leur périmètre Linux. Knowledge Base a validé 28 fichiers, huit documents synthétiques, 16 fragments, 32 tests Python, deux index byte-identiques, les recherches et filtres attendus, la suppression complète d'un document et la reconstruction identique après retrait de sa source. Les embeddings réels, services RAG distants, bases vectorielles externes, grandes volumétries, concurrence, publication et licence globale restent réservés.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
M8 — Publications
Définir la licence globale du projet.
Niveau GPT-5.6 Sol recommandé : Élevée
```

La prochaine décision doit établir une licence globale compatible avec les textes, scripts, fixtures synthétiques, exemples et futures archives du Companion Pack avant toute publication officielle ou redistribution autonome.'''
s=one(s,a,b,'cont next')
mark='## 27. Journal\n\n'
j=f'''### {now} — version 4.24.0

- matérialisation du Companion Pack, Pack 10 — Knowledge Base ;
- 28 fichiers du Pack, huit documents `Project Asteria`, trois schémas et 16 fragments déterministes validés ;
- séparation canon, rumeur, mémoire et référence validée ;
- 32 tests Python réussis ;
- deux index reconstruits byte pour byte ;
- recherches lexicale, vectorielle locale et hybride avec filtres de vérité validées ;
- suppression complète de `AST-RUMOR-EMBER-QUEEN` et reconstruction après retrait de sa source vérifiées ;
- Ubuntu 24.04 et Python `3.12.13` qualifiés, sans modèle ni réseau ;
- run `30551507215`, artefact `8762968115`, digest `sha256:0f85a3d1dd8bf6728c963dd88adee17502a27280b9b7aea4a4515b2565cc8119` ;
- arbre Git propre, sources inchangées, aucun secret, donnée personnelle ou corpus tiers inclus ;
- progression M7 portée à 10 Packs sur 10 et jalon M7 terminé ;
- prochaine action : M8 — Publications, définir la licence globale du projet, niveau Élevée ;
- aucun embedding réel, service RAG distant, base vectorielle externe, grande volumétrie, concurrence, publication, release ou licence globale validé ou produit.

'''
s=one(s,mark,mark+j,'cont journal'); wr(p,s)
E=os.environ.copy(); E['PYTHONDONTWRITEBYTECODE']='1'; E['PYTHONPATH']=str(R/'Companion-Pack/Knowledge-Base/python/src')
cmds=[[sys.executable,'Companion-Pack/Knowledge-Base/scripts/validate_knowledge_base.py','--report','dist/knowledge-base-governance.json'],[sys.executable,'-m','unittest','discover','-s','Companion-Pack/Knowledge-Base/python/tests','-v'],[sys.executable,'tools/validate_chapters.py','--root','.','--report','dist/QA-CHAPTERS.md'],[sys.executable,'tools/validate_livre_v_references.py','--check'],[sys.executable,'tools/check_code_explanation_structure.py','--check'],[sys.executable,'tools/check_context_markers.py','--check'],[sys.executable,'tools/audit_contextes_semantiques.py','--check']]
for c in cmds: subprocess.run(c,check=True,env=E)
subprocess.run(['git','config','user.name','github-actions[bot]'],check=True); subprocess.run(['git','config','user.email','41898282+github-actions[bot]@users.noreply.github.com'],check=True)
subprocess.run(['git','add','ROADMAP.md','contents.txt','plans/COMPANION-PACK-PLAN-MAITRE.md','CONTINUITE-PROJET.md'],check=True)
subprocess.run(['git','commit','-m','chore(companion-pack): clore M7 et ouvrir M8'],check=True)
subprocess.run(['git','push','origin','HEAD:feat/companion-pack-knowledge-base'],check=True)
