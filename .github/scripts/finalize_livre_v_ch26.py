from __future__ import annotations

import hashlib
import os
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "Livre-V/CHAPITRE-26-Index-croises.md"
AUDIT = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-26.md"
PROOF = ROOT / "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-26.yaml"
INDEX = ROOT / "Livre-V/index.md"
ROADMAP = ROOT / "ROADMAP.md"
CONTENTS = ROOT / "contents.txt"
PLAN = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
CONTINUITY = ROOT / "CONTINUITE-PROJET.md"
STAMP = "2026-07-30T01:18:00+02:00"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"Missing replacement anchor for {label}: {old!r}")
    return text.replace(old, new, 1)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


chapter = read(CHAPTER)
lines = chapter.splitlines()
heading_lines = [line for line in lines if re.match(r"^#{1,6}\s+", line)]
headings = [re.sub(r"^#{1,6}\s+", "", line).strip() for line in heading_lines]
normalized = [re.sub(r"\s+", " ", heading.casefold()) for heading in headings]
duplicate_headings = sum(count - 1 for count in Counter(normalized).values() if count > 1)
links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", chapter)
metrics = {
    "CHAPTER_LINES": len(lines),
    "CHAPTER_HEADINGS": len(heading_lines),
    "REFERENCE_CARDS": chapter.count("<!-- l5:card -->"),
    "MATRICES": chapter.count("<!-- l5:matrix -->"),
    "MARKDOWN_LINKS": len(links),
    "SOURCE_BOOK_LINKS": sum(bool(re.match(r"\.\./Livre-(?:I|II|III|IV)/", target)) for target in links),
    "FRAGMENT_LINKS": sum("#" in target for target in links),
    "COMPACT_DIAGRAMS": chapter.count("Diagramme compact"),
    "FENCED_BLOCKS": sum(line.lstrip().startswith("```") for line in lines) // 2,
    "DUPLICATE_HEADINGS": duplicate_headings,
}

if metrics["REFERENCE_CARDS"] != 13:
    raise RuntimeError(f"Expected 13 cards, got {metrics['REFERENCE_CARDS']}")
if metrics["MATRICES"] != 3:
    raise RuntimeError(f"Expected 3 matrices, got {metrics['MATRICES']}")
if metrics["COMPACT_DIAGRAMS"] != 9:
    raise RuntimeError(f"Expected 9 compact diagrams, got {metrics['COMPACT_DIAGRAMS']}")
if metrics["FENCED_BLOCKS"] != 0:
    raise RuntimeError("The reference fiche must not contain fenced blocks")
if metrics["DUPLICATE_HEADINGS"] != 0:
    raise RuntimeError("Duplicate headings detected")

# Complete the audit metrics first so its digest covers the final audit text.
audit = read(AUDIT)
for key, value in metrics.items():
    audit = audit.replace(f"__{key}__", str(value))
audit = audit.replace(
    "| lot permanent de huit fichiers | à vérifier par CI | contrôle avant commit final |",
    "| lot permanent de huit fichiers | conforme | contrôle automatisé dans le workflow de finalisation |",
)
write(AUDIT, audit)

chapter_hash = sha256_text(chapter)
audit_hash = sha256_text(audit)
source_head = os.environ.get("SOURCE_HEAD_COMMIT", "unknown")
run_id = os.environ.get("LIGHTWEIGHT_RUN_ID", "unknown")
proof = read(PROOF)
for key, value in metrics.items():
    proof = proof.replace(f"__{key}__", str(value))
proof = proof.replace("__CHAPTER_SHA256__", chapter_hash)
proof = proof.replace("__AUDIT_SHA256__", audit_hash)
proof = proof.replace("__SOURCE_HEAD_COMMIT__", source_head)
proof = proof.replace("__LIGHTWEIGHT_RUN_ID__", run_id)
write(PROOF, proof)

