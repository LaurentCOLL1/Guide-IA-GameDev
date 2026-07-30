---
title: "Companion Pack — Knowledge Base"
id: "CP-PACK-10-KNOWLEDGE-BASE"
status: "candidate"
version: "1.0.0"
lang: "fr-FR"
validation-status: "candidate"
redistribution-status: "pending-global-license"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Knowledge Base

Le Pack 10 fournit une base de connaissances synthétique pour lore, codex et RAG autour de **Project Asteria**. Il sépare les faits canoniques, les rumeurs, les souvenirs subjectifs et les références éditoriales.

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

## Interprétation

Les vecteurs de hachage sont un banc d'essai déterministe, pas des embeddings sémantiques de production. Aucun modèle, appel réseau, secret, donnée personnelle ou corpus tiers n'est inclus.

## Réserves

Aucun service RAG distant, modèle d'embeddings réel, base vectorielle externe, qualité de réponse produit, concurrence, volumétrie importante, publication, release ou licence globale n'est qualifié.
