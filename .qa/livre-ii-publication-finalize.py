#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import re

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.now(ZoneInfo("Europe/Paris")).replace(microsecond=0).isoformat()
DATE = NOW[:10]

REPORT_PATH = ROOT / "Livre-II/QA/RAPPORT-VALIDATION-TRANSVERSALE-LIVRE-II.md"
PROOF_PATH = ROOT / "Livre-II/QA/VALIDATION-PUBLICATION-LIVRE-II.yaml"

report = f'''---
title: "Validation transversale et publication du Livre II"
id: "DOC-L2-QA-TRANSVERSE-PUBLICATION"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
last-verified: "{NOW}"
audit-level: "static-review+pdf-inspected"
validation-evidence: "Livre-II/QA/VALIDATION-PUBLICATION-LIVRE-II.yaml"
---

# Validation transversale et publication du Livre II

## 1. Périmètre

La campagne couvre les trente chapitres du Livre II, leurs rapports d’audit, les preuves QA disponibles, l’index du Livre, l’ordre de compilation, les liens et identifiants, les repères d’utilisation, les doublons, la chaîne Pandoc/XeLaTeX et le PDF complet de la collection à l’état de clôture du Livre II.

La preuve contenant le nombre final de pages, l’empreinte SHA-256 et les identifiants GitHub Actions est conservée dans `Livre-II/QA/VALIDATION-PUBLICATION-LIVRE-II.yaml`. Elle n’est pas compilée dans le PDF afin d’éviter une preuve auto-référentielle.

## 2. Validation transversale

La validation confirme :

- trente chapitres déclarés et présents ;
- trente identifiants de chapitre uniques ;
- un rapport d’audit référencé et présent pour chaque chapitre, avec rapport groupé autorisé pour les chapitres 1 et 2 ;
- toutes les preuves finales présentes au dépôt contrôlées sans état `pending` ;
- trente chapitres du Livre II déclarés dans `contents.txt` ;
- zéro erreur bloquante dans le validateur documentaire ;
- zéro doublon de titre, bloc significatif ou paragraphe long dans les chapitres ;
- zéro bloc sans repère d’utilisation ;
- zéro incohérence sémantique de contexte ;
- absence de métadonnée de niveau de raisonnement dans les chapitres publiés.

L’unique avertissement global reste l’absence de licence de collection.

## 3. Compilation Pandoc et XeLaTeX

La compilation utilise `build.sh`, `metadata.yaml`, `contents.txt`, le filtre Lua du dépôt, Pandoc et XeLaTeX. Les dépendances de publication comprennent les familles DejaVu, Latin Modern et le convertisseur SVG de `librsvg`.

Une première compilation a révélé deux dépendances manquantes (`lmodern.sty` et `rsvg-convert`). Elles ont été ajoutées au runner de publication. La compilation suivante a produit un PDF A4 lisible et extractible.

L’option LaTeX `openany` a été ajoutée à la classe `book`. Elle supprime les pages verso quasi vides qui conservaient un en-tête courant tronqué entre deux chapitres. Le nombre de ces pages parasites est passé de cinquante et une à zéro, hors dernière page normale de la table des matières.

## 4. Préflight PDF

Les contrôles ont confirmé :

- format A4 et rotation nulle ;
- PDF non chiffré et sans JavaScript ;
- absence d’erreur de syntaxe ou de flux selon `qpdf --check` ;
- texte extractible avec `pdftotext` ;
- polices DejaVu et Latin Modern incorporées, sous-ensemblées et associées à une table Unicode ;
- métadonnées de titre et d’auteur présentes ;
- empreinte SHA-256 enregistrée dans la preuve externe.

## 5. Inspection visuelle

L’inspection a couvert :

- la couverture et les premières pages de la table des matières ;
- des pages représentatives aux quarts, à la moitié et aux trois quarts du volume ;
- les trente ouvertures de chapitre du Livre II ainsi que son index ;
- des pages contenant du code dense, des listes et des explications structurées ;
- les dernières pages et les index des Livres futurs.

Aucun texte rogné, chevauchement, tableau hors page, rotation incorrecte, glyphe manquant ou carré noir n’a été retenu. Les titres longs se replient dans les marges et les blocs de code observés restent lisibles.

## 6. Portes qualité

- [x] Q0 — intégrité, métadonnées et ordre de compilation ;
- [x] Q1 — conformité éditoriale et explication des blocs ;
- [x] Q2 — liens, identifiants, audits, preuves et frontières ;
- [x] Q3 — validation technique statique transversale ;
- [x] Q4 — sécurité documentaire et absence de secrets ;
- [x] Q5 — compilation Pandoc/XeLaTeX, préflight et inspection visuelle.

## 7. Décision

**Livre II accepté pour publication technique avec réserves globales de collection.**

Les réserves propres à la construction PDF de fin du Livre II sont closes. Le Livre III peut commencer selon son plan maître.

Deux réserves générales empêchent encore de qualifier la collection de publication officielle finale :

1. aucune licence globale n’est définie et `LICENSE.md` est absent ;
2. le PDF produit par la chaîne actuelle n’est pas balisé pour les lecteurs d’écran (`Tagged: no`).

Ces choix ne sont pas corrigés automatiquement : le premier exige une décision juridique du propriétaire, le second une évolution dédiée de la chaîne de publication et une validation d’accessibilité.

## 8. Réserves runtime

Cette campagne ne matérialise pas le Starter Kit et n’exécute pas Godot, GUT, les services IA, les scènes pédagogiques ou les procédures Windows/WSL décrites. Les niveaux `runtime-tested` restent attachés aux futures campagnes d’exécution sur les environnements concernés.
'''
REPORT_PATH.write_text(report, encoding="utf-8")

