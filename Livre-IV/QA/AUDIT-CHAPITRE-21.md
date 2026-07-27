---
title: "Audit post-création — Livre IV, chapitre 21"
id: "DOC-L4-QA-AUDIT-CH21"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre IV"
chapter: 21
chapter-id: "DOC-L4-CH21"
chapter-version: "1.0.0"
last-verified: "2026-07-27T21:47:17+02:00"
audit-status: "complete"
audit-date: "2026-07-27T21:47:17+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 21 — Modding et contenu communautaire

## 1. Décision

Décision : **accepté avec réserves runtime, sandbox, plateformes UGC, licences, modération, support, sauvegardes, multijoueur et fin de Livre**.

Le chapitre satisfait le plan maître au niveau documentaire. Il définit surfaces d’extension, formats, API, documentation, isolation, compatibilité, dépendances, versions, licences, modération et support. Il prépare SDK, template, mod d’exemple, sandbox conceptuelle et politique communautaire sans prétendre qu’ils existent.

## 2. Périmètre contrôlé

- frontière avec le chapitre 14 pour CI/CD ;
- frontière avec le chapitre 16 pour les packages officiels ;
- frontière avec le chapitre 17 pour publication initiale et exigences de plateformes ;
- frontière avec le chapitre 19 pour localisation ;
- frontière avec le chapitre 20 pour mises à jour et retours arrière officiels ;
- frontière avec le chapitre 22 pour maintenance, archivage et fin de vie ;
- niveaux de support différenciant données déclaratives, packs Godot et code exécutable ;
- manifeste canonique, identités namespacées, versions et empreintes ;
- staging, inspection d’archives, quotas et activation réversible ;
- PCK et ZIP montés sans remplacement implicite des ressources officielles ;
- exclusion par défaut des scripts communautaires et extensions natives non isolés ;
- capacités, allowlists, chemins, réseau, processus et données sensibles ;
- dépendances, cycles, contraintes, ordre stable, conflits et fusion ;
- installation, activation, désactivation, désinstallation et mode sûr ;
- sauvegardes, état namespacé, migrations et dépréciation ;
- localisation, accessibilité et multijoueur ;
- SDK, templates, mod d’exemple et commandes de validation ;
- Steam Workshop, sources manuelles, releases et adaptateurs de plateforme ;
- licences, provenance, modération, confidentialité et support ;
- tests, performance, observabilité, modes Solo/Studio et dix diagnostics.

## 3. Contrôle du plan maître

Les cinq objectifs sont couverts : surfaces d’extension ; formats, API et documentation ; isolation du contenu non fiable ; compatibilité, dépendances et versions ; licences, modération et support.

Les cinq livrables sont représentés : SDK ou templates, documentation, sandbox conceptuelle, mod d’exemple et politique communautaire. La validation demandée par installation, désactivation et conflit est préparée comme campagne, sans exécution revendiquée.

## 4. Contrôle pédagogique

- vocabulaire défini avant usage ;
- progression du modèle de menace vers manifeste, installation, chargement, compatibilité et gouvernance ;
- exemples GDScript, Python, JSON, YAML, PowerShell, CMD, Bash et Docker expliqués ;
- fonctions, entrées, retours, effets de bord, invariants et limites explicités ;
- tous les repères d’utilisation présents ;
- chaque bloc clôturé possède un repère immédiatement avant le fence ;
- 23 explications structurées hors diagnostics ;
- dix cas fautifs, dix corrections et leurs justifications ;
- checklist, critère de passage et synthèse `Project Asteria` présents ;
- aucune instruction de pilotage du chapitre suivant dans le texte lecteur.

## 5. Contrôle technique

- `ProjectSettings.load_resource_pack()` est utilisé avec `replace_files` à `false` pour le chemin communautaire candidat ;
- les packs sont réservés à un namespace `res://mods/<id>/` ;
- l’ordre de montage et le risque de remplacement sont conformes à la documentation Godot ;
- le chargement de GDScript est traité comme exécution de code, non comme donnée sandboxée ;
- les archives sont inspectées avant extraction ;
- les identités, versions, dépendances et capacités sont validées avant activation ;
- les capacités inconnues sont refusées par défaut ;
- l’ordre de chargement repose sur graphe et départage stable ;
- les sauvegardes conservent ensemble de mods, versions, empreintes et état namespacé ;
- le contrat multijoueur reste sous autorité serveur ;
- SPDX et Creative Commons sont présentés comme formats ou licences, sans preuve de titularité ;
- Steam Workshop et autres plateformes sont des sources, pas des validateurs de sécurité.

