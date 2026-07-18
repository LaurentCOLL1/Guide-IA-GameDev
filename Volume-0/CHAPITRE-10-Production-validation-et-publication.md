---
title: "Chapitre 10 — Production, validation et publication"
id: "DOC-V0-CH10"
status: "draft"
version: "0.5.0"
book: "Volume 0"
chapter: 10
level: "Débutant à avancé"
priority: "Obligatoire"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Chapitre 10 — Production, validation et publication

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## Objectif du chapitre

Ce chapitre définit le cycle officiel utilisé pour transformer une idée, une note, un exemple, un script ou un workflow en contenu publiable dans le guide **Guide-IA-GameDev**.

Le processus couvre cinq dimensions :

1. la préparation du contenu ;
2. sa production ;
3. sa validation ;
4. sa publication ;
5. sa maintenance.

Ces règles s’appliquent aux fichiers Markdown, aux scripts, aux configurations, aux workflows ComfyUI, aux exemples Godot et Blender, aux bases de données, aux tests, aux images, aux fichiers audio et aux livrables générés.

> **Priorité : Obligatoire** — Aucun contenu ne doit être considéré comme terminé tant qu’il n’a pas franchi les étapes de validation adaptées à sa nature.

## 1. Le cycle de vie officiel

Chaque élément produit suit le cycle suivant :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Idée
  ↓
Brouillon
  ↓
Prototype
  ↓
Relecture
  ↓
Validation technique
  ↓
Validation éditoriale
  ↓
Intégration
  ↓
Publication
  ↓
Maintenance
```

Les statuts autorisés sont :

| Statut | Signification |
|---|---|
| `planned` | Élément prévu mais non commencé. |
| `draft` | Première version en cours de rédaction. |
| `in-progress` | Production active avec contenu déjà exploitable. |
| `review` | Élément soumis à relecture. |
| `validated` | Élément vérifié et accepté. |
| `published` | Élément inclus dans une publication officielle. |
| `deprecated` | Élément conservé pour compatibilité mais remplacé. |
| `archived` | Élément retiré du parcours courant. |

Un fichier ne doit jamais passer directement de `draft` à `published` sans validation intermédiaire.

## 2. Définition de « terminé »

Un chapitre n’est terminé que si les conditions suivantes sont réunies :

- son objectif est explicite ;
- ses prérequis sont indiqués ;
- toutes les commandes sont complètes ;
- tous les chemins de fichiers sont cohérents ;
- les exemples ont un résultat attendu ;
- les risques sont signalés ;
- les variantes Solo et Studio sont précisées quand elles sont pertinentes ;
- les éléments Obligatoires, Recommandés et Optionnels sont distingués ;
- les références internes fonctionnent ;
- les informations dépendantes d’une version sont identifiées ;
- les licences et sources sont traçables ;
- la compilation Pandoc fonctionne ;
- la checklist de validation est satisfaite.

La présence d’un texte long ne constitue pas une preuve de complétude. Un contenu est terminé lorsqu’un lecteur peut l’utiliser, le vérifier et le reproduire.

## 3. Préparation d’un nouveau contenu

Avant la rédaction, l’auteur doit créer une fiche de préparation minimale.

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
id: DOC-L1-CH01
title: "Préparer Windows et les pilotes AMD"
objective: "Obtenir une plateforme stable pour les outils IA locaux"
audience:
  - beginner
  - intermediate
prerequisites:
  - Windows installé
  - droits administrateur
outputs:
  - pilotes validés
  - rapport de diagnostic
risks:
  - incompatibilité de pilote
  - redémarrage requis
validation:
  - version du pilote enregistrée
  - test GPU réussi
```

Cette fiche peut être intégrée au front matter du chapitre ou conservée dans un document de planification associé.

## 4. Rédaction par incréments

Les chapitres longs doivent être produits par incréments cohérents.

Un incrément doit apporter une valeur vérifiable, par exemple :

- une procédure complète ;
- une architecture documentée ;
- un exemple fonctionnel ;
- une checklist utilisable ;
- une matrice de décision ;
- un script testé ;
- une section de dépannage.

Les incréments ne doivent pas laisser :

- une commande coupée ;
- un exemple sans résultat ;
- un lien vers un fichier inexistant ;
- une section marquée « à compléter » dans une version publiée ;
- une dépendance non documentée.

## 5. Production des exemples techniques

### 5.1 Principe général

Chaque exemple technique doit comporter :

1. un contexte ;
2. un objectif ;
3. les prérequis ;
4. les fichiers concernés ;
5. les commandes ou le code ;
6. le résultat attendu ;
7. une méthode de vérification ;
8. une procédure de retour arrière si l’opération modifie le système.

