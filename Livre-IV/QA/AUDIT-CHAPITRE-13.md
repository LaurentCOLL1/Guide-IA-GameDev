---
title: "Audit post-création — Livre IV, chapitre 13"
id: "DOC-L4-QA-AUDIT-CH13"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L4-CH13"
chapter-version: "1.0.0"
audit-date: "2026-07-26T17:45:00+02:00"
last-verified: "2026-07-26T17:45:00+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 13

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de production du build dédié, de provisionnement de l’hôte, d’application du pare-feu, de démarrage du service, de construction du conteneur, d’exécution des campagnes d’admission et d’abus, de scan autorisé et d’exercice d’incident.

Aucun serveur public, règle pare-feu, service systemd, conteneur, secret, ticket, scan, attaque simulée, restauration ou résultat de durcissement de `Project Asteria` n’est revendiqué comme produit.

## 2. Périmètre comparé au plan maître

Le chapitre couvre les objectifs du plan maître :

- produire un build serveur et un manifeste d’artefact ;
- déployer, configurer, superviser, drainer et arrêter ;
- protéger secrets, ports, identités système et permissions ;
- limiter tailles, rejeux, cadences, concurrence et amplification ;
- gérer mises à jour, rollback, rotations et incidents.

Les livrables sont préparés comme contrats : configuration serveur, scripts de déploiement, règles pare-feu, procédures d’incident et matrice de tests de durcissement.

## 3. Frontières contrôlées

- le chapitre 11 conserve sessions, lobby, découverte, admission fonctionnelle et reconnexion ;
- le chapitre 12 conserve réplication, prédiction, rollback gameplay et budgets de bande passante ;
- le chapitre 13 possède exploitation, secrets, pare-feu, identité de service, limites anti-abus et incidents ;
- le chapitre 14 conserve CI/CD générale, matrices de plateformes, branches, tags et publication automatisée ;
- le chapitre ne constitue ni audit professionnel, ni test d’intrusion, ni certification ;
- tout scan futur exige cible isolée, autorisation écrite et périmètre déclaré ;
- aucune validation documentaire ne devient une preuve runtime.

## 4. Contrôles pédagogiques

- export dédié, tag `dedicated_server`, `--headless` et argument utilisateur distingués ;
- serveur séparé du rôle de joueur local ;
- manifeste d’artefact et empreinte documentés sans les confondre avec une signature ;
- configuration, credentials, état durable et code installés dans des zones distinctes ;
- `OS.has_environment()` et lecture bornée de credentials encadrées ;
- écoute ENet UDP, interface, port et capacité configurés explicitement ;
- règles pare-feu Windows et Linux ciblées par protocole et port ;
- unité systemd avec identité dédiée, écriture limitée et familles réseau bornées ;
- conteneur non root, lecture seule, capabilities retirées et ressources plafonnées ;
- liveness, readiness, admission et drainage séparés ;
- `SceneMultiplayer.auth_callback`, `auth_timeout`, `complete_auth()` et `allow_object_decoding=false` documentés ;
- tickets à audience, expiration et nonce préparés ;
- tailles, fenêtres anti-rejeu, quotas et concurrence bornés ;
- réponses, journaux et métriques protégés contre amplification et cardinalité ;
- arrêt gracieux, sauvegarde fermée, releases immuables et rollback documentés ;
- porte de promotion, matrice de tests, sévérités, runbook et rotation préparés ;
- modes Solo et Studio documentés sans bloc de code ;
- dix diagnostics suivent la séquence sémantique complète ;
- références techniques sous forme de liens Markdown cliquables ;
- synthèse opérationnelle `Project Asteria` présente.

## 5. Contrôles documentaires

- lignes : 1839 ;
- titres : 67 ;
- blocs de code ou données : 66 ;
- blocs significatifs provisoires : 50 ;
- marqueurs d’explication : 66 ;
- explications structurées hors diagnostics : 46 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- exemples corrigés expliqués : 10 ;
- titres dupliqués : 0 ;
- blocs significatifs dupliqués : 0 ;
- paragraphes longs dupliqués : 0 ;
- section Solo/Studio en Markdown ordinaire ;
- absence de recommandation GPT, de prochaine action et de chaîne d’export du guide dans le texte lecteur.

## 6. Exactitude technique

Le chapitre respecte le mode d’export dédié de Godot, le tag `dedicated_server`, le démarrage `--headless`, les arguments utilisateur et l’usage d’un export template plutôt que de l’éditeur pour l’exploitation. Il distingue `export_presets.cfg` des credentials d’export non versionnables.

Il documente qu’ENet utilise UDP, applique `set_bind_ip()` avant `create_server()`, et maintient le pare-feu aligné sur le protocole. Il utilise le mécanisme d’authentification de `SceneMultiplayer`, appelle `complete_auth()` après validation et conserve le décodage d’objets désactivé pour les sources non fiables.

La supervision Linux active le flush stdout adapté à journald, utilise une identité dédiée, des chemins d’écriture explicitement autorisés et des credentials runtime. Le profil conteneur ne requiert ni root, ni `--privileged`, ni capabilities supplémentaires.

## 7. Contrôle des régressions

- le chemin client ne démarre pas silencieusement un serveur public ;
- le serveur dédié ne devient pas un joueur ;
- aucun secret n’est requis dans le dépôt ou le PCK ;
- l’absence de configuration ou credential ferme le bootstrap ;
- seul le port UDP déclaré est exposé ;
- l’administration reste séparée du protocole gameplay ;
- les commandes clientes restent des intentions validées par le domaine ;
- les objets sérialisés distants restent refusés ;
- admission, rejeu, cadence, concurrence et taille possèdent des bornes ;
- journaux et métriques ne contiennent pas d’identifiants sensibles bruts ;
- drainage et arrêt gracieux possèdent une échéance ;
- état et build sont versionnés séparément ;
- rollback vérifie la compatibilité de lecture ;
- une alerte ou un scan n’est pas une certification ;
- l’approbation finale reste humaine.

## 8. Réserves ouvertes

- preset serveur non configuré dans le projet ;
- build dédié et manifeste non produits ;
- hôte isolé non provisionné ;
- compte de service et permissions non créés ;
- credentials runtime non installés ni tournés ;
- règle pare-feu Windows non appliquée ;
- politique nftables non appliquée ;
- unité systemd non installée ni démarrée ;
- image et exécution conteneur non produites ;
- liveness et readiness non qualifiées ;
- admission et authentification non exécutées ;
- tickets et nonces non matérialisés ;
- quotas, fenêtres et plafonds non qualifiés ;
- journaux et métriques non collectés ;
- état durable, sauvegarde et restauration non testés ;
- drainage, arrêt, mise à jour et rollback non répétés ;
- tests de durcissement non exécutés ;
- scan de sécurité autorisé non réalisé ;
- exercice d’incident et rotation de secrets non réalisés ;
- aucune évaluation professionnelle de sécurité réalisée ;
- licence globale de collection non définie ;
- balisage d’accessibilité de l’export final toujours ouvert.

## 9. Conclusion

Le chapitre satisfait le périmètre du plan maître au niveau documentaire et statique. Les contrôles du dépôt doivent confirmer structure, repères, explications, frontières et absence de sortie documentaire intermédiaire avant fermeture de la preuve QA.
