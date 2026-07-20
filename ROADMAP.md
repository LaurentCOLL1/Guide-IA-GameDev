# Feuille de route

## M0 — Infrastructure documentaire

- [x] Initialiser le dépôt.
- [x] Créer les index principaux.
- [x] Ajouter les métadonnées Pandoc.
- [x] Définir l'ordre de compilation.
- [x] Ajouter la documentation de contribution et de style.
- [x] Ajouter les scripts de construction multiplateformes.
- [x] Créer `CONTINUITE-PROJET.md` comme document permanent de reprise.
- [x] Rendre sa mise à jour obligatoire dans chaque lot de modifications du projet.
- [x] Enregistrer dans ce document le plan maître détaillé des Livres II à V et du Companion Pack.
- [x] Rendre obligatoire l’annonce du niveau GPT-5.6 Sol conseillé avant chaque chapitre.
- [x] Différer la construction PDF à la fin de chaque Livre et à la fin de la collection.
- [x] Séparer le workflow léger des chapitres du workflow de publication PDF.

**Statut M0 : terminé.**

## M1 — Volume 0 : Fondation documentaire

- [x] Vision générale du projet.
- [x] Les 21 règles fondamentales.
- [x] Architecture documentaire.
- [x] Convention des identifiants.
- [x] Conventions Markdown et Pandoc.
- [x] Style rédactionnel.
- [x] Standards techniques.
- [x] Standards IA.
- [x] Politique de compatibilité.
- [x] Production, validation et publication.
- [x] Glossaire, bibliographie et index.
- [x] Assurance qualité documentaire.
- [x] Annexes normatives.
- [x] Validation de la compilation complète.
- [x] Convention des outils et contextes d’utilisation.
- [x] Audit transversal du Volume 0 et du Livre I.

**Statut M1 : terminé.** Le workflow GitHub Actions a validé 27 sources, 26 identifiants uniques, la compilation Pandoc/XeLaTeX et un PDF A4 de 214 pages. La licence globale reste à définir avant publication officielle.

## M2 — Livre I : Préparer la plateforme

- [x] Matériel, Windows, pilotes AMD et voies d’accélération.
- [x] Terminal, PowerShell et outils Windows.
- [x] Git, GitHub et VS Code.
- [x] Python et environnements virtuels.
- [x] Docker et Docker Compose.
- [x] Open WebUI, Open Terminal et Vane.
- [x] ComfyUI.
- [x] LLM locaux.
- [x] Audio IA.
- [x] Sécurité, sauvegarde et validation de la plateforme.
- [x] Nouvelle validation technique, documentaire et compilation du Livre I à dix chapitres.
- [x] Repères d’utilisation appliqués à toutes les commandes, fichiers et procédures web.

**Statut M2 : terminé.** Le workflow `Validate Documentation` a contrôlé 37 sources, les 10 chapitres du Livre I et 36 identifiants uniques sans erreur bloquante. Les identifiants historiques des cinq chapitres déplacés ont été conservés. La compilation Pandoc/XeLaTeX a produit un PDF A4 de 396 pages ; 82 pages réparties dans le document ont été contrôlées visuellement. La licence globale et le balisage d’accessibilité du PDF restent à traiter avant publication officielle.

## M3 — Livre II : Développement et architecture

