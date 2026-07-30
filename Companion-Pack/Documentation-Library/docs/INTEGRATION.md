# Intégration dans le dépôt

Le générateur écrit uniquement le chemin demandé. Il ne modifie ni index, ni roadmap, ni `contents.txt`.

Pour intégrer un document :

- choisir le propriétaire documentaire ;
- générer le brouillon dans une branche dédiée ;
- vérifier l’identifiant et les liens ;
- exécuter `tools/validate_chapters.py` lorsque le document rejoint le parcours lecteur ;
- compiler le document avec Pandoc ;
- joindre l’audit et la preuve QA adaptés ;
- mettre à jour la gouvernance seulement après validation.
