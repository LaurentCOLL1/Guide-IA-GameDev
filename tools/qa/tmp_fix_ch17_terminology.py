from pathlib import Path
import re

ROOT = Path('.')
chapter_path = ROOT / 'Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md'
protocol_path = ROOT / 'Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md'
audit_path = ROOT / 'Livre-II/QA/AUDIT-CHAPITRE-17.md'
evidence_path = ROOT / 'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-17.yaml'
index_path = ROOT / 'Livre-II/index.md'
roadmap_path = ROOT / 'ROADMAP.md'
continuity_path = ROOT / 'CONTINUITE-PROJET.md'


def once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected 1 occurrence, found {count}')
    return text.replace(old, new, 1)

chapter = chapter_path.read_text(encoding='utf-8')
chapter = once(chapter, 'version: "1.0.0"', 'version: "1.0.1"', 'chapter version')

chapter = once(
    chapter,
    '- **Retours et erreurs :** `validate()` renvoie un code `Error` ; `next_sequence()` renvoie `-1` lorsque le tick régresse et n’altère alors aucun compteur.',
    '- **Valeurs de retour :** `validate()` renvoie un code de l’énumération `Error`. `next_sequence()` renvoie une séquence strictement positive après succès, ou la sentinelle `-1` lorsque le tick régresse ; dans ce dernier cas, aucun compteur n’est modifié.',
    'agent state return wording',
)
chapter = once(
    chapter,
    '- **Erreurs :** une clé inconnue produit `ERR_DOES_NOT_EXIST` ; un type incorrect produit `ERR_INVALID_DATA`.',
    '- **Codes de retour de `write()` :** une clé absente du schéma renvoie `ERR_DOES_NOT_EXIST` ; une valeur dont le type ne correspond pas au schéma renvoie `ERR_INVALID_DATA`. Dans les deux cas, `_values` reste inchangé.',
    'blackboard return wording',
)
chapter = once(
    chapter,
    '- **Erreurs :** une action invalide produit `ERR_INVALID_DATA` ; deux identifiants identiques produisent `ERR_ALREADY_EXISTS` ; aucun remplacement partiel n’est effectué.',
    '- **Codes de retour de `replace_all()` :** une action invalide renvoie `ERR_INVALID_DATA` ; deux actions portant le même `action_id` renvoient `ERR_ALREADY_EXISTS`. Le catalogue actif n’est remplacé qu’après validation complète du candidat.',
    'catalog return wording',
)
chapter = once(
    chapter,
    '- **Erreur fréquente :** `NO_PLAN` signifie que la recherche bornée a épuisé les possibilités autorisées ; `BUDGET_EXCEEDED` signifie qu’elle s’est arrêtée avant cette conclusion.',
    '- **Statuts à distinguer :** `NO_PLAN` signifie qu’aucune action n’est à exécuter dans le résultat courant : soit le but est déjà satisfait, soit la recherche complète n’a trouvé aucun chemin autorisé. `BUDGET_EXCEEDED` signifie que la limite d’expansions a interrompu la recherche avant qu’elle puisse conclure.',
    'plan status wording',
)
chapter = once(
    chapter,
    '- **Erreur attendue :** demander une clé non enregistrée produit un refus explicite, jamais un appel dynamique par nom de méthode fourni par les données.',
    '- **Refus contrôlé :** une clé absente du registre renvoie un échec explicite. Elle ne déclenche jamais le chargement d’une classe ou l’appel dynamique d’une méthode indiquée par les données.',
    'executor refusal wording',
)
chapter = once(
    chapter,
    '- **Erreurs :** le code de retour de `decide()` devrait être enregistré dans une trace ou un compteur ; le brouillon ne l’ignore que pour garder l’extrait centré sur l’ordonnancement.',
    '- **Traitement du résultat :** le code renvoyé par `decide()` doit être enregistré dans une trace ou un compteur. L’extrait ne le consomme pas afin de rester centré sur l’ordonnancement ; cette omission pédagogique ne signifie pas que l’application finale peut ignorer le résultat.',
    'scheduler result wording',
)
chapter = once(
    chapter,
    '- **Intervalles :** avec 60 ticks physiques par seconde, les valeurs correspondent approximativement à 10 décisions/s, 1 décision/s et 1 décision/10 s, mais la logique utilise les ticks et non les secondes murales.',
    '- **Intervalles nominaux :** avec `Engine.physics_ticks_per_second = 60`, le mode `ACTIVE` utilise `6` ticks, soit au plus `10` décisions par seconde ; `BACKGROUND` utilise `60` ticks, soit au plus `1` décision par seconde ; `DORMANT` utilise `600` ticks, soit au plus `1` décision toutes les `10` secondes. Ces équivalences changent si la fréquence physique du projet change. Elles restent nominales : lorsqu’un agent échu est reporté par le budget de l’ordonnanceur, sa décision réelle peut survenir plus tard, mais l’échéance demeure exprimée en ticks logiques.',
    'interval wording',
)
old_tick_policy = '''```gdscript
class_name AgentTickPolicy
extends RefCounted

const MAX_CATCH_UP_DECISIONS := 1

func is_due(
\tlogical_tick: int,
\tlast_decision_tick: int,
\tmode: AgentSimulationMode.Value,
\tphase: int,
) -> bool:
\tvar interval := AgentSimulationMode.decision_interval_ticks(mode)
\tif logical_tick < 0 or interval <= 0:
\t\treturn false
\tif last_decision_tick >= logical_tick:
\t\treturn false
\treturn (logical_tick + phase) % interval == 0
```'''
new_tick_policy = '''```gdscript
class_name AgentTickPolicy
extends RefCounted

func is_due(
\tlogical_tick: int,
\tlast_decision_tick: int,
\tmode: AgentSimulationMode.Value,
\tphase: int,
) -> bool:
\tvar interval := AgentSimulationMode.decision_interval_ticks(mode)
\tif logical_tick < 0 or interval <= 0:
\t\treturn false
\tif last_decision_tick >= logical_tick:
\t\treturn false

\tvar normalized_phase := posmod(phase, interval)
\tvar remainder := posmod(last_decision_tick + normalized_phase, interval)
\tvar ticks_until_next_slot := interval - remainder
\tvar next_due_tick := last_decision_tick + ticks_until_next_slot
\treturn logical_tick >= next_due_tick
```'''
chapter = once(chapter, old_tick_policy, new_tick_policy, 'tick policy code')
old_tick_explanation = '''- **Rôle :** la politique répartit les agents sur les ticks grâce à `phase`, tout en interdisant plusieurs décisions au même tick.
- **Phase :** elle est dérivée de manière stable depuis le `CharacterId`, par exemple `abs(hash(id)) % interval` ; elle ne provient pas d’un tirage aléatoire au démarrage.
- **Rattrapage :** après une longue pause, le système ne rejoue pas toutes les décisions manquées ; une seule nouvelle décision est autorisée, puis le monde courant est observé.
- **Vérification :** deux agents ayant des phases différentes doivent répartir leurs échéances sur l’intervalle.'''
new_tick_explanation = '''- **Rôle :** la politique calcule la première échéance canonique strictement postérieure à la dernière décision, puis indique si cette échéance est atteinte ou dépassée.
- **Phase :** `posmod()` ramène `phase` dans l’intervalle positif. La phase est dérivée de manière stable depuis le `CharacterId` ; elle ne provient pas d’un tirage aléatoire au démarrage.
- **Report conservé :** la comparaison `logical_tick >= next_due_tick` maintient l’agent échu tant que l’ordonnanceur ne l’a pas traité. Avec l’ancien test d’égalité modulo, un agent non visité au tick exact pouvait attendre tout un intervalle supplémentaire.
- **Rattrapage borné :** après une longue pause, `decide()` n’est appelé qu’une fois pour l’agent et observe le monde courant ; les créneaux manqués ne sont pas rejoués un par un.
- **Vérification :** deux agents de phases différentes répartissent leurs échéances, et un agent dépassant son créneau reste dû au tick suivant jusqu’à sa décision.'''
chapter = once(chapter, old_tick_explanation, new_tick_explanation, 'tick policy explanation')
chapter_path.write_text(chapter, encoding='utf-8')

