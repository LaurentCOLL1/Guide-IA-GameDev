from __future__ import annotations

import hashlib
import os
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "Livre-V/CHAPITRE-24-Checklists-de-production-et-de-publication.md"
AUDIT = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-24.md"
PROOF = ROOT / "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-24.yaml"
INDEX = ROOT / "Livre-V/index.md"
ROADMAP = ROOT / "ROADMAP.md"
CONTENTS = ROOT / "contents.txt"
PLAN = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
CONTINUITY = ROOT / "CONTINUITE-PROJET.md"
STAMP = "2026-07-29T23:31:00+02:00"


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
if metrics["COMPACT_DIAGRAMS"] != 8:
    raise RuntimeError(f"Expected 8 compact diagrams, got {metrics['COMPACT_DIAGRAMS']}")
if metrics["FENCED_BLOCKS"] != 0:
    raise RuntimeError("The reference fiche must not contain fenced blocks")
if metrics["DUPLICATE_HEADINGS"] != 0:
    raise RuntimeError("Duplicate headings detected")

# Complete the audit metrics first so its digest covers the final audit text.
audit = read(AUDIT)
for key, value in metrics.items():
    audit = audit.replace(f"__{key}__", str(value))
audit = audit.replace(
    "| lot permanent de huit fichiers | à vérifier par CI | contrôle automatisé avant commit final |",
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
index = replace_once(index, 'version: "1.15.0"', 'version: "1.16.0"', "index version")
index = replace_once(
    index,
    "- [ ] Chapitre 24 — Checklists de production et de publication.",
    "- [x] [Fiche 24 — Checklists de production et de publication](CHAPITRE-24-Checklists-de-production-et-de-publication.md) — version `1.0.0`, niveau `static-review`.",
    "index chapter 24",
)
old_status = "Progression : **23 chapitres sur 26** rédigés et audités. Les fiches 01 à 23 utilisent le profil de référence spécialisé du Livre V ; la fiche 23 rassemble contrat de comparaison, portes éliminatoires, critères, pondérations, scénarios, sources, mesures, préférences, coûts, migration, sensibilité, recommandations conditionnelles et maintenance. Les comparatifs exécutés et outils automatisés du Companion Pack, les checklists, la licence globale et les formats de publication avancés restent des chantiers distincts."
new_status = "Progression : **24 chapitres sur 26** rédigés et audités. Les fiches 01 à 24 utilisent le profil de référence spécialisé du Livre V ; la fiche 24 rassemble contrat d’item, obligation et statut, phases, preuves, checklists de préparation à publication, vues Solo/Studio, décisions de porte, dérogations, signatures et réouverture. Les formulaires exécutés et outils automatisés du Companion Pack, les licences et la conformité globale ainsi que les index croisés restent des chantiers distincts."
index = replace_once(index, old_status, new_status, "index status")
write(INDEX, index)

roadmap = read(ROADMAP)
roadmap = replace_once(
    roadmap,
    "- [x] Comparatifs des solutions — fiche 23 rédigée et auditée au niveau `static-review`.\n",
    "- [x] Comparatifs des solutions — fiche 23 rédigée et auditée au niveau `static-review`.\n- [x] Checklists de production et de publication — fiche 24 rédigée et auditée au niveau `static-review`.\n",
    "roadmap chapter 24",
)
roadmap = replace_once(
    roadmap,
    "**Statut M6 : en cours — 23 chapitres rédigés, repérés et audités sur 26.**",
    "**Statut M6 : en cours — 24 chapitres rédigés, repérés et audités sur 26.**",
    "roadmap status",
)
write(ROADMAP, roadmap)

contents = read(CONTENTS)
contents = replace_once(
    contents,
    "Livre-V/CHAPITRE-23-Comparatifs-des-solutions.md\nCompanion-Pack/index.md",
    "Livre-V/CHAPITRE-23-Comparatifs-des-solutions.md\nLivre-V/CHAPITRE-24-Checklists-de-production-et-de-publication.md\nCompanion-Pack/index.md",
    "contents chapter 24",
)
write(CONTENTS, contents)

plan = read(PLAN)
plan = replace_once(plan, 'version: "1.23.0"', 'version: "1.24.0"', "plan version")
plan = replace_once(
    plan,
    "> **Statut :** 23 chapitres sur 26 rédigés et audités au niveau `static-review`",
    "> **Statut :** 24 chapitres sur 26 rédigés et audités au niveau `static-review`",
    "plan status",
)
plan = replace_once(
    plan,
    "## Chapitre 24 — Checklists de production et de publication\n\n**Objectifs**",
    "## Chapitre 24 — Checklists de production et de publication\n\n**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n**Objectifs**",
    "plan chapter state",
)
write(PLAN, plan)

continuity = read(CONTINUITY)
continuity = replace_once(continuity, 'version: "4.10.0"', 'version: "4.11.0"', "continuity version")
continuity = re.sub(r'last-updated: "[^"]+"', f'last-updated: "{STAMP}"', continuity, count=1)
continuity = replace_once(
    continuity,
    "- ne pas conserver une cellule `reference` sans preuve consultable, date et propriétaire ;\n",
    "- ne pas conserver une cellule `reference` sans preuve consultable, date et propriétaire ;\n- ne pas confondre obligation, applicabilité, statut, preuve et décision d’une checklist ;\n- ne pas considérer une case cochée, un nom ou une CI verte comme preuve suffisante sans artefact propriétaire ;\n- ne pas masquer un item obligatoire pour faire passer une porte ;\n- ne pas accepter une dérogation sans portée, propriétaire, compensation et expiration ;\n- ne pas transférer automatiquement une checklist réussie vers un nouveau build, une nouvelle plateforme ou une nouvelle locale ;\n- ne pas réécrire une décision historique lors d’une réouverture ;\n",
    "continuity checklist rules",
)
continuity = replace_once(
    continuity,
    "- progression du Livre V : 23 chapitres sur 26 ;",
    "- progression du Livre V : 24 chapitres sur 26 ;",
    "continuity progress",
)
continuity = replace_once(
    continuity,
    "- chapitre 23 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n",
    "- chapitre 23 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- chapitre 24 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n",
    "continuity chapter 24",
)
next_section = f'''## 26. Prochaine action

Le Livre V contient vingt-quatre fiches sur 26 au niveau `static-review`. La fiche 24 fournit un contrat transversal pour items, obligations, applicabilité, preuves, phases, vues Solo/Studio, portes, dérogations, signatures et réouverture. Les checklists réellement instanciées, formulaires et automatisations du Companion Pack, décisions de licence et conformité, index croisés, approbations organisationnelles et balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-25-Licences-provenance-et-conformite.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 25 synthétisera licences du texte, du code, des modèles et des assets, séparera provenance, consentement, redistribution et obligations, fournira des matrices et modèles de registre, et signalera les situations exigeant un avis professionnel sans rendre de conseil juridique.
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
journal = f'''### {STAMP} — version 4.11.0

- création de la fiche 24 — Checklists de production et de publication ;
- ajout de treize cartes, de trois matrices et de {metrics['COMPACT_DIAGRAMS']} diagrammes compacts ;
- contrat d’item, obligation, statut, phase, preuve, préparation, intégration, QA, build, publication, vues Solo/Studio, décisions, dérogations, signatures et réouverture indexés ;
- frontières avec le Volume 0, les Livres II à IV, les fiches 21 à 23, les futures fiches 25 et 26 et le Companion Pack maintenues sans duplication ;
- métriques statiques : {metrics['CHAPTER_LINES']} lignes, {metrics['CHAPTER_HEADINGS']} titres, {metrics['REFERENCE_CARDS']} fiches, {metrics['MATRICES']} matrices, {metrics['MARKDOWN_LINKS']} liens, {metrics['SOURCE_BOOK_LINKS']} renvois vers les Livres I à IV, {metrics['FRAGMENT_LINKS']} liens profonds et {metrics['COMPACT_DIAGRAMS']} diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 25 — Licences, provenance et conformité, niveau Élevée ;
- aucune checklist, preuve d’exécution, dérogation, signature, approbation, publication, donnée utilisateur, outil du Companion Pack ou PDF produit.

'''
continuity = replace_once(continuity, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal, "continuity journal")
write(CONTINUITY, continuity)

print("Finalized Livre V chapter 24")
for key, value in metrics.items():
    print(f"{key}={value}")
print(f"CHAPTER_SHA256={chapter_hash}")
print(f"AUDIT_SHA256={audit_hash}")
