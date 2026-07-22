#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

STAMP = "2026-07-22T07:05:00+02:00"
CHAPTER = Path("Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md")
AUDIT = Path("Livre-II/QA/AUDIT-CHAPITRE-29.md")
PROOF = Path("Livre-II/QA/VALIDATION-FINALE-CHAPITRE-29.yaml")
CONTINUITY = Path("CONTINUITE-PROJET.md")
ROADMAP = Path("ROADMAP.md")


def once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


def sub_once(text: str, pattern: str, replacement: str, label: str, flags: int = 0) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return updated


def apply() -> None:
    chapter = CHAPTER.read_text(encoding="utf-8")
    chapter = sub_once(chapter, r'^version: "1\.0\.0"$', 'version: "1.0.1"', "chapter version", re.M)
    chapter = sub_once(chapter, r'^last-verified: ".+"$', f'last-verified: "{STAMP}"', "chapter verified", re.M)
    chapter = sub_once(chapter, r'^audit-date: ".+"$', f'audit-date: "{STAMP}"', "chapter audit date", re.M)
    chapter = once(
        chapter,
        'reference-python:\n  implementation: "CPython"\n  version: "3.14.6"',
        'reference-python:\n  implementation: "CPython"\n  version: "3.14.6"\n  fallback-version: "3.13.14"\n  qualification-status: "provisional"',
        "Python metadata",
    )
    chapter = once(
        chapter,
        '> **Versions de référence :** Godot `4.7.1-stable`, CPython `3.14.6`, édition Standard, GDScript, Forward+  ',
        '> **Versions de référence :** Godot `4.7.1-stable`, cible principale CPython `3.14.6`, repli CPython `3.13.14`, édition Standard, GDScript, Forward+  ',
        "version banner",
    )
    chapter = once(
        chapter,
        "Le chapitre 30 restera responsable de l’architecture finale des parcours Solo et Studio.",
        "Le chapitre 30 restera responsable de l’architecture finale des parcours Solo et Studio.\n\nCPython `3.14.6` est une **cible principale de qualification**, pas encore un environnement universellement garanti. CPython `3.13.14` reste le repli documenté tant que l’ensemble réel des dépendances du Starter Kit n’a pas passé la matrice de qualification. Cette distinction interdit de déduire la compatibilité de futures bibliothèques à partir des seules dépendances minimales de ce chapitre.",
        "qualification boundary",
    )
    chapter = once(
        chapter,
        "- **Rôle précis du bloc :** Les commandes créent un environnement isolé lié à CPython 3.14 puis mettent à niveau `pip` dans cet environnement uniquement.",
        "- **Rôle précis du bloc :** Les commandes créent un environnement isolé lié à la cible principale CPython 3.14 puis mettent à niveau `pip` dans cet environnement uniquement.",
        "Windows explanation",
    )
    chapter = once(
        chapter,
        "- **Paramètres importants :** `-3.14` sélectionne la série Python attendue ; `.venv` est un répertoire local non versionné.",
        "- **Paramètres importants :** `-3.14` sélectionne la cible principale ; le repli utilise `-3.13` dans un environnement distinct ; `.venv` est un répertoire local non versionné.",
        "Windows target",
    )
    chapter = once(chapter, 'requires = ["hatchling==1.27.0"]', 'requires = ["hatchling==1.31.0"]', "hatchling")
    chapter = once(chapter, 'requires-python = "==3.14.*"', 'requires-python = ">=3.13.14,<3.15"', "Python range")
    chapter = once(chapter, '  "jsonschema==4.25.1",', '  "jsonschema==4.26.0",', "jsonschema")
    chapter = once(
        chapter,
        "- **Limites et réserves :** Les versions d’exemple doivent être revues lors de la matérialisation ; le chapitre ne prétend pas avoir installé ces paquets.",
        "- **Limites et réserves :** `hatchling 1.31.0` et `jsonschema 4.26.0` déclarent Python 3.14, mais leur présence ne garantit ni les futures dépendances ni les intégrations propres au Starter Kit.",
        "dependency limits",
    )
    qualification = '''**Statut de qualification de l’interpréteur et des dépendances.**

La cible principale est CPython `3.14.6`. CPython `3.13.14` constitue le repli tant que la matrice complète du Starter Kit n’est pas validée. Le paquet d’automatisation reste volontairement minimal : les environnements de ComfyUI, de génération vocale, de LLM, de bases vectorielles ou d’autres services spécialisés conservent leurs propres interpréteurs et verrous.

Les dépendances minimales vérifiées par la matrice sont `hatchling==1.31.0` et `jsonschema==4.26.0`, ainsi que les dépendances transitives résolues par `pip`. L’installation doit utiliser `--only-binary=:all:` pendant la qualification afin qu’une roue native manquante provoque un échec visible au lieu d’une compilation implicite.

**État de qualification CI :** en attente de la matrice GitHub Actions.

| Environnement de qualification | Interpréteur | Rôle | État |
|---|---:|---|---|
| Windows hébergé x86-64 | CPython 3.14.6 | cible principale | à vérifier par la matrice CI |
| Linux hébergé x86-64 | CPython 3.14.6 | proxy de compatibilité pour WSL | à vérifier par la matrice CI |
| Windows hébergé x86-64 | CPython 3.13.14 | repli | à vérifier par la matrice CI |
| Linux hébergé x86-64 | CPython 3.13.14 | proxy de compatibilité pour WSL | à vérifier par la matrice CI |

Linux hébergé vérifie la disponibilité des distributions et les imports sous Linux, mais ne valide pas à lui seul les chemins montés, permissions, interactions Windows/WSL ou performances d’un WSL réel.

**Critères avant de déclarer un environnement validé.**

1. résolution complète sans conflit ;
2. installation avec roues binaires uniquement pour tout paquet natif ;
3. `pip check` sans erreur ;
4. import et lecture de version de chaque dépendance directe ;
5. exécution des tests et commandes du Starter Kit ;
6. verrous distincts pour chaque version de Python et chaque plateforme ;
7. reconstruction réussie dans un environnement vierge ;
8. validation séparée sur un WSL réel avant toute promesse spécifique à WSL.

'''
    chapter = once(
        chapter,
        "- **Limites et réserves :** `pip lock` est expérimental ; son format de sortie et son intégration doivent être validés avant d’en faire une dépendance de publication.\n\n## 10. Décrire la configuration de campagne",
        "- **Limites et réserves :** `pip lock` est expérimental ; son format de sortie et son intégration doivent être validés avant d’en faire une dépendance de publication.\n\n" + qualification + "## 10. Décrire la configuration de campagne",
        "qualification block",
    )
    CHAPTER.write_text(chapter, encoding="utf-8")
    lines = len(chapter.splitlines())
    headings = sum(1 for line in chapter.splitlines() if re.match(r"^#{1,6} ", line))

    audit = AUDIT.read_text(encoding="utf-8")
    audit = sub_once(audit, r'^version: "1\.0\.0"$', 'version: "1.0.1"', "audit version", re.M)
    audit = sub_once(audit, r'^chapter-version: "1\.0\.0"$', 'chapter-version: "1.0.1"', "audit chapter version", re.M)
    audit = sub_once(audit, r'^audit-date: ".+"$', f'audit-date: "{STAMP}"', "audit date", re.M)
    audit = sub_once(audit, r'^last-verified: ".+"$', f'last-verified: "{STAMP}"', "audit verified", re.M)
    audit = sub_once(audit, r'- lignes finales : \*\*\d+\*\* ;', f'- lignes finales : **{lines}** ;', "audit lines")
    audit = sub_once(audit, r'- titres Markdown contrôlés : \*\*\d+\*\* ;', f'- titres Markdown contrôlés : **{headings}** ;', "audit headings")
    audit = once(
        audit,
        "Le chapitre couvre CPython 3.14.6, environnements virtuels, métadonnées `pyproject.toml`, verrouillage reproductible, CLI typées, configuration TOML, codes de sortie, confinement des chemins, écritures contrôlées, JSON canonique, SHA-256, manifestes, RNG locaux, identités dérivées, JSON Schema Draft 2020-12, diagnostics structurés, plans immuables, lancement de Godot, orchestration des validateurs, JSONL borné, checkpoints, staging, parallélisme borné, nouvelle tentative cataloguée, provenance et archives déterministes.",
        "Le chapitre couvre CPython 3.14.6 comme cible principale provisoire, CPython 3.13.14 comme repli, `hatchling 1.31.0`, `jsonschema 4.26.0`, environnements virtuels, métadonnées `pyproject.toml`, verrouillage par version et plateforme, qualification par roues binaires, CLI typées, configuration TOML, codes de sortie, confinement des chemins, écritures contrôlées, JSON canonique, SHA-256, manifestes, RNG locaux, identités dérivées, JSON Schema Draft 2020-12, diagnostics structurés, plans immuables, lancement de Godot, orchestration des validateurs, JSONL borné, checkpoints, staging, parallélisme borné, nouvelle tentative cataloguée, provenance et archives déterministes.",
        "audit completeness",
    )
    audit = once(
        audit,
        "La version Python de référence a été vérifiée contre Python.org. Les contrats `venv`, `tomllib`, `subprocess`, `concurrent.futures` et `zipfile` ont été relus contre la documentation Python 3.14. La structure `pyproject.toml`, la spécification `pylock.toml` et le caractère expérimental de `pip lock` ont été vérifiés contre les documentations officielles PyPA et pip. Le dialecte JSON Schema 2020-12 a été vérifié contre la documentation officielle JSON Schema.\n\nCette revue ne constitue ni une installation de CPython, ni une résolution réelle des dépendances, ni une exécution des scripts.",
        "Python 3.14.6 et Python 3.13.14 ont été vérifiés contre Python.org. `hatchling 1.31.0` et `jsonschema 4.26.0` déclarent Python 3.14 dans leurs métadonnées PyPI. Les contrats `venv`, `tomllib`, `subprocess`, `concurrent.futures` et `zipfile` ont été relus contre la documentation Python. La structure `pyproject.toml`, la spécification `pylock.toml` et le caractère expérimental et dépendant de la plateforme de `pip lock` ont été vérifiés contre les documentations officielles PyPA et pip.\n\n**État de la matrice de compatibilité :** en attente de l’exécution GitHub Actions. Cette revue ne constitue pas encore une validation du Starter Kit ni d’un WSL réel.",
        "audit references",
    )
    audit = once(
        audit,
        "- `pip lock` est décrit comme expérimental ;",
        "- CPython 3.14.6 est présenté comme cible provisoire et CPython 3.13.14 comme repli ;\n- `hatchling 1.31.0` et `jsonschema 4.26.0` sont les seules dépendances directes qualifiées ici ;\n- l’installation de qualification exige des roues binaires ;\n- `pip lock` est décrit comme expérimental et spécifique à la version de Python et à la plateforme ;",
        "audit controls",
    )
    audit = once(
        audit,
        "- CPython 3.14.6 non installé dans le Starter Kit ;\n- dépendances Python non résolues ;\n- `pip lock` non exécuté ;",
        "- CPython 3.14.6 et 3.13.14 non installés dans le Starter Kit ;\n- ensemble complet des dépendances futures non résolu ;\n- comportement d’un WSL réel non qualifié ;\n- `pip lock` non exécuté dans le Starter Kit ;",
        "audit reservations",
    )
    AUDIT.write_text(audit, encoding="utf-8")

    proof = PROOF.read_text(encoding="utf-8")
    proof = sub_once(proof, r'^status: complete$', 'status: pending', "proof status", re.M)
    proof = sub_once(proof, r'^  version: 1\.0\.0$', '  version: 1.0.1', "proof chapter version", re.M)
    proof = sub_once(proof, r'^  blocking-errors: .+$', '  blocking-errors: pending', "proof errors", re.M)
    proof = sub_once(proof, r'^  warnings: .+$', '  warnings: pending', "proof warnings", re.M)
    proof = sub_once(proof, r'^  chapter-lines: \d+$', f'  chapter-lines: {lines}', "proof lines", re.M)
    proof = sub_once(proof, r'^  chapter-headings: \d+$', f'  chapter-headings: {headings}', "proof headings", re.M)
    proof = once(
        proof,
        "  python-3146-reference-documented: true",
        "  python-3146-primary-target-provisional: true\n  python-31314-fallback-documented: true\n  hatchling-1310-documented: true\n  jsonschema-4260-documented: true\n  binary-wheel-qualification-documented: true\n  hosted-compatibility-matrix-documented: true\n  real-wsl-validation-still-required: true\n  heavy-ai-environments-separated: true",
        "proof fields",
    )
    proof = sub_once(
        proof,
        r'ci:\n  validate-chapters-without-pdf:\n    run-id: \d+\n    conclusion: success\n  validate-usage-contexts:\n    run-id: \d+\n    conclusion: success\n  artifact:\n    id: \d+\n    name: chapter-validation-without-pdf\n    digest: sha256:[0-9a-f]+',
        "compatibility-matrix:\n  run-id: pending\n  conclusion: pending\n  windows-python-3146: pending\n  linux-python-3146: pending\n  windows-python-31314: pending\n  linux-python-31314: pending\nci:\n  validate-chapters-without-pdf:\n    run-id: pending\n    conclusion: pending\n  validate-usage-contexts:\n    run-id: pending\n    conclusion: pending\n  artifact:\n    id: pending\n    name: chapter-validation-without-pdf\n    digest: pending",
        "proof CI reset",
    )
    proof = once(
        proof,
        "- CPython 3.14.6 not installed in Starter Kit.\n- Python dependencies not resolved.\n- pip lock not executed.",
        "- CPython 3.14.6 and 3.13.14 not installed in Starter Kit.\n- Full future dependency set not resolved.\n- Real WSL environment not qualified.\n- pip lock not executed in Starter Kit.",
        "proof reservations",
    )
    proof = sub_once(proof, r'evidence-closure:\n  commit: [0-9a-f]+\n  conclusion: success', 'evidence-closure:\n  commit: pending\n  conclusion: pending', "proof closure")
    PROOF.write_text(proof, encoding="utf-8")

    continuity = CONTINUITY.read_text(encoding="utf-8")
    continuity = sub_once(continuity, r'^version: "3\.29\.1"$', 'version: "3.29.2"', "continuity version", re.M)
    continuity = sub_once(continuity, r'^last-updated: ".+"$', f'last-updated: "{STAMP}"', "continuity date", re.M)
    continuity = once(
        continuity,
        "- CPython 3.14.6 constitue la référence documentaire du paquet `asteria-tools` ;",
        "- CPython 3.14.6 constitue la cible principale provisoire du paquet `asteria-tools`, avec CPython 3.13.14 comme repli ;\n- `hatchling 1.31.0` et `jsonschema 4.26.0` constituent les dépendances directes minimales de qualification ;\n- la compatibilité doit être vérifiée avec des roues binaires sous Windows et Linux, puis sur un WSL réel avant toute garantie spécifique à WSL ;\n- les piles IA lourdes conservent des environnements Python séparés ;",
        "continuity decision",
    )
    continuity = once(continuity, "- chapitre 29 : version `1.0.0` ;", "- chapitre 29 : version `1.0.1` ;", "continuity chapter version")
    journal = f'''### {STAMP} — version 3.29.2\n\n- chapitre 29 porté à `1.0.1` après revue de compatibilité Python ;\n- CPython 3.14.6 reclassé en cible principale provisoire et CPython 3.13.14 ajouté comme repli ;\n- dépendances directes mises à jour vers `hatchling 1.31.0` et `jsonschema 4.26.0` ;\n- matrice Windows/Linux avec roues binaires et critères de qualification documentés ;\n- WSL réel et ensemble futur des dépendances maintenus en réserve ;\n- preuve QA remise en attente ; aucun PDF ni test du Starter Kit revendiqué.\n\n'''
    continuity = once(continuity, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal, "continuity journal")
    CONTINUITY.write_text(continuity, encoding="utf-8")

    roadmap = ROADMAP.read_text(encoding="utf-8")
    roadmap = once(
        roadmap,
        "**Statut M3 : en cours — 29 chapitres rédigés, repérés et audités sur 30.** Godot 4.7.1-stable, l’édition Standard, GDScript typé, Forward+ et CPython 3.14.6 constituent la base actuelle de `Project Asteria`.",
        "**Statut M3 : en cours — 29 chapitres rédigés, repérés et audités sur 30.** Godot 4.7.1-stable, l’édition Standard, GDScript typé et Forward+ constituent la base actuelle de `Project Asteria`. CPython 3.14.6 est la cible principale provisoire de l’automatisation, avec CPython 3.13.14 comme repli jusqu’à qualification du Starter Kit.",
        "roadmap status",
    )
    ROADMAP.write_text(roadmap, encoding="utf-8")
    print(f"Applied documentation: {lines} lines, {headings} headings")


