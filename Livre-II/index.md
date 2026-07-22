---
title: "Livre II — Développement du jeu et plateforme IA"
id: "LIV-II-INDEX"
status: "complete"
version: "1.25.0"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Livre II — Développement du jeu et plateforme IA

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

Ce livre construit progressivement le projet fil rouge sous Godot. Il couvre les bases du moteur et de GDScript, l’architecture logicielle, les douze grands systèmes de gameplay, les données persistantes, la communication avec les services IA locaux et l’industrialisation du projet.

## Objectif

À la fin du Livre II, le lecteur doit disposer d’un projet Godot 3D modulaire, sauvegardable, testable et capable d’intégrer des services IA locaux sans rendre le runtime du jeu dépendant d’un service externe permanent.

Le projet fil rouge porte le nom technique provisoire :

> **[LECTURE] Nom de référence — Ne pas saisir.**

```text
Project Asteria
```

## Partie I — Fondations Godot, architecture et données

1. [Découvrir Godot et créer le projet fil rouge](CHAPITRE-01-Decouvrir-Godot-et-creer-le-projet-fil-rouge.md)
2. [Fondamentaux de GDScript](CHAPITRE-02-Fondamentaux-de-GDScript.md)
3. [Scènes, nœuds, Resources et signaux](CHAPITRE-03-Scenes-noeuds-Resources-et-signaux.md)
4. [Architecture modulaire du projet](CHAPITRE-04-Architecture-modulaire-du-projet.md)
5. [Services, gestionnaires, bus d’événements et injection de dépendances](CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md)
6. [Entrées, contrôleurs, caméras et interactions](CHAPITRE-06-Entrees-controleurs-cameras-et-interactions.md)
7. [Données avec Resources, JSON et configurations](CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md)
8. [SQLite, migrations et données persistantes](CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md)
9. [Sauvegardes, chargements et compatibilité des versions](CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md)
10. [Mémoire vectorielle, connaissances et recherche sémantique](CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md)
11. [Communication Godot avec les services IA locaux](CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md)
12. [HTTP, WebSocket, API compatibles OpenAI et files de tâches](CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md)
13. [Sécurité et séparation entre production et runtime de l’IA](CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md)

## Partie II — Les douze grands systèmes de gameplay

14. [Personnages](CHAPITRE-14-Personnages.md)
15. [Relations sociales](CHAPITRE-15-Relations-sociales.md)
16. [Famille et générations](CHAPITRE-16-Famille-et-generations.md)
17. [Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md)
18. [Combat](CHAPITRE-18-Combat.md)
19. [Compétences et pouvoirs](CHAPITRE-19-Competences-et-pouvoirs.md)
20. [Inventaire et réputation des objets](CHAPITRE-20-Inventaire-et-reputation-des-objets.md)
21. [Économie](CHAPITRE-21-Economie.md)
22. [Monde vivant et simulation écologique](CHAPITRE-22-Monde-vivant-et-simulation-ecologique.md)
23. [Politique, factions et justice](CHAPITRE-23-Politique-factions-et-justice.md)
24. [Construction et gestion de domaines](CHAPITRE-24-Construction-et-gestion-de-domaines.md)
25. [Narration, quêtes, codex et connaissances](CHAPITRE-25-Narration-quetes-codex-et-connaissances.md)

## Partie III — Industrialisation du projet

26. [Outils d’édition internes et pipelines de contenu](CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md)
27. [Tests unitaires, tests d’intégration et simulations](CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md)
28. [Journalisation, diagnostic et reproductibilité](CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md)
29. [Automatisation Python et génération de données](CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md)
30. [Architecture Solo et architecture Studio](CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md)

## Principes du Livre II

- Le projet doit rester exécutable après chaque étape importante.
- Les scènes et scripts sont organisés par fonctionnalité.
- Les données de gameplay ne sont pas codées en dur lorsqu’une Resource ou une table convient mieux.
- Les systèmes communiquent par interfaces, signaux ou événements plutôt que par dépendances globales implicites.
- Les services IA sont facultatifs au runtime sauf décision explicite et documentée.
- Un chemin déterministe local reste disponible pour les fonctions essentielles du jeu.
- Les douze grands systèmes possèdent des frontières, des données et des tests distincts.
- Les sauvegardes utilisent des versions et des migrations.
- Le Mode Solo privilégie la simplicité opérationnelle.
- Le Mode Studio ajoute responsabilités, revues, automatisation et validation collective.

## Configuration de référence

- Godot `4.7.1-stable`, édition Standard et GDScript ;
- renderer Forward+ principal, Mobile secondaire et Compatibility pour les anciens matériels ou le Web ;
- AMD Radeon RX 6750 XT 12 Go, Ryzen 7 2700, 32 Go de RAM et Windows 11.
