# Empreinte d’environnement

L’empreinte exclut hostname, nom d’utilisateur, adresse IP, chemins personnels et variables secrètes. Elle conserve : OS, version, architecture, runtime, modèle CPU lorsque disponible, nombre logique de processeurs, mémoire totale déclarée, renderer, adaptateur déclaré et métadonnées publiques du runner.

Un SHA-256 canonique relie les résultats à ces champs sans remplacer leur copie lisible.
