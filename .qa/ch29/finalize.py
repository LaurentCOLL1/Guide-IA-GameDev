#!/usr/bin/env python3
from pathlib import Path
import re

ROOT=Path('.')
STAMP='2026-07-22T04:30:00+02:00'

def read(path): return (ROOT/path).read_text(encoding='utf-8')
def write(path,text): (ROOT/path).write_text(text,encoding='utf-8')
def replace_once(text,old,new,label):
    c=text.count(old)
    if c!=1: raise RuntimeError(f'{label}: expected 1 occurrence, got {c}')
    return text.replace(old,new,1)
def regex_once(text,pattern,repl,label,flags=0):
    new,c=re.subn(pattern,repl,text,count=1,flags=flags)
    if c!=1: raise RuntimeError(f'{label}: expected 1 match, got {c}')
    return new

# Livre-II/index.md
path='Livre-II/index.md'; text=read(path)
text=replace_once(text,'version: "1.20.0"','version: "1.21.0"','index version')
text=replace_once(text,'29. Automatisation Python et génération de données — à rédiger','29. [Automatisation Python et génération de données](CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md) — **rédigé, repéré, expliqué bloc par bloc, environnements, CLI, schémas, génération déterministe, reprise et artefacts reproductibles documentés, audité au niveau static-review**','index chapter29')
text=replace_once(text,'- [audit du chapitre 28](QA/AUDIT-CHAPITRE-28.md) ;','- [audit du chapitre 28](QA/AUDIT-CHAPITRE-28.md) ;\n- [audit du chapitre 29](QA/AUDIT-CHAPITRE-29.md) ;','index audit29')
text=replace_once(text,'Les chapitres 3 à 28 ont utilisé **Élevée**.','Les chapitres 3 à 29 ont utilisé **Élevée**.','index reasoning')
text=replace_once(text,'Les chapitres 17 à 28 utilisent désormais des explications structurées','Les chapitres 17 à 29 utilisent désormais des explications structurées','index explanations')
text=regex_once(text,r'Le milestone \*\*M3 — Livre II : Développement et architecture\*\* est en cours\. \*\*Vingt-sept chapitres sur trente\*\* sont rédigés, repérés et audités au niveau documentaire et statique\. Les neuf chapitres de fondation, les quatre chapitres de plateforme IA locale et les douze systèmes de gameplay sont complets\. La partie industrialisation compte \*\*deux chapitres sur cinq\*\* : outils d’édition et pipelines de contenu, puis tests unitaires, intégration et simulations déterministes\. Les réserves runtime et le PDF restent différés conformément au protocole QA\.', 'Le milestone **M3 — Livre II : Développement et architecture** est en cours. **Vingt-neuf chapitres sur trente** sont rédigés, repérés et audités au niveau documentaire et statique. Les neuf chapitres de fondation, les quatre chapitres de plateforme IA locale et les douze systèmes de gameplay sont complets. La partie industrialisation compte **quatre chapitres sur cinq** : pipelines de contenu, tests et simulations, observabilité et reproductibilité, puis automatisation Python et génération déterministe de données. Les réserves runtime et le PDF restent différés conformément au protocole QA.', 'index status')
write(path,text)

# ROADMAP
path='ROADMAP.md'; text=read(path)
text=replace_once(text,'- [ ] Industrialisation du projet — 3 chapitres rédigés, repérés et audités sur 5.','- [ ] Industrialisation du projet — 4 chapitres rédigés, repérés et audités sur 5.','roadmap industrialisation')
text=replace_once(text,'- [x] Convention des outils et contextes appliquée aux chapitres 1 à 28.','- [x] Convention des outils et contextes appliquée aux chapitres 1 à 29.','roadmap contexts')
text=replace_once(text,'- [x] Chapitre 28 — journalisation structurée, sévérité, corrélation, causalité, métriques, traces, rédaction, paquets de diagnostic et support hors ligne — rédigé et audité au niveau `static-review`.','- [x] Chapitre 28 — journalisation structurée, sévérité, corrélation, causalité, métriques, traces, rédaction, paquets de diagnostic et support hors ligne — rédigé et audité au niveau `static-review`.\n- [x] Chapitre 29 — environnement Python, CLI typées, schémas, génération déterministe, orchestration, parallélisme borné, checkpoints, manifestes et archives reproductibles — rédigé et audité au niveau `static-review`.','roadmap chapter29')
text=regex_once(text,r'\*\*Statut M3 : en cours — 28 chapitres rédigés, repérés et audités sur 30\.\*\*[^\n]*','**Statut M3 : en cours — 29 chapitres rédigés, repérés et audités sur 30.** Godot 4.7.1-stable, l’édition Standard, GDScript typé, Forward+ et CPython 3.14.6 constituent la base actuelle de `Project Asteria`. Les fondations, la plateforme IA locale et les douze systèmes de gameplay sont documentés. Les quatre premiers chapitres d’industrialisation couvrent les pipelines de contenu, les tests déterministes, l’observabilité et les paquets de reproduction, puis l’automatisation Python, les schémas et la génération déterministe de données. Le workflow léger valide chaque chapitre sans PDF ; la publication complète reste différée à la fin du Livre II.','roadmap status')
write(path,text)

