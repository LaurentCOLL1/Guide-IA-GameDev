---
title: "Audit post-création — Livre IV, chapitre 22"
id: "DOC-L4-AUDIT-CH22"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre IV"
chapter: 22
audit-date: "2026-07-28T05:41:07+02:00"
last-verified: "2026-07-28T05:41:07+02:00"
audit-level: "static-review"
target-document: "Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md"
---

# Audit post-création — Chapitre 22

## 1. Décision

Le chapitre 22 — **Maintenance, archivage et pérennité** est accepté au niveau `static-review`.

La décision porte uniquement sur la qualité documentaire et la cohérence statique. Elle ne qualifie aucune archive, restauration, reconstruction historique, topologie de stockage, clé, signature, SBOM, compte, procédure de succession, migration de format ou fin de support réelle.

## 2. Périmètre comparé au plan maître

Les cinq objectifs du plan maître sont couverts :

1. surveillance des dépendances et vulnérabilités ;
2. archivage des sources, outils, builds et documentations ;
3. reproductibilité et reconstruction historique ;
4. succession, fin de support et ouverture éventuelle ;
5. formats lisibles, checksums et fixité.

Les cinq livrables sont documentés sous forme de contrats candidats :

- calendrier de maintenance ;
- inventaire d’archives ;
- procédures de reconstruction ;
- plan de fin de vie ;
- dossier de succession.

## 3. Frontières vérifiées

### Chapitre 14 — DevOps et intégration continue

Le chapitre 14 conserve les pipelines, la construction et la promotion courantes. Le chapitre 22 conserve les environnements, outils et preuves nécessaires à une reconstruction ultérieure.

### Chapitre 15 — Sauvegardes et reprise

Le chapitre 15 conserve la reprise opérationnelle des données et services. Le chapitre 22 ajoute conservation historique, fixité, restauration isolée et formats durables.

### Chapitre 16 — Exports et packaging

Le chapitre 16 produit les packages officiels. Le chapitre 22 les inventorie, les scelle et les relie aux sources, SBOM, licences et rapports.

### Chapitre 20 — Correctifs et mises à jour

Le chapitre 20 possède mise à niveau, migration distribuée, déploiement et rollback. Le chapitre 22 conserve l’ancien environnement, la décision et les preuves de transition.

### Chapitre 21 — Modding

Le chapitre 21 possède les surfaces communautaires actives. Le chapitre 22 conserve versions d’API, SDK, schémas et politiques sans acquérir les droits de republier les contenus tiers.

## 4. Contrôle pédagogique

Le chapitre :

- définit les termes avant les procédures ;
- distingue copie, sauvegarde, archive et miroir ;
- explique fixité, signature, authenticité, restauration et reconstruction séparément ;
- nomme programmes, fichiers, commandes, paramètres, sorties et limites ;
- maintient les procédures Solo et Studio ;
- se termine par une synthèse opérationnelle pour `Project Asteria`.

Chaque bloc de code ou de données porte `<!-- qa:code-explanation -->` et une explication structurée proportionnée.

## 5. Contrôle des repères d’utilisation

Les dix repères obligatoires sont présents :

- `[PS]` pour PowerShell 7 ;
- `[CMD]` pour l’invite de commandes Windows ;
- `[WSL]` pour Bash sous WSL ou Linux ;
- `[DCT]` pour une commande dans un conteneur ;
- `[DCK]` pour une action dans Docker Desktop ;
- `[VSC]` pour la création ou modification de fichiers ;
- `[WEB]` pour une procédure dans un navigateur ;
- `[APP]` pour une application graphique nommée ;
- `[SORTIE]` pour un résultat à lire ;
- `[LECTURE]` pour une structure de référence.

Les marqueurs correspondent à la nature de leur bloc. Les configurations YAML sont placées sous `[VSC]` ou `[LECTURE]`, jamais présentées comme une action Docker Desktop ou web.

## 6. Contrôle des explications structurées

