# Matrice des dépendances

| Couche source | Couches cibles autorisées |
|---|---|
| Domaine | Domaine, Core |
| Application | Domaine, Application, Core |
| Présentation | Domaine, Application, Présentation, Core |
| Infrastructure | Domaine, Application, Infrastructure, Core |
| Core | Core |
| Composition | Toutes les couches nécessaires à l’assemblage |

Une fonctionnalité ne doit pas atteindre directement l’implémentation interne d’une autre fonctionnalité. Le partage passe par une interface publique, un contrat réellement commun ou la composition.
