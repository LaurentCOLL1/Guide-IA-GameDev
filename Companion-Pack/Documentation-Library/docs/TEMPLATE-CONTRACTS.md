# Contrats des patrons

Les tokens utilisent la forme `{{TOKEN_ASCII}}`. Un token est obligatoire dès qu’il apparaît dans le patron. Le générateur refuse les valeurs manquantes, les valeurs inutilisées et les tokens non résolus.

Les profils sont des objets JSON plats. Les fragments Markdown multilignes sont autorisés sous forme de chaînes. Cette simplicité évite l’exécution de code, les conditions implicites et les dépendances de moteur de templates.

Les exemples remplis sont régénérés octet pour octet pendant les tests. Une modification d’un patron exige donc la mise à jour volontaire du profil ou de l’exemple associé.
