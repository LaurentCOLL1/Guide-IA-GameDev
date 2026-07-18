---
title: "Plan maître détaillé — Livre IV"
id: "DOC-PLAN-L4"
status: "active"
version: "1.0.0"
lang: "fr-FR"
last-updated: "2026-07-18"
book: "Livre IV"
chapter-count: 22
---

# Plan maître détaillé — Livre IV

> **Titre du Livre :** Finalisation, optimisation, publication et maintenance  
> **Statut :** non commencé  
> **Rôle :** transformer un projet fonctionnel en produit testable, performant, publiable, maintenable et récupérable après incident.

## Règles transversales du Livre IV

Chaque chapitre doit produire des preuves mesurables, distinguer environnement de développement et production, documenter les risques et inclure procédures de retour arrière. Toute optimisation doit être précédée d’une mesure et suivie d’une comparaison avant/après.

## Chapitre 1 — Équilibrage et télémétrie locale

**Objectifs**

- définir métriques utiles sans collecte excessive ;
- modéliser courbes de progression, économie, combat et difficulté ;
- créer simulations et tableaux de comparaison ;
- distinguer télémétrie locale, tests internes et données joueurs ;
- documenter confidentialité et consentement.

**Livrables**

- catalogue de métriques ;
- tableaux d’équilibrage ;
- scénarios de simulation ;
- rapports de décision ;
- procédure d’anonymisation.

**Frontière et validation**

Le chapitre ne remplace pas les systèmes de gameplay du Livre II. Validation par reproduction d’une décision d’équilibrage à partir de données sourcées.

## Chapitre 2 — Stratégie générale d’assurance qualité

**Objectifs**

- définir niveaux de test, responsabilités et portes qualité ;
- distinguer prévention, détection et correction ;
- organiser risques, priorités et calendrier ;
- définir critères d’entrée et sortie de chaque phase ;
- relier QA documentaire, technique, artistique et produit.

**Livrables**

- stratégie QA ;
- matrice risques/tests ;
- calendrier ;
- rôles Solo/Studio ;
- modèles de rapports.

**Frontière et validation**

Les tests détaillés viennent aux chapitres suivants. Validation par couverture explicite des risques critiques.

## Chapitre 3 — Tests fonctionnels et tests de régression

**Objectifs**

- écrire cas de test reproductibles ;
- créer suites manuelles et automatisées ;
- gérer fixtures, seeds et états contrôlés ;
- définir non-régression ;
- classer tests rapides, complets et de publication.

**Livrables**

- catalogue de cas ;
- scripts et scènes de test ;
- données d’entrée ;
- rapports ;
- matrice de couverture.

**Frontière et validation**

Les tests unitaires de code sont introduits au Livre II ; ici ils sont intégrés à la campagne produit. Validation par détection volontaire d’une régression connue.

## Chapitre 4 — Débogage et reproduction des anomalies

**Objectifs**

- rédiger rapports exploitables ;
- capturer environnement, version, logs, sauvegardes et étapes ;
- réduire un défaut à un cas minimal ;
- prioriser gravité, fréquence et impact ;
- gérer doublons et réouvertures.

**Livrables**

- modèle de bug report ;
- procédure de reproduction ;
- archive diagnostique ;
- politique de triage ;
- exemples corrigés.

**Frontière et validation**

Le chapitre 5 traite la collecte systématique des données. Validation par reproduction indépendante par une seconde personne ou un script.

## Chapitre 5 — Journalisation et observabilité locale

**Objectifs**

- définir niveaux et catégories de logs ;
- ajouter contexte, corrélation et horodatage ;
- distinguer logs, métriques et traces ;
- gérer rotation, taille, confidentialité et export ;
- créer tableaux de bord locaux.

**Livrables**

- politique de logging ;
- format structuré ;
- collecteur local ;
- dashboard ;
- procédure de purge.

**Frontière et validation**

La journalisation ne doit pas exposer secrets ou données personnelles. Validation par diagnostic d’un incident simulé.

## Chapitre 6 — Profilage CPU

**Objectifs**

- utiliser le profiler Godot et outils système ;
- mesurer scripts, physique, navigation, IA et threads ;
- identifier fréquence, durée et appels coûteux ;
- définir budgets par frame ;
- éviter optimisations prématurées.

**Livrables**

- scènes de benchmark ;
- captures de profilage ;
- budget CPU ;
- rapport avant/après ;
- checklist de diagnostic.

**Frontière et validation**

Le chapitre 7 couvre le GPU. Validation par amélioration mesurée sans modification fonctionnelle indésirable.

## Chapitre 7 — Profilage GPU et optimisation du rendu

**Objectifs**

