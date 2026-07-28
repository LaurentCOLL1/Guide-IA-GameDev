#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "Livre-V/CHAPITRE-11-Reference-GDScript.md"
AUDIT = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-11.md"
PROOF = ROOT / "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-11.yaml"
TIMESTAMP = "2026-07-28T22:02:17+02:00"
DATE = "2026-07-28"
BASE_COMMIT = "6dd1f4df63b34220386ea5052471a8ecec5ccca0"
BRANCH = "docs/livre-v-ch11-reference-gdscript"

LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+", re.MULTILINE)
SOURCE_RE = re.compile(r"^\.\./Livre-(?:I|II|III|IV)/")
OFFICIAL_RE = re.compile(r"^https?://")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: attendu une occurrence, trouvé {count}")
    return text.replace(old, new, 1)


def metrics(text: str) -> dict[str, int]:
    links = LINK_RE.findall(text)
    targets = [target.strip().split()[0].strip("<>") for _, target in links]
    source_targets = [target for target in targets if SOURCE_RE.match(target)]
    fragment_targets = [target for target in source_targets if "#" in target]
    official_targets = [target for target in targets if OFFICIAL_RE.match(target)]
    return {
        "lines": len(text.splitlines()),
        "headings": len(HEADING_RE.findall(text)),
        "cards": text.count("<!-- l5:card -->"),
        "matrices": text.count("<!-- l5:matrix -->"),
        "links": len(links),
        "source_links": len(source_targets),
        "fragment_links": len(fragment_targets),
        "official_links": len(official_targets),
        "fenced_blocks": len(re.findall(r"^(?:```|~~~)", text, re.MULTILINE)) // 2,
    }


def assert_chapter_contract(m: dict[str, int], text: str) -> None:
    expected = {"headings": 18, "cards": 13, "matrices": 3, "fenced_blocks": 0}
    for key, value in expected.items():
        if m[key] != value:
            raise RuntimeError(f"métrique {key}: attendu {value}, trouvé {m[key]}")
    if m["source_links"] < 18 or m["fragment_links"] < 16:
        raise RuntimeError(f"liens propriétaires insuffisants: {m}")
    required = (
        'document-format: "reference-cards"',
        'reference-scope: "gdscript-4-7-language-reference"',
        "Godot `4.7.1-stable`",
        "aucun parseur GDScript ni moteur lancé",
        "<!-- l5:card -->",
        "<!-- l5:matrix -->",
    )
    for token in required:
        if token not in text:
            raise RuntimeError(f"contrat absent: {token}")


