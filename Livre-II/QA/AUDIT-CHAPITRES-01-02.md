---
title: "Audit post-création — Livre II, chapitres 1 et 2"
id: "DOC-L2-QA-AUDIT-CH01-CH02"
status: "complete"
version: "2.3.0"
book: "Livre II"
category: "quality-report"
validation-date: "2026-07-18"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
validation-evidence: "Livre-II/QA/VALIDATION-FINALE-CHAPITRES-01-02.yaml"
---

# Audit post-création — Livre II, chapitres 1 et 2

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](../../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## 1. Périmètre

Documents contrôlés :

- `DOC-L2-CH01` — Découvrir Godot et créer le projet fil rouge ;
- `DOC-L2-CH02` — Fondamentaux de GDScript ;
- `DOC-L2-QA-POST-CREATION` — protocole d’audit ;
- l’index du Livre II, la roadmap et les contrôles CI associés.

Cette campagne reprend les audits précédents et ajoute deux contrôles ciblés au chapitre 2 :

- l’absence de doublons exacts significatifs ;
- la profondeur des explications relatives aux fonctions, méthodes, paramètres, arguments, valeurs par défaut et valeurs de retour.

## 2. Méthode

Les deux chapitres ont été relus selon les portes suivantes :

- complétude pédagogique et frontières avec les chapitres suivants ;
- versions, sources officielles et exactitude des affirmations ;
- relecture statique des commandes et extraits GDScript ;
- identification des fichiers réellement à créer ;
- distinction entre commandes, interfaces graphiques, sorties et exemples ;
- contrôle automatique de présence et de cohérence des repères ;
- recherche des titres, paragraphes longs et blocs de code dupliqués ;
- vérification de la décomposition pédagogique des fonctions et paramètres ;
- compilation Pandoc/XeLaTeX et inspection du PDF.

Le projet fil rouge exécutable n’est pas encore matérialisé dans le dépôt. La campagne reste donc au niveau **static-review** et ne revendique pas l’exécution de chaque extrait.

## 3. Vérification technique actualisée

La version de référence reste Godot `4.7.1-stable`. La lecture confirme notamment :

- la distinction entre l’édition Standard et l’édition .NET ;
- Forward+ comme renderer principal du parcours ;
- `--quit-after` exprimé en nombre d’itérations de la boucle principale ;
- la présence et l’usage pédagogique de `is`, `as` et `await` en GDScript ;
- l’épinglage des références à la documentation Godot 4.7 lorsque possible.

Aucune correction technique majeure supplémentaire n’a été nécessaire dans le corps pédagogique lors de cette campagne.

## 4. Chapitre 1 — Godot et projet fil rouge

Le chapitre couvre toujours correctement l’installation portable, le choix du renderer, la création du dépôt, l’arborescence, la scène de bootstrap, le premier script, la validation graphique et headless, Git, les licences et le diagnostic.

### Contextes explicites

- les commandes Windows et Godot headless utilisent `[PS]` ;
- `docs/environment/godot-reference.yaml`, `.gitignore`, `.gitattributes`, `README.md` et `main.gd` utilisent `[VSC]` avec leur chemin ;
- la création du projet, les nœuds, l’Inspector, les raccourcis d’exécution et le dock FileSystem utilisent `[APP]` ;
- les listes de fichiers et sorties de l’éditeur utilisent `[SORTIE]` ;
- les arborescences et exemples conceptuels utilisent `[LECTURE]` ;
- les téléchargements procéduraux utilisent `[WEB]`.

### Décision

**Accepté avec réserve runtime.** Le lecteur dispose du programme, de l’action et du chemin nécessaires avant chaque étape procédurale.

## 5. Chapitre 2 — Fondamentaux de GDScript

Le chapitre couvre la syntaxe, le typage, les collections, fonctions, classes, annotations, cycle de vie, erreurs, débogage et l’exercice `BootstrapReport`.

### Progression pédagogique sans doublon

Le chapitre applique désormais trois niveaux :

1. la première apparition d’un concept reçoit une définition complète, une lecture de gauche à droite et un résultat concret ;
2. une réutilisation reçoit un rappel bref et un renvoi vers la première définition ;
3. une nouvelle combinaison explique uniquement ce qu’elle ajoute.

Ainsi, la section 17.3 explique complètement `%s`, `%`, `key` et `metrics[key]`. La section 25 ne répète pas cette leçon : elle ajoute `%d`, `%f`, les précisions décimales et `%%`.

La section 10.3 se limite au contrat typé d’une fonction, tandis que la section 18 définit fonction, méthode, paramètre, argument, valeur par défaut, type de retour, valeur de retour, appelant et portée locale.

### Fonctions et paramètres renforcés

Les éléments suivants sont maintenant décomposés ligne par ligne :

- fonction simple et association des arguments aux paramètres ;
- paramètres obligatoires et paramètres avec valeur par défaut ;
- fonction privée conventionnelle et chaîne de méthodes ;
- fonction statique et appel par le nom de classe ;
- fonction suspendue avec `await` ;
- rôle de `delta` dans `_process()` et `_physics_process()` ;
- transmission d’un argument à une autre fonction ;
- valeur de retour, type de retour et `void` ;
- boucles sur tableaux et dictionnaires, `while`, `break` et `continue`.

### Contrôle dédié des doublons

Le contrôle permanent `tools/audit_gdscript_ch02.py` recherche :

- les titres identiques ;
- les blocs de code multilignes identiques et significatifs ;
- les paragraphes longs identiques ;
- l’absence d’une explication pédagogique obligatoire.

Résultat de la campagne :

- titres contrôlés : **152** ;
- blocs de code significatifs contrôlés : **57** ;
- paragraphes longs contrôlés : **22** ;
- doublons exacts significatifs : **0** ;
- explications obligatoires manquantes : **0**.

### Contextes explicites

- les commandes de création de dossiers, Git et tests headless utilisent `[PS]` ;
- les fichiers `bootstrap_report.gd`, `main.gd` et `.gitattributes` utilisent `[VSC]` avec leur chemin ;
- les extraits servant uniquement à apprendre la syntaxe utilisent `[LECTURE]` ;
- les sorties de tests et journaux attendus utilisent `[SORTIE]` ;
- le placement d’un point d’arrêt dans l’éditeur Godot utilise `[APP]` ;
- les liens procéduraux utilisent `[WEB]`.

### Décision

**Accepté avec réserve runtime.** Les fonctions, méthodes, paramètres, arguments, valeurs par défaut et retours sont explicités au niveau débutant ; aucun doublon exact significatif n’est accepté par la CI.

## 6. Non-conformités corrigées

| ID | Gravité | Constat | Résolution |
|---|---|---|---|
| L2-AUD-014 | majeure | Les chapitres ne présentaient pas la légende commune des outils et contextes. | Ajout de la convention `DOC-V0-ANN-CONTEXTES` et de sa métadonnée. |
| L2-AUD-015 | majeure | Les commandes PowerShell et Godot headless n’indiquaient pas systématiquement le terminal. | Ajout de `[PS]` devant chaque bloc concerné. |
| L2-AUD-016 | majeure | Certains contenus YAML, Git et GDScript ne précisaient pas clairement le fichier à créer. | Ajout de `[VSC]`, de l’action et du chemin cible. |
| L2-AUD-017 | majeure | Des valeurs destinées au Project Manager, à l’arbre de scène ou à l’Inspector pouvaient sembler être de simples exemples. | Ajout de `[APP]` avec le nom de l’interface et l’action. |
| L2-AUD-018 | mineure | Sorties, raccourcis et structures de référence pouvaient être recopiés sans distinction. | Séparation `[SORTIE]`, `[APP]` et `[LECTURE]`. |
| L2-AUD-019 | majeure | Le workflow des contextes ne surveillait pas `Livre-II/**/*.md`. | Extension permanente du déclencheur et des scripts au Livre II. |
| L2-AUD-020 | majeure | Le premier prototype de migration pouvait insérer un repère dans le front matter YAML. | Rejet du prototype avant écriture et remplacement par une migration déterministe. |
| L2-AUD-021 | majeure | Le vérificateur sémantique et le rapporteur de couverture ne contrôlaient pas encore le Livre II. | Extension des deux outils et ajout de métriques par chapitre. |
| L2-AUD-022 | majeure | Plusieurs exemples introduisaient des symboles, types ou accès sans les expliquer suffisamment pour un débutant. | Ajout d’une méthode de lecture syntaxique et de décompositions ligne par ligne. |
| L2-AUD-023 | majeure | Les exemples de classes natives/personnalisées et de parcours de dictionnaire supposaient des connaissances préalables. | Explication détaillée de `Node3D`, `Camera3D`, `BootstrapReport`, `%s`, `%`, `key` et `metrics[key]`. |
| L2-AUD-024 | majeure | Le chapitre ne distinguait pas formellement répétition pédagogique et progression. | Ajout d’une règle de première définition, rappel bref et nouvelle combinaison. |
| L2-AUD-025 | majeure | Plusieurs fonctions secondaires et paramètres (`value`, `delta`, fonctions statiques ou privées) restaient trop peu décomposés. | Ajout de lectures ligne par ligne, exemples d’appels et résultats concrets. |
| L2-AUD-026 | majeure | L’absence de doublons n’était pas démontrée par un contrôle dédié. | Ajout de `tools/audit_gdscript_ch02.py` et d’un workflow permanent. |

Les treize corrections de l’audit précédent restent acquises. Aucune ancienne correction n’a été annulée.

## 7. Frontières entre les chapitres

La séparation reste cohérente :

- le chapitre 1 installe le moteur et crée une scène minimale ;
- le chapitre 2 enseigne le langage sans définir l’architecture globale ;
- le chapitre 3 approfondira scènes, instances, Resources et signaux ;
- le chapitre 4 définira l’architecture modulaire ;
- les services globaux et bus d’événements restent réservés au chapitre 5.

Aucune duplication majeure ou consommation prématurée du périmètre suivant n’a été détectée.

## 8. Validation automatisée et preuve

Les identifiants des exécutions finales, les empreintes des artefacts, les métriques anti-doublon, les métriques de repérage et les caractéristiques du PDF sont conservés dans :

`Livre-II/QA/VALIDATION-FINALE-CHAPITRES-01-02.yaml`

Ce fichier de preuve n’est pas compilé dans le PDF. Cette séparation évite qu’une modification du présent rapport change la pagination qu’il décrit.

## 9. Portes qualité

- [x] Q0 — Intégrité des fichiers et métadonnées
- [x] Q1 — Complétude pédagogique
- [x] Q2 — Cohérence avec le sommaire maître
- [x] Q3 — Relecture technique statique
- [x] Q4 — Outils et contextes d’utilisation
- [x] Q5 — Sécurité et licences documentées
- [x] Q6 — Anti-doublon, compilation et inspection PDF finales
- [ ] Runtime — Exécution sur le projet matérialisé

Q6 est validée par trois workflows réussis — contextes, audit GDScript et documentation — ainsi que par l’inspection visuelle de huit pages ciblées. La réserve runtime demeure indépendante.

## 10. Règle permanente

Chaque prochain chapitre du Livre II devra être présenté comme **rédigé, repéré et audité**. Pour les chapitres de programmation destinés aux débutants, la première apparition d’une fonction ou d’un paramètre devra également être décomposée et accompagnée d’un exemple d’appel ou de résultat.