- comprendre passes, draw calls, overdraw et shaders ;
- mesurer lumière, ombres, transparence et post-traitement ;
- surveiller VRAM et bande passante ;
- établir profils de qualité ;
- adapter au GPU AMD de référence.

**Livrables**

- budget GPU ;
- captures de frame ;
- profils graphiques ;
- rapport de coût par effet ;
- scène de stress.

**Frontière et validation**

La production des assets optimisés est au Livre III. Validation par stabilité des FPS et qualité visuelle documentée.

## Chapitre 8 — Optimisation RAM, VRAM et allocations

**Objectifs**

- mesurer consommation et pics ;
- identifier fuites, duplications et caches excessifs ;
- gérer chargement, libération et réutilisation ;
- réduire allocations temporaires ;
- définir limites par plateforme.

**Livrables**

- budgets mémoire ;
- rapport d’allocation ;
- stratégie de cache ;
- tests de longue durée ;
- procédure de diagnostic.

**Frontière et validation**

Le chapitre 9 traite le streaming. Validation par réduction mesurée des pics et absence de régression.

## Chapitre 9 — Chargements, streaming et gestion des ressources

**Objectifs**

- charger en arrière-plan ;
- organiser transitions, préchargement et éviction ;
- gérer zones, chunks et priorités ;
- afficher progression fiable ;
- traiter erreurs et annulation.

**Livrables**

- gestionnaire de chargement ;
- profils de streaming ;
- scènes de transition ;
- tests de disque lent ;
- rapport de temps de chargement.

**Frontière et validation**

Le chapitre ne redéfinit pas le monde ouvert du Livre III. Validation par parcours prolongé sans fuite ni blocage excessif.

## Chapitre 10 — Optimisation des scènes, scripts et systèmes de jeu

**Objectifs**

- réduire fréquences de mise à jour ;
- appliquer pooling, activation par distance et LOD logique ;
- découper scènes et systèmes ;
- optimiser signaux, recherches et allocations ;
- préserver lisibilité et testabilité.

**Livrables**

- catalogue de techniques ;
- benchmarks ;
- exemples avant/après ;
- seuils d’activation ;
- checklist de revue.

**Frontière et validation**

Toute optimisation doit rester justifiée par le profiler. Validation par tests fonctionnels et mesures répétées.

## Chapitre 11 — Architecture multijoueur

**Objectifs**

- choisir modèle client-serveur, pair-à-pair ou hybride ;
- définir sessions, lobby, découverte et reconnexion ;
- séparer simulation locale et autorité réseau ;
- organiser protocoles et versions ;
- évaluer coûts et risques.

**Livrables**

- diagramme réseau ;
- contrat de session ;
- prototype de connexion ;
- matrice de risques ;
- stratégie Solo/Studio.

**Frontière et validation**

Le chapitre 12 détaille synchronisation et prédiction. Validation par connexion, déconnexion et reprise contrôlées.

## Chapitre 12 — Synchronisation, autorité et prédiction

**Objectifs**

- synchroniser états et événements ;
- gérer autorité, interpolation et extrapolation ;
- introduire prédiction client et rollback ;
- réduire bande passante ;
- traiter désynchronisations et triche.

**Livrables**

- modèle de réplication ;
- protocoles de messages ;
- tests de latence/perte ;
- outils de comparaison d’état ;
- rapport de compromis.

**Frontière et validation**

La sécurité serveur est au chapitre 13. Validation sous latence, jitter et perte simulés.

## Chapitre 13 — Serveurs dédiés et sécurité réseau

**Objectifs**

- produire un build serveur ;
- déployer, configurer et superviser ;
- protéger secrets, ports et permissions ;
- limiter abus, injections et dénis de service ;
- gérer incidents et mises à jour.

**Livrables**

- configuration serveur ;
- scripts de déploiement ;
- règles pare-feu ;
- procédures d’incident ;
- tests de durcissement.

**Frontière et validation**

Ne constitue pas un audit de sécurité professionnel. Validation par environnement isolé, scans autorisés et scénarios d’échec.

## Chapitre 14 — DevOps et intégration continue

**Objectifs**

- automatiser builds, tests et packaging ;
- gérer branches, tags, versions et artefacts ;
- protéger secrets ;
- créer matrices de plateformes ;
- conserver logs et preuves.

**Livrables**

- workflows CI/CD ;
- scripts de build ;
- conventions de version ;
- artefacts ;
- procédures de reprise.

**Frontière et validation**

Le chapitre ne remplace pas la stratégie QA. Validation par reconstruction propre depuis un clone neuf.

## Chapitre 15 — Sauvegardes, migrations et reprise après incident

**Objectifs**

- inventorier données critiques ;
- définir RPO, RTO et rétention ;
- sauvegarder sources, builds, bases et services ;
- tester restauration et migrations ;
- documenter scénarios catastrophe.

