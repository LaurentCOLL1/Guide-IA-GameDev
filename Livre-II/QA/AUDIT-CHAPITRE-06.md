---
title: "Audit post-création — Livre II, chapitre 6"
id: "DOC-L2-QA-AUDIT-CH06"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
chapter: 6
audit-date: "2026-07-19"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
recommended-reasoning: "GPT-5.6 Sol — Élevée"
decision: "accepted-with-runtime-and-pdf-reservations"
---

# Audit post-création — Chapitre 6

> **Chapitre audité :** `Livre-II/CHAPITRE-06-Entrees-controleurs-cameras-et-interactions.md`  
> **Version auditée :** `1.0.0`  
> **Moteur de référence :** Godot `4.7.1-stable`  
> **Décision :** accepté avec réserves runtime et PDF de fin de Livre  
> **Politique PDF :** aucune construction intermédiaire.

## 1. Périmètre

L’audit couvre :

- Input Map et actions nommées ;
- événements ponctuels et interrogation continue ;
- propagation `_input()` / interface / `_unhandled_input()` ;
- trame d’intention indépendante du périphérique ;
- clavier, souris et manette ;
- `CharacterBody3D` et `move_and_slide()` ;
- déplacement relatif à la caméra ;
- `Camera3D` et `SpringArm3D` ;
- capture de souris ;
- `RayCast3D` et `Area3D` ;
- remappage en mémoire ;
- accessibilité ;
- intégration au composition root du chapitre 5 ;
- profondeur pédagogique ;
- repères d’utilisation ;
- doublons et frontières de collection.

## 2. Contrôles quantitatifs

Résultats de la seconde lecture statique :

| Contrôle | Résultat |
|---|---:|
| lignes du chapitre | 1 446 |
| titres contrôlés | 81 |
| blocs clôturés | 17 |
| blocs avec repère explicite | 17 sur 17 |
| titres identiques | 0 |
| blocs significatifs identiques | 0 |
| paragraphes longs identiques | 0 |
| erreur bloquante ouverte | 0 |

## 3. Non-conformités détectées et corrigées

### L2-CH06-001 — Touches physiques dans le code métier

**Risque :** lier le gameplay à `KEY_E`, `KEY_W` ou un bouton précis.

**Correction :** création d’actions Input Map nommées et d’une classe centralisant leurs identifiants.

### L2-CH06-002 — Événements ponctuels traités comme états maintenus

**Risque :** répéter saut ou interaction plusieurs fois.

**Correction :** accumulation des demandes ponctuelles, copie dans `PlayerInputFrame`, puis remise à zéro après `sample()`.

### L2-CH06-003 — Interface et gameplay en concurrence

**Risque :** un clic sur un bouton déclenche aussi une interaction.

**Correction :** usage de `_unhandled_input()` pour le gameplay et explication de `set_input_as_handled()`.

### L2-CH06-004 — Formule souris identique à la manette

**Risque :** mouvement de caméra dépendant du nombre d’images ou de la fréquence des événements.

**Correction :** la souris fournit un delta accumulé non multiplié par `delta`; le stick fournit un état multiplié par une vitesse et `delta`.

### L2-CH06-005 — Diagonale plus rapide

**Risque :** addition manuelle de quatre directions sans limitation.

**Correction :** `Input.get_vector()` produit un vecteur limité à une longueur de `1.0` et applique une zone morte circulaire.

### L2-CH06-006 — Vitesse multipliée deux fois par `delta`

**Risque :** déplacement incorrect avec `CharacterBody3D`.

**Correction :** `velocity` reste une vitesse ; seules accélération et gravité sont multipliées par `delta` avant `move_and_slide()`.

### L2-CH06-007 — Caméra inclinant le mouvement verticalement

**Risque :** monter ou descendre lorsque la caméra regarde vers le ciel ou le sol.

**Correction :** suppression de la composante Y des axes avant et droite avant normalisation.

### L2-CH06-008 — Caméra traversant le décor

**Risque :** caméra enfant simple sans collision.

**Correction :** `SpringArm3D`, caméra enfant directe, marge et exclusion du corps joueur.

### L2-CH06-009 — Tangage non borné

**Risque :** retournement et désorientation.

**Correction :** séparation yaw/pitch et `clamp()` entre des limites exportées.

### L2-CH06-010 — RayCast non aligné sur la caméra

**Risque :** sélection différente du centre de visée.

**Correction :** `PlayerInteractor` devient un `Node3D` descendant de `Camera3D`; son rayon suit la caméra.

### L2-CH06-011 — Dépendances récupérées avec `get_node()`

**Risque :** erreur immédiate avant le diagnostic personnalisé.

**Correction :** `get_node_or_null()` puis `_validate_dependencies()` et désactivation du traitement en cas d’échec.

