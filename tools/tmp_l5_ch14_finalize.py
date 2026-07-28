#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "Livre-V/CHAPITRE-14-Schemas-SQLite-et-migrations.md"
AUDIT = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-14.md"
PROOF = ROOT / "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-14.yaml"
FIXTURE_REPORT = ROOT / "dist/QA-LIVRE-V-CH14-SQLITE.json"
STAMP = "2026-07-29T01:06:05+02:00"
DATE = "2026-07-29"
BASE_COMMIT = "dac5c877ee32539ee9874b535d7819b4754e27e1"
BRANCH = "docs/livre-v-ch14-schemas-sqlite-migrations"


def replace_once_or_final(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    count = text.count(old)
    if count != 1:
        raise RuntimeError(
            f"{path}: remplacement attendu une fois, trouvé {count}: {old[:120]!r}"
        )
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def insert_once_or_present(path: Path, marker: str, insertion: str) -> None:
    text = path.read_text(encoding="utf-8")
    if insertion in text:
        return
    count = text.count(marker)
    if count != 1:
        raise RuntimeError(
            f"{path}: marqueur attendu une fois, trouvé {count}: {marker[:120]!r}"
        )
    path.write_text(text.replace(marker, marker + insertion, 1), encoding="utf-8")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def yaml_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


if not FIXTURE_REPORT.is_file():
    raise RuntimeError("Le rapport des fixtures SQLite est absent.")

fixture = json.loads(FIXTURE_REPORT.read_text(encoding="utf-8"))
if fixture.get("total") != 36 or fixture.get("passed") != 36 or fixture.get("failed") != 0:
    raise RuntimeError(f"Campagne SQLite non acceptée : {fixture!r}")

chapter = CHAPTER.read_text(encoding="utf-8")
chapter = chapter.replace("\u00ad", "").replace("\u200b", "").replace("\ufeff", "")
CHAPTER.write_text(chapter, encoding="utf-8")

lines = len(chapter.splitlines())
headings = len(re.findall(r"^#{1,6}\s", chapter, flags=re.MULTILINE))
cards = chapter.count("<!-- l5:card -->")
matrices = chapter.count("<!-- l5:matrix -->")
links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", chapter)
source_links = [
    target
    for target in links
    if any(f"../Livre-{roman}/" in target for roman in ("I", "II", "III", "IV"))
]
fragment_links = [target for target in source_links if "#" in target]
official_links = [target for target in links if target.startswith("https://")]
fenced_blocks = len(re.findall(r"^```", chapter, flags=re.MULTILINE)) // 2
sql_blocks = len(re.findall(r"^```sql\s*$", chapter, flags=re.MULTILINE))

if cards != 13 or matrices != 3 or headings != 18:
    raise RuntimeError(
        f"Structure inattendue : headings={headings}, cards={cards}, matrices={matrices}"
    )
if sql_blocks != 3 or fenced_blocks != 3:
    raise RuntimeError(
        f"Blocs inattendus : fenced={fenced_blocks}, sql={sql_blocks}"
    )
if len(source_links) < 12 or len(fragment_links) < 8:
    raise RuntimeError(
        f"Liens propriétaires insuffisants : sources={len(source_links)}, fragments={len(fragment_links)}"
    )

fixture_runtime = str(fixture["sqlite_runtime_version"])
python_version = str(fixture["python_version"])
sqlite_module_version = str(fixture["sqlite_module_version"])
platform = str(fixture["platform"])
compile_options_count = len(fixture.get("compile_options", []))

AUDIT.parent.mkdir(parents=True, exist_ok=True)
audit_text = f'''---
title: "Audit — Livre V, Fiche 14 : Schémas SQLite et migrations"
id: "DOC-L5-QA-AUDIT-CH14"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 14
last-verified: "{STAMP}"
audit-date: "{STAMP}"
audit-level: "static-review"
validation-authority: "livre-v-reference-profile"
---

# Audit — Fiche 14 : Schémas SQLite et migrations

## 1. Décision

La fiche est conforme au profil spécialisé du Livre V au niveau `static-review`. Elle fournit une référence non linéaire des schémas SQLite, transactions, migrations, sauvegardes et diagnostics. Une campagne temporaire de 36 contrôles a créé uniquement des bases synthétiques dans un répertoire isolé.

La référence documentaire est SQLite `3.53.4`, publiée le 24 juillet 2026. La campagne a réellement utilisé SQLite `{fixture_runtime}` via Python `{python_version}` et le module `sqlite3` `{sqlite_module_version}`. Cette différence est conservée : la campagne qualifie les patrons exercés sur son runtime, pas la totalité des comportements de SQLite `3.53.4` ni un binding Godot.

## 2. Périmètre contrôlé

| Domaine | Couverture | Propriétaire conservé |
|---|---|---|
| contrat de base | autorité, identité, moteur, schéma, migration et preuve | systèmes des Livres II et IV |
| identité et version | `application_id`, `user_version`, `schema_version`, options de compilation | adaptateur et manifeste du projet |
| types | affinités, stockage dynamique et tables `STRICT` | codecs et modèles applicatifs |
| clés | clé métier, clé technique, `rowid`, `WITHOUT ROWID`, `AUTOINCREMENT` | domaine propriétaire |
| contraintes | `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `CHECK`, colonnes générées | validation métier complémentaire |
| relations | clés étrangères, actions et temporalité différée | modèle relationnel du Livre II |
| index | simples, composites, partiels, expressions et plans | requêtes et mesures propriétaires |
| connexion | clés étrangères, journal, synchronisation, délai et sécurité | adaptateur SQLite |
| transactions | modes `BEGIN`, rollback et savepoints | unité de travail applicative |
| DDL | trois tables et un index de référence | migrations permanentes du Companion Pack |
| migrations | manifeste, checksum, version, reconstruction et base future | runner du Livre II |
| sauvegarde | copie fermée, Backup API, `VACUUM INTO`, WAL et restauration | Livre IV, chapitre 15 |
| diagnostics | intégrité, relations, schéma, plans et verrous | fiches 20 et 21 |
| sécurité | paramètres, limites, schéma non fiable et extensions | politiques des Livres I et IV |

## 3. Conformité Livre V

- `document-format: "reference-cards"` présent ;
- treize marqueurs `l5:card` et trois marqueurs `l5:matrix` ;
- index express placé avant les cartes ;
- tables de décision avant les paragraphes ;
- consultation non linéaire et paragraphes courts ;
- liens profonds vers les tutoriels propriétaires ;
- trois extraits SQL minimaux, tous précédés du repère `[LECTURE]` ;
- entrées, sorties, effets, paramètres et réserves décrits proportionnellement ;
- aucune procédure Godot, installation d’addon ou scène recopiée ;
- aucun résultat d’apprentissage ni synthèse de tutoriel importé ;
- niveau de preuve et limites visibles.

## 4. Couverture du plan maître

| Exigence | Réponse |
|---|---|
| types | SQL-02 et Matrice B |
| clés | SQL-03 |
| contraintes | SQL-04 et SQL-05 |
| index | SQL-06 |
| transactions | SQL-07 et SQL-08 |
| modèles de migrations | SQL-10 et Matrice C |
| sauvegarde et restauration | SQL-11 |
| schémas de référence | SQL-09 |
| DDL | bloc minimal SQL-09 |
| migrations | bloc minimal SQL-10 |
| diagrammes | relations et dépendances exprimées par matrices compactes |
| requêtes de diagnostic | SQL-12 |
| création et migration d’une base de test | campagne temporaire 36/36 |

## 5. Exactitude technique statique

Les sources officielles SQLite ont été revues le 29 juillet 2026 : chronologie et version `3.53.4`, typage dynamique, tables `STRICT`, clés étrangères, pragmas, transactions, `ALTER TABLE`, Backup API, `VACUUM INTO`, WAL, limites et recommandations de sécurité.

La fiche distingue notamment :

- version documentaire du moteur et version réellement liée par un binding ;
- `application_id`, `user_version` et `schema_version` ;
- classe de stockage, affinité et type `STRICT` ;
- `INTEGER PRIMARY KEY` et autres déclarations de clé ;
- clé technique et identifiant métier ;
- contrainte immédiate et clé étrangère différée ;
- `integrity_check` et `foreign_key_check` ;
- transaction et savepoint ;
- migration, backfill, reconstruction et restauration ;
- copie fermée, Online Backup API et `VACUUM INTO` ;
- WAL et absence de garantie contre `SQLITE_BUSY` ;
- paramètres de valeurs et identifiants SQL dynamiques allowlistés.

## 6. Campagne temporaire SQLite

Le run spécialisé a exécuté 36 cas, tous réussis, sur `{platform}` avec :

- Python `{python_version}` ;
- module `sqlite3` `{sqlite_module_version}` ;
- moteur SQLite `{fixture_runtime}` ;
- {compile_options_count} options de compilation enregistrées ;
- bases créées dans un répertoire temporaire synthétique ;
- aucun fichier utilisateur ou de production.

Les cas couvrent :

- version et options de compilation ;
- `application_id`, `user_version`, `schema_version`, clés étrangères et `trusted_schema` ;
- création de tables `STRICT` et refus de types ou contraintes invalides ;
- clé primaire, orphelin, cascade et contrainte différée ;
- rollback, savepoint et paramètres SQL ;
- migrations 1 et 2, checksums, divergence et refus d’une base future ;
- ajout de colonne et reconstruction de table ;
- présence d’index et utilisation dans un plan ;
- `quick_check`, `integrity_check` et `foreign_key_check` ;
- Backup API, `VACUUM INTO`, WAL et délai d’attente ;
- `WITHOUT ROWID` et identité de famille.

## 7. Corrections issues de la campagne

1. Le premier passage s’est arrêté avant exécution : le garde-fou attendait 36 cas alors que 35 étaient enregistrés. Un contrôle utile sur la séparation `schema_version` / `user_version` a complété la campagne.
2. Le second passage a obtenu 32/36. Les quatre échecs provenaient de `sqlite3.Connection.executescript()`, qui termine implicitement une transaction en cours. Le helper de fixture a été remplacé par des appels `execute()` unitaires, préservant `BEGIN IMMEDIATE ... COMMIT`.
3. Aucun de ces deux problèmes ne contredisait le DDL ou le contrat lecteur ; ils concernaient uniquement le harnais Python temporaire.

## 8. Frontières conservées

- l’intégration Godot-SQLite, l’adaptateur, les dépôts et le bootstrap restent au Livre II, chapitre 8 ;
- les snapshots et migrations de sauvegarde restent au Livre II, chapitre 9 ;
- les bases vectorielles restent à la fiche 15 ;
- la reprise après incident reste au Livre IV, chapitre 15 ;
- les diagnostics transversaux restent à la fiche 20 ;
- les benchmarks et mesures restent à la fiche 21 ;
- les compatibilités restent à la fiche 22 ;
- les licences et conformités restent à la fiche 25 ;
- les fichiers SQL, runners, bases et fixtures permanents restent au Companion Pack.

## 9. Métriques documentaires

| Mesure | Valeur |
|---|---:|
| lignes | {lines} |
| titres | {headings} |
| cartes | {cards} |
| matrices | {matrices} |
| liens Markdown | {len(links)} |
| liens vers Livres I à IV | {len(source_links)} |
| liens profonds propriétaires | {len(fragment_links)} |
| liens officiels | {len(official_links)} |
| blocs clôturés | {fenced_blocks} |
| blocs SQL | {sql_blocks} |
| fixtures SQLite | {fixture['total']} |
| fixtures réussies | {fixture['passed']} |

## 10. Réserves

- aucun binaire Godot, projet, GDExtension ou addon chargé ;
- aucune qualification de Godot-SQLite ou d’un export natif ;
- aucune base utilisateur, de production ou du Companion Pack traitée ;
- aucune concurrence réelle multiprocessus ;
- aucune campagne de charge, fuzzing ou sécurité offensive ;
- aucune migration destructive sur données réelles ;
- aucun test de panne disque, coupure de processus ou corruption injectée ;
- aucun benchmark de taille ou de durée ;
- aucune approbation juridique organisationnelle ;
- aucun PDF produit.

## 11. Acceptation

La fiche est acceptée au niveau `static-review` lorsque le lot permanent, les liens, les cartes, les repères, les empreintes et les validateurs documentaires passent. Les 36 fixtures qualifient uniquement les comportements enregistrés du runtime SQLite `{fixture_runtime}` et du binding Python de la campagne. Un schéma, une migration ou un runner permanent ne devient `qualified` qu’après campagne sur les moteurs, bindings, plateformes et bases sources réellement distribués.
'''
AUDIT.write_text(audit_text, encoding="utf-8")

chapter_hash = digest(CHAPTER)
audit_hash = digest(AUDIT)

proof_text = f'''schema-version: 2
evidence-id: DOC-L5-QA-EVIDENCE-CH14
validation-authority: livre-v-reference-profile
status: complete
validation-date: {yaml_quote(DATE)}
validated-base-commit: {BASE_COMMIT}
source-branch: {BRANCH}
chapter:
  id: DOC-L5-CH14
  path: Livre-V/CHAPITRE-14-Schemas-SQLite-et-migrations.md
  version: 1.0.0
  document-format: reference-cards
  audit-level: static-review
  documentary-sqlite-version: 3.53.4
results:
  blocking-errors: 0
  chapter-lines: {lines}
  chapter-headings: {headings}
  reference-cards: {cards}
  matrices: {matrices}
  markdown-links: {len(links)}
  source-book-links: {len(source_links)}
  fragment-links: {len(fragment_links)}
  official-links: {len(official_links)}
  fenced-blocks: {fenced_blocks}
  sql-blocks: {sql_blocks}
  sqlite-contract-covered: true
  identity-and-version-covered: true
  affinity-and-strict-covered: true
  keys-and-constraints-covered: true
  foreign-keys-covered: true
  indexes-and-plans-covered: true
  transactions-and-savepoints-covered: true
  migrations-and-checksums-covered: true
  backup-and-restore-covered: true
  diagnostics-and-security-covered: true
  fixture-tests: {fixture['total']}
  fixture-tests-passed: {fixture['passed']}
  fixture-tests-failed: {fixture['failed']}
  fixture-python-version: {python_version}
  fixture-sqlite-module-version: {sqlite_module_version}
  fixture-sqlite-runtime-version: {fixture_runtime}
  fixture-compile-options: {compile_options_count}
  fixture-runtime-executed: true
  production-runtime-executed: false
  godot-runtime-executed: false
  addon-runtime-executed: false
  runtime-results-invented: false
  tutorial-boundary-preserved: true
  companion-pack-boundary-preserved: true
  master-plan-scope-covered: true
  pdf-produced: false
integrity:
  chapter-sha256: {chapter_hash}
  audit-sha256: {audit_hash}
ci:
  specialized-sqlite-fixtures:
    status: pending-recording-after-finalizer-run
  permanent-validations:
    status: pending-recording-after-clean-head-run
reservations:
  - Documentary reference SQLite 3.53.4 differs from the executed fixture runtime SQLite {fixture_runtime}.
  - Runtime evidence is limited to 36 synthetic temporary SQLite cases through Python sqlite3.
  - No Godot binary, GDExtension, addon or project was loaded.
  - No user, production, network, secret, personal or Companion Pack data was processed.
  - No real multi-process contention, load, fuzzing or adversarial campaign was executed.
  - No destructive production migration, disk-full or crash-injection campaign was executed.
  - No cross-binding, cross-platform or native export matrix was executed.
  - No organisational legal approval was performed.
  - No PDF was produced; collection licence and advanced accessibility tagging remain open.
'''
PROOF.write_text(proof_text, encoding="utf-8")

# Livre V index
index = ROOT / "Livre-V/index.md"
replace_once_or_final(index, 'version: "1.5.0"', 'version: "1.6.0"')
replace_once_or_final(
    index,
    '- [ ] Chapitre 14 — Schémas SQLite et migrations.',
    '- [x] [Fiche 14 — Schémas SQLite et migrations](CHAPITRE-14-Schemas-SQLite-et-migrations.md) — version `1.0.0`, niveau `static-review`.',
)
replace_once_or_final(
    index,
    'Progression : **13 chapitres sur 26** rédigés et audités. Les fiches 01 à 13 utilisent le profil de référence spécialisé du Livre V ; la fiche 13 distingue JSON, JSONL, JSON Text Sequences, CSV, YAML et formats Godot, avec encodage, schémas, versions, conversions, canonicalisation, sécurité et validation. Les convertisseurs permanents, campagnes inter-parseurs, fichiers du Companion Pack, benchmarks, licence globale et formats de publication avancés restent des chantiers distincts.',
    'Progression : **14 chapitres sur 26** rédigés et audités. Les fiches 01 à 14 utilisent le profil de référence spécialisé du Livre V ; la fiche 14 catalogue schémas SQLite, types, clés, contraintes, index, transactions, migrations, sauvegardes, restaurations et diagnostics. Les bindings Godot, migrations permanentes, bases du Companion Pack, campagnes multiplateformes, benchmarks, licence globale et formats de publication avancés restent des chantiers distincts.',
)

# Roadmap
roadmap = ROOT / "ROADMAP.md"
insert_once_or_present(
    roadmap,
    '- [x] Structures JSON et formats d’échange — fiche 13 rédigée et auditée au niveau `static-review`.\n',
    '- [x] Schémas SQLite et migrations — fiche 14 rédigée et auditée au niveau `static-review`.\n',
)
replace_once_or_final(
    roadmap,
    '**Statut M6 : en cours — 13 chapitres rédigés, repérés et audités sur 26.**',
    '**Statut M6 : en cours — 14 chapitres rédigés, repérés et audités sur 26.**',
)

# Official reading order
contents = ROOT / "contents.txt"
replace_once_or_final(
    contents,
    'Livre-V/CHAPITRE-13-Structures-JSON-et-formats-d-echange.md\nCompanion-Pack/index.md',
    'Livre-V/CHAPITRE-13-Structures-JSON-et-formats-d-echange.md\nLivre-V/CHAPITRE-14-Schemas-SQLite-et-migrations.md\nCompanion-Pack/index.md',
)

# Master plan
plan = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
replace_once_or_final(plan, 'version: "1.13.0"', 'version: "1.14.0"')
replace_once_or_final(plan, 'last-updated: "2026-07-28"', 'last-updated: "2026-07-29"')
replace_once_or_final(
    plan,
    '> **Statut :** 13 chapitres sur 26 rédigés et audités au niveau `static-review`',
    '> **Statut :** 14 chapitres sur 26 rédigés et audités au niveau `static-review`',
)
insert_once_or_present(
    plan,
    '## Chapitre 14 — Schémas SQLite et migrations\n',
    '\n**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n',
)

# Project continuity
continuity = ROOT / "CONTINUITE-PROJET.md"
replace_once_or_final(continuity, 'version: "4.00.0"', 'version: "4.01.0"')
replace_once_or_final(
    continuity,
    'last-updated: "2026-07-28T23:25:14+02:00"',
    f'last-updated: "{STAMP}"',
)
replace_once_or_final(
    continuity,
    '- progression du Livre V : 13 chapitres sur 26 ;',
    '- progression du Livre V : 14 chapitres sur 26 ;',
)
insert_once_or_present(
    continuity,
    '- chapitre 13 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n',
    '- chapitre 14 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n',
)
old_next = '''Le Livre V contient treize fiches sur 26 au niveau `static-review`. La fiche 13 fournit des contrats non linéaires pour JSON, JSONL, JSON Text Sequences, CSV, YAML et les formats Godot, avec encodage, schémas, versions, conversions, canonicalisation, sécurité et validation. Les convertisseurs permanents, matrices inter-parseurs, fichiers du Companion Pack, benchmarks, approbations juridiques, la licence globale et le balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-14-Schemas-SQLite-et-migrations.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 14 cataloguera types SQLite, affinités, clés, contraintes, index, transactions et migrations. Il devra distinguer schéma logique, DDL, migration, transaction, sauvegarde et restauration, fournir des modèles compacts et renvoyer au chapitre 8 du Livre II sans reprendre son tutoriel d’intégration.
'''
new_next = '''Le Livre V contient quatorze fiches sur 26 au niveau `static-review`. La fiche 14 fournit des contrats non linéaires pour SQLite : identité, types, clés, contraintes, index, transactions, migrations, sauvegardes, restaurations et diagnostics. Les bindings Godot, migrations et bases permanentes du Companion Pack, campagnes multiplateformes, benchmarks, approbations juridiques, la licence globale et le balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-15-Bases-vectorielles-et-recherche-semantique.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 15 référencera concepts, métriques et solutions locales de recherche vectorielle : embeddings, dimensions, distances, index, filtres, collections, suppression, réindexation et diagnostics. Il devra renvoyer au chapitre 10 du Livre II sans recopier le pipeline pédagogique ni présenter un backend comme universel.
'''
replace_once_or_final(continuity, old_next, new_next)

journal_entry = f'''### {STAMP} — version 4.01.0

- création de la fiche 14 — Schémas SQLite et migrations ;
- ajout de treize cartes, de trois matrices et de trois extraits SQL minimaux ;
- identité, versions, affinités, tables `STRICT`, clés, contraintes, relations, index, pragmas, transactions, migrations, sauvegardes et diagnostics indexés ;
- documentation officielle SQLite `3.53.4` revue le 29 juillet 2026 ;
- campagne temporaire de 36 bases et opérations synthétiques réussie avec Python `{python_version}`, module `sqlite3` `{sqlite_module_version}` et SQLite `{fixture_runtime}` ;
- différence entre version documentaire et runtime de fixture conservée explicitement ;
- métriques statiques : {lines} lignes, {headings} titres, {cards} fiches, {matrices} matrices, {len(links)} liens, {len(source_links)} renvois vers les Livres I à IV et {len(fragment_links)} liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 15 — Bases vectorielles et recherche sémantique, niveau Élevée ;
- aucun Godot, addon, export, fichier utilisateur, base de production, benchmark, approbation juridique ou PDF produit.


'''
insert_once_or_present(
    continuity,
    '## 27. Journal\n\n',
    journal_entry,
)

print(
    json.dumps(
        {
            "chapter_lines": lines,
            "headings": headings,
            "cards": cards,
            "matrices": matrices,
            "links": len(links),
            "source_links": len(source_links),
            "fragment_links": len(fragment_links),
            "official_links": len(official_links),
            "fenced_blocks": fenced_blocks,
            "sql_blocks": sql_blocks,
            "fixtures": fixture["total"],
            "fixture_runtime": fixture_runtime,
            "chapter_sha256": chapter_hash,
            "audit_sha256": audit_hash,
        },
        ensure_ascii=False,
    )
)
