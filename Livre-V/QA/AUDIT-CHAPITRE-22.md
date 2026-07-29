---
title: "Audit — Livre V, fiche 22 : Matrices de compatibilité"
id: "DOC-L5-QA-AUDIT-CH22"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 22
last-verified: "2026-07-29T21:13:00+02:00"
audit-date: "2026-07-29T21:13:00+02:00"
audit-level: "static-review"
chapter-path: "Livre-V/CHAPITRE-22-Matrices-de-compatibilite.md"
validation-proof: "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-22.yaml"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit de la fiche 22 — Matrices de compatibilité

## 1. Décision

**Statut : accepté au niveau `static-review`, sous réserves explicites.**

La fiche respecte le profil spécialisé du Livre V : consultation non linéaire, contrat de cellule, légende multi-axes, matrices de routage et de promotion, liens profonds vers les autorités propriétaires, séparation entre déclaration amont, preuve locale et décision de la collection.

## 2. Périmètre revu

- contrat d’une cellule de compatibilité ;
- statuts de déclaration fournisseur, de preuve locale et de décision ;
- identité, axes, granularité, direction et portée ;
- sources officielles, communautaires, rapports et artefacts ;
- versions exactes, commits, digests, plages et compatibilité directionnelle ;
- routage par outils, moteurs IA, modèles, formats, données, assets, réseau, exports, mods et archives ;
- systèmes, shells, conteneurs, chemins, permissions et locales ;
- CPU, GPU, pilotes, API graphiques, backends, précision et offload ;
- outils, runtimes, plugins, extensions et dépendances transitives ;
- formats, import, export, conversion, migration et round-trip ;
- API, protocoles, données persistantes, réseau et modding ;
- tests positifs, négatifs, bloqués, invalides, obsolètes et non applicables ;
- portes de promotion, dégradation, référence, laboratoire et retrait ;
- forme des matrices, registre canonique, vues dérivées et accessibilité ;
- migration, rupture, repli, dépréciation, historique et responsabilités.

## 3. Frontières vérifiées

La fiche ne reprend pas les procédures détaillées des propriétaires :

- politique normative et niveaux C0 à C4 : Volume 0, chapitre 9 ;
- outils et commandes minimales : fiche 03 ;
- moteurs, backends et accélérations : fiche 04 ;
- modèles de langage, visuels et audio : fiches 05 à 07 ;
- formats, schémas et conversions : fiches 13 et 14 ;
- production, import et validation graphique/audio : fiches 18 et 19 et Livre III ;
- diagnostic et reproduction : fiche 20 et Livre IV, chapitre 4 ;
- protocoles de mesure : fiche 21 ;
- données, sauvegardes, API et réseau : Livre II ;
- exports, packaging, modding et archivage : Livre IV ;
- comparaison et recommandation : future fiche 23 ;
- matrice centrale exécutable, fixtures et rapports : Companion Pack.

## 4. Conformité au profil Livre V

- `document-format: "reference-cards"` présent ;
- treize marqueurs `<!-- l5:card -->` ;
- trois marqueurs `<!-- l5:matrix -->` ;
- index express en tête ;
- réponses rapides, limites, portes et décisions visibles ;
- tables orientées recherche et gouvernance ;
- liens profonds vers les sources propriétaires ;
- absence de bloc de code et de commande exécutable ;
- absence de structure tutoriel complète ;
- séparation entre information documentaire, test, runtime, sécurité, qualité et décision.

## 5. Revue sémantique

### 5.1 Compatibilité non binaire

La fiche refuse un booléen unique. Elle sépare déclaration amont, preuve locale et décision de la collection, avec des statuts explicites pour inconnu, non évalué, bloqué, obsolète et non applicable.

### 5.2 Absence de test

`not_assessed`, `not_run` et `blocked` ne deviennent jamais une incompatibilité. Une cellule vide est interdite lorsqu’elle pourrait être interprétée comme un échec.

### 5.3 Preuve positive et négative

Un test réussi reste borné à une opération et un environnement. Une incompatibilité exige attendu, versions, environnement, reproduction ou source autoritative et artefacts consultables.

### 5.4 Direction et granularité

Lecture, écriture, import, export, migration, éditeur, build et round-trip sont des relations distinctes. Une réussite dans un sens n’autorise pas le sens inverse.

### 5.5 Versions et temporalité

Les versions exactes, commits, digests, schémas, dates et événements invalidants sont conservés. Une preuve ancienne passe à `stale` au lieu de rester implicitement actuelle.

### 5.6 Matériel et backends

GPU détecté, mémoire allouée et backend affiché ne prouvent pas l’exécution dominante. Matériel, pilote, API, backend, modèle, mémoire, qualité et repli possèdent des contrôles distincts.

### 5.7 Formats et données

Parse, schéma, sémantique, lecture, écriture, import, export, migration et round-trip sont séparés. Les pertes autorisées et les invariants métier restent visibles.

### 5.8 Gouvernance

Chaque cellule active possède propriétaire, preuve, date, expiration et historique. Les changements de sécurité, licence, version, pilote ou dépendance peuvent dégrader un statut même si un test fonctionnel ancien réussissait.

## 6. Vérifications techniques prévues

La validation légère doit contrôler :

1. front matter, identifiant, dates, statut et chemin d’audit ;
2. structure Markdown, titres et doublons ;
3. résolution des fichiers et fragments locaux ;
4. marqueurs de cartes et matrices du Livre V ;
5. densité des renvois vers les Livres I à IV et Volume 0 ;
6. absence de blocs non expliqués ;
7. présence et cohérence des repères d’utilisation ;
8. couverture des contextes ;
9. absence de PDF ;
10. cohérence du lot permanent de huit fichiers.

## 7. Métriques finales

Les métriques statiques du chapitre stabilisé, ainsi que les empreintes SHA-256 du chapitre et de l’audit, sont calculées par le finaliseur et enregistrées dans la preuve QA finale.

## 8. Réserves

- aucun OS, shell, système de fichiers, conteneur ou runner n’a été qualifié ;
- aucun CPU, GPU, pilote, API graphique, backend, précision ou offload n’a été testé ;
- aucun outil, runtime, plugin, extension, dépendance ou image de conteneur n’a été installé ou lancé ;
- aucun format, import, export, conversion, migration ou round-trip n’a été exécuté ;
- aucune API, sauvegarde, base, connexion réseau, synchronisation ou mod n’a été testé ;
- aucune cellule runtime, matrice exécutable, suite de compatibilité ou rapport automatisé n’a été produit ;
- aucune compatibilité, incompatibilité, référence, dérogation ou qualification de plateforme réelle n’a été approuvée ;
- aucune source externe n’a été requalifiée au-delà des références déjà présentes dans le dépôt ;
- aucune donnée joueur, donnée personnelle, secret, licence personnalisée ou artefact confidentiel n’a été traité ;
- aucun outil du Companion Pack et aucun PDF n’a été produit.

## 9. Conclusion

La fiche peut être intégrée comme contrat documentaire transversal des matrices de compatibilité. Toute promotion ultérieure devra citer la relation exacte, les versions, la direction, l’environnement, la déclaration amont, le test propriétaire, les artefacts, les limites, le repli, le responsable et la date de réévaluation.
