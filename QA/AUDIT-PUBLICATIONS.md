---
title: "Audit — Publications PDF, HTML et EPUB"
id: "QA-AUDIT-PUBLICATIONS-M8"
status: "candidate"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-07-30T21:37:00+02:00"
audit-level: "awaiting-runtime"
license: "CC-BY-SA-4.0"
---

# Audit — Publications PDF, HTML et EPUB

## Décision candidate

La chaîne multiformat est structurée autour d’une source unique et d’un orchestrateur commun. La décision finale reste suspendue à une exécution complète sur Linux, au préflight du PDF, à l’inspection des rendus et à EPUBCheck.

## Périmètre

- 162 sources lecteur ordonnées par `contents.txt` ;
- PDF A4 produit par Pandoc et XeLaTeX ;
- HTML5 autonome avec ressources incorporées ;
- EPUB 3 accompagné d’une validation EPUBCheck 5.3.0 ;
- licence, attribution et notices incluses dans les trois formats ;
- manifeste de sources, tailles et SHA-256 ;
- sorties conservées comme artefacts CI, sans release publique.

## Portes attendues

- toutes les sources existent et restent inchangées ;
- les trois artefacts sont non vides et accompagnés de leurs empreintes ;
- le PDF dépasse 4 000 pages, reste A4, non chiffré, extractible et utilise des polices incorporées ;
- le HTML possède une langue française, un titre, une table des matières, des identifiants uniques et des fragments internes résolus ;
- l’EPUB possède un conteneur valide et EPUBCheck ne signale aucune erreur ;
- les anciennes mentions de licence globale en attente sont absentes ;
- les validations documentaires et de licence restent vertes ;
- les fichiers temporaires de finalisation sont absents de l’arbre permanent.

## Réserves

- aucun PDF balisé ou conformité PDF/UA n’est revendiqué ;
- aucune compatibilité avec toutes les liseuses ou tous les navigateurs n’est revendiquée ;
- aucune release, publication commerciale, signature ou horodatage qualifié n’est produit ;
- l’inspection visuelle reste un échantillonnage, pas une preuve page par page.
