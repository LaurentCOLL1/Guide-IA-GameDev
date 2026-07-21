---
title: "Livre II — Développement du jeu et plateforme IA"
id: "LIV-II-INDEX"
status: "in-progress"
version: "1.19.0"
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

1. [Découvrir Godot et créer le projet fil rouge](CHAPITRE-01-Decouvrir-Godot-et-creer-le-projet-fil-rouge.md) — **rédigé, repéré et audité**
2. [Fondamentaux de GDScript](CHAPITRE-02-Fondamentaux-de-GDScript.md) — **rédigé, repéré, enrichi et audité**
3. [Scènes, nœuds, Resources et signaux](CHAPITRE-03-Scenes-noeuds-Resources-et-signaux.md) — **rédigé, repéré et audité au niveau static-review**
4. [Architecture modulaire du projet](CHAPITRE-04-Architecture-modulaire-du-projet.md) — **rédigé, repéré et audité au niveau static-review**
5. [Services, gestionnaires, bus d’événements et injection de dépendances](CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md) — **rédigé, repéré et audité au niveau static-review**
6. [Entrées, contrôleurs, caméras et interactions](CHAPITRE-06-Entrees-controleurs-cameras-et-interactions.md) — **rédigé, repéré et audité au niveau static-review**
7. [Données avec Resources, JSON et configurations](CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md) — **rédigé, repéré et audité au niveau static-review**
8. [SQLite, migrations et données persistantes](CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md) — **rédigé, repéré et audité au niveau static-review**
9. [Sauvegardes, chargements et compatibilité des versions](CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md) — **rédigé, repéré et audité au niveau static-review**
10. [Mémoire vectorielle, connaissances et recherche sémantique](CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md) — **rédigé, repéré et audité au niveau static-review**
11. [Communication Godot avec les services IA locaux](CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md) — **rédigé, repéré et audité au niveau static-review**
12. [HTTP, WebSocket, API compatibles OpenAI et files de tâches](CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md) — **rédigé, repéré et audité au niveau static-review**
13. [Sécurité et séparation entre production et runtime de l’IA](CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md) — **rédigé, repéré et audité au niveau static-review**

## Partie II — Les douze grands systèmes de gameplay

14. [Personnages](CHAPITRE-14-Personnages.md) — **rédigé, repéré et audité au niveau static-review**
15. [Relations sociales](CHAPITRE-15-Relations-sociales.md) — **rédigé, repéré, expliqué bloc par bloc sans répétitions éditoriales, avec renvois internes précis, et audité au niveau static-review**
16. [Famille et générations](CHAPITRE-16-Famille-et-generations.md) — **rédigé, repéré, expliqué bloc par bloc sans répétitions éditoriales, avec renvois internes précis, et audité au niveau static-review**
17. [Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md) — **rédigé, repéré, expliqué bloc par bloc, terminologie des retours clarifiée, métadonnées d’audit horodatées, clôturé par les décisions Project Asteria et audité au niveau static-review**
18. [Combat](CHAPITRE-18-Combat.md) — **rédigé, repéré, expliqué bloc par bloc, clôturé par les décisions Project Asteria et audité au niveau static-review**
19. [Compétences et pouvoirs](CHAPITRE-19-Competences-et-pouvoirs.md) — **rédigé, repéré, expliqué bloc par bloc, commit multi-autorités préparé, clôturé par les décisions Project Asteria et audité au niveau static-review**
20. [Inventaire et réputation des objets](CHAPITRE-20-Inventaire-et-reputation-des-objets.md) — **rédigé, repéré, expliqué bloc par bloc, transferts multi-agrégats préparés, clôturé par les décisions Project Asteria et audité au niveau static-review**
21. [Économie](CHAPITRE-21-Economie.md) — **rédigé, repéré, expliqué bloc par bloc, écritures équilibrées et commit économie-inventaire préparé, clôturé par les décisions Project Asteria et audité au niveau static-review**
22. [Monde vivant et simulation écologique](CHAPITRE-22-Monde-vivant-et-simulation-ecologique.md) — **rédigé, repéré, expliqué bloc par bloc, simulation régionale bornée et commandes écologie-inventaire préparées, clôturé par les décisions Project Asteria et audité au niveau static-review**
23. [Politique, factions et justice](CHAPITRE-23-Politique-factions-et-justice.md) — **rédigé, repéré, expliqué bloc par bloc, lois versionnées et sanctions multi-autorités préparées, clôturé par les décisions Project Asteria et audité au niveau static-review**
24. [Construction et gestion de domaines](CHAPITRE-24-Construction-et-gestion-de-domaines.md) — **rédigé, repéré, expliqué bloc par bloc, chantiers et production multi-autorités préparés, clôturé par les décisions Project Asteria et audité au niveau static-review**
25. [Narration, quêtes, codex et connaissances](CHAPITRE-25-Narration-quetes-codex-et-connaissances.md) — **rédigé, repéré, expliqué bloc par bloc, orchestration événementielle et conséquences multi-autorités préparées, clôturé par les décisions Project Asteria et audité au niveau static-review**