### L2-CH06-012 — Interaction par méthode libre

**Risque :** `has_method("interact")` accepte des signatures incompatibles.

**Correction :** composant typé `InteractionTarget` avec prompt, retour booléen et signal.

### L2-CH06-013 — Remappage supprimant toute voie de secours

**Risque :** bloquer le menu ou le joueur.

**Correction :** refus d’une liste vide, contrôle des conflits et exigence d’une annulation clavier/manette.

### L2-CH06-014 — Persistance anticipée

**Risque :** consommer le périmètre des données et sauvegardes.

**Correction :** le remappage reste en mémoire ; sérialisation et migration sont réservées aux chapitres 7 et 9.

### L2-CH06-015 — Accessibilité ajoutée trop tard

**Risque :** architecture incompatible avec inversion, bascule, zones mortes ou remappage.

**Correction :** exigences intégrées dès la définition des actions et des paramètres de caméra.

### L2-CH06-016 — Pause oubliée dans la trame

**Risque :** action déclarée mais sans consommateur explicite.

**Correction :** `pause_pressed` est capturé et le contrôleur émet `pause_requested` avant de traiter le gameplay.

### L2-CH06-017 — PDF reconstruit par habitude

**Risque :** contrevenir à la politique utilisateur.

**Correction :** aucun PDF n’est construit ; la porte Q7 reste différée à la fin du Livre II.

## 4. Vérification pédagogique

Les fonctions principales disposent d’explications de leurs paramètres, retours et effets :

- `validate_required_actions()` ;
- `is_idle()` ;
- `_unhandled_input(event)` ;
- `sample(delta)` ;
- `set_enabled(value)` ;
- `_accumulate_mouse_look(event)` ;
- `apply_input(frame, camera_basis, delta)` ;
- `apply_look(look_delta)` ;
- `_validate_dependencies()` ;
- `interact(actor)` ;
- `try_interact(actor)` ;
- `_refresh_target()` ;
- `replace_events(action, events)` ;
- les callbacks de proximité et de balise.

Les notions nouvelles sont définies avant usage :

- Input Map ;
- événement ponctuel ;
- interrogation continue ;
- trame d’intention ;
- zone morte ;
- drift ;
- `Basis` ;
- yaw et pitch ;
- spring arm ;
- raycast ;
- cible d’interaction ;
- remappage.

## 5. Vérification technique statique

Les références officielles Godot 4.7 ont été utilisées pour vérifier :

- `InputEvent` et sa propagation ;
- `InputMap` ;
- `Input.get_vector()` ;
- souris capturée et `InputEventMouseMotion.relative` ;
- contrôleurs SDL 3 sur les plateformes de bureau ;
- `CharacterBody3D.velocity` ;
- `move_and_slide()` dans `_physics_process()` ;
- `Camera3D` ;
- `SpringArm3D` ;
- `RayCast3D` ;
- `Area3D.body_entered`, `area_entered` et `monitoring`.

Points spécifiques relus :

- signes des axes avant/arrière ;
- absence de multiplication finale de `velocity` par `delta` ;
- ordre caméra puis moteur ;
- type `CollisionObject3D` pour l’exclusion du spring arm ;
- type `Node3D` de l’acteur ;
- cast du collider ;
- nettoyage des demandes ponctuelles ;
- distinction de la souris et du stick.

## 6. Frontières de collection

Le chapitre ne consomme pas :

- les capacités de personnage du chapitre 14 ;
- les formats de réglages du chapitre 7 ;
- leur persistance du chapitre 9 ;
- les animations du Livre III ;
- les tests complets du chapitre 27 ;
- le multijoueur du Livre IV.

Le chapitre 5 est réutilisé pour l’assemblage, sans réintroduire le registre ou le bus comme dépendances globales dans chaque script.

## 7. Portes de qualité

| Porte | Résultat |
|---|---|
| Q0 — intégrité | validée |
| Q1 — complétude pédagogique | validée |
| Q2 — cohérence de collection | validée |
| Q3 — vérification technique statique | validée |
| Q4 — outils et contextes | validée |
| Q5 — sécurité et licences | validée |
| Q6 — validation documentaire du chapitre | validée sans PDF |
| Q7 — publication PDF de fin de Livre | différée |

## 8. Réserves

- scènes et scripts non matérialisés dans le Starter Kit ;
- aucune exécution avec clavier, souris ou manette réelle ;
- sensations de déplacement et de caméra non évaluées ;
- couches et masques non testés dans une scène physique ;
- remappage non persisté ;
- PDF non construit avant la fin du Livre II.

## 9. Décision

Le chapitre 6 est **accepté avec réserves runtime et PDF de fin de Livre**.

Il peut être déclaré :

> **rédigé, repéré et audité au niveau documentaire et statique, sans construction PDF intermédiaire.**
