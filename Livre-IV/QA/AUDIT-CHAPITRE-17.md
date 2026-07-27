---
title: "Audit post-création — Livre IV, chapitre 17"
id: "DOC-L4-QA-AUDIT-CH17"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L4-CH17"
chapter-version: "1.0.0"
audit-date: "2026-07-27T09:40:10+02:00"
last-verified: "2026-07-27T09:40:10+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 17

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de matérialisation des comptes, fiches produit, médias, classifications, formulaires, prix, territoires, canaux, clés, builds soumis, revues, approbations, lancement et support de `Project Asteria`.

Aucun compte de publication, page boutique, média final, prix réel, classification, déclaration de confidentialité, clé d’accès, téléversement, soumission, approbation, vente, lancement public ou support réel n’est revendiqué. Aucun PDF intermédiaire du Livre IV n’est produit.

## 2. Périmètre comparé au plan maître

Le chapitre couvre :

- pages, médias, descriptions et exigences de publication ;
- boutiques, canaux, identités externes et clés ;
- licences, classifications, confidentialité et conformité ;
- builds candidats, notes de version et corrélation des mêmes octets ;
- calendrier de lancement et organisation du support ;
- dry-run de soumission et traitement des retours de revue.

La publication commerciale est distinguée de l’export et du packaging du chapitre 16. Les correctifs et retours arrière distribués restent au chapitre 20.

## 3. Frontières contrôlées

- chapitre 16 : presets, exports, signatures, packages et manifestes ;
- chapitre 17 : dossier de publication, fiches produit, médias, canaux, clés, déclarations, revue et lancement initial ;
- chapitre 18 : accessibilité du produit complet ;
- chapitre 19 : localisation et internationalisation ;
- chapitre 20 : correctifs, mises à jour et rollback ;
- chapitre 22 : archivage et fin de vie.

## 4. Contrôles pédagogiques

- build, artefact, canal, offre, fiche, soumission, approbation et publication distingués ;
- descriptions et affirmations reliées à des preuves ;
- médias gouvernés par source, droits, dimensions et version ;
- prix pédagogique cohérent en euros : `19,99 €`, `currency: EUR` ;
- territoires, taxes, devises et arrondis non inventés ;
- Steam, Epic Games Store, itch.io, Google Play, Apple App Store et distribution directe préparés ;
- dimensions et champs de portails traités comme données à revérifier ;
- classifications d’âge et déclarations de confidentialité versionnées ;
- credentials et clés exclus du dépôt et des journaux ;
- canaux internes, fermés, preview et publics séparés ;
- promotion des mêmes octets maintenue ;
- dry-run documentaire sans téléversement ;
- retours de revue, refus et nouvelles tentatives identifiés ;
- lancement initial et support préparés sans exécution ;
- modes Solo et Studio documentés ;
- dix diagnostics complets ;
- synthèse opérationnelle Asteria présente.

## 5. Contrôles documentaires

- lignes : 2435 ;
- titres : 95 ;
- blocs de code ou données : 71 ;
- blocs significatifs : 67 ;
- marqueurs d’explication : 71 ;
- explications structurées hors diagnostics : 51 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- exemples corrigés expliqués : 10 ;
- titres dupliqués : 0 ;
- blocs significatifs dupliqués : 0 ;
- paragraphes longs dupliqués : 0 ;
- tous les repères d’utilisation présents ;
- absence de prochaine action et de recommandation de raisonnement dans le texte lecteur.

## 6. Exactitude technique

Les références officielles couvrent Steamworks, Epic Games Store, itch.io, Google Play Console, App Store Connect et IARC. Le chapitre évite de figer des exigences de portail susceptibles d’évoluer et impose une revue datée avant matérialisation.

Les exemples utilisent des statuts candidats, des identités stables, des propriétaires, des preuves, des reçus et des refus contrôlés. Aucun exemple ne transforme une présence de build en publication publique.

## 7. Contrôle des régressions

- aucun package reconstruit pendant la soumission ;
- aucun credential versionné ;
- aucune affirmation produit non sourcée ;
- aucune classification réutilisée sans revue ;
- aucun canal fermé présenté comme public ;
- aucune clé générée sans lot ni révocation ;
- aucune capture ancienne utilisée comme seule autorité ;
- aucun prix pédagogique présenté comme décision ;
- aucun rejet écrasé par une tentative sans identité nouvelle ;
- aucune publication, vente ou support runtime revendiqué.

## 8. Réserves ouvertes

- comptes développeur et organisations non créés ou qualifiés ;
- identités externes et droits d’accès non configurés ;
- fiches produit et médias finaux non produits ;
- droits, licences et validations juridiques non exécutés ;
- classifications d’âge non demandées ;
- déclarations de confidentialité et sécurité non soumises ;
- prix, taxes, territoires et devises non approuvés ;
- builds candidats non téléversés ;
- canaux et branches de distribution non créés ;
- clés et codes d’accès non générés ;
- dry-run de portail non exécuté ;
- revue, approbation et publication non obtenues ;
- calendrier, communication et support non activés ;
- collecte d’indicateurs de lancement non exécutée ;
- licence globale de collection non définie ;
- balisage d’accessibilité PDF final ouvert.

## 9. Conclusion

Le chapitre satisfait le périmètre du plan maître au niveau documentaire et statique. La validation légère doit confirmer structure, explications, repères, doublons, frontières et absence de PDF, sans revendiquer les opérations de publication réelles.
