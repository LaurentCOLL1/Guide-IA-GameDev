---
title: "Audit post-création — Livre IV, chapitre 16"
id: "DOC-L4-QA-AUDIT-CH16"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L4-CH16"
chapter-version: "1.0.0"
audit-date: "2026-07-27T08:32:16+02:00"
last-verified: "2026-07-27T08:32:16+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 16

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de matérialisation des presets, templates, SDK, dépendances natives, icônes dérivées, credentials, certificats, keystores, signatures, notarisation, packages, manifestes réels et campagnes sur machines propres de `Project Asteria`.

Aucun export Godot, template installé, SDK qualifié, build Windows, Linux, macOS, Android, iOS ou Web, signature, notarisation, package, installation, lancement, sauvegarde de test ou retrait n’est revendiqué comme exécuté. Aucun manuel intermédiaire du Livre IV n’est produit.

## 2. Périmètre comparé au plan maître

Le chapitre couvre les objectifs du plan maître :

- configurer des presets par plateforme et architecture ;
- gérer templates, SDK, ressources, icônes et dépendances ;
- séparer credentials confidentiels et presets versionnés ;
- produire les contrats debug, test et release ;
- vérifier fichiers inclus, exclus et interdits ;
- préparer Windows, Linux, macOS, Android, iOS et Web ;
- automatiser export, staging, packaging, manifestes et checksums ;
- préparer signatures et notarisation sans exposer les clés ;
- préparer installation et lancement sur machine propre.

Les livrables sont préparés sous forme de matrice de cibles, politique de ressources, manifeste d’outils, presets de référence, scripts canoniques, contrats de signature, manifestes de packages, checksums, reçus de promotion et campagne de machine propre.

## 3. Frontières contrôlées

- le chapitre 3 conserve suites, fixtures, cas et oracles de tests ;
- le chapitre 13 conserve le runtime et la sécurité du serveur dédié ;
- le chapitre 14 conserve orchestration CI/CD, identités de builds, artefacts et promotion ;
- le chapitre 15 conserve sauvegardes, restaurations, RPO/RTO et continuité ;
- le chapitre 16 possède presets clients, filtres, dépendances, icônes, signatures, packages, manifestes et validation de livraison ;
- le chapitre 17 conserve boutiques, pages, canaux, clés, soumissions et lancement ;
- le chapitre 20 conserve patches, mises à jour distribuées et rollback produit ;
- le chapitre 22 conserve archivage patrimonial et pérennité ;
- aucun contrôle documentaire ne devient une preuve d’export, de signature ou de lancement.

## 4. Contrôles pédagogiques

- export, build, package, artefact, release et publication distingués ;
- matrice plateforme, architecture, profil, outil et porte documentée ;
- templates Godot reliés à la version exacte de l’éditeur ;
- `export_presets.cfg` séparé de `.godot/export_credentials.cfg` ;
- identités produit, versions et codes de plateforme distingués ;
- profils debug, test et release documentés ;
- feature tags limités à un rôle descriptif sans autorité métier ;
- filtres de ressources et fichiers non-ressources encadrés ;
- scan des fichiers privés et secrets préparé ;
- dépendances natives et GDExtension qualifiées par cible ;
- sources d’icônes et dérivés de plateforme séparés ;
- export Windows et Linux en staging neuf préparé ;
- signature Windows séparée des checksums ;
- bundle macOS, signature et notarisation distingués ;
- JDK, SDK, Gradle, AAB et keystore Android encadrés ;
- hôte macOS, Xcode et provisioning iOS maintenus comme préconditions ;
- Web monothread et multithread, contexte sécurisé et en-têtes distingués ;
- package serveur référencé sans redéfinir le chapitre 13 ;
- script Python canonique d’export préparé ;
- manifeste fermé et SHA-256 préparés ;
- archive produite uniquement depuis le staging ;
- image et montages de conteneur encadrés ;
- signature, vérification, manifeste final et promotion ordonnés ;
- campagne de machine propre préparée ;
- promotion des mêmes octets sans reconstruction maintenue ;
- échecs transitoires et permanents distingués ;
- modes Solo et Studio documentés ;
- tous les repères `[PS]`, `[CMD]`, `[WSL]`, `[DCT]`, `[DCK]`, `[VSC]`, `[WEB]`, `[APP]`, `[SORTIE]` et `[LECTURE]` sont utilisés ;
- dix diagnostics suivent la séquence sémantique complète ;
- références techniques officielles sous forme de liens Markdown cliquables ;
- synthèse opérationnelle `Project Asteria` présente.

## 5. Contrôles documentaires