**Livrables**

- politique de sauvegarde ;
- scripts ;
- inventaire ;
- tests de restauration ;
- plan de continuité.

**Frontière et validation**

Les sauvegardes joueurs sont introduites au Livre II. Ici la portée couvre tout le produit et l’infrastructure. Validation par restauration réelle d’un environnement isolé.

## Chapitre 16 — Exports Godot et packaging

**Objectifs**

- configurer presets par plateforme ;
- gérer dépendances, ressources, icônes et signatures ;
- produire builds debug, test et release ;
- vérifier fichiers inclus/exclus ;
- automatiser packaging et checksums.

**Livrables**

- presets d’export ;
- scripts ;
- packages ;
- manifestes ;
- checklist de build.

**Frontière et validation**

La publication commerciale est au chapitre 17. Validation par installation et lancement sur machine propre.

## Chapitre 17 — Publication et distribution

**Objectifs**

- préparer pages, médias, descriptions et exigences ;
- gérer boutiques, canaux et clés ;
- vérifier licences et conformité ;
- planifier lancement et support ;
- publier builds et notes de version.

**Livrables**

- dossier de publication ;
- checklist boutique ;
- calendrier ;
- builds candidats ;
- plan de support.

**Frontière et validation**

Le marketing approfondi reste hors périmètre principal. Validation par dry-run de soumission et conformité documentaire.

## Chapitre 18 — Accessibilité

**Objectifs**

- couvrir commandes, visuel, audio, cognition et motricité ;
- proposer remapping, sous-titres, contrastes et options de rythme ;
- tester avec profils et utilisateurs ;
- documenter limites connues ;
- intégrer l’accessibilité dès les réglages.

**Livrables**

- matrice d’accessibilité ;
- options ;
- scénarios de test ;
- rapport ;
- déclaration publique.

**Frontière et validation**

L’accessibilité visuelle des assets est introduite au Livre III. Ici la portée est produit complet. Validation par parcours représentatifs.

## Chapitre 19 — Localisation et internationalisation

**Objectifs**

- externaliser chaînes et données culturelles ;
- gérer pluriels, dates, nombres et sens d’écriture ;
- prévoir polices, UI, voix et sous-titres ;
- organiser traduction et relecture ;
- automatiser contrôles de chaînes.

**Livrables**

- catalogue de traduction ;
- conventions ;
- pseudo-localisation ;
- tests de débordement ;
- rapport linguistique.

**Frontière et validation**

La création des voix est au Livre III. Validation par pseudo-langue, langues longues et scripts non latins.

## Chapitre 20 — Correctifs, mises à jour et retour arrière

**Objectifs**

- définir canaux stable, beta et interne ;
- produire patches compatibles ;
- migrer données ;
- vérifier intégrité et reprise ;
- prévoir rollback et communication.

**Livrables**

- stratégie de version ;
- packages de patch ;
- scripts de migration ;
- procédure de rollback ;
- notes de version.

**Frontière et validation**

La distribution initiale est au chapitre 17. Validation par mise à jour depuis plusieurs versions antérieures et retour arrière contrôlé.

## Chapitre 21 — Modding et contenu communautaire

**Objectifs**

- définir surfaces d’extension ;
- créer formats, API et documentation ;
- isoler contenu non fiable ;
- gérer compatibilité, dépendances et versions ;
- traiter licences, modération et support.

**Livrables**

- SDK ou templates ;
- documentation ;
- sandbox ;
- exemple de mod ;
- politique communautaire.

**Frontière et validation**

Le modding ne doit pas exposer secrets ou compromettre les sauvegardes. Validation par installation, désactivation et conflit de mods.

## Chapitre 22 — Maintenance, archivage et pérennité

**Objectifs**

- surveiller dépendances et vulnérabilités ;
- archiver sources, outils, builds et documentation ;
- maintenir reproductibilité ;
- planifier succession, fin de support et ouverture éventuelle ;
- conserver formats lisibles et checksums.

**Livrables**

- calendrier de maintenance ;
- inventaire d’archives ;
- procédures de reconstruction ;
- plan de fin de vie ;
- dossier de succession.

**Frontière et validation**

Ce chapitre clôt le cycle de vie. Validation par reconstruction d’une version historique à partir des archives.

## Critères de clôture du Livre IV

- les 22 chapitres sont rédigés, repérés et audités ;
- les campagnes QA et performance sont reproductibles ;
- un build candidat est exporté, installé et testé ;
- sauvegarde, restauration, mise à jour et rollback ont été exécutés ;
- les exigences d’accessibilité et localisation sont documentées ;
- les procédures de maintenance et archivage sont opérationnelles ;
- le PDF et les preuves finales sont validés.
