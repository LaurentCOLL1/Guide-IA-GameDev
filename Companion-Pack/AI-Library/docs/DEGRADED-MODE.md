# Comportement dégradé

L’indisponibilité de l’IA locale n’autorise pas l’invention d’une réponse prétendument générée.

## Contrat

L’appel retourne soit :

- `AiResponse` avec une origine et un identifiant corrélés ;
- une erreur typée : configuration, sécurité, annulation, transport, protocole ou saturation.

## Repli de la fonctionnalité

La fonctionnalité propriétaire choisit un repli déterministe, par exemple :

- texte local pré-écrit ;
- résultat lexical local ;
- action reportée ;
- fonctionnalité facultative masquée avec message explicite.

Le transport ne choisit pas le contenu du repli.
