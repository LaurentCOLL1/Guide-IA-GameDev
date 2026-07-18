---
title: "Volume 0 — Chapitre 3 : Architecture documentaire"
id: "DOC-V0-CH03"
status: "draft"
version: "0.5.0"
lang: "fr-FR"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Volume 0 — Chapitre 3 : Architecture documentaire

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## 1. Objectif du chapitre

Ce chapitre définit l’architecture officielle du dépôt `Guide-IA-GameDev`. Il fixe la place de chaque type de contenu, la relation entre les cinq livres, le Volume 0 et le Companion Pack, ainsi que les règles permettant de maintenir l’ensemble sur plusieurs années sans créer de doublons ni de dépendances documentaires difficiles à gérer.

Cette architecture est normative. Toute nouvelle ressource doit être rangée dans le dossier approprié, recevoir un identifiant stable et être référencée depuis les index correspondants.

## 2. Principes d’architecture

L’organisation du projet repose sur sept principes.

1. **Une seule source de vérité** : les fichiers Markdown du dépôt constituent la source éditoriale principale.
2. **Séparation des responsabilités** : chaque livre traite une phase précise du cycle de développement.
3. **Références croisées plutôt que duplication** : une notion est expliquée une fois, puis citée ailleurs.
4. **Identifiants stables** : les liens logiques ne dépendent pas uniquement des numéros de page.
5. **Compilation reproductible** : l’ordre des fichiers est défini explicitement dans `contents.txt`.
6. **Ressources séparées du texte pédagogique** : les scripts, modèles et workflows résident dans le Companion Pack.
7. **Évolution incrémentale** : les ajouts doivent préserver la compatibilité avec la structure existante.

## 3. Vue d’ensemble du dépôt

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Guide-IA-GameDev/
├── README.md
├── CHANGELOG.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── STYLE_GUIDE.md
├── BUILD.md
├── metadata.yaml
├── contents.txt
├── build.ps1
├── build.sh
├── Volume-0/
├── Livre-I/
├── Livre-II/
├── Livre-III/
├── Livre-IV/
├── Livre-V/
├── Companion-Pack/
├── assets/
├── templates/
├── scripts/
├── docker/
├── workflows/
├── database/
├── diagrams/
├── tests/
└── dist/
```

Les dossiers techniques supplémentaires peuvent être créés progressivement. Ils doivent toutefois respecter les responsabilités décrites dans ce chapitre.

## 4. Documents racine

### 4.1 `README.md`

Le fichier `README.md` est la porte d’entrée du dépôt. Il présente le projet, son public, sa structure, ses prérequis et son état d’avancement.

Il ne remplace pas le Volume 0. Il doit rester synthétique et renvoyer vers les documents normatifs.

### 4.2 `CHANGELOG.md`

Le changelog suit l’évolution des versions publiées. Il ne sert pas de journal quotidien. Les changements significatifs y sont regroupés par version.

### 4.3 `ROADMAP.md`

La roadmap indique l’état des jalons M0 à M9. Elle suit la progression éditoriale globale et ne doit pas contenir le détail de chaque tâche technique.

### 4.4 `CONTRIBUTING.md`

Ce document décrit la manière de proposer une modification, de nommer une branche, de préparer un commit et de soumettre une relecture.

### 4.5 `STYLE_GUIDE.md`

Le guide de style fixe les conventions rédactionnelles, typographiques et structurelles applicables à tous les fichiers Markdown.

### 4.6 `BUILD.md`

Ce document explique comment produire les formats PDF et HTML à partir du dépôt.

### 4.7 `metadata.yaml`

Ce fichier centralise les métadonnées Pandoc communes : titre, langue, auteur, paramètres de table des matières et options de rendu.

### 4.8 `contents.txt`

Ce fichier définit l’ordre officiel de compilation. Tout chapitre destiné au PDF final doit y être ajouté au bon emplacement.

## 5. Rôle du Volume 0

Le Volume 0 constitue la constitution documentaire du projet. Il contient les règles communes qui s’appliquent aux cinq livres et au Companion Pack.

Il traite notamment :

- de la vision générale ;
- des règles fondamentales ;
- de l’architecture documentaire ;
- des identifiants ;
- des conventions Markdown et Pandoc ;
- des standards techniques ;
- de la compatibilité ;
- de l’assurance qualité ;
- des politiques de publication.

Les autres livres ne doivent pas redéfinir ces règles. Ils doivent les appliquer et y renvoyer.

## 6. Rôle des cinq livres

### 6.1 Livre I — Préparer la plateforme

Le Livre I traite de l’installation et de la configuration de l’environnement local : matériel, pilotes AMD, Docker, Open WebUI, Open Terminal, Vane, ComfyUI, Ollama, llama.cpp, LocalAI, LibreChat et outils audio.

### 6.2 Livre II — Développer le jeu et la plateforme IA

Le Livre II couvre Godot, GDScript, l’architecture logicielle, les douze grands systèmes de gameplay, l’intégration des services IA et l’industrialisation du projet.

### 6.3 Livre III — Produire les contenus et les assets

Le Livre III traite de la direction artistique, des personnages, humanoïdes, animaux, créatures, objets, environnements, animations, VFX, UI, UX, audio, cinématiques et pipelines de production.

### 6.4 Livre IV — Finaliser, publier et maintenir

Le Livre IV couvre l’équilibrage, les tests, la QA, le diagnostic, l’optimisation, le multijoueur, le DevOps, la publication, les mises à jour, la localisation, l’accessibilité et la pérennité.

### 6.5 Livre V — Encyclopédie technique

Le Livre V est une documentation de consultation. Il centralise les fiches techniques, workflows, prompts, scripts, structures de données, arbres de décision, matrices de compatibilité et checklists.

## 7. Rôle du Companion Pack

Le Companion Pack contient les artefacts directement réutilisables. Il complète les livres sans remplacer leurs explications.

Il peut contenir :

- projets Godot de référence ;
- scripts GDScript, Python, SQL, Bash et PowerShell ;
- fichiers Docker Compose ;
- schémas SQLite ;
- exemples JSON ;
- workflows ComfyUI ;
- templates Blender ;
- prompts versionnés ;
- tests automatisés ;
- modèles de documents ;
- diagrammes sources.

Chaque ressource du Companion Pack doit posséder un identifiant et une fiche associée dans le Livre V lorsque sa complexité le justifie.

## 8. Organisation interne d’un livre

Chaque livre possède au minimum :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Livre-X/
├── index.md
├── CHAPITRE-01-....md
├── CHAPITRE-02-....md
├── assets/
└── annexes/
```