def build_audit(m: dict[str, int]) -> str:
    return f'''---
title: "Audit — Livre V, fiche 11 : Référence GDScript"
id: "DOC-L5-QA-AUDIT-CH11"
status: "complete"
version: "1.0.0"
last-verified: "{TIMESTAMP}"
lang: "fr-FR"
book: "Livre V"
chapter: 11
audit-date: "{TIMESTAMP}"
audit-level: "static-review"
validation-authority: "livre-v-reference-profile"
---

# Audit — Fiche 11 : Référence GDScript

## 1. Décision

La fiche est conforme au profil spécialisé du Livre V sous réserve des exécutions explicitement laissées ouvertes. Elle fournit une référence non linéaire de GDScript pour Godot `4.7.1-stable`, relie les notions au chapitre pédagogique propriétaire et ne présente aucune forme comme analysée ou exécutée.

## 2. Périmètre contrôlé

- chemin canonique : `Livre-V/CHAPITRE-11-Reference-GDScript.md` ;
- identifiant : `DOC-L5-CH11` ;
- version : `1.0.0` ;
- format : `reference-cards` ;
- niveau de preuve : `static-review` ;
- documentation officielle de Godot `4.7.1-stable` revue le 28 juillet 2026 ;
- aucune compilation PDF intermédiaire.

## 3. Métriques statiques

| Mesure | Valeur |
|---|---:|
| lignes | {m['lines']} |
| titres | {m['headings']} |
| cartes `l5:card` | {m['cards']} |
| matrices `l5:matrix` | {m['matrices']} |
| liens Markdown | {m['links']} |
| renvois vers les Livres I à IV | {m['source_links']} |
| liens profonds vers les sources propriétaires | {m['fragment_links']} |
| liens officiels | {m['official_links']} |
| blocs clôturés | {m['fenced_blocks']} |

## 4. Couverture du plan maître

| Exigence | Couverture |
|---|---|
| syntaxe | déclarations, expressions, contrôle de flux et formes de fonction |
| types | scalaires, textes, mathématiques, collections, objets, `Callable`, `Signal` et `Variant` |
| fonctions | paramètres, retours, statiques, lambdas, appels différés et `await` |
| classes | `class_name`, héritage, composition, classes internes et propriétés |
| annotations | export, onready, tool, warnings, RPC et Inspector |
| collections | tableaux, dictionnaires, types, duplication et mutations |
| opérateurs | matrice par priorité et pièges |
| fonctions courantes | index alphabétique de mots-clés et fonctions |
| chapitre pédagogique | renvois précis vers le Livre II |
| pièges et versions | compatibilité `4.7.1`, docs `stable`, avertissements et migration |
| aide-mémoire | treize cartes et trois matrices consultables isolément |
| exemples minimaux | code inline uniquement, sans fichier exécutable matérialisé |

## 5. Frontières

La fiche conserve les responsabilités suivantes :

- l’apprentissage progressif reste au Livre II, chapitre 2 ;
- scènes, nœuds, Resources et signaux restent au Livre II, chapitre 3 ;
- les recettes exécutables restent au chapitre 10 du Livre V ;
- la référence Python reste au chapitre 12 ;
- les formats d’échange restent au chapitre 13 ;
- les diagnostics transversaux restent au chapitre 20 ;
- les campagnes et mesures restent au chapitre 21 ;
- les compatibilités historiques restent au chapitre 22 ;
- licences et conformité restent au chapitre 25 ;
- les fichiers testables réels restent au Companion Pack.

## 6. Séparation information et exécution

Aucune carte n’annonce :

- un fichier `.gd` écrit hors du chapitre Markdown ;
- un parse ou import Godot ;
- une scène instanciée ;
- un signal connecté ou émis ;
- une Resource chargée ;
- un avertissement réellement observé ;
- un test unitaire ou d’intégration exécuté ;
- une migration de projet réalisée ;
- une compatibilité autre que la cible documentaire déclarée.

## 7. Liens et sources

Les renvois propriétaires ciblent notamment la nature de GDScript, la structure des fichiers, le typage, les types, les fonctions, les classes, les annotations, les collections, le cycle de vie, les ressources, les erreurs, les avertissements et les tests déterministes.

Les liens externes pointent vers la release Godot `4.7.1`, la référence GDScript, le guide de style, le typage statique, les propriétés exportées, les avertissements et les classes officielles. Leur présence ne constitue ni installation, ni parse, ni exécution.

## 8. Risques et réserves

1. aucun binaire Godot téléchargé ou lancé ;
2. aucun fichier GDScript analysé, importé ou exécuté ;
3. aucune scène, nœud, Resource ou Inspector manipulé ;
4. aucun signal, `Callable`, `await` ou cycle de vie observé ;
5. aucun avertissement configuré ou transformé en erreur ;
6. aucun test de type, collection, opérateur ou propriété exécuté ;
7. aucune vérification de performance du typage réalisée ;
8. aucune migration depuis une version antérieure testée ;
9. aucune compatibilité C#, GDExtension ou plateforme exportée qualifiée ;
10. aucun fichier ou test du Companion Pack matérialisé ;
11. aucune approbation juridique organisationnelle réalisée ;
12. aucun PDF produit ; licence globale et balisage avancé ouverts.

## 9. Critère d’acceptation

La fiche est acceptée au niveau `static-review` lorsque les validateurs permanents confirment structure, métadonnées, liens locaux, cartes, matrices, fragments propriétaires et absence de PDF. Toute allégation de syntaxe confirmée ou de comportement exige ensuite un binaire Godot exact, un projet minimal, des commandes et des artefacts enregistrés.
'''


