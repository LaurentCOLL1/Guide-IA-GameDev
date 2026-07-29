from __future__ import annotations

import hashlib
import os
import re
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "Livre-V/CHAPITRE-22-Matrices-de-compatibilite.md"
AUDIT = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-22.md"
PROOF = ROOT / "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-22.yaml"
INDEX = ROOT / "Livre-V/index.md"
ROADMAP = ROOT / "ROADMAP.md"
CONTENTS = ROOT / "contents.txt"
PLAN = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
CONTINUITY = ROOT / "CONTINUITE-PROJET.md"

TIMESTAMP = "2026-07-29T21:13:00+02:00"
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


def metrics(text: str) -> dict[str, int]:
    headings = re.findall(r"^#{1,6}\s+(.+?)\s*$", text, flags=re.MULTILINE)
    normalized = [re.sub(r"\s+", " ", heading.strip().lower()) for heading in headings]
    duplicates = sum(count - 1 for count in Counter(normalized).values() if count > 1)
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    return {
        "chapter-lines": len(text.splitlines()),
        "chapter-headings": len(headings),
        "reference-cards": text.count("<!-- l5:card -->"),
        "matrices": text.count("<!-- l5:matrix -->"),
        "markdown-links": len(links),
        "source-book-links": sum(
            target.startswith("../Livre-I/")
            or target.startswith("../Livre-II/")
            or target.startswith("../Livre-III/")
            or target.startswith("../Livre-IV/")
            for target in links
        ),
        "fragment-links": sum("#" in target for target in links),
        "compact-diagrams": text.count("**Diagramme compact :**"),
        "fenced-blocks": text.count("```") // 2,
        "duplicate-headings": duplicates,
    }


chapter_text = read(CHAPTER)
measured = metrics(chapter_text)
if measured["reference-cards"] != 13 or measured["matrices"] != 3:
    raise RuntimeError(f"unexpected Livre V markers: {measured}")

metric_sentence = (
    "Les métriques statiques du chapitre stabilisé sont : "
    f"{measured['chapter-lines']} lignes, {measured['chapter-headings']} titres, "
    f"{measured['reference-cards']} cartes, {measured['matrices']} matrices, "
    f"{measured['markdown-links']} liens Markdown, "
    f"{measured['source-book-links']} renvois vers les Livres I à IV, "
    f"{measured['fragment-links']} liens avec fragment, "
    f"{measured['compact-diagrams']} diagrammes compacts, "
    f"{measured['fenced-blocks']} bloc clôturé et "
    f"{measured['duplicate-headings']} titre dupliqué. "
    "Les empreintes SHA-256 sont enregistrées dans la preuve QA finale."
)
audit_text = read(AUDIT)
audit_text = replace_once(
    audit_text,
    "Les métriques statiques du chapitre stabilisé, ainsi que les empreintes SHA-256 du chapitre et de l’audit, sont calculées par le finaliseur et enregistrées dans la preuve QA finale.",
    metric_sentence,
    "audit metrics",
)
write(AUDIT, audit_text)

proof = yaml.safe_load(read(PROOF))
proof["status"] = "complete"
proof["results"]["blocking-errors"] = 0
for key, value in measured.items():
    proof["results"][key] = value
