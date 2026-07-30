---
title: "Companion Pack — Knowledge Base"
id: "CP-PACK-10-KNOWLEDGE-BASE"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-07-30T16:24:23+02:00"
validation-status: "runtime-tested-linux"
redistribution-status: "pending-global-license"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Knowledge Base

Le Pack 10 fournit une base de connaissances synthétique pour lore, codex et RAG autour de **Project Asteria**. Il sépare les faits canoniques, les rumeurs, les souvenirs subjectifs et les références éditoriales.

## État qualifié

| Élément | État |
|---|---|
| fichiers du Pack | 28 validés |
| documents synthétiques | 8 |
| fragments déterministes | 16 |
| tests Python | 32 réussis |
| reconstruction | deux index byte-identiques |
| recherche | lexicale, vectorielle locale et hybride |
| filtres | vérité et catégorie |
| suppression | document, fragments, postings, vecteurs et manifeste retirés |
| réindexation | identique à l'index élagué après retrait de la source |

## Fonctions

- corpus JSON versionné avec provenance et statut de vérité ;
- découpage déterministe avec chevauchement contrôlé ;
- index lexical BM25 simplifié et vecteurs de hachage locaux ;
- recherche hybride, lexicale ou vectorielle sans service externe ;
- filtres par statut de vérité et catégorie ;
- suppression complète d'un document dans documents, fragments, termes inversés, vecteurs et manifeste ;
- reconstruction byte-identique depuis les sources.

## Exemple

```powershell
$env:PYTHONPATH = ".\Companion-Pack\Knowledge-Base\python\src"
python .\Companion-Pack\Knowledge-Base\scripts\knowledge_base_cli.py build `
  --source-dir .\Companion-Pack\Knowledge-Base\corpus `
  --output .\dist\knowledge-base\index.json

python .\Companion-Pack\Knowledge-Base\scripts\knowledge_base_cli.py search `
  --index .\dist\knowledge-base\index.json `
  --query "héliostat flux" --top-k 3
```

## Qualification obtenue

Le run `30551507215` a validé 28 fichiers, huit documents synthétiques, 16 fragments, 32 tests Python, deux constructions byte-identiques, les recherches attendues, les filtres de vérité, la suppression complète de `AST-RUMOR-EMBER-QUEEN` et la reconstruction depuis un corpus où sa source avait été retirée.

Environnement : Ubuntu 24.04 et CPython `3.12.13`. PyYAML a été installé uniquement pour les validations documentaires transversales.

Empreinte logique de l'index : `f90186d922ef1c06be0bbf5dadc8af108a79e5ecd307ef5597142dd7f7cc4a9a`. SHA-256 du fichier JSON déterministe : `386475d454a868f28e60e3d6e2fb7cd475e7163e278770588ae406a5a68f8809`.

Artefact `8762968115`, digest `sha256:0f85a3d1dd8bf6728c963dd88adee17502a27280b9b7aea4a4515b2565cc8119`.

## Interprétation

Les vecteurs de hachage sont un banc d'essai déterministe, pas des embeddings sémantiques de production. Aucun modèle, appel réseau, secret, donnée personnelle ou corpus tiers n'est inclus.

## Réserves

Aucun service RAG distant, modèle d'embeddings réel, base vectorielle externe, qualité de réponse produit, concurrence, volumétrie importante, publication, release ou licence globale n'est qualifié.
