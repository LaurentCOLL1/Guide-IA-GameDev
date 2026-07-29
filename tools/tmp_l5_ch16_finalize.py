#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

TIMESTAMP = "2026-07-29T07:08:35+02:00"
CHAPTER_SHA = "23d740ea8746baf7aee5480536b0c89448d5e150e56bb0e543d8f74903fe0e38"
AUDIT_SHA = "9b3b4e57c4d0af0b5ad4b0c98cc2b605c6749f6bae88e1e88629665bd4f9d0ae"


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    Path(path).write_text(content, encoding="utf-8")


def replace_once(content: str, old: str, new: str, label: str) -> str:
    count = content.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return content.replace(old, new, 1)


def sha256(path: str) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate_integrity() -> None:
    if sha256("Livre-V/CHAPITRE-16-Patrons-d-architecture.md") != CHAPTER_SHA:
        raise RuntimeError("Chapter SHA-256 mismatch")
    if sha256("Livre-V/QA/AUDIT-CHAPITRE-16.md") != AUDIT_SHA:
        raise RuntimeError("Audit SHA-256 mismatch")
    metrics = json.loads(Path("dist/QA-LIVRE-V-CH16-CHAPTER.json").read_text(encoding="utf-8"))
    expected = {
        "lines": 409,
        "headings": 19,
        "cards": 13,
        "matrices": 3,
        "markdown_links": 65,
        "source_book_links": 34,
        "fragment_links": 21,
        "official_links": 13,
        "fenced_blocks": 0,
        "compact_diagrams": 7,
        "chapter_sha256": CHAPTER_SHA,
    }
    if metrics != expected:
        raise RuntimeError(f"Chapter metrics mismatch: {metrics!r}")


def patch_index() -> None:
    path = "Livre-V/index.md"
    content = read(path)
    content = replace_once(content, 'version: "1.7.0"', 'version: "1.8.0"', "index version")
    content = replace_once(
        content,
        "- [ ] Chapitre 16 — Patrons d’architecture.",
        "- [x] [Fiche 16 — Patrons d’architecture](CHAPITRE-16-Patrons-d-architecture.md) — version `1.0.0`, niveau `static-review`.",
        "index chapter",
    )
    content = replace_once(
        content,
        "Progression : **15 chapitres sur 26** rédigés et audités. Les fiches 01 à 15 utilisent le profil de référence spécialisé du Livre V ; la fiche 15 catalogue espaces vectoriels, embeddings, métriques, index exacts et ANN, filtres, collections, cycle de vie, réindexation, corpus et évaluations. Les modèles et backends réellement exécutés, campagnes matérielles, fichiers du Companion Pack, licence globale et formats de publication avancés restent des chantiers distincts.",
        "Progression : **16 chapitres sur 26** rédigés et audités. Les fiches 01 à 16 utilisent le profil de référence spécialisé du Livre V ; la fiche 16 catalogue frontières, composition, injection, services d’application, repositories, ports, adaptateurs, événements, propriété d’état, façades, stratégies, coutures de test et anti-patterns. Les scènes, graphes et adaptateurs réellement exécutés, patrons de gameplay, fichiers du Companion Pack, licence globale et formats de publication avancés restent des chantiers distincts.",
        "index status",
    )
    write(path, content)


def patch_roadmap() -> None:
    path = "ROADMAP.md"
    content = read(path)
    content = replace_once(
        content,
        "- [x] Bases vectorielles et recherche sémantique — fiche 15 rédigée et auditée au niveau `static-review`.\n- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
        "- [x] Bases vectorielles et recherche sémantique — fiche 15 rédigée et auditée au niveau `static-review`.\n- [x] Patrons d’architecture — fiche 16 rédigée et auditée au niveau `static-review`.\n- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
        "roadmap chapter",
    )
    content = replace_once(
        content,
        "**Statut M6 : en cours — 15 chapitres rédigés, repérés et audités sur 26.**",
        "**Statut M6 : en cours — 16 chapitres rédigés, repérés et audités sur 26.**",
        "roadmap status",
    )
    write(path, content)


def patch_contents() -> None:
    path = "contents.txt"
    content = read(path)
    content = replace_once(
        content,
        "Livre-V/CHAPITRE-15-Bases-vectorielles-et-recherche-semantique.md\nCompanion-Pack/index.md",
        "Livre-V/CHAPITRE-15-Bases-vectorielles-et-recherche-semantique.md\nLivre-V/CHAPITRE-16-Patrons-d-architecture.md\nCompanion-Pack/index.md",
        "contents chapter",
    )
    write(path, content)


