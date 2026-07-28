#!/usr/bin/env python3
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "Livre-V/CHAPITRE-12-Reference-Python.md"
AUDIT = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-12.md"
PROOF = ROOT / "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-12.yaml"
STAMP = "2026-07-28T22:48:26+02:00"
DATE = "2026-07-28"


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: remplacement attendu une fois, trouvé {count}: {old[:80]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


chapter = CHAPTER.read_text(encoding="utf-8")
lines = len(chapter.splitlines())
headings = len(re.findall(r"^#{1,6}\s", chapter, flags=re.MULTILINE))
cards = chapter.count("<!-- l5:card -->")
matrices = chapter.count("<!-- l5:matrix -->")
links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", chapter)
source_links = [
    target for target in links
    if any(f"../Livre-{roman}/" in target for roman in ("I", "II", "III", "IV"))
]
fragment_links = [target for target in source_links if "#" in target]
official_links = [target for target in links if target.startswith("https://")]
fenced_blocks = len(re.findall(r"^```", chapter, flags=re.MULTILINE)) // 2

expected = {
    "lines": 403,
    "headings": 18,
    "cards": 13,
    "matrices": 3,
    "links": 60,
    "source_links": 21,
    "fragment_links": 21,
    "official_links": 19,
    "fenced_blocks": 0,
}
actual = {
    "lines": lines,
    "headings": headings,
    "cards": cards,
    "matrices": matrices,
    "links": len(links),
    "source_links": len(source_links),
    "fragment_links": len(fragment_links),
    "official_links": len(official_links),
    "fenced_blocks": fenced_blocks,
}
if actual != expected:
    raise RuntimeError(f"Métriques inattendues: {actual!r} != {expected!r}")

audit = f'''---
title: "Audit — Livre V, Fiche 12 : Référence Python"
id: "DOC-L5-QA-AUDIT-CH12"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 12
last-verified: "{STAMP}"
audit-level: "static-review"
validation-authority: "livre-v-reference-profile"
---

# Audit — Fiche 12 : Référence Python

## 1. Décision

La fiche est conforme au profil spécialisé du Livre V au niveau `static-review`. Elle fournit une référence non linéaire de Python pour l’automatisation du guide sans devenir un cours général, sans matérialiser un paquet et sans revendiquer d’exécution.

## 2. Périmètre contrôlé

| Domaine | Couverture | Propriétaire conservé |
|---|---|---|
| interpréteur et environnements | CPython, exécutable, `venv`, `uv`, caches et matrice | Livre I, chapitre 4 |
| valeurs et typage | types intégrés, annotations, unions et garde runtime | documentation Python et outils de typage futurs |
| collections et modèles | séquences, associations, ensembles, dataclasses et protocoles | Livre II, chapitre 29 pour les manifestes |
| flux et erreurs | retours, exceptions, context managers et reprise | contrat de la couche applicative |
| fonctions et itération | paramètres, callables, générateurs et async | référence Python |
| modules et imports | modules, paquets, garde principale et ressources | architecture d’automatisation du Livre II |
| fichiers et sérialisation | `Path`, encodage, staging, JSON, archives et empreintes | chapitre 13 pour les formats |
| CLI et processus | `argparse`, codes, stdout, stderr et `subprocess` | Livre II, chapitre 29 et fiche 10 |
| tests | cas, fixtures, oracles, déterminisme et instabilité | Livre II, chapitre 27 |
| dépendances | `pyproject.toml`, groupes, verrou, index et SBOM | Livre I, chapitre 4 |
| packaging | sdist, wheel, build isolé et points d’entrée | spécifications PyPA |
| correspondances GDScript | notions comparables et différences d’autorité | fiche 11 |
| sécurité et acceptation | données non fiables, archives, processus et portes | Livre IV et Companion Pack futur |

## 3. Conformité Livre V

- `document-format: "reference-cards"` présent ;
- treize marqueurs `l5:card` et trois marqueurs `l5:matrix` ;
- index express placé avant les cartes ;
- tables utilisées avant les paragraphes explicatifs ;
- paragraphes courts et consultation non linéaire ;
- absence de résultats d’apprentissage et de démonstration linéaire ;
- absence de synthèse `Project Asteria` importée du profil tutoriel ;
- aucun bloc de code clôturé ;
- renvois fréquents vers les sources propriétaires ;
- niveau de preuve visible lorsque l’exécution pourrait être supposée.

## 4. Couverture du plan maître

| Exigence du chapitre 12 | Réponse |
|---|---|
| environnements | PY-01 |
| types | PY-02 et PY-03 |
| fonctions | PY-05 |
| fichiers | PY-07 |
| CLI | PY-08 |
| tests | PY-09 |
| automatisation et outils du guide | PY-00, Matrice A et PY-08 |
| dépendances | PY-10 |
| packaging | PY-11 |
| correspondances GDScript | Matrice C |
| aide-mémoire | index, cartes et matrices |
| recettes | formes inline et renvoi vers la fiche 10 |
| conventions | contrats visibles dans chaque table |
| validation future | PY-12 et Companion Pack |

## 5. Frontières

- le cours d’installation et d’environnement reste au Livre I, chapitre 4 ;
- les chaînes d’automatisation complètes restent au Livre II, chapitre 29 ;
- les recettes exécutables restent à la fiche 10 ;
- la syntaxe GDScript reste à la fiche 11 ;
- les formats et schémas restent au chapitre 13 ;
- les campagnes exécutées et benchmarks restent au chapitre 21 ;
- la compatibilité transversale reste au chapitre 22 ;
- les licences et conformités restent au chapitre 25 ;
- les modules, tests et distributions permanents restent au Companion Pack.

## 6. Exactitude technique statique

Les versions CPython `3.14.6` et `3.13.14` correspondent aux cibles enregistrées dans le dépôt. Les documentations Python 3.14 et PyPA ont été revues le 28 juillet 2026 pour `venv`, `typing`, `pathlib`, `argparse`, `subprocess`, `unittest`, `pyproject.toml`, groupes de dépendances, métadonnées, points d’entrée et distributions sources.

La fiche distingue correctement :

- langage, implémentation, interpréteur et environnement ;
- module importé et distribution installée ;
- annotation statique et validation runtime ;
- dépendance directe, transitive, verrou et preuve de compatibilité ;
- arbre source, sdist, wheel et installation éditable ;
- exception interne et code de sortie de processus ;
- checksum, provenance, signature et innocuité ;
- ressemblance syntaxique et autorité architecturale.

## 7. Métriques

| Mesure | Valeur |
|---|---:|
| lignes | {lines} |
| titres | {headings} |
| cartes | {cards} |
| matrices | {matrices} |
| liens Markdown | {len(links)} |
| renvois vers les Livres I à IV | {len(source_links)} |
| liens profonds propriétaires | {len(fragment_links)} |
| liens officiels | {len(official_links)} |
| blocs clôturés | {fenced_blocks} |

## 8. Contrôles et réserves

- structure, métadonnées, liens locaux et doublons : soumis au validateur permanent ;
- marqueurs et fragments du Livre V : soumis au validateur spécialisé ;
- repères de contexte : aucun bloc procédural n’impose de légende ;
- PDF : interdit pour cette validation légère ;
- aucun interpréteur Python téléchargé ou lancé ;
- aucun module compilé, importé ou exécuté ;
- aucun test runner, analyseur de types, linter ou scanner lancé ;
- aucun environnement virtuel créé ou synchronisé ;
- aucune dépendance installée ou verrouillée ;
- aucun processus natif appelé ;
- aucun fichier, archive ou donnée non fiable traité ;
- aucune sdist, wheel ou commande installable construite ;
- aucune matrice Windows, WSL/Linux, Solo ou Studio exécutée ;
- aucune compatibilité de backend IA ou GPU qualifiée ;
- aucun fichier permanent du Companion Pack matérialisé ;
- aucune approbation juridique organisationnelle réalisée.

## 9. Décision finale

Accepté au niveau `static-review` après réussite des validations légères et enregistrement de la preuve QA. Les statuts `syntax-checked`, `tested`, `qualified` et `published` restent interdits sans campagne exécutée.
'''
AUDIT.write_text(audit, encoding="utf-8")
chapter_hash = sha256(CHAPTER.read_bytes()).hexdigest()
audit_hash = sha256(AUDIT.read_bytes()).hexdigest()

proof = f'''schema-version: 2
evidence-id: DOC-L5-QA-EVIDENCE-CH12
validation-authority: livre-v-reference-profile
status: complete
validation-date: '{DATE}'
validated-base-commit: 0b1dde0756fbaa4f2f21f2939c11d8658db191d5
source-branch: docs/livre-v-ch12-reference-python
chapter:
  id: DOC-L5-CH12
  path: Livre-V/CHAPITRE-12-Reference-Python.md
  version: 1.0.0
  document-format: reference-cards
  audit-level: static-review
results:
  blocking-errors: 0
  warnings: 13
  chapter-lines: {lines}
  chapter-headings: {headings}
  reference-cards: {cards}
  matrices: {matrices}
  internal-links: {len(links)}
  source-book-links: {len(source_links)}
  fragment-links: {len(fragment_links)}
  official-links: {len(official_links)}
  fenced-blocks: {fenced_blocks}
  reference-python-primary: CPython-3.14.6
  reference-python-fallback: CPython-3.13.14
  environments-covered: true
  values-and-typing-covered: true
  collections-covered: true
  control-flow-covered: true
  functions-and-iteration-covered: true
  modules-and-imports-covered: true
  files-and-serialization-covered: true
  cli-and-processes-covered: true
  tests-and-determinism-covered: true
  dependencies-and-locking-covered: true
  packaging-covered: true
  python-gdscript-matrix-present: true
  security-and-acceptance-covered: true
  runtime-results-invented: false
  tutorial-boundary-preserved: true
  companion-pack-boundary-preserved: true
  master-plan-scope-covered: true
  pdf-produced: false
  runtime-executed: false
integrity:
  chapter-sha256: {chapter_hash}
  audit-sha256: {audit_hash}
ci:
  permanent-validations:
    status: pending-recording-after-pr-run
reservations:
- No Python interpreter was downloaded or launched.
- No Python module was compiled, imported or executed.
- No virtual environment was created, activated or synchronized.
- No dependency was installed, resolved, locked or scanned.
- No test runner, type checker, linter or coverage tool was executed.
- No CLI, native process, timeout or cancellation path was exercised.
- No file, archive, JSON payload or untrusted input was processed.
- No source distribution, wheel or installed entry point was built.
- No Windows, WSL/Linux, Solo or Studio compatibility matrix was executed.
- No AI backend, GPU library or native wheel compatibility was qualified.
- No permanent Companion Pack module, test or distribution was materialized.
- No organisational legal approval was performed.
- No PDF was produced; collection licence and advanced accessibility tagging remain open.
'''
PROOF.write_text(proof, encoding="utf-8")

index = ROOT / "Livre-V/index.md"
replace_once(index, 'version: "1.3.0"', 'version: "1.4.0"')
replace_once(index, "- [ ] Chapitre 12 — Référence Python.", "- [x] [Fiche 12 — Référence Python](CHAPITRE-12-Reference-Python.md) — version `1.0.0`, niveau `static-review`.")
replace_once(index, "Progression : **11 chapitres sur 26** rédigés et audités. Les fiches 01 à 11 utilisent le profil de référence spécialisé du Livre V ; la fiche 11 fournit une référence GDScript non linéaire pour Godot 4.7.1, avec syntaxe, types, opérateurs, fonctions, classes, annotations, collections et diagnostics. Les parses et exécutions runtime, fichiers du Companion Pack, benchmarks, licence globale et formats de publication avancés restent des chantiers distincts.", "Progression : **12 chapitres sur 26** rédigés et audités. Les fiches 01 à 12 utilisent le profil de référence spécialisé du Livre V ; la fiche 12 fournit une référence Python non linéaire pour l’automatisation, avec environnements, types, fonctions, fichiers, CLI, tests, dépendances, packaging et correspondances GDScript. Les exécutions runtime, fichiers du Companion Pack, benchmarks, licence globale et formats de publication avancés restent des chantiers distincts.")

roadmap = ROOT / "ROADMAP.md"
replace_once(roadmap, "- [x] Référence GDScript — fiche 11 rédigée et auditée au niveau `static-review`.", "- [x] Référence GDScript — fiche 11 rédigée et auditée au niveau `static-review`.\n- [x] Référence Python — fiche 12 rédigée et auditée au niveau `static-review`.")
replace_once(roadmap, "**Statut M6 : en cours — 11 chapitres rédigés, repérés et audités sur 26.**", "**Statut M6 : en cours — 12 chapitres rédigés, repérés et audités sur 26.**")

contents = ROOT / "contents.txt"
replace_once(contents, "Livre-V/CHAPITRE-11-Reference-GDScript.md\nCompanion-Pack/index.md", "Livre-V/CHAPITRE-11-Reference-GDScript.md\nLivre-V/CHAPITRE-12-Reference-Python.md\nCompanion-Pack/index.md")

plan = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
replace_once(plan, 'version: "1.11.0"', 'version: "1.12.0"')
replace_once(plan, "> **Statut :** 11 chapitres sur 26 rédigés et audités au niveau `static-review`", "> **Statut :** 12 chapitres sur 26 rédigés et audités au niveau `static-review`")
replace_once(plan, "## Chapitre 12 — Référence Python\n\n**Objectifs**", "## Chapitre 12 — Référence Python\n\n**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n**Objectifs**")

continuity = ROOT / "CONTINUITE-PROJET.md"
replace_once(continuity, 'version: "3.98.0"', 'version: "3.99.0"')
replace_once(continuity, 'last-updated: "2026-07-28T22:02:17+02:00"', f'last-updated: "{STAMP}"')
replace_once(continuity, "- progression du Livre V : 11 chapitres sur 26 ;", "- progression du Livre V : 12 chapitres sur 26 ;")
replace_once(continuity, "- chapitre 11 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;", "- chapitre 11 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- chapitre 12 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;")
old_next = '''Le Livre V contient onze fiches sur 26 au niveau `static-review`. La fiche 11 fournit une référence non linéaire de GDScript pour Godot `4.7.1-stable`, avec syntaxe, types, opérateurs, fonctions, classes, annotations, collections, signaux, ressources et diagnostics. Les parses et exécutions réels, migrations, fichiers du Companion Pack, benchmarks, approbations juridiques, la licence globale et le balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-12-Reference-Python.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 12 fournira une référence non linéaire de Python pour l’automatisation du guide : environnements, types, fonctions, fichiers, CLI, tests, dépendances et packaging. Il devra renvoyer aux tutoriels propriétaires, comparer seulement les notions utiles avec GDScript et ne présenter aucun script comme exécuté sans preuve.'''
new_next = '''Le Livre V contient douze fiches sur 26 au niveau `static-review`. La fiche 12 fournit une référence non linéaire de Python pour l’automatisation du guide, avec environnements, types, fonctions, modules, fichiers, CLI, tests, dépendances, packaging, sécurité et correspondances GDScript. Les compilations, imports, tests, builds, fichiers du Companion Pack, benchmarks, approbations juridiques, la licence globale et le balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-13-Structures-JSON-et-formats-d-echange.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 13 fournira des fiches de formats pour JSON, JSONL, CSV, YAML et les formats Godot : encodage, schémas, version, limites, sécurité et structures canoniques. Il devra distinguer format, schéma, sérialisation, transport et stockage, puis renvoyer aux usages propriétaires sans dupliquer leurs tutoriels.'''
replace_once(continuity, old_next, new_next)
journal = f'''### {STAMP} — version 3.99.0

- création de la fiche 12 — Référence Python ;
- ajout de treize cartes et de trois matrices compactes ;
- environnements, types, collections, flux, fonctions, modules, fichiers, CLI, tests, dépendances, packaging et sécurité indexés ;
- matrice Python/GDScript ajoutée sans traduction mécanique ni déplacement d’autorité ;
- documentations officielles CPython `3.14.6`, Python 3.14 et PyPA revues le 28 juillet 2026 ;
- métriques statiques : {lines} lignes, {headings} titres, {cards} fiches, {matrices} matrices, {len(links)} liens, {len(source_links)} renvois vers les Livres I à IV et {len(fragment_links)} liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 13 — Structures JSON et formats d’échange, niveau Élevée ;
- aucun interpréteur, environnement, module, test, dépendance, processus, build, artefact du Companion Pack, approbation juridique ou PDF produit.


'''
replace_once(continuity, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal)

print(actual)
