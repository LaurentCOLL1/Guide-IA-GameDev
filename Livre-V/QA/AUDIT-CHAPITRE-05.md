---
title: "Audit — Livre V, fiche 05"
id: "DOC-L5-QA-AUDIT-CH05"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 5
last-verified: "2026-07-28T15:09:18+02:00"
audit-date: "2026-07-28T15:09:18+02:00"
audit-level: "static-review"
audited-document: "Livre-V/CHAPITRE-05-Fiches-des-modeles-de-langage.md"
protocol: "Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md"
---

# Audit de la fiche 05 — Fiches des modèles de langage

## Décision

**Acceptée au niveau `static-review`.** La fiche adopte le profil de référence du Livre V : index express, cartes de familles, matrices en premier, liens profonds vers les tutoriels propriétaires et absence de téléchargement ou de benchmark revendiqué.

## Couverture du plan maître

| Exigence | Résultat |
|---|---|
| familles enregistrées | Qwen3, Gemma 4, Phi-4, Granite 4, Mistral Small 4, Llama et DeepSeek-R1 |
| tailles et architectures | tailles denses, paramètres totaux/actifs et MoE distingués |
| quantifications | Q4, Q5, Q8 et FP16 qualifiés sans recommandation universelle |
| contextes | contexte annoncé, runtime, testé et retenu séparés |
| licences | Apache 2.0, MIT, conditions Gemma, licence Llama et héritage des dérivés visibles |
| usages et langues | usages déclarés, français et multilingue soumis à tests |
| exigences mémoire | poids théoriques calculés, surcoûts runtime et cache KV exclus explicitement |
| tests reproductibles | matrice de huit tests sans résultat prérempli |
| recommandation générale contre résultat matériel | séparation explicite |
| matrice de sélection | présente par usage et enveloppe |
| aucun meilleur universel | conforme |

## Frontières contrôlées

- La fiche 04 conserve moteurs, backends, API et diagnostic d’exécution.
- La fiche 05 conserve familles textuelles, quantifications, contextes, licences, mémoire théorique et protocole de test.
- La fiche 06 conservera les modèles visuels.
- La fiche 07 conservera les modèles audio.
- Le chapitre 21 conservera les benchmarks exécutés.
- Le chapitre 22 conservera les compatibilités historiques.
- Le chapitre 25 conservera l’inventaire transversal des licences.
- Les installations et mesures détaillées restent dans les Livres I et II.

## Contrôles de forme

| Contrôle | Résultat |
|---|---:|
| lignes | 379 |
| titres Markdown | 20 |
| fiches `l5:card` | 13 |
| matrices `l5:matrix` | 3 |
| liens Markdown | 56 |
| renvois vers les Livres I à IV | 19 |
| liens profonds vers des sous-sections | 19 |
| liens web officiels | 13 |
| blocs clôturés | 0 |
| structure « Résultats d’apprentissage » importée | absente |
| synthèse finale `Project Asteria` importée | absente |
| installation ou téléchargement complet recopié | absent |

## Sources officielles datées

Les pages suivantes ont été consultées le `2026-07-28` :

- annonce Qwen3 et tableau des variantes ;
- documentation et historique des versions Gemma 4 ;
- carte Microsoft Phi-4-mini-instruct et rapport Phi-4 ;
- annonce IBM Granite 4.0 ;
- annonce Mistral Small 4 et politique de licence des modèles ouverts Mistral ;
- catalogue, carte et licence Llama 4 ;
- dépôt officiel DeepSeek-R1.

Les cartes reprennent uniquement les informations nécessaires à la sélection : architecture, tailles, contexte annoncé, langues, licence et statut local. Les performances promotionnelles des éditeurs ne sont pas importées comme résultats du guide.

## Qualification des faits volatils

- chaque famille porte une date de revue ;
- un contexte annoncé n’est pas un contexte testé ;
- un nombre de paramètres actifs n’est pas le stockage total ;
- une famille n’est pas un checkpoint ;
- une licence de dérivé ne remplace pas celle de la base ;
- une quantification est un artefact distinct ;
- une prise en charge linguistique déclarée doit être évaluée ;
- une estimation de poids ne comprend pas cache KV, buffers ni runtime.

## Mémoire

La matrice B applique la formule `paramètres × bits ÷ 8` aux poids seuls. Les valeurs sont arrondies et ne constituent ni une mesure de RAM, ni une mesure de VRAM, ni une promesse de chargement. Le profil 7B–9B Q4 avec contexte 4096 reste un point de départ issu du Livre I.

## Tests

La matrice C couvre :

- conformité exacte ;
- résumé fidèle en français ;
- JSON strict ;
- GDScript typé ;
- refus d’invention ;
- rappel dans un contexte croissant ;
- stabilité avec paramètres fixés ;
- appel d’outil à schéma fermé.

Aucune sortie n’est fournie. Les tests doivent être exécutés avec le même fichier, runtime, backend, template, contexte et paramètres, puis enregistrés dans le chapitre 21.

## Liens et ancres

Les 19 renvois profonds visent les sections propriétaires consacrées aux manifestes, licences, profils mémoire, quantification, génération, tests, mesures, sauvegarde, sécurité et reproductibilité. Le validateur spécialisé du Livre V doit vérifier leur résolution sur la branche de PR.

Les 13 liens web sont nommés et visent des pages officielles d’éditeur ou des dépôts officiels. Leur consultation dans ce lot qualifie l’état documentaire, sans téléchargement de poids.

## Doublons et densité

- aucun tutoriel d’installation recopié ;
- aucune commande d’inférence reproduite ;
- aucune matrice de benchmark exécuté importée ;
- aucune famille répétée sous plusieurs cartes ;
- la fiche 04 n’est pas dupliquée ;
- les paragraphes restent courts et les tables portent l’information principale.

## Réserves

- aucun modèle, checkpoint ou quantification téléchargé ;
- aucune inférence ni commande de runtime exécutée ;
- aucun résultat de qualité, débit, latence, RAM, VRAM ou cache KV produit ;
- aucune fenêtre de contexte maximale testée ;
- aucune licence organisationnelle approuvée juridiquement ;
- aucune quantification communautaire auditée ;
- aucun fichier ou manifeste du Companion Pack créé ;
- aucun PDF produit ;
- la licence globale et le balisage avancé de publication restent ouverts.

## Empreinte

L’empreinte du chapitre est enregistrée dans la preuve QA finale. Toute modification ultérieure exige une nouvelle empreinte et une nouvelle validation.
