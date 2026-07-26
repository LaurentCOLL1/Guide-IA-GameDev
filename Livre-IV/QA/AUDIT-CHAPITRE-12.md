---
title: "Audit post-création — Livre IV, chapitre 12"
id: "DOC-L4-QA-AUDIT-CH12"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L4-CH12"
chapter-version: "1.0.0"
audit-date: "2026-07-26T17:30:00+02:00"
last-verified: "2026-07-26T17:30:00+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 12

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de matérialisation du modèle de réplication, des protocoles de messages, de l’interpolation, de la prédiction, du rollback, des outils de comparaison et des campagnes sous altérations réseau.

Aucun serveur, synchroniseur, spawner, snapshot, prédiction, rollback, campagne de latence ou gain de bande passante de `Project Asteria` n’est revendiqué comme produit.

## 2. Périmètre comparé au plan maître

Le chapitre couvre les objectifs du plan maître :

- synchronisation des états et événements ;
- autorité, interpolation et extrapolation ;
- prédiction client, réconciliation et rollback ;
- réduction et budgétisation de la bande passante ;
- diagnostic des désynchronisations et validation des commandes clientes.

Les livrables sont préparés comme contrats : modèle de réplication, protocoles de messages, profils de latence/perte, outils de comparaison d’état et rapport de compromis.

## 3. Frontières contrôlées

- le chapitre 11 conserve topologie, session, lobby, découverte, admission et reconnexion ;
- le chapitre 12 possède autorité détaillée, commandes, événements, snapshots, pertinence, interpolation, prédiction, réconciliation et rollback ;
- le chapitre 13 conserve serveur dédié, authentification de production, secrets, pare-feu, permissions et durcissement ;
- l’autorité réseau ne devient pas une permission métier ;
- la présentation interpolée ou prédite ne devient pas un état autoritaire ;
- un outil de comparaison ou une empreinte ne devient pas une preuve automatique de triche ;
- aucune validation documentaire ne devient une preuve runtime.

## 4. Contrôles pédagogiques

- commande, événement, snapshot, delta, acquittement, interpolation, extrapolation, prédiction, réconciliation et rollback définis ;
- registre d’autorité et attribution par nœud documentés ;
- RPC `any_peer`, émetteur distant, séquences et validation serveur encadrés ;
- snapshots complets, deltas et bases manquantes distingués ;
- `SceneReplicationConfig`, modes `ALWAYS` et `ON_CHANGE` expliqués ;
- `MultiplayerSynchronizer`, intervalles et visibilité par pair encadrés ;
- `MultiplayerSpawner`, `spawn_function`, `spawn_path` et limite documentés ;
- pertinence spatiale, hystérésis et budget de visibilité préparés ;
- modes de transfert et canaux séparés par sémantique ;
- événements fiables, idempotence et fenêtres de séquences documentés ;
- interpolation, extrapolation, prédiction et réconciliation structurées ;
- rollback, anneau d’états, RNG local et ordre déterministe encadrés ;
- compensation de latence historique bornée ;
- budgets de bande passante, quantification et adaptation préparés ;
- empreintes, comparateur Python et captures expurgées documentés ;
- profils de latence, jitter, perte, duplication et réordonnancement préparés ;
- porte de validation, rapport de compromis et rollback de livraison documentés ;
- modes Solo et Studio documentés sans bloc de code ;
- dix diagnostics suivent la séquence sémantique complète ;
- références techniques sous forme de liens Markdown cliquables ;
- synthèse opérationnelle `Project Asteria` présente.

## 5. Contrôles documentaires

- lignes : 2180 ;
- titres : 67 ;
- blocs de code ou données : 65 ;
- blocs significatifs : 57 ;
- marqueurs d’explication : 65 ;
- explications structurées hors diagnostics : 45 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- exemples corrigés expliqués : 10 ;
- titres dupliqués : 0 ;
- blocs significatifs dupliqués : 0 ;
- paragraphes longs dupliqués : 0 ;
- section Solo/Studio en Markdown ordinaire ;
- absence de recommandation GPT, de prochaine action et de chaîne d’export du guide dans le texte lecteur.

## 6. Exactitude technique

Le chapitre distingue `@rpc("any_peer")` d’une validation métier et lit l’émetteur avec `multiplayer.get_remote_sender_id()`. Il conserve des `NodePath` et noms déterministes, sépare les canaux fiables et non fiables, et traite les séquences au niveau applicatif.

Il documente que `SceneReplicationConfig.REPLICATION_MODE_ALWAYS` utilise des mises à jour non fiables, tandis que `REPLICATION_MODE_ON_CHANGE` fiabilise les changements. Il exclut des propriétés synchronisées les `Object`, `Resource`, identifiants d’instance et `RID`.

Il respecte le contrat de `MultiplayerSpawner.spawn_function` : le nœud retourné reste hors arbre et l’ajout est automatique. La visibilité du synchroniseur reste une décision de réplication, pas une autorité d’existence ou de gameplay.

## 7. Contrôle des régressions

- le chemin Solo conserve le même port de simulation ;
- les commandes clientes restent des intentions bornées ;
- l’état autoritaire possède tick, séquence et provenance ;
- les événements fiables sont idempotents ;
- une base de delta absente déclenche une resynchronisation ;
- interpolation et correction visuelle ne modifient pas collision ni règles ;
- extrapolation, historique de prédiction et rollback sont bornés ;
- les budgets CPU, mémoire et bande passante restent des portes indépendantes ;
- les profils d’altération possèdent des oracles fonctionnels et de cohérence ;
- les divergences ouvrent un diagnostic avant toute conclusion ;
- le rollback de livraison restaure une baseline autoritaire simple ;
- l’approbation finale reste humaine.

## 8. Réserves ouvertes

- modèle de réplication non intégré ;
- protocoles de commandes, événements et snapshots non exécutés ;
- synchroniseurs et spawners non configurés dans le projet ;
- profils de pertinence non qualifiés ;
- canaux et modes de transfert non mesurés ;
- interpolation et extrapolation non exécutées ;
- prédiction et réconciliation non intégrées ;
- rollback non implémenté ni mesuré ;
- compensation de latence non exécutée ;
- budget de bande passante non rempli ;
- quantification non qualifiée ;
- outil de comparaison d’état non exécuté ;
- captures réseau non produites ;
- campagne de latence, jitter, perte, duplication ou réordonnancement non réalisée ;
- tests fonctionnels réseau non exécutés ;
- revue anti-abus et sécurité non réalisée ;
- serveur dédié et durcissement réservés au chapitre 13 ;
- licence globale de collection non définie ;
- balisage d’accessibilité de l’export final toujours ouvert.

## 9. Conclusion

Le chapitre satisfait le périmètre du plan maître au niveau documentaire et statique. Les contrôles du dépôt ont confirmé la structure, les repères, les explications, les frontières et l’absence de sortie documentaire intermédiaire ; la preuve QA peut être fermée avec les réserves déclarées.
