# Politique de branches — Studio

## Branches

- `main` : branche protégée recommandée ;
- `feat/<ticket>-<sujet>` : fonctionnalité ;
- `fix/<ticket>-<sujet>` : correction ;
- `release/<version>` : préparation de candidat lorsque nécessaire ;
- `hotfix/<ticket>-<sujet>` : correction urgente avec suivi d’incident.

## Revue

La politique du modèle exige au moins une revue indépendante pour les changements ordinaires. Les changements sensibles doivent impliquer le propriétaire du chemin concerné et un approbateur de release distinct lorsque l’organisation le permet.

## Protection

Configuration recommandée :

- pull request obligatoire ;
- validations CI obligatoires ;
- branche à jour avant fusion ;
- refus du push direct ;
- CODEOWNERS requis pour les chemins sensibles ;
- suppression automatique des branches fusionnées.

Ces réglages ne sont pas activés par ce fichier. Ils doivent être appliqués dans le dépôt cible puis vérifiés séparément.
