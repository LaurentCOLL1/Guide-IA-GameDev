# Profil des manifestes

Les fichiers `.yaml` du Pack utilisent volontairement le sous-ensemble JSON-compatible de YAML 1.2. Ils restent lisibles par un parseur YAML, mais sont validables avec la bibliothèque standard Python.

Champs obligatoires d’un workflow : `id`, `version`, `status`, version ComfyUI, profil backend, chemins du graphe, modèles, custom nodes, paramètres de reproductibilité, sortie attendue et date de vérification.

Un modèle absent conserve `sha256: null`, une licence non résolue et le statut `user-must-resolve-before-execution`. Aucun champ vide n’est transformé en preuve.
