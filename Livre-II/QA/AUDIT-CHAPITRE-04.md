---
title: "Audit post-création — Livre II, chapitre 4"
id: "DOC-L2-QA-AUDIT-CH04"
status: "complete"
version: "1.0.0"
book: "Livre II"
chapter: 4
category: "quality-report"
validation-date: "2026-07-18"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
validation-evidence: "Livre-II/QA/VALIDATION-FINALE-CHAPITRE-04.yaml"
---

# Audit post-création — Livre II, chapitre 4

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir, **[LECTURE]** exemple à étudier. Voir la [convention complète](../../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## 1. Périmètre

Document contrôlé :

- `DOC-L2-CH04` — Architecture modulaire du projet.

Documents de cohérence contrôlés :

- `Livre-II/index.md` ;
- `Livre-II/CHAPITRE-03-Scenes-noeuds-Resources-et-signaux.md` ;
- `Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md` ;
- `ROADMAP.md` ;
- `contents.txt` ;
- `CONTINUITE-PROJET.md`.

Version de référence : Godot `4.7.1-stable`, édition Standard, GDScript, renderer Forward+.

Niveau recommandé avant rédaction : **GPT-5.6 Sol — Élevée**.

## 2. Méthode

La campagne comprend :

- comparaison au plan maître historique du Livre II ;
- lecture pédagogique pour débutants ;
- contrôle des frontières avec les chapitres 3, 5, 7, 27 et 29 ;
- vérification de l’arborescence canonique ;
- revue de la matrice des dépendances ;
- revue statique des exemples GDScript et PowerShell ;
- vérification des contrats, fonctions, paramètres, types et retours ;
- contrôle des repères d’utilisation ;
- contrôle éditorial des répétitions ;
- vérification contre les bonnes pratiques officielles Godot 4.7 ;
- compilation et inspection PDF par la CI ;
- déclaration explicite des limites runtime.

## 3. Couverture du plan maître

Le plan exigeait :

- définition des couches et dossiers ;
- séparation domaine, présentation, données, infrastructure et outils ;
- organisation par modules fonctionnels ;
- dépendances autorisées ;
- composition, interfaces implicites et contrats ;
- prévention des singletons omniprésents et scènes monolithiques ;
- diagramme d’architecture ;
- conventions de nommage, ownership et frontières ;
- arborescence canonique ;
- ADR initiale ;
- règles d’import ;
- matrice de dépendances.

Tous ces points sont couverts.

Décision de périmètre : **conforme**.

Le chapitre ne construit pas le registre de services, les Autoloads définitifs, l’injection de dépendances ou le bus global. Ces éléments restent au chapitre 5.

## 4. Vérification pédagogique

Les concepts suivants sont définis avant leur usage opérationnel :

- architecture ;
- module ;
- couche ;
- dépendance ;
- couplage ;
- cohésion ;
- contrat ;
- frontière ;
- composition root ;
- ADR ;
- feature-first.

Les exemples sont associés à une explication de leur rôle :

- tableau PowerShell `$paths` et boucle `foreach` ;
- `.gdignore` ;
- matrice depuis/vers ;
- contrat par fonction ;
- classe et méthode abstraites ;
- duck typing avec `has_method()` et `call()` ;
- contrat par signal et Resource ;
- `Callable` de transition vers le chapitre 5 ;
- recherches PowerShell de chemins fragiles.

Les répétitions du chapitre 3 sont limitées à l’interface publique de `StatusBeacon`, nécessaire pour expliquer la frontière du module.

Décision pédagogique : **conforme**.

## 5. Vérification technique statique

### 5.1 Organisation Godot

- l’organisation feature-first reste compatible avec le système de fichiers direct de Godot ;
- les fichiers et dossiers utilisent `snake_case` ;
- les noms de nœuds et classes utilisent `PascalCase` ;
- les plugins tiers restent dans `addons/` ;
- `.gdignore` n’est placé que dans `docs` et `tools`, qui ne contiennent pas de Resources runtime.

### 5.2 Déplacement des fichiers

Le chapitre impose le dock FileSystem de Godot pour déplacer les scènes, scripts et Resources déjà référencés.

Une recherche des anciens chemins et une réexécution headless sont exigées après migration.

### 5.3 Dépendances

- le domaine ne dépend pas de la présentation ou de l’infrastructure ;
- la présentation ne doit pas ouvrir directement SQLite ou le réseau ;
- l’infrastructure dépend de contrats, pas de détails de présentation ;
- `src/app` constitue le point d’assemblage des implémentations concrètes ;
- `core` ne dépend d’aucun module fonctionnel.

### 5.4 Contrats GDScript

- une fonction publique typée constitue le contrat minimal ;
- `@abstract` est disponible dans Godot 4.7 ;
- une classe abstraite ne peut pas être attachée à un nœud ni contourner l’héritage unique ;
- le duck typing est associé à `has_method()` et à un avertissement sur sa sûreté ;
- les signaux et Resources sont présentés comme contrats spécialisés.

### 5.5 Commandes PowerShell

Les commandes utilisent PowerShell 7 et indiquent la racine du projet.

Les recherches `Select-String` sont présentées comme des contrôles à interpréter, pas comme une preuve automatique qu’une dépendance est invalide.

Décision technique : **conforme au niveau static-review**.

## 6. Contrôle des doublons

La relecture recherche :

- titres identiques ;
- paragraphes longs répétés ;
- blocs de code significatifs identiques ;
- répétition intégrale des chapitres 2 ou 3 ;
- duplication du périmètre du chapitre 5 ;
- répétition des règles de données du chapitre 7.

Résultat éditorial : **aucun doublon majeur détecté**.

Les répétitions courtes des noms `StatusBeacon`, `BeaconProfile`, `activate()` et des signaux sont nécessaires pour documenter l’interface publique du module et sa migration.

## 7. Non-conformités corrigées pendant la rédaction et la seconde lecture

| ID | Gravité | Constat | Résolution |
|---|---|---|---|
| L2-CH04-001 | majeure | Une arborescence globale par type aurait dispersé chaque fonctionnalité. | Adoption feature-first avec couches locales. |
| L2-CH04-002 | majeure | Les couches pouvaient devenir des dossiers vides et spéculatifs. | Ajout d’une règle de création uniquement lorsqu’une responsabilité existe. |
| L2-CH04-003 | majeure | La migration par PowerShell pouvait casser les chemins Godot. | Déplacement obligatoire depuis le dock FileSystem et vérification des anciens chemins. |
| L2-CH04-004 | majeure | Le domaine pouvait dépendre de détails d’infrastructure. | Matrice explicite et direction des dépendances. |
| L2-CH04-005 | majeure | `core` pouvait devenir un dossier partagé sans propriétaire. | Critères stricts d’entrée dans `core` et interdiction de dépendre d’une feature. |
| L2-CH04-006 | majeure | La classe abstraite pouvait être présentée comme une interface multiple. | Explication de l’héritage unique et exemple rendu optionnel. |
| L2-CH04-007 | majeure | Le duck typing pouvait masquer une signature incompatible. | Ajout de `has_method()`, type `Variant`, avertissement et frontière documentée. |
| L2-CH04-008 | mineure | `owner` architectural pouvait être confondu avec `Node.owner`. | Distinction entre propriétaire fonctionnel et propriété Godot. |
| L2-CH04-009 | mineure | La matrice pouvait être interprétée comme une permission d’accès direct aux fichiers. | Ajout d’explications sur contrats et point de composition. |
| L2-CH04-010 | mineure | Les ADR pouvaient être traitées comme un journal quotidien. | Ajout des critères d’utilisation, statuts et conservation historique. |
| L2-CH04-011 | gouvernance | Le niveau de raisonnement recommandé devait être enregistré. | Ajout de `recommended-reasoning: "GPT-5.6 Sol — Élevée"`. |

Aucune non-conformité majeure reste ouverte au niveau documentaire.

## 8. Contextes d’utilisation

Le chapitre utilise :

- `[PS]` pour les créations, recherches et validations headless ;
- `[VSC]` pour les README, ADR, matrice et exemples de contrats ;
- `[APP]` pour les déplacements sécurisés dans Godot ;
- `[SORTIE]` pour les chemins et arborescences attendus ;
- `[LECTURE]` pour diagrammes, comparaisons et exemples non exécutables ;
- `[WEB]` dans la légende et les références.

Chaque bloc procédural doit réussir le workflow permanent des contextes.

## 9. Sécurité, licences et réversibilité

- aucune commande destructive n’est demandée ;
- aucun secret réel n’est utilisé ;
- aucune dépendance tierce supplémentaire n’est imposée ;
- Godot reste soumis à sa licence MIT ;
- les plugins futurs exigent version, source, licence et procédure de suppression ;
- la migration est progressive et vérifiée avant suppression des anciens chemins ;
- les ADR remplacées restent conservées.

## 10. Validation CI et PDF

À enregistrer après exécution :

- contrôle structurel ;
- contextes d’utilisation ;
- compilation Pandoc/XeLaTeX ;
- inspection technique du PDF ;
- extraction du texte ;
- inspection visuelle ciblée ;
- preuve YAML indépendante.

## 11. Portes qualité

- [x] Q0 — Intégrité des fichiers et métadonnées
- [x] Q1 — Complétude pédagogique
- [x] Q2 — Cohérence avec le plan maître
- [x] Q3 — Relecture technique statique
- [x] Q4 — Outils et contextes d’utilisation, sous réserve du workflow
- [x] Q5 — Sécurité et licences
- [ ] Q6 — CI, compilation et inspection PDF : à enregistrer après exécution
- [ ] Runtime — matérialisation et migration réelle dans le Starter Kit

## 12. Décision provisoire

**Accepté avec réserves CI et runtime au moment de la création du rapport.**

La décision deviendra **Accepté avec réserve runtime** après réussite des workflows, inspection du PDF et enregistrement des preuves dans `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-04.yaml`.

Le chapitre ne doit pas être présenté comme `runtime-tested` tant que l’arborescence, les déplacements et les commandes n’ont pas été exécutés dans le projet matérialisé.