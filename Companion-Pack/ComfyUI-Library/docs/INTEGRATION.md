# Intégration

1. Installer ComfyUI dans un dossier séparé et épingler `v0.28.0`.
2. Conserver modèles, `custom_nodes`, `input`, `output`, `temp` et utilisateur hors du Pack.
3. Copier les workflows dans le dossier utilisateur ComfyUI.
4. Résoudre chaque modèle dans `manifests/models/MODELS.yaml`.
5. Vérifier le SHA-256 local avant tout statut `accepted`.
6. Utiliser le profil CPU pour le diagnostic fonctionnel.
7. Traiter le profil AMD RDNA2 comme laboratoire isolé.
8. Promouvoir une sortie seulement après revue humaine et dossier de provenance.
