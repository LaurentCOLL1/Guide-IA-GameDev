---
title: "Audit — Livre V, fiche 06"
id: "DOC-L5-QA-AUDIT-CH06"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 6
last-verified: "2026-07-28T16:17:52+02:00"
audit-date: "2026-07-28T16:17:52+02:00"
audit-level: "static-review"
audited-document: "Livre-V/CHAPITRE-06-Fiches-des-modeles-visuels.md"
protocol: "Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md"
---

# Audit de la fiche 06 — Fiches des modèles visuels

## Décision

**Acceptée au niveau `static-review`.** La fiche adopte le profil de référence du Livre V : index express, cartes de familles et de composants, matrices en premier, liens profonds vers les tutoriels propriétaires et séparation explicite entre revue documentaire, workflow exécuté, image produite et asset validé.

## Couverture du plan maître

| Exigence | Résultat |
|---|---|
| checkpoints | Stable Diffusion XL/3.5, FLUX.2/FLUX.1, Qwen-Image, HunyuanImage-3.0 et HiDream-I1 qualifiés |
| composants séparés | VAE, encodeurs de texte, ControlNet, LoRA et upscalers traités comme dépendances distinctes |
| licence et provenance | source, révision, fichier, empreinte, licence et restrictions requises |
| formats | checkpoints monolithiques, composants séparés, `safetensors`, diffusers et poids spécifiques distingués |
| besoins VRAM | variables à mesurer et enveloppes prudentes visibles sans résultat inventé |
| résolution et sampler | valeurs natives ou annoncées séparées des paramètres réellement testés |
| workflow de test | matrice de dix contrôles sans sortie préremplie |
| usages restreints | contenus, entrées, personnes, marques, styles et redistribution soumis à revue |
| manifestes | contrat de paquet et fiche d’acceptation présents |
| matrice ComfyUI | compatibilité par composant et preuve requise présente |
| images de test | emplacements et critères préparés ; aucune image matérialisée au niveau `static-review` |

## Frontières contrôlées

- La fiche 03 conserve les applications, installations et versions d’outils.
- La fiche 04 conserve ComfyUI comme moteur, les backends CPU/DirectML/ZLUDA/ROCm et les diagnostics d’exécution.
- La fiche 06 conserve les familles et composants de modèles visuels.
- La fiche 08 conservera les workflows réutilisables.
- Le chapitre 18 du Livre V conservera la référence graphique et 3D transversale.
- Le chapitre 21 conservera les benchmarks exécutés.
- Le chapitre 22 conservera les compatibilités historiques.
- Le chapitre 25 conservera l’inventaire transversal des licences.
- La recherche, la création, la critique et la promotion artistique restent dans le Livre III.

## Contrôles de forme

| Contrôle | Résultat |
|---|---:|
| lignes | 380 |
| titres Markdown | 18 |
| fiches `l5:card` | 13 |
| matrices `l5:matrix` | 3 |
| liens Markdown | 65 |
| renvois vers les Livres I à IV | 20 |
| liens profonds vers des sous-sections | 19 |
| liens web officiels | 23 |
| blocs clôturés | 0 |
| structure « Résultats d’apprentissage » importée | absente |
| synthèse finale `Project Asteria` importée | absente |
| installation ComfyUI complète recopiée | absente |
| image générée intégrée | absente |

## Sources officielles datées

Les pages et dépôts suivants ont été consultés le `2026-07-28` :

- annonces, licences et dépôts Stability AI pour Stable Diffusion 3.5, SDXL et leurs ControlNet ;
- dépôts Black Forest Labs pour FLUX.2 et FLUX.1 ;
- documentation Qwen et exemples ComfyUI pour Qwen-Image ;
- dépôt officiel Tencent HunyuanImage-3.0 ;
- dépôt officiel HiDream-I1 ;
- documentation ComfyUI sur checkpoints, VAE, LoRA, ControlNet et upscalers ;
- dépôt officiel ControlNet ;
- documentation Diffusers sur LoRA ;
- dépôt officiel Real-ESRGAN.

