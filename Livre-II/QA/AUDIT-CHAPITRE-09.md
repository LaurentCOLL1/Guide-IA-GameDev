---
title: "Audit du Livre II — Chapitre 9"
id: "DOC-L2-QA-CH09"
status: "complete"
version: "1.1.0"
book: "Livre II"
chapter: 9
category: "quality-report"
audit-date: "2026-07-19"
audit-level: "static-review"
chapter-id: "DOC-L2-CH09"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du Livre II — Chapitre 9

> **Chapitre audité :** `Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md`  
> **Niveau GPT-5.6 Sol annoncé :** Élevée  
> **Décision :** accepté avec réserves runtime et PDF de fin de Livre.

## 1. Objet

L’audit vérifie que le chapitre définit un système de sauvegarde cohérent, versionné et récupérable sans confondre :

- données de conception ;
- configuration ;
- persistance relationnelle SQLite ;
- état runtime ;
- snapshot de partie ;
- fichier de sauvegarde.

## 2. Couverture du plan maître

| Exigence | Couverture |
|---|---|
| Rôle d’une sauvegarde face aux dépôts SQLite | Complet |
| Snapshot cohérent de partie | Complet |
| Slots manuels, autosaves et quicksaves | Complet |
| Métadonnées, miniatures et temps de jeu | Complet |
| Format versionné | Complet |
| Écriture temporaire et remplacement contrôlé | Complet |
| Validation avant application | Complet |
| Chargement en plusieurs phases | Complet |
| Compatibilité ascendante et migrations | Complet |
| Sauvegardes futures ou corrompues | Complet |
| Rotation, rétention et copies de secours | Complet |
| Séparation conception, SQLite et snapshot | Complet |
| Parcours Solo et Studio | Complet |

## 3. Sources officielles vérifiées

La revue statique s’appuie sur :