Le fichier `index.md` contient :

- le titre du livre ;
- sa finalité ;
- la liste ordonnée des chapitres ;
- leur statut ;
- les dépendances principales ;
- les références vers le Companion Pack.

Les illustrations propres à un livre sont placées dans son dossier `assets/`. Les ressources partagées par plusieurs livres sont placées dans le dossier racine `assets/`.

## 9. Organisation interne d’un chapitre

Un chapitre complet suit une structure commune lorsque les sections sont pertinentes :

1. métadonnées YAML ;
2. titre et identifiant ;
3. objectifs ;
4. public et prérequis ;
5. classement Obligatoire, Recommandé ou Optionnel ;
6. Mode Solo et Mode Studio ;
7. concepts théoriques ;
8. procédure pas à pas ;
9. exemples simples puis avancés ;
10. structure des fichiers ;
11. code, données ou diagrammes ;
12. erreurs fréquentes ;
13. bonnes pratiques ;
14. optimisation ;
15. tests et checklist ;
16. références croisées ;
17. ressources du Companion Pack ;
18. historique des modifications.

Toutes ces sections ne sont pas obligatoires dans les chapitres purement normatifs du Volume 0. Leur pertinence doit être évaluée en fonction du sujet.

## 10. Architecture des ressources transversales

### 10.1 `assets/`

Contient les images, captures, icônes et médias communs à plusieurs volumes.

### 10.2 `diagrams/`

Contient les sources Mermaid, PlantUML ou autres formats textuels de diagrammes. Les rendus exportés peuvent être placés dans `assets/diagrams/`.

### 10.3 `scripts/`

Contient les scripts de construction, validation et automatisation documentaire. Les scripts propres au jeu appartiennent plutôt au Companion Pack.

### 10.4 `templates/`

Contient les modèles Markdown, Pandoc, LaTeX, HTML et les fiches standardisées.

### 10.5 `database/`

Contient les schémas, migrations et exemples de bases utilisés dans le Companion Pack.

### 10.6 `workflows/`

Contient les workflows réutilisables, en particulier ComfyUI et les automatisations de production.

### 10.7 `tests/`

Contient les tests documentaires et techniques : validation des liens, lint Markdown, vérification JSON, tests SQL et scripts de compilation.

### 10.8 `dist/`