## Partie III — Industrialisation du projet

26. [Outils d’édition internes et pipelines de contenu](CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md) — **rédigé, repéré, expliqué bloc par bloc, pipelines déterministes et transactions staged documentés, audité au niveau static-review**
27. [Tests unitaires, tests d’intégration et simulations](CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md) — **rédigé, repéré, expliqué bloc par bloc, suites, doubles et simulations déterministes documentés, audité au niveau static-review**
28. Journalisation, diagnostic et reproductibilité — à rédiger
29. Automatisation Python et génération de données — à rédiger
30. Architecture Solo et architecture Studio — à rédiger

## Audit post-création

Chaque chapitre du Livre II fait l’objet d’un audit distinct après rédaction :

- [protocole obligatoire](QA/PROTOCOLE-AUDIT-POST-CREATION.md) ;
- [audit des chapitres 1 et 2](QA/AUDIT-CHAPITRES-01-02.md) ;
- [audit du chapitre 3](QA/AUDIT-CHAPITRE-03.md) ;
- [audit du chapitre 4](QA/AUDIT-CHAPITRE-04.md) ;
- [audit du chapitre 5](QA/AUDIT-CHAPITRE-05.md) ;
- [audit du chapitre 6](QA/AUDIT-CHAPITRE-06.md) ;
- [audit du chapitre 7](QA/AUDIT-CHAPITRE-07.md) ;
- [audit du chapitre 8](QA/AUDIT-CHAPITRE-08.md) ;
- [audit du chapitre 9](QA/AUDIT-CHAPITRE-09.md) ;
- [audit du chapitre 10](QA/AUDIT-CHAPITRE-10.md) ;
- [audit du chapitre 11](QA/AUDIT-CHAPITRE-11.md) ;
- [audit du chapitre 12](QA/AUDIT-CHAPITRE-12.md) ;
- [audit du chapitre 13](QA/AUDIT-CHAPITRE-13.md) ;
- [audit du chapitre 14](QA/AUDIT-CHAPITRE-14.md) ;
- [audit du chapitre 15](QA/AUDIT-CHAPITRE-15.md) ;
- [audit du chapitre 16](QA/AUDIT-CHAPITRE-16.md) ;
- [audit du chapitre 17](QA/AUDIT-CHAPITRE-17.md) ;
- [audit du chapitre 18](QA/AUDIT-CHAPITRE-18.md) ;
- [audit du chapitre 19](QA/AUDIT-CHAPITRE-19.md) ;
- [audit du chapitre 20](QA/AUDIT-CHAPITRE-20.md) ;
- [audit du chapitre 21](QA/AUDIT-CHAPITRE-21.md) ;
- [audit du chapitre 22](QA/AUDIT-CHAPITRE-22.md) ;
- [audit du chapitre 23](QA/AUDIT-CHAPITRE-23.md) ;
- [audit du chapitre 24](QA/AUDIT-CHAPITRE-24.md) ;
- [audit du chapitre 25](QA/AUDIT-CHAPITRE-25.md) ;
- [audit du chapitre 26](QA/AUDIT-CHAPITRE-26.md) ;
- [audit du chapitre 27](QA/AUDIT-CHAPITRE-27.md) ;
- [audit de restructuration des explications, chapitres 17 à 26](QA/AUDIT-RESTRUCTURATION-EXPLICATIONS-CH17-CH26.md) ;
- [audit rétroactif des exemples d’erreurs, chapitres 1 à 6](QA/AUDIT-RETROACTIF-EXEMPLES-ERREURS-CH01-CH06.md).