protocol = protocol_path.read_text(encoding='utf-8')
protocol = once(protocol, 'version: "1.7.1"', 'version: "1.7.2"', 'protocol version')
anchor = '''Dans une section d’erreurs, d’anti-patterns, de pièges ou de corrections, le format privilégié est plus court : `Pourquoi cet exemple est fautif` sous le contre-exemple et `Pourquoi la correction fonctionne` sous la version corrigée. Un renvoi vers une section ou un chapitre antérieur peut être placé avant le code fautif lorsqu’il évite de répéter une règle déjà établie. Ce renvoi vise la sous-section exacte qui porte la règle ; une section parente n’est acceptable qu’en l’absence de cible plus précise. Son fragment doit être vérifié. Une ancre explicite et stable est privilégiée lorsque le fragment automatique du titre peut être ambigu, fragile ou dépendre du moteur Markdown.
'''
addition = anchor + '''
Hors de ces sections pédagogiques, le mot `erreur` ne sert pas de libellé générique pour tout résultat négatif. Employer :

- `Valeurs de retour` lorsqu’une fonction renvoie plusieurs formes de résultat, y compris une sentinelle ;
- `Codes de retour` lorsqu’une fonction renvoie des valeurs de l’énumération `Error` ;
- `Refus contrôlé` lorsqu’une entrée ou une opération est rejetée normalement par un contrat ;
- `Statuts à distinguer` lorsqu’il faut comparer plusieurs états métier ou résultats de recherche ;
- `Traitement du résultat` lorsque l’appelant doit consommer, journaliser ou propager la valeur renvoyée.

Le libellé `Erreur fréquente` est réservé à un véritable piège que le lecteur pourrait reproduire. S’il apparaît, il relève de Q1.2 et doit être accompagné d’un exemple fautif et d’une correction, ou être reformulé avec l’un des libellés précis ci-dessus.
'''
protocol = once(protocol, anchor, addition, 'protocol terminology insertion')
protocol_path.write_text(protocol, encoding='utf-8')

