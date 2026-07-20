from __future__ import annotations

from datetime import datetime
from pathlib import Path
import re
from zoneinfo import ZoneInfo

ROOT = Path('.')
NOW = datetime.now(ZoneInfo('Europe/Paris')).replace(microsecond=0).isoformat()
BASE_COMMIT = '86ce004b5bb115a8a7d17f92adf0af6049dfcf9c'


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected one occurrence, found {count}')
    return text.replace(old, new, 1)


# Chapter 17.
chapter_path = ROOT / 'Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md'
chapter = chapter_path.read_text(encoding='utf-8')
chapter = replace_once(chapter, 'version: "1.0.2"', 'version: "1.0.3"', 'chapter version')
chapter = re.sub(r'^last-verified: ".+"$', f'last-verified: "{NOW}"', chapter, count=1, flags=re.M)
chapter = re.sub(r'^audit-date: ".+"$', f'audit-date: "{NOW}"', chapter, count=1, flags=re.M)
marker = '## 44. Prochaine étape\n'
if marker not in chapter:
    raise RuntimeError('chapter 44 next-step marker missing')
chapter = chapter[:chapter.index(marker)] + '''## 44. Synthèse opérationnelle pour Project Asteria

Le système d’agents autonomes de `Project Asteria` repose sur les décisions suivantes :

1. l’état logique d’un agent reste séparé du nœud actif, du personnage, du social et de la famille ;
2. les perceptions deviennent des faits structurés, sourcés, bornés et expirables ;
3. la mémoire et le tableau noir sont limités afin de maîtriser coût, persistance et diagnostic ;
4. les buts durables sont distincts des intentions, des plans et des requêtes d’action transitoires ;
5. le catalogue d’actions constitue un vocabulaire fermé avec préconditions, effets, coûts et exécuteurs autorisés ;
6. le planificateur utilise des snapshots détachés, un ordre canonique et des budgets logiques ;
7. l’ordonnanceur répartit les décisions par phases et conserve une échéance reportée jusqu’au traitement effectif ;
8. les modes actif, arrière-plan et dormant modifient la fréquence de décision sans supprimer l’existence logique ;
9. les plans sont invalidés lorsque la révision du monde ou les préconditions ne correspondent plus ;
10. l’IA générative reste consultative et ses suggestions sont filtrées avant toute décision métier ;
11. seules les données durables sont sauvegardées, puis restaurées dans un candidat validé avant remplacement ;
12. le combat, les compétences, l’économie, le monde vivant, la politique et la narration restent autorités de leurs propres règles.

Cette clôture décrit l’état retenu pour le projet fil rouge. Les instructions concernant le chapitre suivant restent exclusivement dans `CONTINUITE-PROJET.md`.
'''
if 'Livre-II/CHAPITRE-18-Combat.md' in chapter or 'Niveau GPT-5.6 Sol recommandé' in chapter:
    raise RuntimeError('next-chapter production instructions remain in chapter 17')
if not chapter.rstrip().endswith('`CONTINUITE-PROJET.md`.'):
    raise RuntimeError('Project Asteria closure is not the final chapter content')
chapter_path.write_text(chapter, encoding='utf-8')
chapter_lines = len(chapter.splitlines())
chapter_blocks = len(re.findall(r'^```', chapter, flags=re.M)) // 2
chapter_markers = chapter.count('<!-- qa:code-explanation -->')
chapter_lecture = len(re.findall(r'^> \*\*\[LECTURE\]', chapter, flags=re.M))

# Audit report.
audit_path = ROOT / 'Livre-II/QA/AUDIT-CHAPITRE-17.md'
audit = audit_path.read_text(encoding='utf-8')
audit = replace_once(audit, 'version: "1.0.2"', 'version: "1.0.3"', 'audit version')
audit = replace_once(audit, 'chapter-version: "1.0.2"', 'chapter-version: "1.0.3"', 'audit chapter version')
audit = re.sub(r'^audit-date: ".+"$', f'audit-date: "{NOW}"', audit, count=1, flags=re.M)
audit = re.sub(r'^last-verified: ".+"$', f'last-verified: "{NOW}"', audit, count=1, flags=re.M)
audit = re.sub(r'- lignes finales : \*\*\d+\*\* ;', f'- lignes finales : **{chapter_lines}** ;', audit, count=1)
audit = re.sub(r'- blocs clôturés : \*\*\d+\*\* ;', f'- blocs clôturés : **{chapter_blocks}** ;', audit, count=1)
audit = re.sub(r'- marqueurs d’explication : \*\*\d+\*\* ;', f'- marqueurs d’explication : **{chapter_markers}** ;', audit, count=1)
if '## 9. Addendum de clôture' not in audit:
    audit += f'''\n## 9. Addendum de clôture — version 1.0.3\n\nLa section `44. Prochaine étape` a été retirée du chapitre. Le chemin et le niveau du chapitre suivant sont des informations de pilotage du projet et restent dans `CONTINUITE-PROJET.md`, pas dans le texte destiné au lecteur.\n\nLa fin du chapitre porte désormais une synthèse opérationnelle des décisions retenues pour `Project Asteria`, conformément aux chapitres de systèmes précédents. La vérification corrective est horodatée `{NOW}`.\n'''
