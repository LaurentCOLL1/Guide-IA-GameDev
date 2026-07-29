---
title: "Audit — Livre V, Fiche 17 : Patrons de gameplay"
id: "DOC-L5-QA-AUDIT-CH17"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 17
audit-date: "2026-07-29T10:21:00+02:00"
last-verified: "2026-07-29T10:21:00+02:00"
audit-level: "static-review"
document-format: "reference-cards"
protocol: "Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md"
---

# Audit — Fiche 17 : Patrons de gameplay

## 1. Décision

**Décision : accepté au niveau `static-review`, sans revendication runtime.**

La fiche respecte le profil spécialisé du Livre V : index express, cartes directement consultables, matrices de sélection, paragraphes courts, renvois vers les systèmes propriétaires et absence de tutoriel complet recopié.

Aucun patron n’est présenté comme solution universelle. Chaque variante avancée est liée à un besoin, une preuve minimale et un signal de retrait.

## 2. Périmètre du plan maître

Le plan maître demande :

- machines à états ;
- capacités ;
- inventaires ;
- quêtes ;
- simulations ;
- séparation entre données, règles et présentation ;
- extensibilité et tests ;
- variantes simples et avancées ;
- fiches, diagrammes, exemples et checklists ;
- validation par petit prototype.

La fiche couvre les neuf premiers éléments sous forme de treize cartes, trois matrices et six diagrammes compacts. La validation reste statique : aucun petit prototype Godot n’a été exécuté. Cette réserve est explicite dans le chapitre et dans la preuve QA.

## 3. Comparaison avec les chapitres voisins

### Fiche 16 — Patrons d’architecture

La fiche 16 possède les frontières, dépendances, services d’application, repositories, ports, adaptateurs, propriété d’état et coutures de test. La fiche 17 consomme ces contrats pour organiser les décisions de gameplay ; elle ne les redéfinit pas.

### Fiche 18 — Référence graphique et 3D

La fiche 18 possédera unités, axes, formats, PBR, UV, LOD, rigs, import et export. La fiche 17 ne définit aucun asset, matériau, animation, collision, rig ou budget graphique.

### Livre II — Systèmes propriétaires

Les règles complètes restent dans :

- chapitre 14 pour personnages et matérialisation ;
- chapitre 17 pour agents, buts, plans et ordonnancement ;
- chapitre 18 pour combat ;
- chapitre 19 pour compétences et effets ;
- chapitre 20 pour inventaire, équipement et provenance ;
- chapitre 22 pour horloge, monde vivant et simulation agrégée ;
- chapitre 25 pour faits, quêtes, objectifs et conséquences ;
- chapitre 27 pour tests et simulations.

La fiche indexe les patrons communs sans recopier leurs classes, services, sauvegardes ou procédures.

## 4. Forme documentaire

Mesures calculées sur le contenu final :

| Mesure | Valeur |
|---|---:|
| lignes | 442 |
| titres | 19 |
| cartes `<!-- l5:card -->` | 13 |
| matrices `<!-- l5:matrix -->` | 3 |
| liens Markdown | 57 |
| renvois vers les Livres I à IV | 33 |
| liens profonds vers les Livres I à IV | 4 |
| diagrammes compacts | 6 |
| blocs clôturés | 0 |
| titres dupliqués | 0 |

L’index express ouvre chaque carte ou matrice. Les identifiants `GP-00` à `GP-12` restent uniques.

## 5. Couverture des cartes

| Unité | Couverture |
|---|---|
| GP-00 | contrat : problème, autorité, données, état, temps, ordre, résultat et preuve |
| Matrice A | sélection par problème et source propriétaire |
| GP-01 | définitions, état runtime, règles, application, présentation et persistance |
| GP-02 | machine à états finie, gardes, transitions, refus et traces |
| Matrice B | variante simple ou avancée et porte de complexification |
| GP-03 | hiérarchie, régions parallèles, pile, priorité, utilité, planification et tableau noir |
| GP-04 | capacités, progression, charges, ciblage et effets composables |
| GP-05 | intention, commande, candidat, résultat, événement et feedback |
| GP-06 | instances, lots, conteneurs, équipement, propriété et provenance |
| GP-07 | faits, quêtes, objectifs, conséquences, connaissances et codex |
| GP-08 | horloge logique, ticks, échéances, budgets, résidus et rattrapage |
| GP-09 | niveaux actif, arrière-plan, dormant et matérialisation |
| GP-10 | préparation, revalidation, commit, compensation et diagnostic |
| GP-11 | extensibilité bornée, capacités et coutures de test |
| Matrice C | preuves, coûts et signaux de retrait |
| GP-12 | anti-patterns, diagnostics et dix portes d’acceptation |

