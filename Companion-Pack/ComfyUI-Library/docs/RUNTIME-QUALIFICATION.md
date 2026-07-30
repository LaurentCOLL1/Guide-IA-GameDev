# Qualification runtime

Le workflow permanent clone le tag ComfyUI `v0.28.0`, enregistre son commit, installe ses dépendances dans Python 3.12, démarre le serveur en CPU sur `127.0.0.1`, soumet `WF-COMFY-0001`, attend la fin de la file, vérifie la sortie PNG et ses métadonnées, puis confirme l’absence de modèles et de custom nodes tiers.

Le workflow `WF-COMFY-0100` reste un modèle de production non exécuté. Il ne devient `accepted` qu’après résolution du modèle, de sa licence, de son empreinte et d’une campagne séparée.
