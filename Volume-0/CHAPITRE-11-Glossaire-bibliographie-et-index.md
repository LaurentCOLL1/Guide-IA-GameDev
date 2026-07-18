---
title: "Chapitre 11 — Glossaire, bibliographie et index"
id: "DOC-V0-CH11"
status: "draft"
version: "0.4.0"
book: "Volume 0"
chapter: 11
level: "Débutant à avancé"
tags:
  - documentation
  - glossaire
  - bibliographie
  - index
  - traçabilité
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Chapitre 11 — Glossaire, bibliographie et index

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## Objectif du chapitre

Ce chapitre définit la manière dont les termes, les sources et les points d’entrée du guide sont organisés. Son rôle est de garantir qu’un lecteur puisse :

- comprendre rapidement un terme technique ;
- retrouver la source d’une affirmation ;
- naviguer entre les livres sans parcourir toute la collection ;
- distinguer une définition, une recommandation, une contrainte et une décision de projet ;
- identifier les informations dépendantes d’une version ;
- retrouver une procédure, un outil, un format, un système de jeu ou une ressource du Companion Pack.

> [!IMPORTANT]
> Le glossaire, la bibliographie et les index ne sont pas des annexes décoratives. Ils constituent une infrastructure de navigation, de vérification et de maintenance.

## 1. Principes généraux

La collection applique les principes suivants :

1. un terme important doit être défini une seule fois dans une entrée canonique ;
2. une affirmation externe doit pouvoir être reliée à une source identifiable ;
3. une information liée à un logiciel doit indiquer sa version ou sa période de validité lorsque cela est pertinent ;
4. un index doit orienter vers l’emplacement canonique, et non recopier son contenu ;
5. les alias et synonymes doivent être redirigés vers le terme principal ;
6. les termes ambigus doivent préciser leur contexte ;
7. les ressources du Companion Pack doivent être indexées avec leur identifiant stable ;
8. les entrées obsolètes ne doivent pas disparaître sans trace : elles sont dépréciées et redirigées.

## 2. Le glossaire central

### 2.1 Rôle

Le glossaire central fournit les définitions normatives de la collection. Il doit couvrir au minimum :

- les outils ;
- les bibliothèques ;
- les moteurs ;
- les formats ;
- les concepts de programmation ;
- les concepts de production 3D ;
- les concepts d’IA générative ;
- les concepts de déploiement et d’exploitation ;
- les concepts de gameplay ;
- les termes juridiques et de licence nécessaires au projet.

### 2.2 Emplacement canonique

Le glossaire global sera placé dans :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Volume-0/annexes/GLOSSAIRE.md
```

Les glossaires propres à un livre peuvent être placés dans :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Livre-X/annexes/GLOSSAIRE-LIVRE-X.md
```

Ils ne doivent contenir que les termes très spécialisés du livre. Toute notion transversale appartient au glossaire global.

### 2.3 Structure d’une entrée

Chaque entrée suit cette structure :

> **[VSC] Visual Studio Code - Créer ou modifier :** `text Livre-X/annexes/GLOSSAIRE-LIVRE-X.md`.

```markdown
### Terme canonique

**Identifiant :** `GLS-DOM-NNN`

**Définition :** définition courte et autonome.

**Contexte dans le guide :** usage précis dans le projet fil rouge.

**Alias :** synonymes, anciennes formes ou noms alternatifs.

**Voir aussi :** références vers les chapitres et entrées liées.

**Statut :** actif, déprécié ou historique.
```

### 2.4 Exemple

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```markdown
### Quantification

**Identifiant :** `GLS-AI-012`

**Définition :** réduction de la précision numérique des poids d’un modèle afin de diminuer sa consommation mémoire et, souvent, d’accélérer son exécution.

**Contexte dans le guide :** utilisée pour exécuter des modèles de langage locaux dans une enveloppe RAM ou VRAM limitée.

**Alias :** quantization.

**Voir aussi :** `DOC-V0-CH08`, `L1-AI-LLM-CHXX`.

**Statut :** actif.
```

### 2.5 Règles de rédaction

Une définition doit :

- être compréhensible sans lire un autre chapitre ;
- éviter les formulations circulaires ;
- utiliser le terme français lorsqu’il est établi ;
- mentionner le terme anglais courant lorsqu’il facilite la recherche ;
- distinguer le sens général du sens propre au guide ;
- éviter les opinions ;
- rester courte, puis renvoyer vers les explications longues.

## 3. Catégories du glossaire

Les préfixes suivants sont recommandés :

