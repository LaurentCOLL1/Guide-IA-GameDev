#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path('.')
STAMP = '2026-07-21T21:00:05+02:00'


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding='utf-8')


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding='utf-8')


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected one occurrence, found {count}')
    return text.replace(old, new, 1)


def regex_once(text: str, pattern: str, replacement: str, label: str, flags: int = 0) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f'{label}: expected one regex match, found {count}')
    return updated

path = 'Livre-II/index.md'
text = read(path)
text = replace_once(text, 'version: "1.18.1"', 'version: "1.19.0"', 'index version')
text = replace_once(text, '27. Tests unitaires, tests d’intégration et simulations — à rédiger', '27. [Tests unitaires, tests d’intégration et simulations](CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md) — **rédigé, repéré, expliqué bloc par bloc, suites, doubles et simulations déterministes documentés, audité au niveau static-review**', 'index chapter 27')
text = replace_once(text, '- [audit du chapitre 26](QA/AUDIT-CHAPITRE-26.md) ;', '- [audit du chapitre 26](QA/AUDIT-CHAPITRE-26.md) ;\n- [audit du chapitre 27](QA/AUDIT-CHAPITRE-27.md) ;', 'index audit 27')
text = replace_once(text, 'Les chapitres 3 à 26 ont utilisé **Élevée**.', 'Les chapitres 3 à 27 ont utilisé **Élevée**.', 'index reasoning range')
text = replace_once(text, 'Les chapitres 17 à 26 utilisent désormais des explications structurées', 'Les chapitres 17 à 27 utilisent désormais des explications structurées', 'index explanation range')
text = regex_once(text, r'Le milestone \*\*M3 — Livre II : Développement et architecture\*\* est en cours\. \*\*Vingt-six chapitres sur trente\*\* sont rédigés, repérés et audités au niveau documentaire et statique\. Les neuf chapitres de fondation, les quatre chapitres de plateforme IA locale et les douze systèmes de gameplay sont complets\. La partie industrialisation compte \*\*un chapitre sur cinq\*\* : outils d’édition, validation, import, provenance et pipelines de contenu\. Les réserves runtime et le PDF restent différés conformément au protocole QA\.', 'Le milestone **M3 — Livre II : Développement et architecture** est en cours. **Vingt-sept chapitres sur trente** sont rédigés, repérés et audités au niveau documentaire et statique. Les neuf chapitres de fondation, les quatre chapitres de plateforme IA locale et les douze systèmes de gameplay sont complets. La partie industrialisation compte **deux chapitres sur cinq** : outils d’édition et pipelines de contenu, puis tests unitaires, intégration et simulations déterministes. Les réserves runtime et le PDF restent différés conformément au protocole QA.', 'index status')
write(path, text)

path = 'ROADMAP.md'
text = read(path)
text = replace_once(text, '- [ ] Douze grands systèmes de jeu — 12 chapitres rédigés, repérés et audités sur 12.', '- [x] Douze grands systèmes de jeu — 12 chapitres rédigés, repérés et audités sur 12.', 'roadmap gameplay complete')
text = replace_once(text, '- [ ] Industrialisation du projet — 1 chapitre rédigé, repéré et audité sur 5.', '- [ ] Industrialisation du projet — 2 chapitres rédigés, repérés et audités sur 5.', 'roadmap industrialisation')
text = replace_once(text, '- [x] Convention des outils et contextes appliquée aux chapitres 1 à 26.', '- [x] Convention des outils et contextes appliquée aux chapitres 1 à 27.', 'roadmap contexts')
text = replace_once(text, '- [x] Chapitre 26 — plugins d’éditeur, docks, inspecteurs, validation, importeurs, provenance, staging et pipelines de contenu — rédigé et audité au niveau `static-review`.', '- [x] Chapitre 26 — plugins d’éditeur, docks, inspecteurs, validation, importeurs, provenance, staging et pipelines de contenu — rédigé et audité au niveau `static-review`.\n- [x] Chapitre 27 — tests unitaires, intégration, doubles, fixtures, simulations déterministes, non-régression et critères de passage — rédigé et audité au niveau `static-review`.', 'roadmap chapter 27')
text = regex_once(text, r'\*\*Statut M3 : en cours — 26 chapitres rédigés, repérés et audités sur 30\.\*\*[^\n]*', '**Statut M3 : en cours — 27 chapitres rédigés, repérés et audités sur 30.** Godot 4.7.1-stable, l’édition Standard, GDScript typé et Forward+ constituent la base actuelle de `Project Asteria`. Les fondations, la plateforme IA locale et les douze systèmes de gameplay sont documentés. Les deux premiers chapitres d’industrialisation couvrent les pipelines de contenu puis une stratégie de tests unitaires, d’intégration et de simulations déterministes avec GUT, doubles, fixtures, scénarios versionnés et critères de passage. Le workflow léger valide chaque chapitre sans PDF ; la publication complète reste différée à la fin du Livre II.', 'roadmap status')
write(path, text)