Les blocs significatifs expliquent selon le cas :

- entrées et chemins ;
- paramètres et politiques ;
- traitements et ordre ;
- codes de retour ;
- effets de bord ;
- invariants ;
- résultats attendus ;
- limites et réserves.

Aucun bloc significatif n’est laissé sans marqueur d’explication.

## 7. Contrôle des diagnostics

La section `<!-- qa:error-correction-section -->` contient dix diagnostics détaillés :

1. miroir confondu avec archive ;
2. code source archivé seul ;
3. checksum confondu avec signature ;
4. secret placé dans Git ;
5. alerte fermée sans justification ;
6. original écrasé pendant une migration ;
7. clone confondu avec reconstruction ;
8. compte personnel unique ;
9. service retiré sans plan de données ;
10. archive déclarée saine sans restauration.

Chaque cas contient symptôme, exemple fautif, explication, exemple corrigé et justification structurée.

## 8. Contrôle technique statique

Les exemples ont été relus statiquement :

- PowerShell utilise `Set-StrictMode`, arrêt sur erreur et chemins explicites ;
- Bash utilise `set -euo pipefail` ;
- les commandes `git bundle create`, `verify`, `list-heads` et `git clone` correspondent à leurs usages documentés ;
- le code Python traite les fichiers par morceaux et refuse les chemins sortant de la racine ;
- les manifestes restent candidats et n’inventent ni digest, ni build, ni durée mesurée ;
- les secrets sont explicitement exclus ;
- les opérations destructives ne sont jamais automatisées par les exemples.

Aucune exécution runtime, reconstruction ou restauration n’a été effectuée.

## 9. Sources officielles

Les références lecteur pointent vers des sources officielles ou normatives :

- documentation Git ;
- documentation GitHub ;
- SPDX ;
- CycloneDX ;
- SLSA ;
- Sigstore ;
- NIST ;
- CISA ;
- Library of Congress ;
- documentation Godot.

Les exigences de plateformes et spécifications sont déclarées volatiles et devront être revérifiées lors d’une implémentation réelle.

## 10. Contrôle anti-doublon

Le contrôle local ne trouve :

- aucun titre dupliqué ;
- aucun bloc significatif dupliqué ;
- aucun paragraphe long dupliqué.

Les rappels sur les frontières, secrets et réserves sont contextualisés plutôt que recopiés intégralement.

## 11. Gouvernance

Le lot permanent doit contenir exactement :

1. `CONTINUITE-PROJET.md` ;
2. `Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md` ;
3. `Livre-IV/QA/AUDIT-CHAPITRE-22.md` ;
4. `Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-22.yaml` ;
5. `Livre-IV/index.md` ;
6. `ROADMAP.md` ;
7. `contents.txt` ;
8. `plans/LIVRE-IV-PLAN-MAITRE.md`.

Le PDF du Livre IV reste différé. La fin de la rédaction des 22 chapitres n’implique pas la fermeture des critères runtime, publication ou PDF.

## 12. Réserves

Restent non matérialisés ou non exécutés :

- calendrier opérationnel ;
- inventaire réel ;
- alertes et triages réels ;
- SBOM et provenance ;
- bundles, objets LFS, sous-modules et releases archivés ;
- copies indépendantes, hors ligne ou immuables ;
- checksums et signatures réels ;
- restauration et reconstruction historique ;
- comparaison d’artefacts ;
- migration de formats ;
- transfert de comptes ou secrets ;
- exercice de succession ;
- plan de fin de support publié ;
- ouverture juridique du code ou des contenus ;
- licence globale de la collection ;
- PDF final accessible et inspecté.

## 13. Conclusion

Le chapitre est complet, débutant-compatible, cohérent avec le plan maître et acceptable au niveau `static-review`. La clôture documentaire du Livre IV peut être enregistrée, tandis que la construction et l’inspection du PDF complet deviennent l’action suivante de gouvernance.