| Préfixe | Domaine | Exemples |
|---|---|---|
| `GLS-AI` | intelligence artificielle | LLM, RAG, seed, embedding |
| `GLS-ART` | art et production 3D | retopologie, UV, rig |
| `GLS-AUD` | audio | LUFS, stem, phonème |
| `GLS-CODE` | programmation | interface, signal, coroutine |
| `GLS-DATA` | données | schéma, migration, sérialisation |
| `GLS-DEVOPS` | build et exploitation | CI, artefact, rollback |
| `GLS-DOC` | documentation | source de vérité, front matter |
| `GLS-GAME` | gameplay | boucle de jeu, état, progression |
| `GLS-GFX` | rendu graphique | PBR, LOD, shader |
| `GLS-LEGAL` | droit et licences | attribution, copyleft, consentement |
| `GLS-NET` | réseau | RPC, autorité serveur, réplication |
| `GLS-PERF` | performance | frametime, budget VRAM, profiling |
| `GLS-SEC` | sécurité | secret, moindre privilège, sandbox |
| `GLS-TOOL` | outils | Godot, Blender, ComfyUI |

## 4. Gestion des synonymes et variantes

### 4.1 Terme canonique

Un seul terme est choisi comme forme principale. Les autres formes redirigent vers lui.

Exemple :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```markdown
### Maillage

Terme canonique. Voir aussi : mesh.
```

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```markdown
### Mesh

Voir : **Maillage** (`GLS-ART-004`).
```

### 4.2 Anglicismes

L’anglais peut être conservé lorsque :

- le terme français est rare ou ambigu ;
- l’interface du logiciel emploie l’anglais ;
- le terme anglais est nécessaire pour rechercher de la documentation ;
- une traduction artificielle nuirait à la précision.

La première occurrence dans un chapitre doit de préférence prendre la forme :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
maillage (*mesh*)
```

ou :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
*prompt* (instruction fournie à un modèle)
```

### 4.3 Termes dépréciés

Une entrée dépréciée conserve :

- son identifiant ;
- son ancienne définition ;
- la date ou version de dépréciation ;
- la nouvelle entrée recommandée ;
- la raison du changement.

## 5. Bibliographie

### 5.1 Objectif

La bibliographie recense les sources utiles à la vérification, à l’apprentissage et à la maintenance. Elle distingue :

- les sources normatives ;
- les documentations officielles ;
- les publications scientifiques ;
- les ouvrages ;
- les articles techniques ;
- les dépôts de code ;
- les licences ;
- les ressources communautaires.

### 5.2 Hiérarchie de confiance

L’ordre de préférence est :

1. spécification ou norme officielle ;
2. documentation officielle du projet ;
3. dépôt officiel et notes de version ;
4. article scientifique ou publication primaire ;
5. documentation d’un mainteneur reconnu ;
6. ouvrage technique récent ;
7. ressource communautaire vérifiable ;
8. forum ou discussion, uniquement comme piste ou retour d’expérience.

> [!WARNING]
> Une vidéo, un billet de blog ou un message de forum peut être utile, mais ne doit pas être présenté comme une norme officielle sans vérification.

### 5.3 Emplacement

La bibliographie globale sera stockée dans :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Volume-0/annexes/BIBLIOGRAPHIE.md
```

Une version structurée pourra être ajoutée au Companion Pack :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Companion-Pack/knowledge-base/bibliography.yaml
```

### 5.4 Métadonnées minimales

Chaque référence doit contenir autant que possible :

- un identifiant stable ;
- l’auteur ou l’organisation ;
- le titre ;
- la version ;
- l’année ou la date ;
- le type de source ;
- l’URL ou le DOI ;
- la date de consultation pour une ressource web ;
- la licence lorsque la réutilisation est concernée ;
- les chapitres qui utilisent la source.

### 5.5 Format d’une entrée bibliographique

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```markdown
### `BIB-TOOL-001` — Documentation officielle de Godot

- **Organisation :** Godot Engine
- **Titre :** Godot Engine Documentation
- **Type :** documentation officielle
- **Version suivie :** à préciser dans le chapitre concerné
- **URL :** lien officiel
- **Consulté le :** AAAA-MM-JJ
- **Utilisé par :** identifiants des chapitres concernés
- **Notes :** privilégier les pages correspondant à la version du moteur documentée.
```

### 5.6 Citations dans les chapitres

