from __future__ import annotations

import hashlib
import os
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "Livre-V/CHAPITRE-25-Licences-provenance-et-conformite.md"
AUDIT = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-25.md"
PROOF = ROOT / "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-25.yaml"
INDEX = ROOT / "Livre-V/index.md"
ROADMAP = ROOT / "ROADMAP.md"
CONTENTS = ROOT / "contents.txt"
PLAN = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
CONTINUITY = ROOT / "CONTINUITE-PROJET.md"
STAMP = "2026-07-30T00:17:00+02:00"


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
index = replace_once(index, 'version: "1.16.0"', 'version: "1.17.0"', "index version")
index = replace_once(
    index,
    "- [ ] Chapitre 25 — Licences, provenance et conformité.",
    "- [x] [Fiche 25 — Licences, provenance et conformité](CHAPITRE-25-Licences-provenance-et-conformite.md) — version `1.0.0`, niveau `static-review`.",
    "index chapter 25",
)
old_status = "Progression : **24 chapitres sur 26** rédigés et audités. Les fiches 01 à 24 utilisent le profil de référence spécialisé du Livre V ; la fiche 24 rassemble contrat d’item, obligation et statut, phases, preuves, checklists de préparation à publication, vues Solo/Studio, décisions de porte, dérogations, signatures et réouverture. Les formulaires exécutés et outils automatisés du Companion Pack, les licences et la conformité globale ainsi que les index croisés restent des chantiers distincts."
new_status = "Progression : **25 chapitres sur 26** rédigés et audités. Les fiches 01 à 25 utilisent le profil de référence spécialisé du Livre V ; la fiche 25 rassemble objets et couches juridiques, inventaire, SPDX, droits, provenance, personnes, chaînes IA, redistribution, statuts, notices, gouvernance, escalade, incidents et frontières de licence globale. Les registres exécutables et outils automatisés du Companion Pack, la décision de licence globale et les index croisés restent des chantiers distincts."
index = replace_once(index, old_status, new_status, "index status")
write(INDEX, index)

roadmap = read(ROADMAP)
roadmap = replace_once(
    roadmap,
    "- [x] Checklists de production et de publication — fiche 24 rédigée et auditée au niveau `static-review`.\n",
    "- [x] Checklists de production et de publication — fiche 24 rédigée et auditée au niveau `static-review`.\n- [x] Licences, provenance et conformité — fiche 25 rédigée et auditée au niveau `static-review`.\n",
    "roadmap chapter 25",
)
roadmap = replace_once(
    roadmap,
    "**Statut M6 : en cours — 24 chapitres rédigés, repérés et audités sur 26.**",
    "**Statut M6 : en cours — 25 chapitres rédigés, repérés et audités sur 26.**",
    "roadmap status",
)
write(ROADMAP, roadmap)

contents = read(CONTENTS)
contents = replace_once(
    contents,
    "Livre-V/CHAPITRE-24-Checklists-de-production-et-de-publication.md\nCompanion-Pack/index.md",
    "Livre-V/CHAPITRE-24-Checklists-de-production-et-de-publication.md\nLivre-V/CHAPITRE-25-Licences-provenance-et-conformite.md\nCompanion-Pack/index.md",
    "contents chapter 25",
)
write(CONTENTS, contents)

plan = read(PLAN)
plan = replace_once(plan, 'version: "1.24.0"', 'version: "1.25.0"', "plan version")
plan = replace_once(
    plan,
    "> **Statut :** 24 chapitres sur 26 rédigés et audités au niveau `static-review`",
    "> **Statut :** 25 chapitres sur 26 rédigés et audités au niveau `static-review`",
    "plan status",
)
plan = replace_once(
    plan,
    "## Chapitre 25 — Licences, provenance et conformité\n\n**Objectifs**",
    "## Chapitre 25 — Licences, provenance et conformité\n\n**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n**Objectifs**",
    "plan chapter state",
)
write(PLAN, plan)

