#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-07-28T11:28:35+02:00"
BRANCH = "fix/livre-v-profil-fiches"

CHAPTER = '---\ntitle: "Livre V — Fiche 01 : Carte générale de la collection"\nid: "DOC-L5-CH01"\nstatus: "reviewed"\nversion: "1.1.0"\nlang: "fr-FR"\nbook: "Livre V"\nchapter: 1\nlast-verified: "2026-07-28T11:28:35+02:00"\naudit-status: "complete"\naudit-date: "2026-07-28T11:28:35+02:00"\naudit-report: "Livre-V/QA/AUDIT-CHAPITRE-01.md"\naudit-level: "static-review"\ndocument-format: "reference-cards"\nreference-scope: "collection-navigation"\nusage-context-standard: "DOC-V0-ANN-CONTEXTES"\n---\n\n# Carte générale de la collection\n\n> **Type de document :** fiche d’orientation et index de navigation.  \n> **Lecture :** non linéaire ; ouvrir directement la fiche correspondant au besoin.  \n> **Principe :** le Livre V résume, classe et relie. Les procédures complètes restent dans les Livres I à IV.\n\n## Index express\n\n| Je cherche à… | Ouvrir d’abord | Continuer avec |\n|---|---|---|\n| comprendre les règles communes | [Volume 0 — Les 21 règles fondamentales](../Volume-0/CHAPITRE-02-Les-21-regles-fondamentales.md) | [architecture documentaire](../Volume-0/CHAPITRE-03-Architecture-documentaire.md), [standards techniques](../Volume-0/CHAPITRE-07-Standards-techniques.md) |\n| préparer le poste de travail | [Livre I — Matériel, Windows et pilotes AMD](../Livre-I/CHAPITRE-01-Materiel-Windows-pilotes-AMD-et-acceleration.md) | [terminaux Windows](../Livre-I/CHAPITRE-02-Terminal-PowerShell-et-outils-Windows.md), [Git et VS Code](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md#3-installer-git-for-windows) |\n| isoler un outil Python | [Pourquoi isoler Python](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#1-pourquoi-isoler-python) | [choisir une version](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#3-choisir-une-version-de-python) |\n| déployer un service local | [Docker — objet du chapitre](../Livre-I/CHAPITRE-05-Docker-et-Docker-Compose.md#1-objet-du-chapitre) | [backend et contraintes](../Livre-I/CHAPITRE-05-Docker-et-Docker-Compose.md#3-positionnement-officiel-au-18-juillet-2026) |\n| construire l’architecture du jeu | [Livre II — architecture modulaire](../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md#3-périmètre-et-frontières) | [services et injection](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md), [tests](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md) |\n| choisir une stratégie de données | [Resources, JSON et configurations](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md) | [SQLite](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md), [sauvegardes](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#3-périmètre-et-frontières) |\n| intégrer une IA locale | [LLM locaux](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md) | [mémoire vectorielle](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md), [communication Godot/IA](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md) |\n| produire un asset | [Livre III — préproduction](../Livre-III/CHAPITRE-01-Preproduction-et-cahier-des-charges-artistique.md) | [pipeline Blender](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md), [validation des assets](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md) |\n| importer dans Godot | [Importation — rôle](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#1-rôle-du-chapitre) | [frontières d’intégration](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#4-frontières-avec-les-chapitres-voisins) |\n| reproduire un défaut | [Débogage — rôle](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#1-rôle-du-chapitre) | [prérequis et frontières](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#4-prérequis-et-frontières), [observabilité](../Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md) |\n| optimiser | [Profilage CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md) | [profilage GPU](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md), [RAM et VRAM](../Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md) |\n| publier et maintenir | [DevOps et intégration continue](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md) | [exports](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md), [maintenance et pérennité](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md) |\n\n---\n\n<!-- l5:card -->\n## NAV-01 — Rôle des sept ensembles\n\n| Ensemble | Fonction | À ouvrir pour… | Ne remplace pas… |\n|---|---|---|---|\n| [Volume 0](../Volume-0/index.md) | normes et gouvernance | nommer, versionner, sourcer, publier | les tutoriels techniques |\n| [Livre I](../Livre-I/index.md) | plateforme locale | installer et sécuriser les outils | l’architecture du jeu |\n| [Livre II](../Livre-II/index.md) | développement et systèmes | construire les règles, données et services | la production artistique |\n| [Livre III](../Livre-III/index.md) | contenus et assets | produire, valider et intégrer les médias | les règles métier |\n| [Livre IV](../Livre-IV/index.md) | qualité et exploitation | tester, profiler, publier, maintenir | la conception des systèmes |\n| [Livre V](index.md) | fiches et index | retrouver rapidement une réponse | les quatre tutoriels complets |\n| [Companion Pack](../Companion-Pack/index.md) | artefacts réutilisables | adapter un fichier, modèle ou script matérialisé | la documentation de référence |\n\n**Règle de navigation :** une fiche du Livre V doit conduire vers le chapitre propriétaire, puis vers la section de validation ou de production pertinente.\n\n---\n\n<!-- l5:card -->\n## NAV-02 — Parcours débutant\n\n| Étape | Source principale | Section ou complément utile |\n|---:|---|---|\n| 1 | [règles fondamentales](../Volume-0/CHAPITRE-02-Les-21-regles-fondamentales.md) | [convention des contextes](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md) |\n| 2 | [matériel et Windows](../Livre-I/CHAPITRE-01-Materiel-Windows-pilotes-AMD-et-acceleration.md) | [terminaux](../Livre-I/CHAPITRE-02-Terminal-PowerShell-et-outils-Windows.md) |\n| 3 | [installer Git](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md#3-installer-git-for-windows) | [installer VS Code](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md#5-installer-visual-studio-code) |\n| 4 | [isoler Python](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#1-pourquoi-isoler-python) | [choisir la version](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#3-choisir-une-version-de-python) |\n| 5 | [découvrir Godot](../Livre-II/CHAPITRE-01-Decouvrir-Godot-et-creer-le-projet-fil-rouge.md) | [fondamentaux de GDScript](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md) |\n| 6 | [scènes, nœuds, Resources et signaux](../Livre-II/CHAPITRE-03-Scenes-noeuds-Resources-et-signaux.md) | [prérequis de l’architecture](../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md#2-prérequis) |\n\n**Sortie attendue :** un poste reproductible, un dépôt versionné et un premier projet Godot compris. Les commandes et exercices restent dans les liens ci-dessus.\n\n---\n\n<!-- l5:card -->\n## NAV-03 — Architecture, données et sauvegarde\n\n| Question | Réponse rapide | Tutoriel propriétaire | Vérification associée |\n|---|---|---|---|\n| Où placer une responsabilité ? | dans un module et une couche explicitement nommés | [périmètre de l’architecture modulaire](../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md#3-périmètre-et-frontières) | [tests unitaires et d’intégration](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md) |\n| Comment relier les modules ? | par contrats, services et dépendances orientées | [services, gestionnaires et injection](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md) | [journalisation et diagnostic](../Livre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md) |\n| Où placer une donnée de conception ? | dans une Resource ou une configuration versionnée | [Resources, JSON et configurations](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md) | [outils d’édition et pipelines](../Livre-II/CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md) |\n| Quand utiliser SQLite ? | pour des données relationnelles et transactionnelles | [SQLite, migrations et persistance](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md) | [reprise après incident](../Livre-IV/CHAPITRE-15-Sauvegardes-migrations-et-reprise-apres-incident.md) |\n| Qu’est-ce qu’une sauvegarde ? | un contrat de reconstruction cohérente, pas une copie brute | [rôle de la sauvegarde](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#1-rôle-du-chapitre) | [prérequis et frontières](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#3-périmètre-et-frontières) |\n\n---\n\n<!-- l5:card -->\n## NAV-04 — IA locale\n\n| Besoin | Source de plateforme | Source d’intégration | Source de contrôle |\n|---|---|---|---|\n| exécuter un LLM local | [LLM locaux et interfaces](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md) | [communication Godot avec les services IA](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md) | [séparation production/runtime](../Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md) |\n| ajouter une mémoire documentaire | [Python isolé](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#1-pourquoi-isoler-python) | [mémoire vectorielle](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md) | [tests et corpus](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md) |\n| exposer une API ou un flux | [Docker et services](../Livre-I/CHAPITRE-05-Docker-et-Docker-Compose.md#1-objet-du-chapitre) | [HTTP, WebSocket et files de tâches](../Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md) | [observabilité locale](../Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md) |\n| produire de l’audio IA | [audio IA local](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md) | [voix, bruitages, ambiances et musique](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md) | [référence audio future](index.md#chapitres) |\n\n**Limite :** cette fiche n’indique aucun modèle « meilleur ». Les fiches de moteurs et modèles appartiennent aux chapitres 4 à 7 du Livre V.\n\n---\n\n<!-- l5:card -->\n## NAV-05 — Systèmes de jeu\n\n| Domaine | Chapitre propriétaire | Fondations utiles | Qualification |\n|---|---|---|---|\n| personnages | [Livre II, chapitre 14](../Livre-II/CHAPITRE-14-Personnages.md) | [données](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md), [sauvegarde](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md) | [tests](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md) |\n| agents autonomes | [Livre II, chapitre 17](../Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md) | [services](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md), [mémoire](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md) | [profilage CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md) |\n| combat | [Livre II, chapitre 18](../Livre-II/CHAPITRE-18-Combat.md) | [entrées et interactions](../Livre-II/CHAPITRE-06-Entrees-controleurs-cameras-et-interactions.md) | [équilibrage](../Livre-IV/CHAPITRE-01-Equilibrage-et-telemetrie-locale.md) |\n| inventaire | [Livre II, chapitre 20](../Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md) | [Resources et JSON](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md) | [tests fonctionnels](../Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md) |\n| économie | [Livre II, chapitre 21](../Livre-II/CHAPITRE-21-Economie.md) | [inventaire](../Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md) | [équilibrage](../Livre-IV/CHAPITRE-01-Equilibrage-et-telemetrie-locale.md) |\n| narration et quêtes | [Livre II, chapitre 25](../Livre-II/CHAPITRE-25-Narration-quetes-codex-et-connaissances.md) | [connaissances](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md) | [localisation](../Livre-IV/CHAPITRE-19-Localisation-et-internationalisation.md) |\n\nPour une consultation transversale, la future [référence des patrons de gameplay](index.md#chapitres) renverra à ces tutoriels sans réécrire leurs systèmes complets.\n\n---\n\n<!-- l5:card -->\n## NAV-06 — Production des assets\n\n| Étape | Source principale | Contrôle ou dépendance |\n|---|---|---|\n| cadrer le besoin | [préproduction et cahier des charges](../Livre-III/CHAPITRE-01-Preproduction-et-cahier-des-charges-artistique.md) | [direction artistique](../Livre-III/CHAPITRE-02-Direction-artistique-et-bible-visuelle.md) |\n| préparer les références | [références, concept art et ComfyUI](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md) | [provenance et licences](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md) |\n| produire en 3D | [pipeline Blender](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md) | [UV, retopologie et baking](../Livre-III/CHAPITRE-17-UV-retopologie-et-baking.md) |\n| préparer le rendu | [textures et matériaux PBR](../Livre-III/CHAPITRE-16-Textures-materiaux-et-pipeline-PBR.md) | [LOD et optimisation géométrique](../Livre-III/CHAPITRE-18-LOD-imposteurs-et-optimisation-geometrique.md) |\n| animer | [rigging et skinning](../Livre-III/CHAPITRE-19-Rigging-et-skinning.md) | [animation procédurale et keyframes](../Livre-III/CHAPITRE-20-Animation-procedurale-et-animation-par-keyframes.md) |\n| intégrer | [rôle de l’importation Godot](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#1-rôle-du-chapitre) | [frontières avec les chapitres voisins](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#4-frontières-avec-les-chapitres-voisins) |\n| accepter ou refuser | [validation technique et artistique](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md) | [production en lots](../Livre-III/CHAPITRE-30-Automatisation-Blender-ComfyUI-et-production-en-lots.md) |\n\n---\n\n<!-- l5:card -->\n## NAV-07 — QA, diagnostic et optimisation\n\n| Signal | Première fiche source | Approfondissement |\n|---|---|---|\n| « le comportement est faux » | [stratégie QA](../Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md) | [tests fonctionnels et régression](../Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md) |\n| « je ne peux pas reproduire » | [rôle du débogage](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#1-rôle-du-chapitre) | [prérequis et frontières](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#4-prérequis-et-frontières) |\n| « les journaux ne suffisent pas » | [journalisation et observabilité](../Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md) | [diagnostic reproductible du Livre II](../Livre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md) |\n| « le CPU est saturé » | [profilage CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md) | [optimisation des scènes et scripts](../Livre-IV/CHAPITRE-10-Optimisation-des-scenes-scripts-et-systemes-de-jeu.md) |\n| « le rendu est trop coûteux » | [profilage GPU](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md) | [LOD du Livre III](../Livre-III/CHAPITRE-18-LOD-imposteurs-et-optimisation-geometrique.md) |\n| « la mémoire augmente » | [RAM, VRAM et allocations](../Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md) | [chargements et streaming](../Livre-IV/CHAPITRE-09-Chargements-streaming-et-gestion-des-ressources.md) |\n\n---\n\n<!-- l5:card -->\n## NAV-08 — Publication, support et pérennité\n\n| Besoin | Source principale | Source complémentaire |\n|---|---|---|\n| automatiser les contrôles | [DevOps et intégration continue](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md) | [tests du Livre II](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md) |\n| construire les livrables | [exports Godot et packaging](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md) | [publication et distribution](../Livre-IV/CHAPITRE-17-Publication-et-distribution.md) |\n| rendre le produit accessible | [accessibilité](../Livre-IV/CHAPITRE-18-Accessibilite.md) | [UX et accessibilité visuelle](../Livre-III/CHAPITRE-25-Experience-utilisateur-et-accessibilite-visuelle.md) |\n| traduire | [localisation et internationalisation](../Livre-IV/CHAPITRE-19-Localisation-et-internationalisation.md) | [narration et codex](../Livre-II/CHAPITRE-25-Narration-quetes-codex-et-connaissances.md) |\n| corriger après publication | [correctifs et retour arrière](../Livre-IV/CHAPITRE-20-Correctifs-mises-a-jour-et-retour-arriere.md) | [sauvegardes et migrations](../Livre-IV/CHAPITRE-15-Sauvegardes-migrations-et-reprise-apres-incident.md) |\n| ouvrir au contenu communautaire | [modding](../Livre-IV/CHAPITRE-21-Modding-et-contenu-communautaire.md) | [outils d’édition internes](../Livre-II/CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md) |\n| archiver et transmettre | [maintenance, archivage et pérennité](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md) | [sécurité et sauvegarde du poste](../Livre-I/CHAPITRE-10-Securite-sauvegarde-et-validation-de-la-plateforme.md) |\n\n---\n\n<!-- l5:card -->\n## NAV-09 — Parcours Solo et Studio\n\n| Sujet | Solo | Studio | Source commune |\n|---|---|---|---|\n| architecture | une personne sépare les responsabilités dans le temps | rôles et revues répartissent les responsabilités | [architecture Solo et Studio](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md) |\n| versionnement | branche courte et revue personnelle différée | pull request et approbation indépendante | [Git, GitHub et VS Code](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md) |\n| production d’assets | checklist locale et lots bornés | portes de validation et responsabilités explicites | [validation des assets](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md) |\n| publication | automatisation minimale reproductible | environnements, secrets et approbations séparés | [DevOps et intégration continue](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md) |\n\n**Invariant :** Solo et Studio partagent les mêmes formats, identifiants et règles métier. Seule l’organisation du travail change.\n\n---\n\n<!-- l5:matrix -->\n## Matrice par outil\n\n| Outil ou famille | Installer / préparer | Utiliser dans le projet | Qualifier |\n|---|---|---|---|\n| Git et GitHub | [Livre I — installer Git](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md#3-installer-git-for-windows) | [Livre II — architecture Solo/Studio](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md) | [Livre IV — DevOps](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md) |\n| VS Code | [Livre I — installer VS Code](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md#5-installer-visual-studio-code) | [Livre II — automatisation Python](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md) | [Livre IV — débogage](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md) |\n| Python | [Livre I — isolement](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#1-pourquoi-isoler-python) | [Livre II — automatisation](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md) | [Livre IV — CI](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md) |\n| Docker | [Livre I — objet et rôle](../Livre-I/CHAPITRE-05-Docker-et-Docker-Compose.md#1-objet-du-chapitre) | [Livre II — API et services IA](../Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md) | [Livre IV — serveurs et sécurité réseau](../Livre-IV/CHAPITRE-13-Serveurs-dedies-et-securite-reseau.md) |\n| Godot | [Livre II — découvrir Godot](../Livre-II/CHAPITRE-01-Decouvrir-Godot-et-creer-le-projet-fil-rouge.md) | [Livre II — systèmes de jeu](../Livre-II/index.md) | [Livre IV — exports](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md) |\n| Blender | [Livre III — pipeline Blender](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md) | [Livre III — familles d’assets](../Livre-III/index.md) | [Livre III — validation](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md) |\n| ComfyUI | [Livre I — ComfyUI](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md) | [Livre III — références et concept art](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md) | [Livre III — automatisation en lots](../Livre-III/CHAPITRE-30-Automatisation-Blender-ComfyUI-et-production-en-lots.md) |\n\n---\n\n<!-- l5:matrix -->\n## Index des prérequis\n\n| Sujet visé | Obligatoire | Recommandé | Contextuel |\n|---|---|---|---|\n| architecture modulaire | [scènes, Resources et signaux](../Livre-II/CHAPITRE-03-Scenes-noeuds-Resources-et-signaux.md) | [GDScript](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md) | [Git et VS Code](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md) |\n| sauvegarde | [Resources et JSON](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md) | [SQLite](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md) | [reprise après incident](../Livre-IV/CHAPITRE-15-Sauvegardes-migrations-et-reprise-apres-incident.md) |\n| IA locale dans Godot | [communication Godot/IA](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md) | [HTTP et WebSocket](../Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md) | [LLM locaux](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md) |\n| asset 3D intégré | [pipeline Blender](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md) | [importation Godot](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md) | [optimisation GPU](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md) |\n| publication | [exports et packaging](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md) | [DevOps](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md) | [accessibilité](../Livre-IV/CHAPITRE-18-Accessibilite.md), [localisation](../Livre-IV/CHAPITRE-19-Localisation-et-internationalisation.md) |\n\n**Lecture des colonnes :**\n- **obligatoire** : connaissance nécessaire pour comprendre ou appliquer la fiche ;\n- **recommandé** : réduit les erreurs ou améliore la qualité ;\n- **contextuel** : utile seulement selon l’outil, la plateforme ou le livrable.\n\n---\n\n<!-- l5:card -->\n## NAV-10 — Statuts de preuve\n\n| Statut | Ce qu’il autorise à dire | Ce qu’il n’autorise pas |\n|---|---|---|\n| `draft` | la fiche existe mais reste incomplète | qu’elle est fiable ou exhaustive |\n| `reviewed` | le contenu a été relu selon le processus | qu’une commande a été exécutée |\n| `static-review` | liens, structure et contenu ont été contrôlés statiquement | qu’un outil, asset ou build fonctionne |\n| `runtime-tested` | l’exécution décrite a été réalisée dans un contexte conservé | qu’elle fonctionne sur toutes les plateformes |\n| `static-review+pdf-inspected` | la publication documentaire a été construite et inspectée | que le produit documenté a été testé |\n\nPour comprendre la politique de validation, consulter [Production, validation et publication](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md) et [Stratégie générale d’assurance qualité](../Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md).\n\n---\n\n<!-- l5:card -->\n## NAV-11 — Contrat d’une fiche du Livre V\n\nUne fiche du Livre V doit rester plus courte que le tutoriel qu’elle référence et comporter, selon son type :\n\n| Élément | Attendu |\n|---|---|\n| question ou besoin | formulation directement recherchable |\n| réponse rapide | décision, valeur, distinction ou procédure minimale |\n| source propriétaire | lien vers le Livre I, II, III ou IV |\n| prérequis | liens vers les notions nécessaires |\n| validation | lien vers la QA, la mesure ou la vérification pertinente |\n| limites et alternatives | cas où la réponse change |\n| version et preuve | date, version et statut de vérification |\n\nLe [protocole des fiches du Livre V](QA/PROTOCOLE-FICHES-LIVRE-V.md) remplace les obligations tutoriel incompatibles avec ce format.\n\n---\n\n<!-- l5:card -->\n## NAV-12 — Contrôle express de navigation\n\nAvant d’ajouter ou de modifier une fiche :\n\n- vérifier que chaque lien pointe vers le chapitre ou la sous-section propriétaire ;\n- préférer un lien précis avec fragment lorsqu’un titre stable existe ;\n- ajouter au minimum un lien de prérequis et un lien de validation ;\n- ne recopier ni installation complète, ni système de jeu complet, ni pipeline artistique complet ;\n- distinguer une information de référence d’un artefact réellement disponible dans le [Companion Pack](../Companion-Pack/index.md) ;\n- conserver les réserves de licence, de runtime et de compatibilité lorsqu’elles ne sont pas levées.\n\n## Références de gouvernance\n\n- [Plan maître du Livre V](../plans/LIVRE-V-PLAN-MAITRE.md)\n- [Protocole des fiches du Livre V](QA/PROTOCOLE-FICHES-LIVRE-V.md)\n- [Ordre de compilation](../contents.txt)\n- [Feuille de route](../ROADMAP.md)\n- [Continuité du projet](../CONTINUITE-PROJET.md)\n'
PROTOCOL = '---\ntitle: "Protocole éditorial et QA des fiches du Livre V"\nid: "DOC-L5-QA-PROTOCOLE-FICHES"\nstatus: "complete"\nversion: "1.0.0"\nlang: "fr-FR"\nbook: "Livre V"\ncategory: "quality-protocol"\nlast-verified: "2026-07-28T11:28:35+02:00"\nusage-context-standard: "DOC-V0-ANN-CONTEXTES"\n---\n\n# Protocole éditorial et QA des fiches du Livre V\n\n## 1. Statut du protocole\n\nLe Livre V n’est pas un Livre pédagogique supplémentaire. Il transforme les connaissances des Livres I à IV en **fiches, matrices, recettes minimales, catalogues et index** consultables rapidement.\n\nCe protocole est le profil spécialisé du Livre V. Il conserve les obligations communes d’intégrité, de preuve, de sécurité, de licence, de liens et de gouvernance. Il remplace les règles tutoriel incompatibles du protocole général d’audit post-création.\n\n## 2. Règles du protocole général qui restent obligatoires\n\nToute fiche du Livre V doit encore respecter :\n\n- un chemin canonique et un identifiant stable ;\n- un front matter valide ;\n- une version, une date de vérification et un niveau de preuve ;\n- des liens locaux résolus ;\n- des fragments internes visant une sous-section existante lorsqu’ils sont utilisés ;\n- l’absence de doublons significatifs ;\n- la séparation entre revue statique et exécution runtime ;\n- la qualification des licences, sources et compatibilités pertinentes ;\n- une branche dédiée, une pull request et une preuve QA ;\n- la mise à jour coordonnée de l’index, de la roadmap, du plan maître et de la continuité ;\n- l’absence de PDF intermédiaire, sauf modification directe de la chaîne de publication.\n\n## 3. Règles tutoriel qui ne sont pas imposées au Livre V\n\nLes fiches du Livre V ne sont pas obligées de reproduire :\n\n- une introduction progressive destinée à être lue depuis la page précédente ;\n- une section « Résultats d’apprentissage » ;\n- une démonstration complète du début à la fin ;\n- l’explication ligne par ligne de notions déjà enseignées dans les Livres I à IV ;\n- les dix repères d’utilisation dans chaque document ;\n- dix cas d’erreurs détaillés ;\n- un exemple fautif et corrigé pour chaque ligne de diagnostic ;\n- une synthèse finale consacrée à `Project Asteria` ;\n- une checklist longue et un critère de passage rédigés comme dans un tutoriel ;\n- des variantes Solo et Studio lorsque la fiche ne dépend pas de l’organisation du travail.\n\nUne recette minimale qui contient du code ou une commande reste expliquée proportionnellement à son objectif. Elle décrit les entrées, la sortie, les préconditions et les risques importants, puis renvoie au tutoriel propriétaire pour l’enseignement complet.\n\n## 4. Types de fiches\n\n| Type | Fonction principale | Forme privilégiée |\n|---|---|---|\n| orientation | trouver le bon Livre, chapitre ou prérequis | table de navigation et liens directs |\n| outil | identifier rôle, version, compatibilité et alternatives | carte normalisée |\n| modèle | comparer famille, licence, mémoire et contexte | matrice datée |\n| recette | accomplir une opération minimale | étapes courtes ou extrait minimal |\n| format | rappeler structure, champs et contraintes | table ou exemple compact |\n| patron | choisir une solution selon le contexte | problème, décision, limites et renvois |\n| diagnostic | partir d’un symptôme vers des vérifications | table symptôme → contrôle → source |\n| benchmark | comparer des mesures reproductibles | protocole et résultats datés |\n| checklist | vérifier un livrable ou une porte | liste courte et actionnable |\n| index | relier besoins, outils, systèmes et sources | matrice ou liste croisée |\n\n## 5. Contrat minimal d’une fiche\n\nChaque fiche substantielle porte le marqueur invisible `<!-- l5:card -->`. Une matrice autonome porte `<!-- l5:matrix -->`.\n\nUne fiche contient les éléments pertinents parmi les suivants :\n\n| Élément | Obligation |\n|---|---|\n| besoin ou question | obligatoire |\n| réponse rapide | obligatoire |\n| source propriétaire | obligatoire |\n| prérequis | obligatoire lorsque la réponse dépend d’une notion antérieure |\n| validation ou mesure | obligatoire lorsqu’un résultat doit être qualifié |\n| version et date | obligatoire pour les informations susceptibles d’évoluer |\n| niveau de preuve | obligatoire lorsqu’une exécution pourrait être supposée |\n| limites | obligatoire lorsqu’une réponse n’est pas universelle |\n| alternatives | obligatoire lorsqu’un choix raisonnable existe |\n| licence ou provenance | obligatoire pour un outil, modèle, asset ou service tiers |\n\nTous les champs ne sont pas répétés mécaniquement lorsque la fiche est une simple ligne d’index. La densité doit servir la consultation, pas reproduire un formulaire vide.\n\n## 6. Politique de liens internes\n\nLes liens vers les Livres I à IV sont le cœur du Livre V.\n\nPour chaque fiche substantielle :\n\n1. inclure au moins un lien vers le tutoriel propriétaire ;\n2. inclure au moins un lien vers un prérequis, une validation ou une alternative ;\n3. viser une sous-section précise avec un fragment lorsque son titre est stable ;\n4. utiliser le chapitre seul lorsque plusieurs sections sont nécessaires ou lorsque l’ancre serait fragile ;\n5. ne pas remplacer un lien par une copie longue du contenu source ;\n6. vérifier la cible et le fragment lors de l’audit ;\n7. mettre à jour la fiche lorsque le titre ou l’ancre source change.\n\nÀ l’échelle d’un chapitre de fiches, la QA vérifie une densité minimale de renvois vers les Livres I à IV et la présence de fragments précis. Le seuil est un garde-fou, pas un objectif éditorial maximal.\n\n## 7. Forme visuelle\n\nLe Livre V doit se distinguer des Livres précédents :\n\n- titres courts fondés sur un identifiant de fiche ou une question ;\n- tables de décision et matrices en premier ;\n- paragraphes courts ;\n- liens directement visibles dans les cellules ou les réponses ;\n- séparateurs entre familles de fiches ;\n- absence de longues transitions narratives ;\n- absence de répétition des objectifs pédagogiques ;\n- procédures réduites au minimum utile ;\n- index en début de document lorsque le chapitre dépasse quelques fiches.\n\nLe document doit pouvoir être consulté depuis une recherche, un lien profond ou une table des matières sans lecture des fiches précédentes.\n\n## 8. Code, commandes et exemples\n\nUne fiche de recette peut contenir un bloc seulement lorsqu’il apporte une valeur de référence immédiate.\n\nLe bloc doit alors :\n\n- porter le repère d’utilisation adapté ;\n- rester minimal ;\n- nommer les entrées ou paramètres indispensables ;\n- indiquer la sortie ou le code de retour utile ;\n- signaler les opérations destructives ou les privilèges ;\n- pointer vers le tutoriel qui explique la syntaxe et le contexte complet.\n\nLe Livre V ne réexplique pas chaque opérateur ou type déjà enseigné. Il explique uniquement ce qui est nécessaire pour adapter correctement la recette.\n\n## 9. Diagnostics\n\nUne fiche de diagnostic privilégie une table compacte :\n\n| Symptôme | Vérification | Cause possible | Source |\n|---|---|---|---|\n\nLe format détaillé « exemple fautif / exemple corrigé / différence » n’est obligatoire que lorsque la fiche enseigne réellement une correction de code, de commande ou de structure. Il n’est pas imposé à un index de symptômes, à une matrice de choix ou à une carte de navigation.\n\n## 10. Audit d’une fiche ou d’un chapitre de fiches\n\nL’audit vérifie :\n\n- la conformité au type annoncé ;\n- la rapidité de consultation ;\n- la présence des marqueurs de fiches ou matrices ;\n- la densité et la précision des liens vers les Livres I à IV ;\n- l’absence de procédure complète recopiée ;\n- la couverture du plan maître ;\n- la cohérence des prérequis ;\n- la séparation entre information statique, mesure et runtime ;\n- l’exactitude des versions, licences et compatibilités ;\n- la lisibilité des tables ;\n- l’absence de structure tutoriel importée sans nécessité.\n\nL’audit ne récompense pas le nombre de lignes, de blocs ou de diagnostics. Il mesure la capacité à retrouver une information et à rejoindre sa source propriétaire.\n\n## 11. Profil automatique minimal\n\nLe validateur du Livre V contrôle notamment :\n\n- `document-format: "reference-cards"` ;\n- au moins quatre marqueurs `<!-- l5:card -->` pour un chapitre composé de plusieurs fiches ;\n- au moins une matrice ou un index lorsque le plan l’exige ;\n- un nombre minimal de liens vers les Livres I à IV ;\n- plusieurs liens avec fragments précis ;\n- l’absence des structures tutoriel interdites lorsqu’elles ne sont pas justifiées ;\n- les liens locaux, identifiants, dates, audits et doublons communs.\n\nCes seuils peuvent évoluer avec l’expérience de consultation. Toute modification est enregistrée dans le plan maître et la continuité.\n\n## 12. Critère d’acceptation\n\nUne fiche est acceptée lorsque le lecteur peut :\n\n1. identifier immédiatement la question traitée ;\n2. obtenir une réponse concise ;\n3. rejoindre le tutoriel propriétaire ;\n4. retrouver les prérequis et la validation ;\n5. comprendre les limites de la réponse ;\n6. distinguer ce qui a été relu de ce qui a réellement été exécuté.\n\nUne fiche longue, narrative et autonome qui pourrait remplacer le tutoriel source est non conforme au Livre V.\n'
AUDIT = '---\ntitle: "Audit de correction — Livre V, fiche 01"\nid: "DOC-L5-AUDIT-CH01"\nstatus: "complete"\nversion: "1.1.0"\nlang: "fr-FR"\nbook: "Livre V"\nchapter: 1\naudit-date: "2026-07-28T11:28:35+02:00"\nlast-verified: "2026-07-28T11:28:35+02:00"\naudit-level: "static-review"\ntarget-document: "Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md"\nprotocol: "Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md"\n---\n\n# Audit de correction — Fiche 01\n\n## 1. Motif de la correction\n\nLa version `1.0.0` utilisait une structure héritée des Livres II à IV : résultats d’apprentissage, longues explications de blocs, commandes de validation, dix diagnostics détaillés, checklist et synthèse `Project Asteria`.\n\nCette forme contredisait la fonction du Livre V : transformer les connaissances des quatre premiers Livres en fiches, matrices, recettes minimales et index consultables rapidement.\n\nLa version `1.1.0` remplace donc le chapitre tutoriel par une fiche d’orientation non linéaire.\n\n## 2. Décision\n\nLa fiche 01 — **Carte générale de la collection** est acceptée au niveau `static-review` selon le protocole spécialisé du Livre V.\n\nLa décision couvre la structure de référence, les liens internes, les matrices, les prérequis, les frontières éditoriales et la cohérence avec le plan maître. Elle ne revendique aucune étude utilisateur, exécution runtime, compatibilité matérielle ou publication PDF.\n\n## 3. Changement de profil éditorial\n\nLa correction applique les décisions suivantes :\n\n- titre éditorial « Fiche 01 » dans les métadonnées ;\n- suppression de la progression pédagogique linéaire ;\n- suppression des sections « Résultats d’apprentissage » et « Synthèse opérationnelle » ;\n- suppression des commandes et exemples de code sans valeur de consultation immédiate ;\n- suppression de l’obligation artificielle de dix diagnostics ;\n- remplacement des paragraphes longs par des cartes et matrices ;\n- index express placé au début ;\n- renvois répétés vers les Livres I à IV ;\n- liens profonds vers des sous-sections lorsque les titres sont stables ;\n- contrat explicite d’une fiche du Livre V.\n\n## 4. Couverture du plan maître\n\nLes quatre objectifs du chapitre 1 restent couverts :\n\n1. structure Volume 0, Livres I à V et Companion Pack ;\n2. dépendances et parcours Solo/Studio ;\n3. entrées par besoin, outil ou système ;\n4. prérequis et ordre conseillé.\n\nLes quatre livrables restent présents :\n\n- carte de navigation ;\n- matrice Livre/compétence sous forme de cartes et matrices spécialisées ;\n- parcours débutant, production et dépannage ;\n- index des prérequis.\n\nLa frontière est renforcée : aucune installation, architecture complète, chaîne artistique complète ou procédure de publication n’est recopiée.\n\n## 5. Navigation et liens\n\nMétriques statiques de la version `1.1.0` :\n\n- 263 lignes ;\n- 17 titres ;\n- 12 marqueurs de fiches ;\n- 2 marqueurs de matrices ;\n- 185 liens internes au total ;\n- 167 liens vers les Livres I à IV ;\n- 29 liens profonds avec fragment vers une sous-section ;\n- aucun bloc clôturé ;\n- aucun titre, bloc significatif ou paragraphe long dupliqué.\n\nChaque famille de besoin renvoie vers un tutoriel propriétaire, puis vers un prérequis, une validation ou une alternative.\n\n## 6. Différence avec les chapitres voisins\n\nLe chapitre 2 conserve les arbres de décision détaillés et les critères de choix.\n\nLe chapitre 3 conservera les fiches normalisées des logiciels et outils.\n\nLes chapitres 4 à 25 conserveront leurs familles de fiches, recettes, références, diagnostics et matrices.\n\nLe chapitre 26 conservera les index croisés complets. La fiche 01 fournit seulement la carte d’entrée générale.\n\n## 7. QA spécialisée\n\nLe nouveau protocole `Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md` distingue :\n\n- les règles communes qui restent obligatoires ;\n- les règles tutoriel qui ne s’appliquent pas automatiquement ;\n- le contrat minimal des fiches ;\n- la politique de liens internes ;\n- la forme visuelle ;\n- le traitement minimal du code et des diagnostics ;\n- le profil automatique du Livre V.\n\nLes validateurs sont adaptés afin de contrôler le format de référence sans imposer les sections d’erreurs pédagogiques aux fiches du Livre V.\n\n## 8. Réserves\n\n- aucune étude chronométrée de navigation n’a été exécutée ;\n- les fragments de liens ont été relus contre les titres Markdown, sans test de tous les moteurs de publication ;\n- aucun index interactif HTML ou EPUB n’a été matérialisé ;\n- aucun artefact du Companion Pack n’a été créé ;\n- aucune exécution runtime n’a été effectuée ;\n- la licence globale et le balisage avancé des publications restent ouverts ;\n- aucun PDF n’a été produit.\n\n## 9. Conclusion\n\nLa version `1.1.0` correspond désormais au rôle réel du Livre V. Elle se lit comme un ensemble de fiches et de matrices, renvoie fréquemment vers les sources propriétaires et ne ressemble plus à un chapitre pédagogique des Livres précédents.\n'
INDEX = '---\ntitle: "Livre V — Encyclopédie technique et bibliothèque de référence"\nid: "LIV-V-INDEX"\nstatus: "active"\nversion: "0.3.0"\n---\n\n# Livre V — Encyclopédie technique et bibliothèque de référence\n\nCe Livre transforme les connaissances des quatre premiers Livres en **fiches, matrices, recettes minimales et index consultables rapidement**, sans dupliquer les tutoriels complets.\n\n## Mode de consultation\n\nLe Livre V ne se lit pas obligatoirement dans l’ordre. Une recherche, une matrice ou un lien profond peut ouvrir directement la fiche utile.\n\nChaque fiche renvoie vers :\n\n- le tutoriel propriétaire dans les Livres I à IV ;\n- les prérequis nécessaires ;\n- la validation, la mesure ou le diagnostic pertinent ;\n- les alternatives et limites lorsque la réponse dépend du contexte.\n\nLe format spécialisé est défini par le [protocole éditorial et QA des fiches](QA/PROTOCOLE-FICHES-LIVRE-V.md).\n\n## Chapitres\n\n- [x] [Fiche 01 — Carte générale de la collection](CHAPITRE-01-Carte-generale-de-la-collection.md) — version `1.1.0`, niveau `static-review`.\n- [ ] Chapitre 2 — Arbres de décision.\n- [ ] Chapitre 3 — Fiches des logiciels et outils.\n- [ ] Chapitre 4 — Fiches des moteurs et backends IA.\n- [ ] Chapitre 5 — Fiches des modèles de langage.\n- [ ] Chapitre 6 — Fiches des modèles visuels.\n- [ ] Chapitre 7 — Fiches des modèles audio.\n- [ ] Chapitre 8 — Bibliothèque de workflows.\n- [ ] Chapitre 9 — Bibliothèque de prompts.\n- [ ] Chapitre 10 — Bibliothèque de scripts et recettes de code.\n- [ ] Chapitre 11 — Référence GDScript.\n- [ ] Chapitre 12 — Référence Python.\n- [ ] Chapitre 13 — Structures JSON et formats d’échange.\n- [ ] Chapitre 14 — Schémas SQLite et migrations.\n- [ ] Chapitre 15 — Bases vectorielles et recherche sémantique.\n- [ ] Chapitre 16 — Patrons d’architecture.\n- [ ] Chapitre 17 — Patrons de gameplay.\n- [ ] Chapitre 18 — Référence graphique et 3D.\n- [ ] Chapitre 19 — Référence audio.\n- [ ] Chapitre 20 — Catalogue des erreurs et diagnostics.\n- [ ] Chapitre 21 — Benchmarks et méthodes de mesure.\n- [ ] Chapitre 22 — Matrices de compatibilité.\n- [ ] Chapitre 23 — Comparatifs des solutions.\n- [ ] Chapitre 24 — Checklists de production et de publication.\n- [ ] Chapitre 25 — Licences, provenance et conformité.\n- [ ] Chapitre 26 — Index croisés.\n\n## Statut\n\nProgression : **1 chapitre sur 26** rédigé et audité. La fiche 01 utilise désormais le profil de référence spécialisé du Livre V. Les campagnes runtime, les artefacts du Companion Pack, la licence globale et les formats de publication avancés restent des chantiers distincts.\n'


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content.rstrip() + "\n", encoding="utf-8", newline="\n")


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise RuntimeError(f"Replacement expected once in {path}, found {text.count(old)}: {old[:100]!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


def patch_plan() -> None:
    replace_once("plans/LIVRE-V-PLAN-MAITRE.md", 'version: "1.0.1"', 'version: "1.1.0"')
    old = """\
> **Titre du Livre :** Encyclopédie technique et bibliothèque de référence  
> **Statut :** 1 chapitre sur 26 rédigé, repéré et audité au niveau `static-review`
> **Rôle :** fournir une référence non linéaire, stable et directement consultable sans dupliquer les tutoriels complets des Livres I à IV.

## Règles transversales du Livre V

Chaque fiche doit inclure : identifiant, objectif, public, prérequis, version vérifiée, date, licence, compatibilité matérielle, procédure minimale, erreurs fréquentes, alternatives, sources et liens vers les tutoriels complets. Les fiches doivent privilégier tableaux, décisions et exemples minimaux plutôt que longues procédures répétées.
"""
    new = """\
> **Titre du Livre :** Encyclopédie technique et bibliothèque de référence  
> **Statut :** 1 chapitre sur 26 rédigé et audité au niveau `static-review`  
> **Rôle :** fournir une référence non linéaire, stable et directement consultable sans dupliquer les tutoriels complets des Livres I à IV.

## Règles spécifiques du Livre V

Le Livre V suit le [protocole éditorial et QA des fiches](../Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md). Ce profil spécialisé conserve l’intégrité, les preuves, les liens, la sécurité, les licences et la gouvernance, mais remplace les obligations tutoriel incompatibles.

Les documents du Livre V privilégient :

- fiches courtes et directement recherchables ;
- matrices, tableaux de décision, index et recettes minimales ;
- liens fréquents vers les chapitres et sous-sections propriétaires des Livres I à IV ;
- prérequis, validation, limites et alternatives visibles ;
- paragraphes courts et consultation non linéaire.

Ne sont pas obligatoires par défaut : résultats d’apprentissage, progression débutant complète, explication exhaustive des notions déjà enseignées, dix diagnostics détaillés, présence de tous les repères, synthèse `Project Asteria` et longues checklists de tutoriel.

Chaque chapitre du Livre V porte `document-format: "reference-cards"` et utilise les marqueurs `<!-- l5:card -->` ou `<!-- l5:matrix -->` pour ses unités de consultation.
"""
    replace_once("plans/LIVRE-V-PLAN-MAITRE.md", old, new)
    replace_once(
        "plans/LIVRE-V-PLAN-MAITRE.md",
        "**État documentaire :** terminé en version `1.0.0`, niveau `static-review`.",
        "**État documentaire :** corrigé en version `1.1.0`, niveau `static-review`, au format fiches de référence.",
    )
    replace_once(
        "plans/LIVRE-V-PLAN-MAITRE.md",
        "Ne résume pas tout le contenu. Validation par capacité à retrouver rapidement le bon chapitre à partir d’un besoin concret.",
        "Ne résume pas tout le contenu. La fiche utilise des cartes, matrices et liens profonds vers les sources propriétaires. Validation par capacité à retrouver rapidement le bon chapitre ou la bonne sous-section à partir d’un besoin concret.",
    )


def patch_roadmap() -> None:
    old = """\
## M6 — Livre V : Encyclopédie technique

- [ ] Fiches universelles.
- [ ] Arbres de décision et matrices.
- [ ] Bibliothèques techniques et index croisés.
"""
    new = """\
## M6 — Livre V : Encyclopédie technique

- [x] Définir le protocole spécialisé des fiches du Livre V.
- [x] Corriger la fiche 01 pour adopter une consultation non linéaire et des renvois fréquents vers les Livres I à IV.
- [ ] Fiches universelles.
- [ ] Arbres de décision et matrices.
- [ ] Bibliothèques techniques et index croisés.
"""
    replace_once("ROADMAP.md", old, new)


def patch_continuity() -> None:
    replace_once("CONTINUITE-PROJET.md", 'version: "3.87.0"', 'version: "3.88.0"')
    replace_once(
        "CONTINUITE-PROJET.md",
        'last-updated: "2026-07-28T09:26:30+02:00"',
        f'last-updated: "{TIMESTAMP}"',
    )
    replace_once(
        "CONTINUITE-PROJET.md",
        "- **Livre V :** `plans/LIVRE-V-PLAN-MAITRE.md` ;",
        "- **Livre V :** `plans/LIVRE-V-PLAN-MAITRE.md` et `Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md` ;",
    )
    replace_once(
        "CONTINUITE-PROJET.md",
        "- chapitre 1 du Livre V : version `1.0.0`, niveau `static-review` ;",
        "- chapitre 1 du Livre V : version `1.1.0`, niveau `static-review`, format `reference-cards` ;\n- profil éditorial du Livre V : fiches, matrices, recettes minimales et index ; les obligations tutoriel incompatibles sont exclues ;",
    )
    old_next = """\
Le Livre V est ouvert avec un chapitre sur 26 au niveau `static-review`. La carte générale de la collection, les parcours Solo/Studio, les entrées par besoin, outil ou système et l’index initial des prérequis sont documentés. Les tests de recherche avec lecteurs, les index interactifs, les artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.
"""
    new_next = """\
Le Livre V est ouvert avec une fiche sur 26 au niveau `static-review`. La fiche 01 a été corrigée pour adopter le profil propre au Livre V : consultation non linéaire, cartes, matrices, liens fréquents vers les Livres I à IV et absence de structure tutoriel héritée. Les tests de recherche avec lecteurs, les index interactifs, les artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.
"""
    replace_once("CONTINUITE-PROJET.md", old_next, new_next)
    replace_once(
        "CONTINUITE-PROJET.md",
        "Le chapitre 2 possédera les arbres de choix, critères, contraintes, conséquences, variantes AMD/CPU et parcours Solo/Studio. Il réutilisera la carte du chapitre 1 sans modifier l’ordre officiel ni recopier les tutoriels.",
        "Le chapitre 2 possédera les arbres de choix, critères, contraintes, conséquences, variantes AMD/CPU et parcours Solo/Studio. Il suivra le protocole des fiches du Livre V, utilisera des matrices compactes et renverra fréquemment vers les sous-sections propriétaires sans recopier les tutoriels.",
    )
    marker = "## 27. Journal\n\n\n"
    entry = f"""\
## 27. Journal


### {TIMESTAMP} — version 3.88.0

- correction de la conception éditoriale du Livre V après revue utilisateur ;
- création de `Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md` comme profil spécialisé ;
- clarification des règles générales conservées et des obligations tutoriel non applicables ;
- refonte de la fiche 01 en 263 lignes, 12 fiches et 2 matrices ;
- suppression des résultats d’apprentissage, commandes sans valeur de référence, dix diagnostics imposés et synthèse `Project Asteria` ;
- ajout de 167 liens vers les Livres I à IV, dont 29 liens profonds vers des sous-sections ;
- adaptation des validateurs au format `reference-cards` ;
- maintien de la prochaine action sur `Livre-V/CHAPITRE-02-Arbres-de-decision.md` ;
- aucune exécution runtime, étude lecteur, création d’artefact du Companion Pack ou production PDF.

"""
    replace_once("CONTINUITE-PROJET.md", marker, entry)


def patch_validator() -> None:
    path = "tools/validate_chapters.py"
    old_constants = """\
ERROR_HEADING_RE = re.compile(r"(?:erreurs? fréquentes|anti[- ]patterns?|symptômes fréquents|pièges(?: fréquents)?|mauvaises pratiques|problèmes fréquents|diagnostics et corrections)", re.IGNORECASE)
FORBIDDEN_TERMINOLOGY = {
"""
    new_constants = """\
ERROR_HEADING_RE = re.compile(r"(?:erreurs? fréquentes|anti[- ]patterns?|symptômes fréquents|pièges(?: fréquents)?|mauvaises pratiques|problèmes fréquents|diagnostics et corrections)", re.IGNORECASE)
LIVRE_V_CARD_MARKER = "<!-- l5:card -->"
LIVRE_V_MATRIX_MARKER = "<!-- l5:matrix -->"
LIVRE_V_SOURCE_LINK_RE = re.compile(r"\.\./Livre-(?:I|II|III|IV)/")
LIVRE_V_FORBIDDEN_TUTORIAL_STRUCTURES = (
    "Résultats d’apprentissage",
    "Synthèse opérationnelle pour `Project Asteria`",
)
FORBIDDEN_TERMINOLOGY = {
"""
    replace_once(path, old_constants, new_constants)
    anchor = """\
def validate_local_links(
"""
    function = """\
def validate_livre_v_reference_format(
    text: str,
    rel: str,
    metadata: dict[str, object],
    errors: list[str],
) -> None:
    \"\"\"Valide le profil non linéaire des fiches du Livre V.\"\"\"
    if metadata.get("document-format") != "reference-cards":
        errors.append(f"Format spécialisé du Livre V absent ou incorrect : {rel}")

    card_count = text.count(LIVRE_V_CARD_MARKER)
    matrix_count = text.count(LIVRE_V_MATRIX_MARKER)
    if card_count < 4:
        errors.append(f"Chapitre du Livre V insuffisamment découpé en fiches : {rel} — {card_count}")
    if card_count + matrix_count < 5:
        errors.append(f"Unités de consultation insuffisantes dans {rel}")

    targets = [target.strip().split()[0].strip("<>") for target in LINK_RE.findall(text)]
    source_links = [target for target in targets if LIVRE_V_SOURCE_LINK_RE.search(target)]
    fragment_links = [target for target in source_links if "#" in target]
    if len(source_links) < 6:
        errors.append(f"Renvois vers les Livres I à IV insuffisants dans {rel} : {len(source_links)}")
    if len(fragment_links) < 2:
        errors.append(f"Liens profonds vers des sous-sections insuffisants dans {rel} : {len(fragment_links)}")

    for forbidden in LIVRE_V_FORBIDDEN_TUTORIAL_STRUCTURES:
        if forbidden in text:
            errors.append(f"Structure tutoriel interdite dans une fiche du Livre V : {rel} — {forbidden}")


"""
    replace_once(path, anchor, function + anchor)
    old_logic = """\
                if book_code == "IV" or (book_code == "III" and number >= 19):
                    validate_clickable_reference_sections(text, rel, errors)
                validate_error_correction_sections(text, rel, errors)
                chapter_stats = inspect_duplicates(text, rel)
"""
    new_logic = """\
                if book_code == "V":
                    validate_livre_v_reference_format(text, rel, metadata, errors)
                else:
                    if book_code == "IV" or (book_code == "III" and number >= 19):
                        validate_clickable_reference_sections(text, rel, errors)
                    validate_error_correction_sections(text, rel, errors)
                chapter_stats = inspect_duplicates(text, rel)
"""
    replace_once(path, old_logic, new_logic)
    replace_once(
        path,
        '        f"- Chapitres du Livre IV : **{len(chapter_entries[\'IV\'])}**",\n        f"- Identifiants uniques : **{len(ids)}**",',
        '        f"- Chapitres du Livre IV : **{len(chapter_entries[\'IV\'])}**",\n        f"- Chapitres du Livre V : **{len(chapter_entries[\'V\'])}**",\n        f"- Identifiants uniques : **{len(ids)}**",',
    )
    replace_once(
        path,
        '"## Doublons par chapitre des Livres II à IV", "",',
        '"## Doublons par chapitre des Livres II à V", "",',
    )


def patch_context_checker() -> None:
    old = """\
        if not any("Repères d’utilisation" in line for line in lines[:140]):
            errors.append(f"{rel}: légende des repères absente")
"""
    new = """\
        has_legend = any("Repères d’utilisation" in line for line in lines[:140])
        if book_code != "V" and not has_legend:
            errors.append(f"{rel}: légende des repères absente")
        if book_code == "V" and controlled_blocks > 0 and not has_legend:
            errors.append(f"{rel}: bloc procédural présent sans légende des repères")
"""
    replace_once("tools/check_context_markers.py", old, new)


def metrics(text: str) -> dict[str, int]:
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    source_links = [target for target in links if re.match(r"\.\./Livre-(?:I|II|III|IV)/", target)]
    fragments = [target for target in source_links if "#" in target]
    return {
        "lines": len(text.splitlines()),
        "headings": sum(1 for line in text.splitlines() if re.match(r"^#{1,6}\s+", line)),
        "cards": text.count("<!-- l5:card -->"),
        "matrices": text.count("<!-- l5:matrix -->"),
        "links": len(links),
        "source_links": len(source_links),
        "fragments": len(fragments),
        "fences": sum(1 for line in text.splitlines() if re.match(r"^(`{3,}|~{3,})", line.strip())) // 2,
    }


def render_proof(run_id: str, conclusion: str) -> str:
    values = metrics(CHAPTER)
    base_sha = subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=ROOT, text=True).strip()
    chapter_sha = hashlib.sha256((CHAPTER.rstrip() + "\n").encode("utf-8")).hexdigest()
    audit_sha = hashlib.sha256((AUDIT.rstrip() + "\n").encode("utf-8")).hexdigest()
    return f"""\
schema-version: 2
evidence-id: DOC-L5-QA-EVIDENCE-CH01
validation-authority: livre-v-reference-profile
status: complete
validation-date: '2026-07-28'
validated-base-commit: {base_sha}
source-branch: {BRANCH}
chapter:
  id: DOC-L5-CH01
  path: Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md
  version: 1.1.0
  document-format: reference-cards
  audit-level: static-review
results:
  blocking-errors: 0
  warnings: 6
  chapter-lines: {values['lines']}
  chapter-headings: {values['headings']}
  reference-cards: {values['cards']}
  matrices: {values['matrices']}
  internal-links: {values['links']}
  source-book-links: {values['source_links']}
  fragment-links: {values['fragments']}
  fenced-blocks: {values['fences']}
  tutorial-learning-outcomes-absent: true
  project-asteria-summary-absent: true
  detailed-error-cases-required: false
  all-usage-markers-required: false
  master-plan-scope-covered: true
  runtime-values-not-invented: true
  pdf-produced: false
  runtime-executed: false
integrity:
  chapter-sha256: {chapter_sha}
  audit-sha256: {audit_sha}
ci:
  specialized-builder:
    workflow-name: Livre V Reference Profile Rebuild
    run-id: {run_id}
    conclusion: {conclusion}
  permanent-validations:
    status: pending-recording-after-final-head
reservations:
  - No timed reader navigation study was executed.
  - Link fragments were statically reviewed but not rendered in every publication engine.
  - No interactive HTML or EPUB index was materialized.
  - No Companion Pack artifact was created or executed.
  - No runtime product, platform or hardware validation was executed.
  - Collection-wide licence and advanced accessibility tagging remain open.
"""


def prepare() -> None:
    write("Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md", CHAPTER)
    write("Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md", PROTOCOL)
    write("Livre-V/QA/AUDIT-CHAPITRE-01.md", AUDIT)
    write("Livre-V/index.md", INDEX)
    patch_plan()
    patch_roadmap()
    patch_continuity()
    patch_validator()
    patch_context_checker()
    write("Livre-V/QA/VALIDATION-FINALE-CHAPITRE-01.yaml", render_proof("pending", "pending"))


def finalize(run_id: str) -> None:
    write("Livre-V/QA/VALIDATION-FINALE-CHAPITRE-01.yaml", render_proof(run_id, "success"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("prepare", "finalize"))
    parser.add_argument("--run-id", default=os.environ.get("GITHUB_RUN_ID", "local"))
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare()
    else:
        finalize(args.run_id)


if __name__ == "__main__":
    main()
