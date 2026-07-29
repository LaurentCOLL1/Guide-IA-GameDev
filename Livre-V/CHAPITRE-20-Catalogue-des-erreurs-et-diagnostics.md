---
title: "Livre V — Fiche 20 : Catalogue des erreurs et diagnostics"
id: "DOC-L5-CH20"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 20
last-verified: "2026-07-29T16:26:00+02:00"
audit-status: "complete"
audit-date: "2026-07-29T16:26:00+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-20.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "cross-domain-errors-diagnostics-and-routing"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-python:
  implementation: "CPython"
  version: "3.14.6"
  fallback-version: "3.13.14"
  qualification-status: "inherited-provisional"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Catalogue des erreurs et diagnostics

> **Type de document :** cartes de diagnostic, index de symptômes et messages, matrices de routage et portes de preuve.
> **Lecture :** partir du symptôme ou du message, enregistrer le contexte exact, suivre les vérifications du moins intrusif au plus ciblé, puis rejoindre la procédure propriétaire.
> **Principe :** un message, une corrélation ou un contournement ne prouve pas une cause ; toute conclusion reste liée à une version, un environnement, une reproduction et une preuve consultable.

## Index express

| Besoin | Ouvrir |
|---|---|
| enregistrer une entrée diagnostique complète | [DIAG-00](#diag-00--contrat-dune-entrée-diagnostique) |
| trouver le propriétaire d’un symptôme | [Matrice A](#matrice-a--routage-du-signal-vers-le-propriétaire) |
| distinguer symptôme, hypothèse et cause | [DIAG-01](#diag-01--vocabulaire-et-niveaux-de-certitude) |
| figer versions, build et configuration | [DIAG-02](#diag-02--empreinte-denvironnement-et-de-version) |
| séparer observation, attendu et reproduction | [DIAG-03](#diag-03--contrat-dobservation-et-de-reproduction) |
| collecter sans surexposer les données | [DIAG-04](#diag-04--collecte-de-preuves-et-expurgation) |
| savoir ce qu’une preuve autorise à conclure | [Matrice B](#matrice-b--preuves-capacités-et-limites) |
| suivre un arbre progressif | [DIAG-05](#diag-05--arbre-de-diagnostic-progressif) |
| indexer messages, codes et signatures | [DIAG-06](#diag-06--messages-codes-et-signatures) |
| tester une hypothèse sans tout modifier | [DIAG-07](#diag-07--hypothèses-et-expériences-contrôlées) |
| qualifier contournement, correction et vérification | [DIAG-08](#diag-08--cause-confirmée-contournement-correction-et-vérification) |
| diagnostiquer outils, dépendances et CI | [DIAG-09](#diag-09--index-outils-dépendances-et-ci) |
| diagnostiquer données, assets et runtime | [DIAG-10](#diag-10--index-données-assets-et-runtime) |
| diagnostiquer performance, réseau et livraison | [DIAG-11](#diag-11--index-performance-réseau-et-livraison) |
| promouvoir une conclusion selon la preuve | [Matrice C](#matrice-c--niveaux-de-preuve-et-portes-de-promotion) |
| maintenir, fusionner ou retirer une fiche | [DIAG-12](#diag-12--maintenance-doublons-versions-et-retrait) |

---

<!-- l5:card -->
## DIAG-00 — Contrat d’une entrée diagnostique

| Champ | Règle |
|---|---|
| identité | identifiant stable indépendant du titre, de l’outil de suivi et du message humain |
| signal | symptôme observable, message exact, code de sortie, alerte ou écart mesuré |
| objet | outil, service, scène, asset, fichier, build, plateforme ou procédure concernée |
| contexte | versions, OS, architecture, renderer, locale, configuration, flags, mods et dépendances |
| attendu | contrat, exigence, invariant, documentation officielle ou oracle de test |
| observé | fait, valeur, instant, étape et artefact consultable, sans interprétation cachée |
| reproduction | préconditions, état initial, actions, tentatives, fréquence et résultat |
| preuves | journaux bornés, traces, métriques, captures, manifests, dumps ou sorties de commandes |
| certitude | inconnu, hypothèse, corrélation, cause probable, cause confirmée ou non applicable |
| traitement | vérification suivante, propriétaire, contournement, correction, test de régression et retrait |
| portée | versions affectées, plateformes, configurations, risques et limites connues |
| confidentialité | minimisation, expurgation, rétention, accès et absence de secret ou donnée personnelle inutile |

**Réponse rapide :** une entrée diagnostique est un dossier de décision, pas une phrase « ça ne marche pas ». Le modèle détaillé de rapport, d’archive et de reproduction appartient au [chapitre 4 du Livre IV](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#1-rôle-du-chapitre), tandis que la présente fiche fournit une consultation transversale et un routage vers les sources propriétaires.

**Diagramme compact :** `signal → contexte → attendu/observé → reproduction → preuves → hypothèses → cause confirmée → correction → non-régression`.

**Niveau de preuve :** `static-review`. Aucun rapport, crash, log, dump, capture, reproduction, cause ou correctif réel n’est matérialisé ici.

---

<!-- l5:matrix -->
## Matrice A — Routage du signal vers le propriétaire

| Signal dominant | Première question | Propriétaire principal | Validation ou correction |
|---|---|---|---|
| installation ou commande absente | quel shell, paquet, chemin et privilège ? | [outils de base](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#matrice-c--commandes-minimales-de-vérification) | tutoriel de l’outil dans le Livre I |
| environnement Python incohérent | quel interpréteur, verrou et environnement actif ? | [Python et backends](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md) | installation propriétaire et fichier de versions |
| modèle IA non chargé | quel paquet exact, moteur, révision et mémoire ? | [fiches de modèles](CHAPITRE-05-Fiches-des-modeles-de-langage.md) | carte du modèle, backend et manifeste |
| fichier ou schéma invalide | quel format, encodage et version de schéma ? | [formats d’échange](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md) | validateur du format et migration propriétaire |
| anomalie fonctionnelle | quel attendu, état initial et scénario minimal ? | [reproduction des anomalies](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#13-étapes-de-reproduction) | cas et oracle du [chapitre 3](../Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md#6-contrat-dun-cas) |
| journal ou trace ambiguë | quelle fenêtre, catégorie et corrélation ? | [observabilité locale](../Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md#8-distinguer-événements-métriques-et-traces) | reproduction et preuve complémentaire |
| lenteur ou saccade | CPU, GPU, mémoire, chargement ou logique ? | [profilage CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md#1-rôle-du-chapitre) | campagne spécialisée des chapitres 6 à 10 |
| corruption ou perte de données | quelle version, migration, sauvegarde et empreinte ? | [sauvegardes et reprise](../Livre-IV/CHAPITRE-15-Sauvegardes-migrations-et-reprise-apres-incident.md#1-rôle-du-chapitre) | restauration, migration et non-régression |
| défaut visuel ou asset | source, export, import, scène ou rendu ? | [référence graphique](CHAPITRE-18-Reference-graphique-et-3D.md#audr-12--symptômes-diagnostics-et-acceptation) | production et validation des chapitres 28 et 29 du Livre III |
| défaut audio | source, signal, export, bus, scène ou dispositif ? | [référence audio](CHAPITRE-19-Reference-audio.md#audr-12--symptômes-diagnostics-et-acceptation) | production audio du [chapitre 26](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#1-rôle-du-chapitre) |
| désynchronisation réseau | autorité, ordre, horloge ou transport ? | [synchronisation réseau](../Livre-IV/CHAPITRE-12-Synchronisation-autorite-et-prediction.md#1-rôle-du-chapitre) | scénario multijoueur reproductible |
| CI ou publication en échec | quel job, artefact, secret, permission ou environnement ? | [DevOps](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#1-rôle-du-chapitre) | job minimal, logs et reproduction locale |
| export ou paquet incorrect | preset, ressource, plateforme ou signature ? | [exports Godot](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md#1-rôle-du-chapitre) | matrice de contenu et test d’installation |
| signal de sécurité | secret, intégrité, permission ou exposition ? | [serveurs et sécurité](../Livre-IV/CHAPITRE-13-Serveurs-dedies-et-securite-reseau.md#1-rôle-du-chapitre) | confinement, rotation, revue et incident séparé |

**Décision :** router par le premier maillon observable, non par le composant supposé coupable. Un propriétaire de diagnostic coordonne la collecte ; il n’est pas automatiquement l’auteur du défaut.

---

<!-- l5:card -->
## DIAG-01 — Vocabulaire et niveaux de certitude

| Terme | Définition opérationnelle | Ce qu’il ne prouve pas |
|---|---|---|
| signal | information initiale provenant d’un joueur, outil, test ou système | qu’une anomalie existe réellement |
| symptôme | comportement visible : crash, blocage, valeur, corruption, artefact, lenteur ou absence | le composant fautif |
| message | texte ou code émis par un outil dans une version et un contexte | une cause unique |
| anomalie | écart observé entre attendu et réel | le défaut source |
| hypothèse | explication testable compatible avec les preuves courantes | une conclusion |
| corrélation | variation conjointe ou proximité temporelle | une causalité |
| cause probable | hypothèse soutenue par plusieurs indices mais non isolée | une correction complète |
| cause confirmée | variable isolée dont la modification contrôlée supprime ou rétablit le symptôme | l’absence d’autres causes |
| contournement | action réduisant l’impact sans supprimer la cause | une résolution |
| correction | modification visant la cause confirmée | une vérification réussie |
| régression | réapparition d’un défaut ou rupture provoquée par une modification | l’identité automatique avec un ancien rapport |
| inconnu | preuve insuffisante ou conflit non résolu | un échec de l’investigation |

**Réponse rapide :** utiliser le vocabulaire du [chapitre 4](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#5-vocabulaire-opérationnel) et la séparation entre preuve, réserve, sévérité et priorité du [chapitre 2](../Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md#5-vocabulaire-opérationnel). La formulation « causé par » est réservée à une relation démontrée.

**Échelle recommandée :** `unreviewed → observed → reproduced → hypothesis → probable → confirmed → corrected → verified → protected`. Chaque promotion nomme la nouvelle preuve.

**Limite :** une source officielle peut confirmer le sens d’un message ou une incompatibilité documentée ; elle ne prouve pas que le cas local possède exactement cette cause sans comparaison du contexte.

---

<!-- l5:card -->
## DIAG-02 — Empreinte d’environnement et de version

| Dimension | Valeurs à conserver | Risque si omise |
|---|---|---|
| produit | build ID, commit, canal, configuration, manifeste de contenu | comparer deux exécutables différents |
| système | OS, édition, architecture, locale, horloge et fuseau | masquer un comportement de plateforme |
| moteur | Godot, renderer, mode headless, template d’export | attribuer au code un écart de runtime |
| langage | Python, GDScript, compilateur ou runtime exact | ignorer une incompatibilité de version |
| dépendances | lockfile, paquet, modèle, plugin, extension et checksum | reproduire avec une autre pile |
| matériel | CPU, GPU, pilotes, RAM, stockage et périphérique | généraliser une limite matérielle |
| configuration | flags, variables, options, mods, permissions et politiques | perdre une branche d’exécution |
| données | schéma, fixture, seed, catalogue, asset et empreinte | tester un état différent |
| réseau | topologie, latence simulée, protocole, serveur et région | confondre logique locale et transport |
| confidentialité | identifiants pseudonymes, redaction et accès | exposer des données inutiles |

**Réponse rapide :** l’empreinte minimale reprend le [manifeste d’environnement](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#9-manifeste-denvironnement), le [build et la révision](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#10-build-et-révision), la configuration active et l’état initial. Elle est capturée avant une mise à jour, un nettoyage de cache ou une réinstallation.

**Contrôle de dérive :** comparer les versions et empreintes ligne par ligne ; ne modifier qu’une dimension à la fois lorsqu’une reproduction contrôlée est possible.

**Alternative :** lorsqu’une information n’est plus accessible, inscrire `unknown` avec la raison plutôt que d’inventer la valeur ou de la déduire d’une machine voisine.

---

<!-- l5:card -->
## DIAG-03 — Contrat d’observation et de reproduction

| Élément | Question | Source propriétaire |
|---|---|---|
| état initial | peut-il être reconstruit sans connaissance tacite ? | [fixture synthétique](../Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md#9-fixture-synthétique) |
| préconditions | sont-elles observables avant l’action ? | [préconditions](../Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md#7-préconditions-observables) |
| actions | chaque étape possède-t-elle un verbe, un ordre et des paramètres ? | [étapes de reproduction](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#13-étapes-de-reproduction) |
| attendu | provient-il d’une exigence, d’un invariant ou d’un oracle ? | [résultat attendu](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#14-résultat-attendu) |
| observé | décrit-il faits, valeurs et premier instant de rupture ? | [résultat observé](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#15-résultat-observé) |
| fréquence | indique-t-elle reproductions, tentatives et conditions ? | [fréquence et tentatives](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#16-fréquence-et-tentatives) |
| indépendance | une autre personne ou un script peut-il rejouer le dossier ? | [reproduction indépendante](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#27-reproduction-indépendante) |
| réduction | actions, état, entrées et non-déterminisme sont-ils isolés ? | [réduction progressive](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#30-réduction-par-suppression-détapes) |

**Réponse rapide :** séparer strictement l’attendu, l’observé et l’interprétation. Un cas non reproduit devient `NOT_REPRODUCED`, un cas impossible à essayer devient `BLOCKED` ; aucun des deux ne signifie « inexistant ».

**Diagramme compact :** `préconditions → état initial → actions atomiques → premier écart → tentatives → reproduction indépendante → réduction`.

**Critère :** une reproduction minimale conserve le symptôme avec moins d’actions ou de données ; elle ne réécrit pas le rapport original et ne garantit pas un minimum global.

---

<!-- l5:card -->
## DIAG-04 — Collecte de preuves et expurgation

| Preuve | Collecte minimale | Risque principal |
|---|---|---|
| log | fenêtre bornée, niveau, catégorie, horodatage et corrélation | volume, texte libre, secrets |
| métrique | unité, fenêtre, agrégation, dimensions et fréquence | cardinalité, moyenne trompeuse |
| trace | opération, spans, statut, parenté et durée | coût, identifiants sensibles |
| sortie de commande | commande exacte, shell, code de sortie et flux utile | chemins personnels, tokens |
| capture | étape, zone, annotation et version | données visibles, contexte incomplet |
| vidéo | début avant le scénario, actions visibles et revue | identité, voix, notifications |
| dump | build, symboles, accès restreint et politique de conservation | mémoire sensible, secrets |
| fichier ou fixture | origine, taille, empreinte, schéma et statut synthétique | données joueur, redistribution |
| manifeste | liste déterministe, tailles et SHA-256 | confusion entre intégrité et authenticité |
| décision | auteur, date, portée, réserves et liens de preuve | conclusion sans artefacts |

**Réponse rapide :** le [chapitre 5](../Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md#1-rôle-du-chapitre) possède la collecte systématique ; le [chapitre 4](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#18-archive-diagnostique) possède l’archive du cas. Exporter seulement la fenêtre nécessaire, puis appliquer l’[expurgation](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#20-expurgation-des-données).

**Diagramme compact :** `source locale → sélection bornée → expurgation → manifeste → accès contrôlé → preuve liée au cas → purge`.

**Sécurité :** ne jamais demander au lecteur de publier un token, une clé privée, un contrat, une voix de référence, une sauvegarde joueur brute ou un dump non revu dans une issue publique.

---

<!-- l5:matrix -->
## Matrice B — Preuves, capacités et limites

| Preuve | Peut établir | Ne peut pas établir seule | Complément recommandé |
|---|---|---|---|
| message exact | texte, code et composant émetteur pour une version | cause unique | contexte et documentation de version |
| log structuré | ordre d’événements et attributs enregistrés | état non journalisé ou causalité | reproduction et trace |
| métrique | tendance ou seuil selon une fenêtre | événement individuel exact | logs, profiler ou scénario |
| trace | chemin et durée d’une opération instrumentée | travail hors trace ou défaut métier | oracle et reproduction |
| capture | symptôme visible à un instant | séquence complète ou valeur interne | étapes, logs et données structurées |
| crash dump | pile et mémoire accessibles au point de crash | cause métier complète ou absence de corruption antérieure | symboles, build et reproduction |
| reproduction | retour du symptôme dans les conditions déclarées | cause | réduction et expérience contrôlée |
| réduction | variables nécessaires au scénario observé | minimum global | répétitions et variations |
| test A/B | effet d’une variable changée | généralisation hors échantillon | répétitions et contrôle des autres variables |
| source officielle | sens, support, défaut connu ou exigence documentée | présence du même défaut local | comparaison versions et cas minimal |
| correctif appliqué | modification de l’artefact | disparition du défaut | vérification et non-régression |
| CI verte | réussite des jobs exécutés | qualité des tests absents ou runtime non couvert | campagne spécialisée |

**Décision :** aucune preuve n’est universellement supérieure. Choisir la preuve qui répond à la question, puis enregistrer ce qu’elle laisse inconnu.

---

<!-- l5:card -->
## DIAG-05 — Arbre de diagnostic progressif

| Étape | Vérification | Action si échec | Action si succès |
|---|---|---|---|
| 1. préserver | versions, message, état, fichiers et horodatages sont conservés | capturer avant toute modification | passer à la qualification |
| 2. qualifier | attendu, observé, impact et périmètre sont distincts | compléter le rapport sans attribuer de cause | router vers le propriétaire |
| 3. vérifier les préconditions | entrée, permission, espace, service et dépendance existent | corriger la précondition puis rejouer | exécuter le scénario |
| 4. reproduire | le symptôme revient dans le contexte déclaré | varier une dimension ou classer intermittent | enregistrer une tentative positive |
| 5. réduire | retirer bruit, actions, données ou dépendances | restaurer la dernière variable nécessaire | obtenir un cas plus petit |
| 6. comparer | version, environnement ou configuration témoin diffère d’un seul facteur | réduire encore les différences | formuler une hypothèse testable |
| 7. instrumenter | la preuve manquante peut être collectée localement et sans risque excessif | documenter la limite | exécuter une collecte bornée |
| 8. tester l’hypothèse | une expérience peut falsifier l’explication | conserver `unknown` ou reformuler | répéter et chercher un contrôle inverse |
| 9. confirmer | modifier la cause candidate supprime puis rétablit le symptôme | rester à `probable` | déclarer la cause bornée |
| 10. corriger | la modification cible la cause et possède un rollback | ne pas confondre contournement et correctif | vérifier le scénario original |
| 11. protéger | un test ou une porte détecte le retour du défaut | enregistrer le risque résiduel | fermer avec preuves et versions |

**Réponse rapide :** commencer par les vérifications réversibles et peu intrusives. Une réinstallation, une suppression de cache, une migration ou une restauration peut détruire la preuve ; elle intervient seulement après capture et lorsqu’elle répond à une hypothèse explicite.

**Diagramme compact :** `préserver → qualifier → préconditions → reproduire → réduire → comparer → instrumenter → falsifier → confirmer → corriger → protéger`.

**Escalade :** interrompre la procédure et suivre le protocole spécialisé si le cas implique sécurité, perte de données, données personnelles, dommage matériel, santé, conformité ou publication irréversible.

---

<!-- l5:card -->
## DIAG-06 — Messages, codes et signatures

| Élément | Règle d’indexation | Exemple de recherche |
|---|---|---|
| message | conserver texte exact, ponctuation, langue, outil et version | phrase entre guillemets puis version |
| code de sortie | enregistrer entier, shell, commande et étape | code + nom de l’exécutable |
| exception | type, message, chaîne de causes et pile symbolisée | classe + première frame propriétaire |
| warning Godot | catégorie, ressource, scène, nœud et renderer | fragment stable + version moteur |
| erreur d’import | source, format, preset, cache et ressource générée | extension + option d’import |
| erreur Python | interpréteur, environnement, paquet, lockfile et traceback | exception + versions du paquet |
| erreur CI | workflow, run, job, step, commit et artefact | nom du step + code de sortie |
| erreur réseau | rôle, direction, protocole, corrélation et horloge | code + côté client/serveur |
| signature | dimensions normalisées utiles à la recherche | sous-système + symptôme + version + rupture |
| alias | ancienne formulation ou traduction liée à l’entrée canonique | message localisé ou renommé |

**Réponse rapide :** un message est une clé de recherche, jamais une cause automatique. La [signature de doublon](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#35-signature-de-doublon) aide à rapprocher les cas, mais la fusion exige une cause commune ou une décision de triage documentée.

**Normalisation :** retirer identifiants volatils uniquement dans un champ dérivé ; conserver le message brut et son empreinte dans la preuve originale.

**Versionnement :** lorsqu’un éditeur change le texte, garder les deux formulations, leurs versions de début et fin, et le même concept canonique seulement si le sens reste confirmé.

---

<!-- l5:card -->
## DIAG-07 — Hypothèses et expériences contrôlées

| Champ | Règle |
|---|---|
| observation expliquée | citer précisément le symptôme et la preuve |
| mécanisme proposé | décrire comment la variable pourrait produire l’écart |
| prédiction | annoncer ce qui devrait changer si l’hypothèse est vraie |
| falsification | définir un résultat qui réfuterait l’hypothèse |
| variable manipulée | changer une seule dimension ou justifier le couplage |
| contrôle | conserver un témoin, une version saine ou un scénario négatif |
| répétitions | enregistrer résultats et conditions, y compris les échecs |
| risque | prévoir sauvegarde, rollback, confinement et confidentialité |
| conclusion | confirmé, réfuté, non concluant ou bloqué |
| suite | nouvelle hypothèse, collecte ou escalade |

**Réponse rapide :** une hypothèse utile est falsifiable. « Le moteur est cassé » n’indique ni variable, ni prédiction, ni contrôle ; « le cache importé de la révision A est incompatible avec le preset B » peut être comparé sur une copie et une réimportation contrôlée selon le [chapitre 28 du Livre III](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#1-rôle-du-chapitre).

**Diagramme compact :** `preuve actuelle → mécanisme → prédiction → variable unique → contrôle → résultat → confirmer, réfuter ou rester inconclusif`.

**Anti-biais :** noter les résultats contraires, rechercher une explication alternative et éviter de modifier simultanément version, configuration, données et matériel.

---

<!-- l5:card -->
## DIAG-08 — Cause confirmée, contournement, correction et vérification

| Élément | Critère minimal | Statut interdit |
|---|---|---|
| cause confirmée | relation isolée, reproduction, contrôle inverse ou source officielle exactement applicable | « probablement » présenté comme certitude |
| périmètre | versions, plateformes, configurations et données affectées | généralisation non testée |
| contournement | réduit l’impact, réversible, limites et retrait connus | « résolu » |
| correction | cible la cause, revue, rollback et migration éventuelle | déploiement sans preuve |
| vérification | scénario original et cas réduit réussissent sur le build corrigé | simple compilation |
| non-régression | test, fixture, oracle et suite appropriée | test qui ne reproduisait jamais le défaut |
| surveillance | signal borné permettant de détecter un retour | collecte permanente non gouvernée |
| fermeture | preuves, réserves, propriétaire, versions et conditions de réouverture | fermeture au seul commit |

**Réponse rapide :** la stratégie QA du [chapitre 2](../Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md#1-rôle-du-chapitre) possède les portes et dérogations ; les [tests fonctionnels](../Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md#1-rôle-du-chapitre) possèdent la non-régression ; le [chapitre 4](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#6-cycle-de-vie-dune-anomalie) possède fermeture et réouverture.

**Diagramme compact :** `cause bornée → correctif réversible → build identifié → scénario original → cas réduit → suite de régression → décision → surveillance et réouverture`.

**Limite :** un contournement peut être acceptable temporairement, mais il conserve une date, un propriétaire, un risque résiduel et une condition de retrait.

---

<!-- l5:card -->
## DIAG-09 — Index outils, dépendances et CI

<!-- qa:error-correction-index -->

| Symptôme ou message | Première vérification | Causes possibles | Source de correction |
|---|---|---|---|
| commande introuvable | shell, `PATH`, version et nouvelle session | outil absent, mauvais shell, chemin non rechargé | [PowerShell et outils Windows](../Livre-I/CHAPITRE-02-Terminal-PowerShell-et-outils-Windows.md#2-terminal-console-et-shell) |
| mauvais paquet installé | identifiant exact, source et éditeur | recherche ambiguë, source différente | [WinGet](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#outil-02--winget) |
| Git refuse une opération | état, branche, index, conflit et remote | travail local non commité, divergence, permission | [Git et GitHub](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md#1-rôle-de-git-dans-le-projet) |
| Python importe le mauvais paquet | interpréteur, environnement, `sys.path` et verrou | environnement global, terminal ancien, dépendance transitive | [Python et environnements isolés](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#outil-06--python-lanceur-py-et-uv) |
| résolution de dépendances impossible | versions, marqueurs, index et lockfile | contraintes incompatibles, paquet indisponible | [backends IA](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md) |
| modèle ou poids absent | manifeste, chemin, révision et licence | téléchargement incomplet, cache différent, composant oublié | [contrat des modèles audio](CHAPITRE-07-Fiches-des-modeles-audio.md#audio-00--contrat-dun-paquet-audio) |
| service conteneur inaccessible | état, ports, réseau, volume et healthcheck | service arrêté, port occupé, réseau incorrect | [Docker et WSL](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#outil-07--docker-desktop-wsl-2-et-compose) |
| Godot ouvre un autre projet | chemin, `project.godot`, version et arguments | répertoire courant, association, cache éditeur | [Godot](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#outil-08--godot-engine) |
| workflow CI vert mais artefact absent | step d’upload, conditions, nom et rétention | chemin vide, job sauté, permission | [DevOps et CI](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#1-rôle-du-chapitre) |
| workflow CI échoue seulement à distance | OS, shell, secrets, cache et permissions | différence d’environnement, token ou chemin | [GitHub Actions](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#outil-04--github-et-github-actions) |
| validation documentaire casse un lien | chemin relatif, casse, extension et fragment | renommage, ancre modifiée, fichier absent | [protocole des fiches](QA/PROTOCOLE-FICHES-LIVRE-V.md#6-politique-de-liens-internes) |
| cache nettoyé puis problème disparu | conserver l’état antérieur si possible | cache obsolète, mais cause non isolée | enregistrer comme corrélation et reproduire sur copie |

**Décision :** privilégier une commande de version, un manifeste ou un état lisible avant une réinstallation. La suppression globale de caches et environnements est une expérience destructive qui exige sauvegarde et hypothèse.

---

<!-- l5:card -->
## DIAG-10 — Index données, assets et runtime

| Symptôme | Première vérification | Causes possibles | Source de correction |
|---|---|---|---|
| JSON ou YAML refusé | encodage, syntaxe, schéma et champ inconnu | virgule, indentation, type, version | [formats d’échange](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md) |
| migration SQLite échoue | version courante, transaction, sauvegarde et contrainte | ordre de migration, donnée incompatible, verrou | [schémas SQLite](CHAPITRE-14-Schemas-SQLite-et-migrations.md) |
| sauvegarde chargée mais état incorrect | schéma, build, fixture, invariant et diff | migration partielle, sérialisation, contenu différent | [sauvegardes et reprise](../Livre-IV/CHAPITRE-15-Sauvegardes-migrations-et-reprise-apres-incident.md#1-rôle-du-chapitre) |
| ressource Godot manquante | UID, chemin, casse, import et dépendances | renommage, export incomplet, cache | [importation Godot](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#1-rôle-du-chapitre) |
| asset déformé ou mal orienté | unités, axes, origine, rig et transform | convention source, export, import | [référence graphique](CHAPITRE-18-Reference-graphique-et-3D.md) |
| matériau incorrect | textures, espace couleur, canaux et preset | sRGB/linéaire, ORM, normal map | [textures et PBR](../Livre-III/CHAPITRE-16-Textures-materiaux-et-pipeline-PBR.md#1-rôle-du-chapitre) |
| animation glisse ou casse | rest pose, BoneMap, racine et retargeting | rig incompatible, échelle, mapping | [rigging](../Livre-III/CHAPITRE-19-Rigging-et-skinning.md#1-rôle-du-chapitre) |
| son absent ou masqué | stream, bus, gain, priorité et distance | import, bus muet, atténuation, concurrence | [diagnostics audio](CHAPITRE-19-Reference-audio.md#audr-12--symptômes-diagnostics-et-acceptation) |
| boucle audio clique | limites en échantillons, encode et import | discontinuité, padding, phase | [boucles audio](CHAPITRE-19-Reference-audio.md#audr-05--boucles-régions-transitions-et-variantes) |
| scène fonctionne isolée mais pas intégrée | dépendances, ordre `_ready`, autorité et état global | couplage, Autoload, signal ou ressource | [patrons d’architecture](CHAPITRE-16-Patrons-d-architecture.md) |
| gameplay diverge après chargement | événement, état canonique et ordre d’application | présentation autoritaire, migration, duplication | [patrons de gameplay](CHAPITRE-17-Patrons-de-gameplay.md) |
| défaut artistique sans erreur technique | critères, références, contexte et revue | décision esthétique, éclairage, mix ou lisibilité | [validation des assets](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md#1-rôle-du-chapitre) |

**Décision :** suivre la chaîne `source → dérivé → export → import → intégration → scène → build`. Corriger le premier maillon confirmé et régénérer les dérivés ; ne jamais éditer un cache importé comme source canonique.

---

<!-- l5:card -->
## DIAG-11 — Index performance, réseau et livraison

| Symptôme | Première vérification | Causes possibles | Source de correction |
|---|---|---|---|
| frame lente côté CPU | capture, scène, build, thread et intervalle | boucle, script, physique, synchronisation | [profilage CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md#1-rôle-du-chapitre) |
| GPU saturé ou artefact | renderer, résolution, capture, pilote et passe | shader, overdraw, bande passante, pilote | [profilage GPU](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md#1-rôle-du-chapitre) |
| mémoire croît | compteur, snapshots, durée et scénario | fuite, cache non borné, ressource retenue | [RAM, VRAM et allocations](../Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md#1-rôle-du-chapitre) |
| chargement bloque | trace, stockage, taille, dépendances et thread | ressource synchrone, compression, fragmentation | [chargements et streaming](../Livre-IV/CHAPITRE-09-Chargements-streaming-et-gestion-des-ressources.md#1-rôle-du-chapitre) |
| optimisation change le comportement | oracle, build témoin et configuration | suppression d’invariant, ordre différent | [optimisation des systèmes](../Livre-IV/CHAPITRE-10-Optimisation-des-scenes-scripts-et-systemes-de-jeu.md#1-rôle-du-chapitre) |
| client et serveur divergent | tick, autorité, séquence, prédiction et correction | ordre, perte, horloge, ownership | [synchronisation réseau](../Livre-IV/CHAPITRE-12-Synchronisation-autorite-et-prediction.md#1-rôle-du-chapitre) |
| serveur refuse une action | identité, permission, validation et journal | règle serveur, token, anti-abus | [serveurs dédiés](../Livre-IV/CHAPITRE-13-Serveurs-dedies-et-securite-reseau.md#1-rôle-du-chapitre) |
| export démarre puis échoue | preset, template, dépendances et espace | ressource absente, permission, outil | [exports et packaging](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md#1-rôle-du-chapitre) |
| build installé diffère de l’artefact | hash, signature, canal et manifeste | mauvais artefact, cache CDN, packaging | [publication](../Livre-IV/CHAPITRE-17-Publication-et-distribution.md#1-rôle-du-chapitre) |
| mise à jour casse une sauvegarde | matrice de versions, migration et rollback | incompatibilité de schéma, ordre ou contenu | [correctifs et retour arrière](../Livre-IV/CHAPITRE-20-Correctifs-mises-a-jour-et-retour-arriere.md#1-rôle-du-chapitre) |
| résultat varie entre machines | matériel, pilotes, température, cache et répétitions | environnement, non-déterminisme, protocole | [plan de la fiche 21](../plans/LIVRE-V-PLAN-MAITRE.md#chapitre-21--benchmarks-et-méthodes-de-mesure) |
| support annoncé mais non reproduit | matrice, version, source et date | support expérimental, option, plateforme | [plan de la fiche 22](../plans/LIVRE-V-PLAN-MAITRE.md#chapitre-22--matrices-de-compatibilité) |

**Décision :** performance et compatibilité exigent des protocoles datés. Une valeur isolée, une seule machine ou un seul run ne devient pas une propriété générale du produit.

---

<!-- l5:matrix -->
## Matrice C — Niveaux de preuve et portes de promotion

| Niveau | Preuve minimale | Déclaration permise | Déclaration interdite |
|---|---|---|---|
| signal reçu | message ou observation attribuée | un signal existe | anomalie confirmée |
| observation qualifiée | attendu, observé, contexte et impact | écart décrit dans ce cas | cause |
| reproduction locale | tentative positive et environnement | symptôme reproduit localement | universalité |
| reproduction indépendante | autre exécuteur ou script | dossier suffisamment explicite | cause confirmée |
| cas réduit | actions ou données minimisées | dépendances nécessaires au cas observé | minimum global |
| hypothèse soutenue | mécanisme, prédiction et indices | explication plausible | causalité démontrée |
| cause probable | plusieurs preuves convergentes | priorité d’investigation justifiée | fermeture définitive |
| cause confirmée | variable isolée et contrôle inverse ou source exactement applicable | cause bornée aux versions et conditions | absence d’autres causes |
| contournement vérifié | impact réduit selon scénario | usage temporaire dans son périmètre | résolution |
| correction vérifiée | scénario original et réduit réussissent | défaut corrigé sur le build testé | absence de régression ailleurs |
| non-régression protégée | test, oracle, fixture et suite | retour détectable dans cette couverture | impossibilité de retour |
| décision de fermeture | propriétaire, preuves, réserves et réouverture | clôture du cas défini | validité éternelle |

**Décision :** le niveau `static-review` de cette fiche couvre la cohérence documentaire et les liens. Aucun signal, cas, reproduction, hypothèse, cause, contournement, correction ou test réel n’est promu.

---

<!-- l5:card -->
## DIAG-12 — Maintenance, doublons, versions et retrait

| Opération | Règle |
|---|---|
| créer | vérifier qu’aucune entrée canonique ne couvre déjà le même concept et les mêmes versions |
| relier | conserver le rapport original et ses preuves même lorsqu’il devient lié ou doublon |
| fusionner | exiger même cause confirmée ou décision explicite ; ne pas fusionner sur le seul message |
| scinder | séparer lorsque plateformes, versions, mécanismes ou corrections divergent |
| versionner | enregistrer début, fin, outil, build, plateforme et statut de chaque solution |
| corriger | pointer vers le propriétaire et le test ; éviter de copier une procédure longue |
| déprécier | indiquer la solution de remplacement, la raison et la date |
| retirer | conserver un tombstone, les alias et la destination canonique |
| réouvrir | appliquer les conditions documentées du défaut ou une nouvelle preuve contradictoire |
| réviser | revalider liens, fragments, versions, sécurité et niveaux de certitude |
| mesurer | envoyer les protocoles chiffrés vers la fiche 21 sans incorporer des moyennes orphelines |
| publier | distinguer index documentaire, outil exécutable du Companion Pack et données de production |

**Réponse rapide :** la [politique de doublons](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#35-signature-de-doublon) préserve les preuves secondaires. Une entrée ancienne reste utile pour ses versions, mais elle ne doit pas apparaître comme solution courante après dépréciation.

**Diagramme compact :** `nouveau signal → recherche d’alias → entrée canonique ou création → versionnement → preuve → correction propriétaire → dépréciation ou retrait → tombstone`.

**Profil Solo :** privilégier un catalogue court, des identifiants stables et des renvois directs ; documenter les inconnues plutôt que multiplier les fiches spéculatives.

**Profil Studio :** ajouter propriétaire, SLA de triage, revue sécurité, matrice de versions, synchronisation issue/catalogue, politique de données et historique de décisions.

**Limite de périmètre :** les commandes exécutables de collecte, fixtures permanentes, extracteurs de logs et interfaces de recherche appartiennent au futur Companion Pack. La présente fiche reste documentaire.

---

## Limites générales

- aucun défaut, incident, crash, message, log, métrique, trace, dump, capture, vidéo ou sauvegarde réelle n’a été collecté ;
- aucune commande, installation, réinstallation, suppression de cache, migration, export, import ou restauration n’a été exécutée ;
- aucune reproduction locale, indépendante, scriptée, réduite, A/B ou multi-plateforme n’a été menée ;
- aucune hypothèse, cause, corrélation, signature de doublon, contournement ou correction réelle n’est déclarée ;
- aucun test de non-régression, benchmark, profilage, test réseau, test de livraison ou décision de fermeture n’a été produit ;
- aucune donnée joueur, donnée personnelle, secret, token, contrat, voix, dump mémoire ou artefact confidentiel n’a été utilisé ;
- aucune source officielle externe n’a été revue spécialement pour un message volatil dans cette fiche ; les propriétaires restent la source de vérité ;
- aucun PDF n’a été produit.

## Synthèse de consultation

Partir du signal brut, préserver l’environnement, séparer attendu et observé, reproduire puis réduire avant d’attribuer une cause. Utiliser les journaux, métriques, traces et sources officielles comme preuves bornées ; falsifier les hypothèses avec une variable contrôlée ; distinguer contournement, correction et vérification ; enfin protéger la correction par non-régression et maintenir le catalogue selon les versions. Toute conclusion reste limitée à son dossier de preuve.