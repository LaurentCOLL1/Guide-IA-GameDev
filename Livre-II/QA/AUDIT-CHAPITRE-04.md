---
title: "Audit post-création — Livre II, chapitre 4"
id: "DOC-L2-QA-AUDIT-CH04"
status: "complete"
version: "1.1.0"
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

Niveau annoncé avant rédaction : **GPT-5.6 Sol — Élevée**.

## 2. Méthode

La campagne comprend :

- comparaison au plan maître du Livre II ;
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
- seconde compilation après correction des pages rognées ;
- déclaration explicite des limites runtime.

## 3. Couverture du plan maître

Le chapitre couvre :

- couches et dossiers ;
- domaine, application, présentation, données, infrastructure et outils ;
- modules fonctionnels ;
- dépendances autorisées ;
- composition, interfaces implicites et contrats ;
- prévention des singletons omniprésents et scènes monolithiques ;
- diagramme d’architecture ;
- nommage, ownership et frontières ;
- arborescence canonique ;
- ADR initiale ;
- règles d’import ;
- matrice de dépendances.

Décision de périmètre : **conforme**.

Le registre de services, les Autoloads définitifs, l’injection de dépendances et le bus global restent au chapitre 5.

## 4. Vérification pédagogique

Les concepts suivants sont définis avant usage :

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

Les exemples expliquent notamment :

- le tableau PowerShell `$paths` et `foreach` ;
- `.gdignore` ;
- la matrice des dépendances ;
- les contrats par fonction, classe abstraite, duck typing, signal et Resource ;
- le contrôle du type retourné par un appel dynamique ;
- la migration du module `beacons` ;
- les recherches PowerShell de chemins fragiles.

Les rappels du chapitre 3 se limitent à l’interface publique de `StatusBeacon` nécessaire pour expliquer la frontière du module.

Décision pédagogique : **conforme**.

## 5. Vérification technique statique

### 5.1 Organisation Godot

- l’organisation feature-first reste compatible avec le système de fichiers de Godot ;
- fichiers et dossiers utilisent `snake_case` ;
- nœuds et classes utilisent `PascalCase` ;
- plugins tiers restent dans `addons/` ;
- `.gdignore` ne masque aucune Resource runtime.

### 5.2 Déplacement des fichiers

Le dock FileSystem de Godot est imposé pour déplacer les scènes, scripts et Resources déjà référencés. Une recherche des anciens chemins et une validation headless suivent la migration.

### 5.3 Dépendances

- le domaine ne dépend pas de la présentation ou de l’infrastructure ;
- la présentation ne doit pas ouvrir directement SQLite ou le réseau ;
- l’infrastructure dépend de contrats ;
- `src/app` assemble les implémentations concrètes ;
- `core` ne dépend d’aucun module fonctionnel.

### 5.4 Contrats GDScript

- une fonction publique typée constitue le contrat minimal ;
- `@abstract` est disponible dans Godot 4.7 ;
- l’héritage unique et la limite des classes abstraites sont déclarés ;
- le duck typing vérifie la présence de la méthode et le type du résultat ;
- les signaux et Resources sont présentés comme contrats spécialisés.

### 5.5 Commandes PowerShell

Les commandes indiquent PowerShell 7 et la racine du projet. Les résultats `Select-String` restent des éléments à interpréter, pas une preuve automatique d’erreur.

Décision technique : **conforme au niveau static-review**.

## 6. Contrôle des doublons

La relecture a recherché :

- titres identiques ;
- paragraphes longs répétés ;
- blocs de code significatifs identiques ;
- répétition intégrale des chapitres 2 ou 3 ;
- consommation du périmètre des chapitres 5 et 7.

Résultat éditorial : **aucun doublon majeur détecté**.

Les rappels courts de `StatusBeacon`, `BeaconProfile`, `activate()` et des signaux servent la documentation de l’interface et de sa migration.

## 7. Non-conformités corrigées