audit_path.write_text(audit, encoding='utf-8')

# QA protocol.
protocol_path = ROOT / 'Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md'
protocol = protocol_path.read_text(encoding='utf-8')
protocol = replace_once(protocol, 'version: "1.7.3"', 'version: "1.7.4"', 'protocol version')
protocol = re.sub(r'^last-verified: ".+"$', f'last-verified: "{NOW}"', protocol, count=1, flags=re.M)
anchor = '**Règle de décision :** si un lecteur débutant doit deviner la fonction d’une ligne importante, d’un paramètre, d’un type, d’un retour ou d’un effet de bord, le bloc est non conforme et le chapitre ne peut pas passer l’audit.'
addition = '''### Q1.1.2 — Clôture du chapitre et pilotage du projet

Le texte destiné au lecteur ne contient pas de section `Prochaine étape`, de chemin canonique du chapitre suivant, de niveau GPT conseillé pour une future rédaction ni d’instruction de pilotage éditorial. Ces informations appartiennent exclusivement à la section `Prochaine action` de `CONTINUITE-PROJET.md`.

Pour les chapitres 14 à 25 consacrés aux systèmes de gameplay, la dernière section éditoriale synthétise les décisions effectivement retenues pour `Project Asteria`. Elle rappelle les responsabilités, invariants et frontières du système sans annoncer le contenu à produire ensuite.

La présence d’instructions de production dans un chapitre publié, ou l’absence de synthèse `Project Asteria` dans un chapitre de système, bloque l’audit.

'''
if addition not in protocol:
    protocol = replace_once(protocol, anchor, addition + anchor, 'protocol closure rule')
protocol_path.write_text(protocol, encoding='utf-8')

# Continuity.
continuity_path = ROOT / 'CONTINUITE-PROJET.md'
continuity = continuity_path.read_text(encoding='utf-8')
continuity = replace_once(continuity, 'version: "3.17.9"', 'version: "3.17.10"', 'continuity version')
continuity = re.sub(r'^last-updated: ".+"$', f'last-updated: "{NOW}"', continuity, count=1, flags=re.M)
old_rule = 'À chaque clôture de chapitre, le bloc **Prochaine action** doit contenir dans le même bloc de texte le chemin canonique et la ligne `Niveau GPT-5.6 Sol recommandé : Moyenne ou Élevée`.'
new_rule = 'À chaque clôture de chapitre, la section **Prochaine action** de `CONTINUITE-PROJET.md` doit contenir dans le même bloc de texte le chemin canonique et la ligne `Niveau GPT-5.6 Sol recommandé : Moyenne ou Élevée`. Le chapitre publié ne contient ni section `Prochaine étape`, ni chemin ou niveau du chapitre suivant : ces informations restent exclusivement dans la continuité du projet.'
continuity = replace_once(continuity, old_rule, new_rule, 'continuity next-action rule')
anchor = 'À partir du chapitre 17 version `1.0.2`, `last-verified` et `audit-date` sont des chaînes ISO 8601 complètes avec heure, secondes et décalage UTC, dans le fuseau `Europe/Paris`. Une heure historique inconnue n’est jamais reconstruite : les documents antérieurs passent au format horodaté seulement lors de leur prochaine révision réellement auditée.'
closure_rule = '\n\nLes chapitres 14 à 25 se terminent par une synthèse opérationnelle des décisions retenues pour `Project Asteria`. Les informations de pilotage éditorial et la préparation du chapitre suivant restent dans la section `Prochaine action` de ce fichier, jamais dans le chapitre destiné au lecteur.'
if closure_rule.strip() not in continuity:
    continuity = replace_once(continuity, anchor, anchor + closure_rule, 'continuity Project Asteria closure rule')
continuity = replace_once(continuity, '- chapitre 17 : version `1.0.2` ;', '- chapitre 17 : version `1.0.3` ;', 'continuity chapter state')
continuity = replace_once(continuity, 'version `1.7.3`', 'version `1.7.4`', 'continuity protocol version')
error_anchor = '- ne pas construire le PDF à chaque chapitre ;\n- ne pas oublier la mise à jour de ce fichier.'
error_new = '- ne pas construire le PDF à chaque chapitre ;\n- ne pas placer la prochaine étape, le chemin ou le niveau du chapitre suivant dans le chapitre publié ;\n- ne pas terminer un chapitre de système sans synthèse opérationnelle de `Project Asteria` ;\n- ne pas oublier la mise à jour de ce fichier.'
continuity = replace_once(continuity, error_anchor, error_new, 'continuity do-not-repeat rules')
if '### 2026-07-20 — version 3.17.10' not in continuity:
    journal = f'''### 2026-07-20 — version 3.17.10\n\n- chapitre 17 porté en version `1.0.3` ;\n- section `Prochaine étape` retirée du texte destiné au lecteur ;\n- chemin et niveau du chapitre suivant conservés uniquement dans `CONTINUITE-PROJET.md` ;\n- clôture remplacée par une synthèse opérationnelle de `Project Asteria` ;\n- règle rendue obligatoire pour les chapitres de systèmes 14 à 25 ;\n- protocole QA porté en version `1.7.4` ;\n- aucun PDF construit et aucun test runtime revendiqué.\n\n'''
    continuity = replace_once(continuity, '## 27. Journal\n\n', '## 27. Journal\n\n' + journal, 'continuity journal')