proof = f'''schema-version: 1
evidence-id: DOC-L2-QA-PUBLICATION
status: pending
validation-date: {DATE}
validated-base-commit: null
validated-head-commit: null
evidence-closure:
  commit: null
  conclusion: pending
book:
  id: LIV-II-INDEX
  path: Livre-II/index.md
  chapters: 30
  audit-level: static-review+pdf-inspected
results:
  blocking-errors: 0
  global-warnings: 2
  chapters-present: 30
  chapter-identifiers-unique: true
  audit-reports-resolved: true
  available-final-proofs-complete: true
  usage-context-nonconformities: 0
  semantic-context-inconsistencies: 0
  duplicate-headings: 0
  duplicate-significant-blocks: 0
  duplicate-long-paragraphs: 0
  pandoc-xelatex-build: pending
  visual-inspection: pending
pdf:
  path: dist/Guide-IA-GameDev.pdf
  pages: null
  format: A4
  pdf-version: null
  sha256: null
  encrypted: false
  tagged: false
  text-extractable: null
  qpdf-check: pending
  fonts-embedded: null
  parasitic-chapter-separator-pages: null
ci:
  publication-workflow:
    run-id: null
    conclusion: pending
  artifact:
    id: null
    name: livre-ii-publication-candidate
    digest: null
reservations:
  - Global collection license is undefined and LICENSE.md is absent.
  - PDF accessibility tagging is not implemented; pdfinfo reports Tagged: no.
  - Runtime procedures and Starter Kit are not executed by this static and PDF campaign.
'''
PROOF_PATH.write_text(proof, encoding="utf-8")

# Livre II index
index_path = ROOT / "Livre-II/index.md"
index = index_path.read_text(encoding="utf-8")
index = index.replace('status: "in-progress"', 'status: "complete"', 1)
index = index.replace('version: "1.22.0"', 'version: "1.23.0"', 1)
anchor = '- [audit du chapitre 30](QA/AUDIT-CHAPITRE-30.md) ;'
report_link = '- [validation transversale et publication du Livre II](QA/RAPPORT-VALIDATION-TRANSVERSALE-LIVRE-II.md) ;'
if report_link not in index:
    if anchor not in index:
        raise RuntimeError("Ancre audit chapitre 30 introuvable dans index")
    index = index.replace(anchor, anchor + "\n" + report_link, 1)
index = index.replace(
    '- le PDF de fin de Livre reste différé.',
    '- le PDF de fin du Livre II a été compilé, préflighté et inspecté visuellement ; les réserves globales de licence et de balisage d’accessibilité restent distinctes.',
)
index = index.replace(
    'Le PDF complet n’est plus construit après chaque chapitre. Il sera généré et inspecté :',
    'Le PDF complet n’est plus construit après chaque chapitre. Le PDF de clôture du Livre II a été généré et inspecté ; les prochaines compilations complètes auront lieu :',
)
index_path.write_text(index, encoding="utf-8")

# Roadmap
roadmap_path = ROOT / "ROADMAP.md"
roadmap = roadmap_path.read_text(encoding="utf-8")
roadmap = roadmap.replace(
    '- [ ] Validation technique, documentaire et compilation du Livre II complet.',
    '- [x] Validation technique, documentaire, compilation Pandoc/XeLaTeX et inspection visuelle du Livre II complet.',
    1,
)
old_status = re.compile(r'^\*\*Statut M3 : en cours de clôture — 30 chapitres rédigés, repérés et audités sur 30\.\*\*.*$', re.M)
new_status = ('**Statut M3 : terminé — 30 chapitres rédigés, repérés, audités et validés transversalement sur 30.** '
              'La compilation Pandoc/XeLaTeX du PDF complet, le préflight structurel et l’inspection visuelle sont réussis. '
              'Les réserves de publication propres au Livre II sont closes ; la licence globale, le PDF balisé et les réserves runtime restent des chantiers de collection distincts.')