Contient uniquement les fichiers générés : PDF, HTML, archives et rapports. Ce dossier n’est pas une source éditoriale.

## 11. Gestion des dépendances documentaires

Les dépendances entre chapitres doivent rester explicites.

Une référence croisée utilise de préférence :

- l’identifiant stable de la ressource ;
- le titre humainement lisible ;
- un lien relatif lorsque la destination existe déjà.

Exemple :

> **[VSC] Visual Studio Code - Créer ou modifier :** `dist/`.

```markdown
Voir `DOC-V0-CH04 — Convention des identifiants`.
```

Lorsqu’un chapitre dépend d’un logiciel ou d’une procédure expliqué ailleurs, il doit résumer le strict minimum puis renvoyer vers la source de référence.

## 12. Prévention des doublons

Avant d’ajouter une nouvelle section, l’auteur doit vérifier :

1. si le sujet existe déjà ;
2. quel chapitre en est la source de vérité ;
3. si une référence croisée suffit ;
4. si le nouveau contenu apporte une information réellement distincte.

Les répétitions pédagogiques courtes sont acceptables lorsqu’elles facilitent la compréhension, mais elles doivent rester identifiées comme des rappels.

## 13. Gestion des versions

Chaque fichier structurant possède une version dans son en-tête YAML.

- une correction mineure incrémente le correctif ;
- un ajout compatible incrémente la version mineure ;
- une restructuration incompatible incrémente la version majeure.

Les versions du dépôt et celles des chapitres peuvent évoluer indépendamment. Le changelog du dépôt enregistre les versions publiées, tandis que l’historique du chapitre décrit ses modifications propres.

## 14. Architecture Solo et Studio

L’architecture documentaire doit servir deux parcours.

### Mode Solo

Le lecteur individuel doit pouvoir suivre uniquement les éléments essentiels, utiliser des workflows simplifiés et limiter les outils d’organisation lourds.

### Mode Studio

Les équipes disposent de sections supplémentaires sur la collaboration, les responsabilités, la revue, les branches, l’intégration continue et la validation collective.

Ces deux modes sont des annotations transversales. Ils ne doivent pas conduire à dupliquer deux versions complètes du guide.

## 15. Publication multi-format

Le Markdown est la source officielle. Les formats suivants sont des sorties générées :

- PDF ;
- HTML ;
- EPUB ou DOCX lorsque pertinent ;
- archives de version.

Une correction apportée directement à un PDF n’est jamais considérée comme valide tant qu’elle n’a pas été répercutée dans la source Markdown.

## 16. Contrôles de cohérence

Avant chaque publication, les vérifications suivantes doivent être exécutées :

- tous les fichiers de `contents.txt` existent ;
- les identifiants sont uniques ;
- les liens relatifs sont valides ;
- les blocs de code indiquent leur langage ;
- les métadonnées YAML sont valides ;
- les fichiers générés ne sont pas mélangés aux sources ;
- les statuts des index correspondent à la roadmap ;
- les ressources du Companion Pack citées existent ou sont marquées comme planifiées.

## 17. Exemple de flux éditorial

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Nouvelle idée
    ↓
Recherche de contenu existant
    ↓
Choix du livre et du chapitre
    ↓
Attribution d’un identifiant
    ↓
Rédaction Markdown
    ↓
Relecture technique et éditoriale
    ↓
Mise à jour des index
    ↓
Ajout à contents.txt
    ↓
Compilation de test
    ↓
Commit et changelog
```

## 18. Checklist de validation

- [ ] Le rôle de chaque livre est défini.
- [ ] Le Volume 0 reste la source normative.
- [ ] Le Companion Pack est séparé du texte pédagogique.
- [ ] Chaque chapitre possède un emplacement unique.
- [ ] Les dépendances documentaires sont explicites.
- [ ] Les contenus générés sont séparés des sources.
- [ ] La compilation suit `contents.txt`.
- [ ] Les modes Solo et Studio sont transversaux.
- [ ] Les doublons sont évités.
- [ ] Les index et la roadmap sont synchronisés.

## 19. Références croisées

- `DOC-V0-CH01 — Vision générale du projet`
- `DOC-V0-CH02 — Les 21 règles fondamentales`
- `DOC-V0-CH04 — Convention des identifiants`
- `STYLE_GUIDE.md`
- `BUILD.md`
- `CONTRIBUTING.md`

## 20. Historique des modifications

| Version | Modification |
|---|---|
| 0.1.0 | Première rédaction complète de l’architecture documentaire. |
