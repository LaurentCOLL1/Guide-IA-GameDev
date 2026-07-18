---
title: "Audit post-création — Livre II, chapitre 5"
id: "DOC-L2-QA-AUDIT-CH05"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
chapter: 5
audit-date: "2026-07-19"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
recommended-reasoning: "GPT-5.6 Sol — Élevée"
decision: "accepted-with-runtime-reservation"
---

# Audit post-création — Chapitre 5

> **Chapitre audité :** `Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md`  
> **Version auditée :** `1.0.0`  
> **Moteur de référence :** Godot `4.7.1-stable`  
> **Décision :** accepté avec réserve runtime  
> **Politique PDF :** aucune construction PDF pour ce chapitre ; publication différée à la fin du Livre II.

## 1. Périmètre de l’audit

L’audit couvre :

- la distinction service, gestionnaire, système, contrôleur et repository ;
- le choix entre `Node`, `RefCounted`, `Resource` et Autoload ;
- l’injection par constructeur, méthode et propriété exportée ;
- le registre de services ;
- le bus d’événements typé ;
- le cycle de vie et l’ordre d’arrêt ;
- le point de composition `AppBootstrap` ;
- l’exercice `beacons` ;
- la profondeur des explications de code ;
- les repères d’utilisation ;
- les doublons ;
- les frontières avec les chapitres voisins ;
- la nouvelle politique de génération PDF.

## 2. Contrôles quantitatifs

Résultats de la seconde lecture statique :

| Contrôle | Résultat |
|---|---:|
| lignes du chapitre | 1 152 |
| titres contrôlés | 78 |
| blocs clôturés | 18 |
| blocs avec repère explicite | 18 sur 18 |
| titres identiques | 0 |
| blocs significatifs identiques | 0 |
| paragraphes longs identiques | 0 |
| erreur bloquante ouverte | 0 |

Les rappels de `signal`, `Callable`, `RefCounted` et `Resource` sont limités au contexte des services. Les explications complètes des chapitres 2 à 4 ne sont pas recopiées.

## 3. Non-conformités détectées et corrigées

### L2-CH05-001 — Terminologie trop vague

**Risque :** employer `Manager` pour toute responsabilité.

**Correction :** ajout d’une grille distinguant service, manager, système, contrôleur et repository, avec critères et exemples.

### L2-CH05-002 — Dépendances globales cachées

**Risque :** présenter un accès `GlobalServices.service` comme méthode principale.

**Correction :** l’exemple est classé comme anti-pattern ; les dépendances sont injectées explicitement.

### L2-CH05-003 — Autoload présenté comme vrai singleton

**Risque :** laisser croire qu’un Autoload ne peut exister qu’une fois.

**Correction :** le chapitre reprend la nuance officielle : l’Autoload se comporte comme un singleton, mais son script peut être instancié ailleurs.

### L2-CH05-004 — Collision de nom entre classe globale et Autoload

**Risque :** utiliser `AppBootstrap` comme `class_name` et comme nom d’Autoload.

**Correction :** le script conserve la classe `AppBootstrap`, mais l’entrée Autoload est nommée `AppRuntime`.

### L2-CH05-005 — Bus générique non typé

**Risque :** utiliser un signal `event(name, data)` et perdre types, autocomplétion et traçabilité.

**Correction :** création de signaux précis avec paramètres typés.

### L2-CH05-006 — Double connexion

**Risque :** connecter plusieurs fois le même `Callable`.

**Correction :** ajout de `is_connected()` avant `connect()` et `disconnect()`.

### L2-CH05-007 — Registre transformé en Service Locator

**Risque :** injecter le registre dans tous les modules.

**Correction :** usage limité au point de composition ; les modules reçoivent le service concret.

### L2-CH05-008 — Démarrage partiellement initialisé

**Risque :** laisser le bus ou une entrée de registre après l’échec d’un enregistrement.

**Correction :** nettoyage immédiat des objets et enregistrements partiels avant le retour d’erreur.

### L2-CH05-009 — Arrêt dans le mauvais ordre

**Risque :** détruire le bus avant les services qui l’utilisent.

**Correction :** arrêt documenté dans l’ordre inverse du démarrage.

### L2-CH05-010 — Signature de `StatusBeacon` incorrecte

**Risque :** appeler `activate()` sans son paramètre et écouter `activated` sans ses deux arguments.

**Correction :** l’exercice appelle `activate(&"Chapter05Service")` et reçoit `beacon_id` et `message`.

### L2-CH05-011 — Resource mutable utilisée comme service

**Risque :** confondre données partagées et service runtime.

**Correction :** séparation explicite entre `Resource` de configuration et objets de service.

### L2-CH05-012 — Preuve runtime revendiquée trop tôt

**Risque :** déclarer les exemples exécutés alors que le Starter Kit n’est pas matérialisé.

**Correction :** niveau maintenu à `static-review`, avec procédure de test future.

### L2-CH05-013 — Construction PDF par chapitre contraire à la décision utilisateur

**Risque :** ralentir chaque lot et produire des preuves auto-référentielles inutiles.

**Correction :** la compilation et l’inspection PDF sont différées à la fin de chaque Livre, puis à la fin de la collection. Une exception reste possible pour une modification directe de la chaîne de publication.

## 4. Vérification pédagogique

Les fonctions suivantes disposent d’explications détaillées de leurs paramètres, retours et effets :

- `_init(events)` ;
- `configure(activation_service)` ;
- `request_activation(beacon_id)` ;
- `register_service(service_id, service)` ;
- `require_service(service_id)` ;
- `start_application()` ;
- `stop_application()` ;
- `create_chapter_05_demo()` ;
- les callbacks de la scène de démonstration.

Les notions suivantes sont définies avant leur usage :

- injection de dépendances ;
- composition root ;
- Autoload ;
- Service Locator ;
- bus d’événements ;
- événement, commande et état ;
- idempotence ;
- Null Object ;
- ordre de démarrage et d’arrêt.

## 5. Vérification technique statique

Sources principales vérifiées :

- documentation officielle Godot 4.7.1 ;
- Autoloads ;
- signaux et `Signal.connect()` ;
- `RefCounted` ;
- `Node` et `_exit_tree()` ;
- `Object`, `is_instance_valid()` et `queue_free()` ;
- Resources et cache ;
- organisation des scènes et injection de dépendances.

Points relus :

- types des paramètres ;
- valeurs de retour `bool`, `Error`, `Object` et types personnalisés ;
- utilisation de `StringName` ;
- dictionnaire typé ;
- ordre de création et de nettoyage ;
- compatibilité des callbacks avec les signaux du chapitre 3 ;
- distinction entre enfant supprimable et nœud Autoload non supprimable.

## 6. Frontières de collection

Le chapitre ne consomme pas prématurément :

- les contrôleurs et entrées du chapitre 6 ;
- les catalogues et formats du chapitre 7 ;
- SQLite du chapitre 8 ;
- la sauvegarde du chapitre 9 ;
- les communications IA des chapitres 11 à 13 ;
- le framework de tests du chapitre 27 ;
- l’observabilité du chapitre 28.

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

- les scripts et scènes ne sont pas encore matérialisés dans le Starter Kit ;
- la commande headless n’a pas été exécutée sur la station de référence ;
- le cycle complet Autoload/démarrage/arrêt reste à tester dans Godot ;
- le PDF sera construit et inspecté à la fin du Livre II.

## 9. Décision

Le chapitre 5 est **accepté avec réserve runtime**.

Il peut être déclaré :

> **rédigé, repéré et audité au niveau documentaire et statique, sans construction PDF intermédiaire.**
