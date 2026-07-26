---
title: "Audit post-création — Livre IV, chapitre 11"
id: "DOC-L4-QA-AUDIT-CH11"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L4-CH11"
chapter-version: "1.0.0"
audit-date: "2026-07-26T16:42:00+02:00"
last-verified: "2026-07-26T16:42:00+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 11

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de matérialisation du prototype de connexion, du lobby, de la découverte, de la reconnexion, des campagnes réseau et du modèle de coûts.

Aucun serveur, pair ENet exécuté, session, lobby, ticket, campagne de latence, coût qualifié ou validation de sécurité de `Project Asteria` n’est revendiqué comme produit.

## 2. Périmètre comparé au plan maître

Le chapitre couvre les objectifs du plan maître :

- choix entre client-serveur, pair-à-pair et hybride ;
- sessions, lobby, découverte et reconnexion ;
- séparation de la simulation locale et de l’autorité réseau ;
- protocoles, versions et capacités ;
- coûts et risques.

Les livrables sont préparés comme contrats : diagramme réseau, contrat de session, prototype de connexion, matrice de risques et stratégie Solo/Studio.

## 3. Frontières contrôlées

- le chapitre 10 conserve l’optimisation des scènes et systèmes actifs ;
- le chapitre 11 possède la topologie, la session, le lobby, la découverte, les identités temporaires et la reconnexion ;
- le chapitre 12 conserve réplication, interpolation, prédiction, rollback et qualité sous latence ou perte ;
- le chapitre 13 conserve serveur dédié, exposition publique, authentification de production, secrets, pare-feu et durcissement ;
- l’identifiant de pair ne devient ni identité durable ni droit ;
- la découverte ne devient ni admission ni autorité ;
- la réussite d’un workflow documentaire ne devient pas une preuve runtime.

## 4. Contrôles pédagogiques

- client-serveur, serveur d’écoute, serveur dédié, pair-à-pair et hybride comparés ;
- décision client-serveur autoritaire enregistrée pour `Project Asteria` ;
- diagramme réseau et frontières applicatives documentés ;
- identités durable, de membre, de pair et de ticket distinguées ;
- contrat de session, machine à états et enveloppe versionnée préparés ;
- compatibilité majeure, mineure, capacités et révision de contenu encadrées ;
- création serveur et client ENet expliquée sans confondre création et connexion ;
- signaux de cycle de vie et fermeture hors ligne documentés ;
- lobby, révisions, commandes, résultats et limites structurés ;
- découverte directe, LAN, invitation et rendez-vous séparés ;
- reconnexion par nouveau pair, ticket, rotation, génération et backoff encadrée ;
- départ volontaire, coupure, expulsion et fermeture distingués ;
- autorité réseau maintenue au serveur sans anticiper la réplication détaillée ;
- adaptateur hors ligne préparé pour préserver le chemin Solo ;
- migration d’hôte désactivée jusqu’à preuve complète ;
- plan de test, profils réseau, journalisation, risques et coûts préparés ;
- modes Solo et Studio documentés sans bloc de code ;
- dix diagnostics suivent la séquence sémantique complète ;
- références techniques présentées sous forme de liens Markdown cliquables ;
- synthèse opérationnelle `Project Asteria` présente.

## 5. Contrôles documentaires

- lignes : 2065 ;
- titres : 64 ;
- blocs de code ou données : 59 ;
- blocs significatifs : 56 ;
- marqueurs d’explication : 59 ;
- explications structurées hors diagnostics : 39 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- exemples corrigés expliqués : 10 ;
- titres dupliqués : 0 ;
- blocs significatifs dupliqués : 0 ;
- paragraphes longs dupliqués : 0 ;
- section Solo/Studio en Markdown ordinaire ;
- absence de recommandation GPT, de prochaine action et de chaîne d’export du guide dans le texte lecteur.

## 6. Exactitude technique

Le chapitre distingue le retour immédiat de `ENetMultiplayerPeer.create_client()` et `create_server()` des signaux asynchrones de `MultiplayerAPI`. Il fixe explicitement l’adresse de liaison du prototype local, restaure `OfflineMultiplayerPeer` à la fermeture et traite l’identifiant de pair comme temporaire.

Il documente les signaux `peer_connected`, `peer_disconnected`, `connected_to_server`, `connection_failed` et `server_disconnected`, ainsi que la propriété `multiplayer_peer`. L’autorité serveur reste un contrat applicatif ; aucune RPC de réplication, interpolation ou prédiction n’est revendiquée.

La reconnexion crée un nouveau pair, utilise un ticket opaque limité, fait tourner ce ticket après réussite et rejette toute complétion dont la génération ne correspond plus à la tentative courante.

## 7. Contrôle des régressions

- le mode hors ligne conserve le même port applicatif ;
- session et lobby possèdent des états finis ;
- version de protocole et révision de contenu sont des portes distinctes ;
- commandes de lobby, révision et idempotence sont séparées ;
- tailles, débits et files possèdent des bornes ;
- coupure, départ et expulsion ont des politiques différentes ;
- migration d’hôte reste fermée sans preuve contre le double hôte ;
- chaque cas de connexion possède un oracle et un résultat `pending` ;
- coûts et risques possèdent des propriétaires à compléter ;
- rollback révoque les tickets candidats et revalide le chemin hors ligne.

## 8. Réserves ouvertes

- prototype ENet non matérialisé ;
- serveur d’écoute non exécuté ;
- serveur dédié non construit ;
- lobby non intégré ;
- découverte LAN non exécutée ;
- service d’invitation ou de rendez-vous non matérialisé ;
- mécanisme d’admission non exécuté ;
- tickets de jonction et de reconnexion non implémentés ;
- reconnexion, rotation et génération non testées ;
- aucune campagne de connexion, coupure ou reprise réalisée ;
- aucune campagne de latence, jitter ou perte réalisée ;
- aucun seuil de grâce ou de backoff qualifié ;
- migration d’hôte non implémentée ;
- modèle de coûts non rempli par des devis ;
- risques non revus avec sécurité et exploitation ;
- aucun test fonctionnel réseau exécuté ;
- aucun durcissement ou test d’exposition publique exécuté ;
- licence globale de collection non définie ;
- balisage d’accessibilité de l’export final toujours ouvert.

## 9. Conclusion

Le chapitre satisfait le périmètre du plan maître au niveau documentaire et statique. Les contrôles du dépôt doivent confirmer la structure, les repères, les explications et les frontières avant fermeture de la preuve QA.