# Update audit report.
audit = audit_path.read_text(encoding='utf-8')
audit = once(audit, 'version: "1.0.0"', 'version: "1.0.1"', 'audit version')
audit = once(audit, 'chapter-version: "1.0.0"', 'chapter-version: "1.0.1"', 'audit chapter version')
audit_append = '''

## 7. Addendum terminologique et ordonnanceur — version 1.0.1

La relecture postérieure à la fusion a distingué six libellés ambigus hors de la section 37 :

- `Valeurs de retour` pour une sentinelle ou un résultat non limité à `Error` ;
- `Codes de retour` pour `ERR_*` ;
- `Refus contrôlé` pour une clé non enregistrée ;
- `Statuts à distinguer` pour `NO_PLAN` et `BUDGET_EXCEEDED` ;
- `Traitement du résultat` pour la consommation du retour de `decide()`.

La phrase des intervalles associe désormais explicitement `ACTIVE`, `BACKGROUND` et `DORMANT` aux valeurs `6`, `60` et `600`, précise la dépendance à `Engine.physics_ticks_per_second` et qualifie les fréquences de nominales.

L’audit a également détecté un défaut fonctionnel dans l’exemple de `AgentTickPolicy` : le test modulo exact pouvait perdre une échéance lorsque la limite de huit décisions empêchait de visiter l’agent au tick prévu. La politique calcule maintenant `next_due_tick` et utilise `logical_tick >= next_due_tick`, ce qui conserve l’échéance jusqu’au traitement effectif.
'''
if '## 7. Addendum terminologique et ordonnanceur — version 1.0.1' not in audit:
    audit += audit_append
audit_path.write_text(audit, encoding='utf-8')

# Evidence waits for CI closure.
evidence = evidence_path.read_text(encoding='utf-8')
evidence = once(evidence, 'status: complete', 'status: pending-ci', 'evidence status')
evidence = once(evidence, '  version: 1.0.0', '  version: 1.0.1', 'evidence chapter version')
evidence = re.sub(r'validated-head-commit: [0-9a-f]+', 'validated-head-commit: pending-ci', evidence, count=1)
evidence = re.sub(r'    run-id: \d+\n    conclusion: success', '    run-id: pending\n    conclusion: pending', evidence, count=2)
evidence = re.sub(r'    id: \d+\n    name: chapter-validation-without-pdf\n    digest: sha256:[0-9a-f]+', '    id: pending\n    name: chapter-validation-without-pdf\n    digest: pending', evidence, count=1)
insert = '''  terminology-clarified: true
  nominal-intervals-explicit: true
  overdue-decisions-preserved: true
  ambiguous-error-labels-outside-section-37: 0
'''
if '  terminology-clarified: true' not in evidence:
    evidence = evidence.replace('  prepared-save-section-documented: true\n', '  prepared-save-section-documented: true\n' + insert, 1)