Les références courtes utilisent l’identifiant bibliographique :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Voir `BIB-TOOL-001`.
```

Pour une affirmation critique, le chapitre doit préciser :

- la source ;
- la version ;
- la date si l’information peut évoluer ;
- la nature de l’affirmation : fait, recommandation ou retour d’expérience.

## 6. Gestion des sources web évolutives

Une ressource web peut changer sans avertissement. Pour limiter les erreurs :

- noter la date de consultation ;
- préférer une URL versionnée ;
- enregistrer le numéro de version du logiciel ;
- conserver un résumé de l’information utilisée ;
- éviter de dépendre d’une capture non vérifiable ;
- vérifier les liens avant une publication ;
- remplacer les liens morts par une source équivalente, sans supprimer l’historique.

## 7. Index de la collection

### 7.1 Types d’index

La collection doit fournir plusieurs index complémentaires :

- index alphabétique ;
- index des outils ;
- index des systèmes de jeu ;
- index des formats ;
- index des scripts ;
- index des workflows IA ;
- index des prompts ;
- index des tests et benchmarks ;
- index des erreurs fréquentes ;
- index des décisions architecturales ;
- index des ressources du Companion Pack ;
- index des licences et obligations.

### 7.2 Emplacement recommandé

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Volume-0/annexes/INDEX-ALPHABETIQUE.md
Volume-0/annexes/INDEX-OUTILS.md
Volume-0/annexes/INDEX-SYSTEMES.md
Volume-0/annexes/INDEX-FORMATS.md
Volume-0/annexes/INDEX-LICENCES.md
Livre-V/indexes/
Companion-Pack/indexes/
```

### 7.3 Index alphabétique

L’index alphabétique contient des entrées courtes :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```markdown
- **ComfyUI** — `GLS-TOOL-004`, `L1-IMG-CHXX`, `WF-IMG-XXX`
- **LOD** — `GLS-GFX-018`, `L3-ENV-CHXX`, `L4-PERF-CHXX`
- **RAG** — `GLS-AI-021`, `DOC-V0-CH08`, `L2-AI-CHXX`
```

### 7.4 Index des outils

Chaque outil doit indiquer :

- son rôle ;
- son statut dans le pipeline ;
- les chapitres d’installation ;
- les chapitres d’utilisation ;
- les workflows associés ;
- les alternatives ;
- les contraintes de licence ;
- les versions testées.

### 7.5 Index des systèmes de jeu

Les douze systèmes de gameplay disposent d’un index transversal comprenant :

- l’identifiant du système ;
- sa fiche fonctionnelle ;
- son architecture ;
- ses données ;
- ses scripts ;
- ses tests ;
- ses interfaces utilisateur ;
- ses ressources audio et visuelles ;
- ses dépendances ;
- ses métriques de performance.

### 7.6 Index du Companion Pack

Toute ressource exécutable ou réutilisable du Companion Pack doit être référencée par :

- un identifiant ;
- un chemin ;
- une version ;
- un statut ;
- une licence ;
- des prérequis ;
- une commande ou procédure d’utilisation ;
- les chapitres qui l’expliquent ;
- les tests qui la valident.

## 8. Index des décisions

Les décisions architecturales importantes doivent être consignées sous forme d’ADR (*Architecture Decision Record*).

Emplacement prévu :

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
Companion-Pack/architecture/decisions/
```

Format recommandé :

> **[VSC] Visual Studio Code - Créer ou modifier :** `text Companion-Pack/architecture/decisions/`.

```markdown
# ADR-NNN — Titre de la décision

- **Statut :** proposé, accepté, remplacé ou rejeté
- **Contexte :** problème à résoudre
- **Décision :** choix retenu
- **Conséquences :** avantages, coûts et risques
- **Alternatives :** options étudiées
- **Références :** chapitres, tests et sources
```

L’index des ADR permet de comprendre pourquoi une solution a été choisie, au lieu de seulement constater son existence.

## 9. Index des erreurs et diagnostics

Les erreurs fréquentes doivent être indexées avec :

- un code stable ;
- le message observé ;
- le contexte ;
- les causes probables ;
- les vérifications à effectuer ;
- les corrections ;
- les risques de récidive ;
- les versions concernées.

Exemple d’identifiant :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
ERR-COMFY-ZLUDA-001
ERR-GODOT-IMPORT-004
ERR-DOCKER-PORT-002
```

## 10. Indexation des contenus destinés aux adultes

Les contenus sensibles ou destinés aux adultes sont indexés de manière technique et neutre. L’index doit préciser :

- la catégorie fonctionnelle ;
- les dépendances système ;
- les paramètres de configuration ;
- les avertissements ;
- les contraintes légales ou de plateforme ;
- les options de désactivation ;
- les tests de consentement, d’âge et de filtrage lorsqu’ils sont applicables.

Les intitulés doivent rester descriptifs et non promotionnels.

## 11. Génération et maintenance automatique

Une partie des index pourra être produite automatiquement à partir :

