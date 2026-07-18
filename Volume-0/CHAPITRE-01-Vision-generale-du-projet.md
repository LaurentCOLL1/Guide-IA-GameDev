---
title: "Volume 0 — Chapitre 1 : Vision générale du projet"
identifier: "DOC-V0-CH01"
version: "1.2.0"
status: "draft-review"
lang: "fr-FR"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Vision générale du projet

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-V0-CH01`  
> **Priorité :** 🟢 Obligatoire  
> **Parcours :** 👤 Mode Solo · 👥 Mode Studio  
> **Public :** débutant à avancé  
> **Résultat attendu :** comprendre la mission, le périmètre et les principes directeurs de la collection.

## 1. Rôle de ce chapitre

Ce chapitre constitue la déclaration d'intention officielle du projet **Guide IA GameDev**. Il explique ce que la collection cherche à accomplir, à qui elle s'adresse, quelles contraintes elle accepte et quelles limites elle reconnaît.

Les choix détaillés d'installation, d'architecture, de modèles d'intelligence artificielle ou de production d'assets seront traités dans les volumes spécialisés. Ici, l'objectif est de fournir une vision commune afin que toutes les décisions ultérieures restent cohérentes.

## 2. Nom et identité du projet

### 2.1 Nom du dépôt

> **[SORTIE] Résultat attendu - Ne pas saisir :** comparer avec la sortie obtenue.

```text
Guide-IA-GameDev
```

### 2.2 Titre éditorial de travail

> **Guide réaliste de création de jeux vidéo 3D avec IA locale**

### 2.3 Sous-titre

> **Godot, Blender, ComfyUI, Open WebUI et outils open source locaux**

Le titre pourra évoluer avant la publication de la version `1.0`. L'identifiant du dépôt et les identifiants techniques resteront stables afin de ne pas casser les références croisées.

## 3. Mission

La mission du projet est de permettre à une personne disposant de peu ou pas d'expérience en informatique, en programmation ou en développement de jeux de construire progressivement un jeu vidéo 3D réaliste en s'appuyant sur des logiciels gratuits, des composants open source et des intelligences artificielles exécutées localement.

Le guide doit accompagner le lecteur sur l'ensemble du cycle de vie :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Comprendre
    ↓
Installer
    ↓
Configurer
    ↓
Concevoir
    ↓
Programmer
    ↓
Produire les contenus
    ↓
Tester et optimiser
    ↓
Publier
    ↓
Maintenir
```

Cette ambition implique de traiter à la fois :

- l'administration de l'environnement local ;
- les modèles de langage ;
- la génération d'images ;
- la création et l'animation 3D ;
- le son, la musique et les voix ;
- la programmation Godot ;
- les systèmes de gameplay ;
- la gestion des données ;
- les tests, l'optimisation et la publication ;
- l'organisation documentaire et la maintenance à long terme.

## 4. Résultat final visé

À la fin de la collection, le lecteur doit disposer de deux résultats complémentaires.

### 4.1 Un projet de jeu fonctionnel

Le projet fil rouge doit démontrer une architecture réaliste comprenant notamment :

- un monde 3D explorable ;
- des personnages et agents autonomes ;
- des dialogues et une narration ;
- des systèmes de progression ;
- un inventaire, une économie et des quêtes ;
- des sauvegardes locales ;
- des contenus graphiques et audio intégrés ;
- des procédures de test, d'optimisation et d'export.

Le projet fil rouge sert de support d'apprentissage. Il ne constitue pas une promesse de produire automatiquement un jeu commercial de grande ampleur ni un substitut au travail de conception, de programmation et de direction artistique.

### 4.2 Un environnement de production réutilisable

Le lecteur doit aussi obtenir une plateforme locale capable de l'assister dans d'autres projets :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Docker
├── Open WebUI
├── Open Terminal
├── Vane
├── Ollama
├── llama.cpp
├── LocalAI
├── services documentaires
└── services de données