### 5.2 Scripts

Un script destiné au Companion Pack doit :

- être exécutable sans modification cachée ;
- accepter des paramètres explicites ;
- vérifier ses prérequis ;
- retourner un code de sortie cohérent ;
- journaliser les erreurs utiles ;
- proposer un mode de simulation quand une action destructive est possible ;
- éviter les secrets en dur ;
- être accompagné d’un exemple d’utilisation.

### 5.3 Projets Godot

Un exemple Godot doit préciser :

- la version majeure et mineure testée ;
- le renderer utilisé ;
- les paramètres de projet non standards ;
- la scène de démarrage ;
- les entrées définies dans l’Input Map ;
- les dépendances et addons ;
- la méthode de lancement ;
- le comportement attendu.

### 5.4 Workflows ComfyUI

Un workflow ComfyUI doit conserver :

- le fichier JSON du workflow ;
- la liste des modèles ;
- la liste des nœuds personnalisés ;
- les versions ou commits testés ;
- les paramètres significatifs ;
- les seeds des exemples reproductibles ;
- les besoins VRAM ;
- une image de résultat autorisée à la redistribution ;
- une variante allégée quand le workflow dépasse la cible de 12 Go de VRAM.

### 5.5 Contenus Blender

Un exemple Blender doit indiquer :

- la version testée ;
- le moteur de rendu ;
- les unités ;
- l’espace colorimétrique ;
- les addons utilisés ;
- la structure des collections ;
- les paramètres d’export ;
- la procédure d’import dans Godot quand elle est concernée.

## 6. Validation éditoriale

La validation éditoriale vérifie :

- la clarté du titre ;
- la cohérence des niveaux de titres ;
- la progression pédagogique ;
- l’absence de jargon non expliqué ;
- la cohérence des termes avec le glossaire ;
- la présence de transitions utiles ;
- la lisibilité des listes et tableaux ;
- la qualité des légendes ;
- la distinction entre faits, recommandations et choix de projet ;
- la neutralité des comparaisons ;
- l’absence de promesses impossibles à vérifier.

Une relecture éditoriale ne doit pas modifier silencieusement le sens technique. En cas de doute, la correction est soumise à une nouvelle validation technique.

## 7. Validation technique

La validation technique dépend du type de contenu.

### 7.1 Commandes et installations

Les vérifications minimales sont :

- commande copiée depuis le document ;
- exécution dans l’environnement annoncé ;
- sortie enregistrée ;
- redémarrage testé si nécessaire ;
- désinstallation ou retour arrière documenté ;
- comportement en cas d’erreur connu.

### 7.2 Code

Le code doit être :

- syntaxiquement valide ;
- exécuté ou compilé ;
- testé sur un cas nominal ;
- testé sur au moins un cas d’erreur ;
- conforme aux conventions du langage ;
- dépourvu de secret ou de donnée personnelle ;
- accompagné de sa licence quand il provient d’une source externe.

### 7.3 Données et schémas

Les fichiers JSON, YAML, CSV et SQL doivent être validés avec un outil adapté. Les schémas doivent préciser :

- les champs obligatoires ;
- les types ;
- les valeurs par défaut ;
- les contraintes ;
- les règles de migration ;
- la compatibilité avec les versions précédentes.

### 7.4 Performances

Toute affirmation de performance doit préciser :

- le matériel ;
- le système ;
- les versions ;
- les paramètres ;
- la taille de l’échantillon ;
- l’unité mesurée ;
- la méthode de mesure ;
- la marge de variation observée.

Une impression subjective ne doit pas être présentée comme un benchmark.

## 8. Validation juridique et des licences

Avant publication, il faut vérifier :

- la licence des logiciels cités ;
- la licence des modèles IA ;
- les conditions de redistribution des poids ;
- les licences des images, sons, polices et textures ;
- les obligations d’attribution ;
- les limitations commerciales ;
- les données personnelles ou sensibles ;
- les marques et logos utilisés ;
- les conditions d’utilisation des contenus générés.

Les fichiers externes ne doivent pas être copiés dans le Companion Pack quand leur licence interdit la redistribution. Le guide doit alors fournir une procédure d’acquisition officielle.

## 9. Validation de sécurité

La revue de sécurité vérifie notamment :

- l’absence de mot de passe ou token dans le dépôt ;
- l’absence de commande destructive non signalée ;
- la limitation des permissions Docker ;
- la validation des fichiers téléchargés ;
- l’exposition réseau des services ;
- la protection des interfaces d’administration ;
- le traitement des données personnelles ;
- la provenance des modèles et extensions ;
- les scripts exécutés avec des droits administrateur.

