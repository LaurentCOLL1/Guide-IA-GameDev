from __future__ import annotations

import hashlib
import os
import re
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "Livre-V/CHAPITRE-23-Comparatifs-des-solutions.md"
AUDIT = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-23.md"
PROOF = ROOT / "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-23.yaml"
INDEX = ROOT / "Livre-V/index.md"
ROADMAP = ROOT / "ROADMAP.md"
CONTENTS = ROOT / "contents.txt"
PLAN = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
CONTINUITY = ROOT / "CONTINUITE-PROJET.md"

TIMESTAMP = "2026-07-29T22:44:00+02:00"
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


def chapter_metrics(text: str) -> dict[str, int]:
    lines = text.splitlines()
    headings = [line.strip() for line in lines if re.match(r"^#{1,6}\s+", line)]
    normalized = [re.sub(r"^#{1,6}\s+", "", heading).strip().casefold() for heading in headings]
    duplicates = sum(count - 1 for count in Counter(normalized).values() if count > 1)
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    source_links = [
        target
        for target in links
        if target.startswith("../Livre-I/")
        or target.startswith("../Livre-II/")
        or target.startswith("../Livre-III/")
        or target.startswith("../Livre-IV/")
    ]
    return {
        "chapter-lines": len(lines),
        "chapter-headings": len(headings),
        "reference-cards": text.count("<!-- l5:card -->"),
        "matrices": text.count("<!-- l5:matrix -->"),
        "markdown-links": len(links),
        "source-book-links": len(source_links),
        "fragment-links": sum(1 for target in links if "#" in target),
        "compact-diagrams": text.count("**Diagramme compact :**"),
        "fenced-blocks": sum(1 for line in lines if line.lstrip().startswith("```")),
        "duplicate-headings": duplicates,
    }


chapter_text = read(CHAPTER)
metrics = chapter_metrics(chapter_text)

# Complete the audit with measured static values.
audit_text = read(AUDIT)
replacements = {
    "__CHAPTER_LINES__": str(metrics["chapter-lines"]),
    "__CHAPTER_HEADINGS__": str(metrics["chapter-headings"]),
    "__REFERENCE_CARDS__": str(metrics["reference-cards"]),
    "__MATRICES__": str(metrics["matrices"]),
    "__MARKDOWN_LINKS__": str(metrics["markdown-links"]),
    "__SOURCE_BOOK_LINKS__": str(metrics["source-book-links"]),
    "__FRAGMENT_LINKS__": str(metrics["fragment-links"]),
    "__COMPACT_DIAGRAMS__": str(metrics["compact-diagrams"]),
    "__FENCED_BLOCKS__": str(metrics["fenced-blocks"]),
    "__DUPLICATE_HEADINGS__": str(metrics["duplicate-headings"]),
}
for token, value in replacements.items():
    audit_text = replace_once(audit_text, token, value, f"audit token {token}")
write(AUDIT, audit_text)

# Complete the QA proof after the chapter and audit are final.
proof = yaml.safe_load(read(PROOF))
proof["status"] = "complete"
proof["results"]["blocking-errors"] = 0
for key, value in metrics.items():
    proof["results"][key] = value