## 6. Frontières d’autorité

La fiche conserve les décisions de `Project Asteria` :

- un agent propose une requête d’action ;
- le système propriétaire valide et applique ;
- une définition partagée reste immuable ;
- l’état runtime possède une identité et une révision ;
- l’interface, l’animation, le son et les VFX reflètent un résultat ;
- le temps autoritaire utilise des ticks logiques ;
- la matérialisation ne crée ni ne détruit implicitement l’entité métier ;
- un événement est publié après commit ;
- une action multi-systèmes prépare tous ses candidats avant mutation ;
- une sortie IA reste consultative.

## 7. Diagnostics et règle sémantique des erreurs

La section `GP-12` est qualifiée comme index de diagnostics par `<!-- qa:error-correction-index -->`. Elle renvoie explicitement vers les sections propriétaires contenant les exemples fautifs, corrections et différences détaillées.

Aucun faux cas pédagogique incomplet n’est introduit. Les lignes de diagnostic restent des entrées compactes symptôme → anti-pattern → vérification → correction minimale, conformément au protocole spécialisé du Livre V.

## 8. Validation documentaire légère

Workflow temporaire : `Temporary Livre V Chapter 17 Finalizer`.

Run final : `30438299611`.

Tête source : `514052ec945646c9d38345ffe2e8509f0468804b`.

Commandes exécutées sans PDF :

- `python tools/validate_chapters.py --root . --report dist/QA-CHAPTERS.md` ;
- `python tools/check_context_markers.py --check`.

Les deux validations ont réussi sur le lot final avant commit. Aucun workflow PDF, Pandoc, XeLaTeX, qpdf ou rendu visuel n’a été lancé.

## 9. Doublons, liens et repères

- aucun titre dupliqué ;
- aucun bloc clôturé à expliquer ;
- aucun paragraphe long recopié depuis les chapitres propriétaires ;
- ordre continu du Livre V maintenu dans `contents.txt` ;
- chemin canonique et identifiant `DOC-L5-CH17` conformes ;
- plus de six renvois vers les Livres I à IV ;
- plus de deux liens profonds vers des sous-sections ;
- aucune structure tutoriel interdite ;
- aucune commande sans repère, car la fiche ne contient aucune commande ou procédure ;
- aucune URL externe ou brute ;
- aucun PDF intermédiaire.

## 10. Exactitude technique et niveau de preuve

Les assertions techniques sont limitées aux contrats déjà consignés dans le dépôt. La fiche ne revendique pas :

- l’exécution de Godot Engine ou GDScript ;
- une machine à états matérialisée ;
- une scène ou un `Node` ;
- une compétence, un inventaire ou une quête fonctionnels ;
- une simulation écologique exécutée ;
- un addon, une base, un réseau ou un service IA ;
- une mesure de performance ou de mémoire ;
- une campagne multiplateforme ;
- une donnée utilisateur ou de production.

Le niveau reste `static-review`.

## 11. Intégrité

Empreinte SHA-256 du chapitre :

`7b389d684720dd2592d98e9270efb1be6fbe11e0cdba768372bf751973b8145a`

L’empreinte de cet audit est enregistrée dans la preuve finale.

## 12. Réserves

- aucun petit prototype Godot exécuté malgré le critère de validation futur du plan maître ;
- aucune fixture permanente du Companion Pack créée ;
- aucune machine à états, capacité, commande, conteneur, quête ou simulation matérialisée ;
- aucune vérification de performance, concurrence, mémoire, sauvegarde réelle ou multijoueur ;
- aucune approbation juridique organisationnelle ;
- aucun PDF produit ;
- licence globale et accessibilité avancée du PDF toujours ouvertes.

## 13. Critère d’acceptation

La fiche est acceptée parce qu’un lecteur peut :

1. choisir un patron à partir d’un problème observable ;
2. identifier l’autorité qui accepte la mutation ;
3. séparer définition, état runtime, règle et présentation ;
4. distinguer machine à états simple et variantes avancées ;
5. relier capacités, inventaires, quêtes et simulations à leurs chapitres propriétaires ;
6. distinguer commande, résultat et événement ;
7. reconnaître existence logique et matérialisation ;
8. associer les actions multi-systèmes à une préparation commune ;
9. choisir une preuve proportionnée ;
10. comprendre qu’aucun runtime n’a été exécuté.