Les commandes potentiellement destructrices doivent être précédées d’un avertissement explicite et d’une méthode de sauvegarde.

## 10. Validation documentaire automatisée

Le projet doit progressivement automatiser les contrôles suivants :

- liens Markdown cassés ;
- identifiants en double ;
- fichiers absents de `contents.txt` ;
- métadonnées YAML invalides ;
- blocs de code sans langage ;
- lignes anormalement longues ;
- chemins vers des ressources inexistantes ;
- images sans texte alternatif ;
- références à des versions non enregistrées ;
- erreurs de compilation Pandoc.

Exemple de pipeline :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Markdown lint
  ↓
Validation YAML
  ↓
Contrôle des liens
  ↓
Contrôle des identifiants
  ↓
Compilation HTML
  ↓
Compilation PDF
  ↓
Tests des exemples
  ↓
Rapport de validation
```

## 11. Revue Solo et revue Studio

### Mode Solo

En Mode Solo, une même personne peut assurer plusieurs rôles, mais doit séparer les étapes dans le temps :

1. rédaction ;
2. pause ;
3. relecture éditoriale ;
4. test technique dans un environnement propre ;
5. compilation ;
6. publication.

La checklist sert de seconde mémoire et réduit les oublis.

### Mode Studio

En Mode Studio, les responsabilités recommandées sont :

| Rôle | Responsabilité principale |
|---|---|
| Auteur | Produit le contenu. |
| Référent technique | Valide les procédures et exemples. |
| Relecteur éditorial | Vérifie la pédagogie et la cohérence. |
| Responsable QA | Exécute les contrôles et tests. |
| Responsable publication | Prépare la version et les livrables. |
| Responsable licences | Vérifie les droits et attributions. |

Une personne peut cumuler plusieurs rôles, mais l’auteur ne doit pas être l’unique validateur d’un contenu critique.

## 12. Gestion des branches et des commits

Le dépôt utilise `main` comme branche stable de référence.

Pour les changements importants, le flux recommandé est :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
main
  └── docs/volume-0-chapter-10
         ├── commits de production
         ├── validation
         └── pull request
```

Les commits doivent être atomiques et descriptifs.

Exemples :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
docs(volume-0): add chapter 10 publication workflow
fix(build): handle spaces in contents paths
test(companion): add identifier validation cases
chore(release): prepare version 0.2.0
```

Un commit ne doit pas mélanger une réécriture éditoriale massive, une migration technique et une modification de build sans nécessité.

## 13. Préparation d’une publication

Une publication doit produire un ensemble identifiable et reproductible.

### 13.1 Contenu minimal d’une publication

- sources Markdown ;
- métadonnées ;
- ordre de compilation ;
- PDF par volume si disponible ;
- PDF complet si disponible ;
- version HTML si disponible ;
- Companion Pack correspondant ;
- changelog ;
- liste des licences ;
- empreintes des archives ;
- notes de version.

### 13.2 Numérotation

Le projet suit une version sémantique adaptée à la documentation :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
MAJEURE.MINEURE.CORRECTIF
```

- **MAJEURE** : changement structurel ou incompatibilité importante ;
- **MINEURE** : ajout de chapitres ou de fonctionnalités documentaires ;
- **CORRECTIF** : corrections sans modification majeure du parcours.

Les versions de travail peuvent utiliser :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
0.1.0-alpha.1
0.2.0-beta.1
1.0.0-rc.1
```

## 14. Notes de version

Chaque publication doit résumer :

- les nouveaux chapitres ;
- les modifications importantes ;
- les corrections ;
- les changements de compatibilité ;
- les migrations nécessaires ;
- les éléments dépréciés ;
- les problèmes connus ;
- les versions des outils principales ;
- les profils matériels testés.

Les notes de version doivent permettre au lecteur de déterminer rapidement s’il doit mettre à jour son environnement ou ses fichiers.

## 15. Publication PDF et HTML

### 15.1 PDF

Avant publication PDF :

- vérifier la table des matières ;
- vérifier les sauts de page ;
- vérifier les tableaux larges ;
- vérifier les blocs de code ;
- vérifier les caractères Unicode ;
- vérifier les liens ;
- vérifier la résolution des images ;
- vérifier les en-têtes et pieds de page ;
- contrôler la taille finale du fichier.

### 15.2 HTML

Avant publication HTML :

- vérifier la navigation ;
- vérifier les ancres ;
- vérifier les chemins relatifs ;
- vérifier l’affichage mobile ;
- vérifier l’accessibilité des images ;
- vérifier les blocs de code ;
- vérifier les liens externes ;
- vérifier que les fichiers privés ne sont pas copiés.

## 16. Publication du Companion Pack

Le Companion Pack doit être aligné sur la version du guide.

Une archive doit comporter :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Companion-Pack-0.2.0/
├── README.md
├── VERSION
├── LICENSES/
├── templates/
├── scripts/
├── workflows/
├── examples/
├── tests/
└── checksums.txt
```