Les cartes reprennent l’architecture, les composants, les licences, les formats, les résolutions annoncées et les contraintes de qualification. Les images promotionnelles, classements et performances éditeur ne sont pas importés comme résultats du guide.

## Qualification des faits volatils

- chaque famille porte une date de revue ;
- une architecture annoncée n’est pas une compatibilité ComfyUI démontrée ;
- une exigence CUDA officielle n’est pas transposée à la RX 6750 XT ;
- une quantité de VRAM annoncée n’est pas un pic mesuré sur le backend du projet ;
- une résolution native n’est pas une taille de production validée ;
- un sampler recommandé n’est pas universel entre familles ;
- un checkpoint ne couvre pas automatiquement VAE, encodeurs, LoRA, ControlNet ou upscalers ;
- la licence du code ne couvre pas automatiquement les poids, datasets, entrées ou sorties ;
- un dérivé communautaire doit conserver sa chaîne de provenance et ses licences héritées.

## Compatibilité ComfyUI

La matrice B exige, pour chaque paquet :

- chargeur ou nœud Core compatible ;
- liste exacte des fichiers ;
- versions de ComfyUI et des nœuds ;
- chemins et formats ;
- backend matériel ;
- workflow JSON et empreinte ;
- exécution témoin ;
- image de sortie mise en quarantaine ;
- décision humaine.

Une présence dans un template ou une réussite de chargement ne prouve ni la conformité juridique, ni la qualité artistique, ni la stabilité sur la configuration AMD de référence.

## Workflow de test

La matrice C couvre :

- chargement du paquet exact ;
- génération texte-vers-image minimale ;
- test de résolution native ;
- variation contrôlée du sampler ou scheduler ;
- cohérence du VAE ;
- contrôle structurel ;
- activation et retrait d’une LoRA ;
- upscale ou restauration ;
- répétition avec paramètres enregistrés ;
- revue de provenance, contenu et promotion.

Aucun résultat ni fichier image n’est fourni. Les exécutions futures doivent conserver le workflow, les modèles, les entrées, les paramètres, les sorties et les empreintes, puis enregistrer les mesures au chapitre 21.

## Liens et ancres

Les 19 renvois profonds visent les sections propriétaires consacrées à ComfyUI, aux environnements qualifiés, aux modèles et droits, aux workflows JSON, aux seeds, aux expériences, à la provenance et aux statuts d’assets. Le validateur spécialisé du Livre V doit vérifier leur résolution sur la branche de PR.

Les 23 liens web sont nommés et visent des pages officielles d’éditeur, documentations ou dépôts officiels. Leur consultation qualifie l’état documentaire sans télécharger les poids.

## Doublons et densité

- aucun tutoriel d’installation ComfyUI recopié ;
- aucune commande de téléchargement ou génération reproduite ;
- aucun workflow complet du Livre III dupliqué ;
- aucune famille répétée comme composant ;
- les cartes VAE, encodeur, ControlNet, LoRA et upscaler restent indépendantes des checkpoints ;
- les paragraphes restent courts et les tables portent l’information principale.

## Réserves

- aucun checkpoint, VAE, encodeur, ControlNet, LoRA ou upscaler téléchargé ;
- aucun workflow ComfyUI chargé ou exécuté ;
- aucune image de test ou sortie générée ;
- aucune mesure de temps, RAM, VRAM, stabilité ou qualité produite ;
- aucune voie CPU, DirectML, ZLUDA, Vulkan ou ROCm qualifiée avec ces modèles ;
- aucune licence organisationnelle ou exploitation de sortie approuvée juridiquement ;
- aucun checkpoint communautaire ni contenu restreint audité ;
- aucun fichier ou manifeste du Companion Pack créé ;
- aucun PDF produit ;
- la licence globale et le balisage avancé de publication restent ouverts.

## Empreinte

L’empreinte du chapitre est enregistrée dans la preuve QA finale. Toute modification ultérieure exige une nouvelle empreinte et une nouvelle validation.
