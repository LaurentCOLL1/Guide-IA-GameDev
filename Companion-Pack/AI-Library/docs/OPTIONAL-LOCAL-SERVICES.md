# Tests optionnels contre des services locaux

Ces tests sont manuels et hors de la qualification obligatoire.

## Conditions

- service explicitement démarré par l’opérateur ;
- modèle et licence vérifiés séparément ;
- URL limitée à la boucle locale ;
- aucune donnée sensible ;
- délai court ;
- arrêt du service après essai ;
- résultats enregistrés comme propres à la version testée.

## Exemples d’URL

- Ollama : `http://127.0.0.1:11434`
- llama.cpp server : `http://127.0.0.1:8080`
- LocalAI : `http://127.0.0.1:8080`

Une réussite avec un fournisseur ne qualifie pas les deux autres.