| ID | Gravité | Constat | Résolution |
|---|---|---|---|
| L2-CH04-001 | majeure | Une arborescence globale par type aurait dispersé les fonctionnalités. | Adoption feature-first avec couches locales. |
| L2-CH04-002 | majeure | Les couches pouvaient devenir spéculatives. | Création seulement lorsqu’une responsabilité réelle existe. |
| L2-CH04-003 | majeure | Une migration PowerShell pouvait casser les chemins Godot. | Déplacement depuis le dock FileSystem et vérification des anciens chemins. |
| L2-CH04-004 | majeure | Le domaine pouvait dépendre de l’infrastructure. | Direction et matrice de dépendances explicites. |
| L2-CH04-005 | majeure | `core` pouvait devenir un dossier fourre-tout. | Critères stricts et interdiction de dépendre d’une feature. |
| L2-CH04-006 | majeure | La classe abstraite pouvait être comprise comme une interface multiple. | Héritage unique expliqué et exemple rendu optionnel. |
| L2-CH04-007 | majeure | Le duck typing pouvait masquer un retour incompatible. | Vérification `result is not bool` avant renvoi. |
| L2-CH04-008 | mineure | Ownership fonctionnel et `Node.owner` pouvaient être confondus. | Distinction explicite. |
| L2-CH04-009 | mineure | La matrice pouvait autoriser implicitement des accès directs. | Contrats et point de composition explicités. |
| L2-CH04-010 | mineure | Les ADR pouvaient devenir un journal quotidien. | Critères, statuts et historique ajoutés. |
| L2-CH04-011 | gouvernance | Le niveau de raisonnement n’était pas enregistré. | Métadonnée `recommended-reasoning` ajoutée. |
| L2-CH04-012 | majeure | La matrice à huit colonnes et des lignes ADR étaient rognées dans le PDF. | Matrice compacte, ADR reformatée et seconde inspection réussie. |

Aucune non-conformité majeure reste ouverte au niveau documentaire.

## 8. Contextes d’utilisation

Le chapitre utilise :

- `[PS]` pour les créations, recherches et validations headless ;
- `[VSC]` pour README, ADR, matrice et contrats ;
- `[APP]` pour les déplacements dans Godot ;
- `[SORTIE]` pour chemins et arborescences attendus ;
- `[LECTURE]` pour diagrammes et exemples non exécutables ;
- `[WEB]` dans la légende et les références.

Le workflow permanent des contextes a réussi.

## 9. Sécurité, licences et réversibilité

- aucune commande destructive ;
- aucun secret réel ;
- aucune dépendance tierce supplémentaire ;
- Godot reste soumis à sa licence MIT ;
- chaque plugin futur exige version, source, licence et procédure de suppression ;
- la migration est progressive ;
- les ADR remplacées restent conservées.

## 10. Validation CI et PDF

Campagne finale :

- `Validate Usage Contexts` : exécution `29661521005`, réussite ;
- `Validate Documentation` : exécution `29661521014`, réussite ;
- 47 sources déclarées ;
- 10 chapitres du Livre I ;
- 4 chapitres du Livre II ;
- 46 identifiants uniques ;
- 0 erreur bloquante ;
- 1 avertissement : licence globale à définir ;
- PDF A4 1.5 de 580 pages et 1 533 828 octets ;
- texte extractible ;
- aucun chiffrement, JavaScript ou page tournée.

Pages inspectées après correction : 525, 526, 530, 534, 537, 542, 543, 544, 549, 550 et 567 à 571.

Résultat visuel : aucun texte rogné, chevauchement majeur, glyphe manquant ou tableau hors page observé.

La première compilation `29661263709` est conservée uniquement comme preuve du défaut détecté et n’est pas la preuve finale.

## 11. Portes qualité

- [x] Q0 — Intégrité des fichiers et métadonnées
- [x] Q1 — Complétude pédagogique
- [x] Q2 — Cohérence avec le plan maître
- [x] Q3 — Relecture technique statique
- [x] Q4 — Outils et contextes d’utilisation
- [x] Q5 — Sécurité et licences
- [x] Q6 — CI, compilation et inspection PDF
- [ ] Runtime — matérialisation et migration réelle dans le Starter Kit

## 12. Décision

**Accepté avec réserve runtime.**

Le chapitre est rédigé, repéré et audité au niveau documentaire et statique. Il ne doit pas être présenté comme `runtime-tested` tant que l’arborescence, les déplacements et les commandes n’ont pas été exécutés dans le projet matérialisé.