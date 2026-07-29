#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAMP = "2026-07-29T06:18:10+02:00"
CHAPTER = ROOT / "Livre-V/CHAPITRE-15-Bases-vectorielles-et-recherche-semantique.md"
AUDIT = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-15.md"
PROOF = ROOT / "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-15.yaml"
FIXTURES = ROOT / "dist/QA-LIVRE-V-CH15-VECTORS.json"


def replace_once_or_present(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: remplacement attendu une fois, trouvé {count}: {old[:100]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def insert_after_once_or_present(path: Path, marker: str, insertion: str) -> None:
    text = path.read_text(encoding="utf-8")
    if insertion.strip() in text:
        return
    if text.count(marker) != 1:
        raise RuntimeError(f"{path}: marqueur absent ou dupliqué : {marker!r}")
    path.write_text(text.replace(marker, marker + insertion, 1), encoding="utf-8")


fixture = json.loads(FIXTURES.read_text(encoding="utf-8"))
if (fixture.get("total"), fixture.get("passed"), fixture.get("failed")) != (43, 43, 0):
    raise RuntimeError(f"Fixtures non acceptées : {fixture!r}")
for field in ("network_used", "model_loaded", "vector_backend_loaded", "user_data_processed"):
    if fixture.get(field) is not False:
        raise RuntimeError(f"Réserve runtime non respectée : {field}")

chapter_sha = hashlib.sha256(CHAPTER.read_bytes()).hexdigest()
audit_sha = hashlib.sha256(AUDIT.read_bytes()).hexdigest()
proof_text = PROOF.read_text(encoding="utf-8")
if chapter_sha != "1d3ca66382ac903bab6da3ea3254148d1029e092a1a4ee0d9f83d93440a1df66":
    raise RuntimeError(f"Empreinte chapitre inattendue : {chapter_sha}")
if audit_sha != "0fa731f03a52c665b7e1b4432065c20967bbaeb5ec4f38a839c195f90f6a2766":
    raise RuntimeError(f"Empreinte audit inattendue : {audit_sha}")
if chapter_sha not in proof_text or audit_sha not in proof_text:
    raise RuntimeError("La preuve ne référence pas les empreintes permanentes.")

index = ROOT / "Livre-V/index.md"
replace_once_or_present(index, 'version: "1.6.0"', 'version: "1.7.0"')
replace_once_or_present(
    index,
    '- [ ] Chapitre 15 — Bases vectorielles et recherche sémantique.',
    '- [x] [Fiche 15 — Bases vectorielles et recherche sémantique](CHAPITRE-15-Bases-vectorielles-et-recherche-semantique.md) — version `1.0.0`, niveau `static-review`.',
)
replace_once_or_present(
    index,
    'Progression : **14 chapitres sur 26** rédigés et audités. Les fiches 01 à 14 utilisent le profil de référence spécialisé du Livre V ; la fiche 14 catalogue schémas SQLite, types, clés, contraintes, index, transactions, migrations, sauvegardes, restaurations et diagnostics. Les bindings Godot, migrations permanentes, bases du Companion Pack, campagnes multiplateformes, benchmarks, licence globale et formats de publication avancés restent des chantiers distincts.',
    'Progression : **15 chapitres sur 26** rédigés et audités. Les fiches 01 à 15 utilisent le profil de référence spécialisé du Livre V ; la fiche 15 catalogue espaces vectoriels, embeddings, métriques, index exacts et ANN, filtres, collections, cycle de vie, réindexation, corpus et évaluations. Les modèles et backends réellement exécutés, campagnes matérielles, fichiers du Companion Pack, licence globale et formats de publication avancés restent des chantiers distincts.',
)

roadmap = ROOT / "ROADMAP.md"
replace_once_or_present(
    roadmap,
    '- [x] Schémas SQLite et migrations — fiche 14 rédigée et auditée au niveau `static-review`.\n- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.',
    '- [x] Schémas SQLite et migrations — fiche 14 rédigée et auditée au niveau `static-review`.\n- [x] Bases vectorielles et recherche sémantique — fiche 15 rédigée et auditée au niveau `static-review`.\n- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.',
)
replace_once_or_present(
    roadmap,
    '**Statut M6 : en cours — 14 chapitres rédigés, repérés et audités sur 26.**',
    '**Statut M6 : en cours — 15 chapitres rédigés, repérés et audités sur 26.**',
)

contents = ROOT / "contents.txt"
replace_once_or_present(
    contents,
    'Livre-V/CHAPITRE-14-Schemas-SQLite-et-migrations.md\nCompanion-Pack/index.md',
    'Livre-V/CHAPITRE-14-Schemas-SQLite-et-migrations.md\nLivre-V/CHAPITRE-15-Bases-vectorielles-et-recherche-semantique.md\nCompanion-Pack/index.md',
)

plan = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
replace_once_or_present(plan, 'version: "1.14.0"', 'version: "1.15.0"')
replace_once_or_present(
    plan,
    '> **Statut :** 14 chapitres sur 26 rédigés et audités au niveau `static-review`',
    '> **Statut :** 15 chapitres sur 26 rédigés et audités au niveau `static-review`',
)
insert_after_once_or_present(
    plan,
    '## Chapitre 15 — Bases vectorielles et recherche sémantique\n',
    '\n**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n',
)

continuity = ROOT / "CONTINUITE-PROJET.md"
replace_once_or_present(continuity, 'version: "4.01.0"', 'version: "4.02.0"')
replace_once_or_present(
    continuity,
    'last-updated: "2026-07-29T01:06:05+02:00"',
    f'last-updated: "{STAMP}"',
)
replace_once_or_present(
    continuity,
    '- progression du Livre V : 14 chapitres sur 26 ;',
    '- progression du Livre V : 15 chapitres sur 26 ;',
)
replace_once_or_present(
    continuity,
    '- chapitre 14 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- profil éditorial du Livre V',
    '- chapitre 14 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- chapitre 15 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- profil éditorial du Livre V',
)
text = continuity.read_text(encoding="utf-8")
pattern = re.compile(r"## 26\. Prochaine action\n.*?(?=## 27\. Journal)", re.DOTALL)
section = '''## 26. Prochaine action

Le Livre V contient quinze fiches sur 26 au niveau `static-review`. La fiche 15 fournit des contrats non linéaires pour espaces vectoriels, embeddings, métriques, index exacts et approximatifs, filtres, collections, cycle de vie, réindexation, corpus et évaluations. Les modèles et backends réellement exécutés, campagnes ANN et matérielles, fichiers du Companion Pack, approbations juridiques, licence globale et balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-16-Patrons-d-architecture.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 16 cataloguera composition, services, repositories, événements, états, anti-patterns, contextes d’usage et conséquences. Il devra relier chaque patron aux chapitres propriétaires et fournir des exemples compacts testables sans prescrire une architecture universelle ni recopier les systèmes complets.
'''
text, count = pattern.subn(section, text, count=1)
if count != 1:
    raise RuntimeError(f"Section prochaine action trouvée {count} fois.")
marker = "## 27. Journal\n"
entry = '''
### 2026-07-29T06:18:10+02:00 — version 4.02.0

- création de la fiche 15 — Bases vectorielles et recherche sémantique ;
- ajout de treize cartes et de trois matrices de référence ;
- espaces vectoriels, modèles, dimensions, métriques, normalisation, fragments, métadonnées, collections, exact, ANN, filtres, cycle de vie, réindexation et évaluation indexés ;
- Qdrant `1.18.2`, Faiss `1.14.3`, Chroma `1.5.9` et Sentence Transformers `5.5.1` revus comme références documentaires ;
- campagne temporaire de 43 contrats synthétiques réussie avec CPython `3.12.3` sans réseau, modèle, backend vectoriel ni donnée utilisateur ;
- échecs préparatoires du seuil 42/43 et de l’import dynamique Python 3.12 tracés avant le run réussi ;
- métriques statiques : 424 lignes, 19 titres, 13 fiches, 3 matrices, 67 liens, 28 renvois vers les Livres I à IV et 12 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 16 — Patrons d’architecture, niveau Élevée ;
- aucun Qdrant, Faiss, Chroma, modèle, Godot, réseau, GPU, corpus réel, benchmark matériel, approbation juridique ou PDF produit.

'''
if entry.strip() not in text:
    if text.count(marker) != 1:
        raise RuntimeError("Marqueur de journal absent ou dupliqué.")
    text = text.replace(marker, marker + entry, 1)
continuity.write_text(text, encoding="utf-8")

print(json.dumps({
    "fixtures": fixture["total"],
    "chapter_sha256": chapter_sha,
    "audit_sha256": audit_sha,
    "progress": "15/26",
    "next": "Livre-V/CHAPITRE-16-Patrons-d-architecture.md",
}, ensure_ascii=False))
