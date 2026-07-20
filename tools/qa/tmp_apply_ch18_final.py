from pathlib import Path
import base64, gzip, re, subprocess
R=Path(".")
TS="2026-07-20T14:18:58+02:00"
def one(t,o,n,label):
    c=t.count(o)
    if c!=1: raise RuntimeError(f"{label}: {c}")
    return t.replace(o,n,1)
def sub(t,p,n,label,flags=0):
    t,c=re.subn(p,n,t,count=1,flags=flags)
    if c!=1: raise RuntimeError(f"{label}: {c}")
    return t
payload="".join((R/f"tools/qa/tmp_ch18_payload.part{i}").read_text().strip() for i in range(1,7))
patch=R/"tools/qa/tmp_ch18_audited.patch"
patch.write_bytes(gzip.decompress(base64.b64decode(payload)))
subprocess.run(["git","apply","--check",str(patch)],check=True)
subprocess.run(["git","apply",str(patch)],check=True)
patch.unlink()
p=R/"Livre-II/index.md"; t=p.read_text()
t=one(t,'version: "1.12.4"','version: "1.12.5"',"index version")
t=one(t,"18. Combat — à rédiger","18. [Combat](CHAPITRE-18-Combat.md) — **rédigé, repéré, expliqué bloc par bloc, clôturé par les décisions Project Asteria et audité au niveau static-review**","index ch18")
t=one(t,"- [audit du chapitre 17](QA/AUDIT-CHAPITRE-17.md) ;","- [audit du chapitre 17](QA/AUDIT-CHAPITRE-17.md) ;\n- [audit du chapitre 18](QA/AUDIT-CHAPITRE-18.md) ;","index audit")
t=one(t,"Les chapitres 3 à 17 utilisent **Élevée**.","Les chapitres 3 à 18 utilisent **Élevée**.","index reasoning")
p.write_text(t)
p=R/"ROADMAP.md"; t=p.read_text()
t=one(t,"Douze grands systèmes de jeu — 4 chapitres rédigés, repérés et audités sur 12.","Douze grands systèmes de jeu — 5 chapitres rédigés, repérés et audités sur 12.","roadmap count")
t=one(t,"Convention des outils et contextes appliquée aux chapitres 1 à 17.","Convention des outils et contextes appliquée aux chapitres 1 à 18.","roadmap contexts")
a="- [x] Chapitre 17 — perceptions, mémoire bornée, buts, planification déterministe, ordonnanceur, simulation hors écran, invalidation, IA consultative et sauvegarde minimale — rédigé et audité au niveau `static-review`."
t=one(t,a,a+"\n- [x] Chapitre 18 — commandes typées, côtés, initiative déterministe, ciblage, portée, ligne de vue, dégâts, garde, états, commit préparé, simulation hors écran et sauvegarde stricte — rédigé et audité au niveau `static-review`.","roadmap ch18")
t=one(t,"**Statut M3 : en cours — 17 chapitres rédigés, repérés et audités sur 30.**","**Statut M3 : en cours — 18 chapitres rédigés, repérés et audités sur 30.**","roadmap status")
t=one(t,"Quatre des douze systèmes de gameplay sont documentés : personnages, relations sociales, famille et agents autonomes.","Cinq des douze systèmes de gameplay sont documentés : personnages, relations sociales, famille, agents autonomes et combat.","roadmap prose")
t=one(t,"le chapitre 18 traitera désormais le combat.","le chapitre 18 définit désormais l’autorité de combat et le chapitre 19 traitera les compétences et pouvoirs.","roadmap next")
p.write_text(t)
p=R/"contents.txt"; t=p.read_text()
t=one(t,"Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md","Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md\nLivre-II/CHAPITRE-18-Combat.md","contents chapter")
t=one(t,"Livre-II/QA/AUDIT-CHAPITRE-17.md","Livre-II/QA/AUDIT-CHAPITRE-17.md\nLivre-II/QA/AUDIT-CHAPITRE-18.md","contents audit")
t=one(t,"Livre-II/QA/VALIDATION-FINALE-CHAPITRE-17.yaml","Livre-II/QA/VALIDATION-FINALE-CHAPITRE-17.yaml\nLivre-II/QA/VALIDATION-FINALE-CHAPITRE-18.yaml","contents evidence")
p.write_text(t)
p=R/"CONTINUITE-PROJET.md"; t=p.read_text()
t=one(t,'version: "3.17.10"','version: "3.18.0"',"continuity version")
t=sub(t,r'^last-updated: ".+"$',f'last-updated: "{TS}"',"continuity time",re.M)
t=one(t,"**En cours : 17 chapitres sur 30.**","**En cours : 18 chapitres sur 30.**","continuity progress")
t=one(t,"17. Agents IA et comportements autonomes — terminé au niveau `static-review`.\n18. Combat.","17. Agents IA et comportements autonomes — terminé au niveau `static-review`.\n18. Combat — terminé au niveau `static-review`.","continuity list")
t=one(t,"Chapitres 3 à 17 : **Élevée**.","Chapitres 3 à 18 : **Élevée**.","continuity reasoning")
decisions='''### 11.13 Combat

- `CombatService` constitue l’autorité des commandes de combat ;
- les joueurs, agents et scénarios soumettent des commandes typées sans imposer le résultat ;
- santé, endurance et état de vie restent dans `CharacterRuntimeState` ;
- initiative, côté, garde et états temporaires restent dans `CombatantState` ;
- les côtés sont explicites et le tir allié dépend d’une règle de conception ;
- l’initiative utilise des entiers bornés et un départage lexical stable, jamais `hash()` ;
- portée logique et ligne de vue sont validées séparément ;
- les mutations sont calculées sur des copies détachées puis committées comme un lot validé ;
- l’historique candidat est écrit avant commit et les événements ne sont émis qu’après succès ;
- les commandes sont corrélées, idempotentes, bornées et ordonnées ;
- le codec de sauvegarde est strict et encode le RNG 64 bits sans perte par deux mots de 32 bits ;
- file de commandes, raycasts, caches et présentation sont exclus de la persistance ;
- compétences, objets, économie, politique et narration restent dans leurs systèmes propres.

'''
t=one(t,"## 12. Chapitre 5 — état résumé",decisions+"## 12. Chapitre 5 — état résumé","continuity decisions")
anchor="- ne pas placer la prochaine étape, le chemin ou le niveau du chapitre suivant dans le chapitre publié ;"
errs='''- ne pas laisser un agent, une animation ou un raycast muter directement la santé ;
- ne pas utiliser `hash()` comme départage reproductible d’initiative ;
- ne pas déduire une équipe depuis une relation sociale ou une proximité spatiale ;
- ne pas confondre portée logique et ligne de vue physique ;
- ne pas émettre un événement de combat avant le commit autoritaire ;
- ne pas modifier le dépôt actif avant validation complète des candidats ;
- ne pas conserver des références mutables dans l’historique ou la file ;
- ne pas sérialiser un entier 64 bits directement dans JSON sans représentation sûre ;
- ne pas charger directement dans les affrontements actifs ;
- ne pas persister raycasts, commandes en attente, caches ou présentation ;
'''
t=one(t,anchor,errs+anchor,"continuity errors")
t=one(t,"- progression : 17 chapitres sur 30 ;","- progression : 18 chapitres sur 30 ;","continuity current")
t=one(t,"- chapitre 17 : version `1.0.3` ;","- chapitre 17 : version `1.0.3` ;\n- chapitre 18 : version `1.0.0` ;","continuity version list")
next='''## 26. Prochaine action

Le chapitre 18 est terminé au niveau `static-review`. Le combat reçoit des commandes typées, valide leurs cibles et applique des mutations préparées sans transférer son autorité aux agents, à la physique ou à la présentation.

Chapitre suivant :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-II/CHAPITRE-19-Competences-et-pouvoirs.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Périmètre attendu : définitions de compétences et pouvoirs, coûts, temps de recharge, ciblage spécialisé, effets composables et progression, en réutilisant les contrats de combat sans déplacer les règles de portée, défense, dégâts ou commit hors du système propriétaire.

'''
t=sub(t,r'## 26\. Prochaine action\n.*?(?=## 27\. Journal)',next,"continuity next",re.S)
journal=f'''### {TS} — version 3.18.0

- chapitre 18 porté de la porte de brouillon `0.9.0` à la version auditée `1.0.0` ;
- côtés, initiative, ciblage, portée, ligne de vue, dégâts, garde et états documentés ;
- copies détachées, historique avant commit, événements après commit et sauvegarde stricte établis ;
- chapitre clôturé par les décisions `Project Asteria`, sans prochaine étape dans le texte lecteur ;
- gouvernance et ordre de compilation mis à jour ;
- aucun PDF construit et aucun test runtime revendiqué.

'''
t=one(t,"## 27. Journal\n\n","## 27. Journal\n\n"+journal,"continuity journal")
p.write_text(t)
chapter=(R/"Livre-II/CHAPITRE-18-Combat.md").read_text()
assert 'status: "reviewed"' in chapter and 'version: "1.0.0"' in chapter
assert chapter.count("<!-- qa:code-explanation -->")==67
assert len(re.findall(r'^```',chapter,re.M))==134
assert "## 50. Synthèse opérationnelle pour Project Asteria" in chapter
assert "Prochaine étape" not in chapter and "CHAPITRE-19" not in chapter
print("chapter_lines",len(chapter.splitlines()))
print("finalize_ch18=ok")
