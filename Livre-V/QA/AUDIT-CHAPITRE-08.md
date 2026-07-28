---
title: "Audit — Livre V, fiche 08 : Bibliothèque de workflows"
id: "DOC-L5-QA-AUDIT-CH08"
status: "complete"
version: "1.0.0"
last-verified: "2026-07-28T18:20:01+02:00"
lang: "fr-FR"
book: "Livre V"
chapter: 8
audit-date: "2026-07-28T18:20:01+02:00"
audit-level: "static-review"
validation-authority: "livre-v-reference-profile"
---

# Audit — Fiche 08 : Bibliothèque de workflows

## 1. Décision

La fiche est conforme au profil spécialisé du Livre V sous réserve des exécutions explicitement laissées ouvertes. Elle catalogue des contrats de workflows Godot, Blender, ComfyUI, audio et documentation sans recopier leurs tutoriels propriétaires ni présenter les futurs fichiers du Companion Pack comme matérialisés.

## 2. Périmètre contrôlé

- chemin canonique : `Livre-V/CHAPITRE-08-Bibliotheque-de-workflows.md` ;
- identifiant : `DOC-L5-CH08` ;
- version : `1.0.0` ;
- format : `reference-cards` ;
- niveau de preuve : `static-review` ;
- sources évolutives revues le 28 juillet 2026 ;
- aucune compilation PDF intermédiaire.

## 3. Métriques statiques

| Mesure | Valeur |
|---|---:|
| lignes | 409 |
| titres | 18 |
| cartes `l5:card` | 13 |
| matrices `l5:matrix` | 3 |
| liens Markdown | 70 |
| renvois vers les Livres I à IV | 36 |
| liens profonds vers les Livres I à IV | 36 |
| liens officiels | 13 |
| blocs clôturés | 0 |

## 4. Couverture du plan maître

| Exigence | Couverture |
|---|---|
| workflows Godot | contenu, QA, import et export distingués |
| workflows Blender | source, collection, export glTF et contrôle Godot séparés |
| workflows ComfyUI | graphe éditable, format API, modèles, run et quarantaine séparés |
| workflows audio | TTS, STT, génération exploratoire et postproduction encadrés |
| workflows documentation | branche, validations légères, audit, preuve et fusion ciblée |
| entrées, sorties, dépendances et étapes | contrat commun et cartes de domaine |
| variantes Solo et Studio | deux cartes dédiées avec gouvernance différenciée |
| reproduction et adaptation | cycle, manifestes, idempotence, repli et qualification |
| fiches workflow | treize cartes directement consultables |
| diagrammes | remplacés par matrices tabulaires adaptées au profil Livre V |
| fichiers réutilisables | emplacements et contrat définis, statut `not-materialized` |
| checklists | porte d’acceptation et matrice de douze qualifications compactes |

## 5. Frontières

La fiche conserve les responsabilités suivantes :

- les tutoriels détaillés restent dans les Livres I à IV ;
- les outils et installations restent à la fiche 03 ;
- les moteurs, API et backends restent à la fiche 04 ;
- les modèles restent aux fiches 05 à 07 ;
- les prompts restent à la fiche 09 ;
- les scripts restent au chapitre 10 ;
- les mesures exécutées restent au chapitre 21 ;
- les compatibilités historiques restent au chapitre 22 ;
- les checklists transversales restent au chapitre 24 ;
- licences, provenance et conformité restent au chapitre 25 ;
- les fichiers exécutables et templates réels restent au Companion Pack.

## 6. Séparation définition et exécution

Chaque workflow est classé comme contrat documentaire. Les cartes décrivent les entrées, transformations, sorties, refus, reprise et preuves nécessaires. Aucune carte n’annonce :

- un import ou export Godot exécuté ;
- un script Blender lancé ou un GLB produit ;
- un graphe ComfyUI soumis ou un média généré ;
- une synthèse, transcription ou postproduction audio réalisée ;
- un build, workflow CI de produit ou publication généré ;
- une performance, reproductibilité binaire ou compatibilité matérielle mesurée.

## 7. Sécurité et gouvernance

Les contrôles visibles couvrent les écritures bornées, fichiers non fiables, scripts tiers, custom nodes, secrets, services exposés, données personnelles, sorties génératives, opérations destructives, dépendances distantes et déclencheurs de pull request.

Le workflow documentaire reste distinct d’une autorité métier. La réussite technique ne promeut jamais automatiquement un asset, un build ou une publication.

## 8. Liens et consultation

Les 36 renvois vers les Livres I à IV évitent les duplications. Les 36 fragments visent des sous-sections propriétaires pour les contrats de contenu, l’automatisation Python, Blender, ComfyUI, audio, Solo/Studio, documentation et CI.

Les liens externes pointent vers les documentations officielles de Godot, Blender, ComfyUI, GitHub Actions, FFmpeg et Pandoc. Leur présence ne constitue pas une exécution ni une campagne automatisée de vérification réseau.

## 9. Réserves ouvertes

1. aucun template ou fichier workflow du Companion Pack créé ;
2. aucun projet Godot importé, testé ou exporté ;
3. aucun script Blender exécuté et aucun GLB produit ;
4. aucun graphe ComfyUI soumis et aucun média généré ;
5. aucun moteur audio chargé et aucun fichier audio traité ;
6. aucun workflow produit ou pipeline de publication exécuté ;
7. aucun test d’idempotence, retry, interruption ou reprise effectué ;
8. aucun résultat de reproductibilité ou de performance produit ;
9. aucun secret, fichier externe, donnée personnelle ou service manipulé ;
10. aucune approbation juridique ou organisationnelle réalisée ;
11. aucun artefact permanent du Companion Pack matérialisé ;
12. aucun PDF produit ; licence globale et balisage avancé ouverts.

## 10. Critère d’acceptation

La fiche est acceptée au niveau `static-review` lorsque les validateurs permanents confirment la structure, les métadonnées, les liens locaux, les marqueurs Livre V, les liens profonds, les repères et l’absence de PDF. Les workflows eux-mêmes restent `defined` jusqu’à leur matérialisation et leur qualification runtime.
