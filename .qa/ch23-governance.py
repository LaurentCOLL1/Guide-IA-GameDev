from pathlib import Path
import json,re
ROOT=Path('.')
CONTINUITY=ROOT/'CONTINUITE-PROJET.md'
INDEX=ROOT/'Livre-II/index.md'
ROADMAP=ROOT/'ROADMAP.md'
CONTENTS=ROOT/'contents.txt'
def read(path): return path.read_text(encoding='utf-8')
def write(path,text): path.write_text(text,encoding='utf-8',newline='\n')
def replace_once(text,old,new,label):
 count=text.count(old)
 if count!=1: raise RuntimeError(f'{label}: expected one occurrence, got {count}')
 return text.replace(old,new,1)
m=json.loads(Path('.qa/ch23-metrics.json').read_text(encoding='utf-8')); stamp=m['stamp']

continuity = read(CONTINUITY)
continuity = replace_once(continuity, 'version: "3.22.2"', 'version: "3.23.0"', 'continuity version')
continuity = re.sub(r'last-updated: "[^"]+"', f'last-updated: "{stamp}"', continuity, count=1)
continuity = replace_once(continuity, '**En cours : 22 chapitres sur 30.**', '**En cours : 23 chapitres sur 30.**', 'collection progress')
continuity = replace_once(continuity, '23. Politique, factions et justice.', '23. Politique, factions et justice — terminé au niveau `static-review`.', 'chapter 23 collection status')
continuity = replace_once(continuity, 'Chapitres 3 à 22 : **Élevée**.', 'Chapitres 3 à 23 : **Élevée**.', 'reasoning range')

architecture = '''### 11.18 Politique, factions et justice

- institutions, factions, rangs, fonctions et lois utilisent des identifiants stables ;
- définitions de conception et états vivants restent séparés ;
- adhésions et mandats portent statuts, ticks, causes et révisions ;
- relations sociales et liens familiaux ne créent aucun droit institutionnel implicite ;
- lois et promulgations sont versionnées et immuables après publication ;
- juridictions et périodes d’effet utilisent des références logiques et l’horloge du monde ;
- autorisations calculées distinguent `ALLOW`, `DENY`, `NOT_APPLICABLE` et `INDETERMINATE` ;
- seule une décision `ALLOW` autorise une action protégée ;
- une infraction rapportée ouvre un dossier sans établir la culpabilité ;
- preuves, faits sources, recevabilité, poids et verdicts restent distincts ;
- la chaîne de garde utilise identité, séquence, provenance et empreinte ;
- verdicts référencent lois, preuves et codes de raisonnement ;
- sanctions sont décrites par un plan puis préparées par les autorités propriétaires ;
- amendes, confiscations, restrictions et changements de domaine sont committés avec dossier, verdict et idempotence ;
- commandes, résultats et décisions durables sont révisionnés et idempotents ;
- événements sont émis uniquement après commit ;
- sorties IA restent consultatives et ne peuvent ni promulguer ni condamner ;
- définitions, droits dérivés, contextes, candidats, observations et présentation sont exclus de la persistance.

'''
continuity = replace_once(continuity, '## 12. Chapitre 5 — état résumé', architecture + '## 12. Chapitre 5 — état résumé', 'architecture section')