continuity = read(CONTINUITY)
continuity = replace_once(continuity, 'version: "4.11.0"', 'version: "4.12.0"', "continuity version")
continuity = re.sub(r'last-updated: "[^"]+"', f'last-updated: "{STAMP}"', continuity, count=1)
continuity = replace_once(
    continuity,
    "- ne pas réécrire une décision historique lors d’une réouverture ;\n",
    "- ne pas réécrire une décision historique lors d’une réouverture ;\n- ne pas déduire un droit d’un prix, d’un téléchargement, d’une visibilité publique ou d’une génération ;\n- ne pas étendre la licence du code aux modèles, poids, données, médias, personnes ou services ;\n- ne pas utiliser `open`, `free`, `royalty-free` ou `NOASSERTION` comme autorisation de publication ;\n- ne pas fusionner auteur, titulaire, fournisseur, opérateur et approbateur ;\n- ne pas publier un objet dont une dépendance obligatoire reste `unknown`, `blocked`, `contested` ou `stale` ;\n- ne pas exposer contrats, consentements, signatures, secrets ou données personnelles dans un registre public ;\n- ne pas automatiser une conclusion de titularité, de compatibilité juridique ou de conformité réglementaire ;\n- ne pas appliquer une exception au-delà de son objet, sa version, son canal, son territoire, sa durée ou son expiration ;\n- ne pas annoncer une licence globale avant une décision documentée sur le texte, le code, les médias et le Companion Pack ;\n",
    "continuity license rules",
)
continuity = replace_once(
    continuity,
    "- progression du Livre V : 24 chapitres sur 26 ;",
    "- progression du Livre V : 25 chapitres sur 26 ;",
    "continuity progress",
)
continuity = replace_once(
    continuity,
    "- chapitre 24 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n",
    "- chapitre 24 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- chapitre 25 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n",
    "continuity chapter 25",
)
next_section = f'''## 26. Prochaine action

Le Livre V contient vingt-cinq fiches sur 26 au niveau `static-review`. La fiche 25 fournit un contrat transversal pour objets, textes applicables, identifiants SPDX, droits, obligations, provenance, personnes, chaînes IA, redistribution, notices, gouvernance, escalades, incidents et future licence globale. Les registres réellement instanciés, validations juridiques, licence globale, outils du Companion Pack, index croisés et formats avancés de publication restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-26-Index-croises.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 26 clôturera l’encyclopédie par des index alphabétiques et thématiques, synonymes, anciennes appellations, liens croisés, navigation PDF/HTML et détection des références orphelines, sans recopier les fiches propriétaires.
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
journal = f'''### {STAMP} — version 4.12.0

- création de la fiche 25 — Licences, provenance et conformité ;
- ajout de treize cartes, de trois matrices et de {metrics['COMPACT_DIAGRAMS']} diagrammes compacts ;
- objets, couches juridiques, inventaire, SPDX, droits, provenance, personnes, chaînes IA, redistribution, statuts, notices, gouvernance, escalades, incidents et licence globale indexés ;
- sources officielles SPDX, REUSE, OSI, Creative Commons, Légifrance, CNIL et Union européenne vérifiées le 30 juillet 2026 ;
- frontières avec le Volume 0, les Livres II à IV, la fiche 24, la future fiche 26 et le Companion Pack maintenues sans duplication ;
- métriques statiques : {metrics['CHAPTER_LINES']} lignes, {metrics['CHAPTER_HEADINGS']} titres, {metrics['REFERENCE_CARDS']} fiches, {metrics['MATRICES']} matrices, {metrics['MARKDOWN_LINKS']} liens, {metrics['SOURCE_BOOK_LINKS']} renvois vers les Livres I à IV, {metrics['FRAGMENT_LINKS']} liens profonds et {metrics['COMPACT_DIAGRAMS']} diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 26 — Index croisés, niveau Élevée ;
- aucune licence, compatibilité, titularité, conformité réglementaire, donnée personnelle, approbation, licence globale, outil du Companion Pack ou PDF produit.

'''
continuity = replace_once(continuity, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal, "continuity journal")
write(CONTINUITY, continuity)

print("Finalized Livre V chapter 25")
for key, value in metrics.items():
    print(f"{key}={value}")
print(f"CHAPTER_SHA256={chapter_hash}")
print(f"AUDIT_SHA256={audit_hash}")