La mention **rédigé, repéré et audité** signifie que :

- la complétude et les exemples ont été relus statiquement ;
- chaque commande, fichier, action graphique, sortie ou exemple possède un contexte explicite ;
- le contrôle des doublons a été effectué ;
- les limites runtime restent déclarées ;
- le PDF de fin de Livre reste différé.

Elle ne remplace pas un test runtime sur le projet matérialisé.

## Politique PDF

Le PDF complet n’est plus construit après chaque chapitre. Il sera généré et inspecté :

1. à la fin du Livre II ;
2. à la fin de chaque Livre suivant ;
3. à la fin de la collection complète.

Une compilation intermédiaire est réservée aux modifications directes de la chaîne de publication ou de la mise en page.

## Niveau de raisonnement avant chaque chapitre

Avant la rédaction d’un nouveau chapitre, la conversation doit annoncer le niveau conseillé de GPT-5.6 Sol :

- **Moyenne** pour un chapitre principalement descriptif ou linéaire ;
- **Élevée** pour architecture, code imbriqué, données, IA, sécurité, optimisation ou dépendances nombreuses.

Les chapitres 3 à 27 ont utilisé **Élevée**. La recommandation doit être justifiée avant le début du travail et reste une donnée de gouvernance du processus, jamais une métadonnée du chapitre publié.

## Principes du Livre II

Les chapitres 17 à 27 utilisent désormais des explications structurées : les formulations pédagogiques antérieures sont conservées et reclassées, puis complétées seulement lorsque le bloc l’exige. Les parcours Solo et Studio restent en Markdown ordinaire lorsqu’ils ne constituent pas un format littéral.

- Le projet doit rester exécutable après chaque chapitre.
- Les scènes et scripts sont organisés par fonctionnalité.
- Les données de gameplay ne sont pas codées en dur lorsqu’une Resource ou une table convient mieux.
- Les systèmes communiquent par interfaces, signaux ou événements plutôt que par dépendances globales implicites.
- Les services IA sont facultatifs au runtime sauf décision explicite et documentée.
- Un chemin déterministe local reste disponible pour les fonctions essentielles du jeu.
- Les douze grands systèmes possèdent des frontières, des données et des tests distincts.
- Les sauvegardes utilisent des versions et des migrations.
- Le Mode Solo privilégie la simplicité opérationnelle.
- Le Mode Studio ajoute responsabilités, revues, automatisation et validation collective.

## Version de référence

Au 19 juillet 2026 :

- Godot `4.7.1-stable` constitue la version de référence ;
- l’édition Standard et GDScript constituent le parcours principal ;
- Forward+ constitue le renderer principal ;
- Mobile sert de profil secondaire ;
- Compatibility sert de profil ancien ou Web ;
- la configuration de référence reste la RX 6750 XT 12 Go, le Ryzen 7 2700 et 32 Go de RAM sous Windows 11.

## Statut

Le milestone **M3 — Livre II : Développement et architecture** est en cours. **Vingt-sept chapitres sur trente** sont rédigés, repérés et audités au niveau documentaire et statique. Les neuf chapitres de fondation, les quatre chapitres de plateforme IA locale et les douze systèmes de gameplay sont complets. La partie industrialisation compte **deux chapitres sur cinq** : outils d’édition et pipelines de contenu, puis tests unitaires, intégration et simulations déterministes. Les réserves runtime et le PDF restent différés conformément au protocole QA.