error_anchor = '- ne pas laisser une sortie IA remplacer directement populations, ressources ou horloge ;\n'
new_errors = error_anchor + '''- ne pas utiliser un nom affiché comme identité institutionnelle ;
- ne pas déduire une adhésion, un rang ou un droit depuis une relation sociale ;
- ne pas modifier en place une version de loi promulguée ;
- ne pas autoriser une action protégée par simple absence de règle ;
- ne pas traiter une accusation ou un rapport comme un verdict ;
- ne pas copier un objet, une transaction ou un événement comme preuve autoritaire ;
- ne pas laisser une sortie IA promulguer, juger ou condamner ;
- ne pas appliquer séparément amende, confiscation, restriction ou changement de domaine ;
- ne pas dater adhésions, mandats ou lois avec l’heure système ;
- ne pas émettre un événement politique ou judiciaire avant commit ;
'''
continuity = replace_once(continuity, error_anchor, new_errors, 'continuity errors')
continuity = replace_once(continuity, '- progression : 22 chapitres sur 30 ;', '- progression : 23 chapitres sur 30 ;', 'current progress')
continuity = replace_once(continuity, '- chapitre 22 : version `1.0.1` ;', '- chapitre 22 : version `1.0.1` ;\n- chapitre 23 : version `1.0.0` ;', 'current chapter version')

next_action = f'''## 26. Prochaine action

Le chapitre 23 est terminé au niveau `static-review`. La politique et la justice séparent institutions, droits, lois, allégations, preuves, verdicts et sanctions, puis coordonnent les effets externes sans reprendre l’autorité des autres systèmes.

Chapitre suivant :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-II/CHAPITRE-24-Construction-et-gestion-de-domaines.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Périmètre attendu : domaines et parcelles, titres et droits d’usage, bâtiments, emplacements, plans de construction, matériaux, progression de chantier, production, entretien et permissions d’accès. Le chapitre 24 consommera juridictions et droits du chapitre 23, objets du chapitre 20, coûts du chapitre 21 et ressources du chapitre 22 par des ports ; les quêtes et conséquences narratives resteront au chapitre 25.

## 27. Journal
'''
continuity, n = re.subn(r'## 26\. Prochaine action\n.*?\n## 27\. Journal\n', next_action, continuity, count=1, flags=re.S)
if n != 1:
    raise RuntimeError('Unable to replace next action')
journal = f'''### {stamp} — version 3.23.0

- chapitre 23 créé, relu, corrigé et audité au niveau `static-review` ;
- institutions, factions, adhésions, rangs, mandats, lois, autorisations, dossiers, preuves, verdicts et sanctions documentés ;
- invariants de restauration des rangs, fonctions, institutions et sièges vacants renforcés ;
- sanctions multi-autorités et idempotence explicitées ;
- index, roadmap, `contents.txt`, audit et preuve QA initiale mis à jour ;
- prochaine action déplacée vers le chapitre 24 — Construction et gestion de domaines, niveau Élevée ;
- aucun test runtime revendiqué et aucun PDF construit.

'''
continuity = replace_once(continuity, '## 27. Journal\n', '## 27. Journal\n\n' + journal, 'continuity journal')
write(CONTINUITY, continuity)

index = read(INDEX)
index = replace_once(index, 'version: "1.15.0"', 'version: "1.16.0"', 'index version')
index = replace_once(index, '23. Politique, factions et justice — à rédiger', '23. [Politique, factions et justice](CHAPITRE-23-Politique-factions-et-justice.md) — **rédigé, repéré, expliqué bloc par bloc, lois versionnées et sanctions multi-autorités préparées, clôturé par les décisions Project Asteria et audité au niveau static-review**', 'index chapter 23')
index = replace_once(index, '- [audit du chapitre 22](QA/AUDIT-CHAPITRE-22.md) ;', '- [audit du chapitre 22](QA/AUDIT-CHAPITRE-22.md) ;\n- [audit du chapitre 23](QA/AUDIT-CHAPITRE-23.md) ;', 'index audit')
index = replace_once(index, 'Les chapitres 3 à 22 utilisent **Élevée**.', 'Les chapitres 3 à 23 utilisent **Élevée**.', 'index reasoning')
index, n = re.subn(r'(## Statut\n\n).*', r'\1Le milestone **M3 — Livre II : Développement et architecture** est en cours. **Vingt-trois chapitres sur trente** sont rédigés, repérés et audités au niveau documentaire et statique. Les neuf chapitres de fondation et les quatre chapitres de plateforme IA locale sont complets. La partie gameplay compte désormais **dix systèmes sur douze** : personnages, relations sociales, famille, agents autonomes, combat, compétences et pouvoirs, inventaire et réputation des objets, économie, monde vivant, puis politique, factions et justice. Le chapitre 23 possède institutions, adhésions, mandats, lois, autorisations, dossiers, preuves, verdicts et sanctions coordonnées sans reprendre l’autorité des autres systèmes. Les réserves runtime et le PDF restent différés conformément au protocole QA.\n', index, count=1, flags=re.S)
if n != 1:
    raise RuntimeError('Unable to update index status')