Poste de création
├── ComfyUI
├── Blender
├── Godot
├── outils audio
├── Git
└── scripts d'automatisation
```

Cette plateforme doit rester modulaire : un outil peut être remplacé ou retiré sans imposer la reconstruction totale du projet.

## 5. Public visé

### 5.1 Débutants complets

Le guide ne suppose pas que le lecteur connaît déjà :

- le terminal ;
- Git ;
- Docker ;
- Python ;
- la programmation orientée objet ;
- la modélisation 3D ;
- les bases de données ;
- le fonctionnement d'un moteur de jeu.

Chaque notion indispensable doit être expliquée avant son utilisation, accompagnée d'un exemple simple puis d'une mise en pratique.

### 5.2 Créateurs indépendants

Le parcours **Mode Solo** privilégie :

- les outils simples à maintenir ;
- l'automatisation des tâches répétitives ;
- les compromis réalistes ;
- la réduction du nombre de services simultanés ;
- les méthodes de sauvegarde et de reprise adaptées à une seule personne.

### 5.3 Équipes et petits studios

Le parcours **Mode Studio** ajoute :

- les rôles et responsabilités ;
- les branches Git et les pull requests ;
- la validation des contenus ;
- la documentation partagée ;
- les tests automatisés ;
- les serveurs dédiés et les workflows collaboratifs.

### 5.4 Lecteurs expérimentés

Les développeurs avancés peuvent utiliser la collection comme :

- référence d'architecture ;
- bibliothèque de scripts et de schémas ;
- catalogue de workflows ;
- matrice de compatibilité ;
- base de comparaison entre solutions locales.

## 6. Configuration matérielle de référence

La collection est optimisée et illustrée en priorité avec la configuration suivante :

| Composant | Référence |
|---|---|
| Carte graphique | AMD Radeon RX 6750 XT |
| Mémoire vidéo | 12 Go |
| Processeur | AMD Ryzen 7 2700, 8 cœurs |
| Mémoire vive | 32 Go |
| Système principal | Windows |
| Conteneurisation | Docker Desktop |
| Interface d'image principale | ComfyUI |
| Accélération ComfyUI historique | ZLUDA, lorsque compatible et maintenu |

Cette configuration n'est ni une configuration minimale universelle ni une garantie de performances. Elle sert de profil de référence pour :

- les exemples de consommation de VRAM ;
- le choix des quantifications de modèles ;
- les stratégies de déchargement CPU/GPU ;
- les tailles de textures ;
- les compromis de rendu ;
- les benchmarks reproductibles.

Les informations susceptibles d'évoluer, en particulier les pilotes AMD, ZLUDA, ROCm, DirectML, Vulkan et les backends d'inférence, devront être vérifiées et datées dans les chapitres concernés.

## 7. Principes technologiques

### 7.1 Local par défaut

Les données de conception, le code, les documents, les conversations de travail et les assets doivent pouvoir rester sur la machine de l'utilisateur.

Le fonctionnement hors ligne est recherché lorsque la technologie le permet. Une connexion peut rester nécessaire pour télécharger les logiciels, les modèles, les mises à jour ou certaines documentations.

### 7.2 Gratuit et open source dans le pipeline principal

Le pipeline principal privilégie les composants :

- gratuits ;
- exécutables localement ;
- open source lorsque possible ;
- sans abonnement obligatoire.

Lorsqu'un outil gratuit n'est pas open source, sa nature doit être indiquée clairement. Les comparatifs peuvent mentionner des solutions propriétaires, mais elles ne doivent pas devenir une dépendance obligatoire du parcours principal.

### 7.3 Une source de vérité documentaire

Le Markdown constitue la source officielle de la collection. Les PDF, pages HTML, fichiers DOCX ou EPUB sont des formats générés.

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Markdown versionné
        ↓
Validation
        ↓
Pandoc / générateur de site
        ↓
PDF · HTML · autres formats
```

Aucune correction ne doit être appliquée uniquement au PDF généré.

### 7.4 Architecture modulaire

Chaque composant doit posséder une responsabilité claire.

| Composant | Responsabilité principale |
|---|---|
| Godot | moteur de jeu et runtime |
| GDScript | logique de gameplay principale |
| Blender | production, rigging et optimisation 3D |
| ComfyUI | génération et traitement graphique par nœuds |
| Open WebUI | interface et orchestration des assistants locaux |
| Ollama / llama.cpp / LocalAI | exécution ou exposition des modèles locaux |
| SQLite | données structurées persistantes |
| Base vectorielle | recherche sémantique et mémoire documentaire |
| Outils audio locaux | voix, musique, ambiances et effets |
| Git | historique et collaboration |
| Docker | isolation et orchestration des services compatibles |

