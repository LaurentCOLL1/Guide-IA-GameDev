# Scan terminologique du chapitre 17

- ligne des intervalles : 1314
- libellés ambigus hors section 37 : 6

- ligne 230: - **Retours et erreurs :** `validate()` renvoie un code `Error` ; `next_sequence()` renvoie `-1` lorsque le tick régresse et n’altère alors aucun compteur.
- ligne 411: - **Erreurs :** une clé inconnue produit `ERR_DOES_NOT_EXIST` ; un type incorrect produit `ERR_INVALID_DATA`.
- ligne 666: - **Erreurs :** une action invalide produit `ERR_INVALID_DATA` ; deux identifiants identiques produisent `ERR_ALREADY_EXISTS` ; aucun remplacement partiel n’est effectué.
- ligne 834: - **Erreur fréquente :** `NO_PLAN` signifie que la recherche bornée a épuisé les possibilités autorisées ; `BUDGET_EXCEEDED` signifie qu’elle s’est arrêtée avant cette conclusion.
- ligne 1218: - **Erreur attendue :** demander une clé non enregistrée produit un refus explicite, jamais un appel dynamique par nom de méthode fourni par les données.
- ligne 1421: - **Erreurs :** le code de retour de `decide()` devrait être enregistré dans une trace ou un compteur ; le brouillon ne l’ignore que pour garder l’extrait centré sur l’ordonnancement.