def close(run_id: str) -> None:
    chapter = CHAPTER.read_text(encoding="utf-8")
    chapter = once(
        chapter,
        "**État de qualification CI :** en attente de la matrice GitHub Actions.",
        f"**État de qualification CI :** les quatre combinaisons hébergées ont installé les dépendances et leurs transitives avec des roues binaires, puis réussi `pip check` et les imports — run `{run_id}`. Ce résultat ne couvre ni les futures dépendances, ni le Starter Kit complet, ni un WSL réel.",
        "chapter matrix result",
    )
    chapter = chapter.replace("à vérifier par la matrice CI", "confirmé par la matrice CI")
    CHAPTER.write_text(chapter, encoding="utf-8")

    audit = AUDIT.read_text(encoding="utf-8")
    audit = once(
        audit,
        "**État de la matrice de compatibilité :** en attente de l’exécution GitHub Actions. Cette revue ne constitue pas encore une validation du Starter Kit ni d’un WSL réel.",
        f"**État de la matrice de compatibilité :** succès du run `{run_id}` pour CPython 3.14.6 et 3.13.14 sous Windows et Linux hébergés, avec roues binaires uniquement, `pip check` et imports. Ce résultat ne constitue pas une validation du Starter Kit ni d’un WSL réel.",
        "audit matrix result",
    )
    AUDIT.write_text(audit, encoding="utf-8")

    proof = PROOF.read_text(encoding="utf-8")
    proof = once(
        proof,
        "compatibility-matrix:\n  run-id: pending\n  conclusion: pending\n  windows-python-3146: pending\n  linux-python-3146: pending\n  windows-python-31314: pending\n  linux-python-31314: pending",
        f"compatibility-matrix:\n  run-id: {run_id}\n  conclusion: success\n  windows-python-3146: success\n  linux-python-3146: success\n  windows-python-31314: success\n  linux-python-31314: success",
        "proof matrix result",
    )
    PROOF.write_text(proof, encoding="utf-8")
    print(f"Closed matrix run {run_id}")


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("usage: fix.py apply | fix.py close <run-id>")
    if sys.argv[1] == "apply":
        apply()
    elif sys.argv[1] == "close" and len(sys.argv) == 3 and sys.argv[2].isdigit():
        close(sys.argv[2])
    else:
        raise SystemExit("usage: fix.py apply | fix.py close <run-id>")


if __name__ == "__main__":
    main()