Les fichiers volumineux, modèles IA et dépendances externes doivent être remplacés par :

- un manifeste ;
- une URL officielle ;
- une empreinte ;
- une procédure d’installation ;
- une indication de licence.

## 17. Publication progressive

Le guide peut être publié progressivement selon quatre niveaux :

| Niveau | Contenu |
|---|---|
| `Preview` | Brouillon public, incomplet et clairement signalé. |
| `Alpha` | Structure stable, contenu encore susceptible de changer. |
| `Beta` | Contenu presque complet, validation étendue en cours. |
| `Stable` | Version validée et destinée à un usage de référence. |

Le statut doit apparaître dans le README, les métadonnées et les notes de version.

## 18. Maintenance après publication

Après publication, chaque retour doit être classé :

- erreur factuelle ;
- procédure obsolète ;
- incompatibilité ;
- lien cassé ;
- problème de licence ;
- erreur de sécurité ;
- manque pédagogique ;
- amélioration ;
- demande de nouveau contenu.

Les erreurs de sécurité, de perte de données ou de licence sont prioritaires.

Chaque correction doit indiquer :

- la version affectée ;
- la gravité ;
- la solution ;
- les fichiers modifiés ;
- le besoin éventuel de migration.

## 19. Archivage

Une version publiée doit pouvoir être reconstruite ultérieurement.

Il faut conserver :

- le tag Git ;
- les sources ;
- les scripts de build ;
- les fichiers de verrouillage ;
- les métadonnées ;
- les manifests de modèles ;
- les résultats de validation ;
- les livrables ;
- les checksums ;
- les notes de version.

Un fichier généré sans source ni procédure de reconstruction ne constitue pas une archive suffisante.

## 20. Critères de blocage d’une publication

Une publication doit être bloquée si :

- une commande critique n’a pas été testée ;
- une dépendance obligatoire est introuvable ;
- un secret est présent dans le dépôt ;
- une licence est inconnue ;
- un lien indispensable est cassé ;
- la compilation échoue ;
- un chapitre obligatoire est absent ;
- une procédure peut détruire des données sans avertissement ;
- une affirmation majeure n’est pas vérifiable ;
- le Companion Pack ne correspond pas à la version annoncée.

## 21. Checklist de validation d’un chapitre

### Contenu

- [ ] L’objectif est explicite.
- [ ] Les prérequis sont listés.
- [ ] Les niveaux Obligatoire, Recommandé et Optionnel sont visibles.
- [ ] Les procédures sont complètes.
- [ ] Les résultats attendus sont décrits.
- [ ] Le dépannage couvre les erreurs principales.
- [ ] Les parcours Solo et Studio sont traités quand nécessaire.

### Technique

- [ ] Les commandes ont été exécutées.
- [ ] Le code a été testé.
- [ ] Les versions utilisées sont enregistrées.
- [ ] Les chemins et noms de fichiers sont exacts.
- [ ] Les données d’exemple sont redistribuables.
- [ ] Les performances annoncées sont mesurées.

### Documentation

- [ ] Le front matter YAML est valide.
- [ ] L’identifiant est unique.
- [ ] Les liens internes fonctionnent.
- [ ] Les images possèdent un texte alternatif.
- [ ] Le chapitre figure dans `contents.txt`.
- [ ] L’index du livre est à jour.
- [ ] La roadmap est à jour.

### Sécurité et licences

- [ ] Aucun secret n’est présent.
- [ ] Les commandes risquées sont signalées.
- [ ] Les licences sont identifiées.
- [ ] Les attributions sont présentes.
- [ ] Les données personnelles sont absentes ou protégées.

### Publication

- [ ] La compilation Markdown vers HTML réussit.
- [ ] La compilation Markdown vers PDF réussit.
- [ ] Le rendu des tableaux et blocs de code est vérifié.
- [ ] Le changelog est mis à jour.
- [ ] Le statut du chapitre est cohérent.

## Conclusion

La qualité du guide dépend moins de la quantité de texte produite que de la capacité à transformer chaque élément en ressource reproductible, testée, traçable et maintenable.

Le cycle de production impose donc une discipline simple : préparer, produire, vérifier, publier et maintenir. Cette discipline s’applique à tous les volumes et au Companion Pack, en Mode Solo comme en Mode Studio.

Le chapitre suivant organise les éléments de référence transversaux : glossaire, bibliographie, index et annexes documentaires.