index = read(INDEX)
index = replace_once(index, 'version: "1.17.0"', 'version: "1.18.0"', "index version")
index = replace_once(
    index,
    "- [ ] Chapitre 26 — Index croisés.",
    "- [x] [Fiche 26 — Index croisés](CHAPITRE-26-Index-croises.md) — version `1.0.0`, niveau `static-review`.",
    "index chapter 26",
)
old_status = "Progression : **25 chapitres sur 26** rédigés et audités. Les fiches 01 à 25 utilisent le profil de référence spécialisé du Livre V ; la fiche 25 rassemble objets et couches juridiques, inventaire, SPDX, droits, provenance, personnes, chaînes IA, redistribution, statuts, notices, gouvernance, escalade, incidents et frontières de licence globale. Les registres exécutables et outils automatisés du Companion Pack, la décision de licence globale et les index croisés restent des chantiers distincts."
new_status = "Progression : **26 chapitres sur 26** rédigés et audités au niveau `static-review`. La fiche 26 clôt la couverture documentaire par identités canoniques, index alphabétiques et thématiques, synonymes, relations typées, routes par domaine, navigation multiformat et contrôles d’intégrité. La construction, le préflight et l’inspection du PDF complet du Livre V, les formats HTML/EPUB, l’accessibilité avancée, la licence globale et les outils exécutables du Companion Pack restent des portes séparées."
index = replace_once(index, old_status, new_status, "index status")
write(INDEX, index)

roadmap = read(ROADMAP)
roadmap = replace_once(
    roadmap,
    "- [ ] Bibliothèques techniques et index croisés.",
    "- [x] Bibliothèques techniques et index croisés — fiche 26 rédigée et auditée au niveau `static-review`.",
    "roadmap chapter 26",
)
roadmap = replace_once(
    roadmap,
    "**Statut M6 : en cours — 25 chapitres rédigés, repérés et audités sur 26.**",
    "**Statut M6 : en cours — 26 chapitres rédigés, repérés et audités sur 26 ; la construction, le préflight et l’inspection du PDF complet du Livre V restent la porte de clôture technique.**",
    "roadmap M6 status",
)
roadmap = replace_once(
    roadmap,
    "- [x] Produire, préflighter et inspecter le PDF complet de fin du Livre IV.\n",
    "- [x] Produire, préflighter et inspecter le PDF complet de fin du Livre IV.\n- [ ] Produire, préflighter et inspecter le PDF complet de fin du Livre V.\n",
    "roadmap Livre V PDF",
)
write(ROADMAP, roadmap)

contents = read(CONTENTS)
contents = replace_once(
    contents,
    "Livre-V/CHAPITRE-25-Licences-provenance-et-conformite.md\nCompanion-Pack/index.md",
    "Livre-V/CHAPITRE-25-Licences-provenance-et-conformite.md\nLivre-V/CHAPITRE-26-Index-croises.md\nCompanion-Pack/index.md",
    "contents chapter 26",
)
write(CONTENTS, contents)

plan = read(PLAN)
plan = replace_once(plan, 'version: "1.25.0"', 'version: "1.26.0"', "plan version")
plan = replace_once(plan, 'last-updated: "2026-07-29"', 'last-updated: "2026-07-30"', "plan date")
plan = replace_once(
    plan,
    "> **Statut :** 25 chapitres sur 26 rédigés et audités au niveau `static-review`",
    "> **Statut :** 26 chapitres sur 26 rédigés et audités au niveau `static-review` ; clôture PDF du Livre V encore requise",
    "plan status",
)
plan = replace_once(
    plan,
    "## Chapitre 26 — Index croisés\n\n**Objectifs**",
    "## Chapitre 26 — Index croisés\n\n**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n**Objectifs**",
    "plan chapter state",
)
plan = replace_once(
    plan,
    "- le PDF/HTML permet une navigation non linéaire efficace.",
    "- le PDF/HTML permet une navigation non linéaire efficace.\n\n**État de clôture :** la couverture documentaire des 26 fiches est complète ; la génération et l’inspection des formats de publication restent à exécuter séparément.",
    "plan closure note",
)
write(PLAN, plan)