continuity_path.write_text(continuity, encoding='utf-8')

# Index and roadmap.
index_path = ROOT / 'Livre-II/index.md'
index = index_path.read_text(encoding='utf-8')
index = replace_once(index, 'version: "1.12.3"', 'version: "1.12.4"', 'index version')
index = replace_once(
    index,
    '17. [Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md) — **rédigé, repéré, expliqué bloc par bloc, terminologie des retours clarifiée et audité au niveau static-review**',
    '17. [Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md) — **rédigé, repéré, expliqué bloc par bloc, terminologie des retours clarifiée, clôturé par les décisions Project Asteria et audité au niveau static-review**',
    'index chapter status',
)
index_path.write_text(index, encoding='utf-8')

roadmap_path = ROOT / 'ROADMAP.md'
roadmap = roadmap_path.read_text(encoding='utf-8')
roadmap_anchor = '- [x] Clarification du chapitre 17 — intervalles nominaux explicités, codes de retour distingués des erreurs pédagogiques et échéances reportées conservées.'
roadmap_line = '- [x] Correction de clôture du chapitre 17 — prochaine étape réservée à la continuité et synthèse finale consacrée à `Project Asteria`.'
if roadmap_line not in roadmap:
    roadmap = replace_once(roadmap, roadmap_anchor, roadmap_anchor + '\n' + roadmap_line, 'roadmap closure correction')
roadmap_path.write_text(roadmap, encoding='utf-8')

# Evidence reset before CI.
evidence_path = ROOT / 'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-17.yaml'
evidence = evidence_path.read_text(encoding='utf-8')
evidence = replace_once(evidence, 'status: complete', 'status: pending-ci', 'evidence status')
evidence = replace_once(evidence, f'validated-base-commit: 253f30c2ef869f36ac094b85c3bc60f666ded858', f'validated-base-commit: {BASE_COMMIT}', 'evidence base')
evidence = re.sub(r'^validated-head-commit: .+$', 'validated-head-commit: pending-ci', evidence, count=1, flags=re.M)
evidence = replace_once(evidence, 'version: 1.0.2', 'version: 1.0.3', 'evidence chapter version')
evidence = re.sub(r'^  chapter-lines: \d+$', f'  chapter-lines: {chapter_lines}', evidence, count=1, flags=re.M)
evidence = re.sub(r'^  chapter-code-and-data-blocks: \d+$', f'  chapter-code-and-data-blocks: {chapter_blocks}', evidence, count=1, flags=re.M)
evidence = re.sub(r'^  code-explanation-markers: \d+$', f'  code-explanation-markers: {chapter_markers}', evidence, count=1, flags=re.M)
evidence = re.sub(r'^    LECTURE: \d+$', f'    LECTURE: {chapter_lecture}', evidence, count=1, flags=re.M)
evidence = re.sub(r'^  total-context-blocks: \d+$', '  total-context-blocks: 1710', evidence, count=1, flags=re.M)
evidence = re.sub(r'^  marked-context-blocks: \d+$', '  marked-context-blocks: 1710', evidence, count=1, flags=re.M)
if '  next-step-absent-from-reader-chapter: true' not in evidence:
    evidence = replace_once(evidence, '  audit-timestamps-with-offset: true', '  audit-timestamps-with-offset: true\n  next-step-absent-from-reader-chapter: true\n  project-asteria-final-synthesis: true', 'evidence closure flags')
evidence = re.sub(r'(?ms)^ci:\n.*?^reservations:', '''ci:\n  validate-chapters-without-pdf:\n    run-id: pending\n    conclusion: pending\n  validate-usage-contexts:\n    run-id: pending\n    conclusion: pending\n  artifact:\n    id: pending\n    name: chapter-validation-without-pdf\n    digest: pending\nreservations:''', evidence, count=1)
evidence_path.write_text(evidence, encoding='utf-8')

print(f'timestamp={NOW}')
print(f'chapter_lines={chapter_lines}')
print(f'chapter_blocks={chapter_blocks}')
print(f'chapter_markers={chapter_markers}')
print(f'chapter_lecture={chapter_lecture}')
print('closure_fix=ok')
