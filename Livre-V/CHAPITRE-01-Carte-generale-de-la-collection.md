---
title: "Livre V — Fiche 01 : Carte générale de la collection"
id: "DOC-L5-CH01"
status: "reviewed"
version: "1.1.0"
lang: "fr-FR"
book: "Livre V"
chapter: 1
last-verified: "2026-07-28T11:28:35+02:00"
audit-status: "complete"
audit-date: "2026-07-28T11:28:35+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-01.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "collection-navigation"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Carte générale de la collection

> **Type de document :** fiche d’orientation et index de navigation.
> **Lecture :** non linéaire ; ouvrir directement la fiche correspondant au besoin.
> **Principe :** le Livre V résume, classe et relie. Les procédures complètes restent dans les Livres I à IV.

## Index express

| Je cherche à… | Ouvrir d’abord | Continuer avec |
|---|---|---|
| comprendre les règles communes | [Volume 0 — Les 21 règles fondamentales](../Volume-0/CHAPITRE-02-Les-21-regles-fondamentales.md) | [architecture documentaire](../Volume-0/CHAPITRE-03-Architecture-documentaire.md), [standards techniques](../Volume-0/CHAPITRE-07-Standards-techniques.md) |
| préparer le poste de travail | [Livre I — Matériel, Windows et pilotes AMD](../Livre-I/CHAPITRE-01-Materiel-Windows-pilotes-AMD-et-acceleration.md) | [terminaux Windows](../Livre-I/CHAPITRE-02-Terminal-PowerShell-et-outils-Windows.md), [Git et VS Code](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md#3-installer-git-for-windows) |
| isoler un outil Python | [Pourquoi isoler Python](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#1-pourquoi-isoler-python) | [choisir une version](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#3-choisir-une-version-de-python) |
| déployer un service local | [Docker — objet du chapitre](../Livre-I/CHAPITRE-05-Docker-et-Docker-Compose.md#1-objet-du-chapitre) | [backend et contraintes](../Livre-I/CHAPITRE-05-Docker-et-Docker-Compose.md#3-positionnement-officiel-au-18-juillet-2026) |
| construire l’architecture du jeu | [Livre II — architecture modulaire](../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md#3-périmètre-et-frontières) | [services et injection](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md), [tests](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md) |
| choisir une stratégie de données | [Resources, JSON et configurations](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md) | [SQLite](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md), [sauvegardes](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#3-périmètre-et-frontières) |
| intégrer une IA locale | [LLM locaux](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md) | [mémoire vectorielle](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md), [communication Godot/IA](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md) |
| produire un asset | [Livre III — préproduction](../Livre-III/CHAPITRE-01-Preproduction-et-cahier-des-charges-artistique.md) | [pipeline Blender](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md), [validation des assets](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md) |
| importer dans Godot | [Importation — rôle](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#1-rôle-du-chapitre) | [frontières d’intégration](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#4-frontières-avec-les-chapitres-voisins) |
| reproduire un défaut | [Débogage — rôle](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#1-rôle-du-chapitre) | [prérequis et frontières](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#4-prérequis-et-frontières), [observabilité](../Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md) |
| optimiser | [Profilage CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md) | [profilage GPU](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md), [RAM et VRAM](../Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md) |
| publier et maintenir | [DevOps et intégration continue](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md) | [exports](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md), [maintenance et pérennité](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md) |

---

<!-- l5:card -->
## NAV-01 — Rôle des sept ensembles

| Ensemble | Fonction | À ouvrir pour… | Ne remplace pas… |
|---|---|---|---|
| [Volume 0](../Volume-0/index.md) | normes et gouvernance | nommer, versionner, sourcer, publier | les tutoriels techniques |
| [Livre I](../Livre-I/index.md) | plateforme locale | installer et sécuriser les outils | l’architecture du jeu |
| [Livre II](../Livre-II/index.md) | développement et systèmes | construire les règles, données et services | la production artistique |
| [Livre III](../Livre-III/index.md) | contenus et assets | produire, valider et intégrer les médias | les règles métier |
| [Livre IV](../Livre-IV/index.md) | qualité et exploitation | tester, profiler, publier, maintenir | la conception des systèmes |
| [Livre V](index.md) | fiches et index | retrouver rapidement une réponse | les quatre tutoriels complets |
| [Companion Pack](../Companion-Pack/index.md) | artefacts réutilisables | adapter un fichier, modèle ou script matérialisé | la documentation de référence |

**Règle de navigation :** une fiche du Livre V doit conduire vers le chapitre propriétaire, puis vers la section de validation ou de production pertinente.

---

<!-- l5:card -->
## NAV-02 — Parcours débutant

| Étape | Source principale | Section ou complément utile |
|---:|---|---|
| 1 | [règles fondamentales](../Volume-0/CHAPITRE-02-Les-21-regles-fondamentales.md) | [convention des contextes](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md) |
| 2 | [matériel et Windows](../Livre-I/CHAPITRE-01-Materiel-Windows-pilotes-AMD-et-acceleration.md) | [terminaux](../Livre-I/CHAPITRE-02-Terminal-PowerShell-et-outils-Windows.md) |
| 3 | [installer Git](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md#3-installer-git-for-windows) | [installer VS Code](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md#5-installer-visual-studio-code) |
| 4 | [isoler Python](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#1-pourquoi-isoler-python) | [choisir la version](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#3-choisir-une-version-de-python) |
| 5 | [découvrir Godot](../Livre-II/CHAPITRE-01-Decouvrir-Godot-et-creer-le-projet-fil-rouge.md) | [fondamentaux de GDScript](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md) |
| 6 | [scènes, nœuds, Resources et signaux](../Livre-II/CHAPITRE-03-Scenes-noeuds-Resources-et-signaux.md) | [prérequis de l’architecture](../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md#2-prérequis) |

**Sortie attendue :** un poste reproductible, un dépôt versionné et un premier projet Godot compris. Les commandes et exercices restent dans les liens ci-dessus.

---

<!-- l5:card -->
## NAV-03 — Architecture, données et sauvegarde

| Question | Réponse rapide | Tutoriel propriétaire | Vérification associée |
|---|---|---|---|
| Où placer une responsabilité ? | dans un module et une couche explicitement nommés | [périmètre de l’architecture modulaire](../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md#3-périmètre-et-frontières) | [tests unitaires et d’intégration](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md) |
| Comment relier les modules ? | par contrats, services et dépendances orientées | [services, gestionnaires et injection](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md) | [journalisation et diagnostic](../Livre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md) |
| Où placer une donnée de conception ? | dans une Resource ou une configuration versionnée | [Resources, JSON et configurations](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md) | [outils d’édition et pipelines](../Livre-II/CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md) |
| Quand utiliser SQLite ? | pour des données relationnelles et transactionnelles | [SQLite, migrations et persistance](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md) | [reprise après incident](../Livre-IV/CHAPITRE-15-Sauvegardes-migrations-et-reprise-apres-incident.md) |
| Qu’est-ce qu’une sauvegarde ? | un contrat de reconstruction cohérente, pas une copie brute | [rôle de la sauvegarde](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#1-rôle-du-chapitre) | [prérequis et frontières](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#3-périmètre-et-frontières) |

---

<!-- l5:card -->
## NAV-04 — IA locale

| Besoin | Source de plateforme | Source d’intégration | Source de contrôle |
|---|---|---|---|
| exécuter un LLM local | [LLM locaux et interfaces](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md) | [communication Godot avec les services IA](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md) | [séparation production/runtime](../Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md) |
| ajouter une mémoire documentaire | [Python isolé](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#1-pourquoi-isoler-python) | [mémoire vectorielle](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md) | [tests et corpus](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md) |
| exposer une API ou un flux | [Docker et services](../Livre-I/CHAPITRE-05-Docker-et-Docker-Compose.md#1-objet-du-chapitre) | [HTTP, WebSocket et files de tâches](../Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md) | [observabilité locale](../Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md) |
| produire de l’audio IA | [audio IA local](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md) | [voix, bruitages, ambiances et musique](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md) | [référence audio future](index.md#chapitres) |

**Limite :** cette fiche n’indique aucun modèle « meilleur ». Les fiches de moteurs et modèles appartiennent aux chapitres 4 à 7 du Livre V.

---

<!-- l5:card -->
## NAV-05 — Systèmes de jeu

| Domaine | Chapitre propriétaire | Fondations utiles | Qualification |
|---|---|---|---|
| personnages | [Livre II, chapitre 14](../Livre-II/CHAPITRE-14-Personnages.md) | [données](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md), [sauvegarde](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md) | [tests](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md) |
| agents autonomes | [Livre II, chapitre 17](../Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md) | [services](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md), [mémoire](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md) | [profilage CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md) |
| combat | [Livre II, chapitre 18](../Livre-II/CHAPITRE-18-Combat.md) | [entrées et interactions](../Livre-II/CHAPITRE-06-Entrees-controleurs-cameras-et-interactions.md) | [équilibrage](../Livre-IV/CHAPITRE-01-Equilibrage-et-telemetrie-locale.md) |
| inventaire | [Livre II, chapitre 20](../Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md) | [Resources et JSON](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md) | [tests fonctionnels](../Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md) |
| économie | [Livre II, chapitre 21](../Livre-II/CHAPITRE-21-Economie.md) | [inventaire](../Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md) | [équilibrage](../Livre-IV/CHAPITRE-01-Equilibrage-et-telemetrie-locale.md) |
| narration et quêtes | [Livre II, chapitre 25](../Livre-II/CHAPITRE-25-Narration-quetes-codex-et-connaissances.md) | [connaissances](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md) | [localisation](../Livre-IV/CHAPITRE-19-Localisation-et-internationalisation.md) |

Pour une consultation transversale, la future [référence des patrons de gameplay](index.md#chapitres) renverra à ces tutoriels sans réécrire leurs systèmes complets.

---

<!-- l5:card -->
## NAV-06 — Production des assets

| Étape | Source principale | Contrôle ou dépendance |
|---|---|---|
| cadrer le besoin | [préproduction et cahier des charges](../Livre-III/CHAPITRE-01-Preproduction-et-cahier-des-charges-artistique.md) | [direction artistique](../Livre-III/CHAPITRE-02-Direction-artistique-et-bible-visuelle.md) |
| préparer les références | [références, concept art et ComfyUI](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md) | [provenance et licences](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md) |
| produire en 3D | [pipeline Blender](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md) | [UV, retopologie et baking](../Livre-III/CHAPITRE-17-UV-retopologie-et-baking.md) |
| préparer le rendu | [textures et matériaux PBR](../Livre-III/CHAPITRE-16-Textures-materiaux-et-pipeline-PBR.md) | [LOD et optimisation géométrique](../Livre-III/CHAPITRE-18-LOD-imposteurs-et-optimisation-geometrique.md) |
| animer | [rigging et skinning](../Livre-III/CHAPITRE-19-Rigging-et-skinning.md) | [animation procédurale et keyframes](../Livre-III/CHAPITRE-20-Animation-procedurale-et-animation-par-keyframes.md) |
| intégrer | [rôle de l’importation Godot](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#1-rôle-du-chapitre) | [frontières avec les chapitres voisins](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#4-frontières-avec-les-chapitres-voisins) |
| accepter ou refuser | [validation technique et artistique](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md) | [production en lots](../Livre-III/CHAPITRE-30-Automatisation-Blender-ComfyUI-et-production-en-lots.md) |

---

<!-- l5:card -->
## NAV-07 — QA, diagnostic et optimisation

| Signal | Première fiche source | Approfondissement |
|---|---|---|
| « le comportement est faux » | [stratégie QA](../Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md) | [tests fonctionnels et régression](../Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md) |
| « je ne peux pas reproduire » | [rôle du débogage](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#1-rôle-du-chapitre) | [prérequis et frontières](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#4-prérequis-et-frontières) |
| « les journaux ne suffisent pas » | [journalisation et observabilité](../Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md) | [diagnostic reproductible du Livre II](../Livre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md) |
| « le CPU est saturé » | [profilage CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md) | [optimisation des scènes et scripts](../Livre-IV/CHAPITRE-10-Optimisation-des-scenes-scripts-et-systemes-de-jeu.md) |
| « le rendu est trop coûteux » | [profilage GPU](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md) | [LOD du Livre III](../Livre-III/CHAPITRE-18-LOD-imposteurs-et-optimisation-geometrique.md) |
| « la mémoire augmente » | [RAM, VRAM et allocations](../Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md) | [chargements et streaming](../Livre-IV/CHAPITRE-09-Chargements-streaming-et-gestion-des-ressources.md) |

---

<!-- l5:card -->
## NAV-08 — Publication, support et pérennité

| Besoin | Source principale | Source complémentaire |
|---|---|---|
| automatiser les contrôles | [DevOps et intégration continue](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md) | [tests du Livre II](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md) |
| construire les livrables | [exports Godot et packaging](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md) | [publication et distribution](../Livre-IV/CHAPITRE-17-Publication-et-distribution.md) |
| rendre le produit accessible | [accessibilité](../Livre-IV/CHAPITRE-18-Accessibilite.md) | [UX et accessibilité visuelle](../Livre-III/CHAPITRE-25-Experience-utilisateur-et-accessibilite-visuelle.md) |
| traduire | [localisation et internationalisation](../Livre-IV/CHAPITRE-19-Localisation-et-internationalisation.md) | [narration et codex](../Livre-II/CHAPITRE-25-Narration-quetes-codex-et-connaissances.md) |
| corriger après publication | [correctifs et retour arrière](../Livre-IV/CHAPITRE-20-Correctifs-mises-a-jour-et-retour-arriere.md) | [sauvegardes et migrations](../Livre-IV/CHAPITRE-15-Sauvegardes-migrations-et-reprise-apres-incident.md) |
| ouvrir au contenu communautaire | [modding](../Livre-IV/CHAPITRE-21-Modding-et-contenu-communautaire.md) | [outils d’édition internes](../Livre-II/CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md) |
| archiver et transmettre | [maintenance, archivage et pérennité](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md) | [sécurité et sauvegarde du poste](../Livre-I/CHAPITRE-10-Securite-sauvegarde-et-validation-de-la-plateforme.md) |

---

<!-- l5:card -->
## NAV-09 — Parcours Solo et Studio

| Sujet | Solo | Studio | Source commune |
|---|---|---|---|
| architecture | une personne sépare les responsabilités dans le temps | rôles et revues répartissent les responsabilités | [architecture Solo et Studio](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md) |
| versionnement | branche courte et revue personnelle différée | pull request et approbation indépendante | [Git, GitHub et VS Code](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md) |
| production d’assets | checklist locale et lots bornés | portes de validation et responsabilités explicites | [validation des assets](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md) |
| publication | automatisation minimale reproductible | environnements, secrets et approbations séparés | [DevOps et intégration continue](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md) |

**Invariant :** Solo et Studio partagent les mêmes formats, identifiants et règles métier. Seule l’organisation du travail change.

---

<!-- l5:matrix -->
## Matrice par outil

| Outil ou famille | Installer / préparer | Utiliser dans le projet | Qualifier |
|---|---|---|---|
| Git et GitHub | [Livre I — installer Git](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md#3-installer-git-for-windows) | [Livre II — architecture Solo/Studio](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md) | [Livre IV — DevOps](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md) |
| VS Code | [Livre I — installer VS Code](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md#5-installer-visual-studio-code) | [Livre II — automatisation Python](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md) | [Livre IV — débogage](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md) |
| Python | [Livre I — isolement](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#1-pourquoi-isoler-python) | [Livre II — automatisation](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md) | [Livre IV — CI](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md) |
| Docker | [Livre I — objet et rôle](../Livre-I/CHAPITRE-05-Docker-et-Docker-Compose.md#1-objet-du-chapitre) | [Livre II — API et services IA](../Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md) | [Livre IV — serveurs et sécurité réseau](../Livre-IV/CHAPITRE-13-Serveurs-dedies-et-securite-reseau.md) |
| Godot | [Livre II — découvrir Godot](../Livre-II/CHAPITRE-01-Decouvrir-Godot-et-creer-le-projet-fil-rouge.md) | [Livre II — systèmes de jeu](../Livre-II/index.md) | [Livre IV — exports](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md) |
| Blender | [Livre III — pipeline Blender](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md) | [Livre III — familles d’assets](../Livre-III/index.md) | [Livre III — validation](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md) |
| ComfyUI | [Livre I — ComfyUI](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md) | [Livre III — références et concept art](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md) | [Livre III — automatisation en lots](../Livre-III/CHAPITRE-30-Automatisation-Blender-ComfyUI-et-production-en-lots.md) |

---

<!-- l5:matrix -->
## Index des prérequis

| Sujet visé | Obligatoire | Recommandé | Contextuel |
|---|---|---|---|
| architecture modulaire | [scènes, Resources et signaux](../Livre-II/CHAPITRE-03-Scenes-noeuds-Resources-et-signaux.md) | [GDScript](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md) | [Git et VS Code](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md) |
| sauvegarde | [Resources et JSON](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md) | [SQLite](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md) | [reprise après incident](../Livre-IV/CHAPITRE-15-Sauvegardes-migrations-et-reprise-apres-incident.md) |
| IA locale dans Godot | [communication Godot/IA](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md) | [HTTP et WebSocket](../Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md) | [LLM locaux](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md) |
| asset 3D intégré | [pipeline Blender](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md) | [importation Godot](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md) | [optimisation GPU](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md) |
| publication | [exports et packaging](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md) | [DevOps](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md) | [accessibilité](../Livre-IV/CHAPITRE-18-Accessibilite.md), [localisation](../Livre-IV/CHAPITRE-19-Localisation-et-internationalisation.md) |

**Lecture des colonnes :**
- **obligatoire** : connaissance nécessaire pour comprendre ou appliquer la fiche ;
- **recommandé** : réduit les erreurs ou améliore la qualité ;
- **contextuel** : utile seulement selon l’outil, la plateforme ou le livrable.

---

<!-- l5:card -->
## NAV-10 — Statuts de preuve

| Statut | Ce qu’il autorise à dire | Ce qu’il n’autorise pas |
|---|---|---|
| `draft` | la fiche existe mais reste incomplète | qu’elle est fiable ou exhaustive |
| `reviewed` | le contenu a été relu selon le processus | qu’une commande a été exécutée |
| `static-review` | liens, structure et contenu ont été contrôlés statiquement | qu’un outil, asset ou build fonctionne |
| `runtime-tested` | l’exécution décrite a été réalisée dans un contexte conservé | qu’elle fonctionne sur toutes les plateformes |
| `static-review+pdf-inspected` | la publication documentaire a été construite et inspectée | que le produit documenté a été testé |

Pour comprendre la politique de validation, consulter [Production, validation et publication](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md) et [Stratégie générale d’assurance qualité](../Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md).

---

<!-- l5:card -->
## NAV-11 — Contrat d’une fiche du Livre V

Une fiche du Livre V doit rester plus courte que le tutoriel qu’elle référence et comporter, selon son type :

| Élément | Attendu |
|---|---|
| question ou besoin | formulation directement recherchable |
| réponse rapide | décision, valeur, distinction ou procédure minimale |
| source propriétaire | lien vers le Livre I, II, III ou IV |
| prérequis | liens vers les notions nécessaires |
| validation | lien vers la QA, la mesure ou la vérification pertinente |
| limites et alternatives | cas où la réponse change |
| version et preuve | date, version et statut de vérification |

Le [protocole des fiches du Livre V](QA/PROTOCOLE-FICHES-LIVRE-V.md) remplace les obligations tutoriel incompatibles avec ce format.

---

<!-- l5:card -->
## NAV-12 — Contrôle express de navigation

Avant d’ajouter ou de modifier une fiche :

- vérifier que chaque lien pointe vers le chapitre ou la sous-section propriétaire ;
- préférer un lien précis avec fragment lorsqu’un titre stable existe ;
- ajouter au minimum un lien de prérequis et un lien de validation ;
- ne recopier ni installation complète, ni système de jeu complet, ni pipeline artistique complet ;
- distinguer une information de référence d’un artefact réellement disponible dans le [Companion Pack](../Companion-Pack/index.md) ;
- conserver les réserves de licence, de runtime et de compatibilité lorsqu’elles ne sont pas levées.

## Références de gouvernance

- [Plan maître du Livre V](../plans/LIVRE-V-PLAN-MAITRE.md)
- [Protocole des fiches du Livre V](QA/PROTOCOLE-FICHES-LIVRE-V.md)
- [Ordre de compilation](../contents.txt)
- [Feuille de route](../ROADMAP.md)
- [Continuité du projet](../CONTINUITE-PROJET.md)