## 6. Métriques statiques

| Mesure | Valeur |
|---|---:|
| Lignes | 1731 |
| Titres | 66 |
| Blocs de code ou données | 43 |
| Blocs significatifs | 42 |
| Marqueurs d’explication | 43 |
| Explications structurées hors diagnostics | 23 |
| Cas fautifs expliqués | 10 |
| Corrections expliquées | 10 |
| Titres dupliqués | 0 |
| Blocs significatifs dupliqués | 0 |
| Paragraphes longs dupliqués | 0 |

## 7. Contrôle des références

Références officielles vérifiées :

- Godot Engine pour PCK/ZIP, chargement runtime, `ProjectSettings`, `PCKPacker`, `ZIPReader`, `FileAccess`, `DirAccess`, JSON et GDScript ;
- Steamworks pour Workshop, guide d’implémentation et `ISteamUGC` ;
- itch.io pour Butler ;
- GitHub Docs pour les releases ;
- documentation Python pour `zipfile` ;
- SPDX pour spécification et expressions de licences ;
- Creative Commons pour les considérations de licence.

Les liens sont nommés et cliquables. Les mécanismes volatils de plateforme restent à revérifier au moment d’une implémentation.

## 8. Contrôle des doublons et frontières

Aucun titre dupliqué, bloc significatif dupliqué ou paragraphe long dupliqué n’est détecté par le contrôle local.

Le chapitre ne recrée ni la chaîne CI/CD, ni les packages officiels, ni la publication initiale, ni la localisation, ni le système de mises à jour, ni l’archivage. Il consomme ces autorités et documente leurs interfaces avec l’écosystème communautaire.

## 9. Contrôle des revendications

- aucun chargeur, SDK, template, schéma final ou mod d’exemple n’est matérialisé ;
- aucun PCK, ZIP, script, asset ou extension native n’est chargé ;
- aucune sandbox n’est qualifiée ;
- aucun quota n’est mesuré ;
- aucune plateforme UGC ou Workshop n’est configurée ;
- aucune installation, activation, désactivation, désinstallation ou migration n’est exécutée ;
- aucune sauvegarde moddée ni session multijoueur n’est testée ;
- aucune licence ou provenance n’est juridiquement validée ;
- aucune modération, suppression, sanction ou procédure d’appel n’est exécutée ;
- aucun support utilisateur réel n’est traité ;
- aucun PDF du Livre IV n’est produit.

## 10. Réserves

- matérialiser un chargeur et un gestionnaire de mods ;
- adopter et versionner les schémas de manifeste et de contenu ;
- qualifier les formats runtime et les quotas par plateforme ;
- démontrer l’isolation ou maintenir l’exclusion du code communautaire ;
- produire SDK, templates, validateur et mod d’exemple redistribuable ;
- exécuter les campagnes d’installation, désactivation, conflit et mode sûr ;
- tester les sauvegardes, migrations et ensembles de mods absents ;
- tester les divergences multijoueur sous autorité serveur ;
- intégrer et qualifier les adaptateurs de plateformes UGC ;
- faire revoir licences, provenance, politique communautaire, modération et confidentialité ;
- publier les limites de support ;
- définir la licence globale de la collection ;
- traiter le balisage final d’accessibilité PDF.

## 11. Preuves d’intégrité

- empreinte SHA-256 du chapitre : `964faaa7b0bb73f57febe16c5737bddf638f2f8aa71c7a9f73fae6fd143e8f6d` ;
- empreinte SHA-256 de l’audit : calculée après fermeture du présent rapport et enregistrée dans la preuve YAML ;
- validation permanente légère : en attente du commit final de la branche ;
- niveau d’audit : `static-review`.

## 12. Conclusion

Le chapitre 21 est accepté au niveau documentaire avec zéro erreur bloquante dans les contrôles locaux. Les réserves concernent toute matérialisation, exécution, sécurité, plateforme, donnée utilisateur, licence, modération et publication. La seule alerte globale attendue reste la licence de collection non définie.