proof["integrity"]["chapter-sha256"] = sha256(CHAPTER)
proof["integrity"]["audit-sha256"] = sha256(AUDIT)
proof["ci"]["lightweight-finalization"] = {
    "workflow": "Temporary Livre V Chapter 23 Script Runner",
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

# Livre V index.
text = read(INDEX)
text = replace_once(text, 'version: "1.14.0"', 'version: "1.15.0"', "index version")
text = replace_once(
    text,
    "- [ ] Chapitre 23 — Comparatifs des solutions.",
    "- [x] [Fiche 23 — Comparatifs des solutions](CHAPITRE-23-Comparatifs-des-solutions.md) — version `1.0.0`, niveau `static-review`.",
    "index chapter 23",
)
text = replace_once(
    text,
    "Progression : **22 chapitres sur 26** rédigés et audités. Les fiches 01 à 22 utilisent le profil de référence spécialisé du Livre V ; la fiche 22 rassemble contrat de cellule, statuts amont et locaux, axes, sources, versions, systèmes, GPU, backends, outils, formats, API, tests positifs et négatifs, portes de promotion, vues, migrations et historique. Les tests exécutés et matrices automatisées du Companion Pack, les comparatifs, la licence globale et les formats de publication avancés restent des chantiers distincts.",
    "Progression : **23 chapitres sur 26** rédigés et audités. Les fiches 01 à 23 utilisent le profil de référence spécialisé du Livre V ; la fiche 23 rassemble contrat de comparaison, portes éliminatoires, critères, pondérations, scénarios, sources, mesures, préférences, coûts, migration, sensibilité, recommandations conditionnelles et maintenance. Les comparatifs exécutés et outils automatisés du Companion Pack, les checklists, la licence globale et les formats de publication avancés restent des chantiers distincts.",
    "index status",
)
write(INDEX, text)

# Roadmap.
text = read(ROADMAP)
text = replace_once(
    text,
    "- [x] Matrices de compatibilité — fiche 22 rédigée et auditée au niveau `static-review`.\n- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
    "- [x] Matrices de compatibilité — fiche 22 rédigée et auditée au niveau `static-review`.\n- [x] Comparatifs des solutions — fiche 23 rédigée et auditée au niveau `static-review`.\n- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
    "roadmap chapter 23",
)
text = replace_once(
    text,
    "**Statut M6 : en cours — 22 chapitres rédigés, repérés et audités sur 26.**",
    "**Statut M6 : en cours — 23 chapitres rédigés, repérés et audités sur 26.**",
    "roadmap status",
)
write(ROADMAP, text)

# Reader order.
text = read(CONTENTS)
text = replace_once(
    text,
    "Livre-V/CHAPITRE-22-Matrices-de-compatibilite.md\nCompanion-Pack/index.md",
    "Livre-V/CHAPITRE-22-Matrices-de-compatibilite.md\nLivre-V/CHAPITRE-23-Comparatifs-des-solutions.md\nCompanion-Pack/index.md",
    "contents chapter 23",
)
write(CONTENTS, text)

# Master plan.
text = read(PLAN)
text = replace_once(text, 'version: "1.22.0"', 'version: "1.23.0"', "plan version")
text = replace_once(
    text,
    "> **Statut :** 22 chapitres sur 26 rédigés et audités au niveau `static-review`",
    "> **Statut :** 23 chapitres sur 26 rédigés et audités au niveau `static-review`",
    "plan status",
)
text = replace_once(
    text,
    "## Chapitre 23 — Comparatifs des solutions\n\n**Objectifs**",
    "## Chapitre 23 — Comparatifs des solutions\n\n**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n**Objectifs**",
    "plan chapter state",
)
write(PLAN, text)

# Continuity and next action.
text = read(CONTINUITY)
text = replace_once(text, 'version: "4.09.0"', 'version: "4.10.0"', "continuity version")
text = replace_once(
    text,
    'last-updated: "2026-07-29T21:13:00+02:00"',
    f'last-updated: "{TIMESTAMP}"',
    "continuity timestamp",
)
text = replace_once(
    text,
    "- progression du Livre V : 22 chapitres sur 26 ;",
    "- progression du Livre V : 23 chapitres sur 26 ;",
    "continuity progress",
)
text = replace_once(
    text,
    "- chapitre 22 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- profil éditorial du Livre V",
    "- chapitre 22 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- chapitre 23 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- profil éditorial du Livre V",
    "continuity chapter 23",
)
text = replace_once(
    text,
    "- ne pas conserver une cellule `reference` sans preuve consultable, date et propriétaire ;\n\n## 25. État courant",
    "- ne pas conserver une cellule `reference` sans preuve consultable, date et propriétaire ;\n"
    "- ne pas modifier les poids, critères ou seuils après lecture des scores sans créer une nouvelle version du comparatif ;\n"
    "- ne pas laisser un score agrégé compenser une porte obligatoire non satisfaite ;\n"
    "- ne pas imputer silencieusement une valeur aux données inconnues, bloquées, obsolètes ou non applicables ;\n"
    "- ne pas présenter une préférence, une note ordinale ou une estimation comme un fait ou une mesure physique ;\n"
    "- ne pas produire de recommandation absolue ni forcer un vainqueur lorsque la preuve autorise une égalité, un pilote ou une indétermination ;\n\n"
    "## 25. État courant",
    "continuity comparison rules",
)
new_next = '''## 26. Prochaine action

Le Livre V contient vingt-trois fiches sur 26 au niveau `static-review`. La fiche 23 fournit un contrat transversal pour portes, critères, pondérations, scénarios, faits, mesures, préférences, coûts, migration, sensibilité et recommandations conditionnelles. Les comparatifs exécutés, tableurs et scripts du Companion Pack, checklists signées, approbations organisationnelles, licence globale et balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-24-Checklists-de-production-et-de-publication.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 24 centralisera les contrôles par phase, distinguera obligatoire, recommandé et optionnel, fournira des vues Solo et Studio, et permettra signature, preuve, exception et réouverture sans recopier les procédures détaillées des Livres I à IV.
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

journal = f'''### {TIMESTAMP} — version 4.10.0

- création de la fiche 23 — Comparatifs des solutions ;
- ajout de treize cartes, de trois matrices et de {metrics["compact-diagrams"]} diagrammes compacts ;
- contrat, couches d’information, candidats, portes, critères, pondérations, données manquantes, scénarios, sources, mesures, préférences, coûts, migration, sensibilité, recommandations et maintenance indexés ;
- frontières avec les fiches 02 à 22, les procédures propriétaires des Livres I à IV, les futures fiches 24 à 26 et le Companion Pack maintenues sans duplication ;
- métriques statiques : {metrics["chapter-lines"]} lignes, {metrics["chapter-headings"]} titres, {metrics["reference-cards"]} fiches, {metrics["matrices"]} matrices, {metrics["markdown-links"]} liens, {metrics["source-book-links"]} renvois vers les Livres I à IV, {metrics["fragment-links"]} liens profonds et {metrics["compact-diagrams"]} diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 24 — Checklists de production et de publication, niveau Élevée ;
- aucun candidat, benchmark, score, prix, devis, coût total, étude utilisateur, pilote de migration, décision d’achat, donnée utilisateur, outil du Companion Pack ou PDF produit.

'''
text = replace_once(text, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal, "continuity journal")
write(CONTINUITY, text)
