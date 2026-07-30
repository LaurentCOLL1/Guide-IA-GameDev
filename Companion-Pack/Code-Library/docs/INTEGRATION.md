# Intégration

## Python

Ajoutez `Companion-Pack/Code-Library/python/src` au `PYTHONPATH`, puis importez depuis `asteria_code`.

## Godot

Copiez le dossier `godot/addons/asteria_code` dans le projet cible ou ajoutez-le comme sous-arbre versionné. Les scripts n’utilisent aucun autoload et ne modifient aucun réglage de projet.

## Choix progressif

Adoptez un composant à la fois. Un projet peut utiliser la validation sans utiliser le repository, ou la machine à états sans le registre de services. Les dépendances entre composants sont limitées et déclarées dans `catalog.json`.