path = 'contents.txt'
text = read(path)
text = replace_once(text, 'Livre-II/CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md', 'Livre-II/CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md\nLivre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md', 'contents chapter 27')
text = replace_once(text, 'Livre-II/QA/AUDIT-CHAPITRE-26.md', 'Livre-II/QA/AUDIT-CHAPITRE-26.md\nLivre-II/QA/AUDIT-CHAPITRE-27.md', 'contents audit 27')
text = replace_once(text, 'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-26.yaml', 'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-26.yaml\nLivre-II/QA/VALIDATION-FINALE-CHAPITRE-27.yaml', 'contents proof 27')
write(path, text)

path = 'CONTINUITE-PROJET.md'
text = read(path)
text = replace_once(text, 'version: "3.26.2"', 'version: "3.27.0"', 'continuity version')
text = regex_once(text, r'last-updated: "[^"]+"', f'last-updated: "{STAMP}"', 'continuity timestamp')
text = replace_once(text, '**En cours : 26 chapitres sur 30.**', '**En cours : 27 chapitres sur 30.**', 'continuity progress collection')
text = replace_once(text, '27. Tests unitaires, tests d’intégration et simulations.', '27. Tests unitaires, tests d’intégration et simulations — terminé au niveau `static-review`.', 'continuity chapter list')
text = replace_once(text, 'Chapitres 3 à 26 : **Élevée**.', 'Chapitres 3 à 27 : **Élevée**.', 'continuity reasoning range')
text = replace_once(text, 'version `1.7.6`', 'version `1.7.8`', 'continuity protocol version')

decisions = '''### 11.23 Tests, intégration et simulations

- GUT 9.x constitue le framework de référence pour les scripts du projet, avec une révision compatible Godot 4.7 épinglée et sa licence MIT conservée ;
- les suites sont séparées entre tests unitaires, tests de composant, intégration, simulations et campagnes de plateforme ;
- les règles pures utilisent builders, fixtures, fakes, stubs et spies sans charger une scène inutilement ;
- un `SceneTree` réel est utilisé uniquement lorsque le cycle de vie Godot, les signaux, les frames ou la physique appartiennent au contrat ;
- horloge logique, RNG, dépôts et services externes sont injectés et contrôlés par le test ;
- fichiers, bases SQLite et workspaces utilisent des racines temporaires uniques et sont nettoyés après chaque cas ;
- chaque simulation déclare un scénario versionné, ses graines, un maximum de ticks et des invariants vérifiés pendant l’exécution ;
- snapshots, événements canoniques et empreintes permettent de comparer deux exécutions sans dépendre du rendu ;
- les golden files sont revus explicitement et ne sont jamais régénérés automatiquement par le test qui les compare ;
- les exécutions headless conservent les codes de sortie et publient les rapports JUnit et artefacts de diagnostic ;
- aucun retry automatique ne masque un test instable ; les services IA et réseaux réels restent hors des suites déterministes.

'''
text = replace_once(text, '## 24. Erreurs à ne pas reproduire', decisions + '## 24. Erreurs à ne pas reproduire', 'continuity decisions section')