La présence d'un outil dans cette liste ne signifie pas qu'il doit toujours être actif pendant le jeu. Le guide distinguera les outils de **production** des composants éventuellement utilisés au **runtime**.

## 8. Organisation de la collection

### 8.1 Volume 0 — Fondation documentaire

Il définit :

- les règles du guide ;
- les conventions de rédaction ;
- les identifiants ;
- les standards de code et de données ;
- la politique de compatibilité ;
- le contrôle qualité documentaire.

### 8.2 Livre I — Préparer la plateforme

Il couvre :

- le matériel et le système ;
- les pilotes et backends AMD ;
- Docker ;
- Open WebUI, Open Terminal et Vane ;
- ComfyUI ;
- les LLM locaux ;
- les outils audio locaux.

### 8.3 Livre II — Développement du jeu et plateforme IA

Il rassemble :

- Godot et GDScript ;
- l'architecture logicielle ;
- les douze grands systèmes de gameplay ;
- les communications entre services ;
- l'industrialisation du projet.

### 8.4 Livre III — Production des contenus et des assets

Il traite :

- la préproduction ;
- les humains, humanoïdes, animaux et créatures ;
- les environnements, objets et matériaux ;
- le rigging, l'animation, les cinématiques et l'audio ;
- les effets visuels ;
- l'interface et l'expérience utilisateur ;
- l'intégration et la validation des assets.

### 8.5 Livre IV — Finalisation, publication et maintenance

Il couvre :

- l'équilibrage ;
- l'assurance qualité ;
- le diagnostic et l'observabilité locale ;
- l'optimisation ;
- le multijoueur ;
- le DevOps ;
- l'export, la publication et la maintenance.

### 8.6 Livre V — Encyclopédie technique

Il sert de référence non linéaire et centralise :

- les arbres de décision ;
- les fiches d'outils ;
- les workflows ;
- les prompts ;
- le code ;
- les formats de données ;
- les architectures ;
- les checklists et matrices.

### 8.7 Companion Pack

Il fournit les artefacts directement utilisables :

- templates ;
- scripts ;
- schémas SQL ;
- exemples JSON ;
- fichiers Docker Compose ;
- workflows ComfyUI ;
- modèles documentaires ;
- projets de démonstration.

## 9. Les douze grands systèmes de gameplay

Le Livre II organise le gameplay autour de douze domaines afin d'éviter une accumulation de fonctionnalités sans architecture commune :

1. personnages ;
2. relations sociales ;
3. famille ;
4. agents IA ;
5. combat ;
6. compétences et pouvoirs ;
7. inventaire et réputation des objets ;
8. économie ;
9. monde vivant et simulation écologique ;
10. politique, factions et justice ;
11. construction et gestion de domaines ;
12. narration, quêtes, codex et connaissances.

Les sous-systèmes spécialisés sont rattachés à l'un de ces domaines. Ils ne doivent pas créer de copie parallèle des mêmes données ou règles.

## 10. Projet fil rouge

Un projet unique accompagne la collection. Chaque chapitre doit soit :

- ajouter un élément au projet ;
- expliquer une notion nécessaire à une étape ultérieure ;
- fournir une référence réutilisable.

Le projet fil rouge évite une succession de tutoriels indépendants. Il doit rester suffisamment générique pour être adapté à plusieurs genres : RPG, simulation de vie, survival, sandbox ou aventure narrative.

## 11. Contenu destiné à un public adulte

La collection prévoit des sections consacrées à la conception de jeux destinés à un public adulte, y compris la nudité et des relations sexuelles entre personnages adultes.

Ces sections doivent respecter les règles suivantes :

- tous les personnages impliqués sont explicitement adultes ;
- les systèmes de consentement, de limites et de conséquences sont traités comme des éléments de conception essentiels ;
- aucun contenu sexuel impliquant des mineurs ou des personnes présentées comme mineures ;
- aucune sexualisation d'animaux réels ;
- les questions juridiques, de plateforme de distribution, de classification et de licence sont signalées ;
- les aspects techniques sont séparés des contenus graphiques afin de maintenir la réutilisabilité des systèmes.

