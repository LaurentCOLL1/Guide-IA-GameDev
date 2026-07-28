#!/usr/bin/env python3
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "Livre-V/CHAPITRE-13-Structures-JSON-et-formats-d-echange.md"
AUDIT = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-13.md"
PROOF = ROOT / "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-13.yaml"
STAMP = "2026-07-28T23:25:14+02:00"
DATE = "2026-07-28"
FIXTURE_CASES = 24


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: remplacement attendu une fois, trouvé {count}: {old[:100]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def yaml_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


chapter = CHAPTER.read_text(encoding="utf-8")
chapter = chapter.replace("\u00ad", "").replace("\u200b", "").replace("\ufeff", "")
CHAPTER.write_text(chapter, encoding="utf-8")

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

if headings != 18:
    raise RuntimeError(f"18 titres attendus, trouvé {headings}")
if cards != 13 or matrices != 3:
    raise RuntimeError(f"13 cartes et 3 matrices attendues, trouvé {cards} / {matrices}")
if len(source_links) < 16 or len(fragment_links) < 14:
    raise RuntimeError(
        f"Densité de sources insuffisante: {len(source_links)} liens, {len(fragment_links)} fragments"
    )
if len(official_links) < 16:
    raise RuntimeError(f"Sources officielles insuffisantes: {len(official_links)}")
if fenced_blocks != 0:
    raise RuntimeError(f"Aucun bloc clôturé attendu, trouvé {fenced_blocks}")
if "reparser" not in chapter:
    raise RuntimeError("La correction typographique reparser est absente")

metrics = {
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

audit = f'''---
title: "Audit — Livre V, Fiche 13 : Structures JSON et formats d’échange"
id: "DOC-L5-QA-AUDIT-CH13"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 13
last-verified: "{STAMP}"
audit-date: "{STAMP}"
audit-level: "static-review"
validation-authority: "livre-v-reference-profile"
---

# Audit — Fiche 13 : Structures JSON et formats d’échange

## 1. Décision

La fiche est conforme au profil spécialisé du Livre V au niveau `static-review`. Elle fournit une référence non linéaire des formats d’échange, complétée par une campagne temporaire de {FIXTURE_CASES} contrôles locaux en mémoire. Aucun convertisseur permanent, fichier Godot ou artefact du Companion Pack n’est matérialisé.

## 2. Périmètre contrôlé

| Domaine | Couverture | Propriétaire conservé |
|---|---|---|
| contrat de format | identité, modèle, syntaxe, encodage, schéma, évolution et preuve | systèmes propriétaires des Livres I à IV |
| couches | métier, modèle, représentation, document, flux, sérialisation, transport et stockage | chapitres 11 et 12 du Livre II pour les transports |
| encodage et média | UTF-8, BOM, fins de ligne, extensions et types média | RFC et registres officiels |
| JSON | profil strict, doublons, nombres finis, ordre et nullabilité | RFC 8259 et codecs propriétaires |
| JSON Schema | dialecte 2020-12, `$schema`, `$id`, types et champs | schémas futurs du Companion Pack |
| versionnement | `format`, `format_version`, métadonnées, payload et migrations | Livre II, chapitre 9 |
| JSONL | une valeur compacte par ligne | Livre II, chapitre 11 |
| JSON Text Sequences | séparateur `0x1E` et `application/json-seq` | RFC 7464 |
| CSV | dialecte, en-tête, types, multiline, `null` et formules | contrats d’import et d’export futurs |
| YAML | profil 1.2.2, document unique, chargeur sûr, tags et aliases | configurations humaines bornées |
| formats Godot | `.tres`, `.res`, `.tscn`, `.scn`, `.escn` et caches | Godot et Livre II, chapitre 7 |
| configurations | `res://`, `user://`, `ConfigFile`, sauvegardes, caches et logs | Livres II, chapitres 7 et 9 |
| conversions | correspondances, pertes, round-trip, staging et rapport | Companion Pack futur |
| canonicalisation | pretty-print, convention interne, JCS, hash et signature | Livre II, chapitre 29 et publication future |
| sécurité | limites, données non fiables, formules, tags, archives et chemins | Livre IV et chapitre 25 du Livre V |

## 3. Conformité Livre V

- `document-format: "reference-cards"` présent ;
- treize marqueurs `l5:card` et trois marqueurs `l5:matrix` ;
- index express avant les cartes ;
- tables de décision avant les paragraphes ;
- paragraphes courts et accès non linéaire ;
- liens profonds vers les tutoriels propriétaires ;
- exemples valides et invalides compacts, sans procédure dupliquée ;
- aucun résultat d’apprentissage ni synthèse `Project Asteria` importé du profil tutoriel ;
- aucun bloc de code clôturé ;
- niveau de preuve et limites visibles.

## 4. Couverture du plan maître

| Exigence | Réponse |
|---|---|
| JSON | FMT-02 à FMT-05 |
| JSONL | FMT-05 |
| CSV | FMT-06 |
| YAML | FMT-07 |
| formats Godot | FMT-08 et FMT-09 |
| encodage | FMT-02 |
| schémas | FMT-04 et Matrice B |
| version | FMT-04 |
| validation | Matrice B et FMT-12 |
| avantages et limites | Matrice A et chaque carte de format |
| sécurité | FMT-06, FMT-07 et FMT-12 |
| structures canoniques | FMT-04 et FMT-10 |
| fiches formats | FMT-03, 05, 06, 07, 08 et 09 |
| exemples valides et invalides | FMT-03, 05, 06 et 07 |
| convertisseurs | contrat FMT-11 ; fichiers permanents réservés au Companion Pack |
| validateurs automatiques | campagne temporaire de {FIXTURE_CASES} cas et portes permanentes |

## 5. Frontières

- les données de conception, Resources, JSON et configurations restent au Livre II, chapitre 7 ;
- les sauvegardes, migrations de documents et slots restent au Livre II, chapitre 9 ;
- le protocole JSONL du processus compagnon reste au Livre II, chapitre 11 ;
- HTTP, WebSocket et enveloppes réseau restent au Livre II, chapitre 12 ;
- les codecs Python et pipelines de conversion restent au Livre II, chapitre 29 et au Companion Pack ;
- SQLite et ses migrations restent au chapitre 14 ;
- les diagnostics transversaux restent au chapitre 20 ;
- les benchmarks restent au chapitre 21 ;
- les compatibilités restent au chapitre 22 ;
- les licences, provenance et conformité restent au chapitre 25.

## 6. Exactitude technique statique

Les références officielles ont été revues le 28 juillet 2026 : RFC 8259, RFC 4180, RFC 7464, RFC 8785, RFC 9512, YAML 1.2.2, JSON Schema 2020-12, Python 3.14, PyYAML, OWASP CSV Injection et Godot `4.7.1-stable`.

La fiche distingue correctement :

- JSONL et JSON Text Sequences ;
- modèle logique, représentation, document, flux, transport et stockage ;
- syntaxe JSON, profil strict, schéma et invariants métier ;
- champ absent et valeur `null` ;
- `format_version`, `schema_version`, `$schema`, `$id` et version du producteur ;
- dialecte CSV et type média `text/csv` ;
- YAML 1.2.2, chargeur sûr et profil de sécurité ;
- formats texte et binaires de Godot ;
- pretty-print, canonicalisation interne et JCS RFC 8785 ;
- empreinte, signature, chiffrement et compression ;
- round-trip par octets, modèle, normalisation ou perte.

## 7. Campagne temporaire de fixtures

La CI installe PyYAML et `jsonschema`, puis exécute `tools/tmp_l5_ch13_validate_formats.py`. Les {FIXTURE_CASES} cas couvrent JSON strict, JSON Schema 2020-12, JSONL, CSV, YAML et canonicalisation. Le rapport `dist/QA-LIVRE-V-CH13-FORMATS.json` conserve versions, résultats et réserves.

Cette campagne ne qualifie pas Godot, les autres bibliothèques de parsing, un convertisseur permanent, une plateforme complète ou des données réelles.

## 8. Métriques

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
| fixtures temporaires | {FIXTURE_CASES} |

## 9. Contrôles et réserves

- structure, métadonnées, liens locaux et doublons : validateur permanent ;
- marqueurs et fragments du Livre V : validateur spécialisé ;
- repères de contexte : aucun bloc procédural dans la fiche ;
- fixtures : chaînes et flux en mémoire seulement ;
- PDF : interdit pour ce lot léger ;
- aucun binaire Godot ou projet Godot chargé ;
- aucune Resource ou scène parsée, importée ou sauvegardée ;
- aucun fichier utilisateur, secret, réseau ou archive traité ;
- aucun convertisseur permanent créé ;
- aucun fichier du Companion Pack matérialisé ;
- aucune matrice inter-parseurs, OS ou architecture exécutée ;
- aucune campagne de performance ou de sécurité offensive ;
- aucune approbation juridique organisationnelle.

## 10. Décision finale

Accepté au niveau `static-review` après réussite des validateurs permanents et des {FIXTURE_CASES} fixtures temporaires. Les formats et convertisseurs réels restent non qualifiés hors de l’environnement et du périmètre enregistrés.
'''
AUDIT.write_text(audit, encoding="utf-8")
chapter_hash = sha256(CHAPTER.read_bytes()).hexdigest()
audit_hash = sha256(AUDIT.read_bytes()).hexdigest()

proof = f'''schema-version: 2
evidence-id: DOC-L5-QA-EVIDENCE-CH13
validation-authority: livre-v-reference-profile
status: complete
validation-date: {yaml_quote(DATE)}
validated-base-commit: cf6416e565aa13ba76a495ca2f08f119e03b4f3a
source-branch: docs/livre-v-ch13-formats-echange
chapter:
  id: DOC-L5-CH13
  path: Livre-V/CHAPITRE-13-Structures-JSON-et-formats-d-echange.md
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
  markdown-links: {len(links)}
  source-book-links: {len(source_links)}
  fragment-links: {len(fragment_links)}
  official-links: {len(official_links)}
  fenced-blocks: {fenced_blocks}
  formats-covered: 7
  json-strict-profile-covered: true
  json-schema-2020-12-covered: true
  jsonl-covered: true
  json-text-sequences-distinguished: true
  csv-dialect-covered: true
  yaml-safe-profile-covered: true
  godot-formats-covered: true
  config-and-runtime-files-covered: true
  conversion-loss-matrix-present: true
  canonicalisation-and-integrity-covered: true
  round-trip-contract-covered: true
  security-and-limits-covered: true
  fixture-tests: {FIXTURE_CASES}
  fixture-runtime-executed: true
  production-runtime-executed: false
  godot-runtime-executed: false
  runtime-results-invented: false
  tutorial-boundary-preserved: true
  companion-pack-boundary-preserved: true
  master-plan-scope-covered: true
  pdf-produced: false
integrity:
  chapter-sha256: {chapter_hash}
  audit-sha256: {audit_hash}
ci:
  specialized-finalizer:
    status: pending-recording-after-pr-run
  permanent-validations:
    status: pending-recording-after-clean-head-run
reservations:
- The runtime evidence is limited to {FIXTURE_CASES} temporary in-memory Python, PyYAML and jsonschema cases.
- No Godot binary or project was loaded.
- No Resource, scene, ConfigFile or Godot import cache was parsed or written.
- No user file, network request, secret, personal data or archive was processed.
- No permanent converter, schema package or Companion Pack fixture was materialized.
- No cross-parser, cross-platform or native-architecture compatibility matrix was executed.
- No benchmark, fuzzing campaign or adversarial security test was executed.
- No production data migration or round-trip was performed.
- No external JSON Schema reference was resolved during the fixtures.
- No organisational legal approval was performed.
- No PDF was produced; collection licence and advanced accessibility tagging remain open.
'''
PROOF.write_text(proof, encoding="utf-8")

index = ROOT / "Livre-V/index.md"
replace_once(index, 'version: "1.4.0"', 'version: "1.5.0"')
replace_once(
    index,
    "- [ ] Chapitre 13 — Structures JSON et formats d’échange.",
    "- [x] [Fiche 13 — Structures JSON et formats d’échange](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md) — version `1.0.0`, niveau `static-review`.",
)
replace_once(
    index,
    "Progression : **12 chapitres sur 26** rédigés et audités. Les fiches 01 à 12 utilisent le profil de référence spécialisé du Livre V ; la fiche 12 fournit une référence Python non linéaire pour l’automatisation, avec environnements, types, fonctions, fichiers, CLI, tests, dépendances, packaging et correspondances GDScript. Les exécutions runtime, fichiers du Companion Pack, benchmarks, licence globale et formats de publication avancés restent des chantiers distincts.",
    "Progression : **13 chapitres sur 26** rédigés et audités. Les fiches 01 à 13 utilisent le profil de référence spécialisé du Livre V ; la fiche 13 distingue JSON, JSONL, JSON Text Sequences, CSV, YAML et formats Godot, avec encodage, schémas, versions, conversions, canonicalisation, sécurité et validation. Les convertisseurs permanents, campagnes inter-parseurs, fichiers du Companion Pack, benchmarks, licence globale et formats de publication avancés restent des chantiers distincts.",
)

roadmap = ROOT / "ROADMAP.md"
replace_once(
    roadmap,
    "- [x] Référence Python — fiche 12 rédigée et auditée au niveau `static-review`.",
    "- [x] Référence Python — fiche 12 rédigée et auditée au niveau `static-review`.\n- [x] Structures JSON et formats d’échange — fiche 13 rédigée et auditée au niveau `static-review`.",
)
replace_once(
    roadmap,
    "**Statut M6 : en cours — 12 chapitres rédigés, repérés et audités sur 26.**",
    "**Statut M6 : en cours — 13 chapitres rédigés, repérés et audités sur 26.**",
)

contents = ROOT / "contents.txt"
replace_once(
    contents,
    "Livre-V/CHAPITRE-12-Reference-Python.md\nCompanion-Pack/index.md",
    "Livre-V/CHAPITRE-12-Reference-Python.md\nLivre-V/CHAPITRE-13-Structures-JSON-et-formats-d-echange.md\nCompanion-Pack/index.md",
)

plan = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
replace_once(plan, 'version: "1.12.0"', 'version: "1.13.0"')
replace_once(
    plan,
    "> **Statut :** 12 chapitres sur 26 rédigés et audités au niveau `static-review`",
    "> **Statut :** 13 chapitres sur 26 rédigés et audités au niveau `static-review`",
)
replace_once(
    plan,
    "## Chapitre 13 — Structures JSON et formats d’échange\n\n**Objectifs**",
    "## Chapitre 13 — Structures JSON et formats d’échange\n\n**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n**Objectifs**",
)

continuity = ROOT / "CONTINUITE-PROJET.md"
replace_once(continuity, 'version: "3.99.0"', 'version: "4.00.0"')
replace_once(
    continuity,
    'last-updated: "2026-07-28T22:48:26+02:00"',
    f'last-updated: "{STAMP}"',
)
replace_once(
    continuity,
    "- progression du Livre V : 12 chapitres sur 26 ;",
    "- progression du Livre V : 13 chapitres sur 26 ;",
)
replace_once(
    continuity,
    "- chapitre 12 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;",
    "- chapitre 12 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- chapitre 13 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;",
)
old_next = '''Le Livre V contient douze fiches sur 26 au niveau `static-review`. La fiche 12 fournit une référence non linéaire de Python pour l’automatisation du guide, avec environnements, types, fonctions, modules, fichiers, CLI, tests, dépendances, packaging, sécurité et correspondances GDScript. Les compilations, imports, tests, builds, fichiers du Companion Pack, benchmarks, approbations juridiques, la licence globale et le balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-13-Structures-JSON-et-formats-d-echange.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 13 fournira des fiches de formats pour JSON, JSONL, CSV, YAML et les formats Godot : encodage, schémas, version, limites, sécurité et structures canoniques. Il devra distinguer format, schéma, sérialisation, transport et stockage, puis renvoyer aux usages propriétaires sans dupliquer leurs tutoriels.'''
new_next = '''Le Livre V contient treize fiches sur 26 au niveau `static-review`. La fiche 13 fournit des contrats non linéaires pour JSON, JSONL, JSON Text Sequences, CSV, YAML et les formats Godot, avec encodage, schémas, versions, conversions, canonicalisation, sécurité et validation. Les convertisseurs permanents, matrices inter-parseurs, fichiers du Companion Pack, benchmarks, approbations juridiques, la licence globale et le balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-14-Schemas-SQLite-et-migrations.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 14 cataloguera types SQLite, affinités, clés, contraintes, index, transactions et migrations. Il devra distinguer schéma logique, DDL, migration, transaction, sauvegarde et restauration, fournir des modèles compacts et renvoyer au chapitre 8 du Livre II sans reprendre son tutoriel d’intégration.'''
replace_once(continuity, old_next, new_next)
journal = f'''### {STAMP} — version 4.00.0

- création de la fiche 13 — Structures JSON et formats d’échange ;
- ajout de treize cartes et de trois matrices compactes ;
- JSON, JSONL, JSON Text Sequences, CSV, YAML, Resources, scènes et configurations Godot distingués ;
- format, schéma, sérialisation, transport, stockage, conversion, round-trip, canonicalisation et intégrité séparés ;
- profils stricts, encodages, types média, versions, limites et risques documentés ;
- documentations officielles RFC, YAML, JSON Schema, Python, PyYAML, OWASP et Godot `4.7.1-stable` revues le 28 juillet 2026 ;
- campagne temporaire de {FIXTURE_CASES} fixtures locales en mémoire prévue comme porte avant commit ;
- métriques statiques : {lines} lignes, {headings} titres, {cards} fiches, {matrices} matrices, {len(links)} liens, {len(source_links)} renvois vers les Livres I à IV et {len(fragment_links)} liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 14 — Schémas SQLite et migrations, niveau Élevée ;
- aucun moteur Godot, fichier utilisateur, réseau, secret, archive, convertisseur permanent, artefact du Companion Pack, approbation juridique ou PDF produit.


'''
replace_once(continuity, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal)

print(metrics)