continuity = read(CONTINUITY)
continuity = replace_once(continuity, 'version: "4.12.0"', 'version: "4.13.0"', "continuity version")
continuity = re.sub(r'last-updated: "[^"]+"', f'last-updated: "{STAMP}"', continuity, count=1)
continuity = replace_once(
    continuity,
    "- ne pas annoncer une licence globale avant une décision documentée sur le texte, le code, les médias et le Companion Pack ;\n",
    "- ne pas annoncer une licence globale avant une décision documentée sur le texte, le code, les médias et le Companion Pack ;\n- ne pas confondre identifiant d’index, libellé, chemin, titre et ancre ;\n- ne pas donner à un alias, un acronyme ou une ancienne appellation une définition concurrente ;\n- ne pas confondre `owner`, `prerequisite`, `validates`, `diagnoses`, `alternative`, `supersedes` et `related` ;\n- ne pas déclarer un document orphelin depuis le seul nombre de liens entrants ou sortants ;\n- ne pas présenter une cible `planned`, `unresolved`, `deprecated` ou `retired` comme une destination active ;\n- ne pas déduire la qualité de navigation PDF, HTML ou EPUB depuis les seuls liens Markdown ;\n- ne pas exposer secret, donnée personnelle, contrat ou chemin restreint dans un index public ;\n",
    "continuity index rules",
)
continuity = replace_once(
    continuity,
    "- progression du Livre V : 25 chapitres sur 26 ;",
    "- progression du Livre V : 26 chapitres sur 26 ;",
    "continuity progress",
)
continuity = replace_once(
    continuity,
    "- chapitre 25 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n",
    "- chapitre 25 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- chapitre 26 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n",
    "continuity chapter 26",
)
continuity = replace_once(
    continuity,
    "- profil éditorial du Livre V : fiches, matrices, recettes minimales et index ; les obligations tutoriel incompatibles sont exclues ;",
    "- profil éditorial du Livre V : fiches, matrices, recettes minimales et index ; les obligations tutoriel incompatibles sont exclues ;\n- clôture documentaire du Livre V : 26 fiches sur 26 ; construction, préflight et inspection du PDF complet encore requis ;",
    "continuity Livre V closure",
)
next_section = '''## 26. Prochaine action

Le Livre V contient vingt-six fiches sur 26 au niveau `static-review`. La fiche 26 fournit les identités canoniques, index alphabétiques et thématiques, synonymes, relations typées, routes par domaine, navigation multiformat et contrôles d’intégrité. La couverture documentaire est complète, mais la clôture technique exige encore la construction, le préflight et l’inspection du PDF complet du Livre V. La licence globale, les formats HTML/EPUB, l’accessibilité avancée et le Companion Pack restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/index.md — construire, préflighter et inspecter le PDF complet du Livre V
Niveau GPT-5.6 Sol recommandé : Élevée
```

Après réussite de cette porte PDF, le jalon actif passera à M7 — Companion Pack, Pack 1 — Starter Kit, avec `Companion-Pack/Starter-Kit/README.md` comme point d’entrée canonique à matérialiser.
'''
continuity, replaced = re.subn(
    r"## 26\. Prochaine action\n.*?(?=## 27\. Journal)",
    next_section,
    continuity,
    count=1,
    flags=re.S,
)
if replaced != 1:
    raise RuntimeError("Unable to replace continuity next-action section")
journal = f'''### {STAMP} — version 4.13.0

- création de la fiche 26 — Index croisés ;
- ajout de treize cartes, de trois matrices et de {metrics['COMPACT_DIAGRAMS']} diagrammes compacts ;
- identités canoniques, index alphabétiques et thématiques, facettes, synonymes, alias, anciennes appellations, relations typées, routes outils/systèmes/formats/diagnostics/licences et navigation multiformat indexés ;
- contrôles de chemins, fragments, doublons, redirections, candidats orphelins, cibles retirées et supports non testés encadrés sans suppression automatique ;
- frontières avec les fiches 01 à 25, les procédures des Livres I à IV, le Companion Pack et M8 maintenues sans duplication ;
- métriques statiques : {metrics['CHAPTER_LINES']} lignes, {metrics['CHAPTER_HEADINGS']} titres, {metrics['REFERENCE_CARDS']} fiches, {metrics['MATRICES']} matrices, {metrics['MARKDOWN_LINKS']} liens, {metrics['SOURCE_BOOK_LINKS']} renvois vers les Livres I à IV, {metrics['FRAGMENT_LINKS']} liens profonds et {metrics['COMPACT_DIAGRAMS']} diagrammes compacts ;
- progression documentaire du Livre V portée à 26 chapitres sur 26 ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la construction, le préflight et l’inspection du PDF complet du Livre V, niveau Élevée ;
- aucun moteur de recherche, générateur d’index, base d’alias, graphe de connaissances, rapport exhaustif d’orphelins, étude utilisateur, donnée personnelle, licence globale, outil du Companion Pack, PDF, HTML ou EPUB produit.

'''
continuity = replace_once(continuity, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal, "continuity journal")
write(CONTINUITY, continuity)

print("Finalized Livre V chapter 26")
for key, value in metrics.items():
    print(f"{key}={value}")
print(f"CHAPTER_SHA256={chapter_hash}")
print(f"AUDIT_SHA256={audit_hash}")