write(INDEX, index)

roadmap = read(ROADMAP)
roadmap = replace_once(roadmap, '- [ ] Douze grands systèmes de jeu — 9 chapitres rédigés, repérés et audités sur 12.', '- [ ] Douze grands systèmes de jeu — 10 chapitres rédigés, repérés et audités sur 12.', 'roadmap gameplay count')
roadmap = replace_once(roadmap, '- [x] Convention des outils et contextes appliquée aux chapitres 1 à 22.', '- [x] Convention des outils et contextes appliquée aux chapitres 1 à 23.', 'roadmap contexts')
roadmap = replace_once(roadmap, '- [x] Chapitre 22 — horloge logique, régions, populations, ressources, résidus, simulation bornée, matérialisation, récoltes, signaux économiques et sauvegarde — rédigé et audité au niveau `static-review`.', '- [x] Chapitre 22 — horloge logique, régions, populations, ressources, résidus, simulation bornée, matérialisation, récoltes, signaux économiques et sauvegarde — rédigé et audité au niveau `static-review`.\n- [x] Chapitre 23 — institutions, factions, adhésions, rangs, mandats, lois versionnées, autorisations, infractions, preuves, verdicts, sanctions coordonnées et sauvegarde — rédigé et audité au niveau `static-review`.', 'roadmap chapter 23')
roadmap, n = re.subn(r'\*\*Statut M3 : en cours — 22 chapitres.*', '**Statut M3 : en cours — 23 chapitres rédigés, repérés et audités sur 30.** Godot 4.7.1-stable, l’édition Standard, GDScript typé et Forward+ constituent la base actuelle du projet fil rouge `Project Asteria`. Les neuf chapitres de fondation et les quatre chapitres de plateforme IA locale sont complets. Dix des douze systèmes de gameplay sont documentés. Le chapitre 23 sépare identités institutionnelles, lois, autorisations, allégations, preuves, verdicts et sanctions, puis coordonne les effets externes par des ports. Le workflow léger valide chaque chapitre sans PDF ; la publication complète reste différée à la fin du Livre II.', roadmap, count=1)
if n != 1:
    raise RuntimeError('Unable to update roadmap status')
write(ROADMAP, roadmap)

contents = read(CONTENTS)
contents = replace_once(contents, 'Livre-II/CHAPITRE-22-Monde-vivant-et-simulation-ecologique.md', 'Livre-II/CHAPITRE-22-Monde-vivant-et-simulation-ecologique.md\nLivre-II/CHAPITRE-23-Politique-factions-et-justice.md', 'contents chapter')
contents = replace_once(contents, 'Livre-II/QA/AUDIT-CHAPITRE-22.md', 'Livre-II/QA/AUDIT-CHAPITRE-22.md\nLivre-II/QA/AUDIT-CHAPITRE-23.md', 'contents audit')
contents = replace_once(contents, 'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-22.yaml', 'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-22.yaml\nLivre-II/QA/VALIDATION-FINALE-CHAPITRE-23.yaml', 'contents proof')
write(CONTENTS, contents)

if '23 chapitres sur 30' not in read(CONTINUITY): raise RuntimeError('Continuity progress not updated')
if 'CHAPITRE-24-Construction-et-gestion-de-domaines.md' not in read(CONTINUITY): raise RuntimeError('Next action not updated')