evidence_path.write_text(evidence, encoding='utf-8')

index = index_path.read_text(encoding='utf-8')
index = once(index, 'version: "1.12.1"', 'version: "1.12.2"', 'index version')
index = once(
    index,
    '17. [Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md) — **rédigé, repéré, expliqué bloc par bloc et audité au niveau static-review**',
    '17. [Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md) — **rédigé, repéré, expliqué bloc par bloc, terminologie des retours clarifiée et audité au niveau static-review**',
    'index chapter line',
)
index_path.write_text(index, encoding='utf-8')

roadmap = roadmap_path.read_text(encoding='utf-8')
roadmap_anchor = '- [x] Chapitre 17 — perceptions, mémoire bornée, buts, planification déterministe, ordonnanceur, simulation hors écran, invalidation, IA consultative et sauvegarde minimale — rédigé et audité au niveau `static-review`.'
roadmap_line = '- [x] Clarification du chapitre 17 — intervalles nominaux explicités, codes de retour distingués des erreurs pédagogiques et échéances reportées conservées.'
if roadmap_line not in roadmap:
    roadmap = once(roadmap, roadmap_anchor, roadmap_anchor + '\n' + roadmap_line, 'roadmap insertion')
roadmap_path.write_text(roadmap, encoding='utf-8')

continuity = continuity_path.read_text(encoding='utf-8')
continuity = once(continuity, 'version: "3.17.7"', 'version: "3.17.8"', 'continuity version')
continuity = once(continuity, '- chapitre 17 : version `1.0.0` ;', '- chapitre 17 : version `1.0.1` ;', 'continuity chapter version')
agent_anchor = '- ordonnanceur round-robin limité à `8` décisions par tick physique ;'
agent_add = agent_anchor + '\n- échéance conservée avec `logical_tick >= next_due_tick` lorsqu’un agent est reporté par le budget ;'
if 'échéance conservée avec `logical_tick >= next_due_tick`' not in continuity:
    continuity = once(continuity, agent_anchor, agent_add, 'continuity architecture insertion')
if '### 2026-07-20 — version 3.17.8' not in continuity:
    journal = '''## 27. Journal

### 2026-07-20 — version 3.17.8

- chapitre 17 porté en version `1.0.1` ;
- intervalles `ACTIVE`, `BACKGROUND` et `DORMANT` explicitement reliés à `6`, `60` et `600` ticks ;
- fréquences qualifiées de nominales et dépendantes de la fréquence physique configurée ;
- six libellés ambigus remplacés par valeurs ou codes de retour, refus contrôlé, statuts à distinguer et traitement du résultat ;
- politique de tick corrigée afin de conserver une échéance reportée par le budget ;
- protocole QA porté en version `1.7.2` ;
- aucun PDF construit et aucun test runtime revendiqué.
'''
    continuity = once(continuity, '## 27. Journal\n', journal, 'continuity journal')
continuity_path.write_text(continuity, encoding='utf-8')

# Assertions.
chapter = chapter_path.read_text(encoding='utf-8')
section_37_start = chapter.index('## 37. Erreurs fréquentes et corrections')
section_38_start = chapter.index('## 38. Checklist de réalisation')
outside = chapter[:section_37_start] + chapter[section_38_start:]
ambiguous = re.findall(r'^- \*\*(?:Erreur|Erreurs|Erreur attendue|Erreur fréquente|Retours et erreurs)\s*:', outside, flags=re.M)
if ambiguous:
    raise RuntimeError(f'ambiguous labels remain: {ambiguous}')
if 'return (logical_tick + phase) % interval == 0' in chapter:
    raise RuntimeError('old exact-modulo scheduler remains')
if 'logical_tick >= next_due_tick' not in chapter:
    raise RuntimeError('overdue preservation missing')
if chapter.count('**Pourquoi cet exemple est fautif :**') != 16:
    raise RuntimeError('error examples changed unexpectedly')
if chapter.count('**Pourquoi la correction fonctionne :**') != 16:
    raise RuntimeError('corrections changed unexpectedly')

print('chapter_version=1.0.1')
print('protocol_version=1.7.2')
print('ambiguous_labels_outside_section_37=0')
print('overdue_decisions_preserved=true')
