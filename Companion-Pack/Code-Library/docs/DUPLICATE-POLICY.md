# Politique de non-duplication

`catalog.json` attribue un propriétaire à chaque concept. Le validateur refuse :

- deux composants du même langage portant le même concept ;
- deux symboles publics identiques dans un même langage ;
- deux chemins sources identiques ;
- un concept réservé à un autre pack.

Les paires Python/GDScript sont autorisées uniquement lorsque leur `concept_id` est identique et leur `port_group` explicite.

## Concepts réservés à d’autres packs

- `bounded-task-queue` et `ttl-lru-cache` : AI Library ;
- `bootstrap-report` et `project-composition` : Starter Kit / Project Templates ;
- `module-generator` : Project Templates.

Le repository mémoire générique du Pack 4 remplace les exemples pédagogiques locaux uniquement lorsqu’un projet choisit explicitement de l’adopter ; il n’impose pas une migration automatique.
