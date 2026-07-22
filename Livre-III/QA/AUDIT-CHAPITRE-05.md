---
title: "Audit du Livre III — Chapitre 5"
id: "DOC-L3-QA-AUDIT-CH05"
status: "complete"
version: "1.0.0"
chapter-id: "DOC-L3-CH05"
chapter-version: "1.0.0"
audit-level: "static-review"
audit-date: "2026-07-22T23:35:44+02:00"
last-verified: "2026-07-22T23:35:44+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 5 — Provenance, licences et validation des assets

## 1. Porte de création

La création intervient après la fusion, la clôture QA et le nettoyage opérationnel du chapitre 4. `CONTINUITE-PROJET.md` version `3.34.1` désignait explicitement le chemin `Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md` et recommandait un niveau élevé.

Avant rédaction, le dépôt ne contenait ni chapitre 5, ni audit, ni preuve finale, ni branche `ch05` ou `provenance`, ni pull request ouverte concurrente. La branche `docs/livre-iii-ch05-provenance-licences` a donc été créée depuis `main` sans écraser de travail existant.

Le chemin, l’intention, les résultats d’apprentissage, les sept contenus obligatoires, les cinq livrables, les parcours Solo et Studio, les critères de validation et la frontière ont été comparés à `plans/LIVRE-III-PLAN-MAITRE.md`.

Le texte lecteur ne contient ni recommandation de raisonnement, ni procédure QA interne, ni chemin du chapitre suivant.

## 2. Résultats documentaires

- lignes finales : **1 555** ;
- titres Markdown contrôlés hors blocs : **63** ;
- sections principales numérotées : **44** ;
- blocs de code, données ou structures : **36** ;
- marqueurs d’explication : **36** ;
- explications structurées hors section d’erreurs : **16** ;
- cas d’erreurs détaillés : **10** ;
- exemples fautifs expliqués : **10** ;
- corrections expliquées : **10** ;
- métadonnée de processus de raisonnement : **0** ;
- instruction de prochaine étape dans le texte lecteur : **0**.

Les métriques de doublons et de blocs significatifs seront fermées par les validations documentaires permanentes avant la preuve finale.

## 3. Complétude contre le plan maître

Le chapitre couvre :

- distinction entre droit d’auteur, droits patrimoniaux, droit moral, droits voisins, licence, cession, consentement, marque, droit à l’image et données personnelles ;
- séparation entre auteur, titulaire, fournisseur, acquéreur et responsable de publication ;
- catégories `internal-original`, `commissioned`, `purchased`, `open-licensed`, `public-domain-claimed`, `generated`, `captured`, `user-submitted`, `mixed` et `unknown` ;
- identifiants stables et versions immuables ;
- fiche d’asset détaillée ;
- registre central de provenance ;
- chaîne append-only de transformations ;
- paquet de preuves et empreintes ;
- matrice des licences et restrictions ;
- identifiants SPDX et `LicenseRef-...` ;
- règles de réutilisation Creative Commons ;
- créations internes, commandes, prestataires, boutiques, services, assets gratuits, ouverts et revendiqués comme domaine public ;
- code, extensions, modèles, poids, datasets, entrées, workflows et sorties d’une chaîne IA ;
- contribution humaine et revue de similarité ;
- photos, textures, scans, photogrammétrie, polices, musiques, sons et enregistrements ;
- voix, artistes-interprètes, clonage, entraînement, image, visage, mocap et données personnelles ;
- marques, logos, patrimoine, cultures et contenus sensibles ;
- dépendances transitives ;
- contrôles automatiques minimaux ;
- statuts de blocage et porte de publication ;
- procédure de retrait et remplacement ;
- incident, conservation, accès, sécurité et confidentialité ;
- parcours Solo et Studio ;
- mesures de pilotage ;
- dix erreurs fréquentes avec contre-exemple et correction ;
- synthèse opérationnelle pour `Project Asteria`.

Les cinq livrables du plan maître sont matérialisés dans le chapitre : registre de provenance, modèle de fiche d’asset, matrice des licences, procédure de retrait et remplacement, règles de blocage et contrôles minimaux.

## 4. Frontières contrôlées

- le chapitre organise une politique de production et de preuve ;
- il ne fournit pas d’avis juridique personnalisé ;
- il ne conclut pas qu’un achat, une commande, une facture, une gratuité ou une génération accorde automatiquement les droits nécessaires ;
- il ne transforme pas un statut automatisé en garantie juridique ;
- il ne présente pas une empreinte comme preuve de validité d’un contrat ;
- il ne présente pas `royalty-free`, `free`, `open` ou `AI-generated` comme licences ;
- il ne fusionne pas droit d’auteur, consentement, données personnelles, droit à l’image, droits voisins et marques ;
- il ne publie pas de contrat, identité, signature ou donnée sensible dans le registre général ;
- il ne prétend pas qu’une licence ouverte couvre automatiquement les droits de tiers ;
- il ne revendique aucun registre, contrat, consentement, asset ou contrôle runtime réellement matérialisé ;
- il ne construit aucun PDF intermédiaire.