- [Godot 4.7 — Saving games](https://docs.godotengine.org/en/4.7/tutorials/io/saving_games.html) ;
- [Godot 4.7 — FileAccess](https://docs.godotengine.org/en/4.7/classes/class_fileaccess.html) ;
- [Godot 4.7 — DirAccess](https://docs.godotengine.org/en/4.7/classes/class_diraccess.html) ;
- [Godot 4.7 — JSON](https://docs.godotengine.org/en/4.7/classes/class_json.html) ;
- [Godot 4.7 — HashingContext](https://docs.godotengine.org/en/4.7/classes/class_hashingcontext.html) ;
- [Godot 4.7 — Runtime file loading and saving](https://docs.godotengine.org/en/4.7/tutorials/io/runtime_file_loading_and_saving.html) ;
- [Godot 4.7 — Resources](https://docs.godotengine.org/en/4.7/tutorials/scripting/resources.html) ;
- [Godot 4.7 — ResourceSaver](https://docs.godotengine.org/en/4.7/classes/class_resourcesaver.html).

## 4. Vérifications techniques

### 4.1 JSON et précision numérique

La documentation Godot précise que JSON utilise un type numérique commun. Le chapitre normalise donc les `int` et `float` avant calcul de l’empreinte.

`JSON.stringify()` utilise :

- le tri des clés ;
- la précision complète ;
- une indentation lisible pour le fichier final.

Les entiers qui exigent une précision exacte sont limités à la plage sûre de 53 bits.

### 4.2 Types Godot

`Vector3` est converti explicitement vers un dictionnaire `{x, y, z}`.

La reconstruction vérifie :

- la présence des trois composantes ;
- leur type numérique ;
- l’absence de `NaN` et d’infini.

### 4.3 Intégrité

L’empreinte SHA-256 porte sur une représentation canonique du payload.

L’audit vérifie que :

- les clés sont textuelles et triées ;
- `String` et `StringName` sont normalisés ;
- les doublons après normalisation sont refusés ;
- les objets et ressources sont refusés ;
- l’empreinte est vérifiée avant migration ;
- elle est recalculée sur la copie migrée.

L’empreinte n’est jamais présentée comme un chiffrement ou une protection absolue contre la triche.

### 4.4 Écriture et remplacement

La documentation Godot indique que `DirAccess.rename_absolute()` peut écraser une destination accessible. Elle ne promet pas une atomicité identique sur toutes les plateformes.

Le chapitre utilise donc le terme **remplacement contrôlé**.

La séquence relue est :

1. écrire dans `.tmp` ;
2. appeler `flush()` ;
3. fermer ;
4. relire ;
5. parser ;
6. vérifier l’empreinte ;
7. conserver une copie `.bak` seulement si l’ancien principal est valide ;
8. renommer le temporaire vers la cible.

### 4.5 Fichier futur

Une sauvegarde dont `format_version` dépasse la version courante :

- est refusée avant mutation ;
- n’est pas remplacée par son `.bak` ;
- n’est pas écrasée par un ancien build ;
- reste disponible pour diagnostic.

### 4.6 Fichier corrompu

Un principal corrompu ne remplace pas une copie `.bak` encore valide.

Le système peut charger la copie de secours en mémoire, mais ne réécrit pas automatiquement le principal corrompu.

### 4.7 Limites

Le lecteur applique une limite initiale de 16 Mio avant parsing.

La section des balises limite également le nombre d’entrées et vérifie :

- identifiants stables ;
- doublons ;
- booléens ;
- compteurs entiers non négatifs ;
- nombres finis et non négatifs.

### 4.8 Chargement en plusieurs phases

Le chapitre impose :

- lecture ;
- validation d’enveloppe ;
- refus des versions futures ;
- migration d’une copie ;
- validation du format courant ;
- validation des sections ;
- préparation du monde cible ;
- application ;
- bascule ;
- libération de l’ancien monde.

Le verrou de chargement reste actif jusqu’à `finish_apply()` ou `cancel_load()`.

### 4.9 Sections

Le registre vérifie :

- les sections obligatoires absentes ;
- les types des sections ;
- les sections inconnues dans le mode strict ;
- les clés non textuelles.

### 4.10 Correspondance du slot

Le coordinateur vérifie que l’identifiant contenu dans le document correspond au slot demandé.

Un fichier déplacé sous un autre nom ne peut donc pas être chargé silencieusement comme ce nouveau slot.

## 5. Non-conformités détectées et corrigées

| N° | Risque initial | Correction |
|---:|---|---|
| 1 | Assimiler SQLite à un slot | Snapshot logique distinct |
| 2 | Sérialiser des objets complets | Dictionnaires simples et codecs explicites |
| 3 | Utiliser un nom libre comme chemin | `SaveSlotId` validé |
| 4 | Hash différent après cycle JSON | Normalisation commune des nombres |
| 5 | Perte de précision des flottants | `full_precision = true` |
| 6 | Collision `String` / `StringName` | Normalisation et refus des doublons |
| 7 | Entier JSON imprécis | Limite exacte de 53 bits |
| 8 | Valeur vectorielle non finie | Rejet de `NaN` et de l’infini |
| 9 | Fichier géant parsé sans limite | Limite de 16 Mio |
| 10 | Écriture directe de la cible | `.tmp`, relecture et validation |
| 11 | Promesse d’atomicité universelle | Terme « remplacement contrôlé » |
| 12 | Principal corrompu copié vers `.bak` | Conserver le `.bak` existant |
| 13 | Sauvegarde future remplacée par `.bak` | Refus immédiat |
| 14 | Sauvegarde future écrasée | Écriture refusée |
| 15 | Fichier déplacé vers un autre slot | Comparaison slot demandé / slot contenu |
| 16 | Section inconnue ignorée en mode strict | Diagnostic et refus |
| 17 | Verrou libéré avant application | Verrou jusqu’à fin ou annulation |
| 18 | Migration réécrite | Chaîne append-only `N` vers `N + 1` |
| 19 | Hash comparé après transformation | Vérification avant, recalcul après |
| 20 | Application partielle présentée comme sûre | Réserve transactionnelle explicite |

## 6. Règle sémantique des erreurs

La section `Erreurs fréquentes, pièges et corrections` porte :

> **[LECTURE] Marqueur QA — Ne pas saisir.**

```html
<!-- qa:error-correction-section -->
```

Elle contient douze cas. Chaque cas fournit :

- un symptôme ;
- un exemple fautif ;
- une correction ;
- un exemple corrigé ou équivalent sémantique ;
- une différence explicite.

## 7. Repères d’utilisation

Les blocs sont qualifiés par :

- `[VSC]` pour les fichiers à créer ;
- `[LECTURE]` pour les exemples non exécutables ;
- `[SORTIE]` lorsqu’un résultat est fourni ;
- `[APP]`, `[PS]` ou `[WEB]` uniquement lorsque l’action correspondante existe.

Aucune commande de terminal n’est présentée comme du code GDScript à copier.

## 8. Frontières avec les chapitres voisins

### Chapitre 7

Le chapitre 9 réutilise la validation JSON et les identifiants stables sans redéfinir les données de conception.

### Chapitre 8

Les repositories SQLite contribuent au snapshot. Le fichier SQLite n’est pas traité comme le slot complet.

### Chapitre 10

La mémoire vectorielle ne devient ni une sauvegarde, ni une source d’autorité pour la reconstruction du monde.

### Chapitre 27

Les fixtures, coupures simulées, matrices de compatibilité et tests de migrations seront industrialisés au chapitre 27.

### Chapitre 28

La journalisation générale des opérations, durées et diagnostics sera centralisée au chapitre 28.

## 9. Réserves runtime

Ne sont pas encore exécutés :

- écriture réelle dans `user://saves/` sous Windows 11 ;
- comportement de `rename_absolute()` sur NTFS ;
- panne entre chaque étape ;
- disque plein ;
- remplacement inaccessible ;
- récupération `.bak` ;
- rotation des autosaves ;
- migration V1 vers V2 ;
- limite de taille ;
- restauration transactionnelle de plusieurs records ;
- monde temporaire et bascule ;
- génération de miniature ;
- export Windows sur machine propre.

## 10. PDF

Conformément à la politique utilisateur :

- aucun PDF intermédiaire n’est construit ;
- la compilation et l’inspection sont différées jusqu’à la fin du Livre II.

## 11. Décision

**Accepté avec réserves runtime et PDF de fin de Livre.**

Le chapitre peut être déclaré **rédigé, repéré et audité au niveau `static-review`** après réussite des workflows légers :

- `Validate Chapters Without PDF` ;
- `Validate Usage Contexts`.
