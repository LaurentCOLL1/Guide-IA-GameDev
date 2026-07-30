# Politique de branches — Solo

## Branches

- `main` : état intégré et publiable uniquement après validation ;
- `feat/<sujet>` : fonctionnalité courte ;
- `fix/<sujet>` : correction ;
- `docs/<sujet>` : documentation ;
- `chore/<sujet>` : maintenance sans changement produit.

## Revue

Le profil Solo utilise une auto-revue différée :

1. travailler sur une branche courte ;
2. exécuter les validations ;
3. quitter le contexte de modification ;
4. relire le diff dans une session distincte ;
5. fusionner seulement depuis un commit identifié.

`required_reviewers: 0` ne signifie pas absence de contrôle. Il évite d’inventer un second membre d’équipe.

## Protection

La protection de `main` est recommandée, mais ce fichier ne l’active pas. La règle doit être configurée sur l’hébergement Git réel.
