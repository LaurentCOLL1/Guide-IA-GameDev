# Contribuer au Guide IA GameDev

Merci de contribuer à ce projet documentaire.

## Principes

Toute contribution doit :

- respecter `STYLE_GUIDE.md` ;
- préserver la compatibilité Markdown/Pandoc ;
- privilégier les outils gratuits, locaux et open source dans le pipeline principal ;
- signaler clairement les composants uniquement gratuits, propriétaires ou soumis à des restrictions de licence ;
- inclure des sources primaires pour les informations techniques susceptibles d'évoluer ;
- ne contenir aucun secret, modèle propriétaire redistribué sans autorisation ou ressource sans licence vérifiable.

## Flux de contribution recommandé

1. Créer une branche depuis `main`.
2. Limiter chaque branche à un sujet cohérent.
3. Mettre à jour les fichiers Markdown concernés.
4. Construire localement la documentation.
5. Vérifier les liens, le code et les références croisées.
6. Ouvrir une pull request décrivant les changements et les tests effectués.

## Convention de branches

- `docs/...` : rédaction et correction documentaire.
- `build/...` : chaîne de compilation.
- `companion/...` : ressources du Companion Pack.
- `fix/...` : correction ciblée.

## Convention de commits

Exemples :

```text
docs(volume-0): add project vision chapter
docs(livre-i): document Docker installation
build: add PDF generation workflow
fix(comfyui): correct AMD ZLUDA instructions
```

## Validation minimale

Avant toute pull request :

- [ ] Le Markdown est lisible.
- [ ] Les blocs de code indiquent leur langage.
- [ ] Les commandes destructrices comportent un avertissement.
- [ ] Les informations évolutives indiquent leur source et leur date de vérification.
- [ ] La génération Pandoc réussit ou les limitations sont documentées.
- [ ] Les nouveaux fichiers sont ajoutés à l'index et à `contents.txt` si nécessaire.

## Contenu sensible et adulte

Les contributions relatives aux thèmes adultes doivent respecter la loi applicable, concerner exclusivement des adultes et éviter tout contenu non consensuel présenté comme souhaitable. Aucun contenu sexuel impliquant des mineurs, des personnes présentées comme mineures ou des animaux réels n'est accepté.

## Signalement des problèmes

Une issue doit préciser :

- la page ou l'identifiant concerné ;
- le comportement observé ;
- le résultat attendu ;
- les versions des outils ;
- la configuration matérielle lorsque le problème concerne les performances.