def patch_plan() -> None:
    path = "plans/LIVRE-V-PLAN-MAITRE.md"
    content = read(path)
    content = replace_once(content, 'version: "1.15.0"', 'version: "1.16.0"', "plan version")
    content = replace_once(
        content,
        "> **Statut :** 15 chapitres sur 26 rédigés et audités au niveau `static-review`",
        "> **Statut :** 16 chapitres sur 26 rédigés et audités au niveau `static-review`",
        "plan status",
    )
    content = replace_once(
        content,
        "## Chapitre 16 — Patrons d’architecture\n\n**Objectifs**",
        "## Chapitre 16 — Patrons d’architecture\n\n**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n**Objectifs**",
        "plan chapter state",
    )
    write(path, content)


def patch_continuity() -> None:
    path = "CONTINUITE-PROJET.md"
    content = read(path)
    content = replace_once(content, 'version: "4.02.0"', 'version: "4.03.0"', "continuity version")
    content = replace_once(
        content,
        'last-updated: "2026-07-29T06:18:10+02:00"',
        f'last-updated: "{TIMESTAMP}"',
        "continuity timestamp",
    )
    content = replace_once(
        content,
        "- progression du Livre V : 15 chapitres sur 26 ;",
        "- progression du Livre V : 16 chapitres sur 26 ;",
        "continuity progress",
    )
    content = replace_once(
        content,
        "- chapitre 15 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- profil éditorial du Livre V",
        "- chapitre 15 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- chapitre 16 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- profil éditorial du Livre V",
        "continuity chapter state",
    )
    old_next = """Le Livre V contient quinze fiches sur 26 au niveau `static-review`. La fiche 15 fournit des contrats non linéaires pour espaces vectoriels, embeddings, métriques, index exacts et approximatifs, filtres, collections, cycle de vie, réindexation, corpus et évaluations. Les modèles et backends réellement exécutés, campagnes ANN et matérielles, fichiers du Companion Pack, approbations juridiques, licence globale et balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-16-Patrons-d-architecture.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 16 cataloguera composition, services, repositories, événements, états, anti-patterns, contextes d’usage et conséquences. Il devra relier chaque patron aux chapitres propriétaires et fournir des exemples compacts testables sans prescrire une architecture universelle ni recopier les systèmes complets."""
    new_next = """Le Livre V contient seize fiches sur 26 au niveau `static-review`. La fiche 16 fournit des contrats non linéaires pour frontières, composition, injection, services d’application, repositories, ports, adaptateurs, événements, propriété d’état, façades, stratégies, coutures de test et anti-patterns. Les scènes, graphes, adaptateurs et tests de contrat réellement exécutés, patrons de gameplay, fichiers du Companion Pack, approbations juridiques, licence globale et balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-17-Patrons-de-gameplay.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 17 cataloguera machines à états, capacités, inventaires, quêtes et simulations, avec séparation des données, règles et présentations, variantes simples et avancées, diagnostics et critères de test. Il devra renvoyer aux systèmes propriétaires du Livre II sans les recopier ni prétendre qu’un patron de gameplay convient à tous les projets."""
    content = replace_once(content, old_next, new_next, "continuity next action")
    journal_anchor = "## 27. Journal\n\n"
    journal = f"""## 27. Journal

### {TIMESTAMP} — version 4.03.0

- création de la fiche 16 — Patrons d’architecture ;
- ajout de treize cartes, de trois matrices et de sept diagrammes compacts ;
- frontières, dépendances, composition root, injection, composition, services, repositories, ports, adaptateurs, événements, propriété d’état, façades, stratégies et coutures de test indexés ;
- documentation Godot `4.7` et sources spécialisées sur injection, Repository et architectures événementielles relues le 29 juillet 2026 ;
- campagne temporaire de 67 contrats synthétiques réussie avec CPython `3.12.3`, sans Godot, addon, stockage, réseau ni donnée utilisateur ;
- métriques statiques : 409 lignes, 19 titres, 13 fiches, 3 matrices, 65 liens, 34 renvois vers les Livres I à IV, 21 liens profonds et 7 diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 17 — Patrons de gameplay, niveau Élevée ;
- aucun runtime Godot, GDScript, scène, addon, base, service, projet Companion Pack, approbation juridique ou PDF produit.


"""
    content = replace_once(content, journal_anchor, journal, "continuity journal")
    write(path, content)


def main() -> int:
    validate_integrity()
    patch_index()
    patch_roadmap()
    patch_contents()
    patch_plan()
    patch_continuity()
    print("Permanent governance patched successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