Les systèmes génériques — animation, états, relations, dialogue, caméra, shaders, particules, sauvegarde et interface — doivent rester utilisables dans des projets non adultes.

## 12. Ce que le guide promet

Le guide promet de fournir :

- une progression structurée ;
- des procédures détaillées ;
- des exemples simples et avancés ;
- des fichiers réutilisables ;
- une distinction claire entre obligatoire, recommandé et optionnel ;
- des informations de compatibilité et de licence ;
- des erreurs fréquentes et méthodes de diagnostic ;
- des optimisations adaptées à la configuration de référence ;
- des références croisées stables.

## 13. Ce que le guide ne promet pas

Le guide ne garantit pas :

- qu'un débutant terminera seul un jeu de taille AAA ;
- que toutes les combinaisons de versions resteront compatibles ;
- que tous les modèles téléchargés autorisent l'utilisation commerciale ;
- que les sorties générées par IA seront exactes ou juridiquement exploitables sans validation humaine ;
- qu'un outil expérimental, un fork ou une méthode de compatibilité restera maintenu ;
- que les performances mesurées sur la configuration de référence seront identiques sur une autre machine.

L'utilisateur reste responsable de la validation de son code, de ses licences, de ses données, de ses contenus et de la conformité légale de son produit.

## 14. Critères de qualité

Un chapitre n'est considéré comme terminé que s'il satisfait, lorsque pertinent, les critères suivants :

- exactitude technique ;
- reproductibilité ;
- clarté pour un débutant ;
- cohérence avec les autres volumes ;
- séparation entre faits, recommandations et hypothèses ;
- identification des versions et dépendances ;
- exemples vérifiables ;
- prise en compte des erreurs fréquentes ;
- validation des licences ;
- références croisées mises à jour.

## 15. Parcours Mode Solo et Mode Studio

### 15.1 Mode Solo

Les encadrés Solo indiquent :

- ce qui peut être simplifié ;
- ce qui peut être automatisé ;
- ce qui peut attendre une version ultérieure ;
- quels services ne doivent pas fonctionner simultanément sur la configuration de référence.

### 15.2 Mode Studio

Les encadrés Studio précisent :

- les responsabilités par rôle ;
- les validations et revues ;
- les conventions de branches ;
- la gestion des accès ;
- les tests et intégrations continues ;
- la communication entre équipes techniques et artistiques.

Les deux parcours partagent le même socle technique. Le Mode Studio ne doit pas rendre le Mode Solo incomplet.

## 16. Évolution et versionnement

La collection est conçue comme un manuel vivant. Chaque changement important doit être :

- versionné dans Git ;
- mentionné dans `CHANGELOG.md` ;
- relié à une version ou une date de vérification lorsque l'information est évolutive ;
- accompagné d'une migration si le changement casse un exemple ou une ressource du Companion Pack.

Les identifiants tels que `DOC-V0-CH01`, `GDS-001` ou `WF-CFY-001` restent stables même si la pagination ou l'ordre de certaines sections évolue.

## 17. Checklist de validation du chapitre

- [x] La mission du projet est définie.
- [x] Le public visé est identifié.
- [x] La configuration matérielle de référence est documentée.
- [x] Le principe local, gratuit et open source est expliqué.
- [x] Les cinq livres et le Companion Pack sont situés.
- [x] Les parcours Solo et Studio sont décrits.
- [x] Le projet fil rouge est défini.
- [x] Le traitement des contenus adultes possède des limites explicites.
- [x] Les promesses et limites du guide sont distinguées.
- [x] Les critères de qualité sont établis.

## 18. Références croisées

- `DOC-V0-CH02` — Les 21 règles fondamentales.
- `DOC-V0-CH03` — Architecture documentaire.
- `DOC-V0-CH04` — Convention des identifiants.
- `STYLE_GUIDE.md` — Style éditorial et conventions Markdown.
- `ROADMAP.md` — Jalons de production.
- `BUILD.md` — Génération des formats de publication.

## 19. Historique

| Version | Date | Modification |
|---|---|---|
| 1.0.0 | 2026-07-18 | Première rédaction complète du chapitre. |