# contents
path='contents.txt'; text=read(path)
text=replace_once(text,'Livre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md','Livre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md\nLivre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md','contents chapter29')
text=replace_once(text,'Livre-II/QA/AUDIT-CHAPITRE-28.md','Livre-II/QA/AUDIT-CHAPITRE-28.md\nLivre-II/QA/AUDIT-CHAPITRE-29.md','contents audit29')
text=replace_once(text,'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-28.yaml','Livre-II/QA/VALIDATION-FINALE-CHAPITRE-28.yaml\nLivre-II/QA/VALIDATION-FINALE-CHAPITRE-29.yaml','contents proof29')
write(path,text)

# continuity
path='CONTINUITE-PROJET.md'; text=read(path)
text=replace_once(text,'version: "3.28.0"','version: "3.29.0"','continuity version')
text=regex_once(text,r'last-updated: "[^"]+"',f'last-updated: "{STAMP}"','continuity timestamp')

decisions='''### 11.24 Journalisation, diagnostic et reproductibilité

- journaux, métriques et traces restent descriptifs et n’acquièrent aucune autorité métier ;
- les événements utilisent des identifiants stables, des sévérités explicites et une corrélation séparée de la causalité ;
- UTC décrit un instant civil, un compteur monotone mesure une durée et le tick logique ordonne la simulation ;
- secrets, jetons, clés, chaînes de connexion, prompts et réponses IA brutes sont exclus des exports ;
- métriques et traces utilisent une cardinalité bornée et des politiques d’échantillonnage conservant les événements graves ;
- le logger moteur multithread écrit dans une file protégée sans rappel récursif de la journalisation ;
- un marqueur de session non fermé indique une fin non propre possible, jamais une preuve certaine de crash ;
- les paquets de diagnostic utilisent une liste fermée, des chemins relatifs, un manifeste, des empreintes et un consentement explicite ;
- ZIP est un conteneur compressé et ne constitue ni un chiffrement ni une signature ;
- le support hors ligne reste possible sans transmission distante obligatoire.

### 11.25 Automatisation Python et génération de données

- CPython 3.14.6 constitue la référence documentaire du paquet `asteria-tools` ;
- les environnements utilisent `venv`, `pyproject.toml` et des verrous séparés lorsque la plateforme l’exige ;
- `pip lock` reste expérimental et ne devient obligatoire qu’après validation dans le Starter Kit ;
- les CLI utilisent `argparse`, des codes de sortie stables et des chemins `Path` confinés ;
- configurations TOML, instances JSON, checkpoints et manifestes portent une version ;
- JSON Schema Draft 2020-12 valide les échanges sans remplacer les règles métier ;
- les générateurs utilisent des RNG locaux, des graines dérivées, des identités et des ordres stables ;
- les écritures passent par staging, validation, empreintes et promotion contrôlée ;
- les processus externes reçoivent une liste d’arguments, `shell=False`, des délais et leurs codes non nuls conservés ;
- le parallélisme est borné et les résultats sont réordonnés canoniquement ;
- une reprise exige un plan identique et des empreintes valides ;
- les nouvelles tentatives sont limitées à des erreurs transitoires cataloguées ;
- chaque lot publiable possède provenance, manifeste, SHA-256, rapport et archive vérifiée ;
- Python orchestre les chapitres 26 à 28 sans acquérir d’autorité métier.

'''
text=replace_once(text,'## 24. Erreurs à ne pas reproduire',decisions+'## 24. Erreurs à ne pas reproduire','continuity decisions')