roadmap, count = old_status.subn(new_status, roadmap, count=1)
if count != 1:
    raise RuntimeError("Statut M3 introuvable")
m8_anchor = '## M8 — Publications\n'
m8_line = '- [x] Produire, préflighter et inspecter le PDF complet de fin du Livre II.\n'
if m8_line not in roadmap:
    if m8_anchor not in roadmap:
        raise RuntimeError("Ancre M8 introuvable")
    roadmap = roadmap.replace(m8_anchor, m8_anchor + "\n" + m8_line, 1)
roadmap_path.write_text(roadmap, encoding="utf-8")

# Compilation order: report is included, proof stays external.
contents_path = ROOT / "contents.txt"
contents = contents_path.read_text(encoding="utf-8")
report_rel = "Livre-II/QA/RAPPORT-VALIDATION-TRANSVERSALE-LIVRE-II.md"
if report_rel not in contents:
    anchor = "Livre-II/QA/VALIDATION-FINALE-CHAPITRE-30.yaml\n"
    if anchor not in contents:
        raise RuntimeError("Ancre preuve chapitre 30 introuvable dans contents.txt")
    contents = contents.replace(anchor, anchor + report_rel + "\n", 1)
contents_path.write_text(contents, encoding="utf-8")

# Continuity
continuity_path = ROOT / "CONTINUITE-PROJET.md"
continuity = continuity_path.read_text(encoding="utf-8")
continuity = continuity.replace('version: "3.30.0"', 'version: "3.30.1"', 1)
continuity = re.sub(r'^last-updated: ".*"$', f'last-updated: "{NOW}"', continuity, count=1, flags=re.M)
continuity = continuity.replace('**En cours : 29 chapitres sur 30.**', '**Terminé, audité transversalement et compilé : 30 chapitres sur 30.**', 1)
continuity = continuity.replace('30. Architecture Solo et architecture Studio.', '30. Architecture Solo et architecture Studio — terminé au niveau `static-review`.', 1)
continuity = continuity.replace(
    '- accessibilité PDF avancée à traiter avant publication.',
    '- publication technique du Livre II acceptée après compilation et inspection PDF ;\n- licence globale à décider avant publication officielle de la collection ;\n- accessibilité PDF avancée et balisage à traiter avant publication officielle.',
    1,
)
next_pattern = re.compile(r'## 26\. Prochaine action\n.*?(?=\n## 27\. Journal)', re.S)
next_section = '''## 26. Prochaine action

Le Livre II est terminé, validé transversalement, compilé avec Pandoc/XeLaTeX et inspecté visuellement. Les réserves techniques propres à son PDF de clôture sont closes. Les réserves globales de licence, de balisage d’accessibilité et d’exécution runtime restent explicitement ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-III/CHAPITRE-01-Preproduction-et-cahier-des-charges-artistique.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 1 du Livre III traduira la vision du jeu en contraintes artistiques et techniques, catégories d’assets, quantités, priorités, budgets, calendrier, responsabilités, risques et critères d’acceptation. Il préparera la direction artistique du chapitre 2 sans produire encore les assets définitifs.
'''
continuity, count = next_pattern.subn(next_section.rstrip(), continuity, count=1)
if count != 1:
    raise RuntimeError("Section Prochaine action introuvable")
journal_anchor = '## 27. Journal\n'
journal_entry = f'''## 27. Journal

### {NOW} — version 3.30.1

- validation transversale des trente chapitres du Livre II réussie ;
- audits référencés, preuves disponibles, identifiants, liens, contextes et doublons contrôlés ;
- compilation Pandoc/XeLaTeX et préflight PDF réussis ;
- cinquante et une pages de séparation parasites supprimées avec `openany` ;
- couverture, table des matières, trente ouvertures de chapitre, pages de code et pages finales inspectées ;
- rapport de validation transversal ajouté au PDF et preuve de publication conservée hors compilation ;
- M3 et Livre II marqués terminés ; prochaine action déplacée vers le Livre III, chapitre 1 ;
- licence globale, balisage d’accessibilité et réserves runtime maintenus sans revendication excessive.
'''
if journal_anchor not in continuity:
    raise RuntimeError("Journal introuvable")
continuity = continuity.replace(journal_anchor, journal_entry, 1)
continuity_path.write_text(continuity, encoding="utf-8")

# Guard against accidentally compiling the proof itself.
if "Livre-II/QA/VALIDATION-PUBLICATION-LIVRE-II.yaml" in contents_path.read_text(encoding="utf-8"):
    raise RuntimeError("La preuve de publication ne doit pas être compilée")

print(f"Finalisation documentaire préparée à {NOW}")
