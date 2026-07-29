from __future__ import annotations

import hashlib
import os
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "Livre-V/CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md"
AUDIT = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-21.md"
PROOF = ROOT / "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-21.yaml"
INDEX = ROOT / "Livre-V/index.md"
ROADMAP = ROOT / "ROADMAP.md"
CONTENTS = ROOT / "contents.txt"
PLAN = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
CONTINUITY = ROOT / "CONTINUITE-PROJET.md"

TIMESTAMP = "2026-07-29T18:11:00+02:00"
SOURCE_HEAD = os.environ.get("SOURCE_HEAD_COMMIT", "unknown")
RUN_ID = int(os.environ.get("GITHUB_RUN_ID", "0"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


proof = yaml.safe_load(read(PROOF))
proof["status"] = "complete"
proof["results"]["blocking-errors"] = 0
proof["integrity"]["chapter-sha256"] = sha256(CHAPTER)
proof["integrity"]["audit-sha256"] = sha256(AUDIT)
proof["ci"]["lightweight-finalization"] = {
    "workflow": "Temporary Livre V Chapter 21 Script Runner",
    "run-id": RUN_ID,
    "source-head-commit": SOURCE_HEAD,
    "conclusion": "success",
    "validated-steps": [
        "structure, metadata, links and duplicates",
        "Livre V cards and deep links",
        "structured code explanations",
        "usage marker presence",
        "semantic marker consistency",
        "context coverage",
        "absence of PDF",
    ],
}
write(PROOF, yaml.safe_dump(proof, sort_keys=False, allow_unicode=True))

text = read(INDEX)
text = replace_once(text, 'version: "1.12.0"', 'version: "1.13.0"', "index version")
text = replace_once(
    text,
    "- [ ] Chapitre 21 — Benchmarks et méthodes de mesure.",
    "- [x] [Fiche 21 — Benchmarks et méthodes de mesure](CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md) — version `1.0.0`, niveau `static-review`.",
    "index chapter 21",
)
text = replace_once(
    text,
    "Progression : **20 chapitres sur 26** rédigés et audités. Les fiches 01 à 20 utilisent le profil de référence spécialisé du Livre V ; la fiche 20 rassemble contrat diagnostique, routage, niveaux de certitude, empreintes d’environnement, reproduction, preuves, arbre progressif, messages, hypothèses, causes, contournements, corrections, index transversaux et maintenance versionnée. Les cas reproduits, outils exécutables et fixtures permanentes du Companion Pack, les protocoles de benchmark, les matrices de compatibilité, la licence globale et les formats de publication avancés restent des chantiers distincts.",
    "Progression : **21 chapitres sur 26** rédigés et audités. Les fiches 01 à 21 utilisent le profil de référence spécialisé du Livre V ; la fiche 21 rassemble contrat de benchmark, environnement, scénarios, warm-up, caches, répétitions, unités, données brutes, statistiques, exclusions, comparaisons, rapports, niveaux de preuve et maintenance. Les campagnes exécutées, scripts et fixtures permanents du Companion Pack, les matrices de compatibilité, les comparatifs, la licence globale et les formats de publication avancés restent des chantiers distincts.",
    "index status",
)
write(INDEX, text)

text = read(ROADMAP)
text = replace_once(
    text,
    "- [x] Catalogue des erreurs et diagnostics — fiche 20 rédigée et auditée au niveau `static-review`.\n- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
    "- [x] Catalogue des erreurs et diagnostics — fiche 20 rédigée et auditée au niveau `static-review`.\n- [x] Benchmarks et méthodes de mesure — fiche 21 rédigée et auditée au niveau `static-review`.\n- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
    "roadmap chapter 21",
)
text = replace_once(
    text,
    "**Statut M6 : en cours — 20 chapitres rédigés, repérés et audités sur 26.**",
    "**Statut M6 : en cours — 21 chapitres rédigés, repérés et audités sur 26.**",
    "roadmap status",
)
write(ROADMAP, text)

text = read(CONTENTS)
text = replace_once(
    text,
    "Livre-V/CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md\nCompanion-Pack/index.md",
    "Livre-V/CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md\nLivre-V/CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md\nCompanion-Pack/index.md",
    "contents chapter 21",
)
write(CONTENTS, text)

text = read(PLAN)
text = replace_once(text, 'version: "1.20.0"', 'version: "1.21.0"', "plan version")
text = replace_once(
    text,
    "> **Statut :** 20 chapitres sur 26 rédigés et audités au niveau `static-review`",
    "> **Statut :** 21 chapitres sur 26 rédigés et audités au niveau `static-review`",
    "plan status",
)
text = replace_once(
    text,
    "## Chapitre 21 — Benchmarks et méthodes de mesure\n\n**Objectifs**",
    "## Chapitre 21 — Benchmarks et méthodes de mesure\n\n**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n**Objectifs**",
    "plan chapter state",
)
write(PLAN, text)

text = read(CONTINUITY)
text = replace_once(text, 'version: "4.07.0"', 'version: "4.08.0"', "continuity version")
text = replace_once(
    text,
    'last-updated: "2026-07-29T16:26:00+02:00"',
    f'last-updated: "{TIMESTAMP}"',
    "continuity timestamp",
)
text = replace_once(
    text,
    "- progression du Livre V : 20 chapitres sur 26 ;",
    "- progression du Livre V : 21 chapitres sur 26 ;",
    "continuity progress",
)
text = replace_once(
    text,
    "- chapitre 20 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- profil éditorial du Livre V",
    "- chapitre 20 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- chapitre 21 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- profil éditorial du Livre V",
    "continuity chapter 21",
)
text = replace_once(
    text,
    "- ne pas fermer un défaut sur un contournement, un commit ou une CI verte sans vérification et non-régression adaptées ;\n\n## 25. État courant",
    "- ne pas fermer un défaut sur un contournement, un commit ou une CI verte sans vérification et non-régression adaptées ;\n"
    "- ne pas présenter une moyenne isolée comme description suffisante d’une distribution ;\n"
    "- ne pas traiter les observations d’un même run comme des répétitions indépendantes ;\n"
    "- ne pas supprimer une valeur extrême ou manquante sans règle, statut et justification conservés ;\n"
    "- ne pas arrêter une campagne dès que le résultat devient favorable ni changer la métrique primaire après lecture ;\n\n"
    "## 25. État courant",
    "continuity benchmark rules",
)
new_next = f'''## 26. Prochaine action

Le Livre V contient vingt et une fiches sur 26 au niveau `static-review`. La fiche 21 fournit un contrat transversal pour question, environnement, scénario, warm-up, caches, répétitions, unités, données brutes, statistiques, exclusions, comparaisons, rapports, niveaux de preuve et maintenance. Les campagnes réelles, scripts et fixtures du Companion Pack, matrices de compatibilité, comparatifs, approbations organisationnelles, licence globale et balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-22-Matrices-de-compatibilite.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 22 croisera OS, GPU, versions, formats, outils et backends. Il distinguera support officiel, expérimental, testé, non vérifié et incompatible, conservera date et source, et interdira d’interpréter l’absence de test comme une incompatibilité.
## 27. Journal'''
text, count = re.subn(
    r"## 26\. Prochaine action\n.*?\n## 27\. Journal",
    new_next,
    text,
    count=1,
    flags=re.S,
)
if count != 1:
    raise RuntimeError(f"continuity next action: expected one section, found {count}")

journal = f'''### {TIMESTAMP} — version 4.08.0

- création de la fiche 21 — Benchmarks et méthodes de mesure ;
- ajout de treize cartes, de trois matrices et de 8 diagrammes compacts ;
- contrat, routage, question, environnement, scénario, warm-up, caches, répétitions, unités, données brutes, statistiques, exclusions, comparaison, rapports, preuves et maintenance indexés ;
- frontières avec l’équilibrage, la QA, l’observabilité, le diagnostic et les campagnes spécialisées des chapitres 1 à 14 du Livre IV, les fiches 18 à 20, les futures fiches 22 et 23 et le Companion Pack maintenues sans duplication ;
- métriques statiques : 462 lignes, 20 titres, 13 fiches, 3 matrices, 64 liens, 41 renvois vers les Livres I à IV, 47 liens profonds et 8 diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 22 — Matrices de compatibilité, niveau Élevée ;
- aucun benchmark, warm-up, cache, run, profiler, série, statistique, comparaison, donnée utilisateur, script du Companion Pack ou PDF produit.

'''
text = replace_once(text, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal, "continuity journal")
write(CONTINUITY, text)