- [x] Fondations Godot, GDScript, architecture et données — 9 chapitres rédigés, repérés et audités sur 9.
- [x] Plateforme IA locale — 4 chapitres rédigés, repérés et audités sur 4.
- [ ] Douze grands systèmes de jeu — 4 chapitres rédigés, repérés et audités sur 12.
- [ ] Industrialisation du projet — 0 chapitre sur 5.
- [x] Convention des outils et contextes appliquée aux chapitres 1 à 17.
- [x] Audit anti-doublon et approfondissement pédagogique du chapitre 2.
- [x] Chapitre 3 — scènes, nœuds, Resources et signaux — rédigé et audité au niveau `static-review`.
- [x] Chapitre 4 — architecture modulaire, arborescence, dépendances et ADR — rédigé et audité au niveau `static-review`.
- [x] Chapitre 5 — services, Autoloads, bus d’événements, registre et injection de dépendances — rédigé et audité au niveau `static-review`.
- [x] Chapitre 6 — Input Map, contrôleurs, caméra et interactions — rédigé et audité au niveau `static-review`.
- [x] Chapitre 7 — Resources, JSON, catalogues, identifiants stables et configurations — rédigé et audité au niveau `static-review`.
- [x] Chapitre 8 — SQLite, schéma relationnel, dépôts, transactions, migrations et intégrité — rédigé et audité au niveau `static-review`.
- [x] Chapitre 9 — snapshots, slots, remplacement contrôlé, copies de secours et migrations de sauvegarde — rédigé et audité au niveau `static-review`.
- [x] Chapitre 10 — sources canoniques, découpage, embeddings locaux, Qdrant dérivé, repli lexical et évaluation — rédigé et audité au niveau `static-review`.
- [x] Chapitre 11 — port applicatif, processus compagnon, protocole JSONL, capacités, délais, corrélation, repli et arrêt contrôlé — rédigé et audité au niveau `static-review`.
- [x] Chapitre 12 — HTTP, WebSocket, contrats versionnés, tâches bornées, idempotence, backpressure, streaming et adaptateurs compatibles OpenAI — rédigé et audité au niveau `static-review`.
- [x] Chapitre 13 — modèle de menaces, séparation production/runtime, secrets, authentification, autorisation, TLS, limites, journaux, SBOM, provenance et signature — rédigé et audité au niveau `static-review`.
- [x] Chapitre 14 — identité stable, définition, état runtime, statistiques dérivées, scène, contrôleurs, apparition, registre actif, événements et sauvegarde — rédigé et audité au niveau `static-review`.
- [x] Chapitre 15 — relations orientées, axes bornés, causes, historique, vues mutuelles, requêtes, événements et sauvegarde indépendante — rédigé et audité au niveau `static-review`.
- [x] Chapitre 16 — filiation dirigée, adoption, tutelle, unions canoniques, cycles, générations dérivées et sauvegarde familiale — rédigé et audité au niveau `static-review`.
- [x] Chapitre 17 — perceptions, mémoire bornée, buts, planification déterministe, ordonnanceur, simulation hors écran, invalidation, IA consultative et sauvegarde minimale — rédigé et audité au niveau `static-review`.
- [x] Clarification du chapitre 17 — intervalles nominaux explicités, codes de retour distingués des erreurs pédagogiques et échéances reportées conservées.
- [x] Correction de clôture du chapitre 17 — prochaine étape réservée à la continuité et synthèse finale consacrée à `Project Asteria`.
- [x] Horodatage des audits — `last-verified` et `audit-date` utilisent ISO 8601 avec heure et offset à partir du chapitre 17, sans heure rétroactive inventée.
- [x] Correction pédagogique du chapitre 15 — blocs de code expliqués selon QA Q1.1.
- [x] Correction pédagogique du chapitre 16 — blocs de code expliqués selon QA Q1.1.
- [x] Audits et preuves QA corrigés des chapitres 15 et 16 fermés avant le chapitre 17.
- [x] Explications des chapitres 15 et 16 rendues concises : chemins et syntaxe non répétés, rôles spécifiques, erreurs au format fautif/correction.
- [x] Auto-paraphrases supprimées et renvois internes des chapitres 15 et 16 recâblés vers des ancres explicites de sous-sections.
- [x] Audit rétroactif des sections d’erreurs, diagnostics et anti-patterns des chapitres 1 à 6 — 52 cas avec exemples fautifs et corrigés.
- [x] Protocole QA adapté à la construction PDF différée.
- [x] Validation automatique rétroactive sans PDF des chapitres 5 et 6.
- [ ] Validation technique, documentaire et compilation du Livre II complet.

**Statut M3 : en cours — 17 chapitres rédigés, repérés et audités sur 30.** Godot 4.7.1-stable, l’édition Standard, GDScript typé et Forward+ constituent la base actuelle du projet fil rouge `Project Asteria`. Les neuf chapitres de fondation et les quatre chapitres de plateforme IA locale sont complets. Quatre des douze systèmes de gameplay sont documentés : personnages, relations sociales, famille et agents autonomes. Le graphe familial distingue filiation, adoption, tutelle et union, refuse auto-liens, doublons et cycles, calcule les relations dérivées, reste indépendant des scènes et se restaure par candidat complet. La correction pédagogique des chapitres 15 et 16 est terminée et leurs audits et preuves QA sont révisés. Le chapitre 17 sépare l’état d’agent, les snapshots, la mémoire, les buts, le plan transitoire et les exécuteurs ; le chapitre 18 traitera désormais le combat. Le workflow léger valide chaque chapitre sans PDF ; la publication complète reste différée à la fin du Livre II.

## M4 — Livre III : Production des contenus et assets

- [ ] Préproduction et direction artistique.
- [ ] Êtres vivants, objets et environnements.
- [ ] Animation, audio, VFX, UI et UX.
- [ ] Automatisation et validation artistique.

## M5 — Livre IV : Finalisation et exploitation

- [ ] Équilibrage, QA et diagnostic.
- [ ] Optimisation et multijoueur.
- [ ] DevOps, publication et maintenance.

## M6 — Livre V : Encyclopédie technique

- [ ] Fiches universelles.
- [ ] Arbres de décision et matrices.
- [ ] Bibliothèques techniques et index croisés.

## M7 — Companion Pack

- [ ] Starter Kit.
- [ ] Project Templates.
- [ ] AI Library.
- [ ] Code Library.
- [ ] Database Library.
- [ ] ComfyUI Library.
- [ ] Documentation Library.
- [ ] Test & Benchmark Library.
- [ ] Production Toolkit.
- [ ] Knowledge Base.

## M8 — Publications

- [ ] Définir la licence globale du projet.
- [ ] Produire les versions PDF, HTML et EPUB.
- [ ] Produire un PDF balisé pour les lecteurs d’écran.
- [ ] Publier les archives du Companion Pack.

## M9 — Version 1.0

- [ ] Stabiliser les cinq Livres et le Companion Pack.
- [ ] Exécuter les campagnes finales de QA.
- [ ] Publier la version 1.0 de la collection.