- des métadonnées YAML des chapitres ;
- du registre des identifiants ;
- des manifestes du Companion Pack ;
- des fichiers de modèles ;
- des registres de workflows et de prompts ;
- des rapports de tests ;
- des licences détectées.

Les scripts futurs devront :

1. parcourir les sources ;
2. extraire les identifiants et métadonnées ;
3. vérifier l’unicité ;
4. détecter les références cassées ;
5. générer les index dérivés ;
6. comparer le résultat à la version suivie par Git ;
7. échouer en cas d’incohérence bloquante.

## 12. Matrice de traçabilité

La matrice centrale relie :

| Élément | Relie vers |
|---|---|
| Chapitre | sources, outils, systèmes, scripts, tests |
| Outil | installation, configuration, workflows, licences |
| Système | architecture, données, code, UI, tests |
| Modèle IA | licence, hash, prompt, benchmark, workflow |
| Asset | source, licence, version, import, validation |
| Script | chapitre, dépendances, tests, exemples |
| Test | exigence, système, résultat, plateforme |
| Décision | contexte, alternatives, conséquences |

Cette matrice sera progressivement matérialisée dans le Companion Pack.

## 13. Contrôles qualité

Avant de déclarer un glossaire ou un index valide, vérifier :

- [ ] chaque entrée possède un identifiant unique ;
- [ ] chaque définition est autonome ;
- [ ] les alias redirigent vers une entrée canonique ;
- [ ] les liens relatifs fonctionnent ;
- [ ] les sources indiquent leur type ;
- [ ] les sources évolutives indiquent une date ;
- [ ] les informations dépendantes d’une version sont signalées ;
- [ ] les entrées dépréciées sont conservées ;
- [ ] les ressources du Companion Pack ont un chemin valide ;
- [ ] les index ne dupliquent pas les chapitres ;
- [ ] les termes sensibles sont décrits avec neutralité ;
- [ ] les licences et obligations sont traçables ;
- [ ] la génération automatique est reproductible ;
- [ ] aucune référence obligatoire n’est cassée.

## 14. Mode Solo

En Mode Solo, le minimum recommandé est :

- un glossaire central ;
- une bibliographie simple ;
- un index alphabétique ;
- un index des outils ;
- un index des scripts et workflows ;
- une vérification automatique des liens.

Le mainteneur peut regrouper les données dans peu de fichiers, à condition de conserver les identifiants stables.

## 15. Mode Studio

En Mode Studio, il est recommandé d’ajouter :

- des responsables par domaine ;
- une revue des nouvelles entrées ;
- un registre structuré en YAML ou base de données ;
- une génération automatique dans l’intégration continue ;
- une matrice de traçabilité complète ;
- des ADR obligatoires pour les décisions importantes ;
- un audit périodique des liens, licences et versions ;
- des règles de validation avant fusion.

## 16. Livrables attendus

À terme, ce chapitre doit conduire à la création des fichiers suivants :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Volume-0/annexes/GLOSSAIRE.md
Volume-0/annexes/BIBLIOGRAPHIE.md
Volume-0/annexes/INDEX-ALPHABETIQUE.md
Volume-0/annexes/INDEX-OUTILS.md
Volume-0/annexes/INDEX-SYSTEMES.md
Volume-0/annexes/INDEX-FORMATS.md
Volume-0/annexes/INDEX-LICENCES.md
Companion-Pack/knowledge-base/bibliography.yaml
Companion-Pack/knowledge-base/glossary.yaml
Companion-Pack/indexes/resource-index.yaml
Companion-Pack/architecture/decisions/
```

## 17. Résultat attendu

À l’issue de l’application de ces règles, le lecteur doit pouvoir partir d’un terme, d’un outil, d’une erreur, d’un système ou d’une ressource et retrouver rapidement :

- sa définition ;
- sa source ;
- son chapitre canonique ;
- sa version ;
- ses dépendances ;
- ses exemples ;
- ses tests ;
- ses contraintes de licence ;
- son emplacement dans le Companion Pack.

Le glossaire, la bibliographie et les index constituent ainsi la carte de navigation et la mémoire technique de l’ensemble du projet.

## Checklist de fin de chapitre

- [x] Le rôle du glossaire est défini.
- [x] Le format des entrées est normalisé.
- [x] Les règles de synonymes et de dépréciation sont définies.
- [x] La hiérarchie des sources est précisée.
- [x] Le format bibliographique est défini.
- [x] Les principaux index sont recensés.
- [x] Les décisions architecturales sont intégrées.
- [x] Les erreurs et diagnostics sont indexables.
- [x] La traçabilité du Companion Pack est prévue.
- [x] Les modes Solo et Studio sont distingués.
- [x] Les livrables futurs sont identifiés.