test_errors = '''- ne pas présenter `godot --test` comme le runner des scripts GDScript du projet ;
- ne pas laisser le framework de test entrer dans les dépendances runtime ;
- ne pas utiliser l’heure système, un RNG global ou un ordre de dictionnaire comme oracle ;
- ne pas partager un fixture mutable entre deux tests ;
- ne pas lancer un serveur IA ou réseau réel dans une suite déterministe ;
- ne pas comparer un `float` par égalité stricte lorsqu’une tolérance appartient au contrat ;
- ne pas générer un golden file depuis le test qui doit le vérifier ;
- ne pas utiliser un retry automatique pour masquer un test instable ;
- ne pas oublier de borner les attentes de signaux, le nombre de ticks et les files simulées ;
- ne pas considérer une couverture élevée comme preuve de qualité ou de correction métier ;
'''
text = replace_once(text, '- ne pas oublier la mise à jour de ce fichier.', test_errors + '\n- ne pas oublier la mise à jour de ce fichier.', 'continuity test errors')
text = replace_once(text, '- progression : 26 chapitres sur 30 ;', '- progression : 27 chapitres sur 30 ;\n- industrialisation : 2 chapitres sur 5 ;', 'continuity state progress')
text = replace_once(text, '- chapitre 26 : version `1.0.2` ;', '- chapitre 26 : version `1.0.2` ;\n- chapitre 27 : version `1.0.0` ;', 'continuity chapter version')

next_action = '''## 26. Prochaine action

Le chapitre 27 est terminé au niveau `static-review`. La stratégie de tests sépare unités, composants, intégrations, simulations et campagnes de plateforme ; elle contrôle les dépendances, le temps, l’aléatoire, les stockages temporaires, les scénarios et les critères de passage sans revendiquer une exécution runtime non réalisée.

Chapitre suivant :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Périmètre attendu : journalisation structurée, niveaux de sévérité, identifiants d’événements stables, corrélation et causalité, rédaction des secrets, métriques, traces, paquets de diagnostic, manifestes de reproduction, collecte après crash et support hors ligne. Le chapitre 28 exploitera les sorties des tests sans redéfinir leurs suites, fixtures ou scénarios.

'''
text = regex_once(text, r'## 26\. Prochaine action\n.*?(?=## 27\. Journal)', next_action, 'continuity next action', flags=re.S)

journal = f'''### {STAMP} — version 3.27.0

- chapitre 27 créé, relu et audité au niveau `static-review` ;
- niveaux unitaires, composants, intégration, simulations et plateformes distingués ;
- GUT 9.x, dépendance épinglée, doubles, fixtures, builders, `SceneTree`, signaux et exécution headless documentés ;
- horloges, RNG, stockages temporaires, scénarios versionnés, graines, invariants, empreintes et golden files encadrés ;
- critères de passage, rapports JUnit et artefacts de diagnostic définis sans retry masquant les échecs ;
- progression portée à 27 chapitres sur 30 et prochaine action déplacée vers le chapitre 28 ;
- aucun test runtime revendiqué et aucun PDF construit.

'''
text = replace_once(text, '## 27. Journal\n\n', '## 27. Journal\n\n' + journal, 'continuity journal')
write(path, text)

chapter = read('Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md')
assert '__CHAPTER_CONTENT_PLACEHOLDER__' not in chapter
assert 'recommended-reasoning' not in chapter
assert 'Niveau GPT-5.6 Sol' not in chapter
assert '<!-- qa:error-correction-section -->' in chapter
assert chapter.count('<!-- qa:code-explanation -->') == 64
assert chapter.count('**Explication structurée du bloc :**') == 44
assert chapter.count('**Pourquoi cet exemple est fautif :**') == 10
assert chapter.count('**Pourquoi la correction fonctionne :**') == 10
assert '## 50. Mode Solo' in chapter
assert '## 51. Mode Studio' in chapter
assert '## 52. Contrat commun Solo et Studio' in chapter
assert '## 58. Décisions retenues pour Project Asteria' in chapter
print('Chapter 27 governance finalized.')
