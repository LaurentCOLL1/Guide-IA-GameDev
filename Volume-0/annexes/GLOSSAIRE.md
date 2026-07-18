---
title: "Annexe — Glossaire normatif"
id: "DOC-V0-ANN-GLOSSAIRE"
status: "in-progress"
version: "0.1.0"
---

# Glossaire normatif

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](CONVENTION-OUTILS-ET-CONTEXTES.md).

Cette annexe centralise les termes employés dans l’ensemble du guide. Une définition publiée ici prévaut sur les reformulations locales. Les chapitres peuvent ajouter du contexte, mais ne doivent pas créer une définition concurrente.

## Règles d’utilisation

- Chaque terme possède un identifiant stable `GL-XXX`.
- Le terme français est privilégié lorsqu’il est naturel et non ambigu.
- L’anglicisme courant est indiqué comme synonyme lorsqu’il facilite les recherches.
- Une définition décrit l’usage du terme dans ce guide, pas toutes ses acceptions possibles.
- Les termes dépendant d’une version ou d’un outil doivent renvoyer vers une source technique vérifiable.
- Toute modification qui change le sens d’un terme doit être signalée dans le changelog.

## Termes fondamentaux

| ID | Terme | Synonymes ou forme anglaise | Définition normative |
|---|---|---|---|
| GL-001 | Agent IA | AI agent | Système logiciel utilisant un modèle pour analyser un contexte, choisir des actions et éventuellement appeler des outils dans les limites de permissions explicites. |
| GL-002 | API | Interface de programmation | Contrat permettant à des logiciels de communiquer au moyen d’opérations, de paramètres et de formats définis. |
| GL-003 | Asset | Ressource de jeu | Fichier ou ensemble de fichiers utilisé par le jeu : modèle 3D, texture, son, animation, scène, script ou donnée. |
| GL-004 | Benchmark | Banc d’essai | Procédure reproductible servant à mesurer les performances, la qualité ou la stabilité d’un système. |
| GL-005 | Checkpoint | Point de contrôle | Fichier contenant les poids d’un modèle entraîné à un état déterminé. |
| GL-006 | Companion Pack | Pack compagnon | Ensemble versionné de modèles, scripts, configurations, workflows et projets de référence accompagnant les livres. |
| GL-007 | Conteneur | Container | Environnement logiciel isolé regroupant une application et ses dépendances, généralement exécuté avec Docker. |
| GL-008 | Dépendance | Dependency | Bibliothèque, outil, modèle ou service requis par un composant pour fonctionner. |
| GL-009 | Embedding | Représentation vectorielle | Vecteur numérique représentant le sens ou les caractéristiques d’un contenu afin de permettre comparaison et recherche. |
| GL-010 | Empreinte | Hash, checksum | Valeur calculée à partir d’un fichier ou d’un ensemble de données afin de vérifier son identité et son intégrité. |
| GL-011 | Endpoint | Point d’accès | Adresse et opération exposées par un service ou une API. |
| GL-012 | Inférence | Inference | Exécution d’un modèle entraîné afin de produire une sortie à partir d’une entrée. |
| GL-013 | Jeu de données | Dataset | Ensemble structuré de données destiné à l’entraînement, à l’évaluation ou à la validation. |
| GL-014 | LLM | Grand modèle de langage | Modèle neuronal entraîné à comprendre et générer du texte ou des données structurées. |
| GL-015 | LoRA | Low-Rank Adaptation | Technique d’adaptation légère d’un modèle au moyen de poids additionnels de faible dimension. |
| GL-016 | Modèle local | Local model | Modèle exécuté sur la machine ou l’infrastructure contrôlée par l’utilisateur, sans dépendance obligatoire à un service distant. |
| GL-017 | Nœud | Node | Unité fonctionnelle d’un graphe, d’une scène ou d’un workflow. Son sens précis dépend de l’outil concerné. |
| GL-018 | Pipeline | Chaîne de production | Suite ordonnée d’étapes transformant des entrées en livrables vérifiables. |
| GL-019 | Prompt | Instruction de modèle | Texte ou structure fournie à un modèle pour définir une tâche, un contexte, des contraintes et un format de sortie. |
| GL-020 | Quantification | Quantization | Réduction de la précision numérique des poids ou calculs d’un modèle afin de diminuer son empreinte mémoire et parfois accélérer son exécution. |
| GL-021 | RAG | Génération augmentée par recherche | Architecture combinant une recherche documentaire avec un modèle génératif afin de fonder la réponse sur des sources récupérées. |
| GL-022 | Reproductibilité | Reproducibility | Capacité à répéter une procédure dans un environnement documenté et à obtenir un résultat identique ou suffisamment comparable. |
| GL-023 | Seed | Graine aléatoire | Valeur initialisant un générateur pseudo-aléatoire afin de faciliter la répétition d’une génération. |
| GL-024 | Service | Service logiciel | Processus exposant une capacité à d’autres composants, localement ou sur un réseau. |
| GL-025 | Source de vérité | Single source of truth | Emplacement faisant autorité pour une information donnée et évitant les copies divergentes. |
| GL-026 | Workflow | Flux de travail | Séquence explicite d’opérations, manuelles ou automatisées, permettant d’obtenir un résultat défini. |
| GL-027 | VRAM | Mémoire vidéo | Mémoire disponible sur le processeur graphique pour stocker modèles, textures, buffers et données de calcul. |
| GL-028 | Mode Solo | Solo mode | Parcours adapté à une personne travaillant sur une seule station avec une administration minimale. |
| GL-029 | Mode Studio | Studio mode | Parcours adapté à une équipe avec partage, rôles, validation, sauvegardes et traçabilité renforcés. |
| GL-030 | Obligatoire | Required | Élément nécessaire pour respecter le socle normatif ou obtenir le résultat annoncé. |
| GL-031 | Recommandé | Recommended | Élément fortement conseillé pour la robustesse, la qualité ou la maintenance, mais non indispensable au résultat minimal. |
| GL-032 | Optionnel | Optional | Amélioration ou variante pouvant être omise sans invalider le parcours principal. |
| GL-033 | ZLUDA | — | Couche de compatibilité permettant à certains logiciels prévus pour CUDA d’exécuter des calculs sur du matériel non NVIDIA, sous réserve de compatibilité vérifiée. |
| GL-034 | ComfyUI | — | Interface nodale utilisée dans ce guide pour construire, versionner et exécuter des workflows de génération visuelle. |
| GL-035 | Open WebUI | — | Interface centrale retenue dans ce guide pour accéder aux modèles de langage locaux et à certains outils associés. |
| GL-036 | Godot | — | Moteur de jeu principal retenu pour l’architecture et l’implémentation du projet fil rouge. |
| GL-037 | Blender | — | Suite 3D principale retenue pour la création, la modification, l’animation et la préparation des assets. |

## Termes à ajouter

Les futurs livres enrichiront cette annexe. Une nouvelle entrée doit être ajoutée lorsqu’un terme remplit au moins une des conditions suivantes :

- il apparaît dans plusieurs chapitres ;
- il possède plusieurs sens possibles ;
- sa traduction française n’est pas évidente ;
- il intervient dans une règle de compatibilité, de sécurité ou de licence ;
- son absence pourrait provoquer une erreur de mise en œuvre.

## Checklist de validation

- [ ] Chaque terme possède un identifiant unique.
- [ ] Les synonymes renvoient vers une seule définition canonique.
- [ ] Les définitions sont compréhensibles hors contexte.
- [ ] Les termes sensibles aux versions renvoient vers la bibliographie.
- [ ] Les nouveaux termes des livres publiés sont intégrés avant chaque version stable.