- lignes : 2004 ;
- titres : 73 ;
- blocs de code ou données : 60 ;
- blocs significatifs : 56 ;
- marqueurs d’explication : 60 ;
- explications structurées hors diagnostics : 40 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- exemples corrigés expliqués : 10 ;
- titres dupliqués : 0 ;
- blocs significatifs dupliqués : 0 ;
- paragraphes longs dupliqués : 0 ;
- section Solo/Studio en Markdown ordinaire ;
- absence de recommandation GPT, de prochaine action et de chaîne de fabrication éditoriale dans le texte lecteur.

## 6. Exactitude technique

Le chapitre s’appuie sur les contrats documentés de Godot : templates d’export requis, presets nommés, séparation entre configuration versionnable et credentials confidentiels, filtres de ressources, export en ligne de commande avec `--export-debug`, `--export-release` ou `--export-pack`, et feature tags limités au contexte exporté.

Les procédures Windows, Linux, macOS, Android, iOS et Web sont présentées avec leurs préconditions propres. Elles ne prétendent pas qu’une machine unique peut construire, signer et valider toutes les cibles. macOS et iOS conservent leurs exigences d’hôte et d’outils Apple ; Android conserve JDK, SDK, Gradle et identité de signature ; le Web conserve ses contraintes de serveur et d’isolation.

Les exemples Python expliquent types, paramètres, retours, exceptions, effets de bord, confinement des chemins, listes fermées et empreintes. Les exemples PowerShell, batch et Bash propagent les codes de retour, refusent les stagings existants et ne publient aucun secret.

## 7. Contrôle des régressions

- un export release ne devient pas publication approuvée ;
- les credentials ne sont pas versionnés avec les presets ;
- une feature tag ne devient pas autorité métier ;
- un staging existant n’est pas réutilisé ;
- le workspace entier n’est pas compressé ;
- les caches, tests et outils ne deviennent pas contenu client ;
- une cible sans bibliothèque native qualifiée est bloquée ;
- une signature ne devient pas checksum et inversement ;
- l’empreinte finale est calculée après signature ;
- un keystore debug ne signe pas un candidat Android public ;
- macOS et iOS ne sont pas déclarés validés sans hôte Apple ;
- le Web n’est pas validé par ouverture `file://` ;
- une présence de package n’est pas une preuve d’installation ;
- la promotion ne reconstruit pas les octets ;
- les chapitres 13, 14, 15, 17, 20 et 22 conservent leurs responsabilités ;
- l’approbation finale reste humaine et réversible.

## 8. Réserves ouvertes

- presets réels de `Project Asteria` non matérialisés ;
- templates officiels Godot non installés ni qualifiés ;
- empreintes de l’éditeur et des templates non produites ;
- matrice réelle de plateformes et architectures non approuvée ;
- identifiants produit, bundle IDs, package names et codes de version non réservés ;
- fichiers de credentials et mécanismes d’injection non configurés ;
- politiques réelles d’inclusion et d’exclusion non appliquées ;
- scan de secrets et de fichiers privés non exécuté ;
- dépendances GDExtension et bibliothèques natives non qualifiées ;
- icônes, splashs et catalogues de plateforme non produits ;
- export Windows non exécuté ;
- signature Windows et chaîne de certificat non qualifiées ;
- export Linux et compatibilité de distributions non exécutés ;
- export macOS, signature, notarisation et Gatekeeper non exécutés ;
- JDK, SDK Android et Gradle non qualifiés ;
- keystore Android release non généré, récupéré ni testé ;
- APK et AAB non produits ;
- hôte macOS, Xcode, équipe et provisioning iOS non qualifiés ;
- export iOS et installation sur appareil non exécutés ;
- export Web et matrice de navigateurs non exécutés ;
- en-têtes du profil Web multithread non vérifiés ;
- script canonique d’export non matérialisé ;
- conteneur de build et digest d’image non qualifiés ;
- staging réel, manifeste fermé et checksums non produits ;
- certificats, keystores et identités de signature non configurés ;
- aucun package final signé ou notarié ;
- aucune campagne d’installation, lancement, sauvegarde, relance ou retrait sur machine propre ;
- aucune identité binaire ou reproductibilité de package mesurée ;
- licence globale de collection non définie ;
- balisage d’accessibilité de l’export final toujours ouvert.

## 9. Conclusion

Le chapitre satisfait le périmètre du plan maître au niveau documentaire et statique. Les contrôles du dépôt doivent confirmer structure, repères, explications, liens, doublons, frontières et absence de sortie éditoriale intermédiaire. La preuve QA peut être initialisée avec les réserves déclarées, sans revendiquer les exécutions nécessaires au niveau `runtime-tested`.
