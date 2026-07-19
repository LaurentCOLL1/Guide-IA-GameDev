---
title: "Audit du Livre II — Chapitre 14"
id: "DOC-L2-QA-CH14"
status: "complete"
version: "1.0.0"
book: "Livre II"
chapter: 14
category: "quality-report"
audit-date: "2026-07-19"
audit-level: "static-review"
chapter-id: "DOC-L2-CH14"
chapter-version: "1.0.0"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du Livre II — Chapitre 14

> **Chapitre audité :** `Livre-II/CHAPITRE-14-Personnages.md`  
> **Niveau GPT-5.6 Sol annoncé :** Élevée  
> **Décision :** accepté après corrections, avec réserves runtime et PDF de fin de Livre.

## 1. Objet

L’audit vérifie que le premier système de gameplay du Livre II définit un personnage sans créer un objet universel couplé aux onze systèmes suivants.

Il contrôle notamment :

- l’identité stable indépendante du nom ;
- la séparation définition, état runtime et snapshot ;
- les statistiques dérivées ;
- la composition de scène ;
- la séparation corps, contrôleur, visuel et état ;
- l’apparition et la disparition ;
- le registre limité aux personnages actifs ;
- les événements typés ;
- la persistance sans nœuds ni caches ;
- les frontières avec les chapitres 15 à 19.

## 2. Porte d’audit distincte

Le premier commit du chapitre portait explicitement :

- `status: draft` ;
- `version: 0.9.0` ;
- `audit-status: pending` ;
- `audit-level: not-audited`.

Le chapitre n’a donc pas été déclaré audité avant la seconde lecture et la création du présent rapport.

La séquence appliquée est :

1. annonce du titre et du niveau GPT-5.6 Sol ;
2. rédaction du brouillon ;
3. audit de complétude et de périmètre ;
4. audit des repères d’utilisation ;
5. contrôle des doublons et seconde lecture ;
6. vérification technique contre les sources officielles ;
7. corrections ;
8. rapport d’audit et preuve YAML ;
9. déclaration finale du chapitre ;
10. gouvernance et workflows.

## 3. Complétude du périmètre

Les éléments enregistrés dans `CONTINUITE-PROJET.md` sont couverts :

- premier système de gameplay ;
- identité stable ;
- définition de conception ;
- état runtime ;
- persistance ;
- attributs et statistiques dérivées ;
- scène de personnage ;
- séparation personnage, contrôleur, visuel et corps ;
- réutilisation du chapitre 6 ;
- apparition et disparition ;
- registre actif limité ;
- événements typés ;
- section de sauvegarde ;
- frontières avec les systèmes futurs ;
- parcours Solo et Studio ;
- critères d’acceptation et tests à préparer.

Aucun système social, familial, autonome, de combat ou de compétences n’est implémenté dans l’état du personnage.

## 4. Corrections appliquées

### 4.1 Espaces d’identifiants distincts

Le brouillon utilisait initialement la forme `chr_...` pour les instances et les définitions.

Correction :

- les instances utilisent `CharacterId` et le préfixe `chr_` ;
- les définitions utilisent le `StableId` du chapitre 7, par exemple `character.definition.aster` ;
- `species_id` utilise également un `StableId`.

Cette séparation évite de confondre contenu de conception et entité de partie.

### 4.2 Validation renforcée des définitions

Les attributs exportés sont maintenant contrôlés entre `1` et `100`, y compris lorsque la ressource est chargée depuis un fichier modifié hors Inspector.

Le catalogue retourne un code `Error` et distingue :

- paramètre absent ;
- donnée invalide ;
- identifiant dupliqué ;
- succès.

### 4.3 Catalogue construit atomiquement

Le bootstrap construit un catalogue candidat. Il ne remplace le catalogue actif que lorsque toutes les définitions sont valides.

Une définition invalide ne laisse donc plus un catalogue partiellement rempli.

### 4.4 Bornes de l’état runtime

L’état valide désormais :

- la longueur du nom personnalisé ;
- les quatre bonus entre `-100` et `100` ;
- la cohérence de l’état de vie ;
- les limites de santé et d’endurance ;
- les coordonnées et le lacet finis.

### 4.5 Événements d’endurance complets

Le brouillon déclarait `stamina_changed` sans montrer les opérations qui l’émettent.

Les méthodes `spend_stamina()` et `restore_stamina()` ont été ajoutées au composant `CharacterRuntime`.

### 4.6 Cycle de vie des nœuds

Le spawner distingue désormais :

- `free()` pour une instance refusée avant son entrée dans l’arbre ;
- `queue_free()` pour une instance déjà ajoutée ;
- initialisation avant `add_child()` ;
- affectation de `global_transform` après `add_child()`.

`CharacterTransformSync` a aussi été ajouté à l’arbre de scène attendu.

### 4.7 Registre actif

La méthode `clear_without_freeing()` a été supprimée. Elle pouvait vider le registre tout en laissant des nœuds actifs, créant une divergence silencieuse.

Le registre conserve uniquement les opérations d’enregistrement, de retrait et de recherche.

### 4.8 Snapshot strict

Le décodeur refuse maintenant les conversions silencieuses :

- identifiants obligatoirement textuels ;
- santé, endurance et bonus obligatoirement entiers ;
- état de vie obligatoirement booléen ;
- coordonnées et lacet obligatoirement numériques ;
- définition validée avant résolution.

Le `StringName` de définition est explicitement converti en `String` lors de l’encodage JSON.

### 4.9 Capture de sauvegarde

La capture ne saute plus silencieusement un état absent ou invalide. Elle refuse la section et produit une erreur de diagnostic.

