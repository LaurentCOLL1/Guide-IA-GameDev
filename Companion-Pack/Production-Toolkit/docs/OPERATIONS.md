# Guide d'exploitation

## Dry-run

Toute opération mutante expose `--dry-run`. Elle valide les entrées et imprime le plan sans créer de sortie métier, de checkpoint ou d'archive.

## Journaux et codes de sortie

Les commandes écrivent des événements JSON. Codes : `0` succès, `2` argument invalide, `3` validation refusée, `4` échec de tâche, `5` collision ou overwrite interdit.

## Préservation des sources

Une sortie ne peut pas être identique à sa source. L'écrasement est refusé par défaut. Le renommage copie vers un workspace et les campagnes comparent les SHA-256 avant et après.

## Reprise

Le pipeline écrit atomiquement un checkpoint après chaque tâche. Une reprise ignore les tâches terminées si l'empreinte du plan reste identique ; un plan modifié invalide le checkpoint.

## Blender et Godot

Blender importe un OBJ synthétique et exporte un GLB. Godot charge ce GLB comme `PackedScene`. Cette preuve ne qualifie ni matériaux complexes, ni animation, ni bake, ni export de jeu.

## Packaging

Les fichiers sont triés, les dates ZIP fixées à 1980-01-01 et les permissions normalisées. Deux builds identiques doivent avoir le même SHA-256.

## Extension

Toute nouvelle famille doit définir son dry-run, ses codes de sortie, sa politique d'overwrite, ses tests synthétiques, son nettoyage et sa preuve de préservation des sources.