def build_proof(m: dict[str, int], chapter_hash: str, audit_hash: str) -> str:
    return f'''schema-version: 2
evidence-id: DOC-L5-QA-EVIDENCE-CH11
validation-authority: livre-v-reference-profile
status: complete
validation-date: '{DATE}'
validated-base-commit: {BASE_COMMIT}
source-branch: {BRANCH}
chapter:
  id: DOC-L5-CH11
  path: Livre-V/CHAPITRE-11-Reference-GDScript.md
  version: 1.0.0
  document-format: reference-cards
  audit-level: static-review
results:
  blocking-errors: 0
  warnings: 12
  chapter-lines: {m['lines']}
  chapter-headings: {m['headings']}
  reference-cards: {m['cards']}
  matrices: {m['matrices']}
  internal-links: {m['links']}
  source-book-links: {m['source_links']}
  fragment-links: {m['fragment_links']}
  official-links: {m['official_links']}
  fenced-blocks: {m['fenced_blocks']}
  reference-engine: Godot-4.7.1-stable
  syntax-covered: true
  typing-covered: true
  built-in-types-covered: true
  operators-covered: true
  control-flow-covered: true
  functions-and-callables-covered: true
  classes-and-properties-covered: true
  annotations-covered: true
  collections-covered: true
  signals-and-lifecycle-covered: true
  resources-and-paths-covered: true
  diagnostics-covered: true
  alphabetical-index-present: true
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
- No Godot binary was downloaded or launched.
- No GDScript file was parsed, imported or executed.
- No scene, node, Resource or Inspector was manipulated.
- No signal, Callable, await or lifecycle behavior was observed.
- No warning was configured, raised or converted to an error.
- No type, collection, operator or property test was executed.
- No static-typing performance measurement was produced.
- No migration from an earlier Godot version was tested.
- No C#, GDExtension or exported-platform compatibility was qualified.
- No permanent Companion Pack file or test was materialized.
- No organisational legal approval was performed.
- No PDF was produced; collection licence and advanced accessibility tagging remain open.
'''


def update_index() -> None:
    path = ROOT / "Livre-V/index.md"
    text = read(path)
    text = replace_once(text, 'version: "1.2.0"', 'version: "1.3.0"', "index version")
    text = replace_once(
        text,
        '- [ ] Chapitre 11 — Référence GDScript.',
        '- [x] [Fiche 11 — Référence GDScript](CHAPITRE-11-Reference-GDScript.md) — version `1.0.0`, niveau `static-review`.',
        "index chapter",
    )
    old = "Progression : **10 chapitres sur 26** rédigés et audités. Les fiches 01 à 10 utilisent le profil de référence spécialisé du Livre V ; la fiche 10 catalogue recettes GDScript, Python, PowerShell et Bash, statuts de preuve, codes de sortie, tests, sécurité et licences. Les exécutions runtime, fichiers du Companion Pack, benchmarks, licence globale et formats de publication avancés restent des chantiers distincts."
    new = "Progression : **11 chapitres sur 26** rédigés et audités. Les fiches 01 à 11 utilisent le profil de référence spécialisé du Livre V ; la fiche 11 fournit une référence GDScript non linéaire pour Godot 4.7.1, avec syntaxe, types, opérateurs, fonctions, classes, annotations, collections et diagnostics. Les parses et exécutions runtime, fichiers du Companion Pack, benchmarks, licence globale et formats de publication avancés restent des chantiers distincts."
    text = replace_once(text, old, new, "index status")
    write(path, text)


def update_roadmap() -> None:
    path = ROOT / "ROADMAP.md"
    text = read(path)
    anchor = '- [x] Bibliothèque de scripts et recettes de code — fiche 10 rédigée et auditée au niveau `static-review`.\n'
    addition = anchor + '- [x] Référence GDScript — fiche 11 rédigée et auditée au niveau `static-review`.\n'
    text = replace_once(text, anchor, addition, "roadmap chapter")
    text = replace_once(
        text,
        "**Statut M6 : en cours — 10 chapitres rédigés, repérés et audités sur 26.**",
        "**Statut M6 : en cours — 11 chapitres rédigés, repérés et audités sur 26.**",
        "roadmap status",
    )
    write(path, text)


def update_contents() -> None:
    path = ROOT / "contents.txt"
    text = read(path)
    anchor = "Livre-V/CHAPITRE-10-Bibliotheque-de-scripts-et-recettes-de-code.md\nCompanion-Pack/index.md"
    replacement = "Livre-V/CHAPITRE-10-Bibliotheque-de-scripts-et-recettes-de-code.md\nLivre-V/CHAPITRE-11-Reference-GDScript.md\nCompanion-Pack/index.md"
    text = replace_once(text, anchor, replacement, "contents")
    write(path, text)