L’application reste précédée par une préparation complète dans un dictionnaire temporaire.

### 4.10 Nom personnalisé

Le bootstrap borne le nom personnalisé avant son insertion et valide de nouveau l’état après personnalisation.

## 5. Audit des repères d’utilisation

Les 55 blocs sont précédés d’un repère reconnu :

- `[VSC]` : 15 ;
- `[SORTIE]` : 3 ;
- `[LECTURE]` : 37 ;
- bloc non repéré : 0.

Les commandes terminal ne sont pas nécessaires dans ce chapitre. Les actions d’éditeur indiquent Godot et les chemins à créer.

## 6. Audit des erreurs et corrections

La section 26 porte le marqueur :

> **[LECTURE] Marqueur présent — Ne pas saisir.**

```html
<!-- qa:error-correction-section -->
```

Les seize sous-cas contiennent chacun :

- un symptôme ;
- un exemple fautif ;
- une correction ;
- un exemple corrigé ;
- une différence explicite.

Cas couverts :

1. nom affiché utilisé comme identité ;
2. `Resource` partagée modifiée ;
3. statistique dérivée sauvegardée comme autorité ;
4. lecture directe de `Input` ;
5. contrôleur confondu avec identité ;
6. index de tableau utilisé comme identité ;
7. initialisation après `add_child()` ;
8. transform global défini avant le parent ;
9. double instance active ;
10. disparition confondue avec suppression ;
11. nœud ou ressource placé dans le snapshot ;
12. application avant validation complète ;
13. registre transformé en Service Locator ;
14. relations placées dans l’état du personnage ;
15. identifiant traité comme autorisation ;
16. vitesse multipliée deux fois par `delta`.

## 7. Contrôle des doublons

Résultat de la seconde lecture :

- titre dupliqué : 0 ;
- bloc significatif dupliqué : 0 ;
- long paragraphe dupliqué : 0 ;
- section d’erreur incomplète : 0.

Les rappels du chapitre 6 sont limités aux frontières nécessaires ; le code complet d’entrée et de caméra n’est pas recopié.

## 8. Vérification technique

Les points suivants ont été relus contre la documentation Godot 4.7 :

- `CharacterBody3D` et `move_and_slide()` ;
- cycle de vie et ajout des `Node` ;
- transforms globaux de `Node3D` ;
- sérialisation et partage des `Resource` ;
- instanciation de `PackedScene` ;
- signaux personnalisés ;
- génération d’octets avec `Crypto` ;
- `PackedByteArray.hex_encode()` ;
- `StringName`, `Dictionary`, `Array`, `Vector3` et `Transform3D` ;
- `is_finite()`.

Les quinze références techniques du chapitre sont des liens Markdown nommés et cliquables.

## 9. Revue statique du code

Les extraits GDScript ont été relus pour :

- indentation et fermeture des blocs ;
- types et valeurs de retour ;
- références `null` ;
- ordre d’initialisation ;
- validation avant mutation ;
- tri déterministe ;
- absence de chemin provenant du snapshot ;
- absence de `Node` ou `Resource` dans le JSON ;
- bornage des valeurs ;
- absence de secret ;
- séparation des systèmes futurs.

Aucun parseur Godot ni projet matérialisé n’a été exécuté.

## 10. Cohérence avec les chapitres voisins

### 10.1 Chapitre 6

Le chapitre réutilise la chaîne :

`PlayerInputReader → PlayerInputFrame → PlayerController → corps`

Il ne replace pas les touches ou `Input` dans le personnage.

### 10.2 Chapitre 7

Les définitions utilisent :

- `Resource` ;
- `StableId` ;
- catalogue validé ;
- séparation définition/état.

### 10.3 Chapitre 9

La persistance conserve :

- capture ;
- validation ;
- préparation ;
- application après validation globale ;
- absence de cache dérivé dans l’autorité.

### 10.4 Chapitre 13

L’identifiant localise un personnage mais ne vaut jamais autorisation.

### 10.5 Chapitre 15

Les relations sociales restent dans un état et une section de sauvegarde séparés, reliés par les identifiants stables des personnages.

## 11. Parcours Solo et Studio

Le parcours Solo reste exploitable avec :

- catalogue explicite ;
- dictionnaire d’états ;
- scène de joueur ;
- registre actif injecté ;
- section de sauvegarde ;
- personnages hors scène conservés sans nœud.

Le parcours Studio ajoute gouvernance des schémas, validation de contenu, budgets d’instances, streaming de zones et compatibilité des anciennes sauvegardes.

## 12. Réserves runtime

Ne sont pas revendiqués :

- analyse GDScript par Godot 4.7.1 ;
- création des scènes dans l’éditeur ;
- génération d’identifiants sur les exports ;
- instanciation réelle de `PackedScene` ;
- ordre runtime des callbacks dans le Starter Kit ;
- déplacement et collisions ;
- connexion du contrôleur du chapitre 6 ;
- apparition, disparition et streaming ;
- capture de transform avec interpolation ;
- intégration réelle au système de sauvegarde ;
- migrations de snapshots ;
- performances et budgets ;
- packaging ;
- PDF du Livre II.

## 13. Décision

Le chapitre 14 est accepté au niveau `static-review` après application des corrections recensées.

La preuve finale est enregistrée dans :

`Livre-II/QA/VALIDATION-FINALE-CHAPITRE-14.yaml`.

Le chapitre ne deviendra `runtime-tested` qu’après matérialisation des scripts et scènes dans Godot, exécution des parcours et conservation des journaux correspondants.