## 5. Vérification juridique et institutionnelle

La revue du 22 juillet 2026 a utilisé des sources institutionnelles et des standards officiels :

- le Code de la propriété intellectuelle français distingue la naissance du droit d’auteur du seul fait de la création et l’existence d’un contrat de service ;
- les transmissions de droits exigent un écrit dans les cas prévus et une délimitation des droits et du domaine d’exploitation ;
- les artistes-interprètes disposent de droits propres sur leur nom, leur interprétation et certaines utilisations de leur prestation ;
- le Code civil protège la vie privée ;
- la CNIL inclut notamment la voix et l’image parmi les informations pouvant identifier une personne ;
- SPDX fournit des identifiants courts, textes et liens canoniques pour des licences et exceptions ;
- Creative Commons distingue Attribution, ShareAlike, NonCommercial et NoDerivatives, et rappelle que seule une personne contrôlant les droits peut appliquer une licence ;
- l’OMPI traite la licence comme une manière d’exercer des droits exclusifs, et non comme un abandon automatique du droit d’auteur ;
- le cadre européen de l’intelligence artificielle comprend des exigences de transparence et des règles liées au droit d’auteur pour certains acteurs, sans permettre au chapitre de déduire automatiquement les obligations d’un projet particulier.

Les références exactes sont conservées dans la dernière section du chapitre. Les formulations juridiquement variables restent conditionnelles et renvoient à une revue adaptée à la juridiction, au contrat et à l’exploitation.

## 6. Explications pédagogiques

Les **36** blocs possèdent **36** marqueurs. Les **16** blocs hors erreurs expliquent selon leur nature : rôle, champs, entrées, statuts, expressions, codes de retour, propagation, effets de bord, limites et résultat attendu.

Les dix cas d’erreurs respectent la séquence directe :

1. symptôme ;
2. exemple fautif ;
3. `Pourquoi cet exemple est fautif` ;
4. exemple corrigé ;
5. `Pourquoi la correction fonctionne`.

Aucune rubrique `Explication structurée du bloc` ne s’intercale dans les séquences d’erreurs.

## 7. Contrôles particuliers

- chaque bloc clôturé possède un repère reconnu ;
- les fichiers à créer utilisent `[VSC]` avec leur chemin ;
- les commandes PowerShell utilisent `[PS]` ;
- les structures non exécutables utilisent `[LECTURE]` ;
- les sections Solo et Studio restent en Markdown ordinaire ;
- les statuts inconnus restent bloquants ;
- la publication exige une décision humaine ;
- `accepted_limited` conserve un périmètre contrôlable ;
- les documents sensibles utilisent des références opaques ;
- les dépendances bloquées se propagent ;
- les assets retirés conservent leur identité et leurs preuves ;
- le validateur Python ne prononce aucune conclusion juridique ;
- les valeurs factices sont explicitement signalées ;
- aucune valeur runtime ou mesure juridique n’est inventée.

## 8. Réserves

- registre central réel non matérialisé ;
- fiches d’assets réelles non créées ;
- licences, contrats, reçus et conditions de fournisseurs non collectés ;
- consentements voix, image, scan ou mocap non obtenus ;
- stockage restreint des preuves non configuré ;
- matrice réelle des licences non peuplée ;
- modèles IA, datasets, poids et extensions non qualifiés ;
- chaînes de transformations et empreintes réelles non produites ;
- script Python proposé non exécuté sur un registre réel ;
- CI de provenance non installée ;
- revue juridique ou responsable désigné non exécutée ;
- inventaire des marques et contenus sensibles non réalisé ;
- procédure de retrait non exercée sur un incident pilote ;
- durées de conservation et règles de suppression non décidées pour les données réelles ;
- Starter Kit non matérialisé ;
- licence globale de la collection non définie ;
- PDF du Livre III non construit conformément à la politique de fin de Livre.

## 9. Décision

Le chapitre 5 du Livre III est **accepté au niveau `static-review` sous réserve de réussite des validations documentaires permanentes**. Il définit une chaîne de provenance, de qualification, de blocage, de publication et de retrait conforme au périmètre du plan maître, sans présenter ses modèles documentaires comme des contrats réels ni fournir d’avis juridique personnalisé.