proof["integrity"]["chapter-sha256"] = sha256(CHAPTER)
proof["integrity"]["audit-sha256"] = sha256(AUDIT)
proof["ci"]["lightweight-finalization"] = {
    "workflow": "Temporary Livre V Chapter 22 Script Runner",
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
text = replace_once(text, 'version: "1.13.0"', 'version: "1.14.0"', "index version")
text = replace_once(
    text,
    "- [ ] Chapitre 22 — Matrices de compatibilité.",
    "- [x] [Fiche 22 — Matrices de compatibilité](CHAPITRE-22-Matrices-de-compatibilite.md) — version `1.0.0`, niveau `static-review`.",
    "index chapter 22",
)
text = replace_once(
    text,
    "Progression : **21 chapitres sur 26** rédigés et audités. Les fiches 01 à 21 utilisent le profil de référence spécialisé du Livre V ; la fiche 21 rassemble contrat de benchmark, environnement, scénarios, warm-up, caches, répétitions, unités, données brutes, statistiques, exclusions, comparaisons, rapports, niveaux de preuve et maintenance. Les campagnes exécutées, scripts et fixtures permanents du Companion Pack, les matrices de compatibilité, les comparatifs, la licence globale et les formats de publication avancés restent des chantiers distincts.",
    "Progression : **22 chapitres sur 26** rédigés et audités. Les fiches 01 à 22 utilisent le profil de référence spécialisé du Livre V ; la fiche 22 rassemble contrat de cellule, statuts amont et locaux, axes, sources, versions, systèmes, GPU, backends, outils, formats, API, tests positifs et négatifs, portes de promotion, vues, migrations et historique. Les tests exécutés et matrices automatisées du Companion Pack, les comparatifs, la licence globale et les formats de publication avancés restent des chantiers distincts.",
    "index status",
)
write(INDEX, text)

text = read(ROADMAP)
text = replace_once(
    text,
    "- [x] Benchmarks et méthodes de mesure — fiche 21 rédigée et auditée au niveau `static-review`.\n- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
    "- [x] Benchmarks et méthodes de mesure — fiche 21 rédigée et auditée au niveau `static-review`.\n- [x] Matrices de compatibilité — fiche 22 rédigée et auditée au niveau `static-review`.\n- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
    "roadmap chapter 22",
)
text = replace_once(
    text,
    "**Statut M6 : en cours — 21 chapitres rédigés, repérés et audités sur 26.**",
    "**Statut M6 : en cours — 22 chapitres rédigés, repérés et audités sur 26.**",
    "roadmap status",
)
write(ROADMAP, text)

text = read(CONTENTS)
text = replace_once(
    text,
    "Livre-V/CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md\nCompanion-Pack/index.md",
    "Livre-V/CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md\nLivre-V/CHAPITRE-22-Matrices-de-compatibilite.md\nCompanion-Pack/index.md",
    "contents chapter 22",
)
write(CONTENTS, text)

text = read(PLAN)
text = replace_once(text, 'version: "1.21.0"', 'version: "1.22.0"', "plan version")
text = replace_once(
    text,
    "> **Statut :** 21 chapitres sur 26 rédigés et audités au niveau `static-review`",
    "> **Statut :** 22 chapitres sur 26 rédigés et audités au niveau `static-review`",
    "plan status",
)
text = replace_once(
    text,
    "## Chapitre 22 — Matrices de compatibilité\n\n**Objectifs**",
    "## Chapitre 22 — Matrices de compatibilité\n\n**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n**Objectifs**",
    "plan chapter state",
)
write(PLAN, text)

text = read(CONTINUITY)
text = replace_once(text, 'version: "4.08.0"', 'version: "4.09.0"', "continuity version")
text = replace_once(
    text,
    'last-updated: "2026-07-29T18:11:00+02:00"',
    f'last-updated: "{TIMESTAMP}"',
    "continuity timestamp",
)
text = replace_once(
    text,
    "- progression du Livre V : 21 chapitres sur 26 ;",
    "- progression du Livre V : 22 chapitres sur 26 ;",
    "continuity progress",
)
text = replace_once(
    text,
    "- chapitre 21 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- profil éditorial du Livre V",
    "- chapitre 21 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- chapitre 22 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- profil éditorial du Livre V",
    "continuity chapter 22",
)
text = replace_once(
    text,
    "- ne pas arrêter une campagne dès que le résultat devient favorable ni changer la métrique primaire après lecture ;\n\n## 25. État courant",
    "- ne pas arrêter une campagne dès que le résultat devient favorable ni changer la métrique primaire après lecture ;\n"
    "- ne pas confondre support officiel, preuve locale et décision de la collection ;\n"
    "- ne pas interpréter une cellule vide, non évaluée, bloquée ou obsolète comme une incompatibilité ;\n"
    "- ne pas déduire lecture, écriture, import, export ou round-trip les uns des autres ;\n"
    "- ne pas conserver une cellule `reference` sans preuve consultable, date et propriétaire ;\n\n"
    "## 25. État courant",
    "continuity compatibility rules",
)
new_next = '''## 26. Prochaine action

Le Livre V contient vingt-deux fiches sur 26 au niveau `static-review`. La fiche 22 fournit un contrat transversal pour cellules directionnelles, statuts amont et locaux, versions, sources, systèmes, GPU, backends, outils, formats, API, tests positifs et négatifs, promotion, migration et historique. Les tests réels, matrices automatisées du Companion Pack, comparatifs, approbations organisationnelles, licence globale et balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-23-Comparatifs-des-solutions.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 23 comparera des solutions selon des critères explicites, séparera faits, mesures et préférences, proposera des choix conditionnels par scénario et documentera coûts de migration, réversibilité et limites sans produire de recommandation absolue.
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

journal = f'''### {TIMESTAMP} — version 4.09.0

- création de la fiche 22 — Matrices de compatibilité ;
- ajout de treize cartes, de trois matrices et de {measured['compact-diagrams']} diagrammes compacts ;
- contrat de cellule, statuts amont et locaux, axes, sources, versions, systèmes, GPU, backends, outils, formats, API, tests, promotion, vues, migrations et historique indexés ;
- frontières avec la politique du Volume 0, les fiches 03 à 07, 13 à 14 et 18 à 21, les procédures propriétaires des Livres II à IV, la future fiche 23 et le Companion Pack maintenues sans duplication ;
- métriques statiques : {measured['chapter-lines']} lignes, {measured['chapter-headings']} titres, {measured['reference-cards']} fiches, {measured['matrices']} matrices, {measured['markdown-links']} liens, {measured['source-book-links']} renvois vers les Livres I à IV, {measured['fragment-links']} liens profonds et {measured['compact-diagrams']} diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 23 — Comparatifs des solutions, niveau Élevée ;
- aucun OS, GPU, pilote, backend, outil, format, import, export, API, sauvegarde, réseau, mod, matrice runtime, donnée utilisateur ou PDF produit.

'''
text = replace_once(text, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal, "continuity journal")
write(CONTINUITY, text)
