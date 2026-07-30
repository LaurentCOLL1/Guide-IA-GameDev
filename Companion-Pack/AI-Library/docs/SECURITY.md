# Sécurité

## Hypothèses de qualification

La campagne automatique utilise uniquement `127.0.0.1`, des fixtures synthétiques et des faux serveurs inclus. Aucun trafic Internet de fournisseur n’est émis.

## Contrôles

- validation stricte du schéma et du port ;
- boucle locale obligatoire par défaut ;
- HTTP distant interdit sans décision explicite ;
- taille maximale des réponses ;
- délais de connexion et de réponse ;
- reprises limitées ;
- file bornée ;
- opérations autorisées ;
- rejet des caractères de contrôle dangereux ;
- rédaction des jetons et en-têtes d’autorisation ;
- aucun secret dans les messages d’erreur ;
- annulation vérifiée avant et après le transport.

## Secrets

`api_key_env` contient uniquement le nom d’une variable d’environnement. La valeur :

- n’est pas sérialisée ;
- n’est pas incluse dans les clés de cache ;
- n’est pas journalisée ;
- n’est pas écrite dans les preuves.

## Limites

Ces contrôles ne remplacent pas TLS, authentification, sandbox, permissions système, signature, SBOM complet ou revue de sécurité d’un déploiement réel.