new_errors='''- ne pas utiliser un environnement Python global pour le projet ;
- ne pas présenter `pip freeze` comme un verrou résolu ;
- ne pas traiter `pip lock` comme une interface stabilisée tant que son statut reste expérimental ;
- ne pas accepter une configuration TOML ou JSON sans limite de taille et validation de version ;
- ne pas construire une commande externe par concaténation ni avec `shell=True` ;
- ne pas laisser un chemin configuré sortir du workspace autorisé ;
- ne pas utiliser le RNG global ou `hash()` pour une génération reproductible ;
- ne pas dépendre de l’ordre du système de fichiers ou de l’ordre de fin des tâches parallèles ;
- ne pas écrire directement dans les sources ou sorties publiées ; utiliser staging, validation et promotion ;
- ne pas reprendre une tâche sur la seule présence d’un fichier ; vérifier plan et empreinte ;
- ne pas retenter sans limite ni retenter une erreur de schéma, d’intégrité ou d’autorité ;
- ne pas lancer un pool non borné ni utiliser `ProcessPoolExecutor` avec des fonctions non sérialisables ;
- ne pas considérer SHA-256 comme une preuve d’auteur ou ZIP comme un chiffrement ;
- ne pas laisser l’orchestrateur Python modifier directement un état métier Godot ;
'''
text=replace_once(text,'- ne pas oublier la mise à jour de ce fichier.',new_errors+'\n- ne pas oublier la mise à jour de ce fichier.','continuity errors')
text=replace_once(text,'- progression : 28 chapitres sur 30 ;','- progression : 29 chapitres sur 30 ;','continuity progress')
text=replace_once(text,'- industrialisation : 3 chapitres sur 5 ;','- industrialisation : 4 chapitres sur 5 ;','continuity industrialisation')
text=replace_once(text,'- chapitre 28 : version `1.0.0` ;','- chapitre 28 : version `1.0.0` ;\n- chapitre 29 : version `1.0.0` ;','continuity chapter version')
next_action='''## 26. Prochaine action

Le chapitre 29 est terminé au niveau `static-review`. L’automatisation Python sépare environnement, configuration, planification, exécution, validation et publication ; elle stabilise graines, ordres, chemins, codes de sortie, checkpoints, empreintes et manifestes sans transférer l’autorité métier aux scripts.

Chapitre suivant :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Périmètre attendu : synthèse finale du Livre II, architecture de référence pour Mode Solo et Mode Studio, responsabilités, profils d’environnement, conventions de modules, flux de travail, revues, validations, intégration continue, empaquetage, exploitation locale, critères de passage et plan de matérialisation du Starter Kit. Le chapitre 30 consolidera les contrats existants sans créer une nouvelle autorité transversale.

'''
text=regex_once(text,r'## 26\. Prochaine action\n.*?(?=## 27\. Journal)',next_action,'continuity next action',flags=re.S)
journal=f'''### {STAMP} — version 3.29.0

- chapitre 29 créé, relu et audité au niveau `static-review` ;
- CPython 3.14.6, environnements virtuels, `pyproject.toml`, verrouillage et CLI typées documentés ;
- configurations versionnées, JSON Schema, génération déterministe, graines locales et identités stables encadrés ;
- processus externes, parallélisme borné, reprise par checkpoint, staging, promotion, manifestes et archives vérifiées définis ;
- chapitres 26 à 28 orchestrés sans transfert d’autorité métier ;
- progression portée à 29 chapitres sur 30 et prochaine action déplacée vers le chapitre 30 ;
- aucun test runtime revendiqué et aucun PDF construit.

'''
text=replace_once(text,'## 27. Journal\n\n','## 27. Journal\n\n'+journal,'continuity journal')
write(path,text)

# chapter assertions
chapter=read('Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md')
assert 'recommended-reasoning' not in chapter
assert 'Niveau GPT-5.6 Sol' not in chapter
for forbidden in ('durée murale','temps mur','temps mural','temps horloge'):
    assert forbidden.casefold() not in chapter.casefold(), forbidden
assert chapter.count('<!-- qa:code-explanation -->') == 65
assert chapter.count('**Explication structurée du bloc :**') == 45
assert chapter.count('**Pourquoi cet exemple est fautif :**') == 10
assert chapter.count('**Pourquoi la correction fonctionne :**') == 10
assert '<!-- qa:error-correction-section -->' in chapter
assert '## 50. Mode Solo' in chapter and '## 51. Mode Studio' in chapter
assert '## 55. Décisions retenues pour Project Asteria' in chapter
print('Chapter 29 governance finalized.')