def update_plan() -> None:
    path = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
    text = read(path)
    text = replace_once(text, 'version: "1.10.0"', 'version: "1.11.0"', "plan version")
    text = replace_once(
        text,
        "> **Statut :** 10 chapitres sur 26 rédigés et audités au niveau `static-review`",
        "> **Statut :** 11 chapitres sur 26 rédigés et audités au niveau `static-review`",
        "plan status",
    )
    text = replace_once(
        text,
        "## Chapitre 11 — Référence GDScript\n\n**Objectifs**",
        "## Chapitre 11 — Référence GDScript\n\n**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n**Objectifs**",
        "plan chapter state",
    )
    write(path, text)


def update_continuity(m: dict[str, int]) -> None:
    path = ROOT / "CONTINUITE-PROJET.md"
    text = read(path)
    text = replace_once(text, 'version: "3.97.0"', 'version: "3.98.0"', "continuity version")
    text = replace_once(
        text,
        'last-updated: "2026-07-28T21:24:52+02:00"',
        f'last-updated: "{TIMESTAMP}"',
        "continuity timestamp",
    )
    text = replace_once(
        text,
        "- progression du Livre V : 10 chapitres sur 26 ;",
        "- progression du Livre V : 11 chapitres sur 26 ;",
        "continuity progression",
    )
    anchor = "- chapitre 10 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
    addition = anchor + "- chapitre 11 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
    text = replace_once(text, anchor, addition, "continuity chapter")

    new_next = '''## 26. Prochaine action

Le Livre V contient onze fiches sur 26 au niveau `static-review`. La fiche 11 fournit une référence non linéaire de GDScript pour Godot `4.7.1-stable`, avec syntaxe, types, opérateurs, fonctions, classes, annotations, collections, signaux, ressources et diagnostics. Les parses et exécutions réels, migrations, fichiers du Companion Pack, benchmarks, approbations juridiques, la licence globale et le balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-12-Reference-Python.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 12 fournira une référence non linéaire de Python pour l’automatisation du guide : environnements, types, fonctions, fichiers, CLI, tests, dépendances et packaging. Il devra renvoyer aux tutoriels propriétaires, comparer seulement les notions utiles avec GDScript et ne présenter aucun script comme exécuté sans preuve.
'''
    text, count = re.subn(r"## 26\. Prochaine action\n.*?(?=## 27\. Journal)", new_next, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError("continuity next action: section introuvable")

    journal = f'''## 27. Journal

### {TIMESTAMP} — version 3.98.0

- création de la fiche 11 — Référence GDScript ;
- ajout de treize cartes et de trois matrices compactes ;
- syntaxe, types, opérateurs, contrôle de flux, fonctions, classes, annotations, collections, signaux, ressources et diagnostics indexés ;
- aide-mémoire relié au chapitre pédagogique du Livre II sans duplication du cours ;
- documentation officielle de Godot `4.7.1-stable`, du typage, du guide de style, des exports et des avertissements revue le 28 juillet 2026 ;
- métriques statiques : {m['lines']} lignes, {m['headings']} titres, {m['cards']} fiches, {m['matrices']} matrices, {m['links']} liens, {m['source_links']} renvois vers les Livres I à IV et {m['fragment_links']} liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 12 — Référence Python, niveau Élevée ;
- aucun binaire Godot, parseur, import, scène, test, migration, artefact du Companion Pack, approbation juridique ou PDF produit.


'''
    text = replace_once(text, "## 27. Journal\n\n", journal, "continuity journal")
    write(path, text)


def main() -> None:
    chapter = read(CHAPTER)
    m = metrics(chapter)
    assert_chapter_contract(m, chapter)

    audit = build_audit(m)
    write(AUDIT, audit)
    proof = build_proof(m, sha256(chapter), sha256(audit))
    write(PROOF, proof)

    update_index()
    update_roadmap()
    update_contents()
    update_plan()
    update_continuity(m)

    print("chapter_metrics:", m)
    print("chapter_sha256:", sha256(chapter))
    print("audit_sha256:", sha256(audit))


if __name__ == "__main__":
    main()
