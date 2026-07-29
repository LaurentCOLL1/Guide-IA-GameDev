from __future__ import annotations

import hashlib
import os
import re
from collections import Counter
from pathlib import Path

ROOT = Path('.')
RUN_ID = os.environ['RUN_ID']
SOURCE_HEAD = os.environ['SOURCE_HEAD']
STAMP = '2026-07-29T15:46:00+02:00'


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding='utf-8')


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding='utf-8')


def replace_once(path: str, old: str, new: str) -> None:
    text = read(path)
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{path}: remplacement attendu une fois, trouvé {count}: {old[:120]!r}')
    write(path, text.replace(old, new, 1))


def regex_once(path: str, pattern: str, replacement: str, flags: int = 0) -> None:
    text = read(path)
    updated, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f'{path}: motif remplacé {count} fois: {pattern!r}')
    write(path, updated)


chapter_path = 'Livre-V/CHAPITRE-19-Reference-audio.md'
chapter = read(chapter_path)
lines = chapter.splitlines()
headings = [line.strip() for line in lines if re.match(r'^#{1,6} ', line)]
duplicates = [title for title, count in Counter(headings).items() if count > 1]
if duplicates:
    raise RuntimeError(f'titres dupliqués: {duplicates}')

metrics = {
    '__LINES__': str(len(lines)),
    '__HEADINGS__': str(len(headings)),
    '__CARDS__': str(chapter.count('<!-- l5:card -->')),
    '__MATRICES__': str(chapter.count('<!-- l5:matrix -->')),
    '__LINKS__': str(len(re.findall(r'\[[^\]]+\]\([^)]+\)', chapter))),
    '__SOURCE_LINKS__': str(len(re.findall(r'\]\(\.\./Livre-(?:I|II|III|IV)/', chapter))),
    '__FRAGMENT_LINKS__': str(len(re.findall(r'\]\(\.\./Livre-(?:I|II|III|IV)/[^)#]+#[^)]+\)', chapter))),
    '__DIAGRAMS__': str(chapter.count('**Diagramme compact :**')),
    '__FENCED_BLOCKS__': str(chapter.count('```') // 2),
}

if metrics['__CARDS__'] != '13':
    raise RuntimeError(f"nombre de cartes inattendu: {metrics['__CARDS__']}")
if metrics['__MATRICES__'] != '3':
    raise RuntimeError(f"nombre de matrices inattendu: {metrics['__MATRICES__']}")
if metrics['__FENCED_BLOCKS__'] != '0':
    raise RuntimeError(f"blocs clôturés inattendus: {metrics['__FENCED_BLOCKS__']}")

replace_once('Livre-V/index.md', 'version: "1.10.0"', 'version: "1.11.0"')
replace_once(
    'Livre-V/index.md',
    '- [ ] Chapitre 19 — Référence audio.',
    '- [x] [Fiche 19 — Référence audio](CHAPITRE-19-Reference-audio.md) — version `1.0.0`, niveau `static-review`.',
)
regex_once(
    'Livre-V/index.md',
    r'Progression : \*\*18 chapitres sur 26\*\*.*',
    'Progression : **19 chapitres sur 26** rédigés et audités. Les fiches 01 à 19 utilisent le profil de référence spécialisé du Livre V ; la fiche 19 rassemble signal, niveaux, formats, cycle de vie, boucles, familles audio, spatialisation, bus, voix, TTS/STT, localisation, accessibilité, budgets contextualisés, preuves et diagnostics. Les fichiers de test, presets exécutables et fixtures permanentes du Companion Pack, le catalogue transversal des erreurs, la licence globale et les formats de publication avancés restent des chantiers distincts.',
)

replace_once(
    'ROADMAP.md',
    '- [x] Référence graphique et 3D — fiche 18 rédigée et auditée au niveau `static-review`.',
    '- [x] Référence graphique et 3D — fiche 18 rédigée et auditée au niveau `static-review`.\n- [x] Référence audio — fiche 19 rédigée et auditée au niveau `static-review`.',
)
replace_once(
    'ROADMAP.md',
    '**Statut M6 : en cours — 18 chapitres rédigés, repérés et audités sur 26.**',
    '**Statut M6 : en cours — 19 chapitres rédigés, repérés et audités sur 26.**',
)

replace_once(
    'contents.txt',
    'Livre-V/CHAPITRE-18-Reference-graphique-et-3D.md\nCompanion-Pack/index.md',
    'Livre-V/CHAPITRE-18-Reference-graphique-et-3D.md\nLivre-V/CHAPITRE-19-Reference-audio.md\nCompanion-Pack/index.md',
)

replace_once('plans/LIVRE-V-PLAN-MAITRE.md', 'version: "1.18.0"', 'version: "1.19.0"')
replace_once(
    'plans/LIVRE-V-PLAN-MAITRE.md',
    '> **Statut :** 18 chapitres sur 26 rédigés et audités au niveau `static-review`',
    '> **Statut :** 19 chapitres sur 26 rédigés et audités au niveau `static-review`',
)
replace_once(
    'plans/LIVRE-V-PLAN-MAITRE.md',
    '## Chapitre 19 — Référence audio\n\n**Objectifs**',
    '## Chapitre 19 — Référence audio\n\n**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n**Objectifs**',
)

replace_once('CONTINUITE-PROJET.md', 'version: "4.05.0"', 'version: "4.06.0"')
replace_once(
    'CONTINUITE-PROJET.md',
    'last-updated: "2026-07-29T13:59:00+02:00"',
    f'last-updated: "{STAMP}"',
)
replace_once(
    'CONTINUITE-PROJET.md',
    '- progression du Livre V : 18 chapitres sur 26 ;',
    '- progression du Livre V : 19 chapitres sur 26 ;',
)
replace_once(
    'CONTINUITE-PROJET.md',
    '- chapitre 18 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;',
    '- chapitre 18 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- chapitre 19 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;',
)

continuity = read('CONTINUITE-PROJET.md')
next_section = '''## 26. Prochaine action

Le Livre V contient dix-neuf fiches sur 26 au niveau `static-review`. La fiche 19 fournit une référence non linéaire pour signal, fréquence, profondeur, canaux, niveaux, loudness, formats, cycle de vie, boucles, variantes, spatialisation, bus, voix, TTS/STT, localisation, accessibilité, budgets contextualisés, niveaux de preuve et diagnostics audio. Les fichiers de test, presets exécutables et fixtures permanentes du Companion Pack, le catalogue transversal des erreurs, les campagnes de mesure, les approbations artistiques et juridiques, la licence globale et le balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 20 classera les erreurs par outil, symptôme, message, cause et version, puis fournira des arbres de diagnostic progressifs. Il devra distinguer cause confirmée, hypothèse et contournement, renvoyer aux corrections propriétaires et ne pas promettre qu’un message possède une cause unique.
'''
updated, count = re.subn(
    r'## 26\. Prochaine action\n.*?(?=## 27\. Journal)',
    next_section,
    continuity,
    count=1,
    flags=re.DOTALL,
)
if count != 1:
    raise RuntimeError(f'CONTINUITE-PROJET.md: section prochaine action remplacée {count} fois')
continuity = updated

journal_entry = f'''### {STAMP} — version 4.06.0

- création de la fiche 19 — Référence audio ;
- ajout de treize cartes, de trois matrices et de {metrics['__DIAGRAMS__']} diagrammes compacts ;
- signal, niveaux, formats, cycle de vie, boucles, familles, spatialisation, bus, voix, TTS/STT, localisation, accessibilité, budgets, preuves et diagnostics audio indexés ;
- frontières avec la fiche 07, les chapitres 9 du Livre I, 5, 26 à 29 du Livre III et 18 à 19 du Livre IV maintenues sans duplication ;
- validations documentaires légères sans PDF réussies dans le run `{RUN_ID}` ;
- métriques statiques : {metrics['__LINES__']} lignes, {metrics['__HEADINGS__']} titres, {metrics['__CARDS__']} fiches, {metrics['__MATRICES__']} matrices, {metrics['__LINKS__']} liens, {metrics['__SOURCE_LINKS__']} renvois vers les Livres I à IV, {metrics['__FRAGMENT_LINKS__']} liens profonds et {metrics['__DIAGRAMS__']} diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 20 — Catalogue des erreurs et diagnostics, niveau Élevée ;
- aucun outil audio, TTS, STT, fichier, encodage, écoute, import, bus, effet, boucle, mesure, donnée vocale, approbation juridique ou PDF produit.


'''
marker = '## 27. Journal\n\n'
if marker not in continuity:
    raise RuntimeError('CONTINUITE-PROJET.md: marqueur de journal absent')
continuity = continuity.replace(marker, marker + journal_entry, 1)
write('CONTINUITE-PROJET.md', continuity)

chapter_sha = hashlib.sha256((ROOT / chapter_path).read_bytes()).hexdigest()
audit_path = 'Livre-V/QA/AUDIT-CHAPITRE-19.md'
audit = read(audit_path)
replacements = {
    **metrics,
    '__RUN_ID__': RUN_ID,
    '__SOURCE_HEAD__': SOURCE_HEAD,
    '__CHAPTER_SHA__': chapter_sha,
}
for placeholder, value in replacements.items():
    if placeholder not in audit:
        raise RuntimeError(f'{audit_path}: placeholder absent {placeholder}')
    audit = audit.replace(placeholder, value)
write(audit_path, audit)
audit_sha = hashlib.sha256((ROOT / audit_path).read_bytes()).hexdigest()

proof_path = 'Livre-V/QA/VALIDATION-FINALE-CHAPITRE-19.yaml'
proof = read(proof_path)
replacements = {
    **metrics,
    '__RUN_ID__': RUN_ID,
    '__SOURCE_HEAD__': SOURCE_HEAD,
    '__CHAPTER_SHA__': chapter_sha,
    '__AUDIT_SHA__': audit_sha,
}
for placeholder, value in replacements.items():
    if placeholder not in proof:
        raise RuntimeError(f'{proof_path}: placeholder absent {placeholder}')
    proof = proof.replace(placeholder, value)
write(proof_path, proof)

print(f'chapter_sha256={chapter_sha}')
print(f'audit_sha256={audit_sha}')
print(f'metrics={metrics}')
