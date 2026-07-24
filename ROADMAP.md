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
- [x] Douze grands systèmes de jeu — 12 chapitres rédigés, repérés et audités sur 12.
- [x] Industrialisation du projet — 5 chapitres rédigés, repérés et audités sur 5.
- [x] Convention des outils et contextes appliquée aux chapitres 1 à 30.
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
- [x] Chapitre 18 — commandes typées, côtés, initiative déterministe, ciblage, portée, ligne de vue, dégâts, garde, états, commit préparé, simulation hors écran et sauvegarde stricte — rédigé et audité au niveau `static-review`.
- [x] Chapitre 19 — définitions de compétences, coûts, ciblages, effets composables, progression, charges, recharges, unité de travail commune et sauvegarde stricte — rédigé et audité au niveau `static-review`.
- [x] Chapitre 20 — définitions et instances d’objets, lots fongibles, conteneurs, transferts autorisés, équipement, durabilité, propriété, provenance, réputation et sauvegarde stricte — rédigé et audité au niveau `static-review`.
- [x] Chapitre 21 — devises, unités mineures, portefeuilles, écritures équilibrées, prix, offres, achats, taxes, récompenses, idempotence et commit avec l’inventaire — rédigé et audité au niveau `static-review`.
- [x] Chapitre 22 — horloge logique, régions, populations, ressources, résidus, simulation bornée, matérialisation, récoltes, signaux économiques et sauvegarde — rédigé et audité au niveau `static-review`.
- [x] Chapitre 23 — institutions, factions, adhésions, rangs, mandats, lois versionnées, autorisations, infractions, preuves, verdicts, sanctions coordonnées et sauvegarde — rédigé et audité au niveau `static-review`.
- [x] Chapitre 25 — faits narratifs, arcs, quêtes, objectifs, conditions, conséquences, codex, connaissances et sauvegarde — rédigé et audité au niveau `static-review`.
- [x] Chapitre 26 — plugins d’éditeur, docks, inspecteurs, validation, importeurs, provenance, staging et pipelines de contenu — rédigé et audité au niveau `static-review`.
- [x] Chapitre 27 — tests unitaires, intégration, doubles, fixtures, simulations déterministes, non-régression et critères de passage — rédigé et audité au niveau `static-review`.
- [x] Chapitre 28 — journalisation structurée, sévérité, corrélation, causalité, métriques, traces, rédaction, paquets de diagnostic et support hors ligne — rédigé et audité au niveau `static-review`.
- [x] Chapitre 29 — environnement Python, CLI typées, schémas, génération déterministe, orchestration, parallélisme borné, checkpoints, manifestes et archives reproductibles — rédigé et audité au niveau `static-review`.
- [x] Chapitre 30 — architecture Solo et Studio, responsabilités, profils, gouvernance, qualification des dépendances, CI, publication et plan du Starter Kit — rédigé et audité au niveau `static-review`.
- [x] Règle permanente — toute dépendance future du Starter Kit doit être qualifiée avant adoption.
- [x] Chapitre 24 — domaines, parcelles, liens de tenure, bâtiments, chantiers, matériaux, production, entretien, permissions et sauvegarde — rédigé et audité au niveau `static-review`.
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
- [x] Gouvernance GPT-5.6 Sol corrigée : recommandation conservée dans le processus, retirée des métadonnées et des en-têtes lecteurs des chapitres.
- [x] Explications des blocs restructurées sans perte pour les chapitres 17 à 26 ; Solo/Studio replacé en Markdown ordinaire dans les chapitres 25 et 26.
- [x] Validation automatique rétroactive sans PDF des chapitres 5 et 6.
- [x] Validation technique, documentaire, compilation Pandoc/XeLaTeX et inspection visuelle du Livre II complet.

**Statut M3 : terminé — 30 chapitres rédigés, repérés, audités et validés transversalement sur 30.** La compilation Pandoc/XeLaTeX du PDF complet, le préflight structurel et l’inspection visuelle sont réussis. Les réserves de publication propres au Livre II sont closes ; la licence globale, le PDF balisé et les réserves runtime restent des chantiers de collection distincts.

## M4 — Livre III : Production des contenus et assets

- [x] Chapitre 1 — Préproduction et cahier des charges artistique.
- [x] Chapitre 2 — Direction artistique et bible visuelle.
- [x] Chapitre 3 — Références, concept art et ComfyUI.
- [x] Chapitre 4 — Pipeline Blender et organisation des fichiers.
- [x] Chapitre 5 — Provenance, licences et validation des assets.
- [x] Chapitre 6 — Création des humains.
- [x] Chapitre 7 — Création des humanoïdes.
- [x] Chapitre 8 — Création des animaux.
- [x] Chapitre 9 — Création des créatures.
- [x] Chapitre 10 — Visages, peau, yeux, cheveux et pilosité.
- [x] Chapitre 11 — Vêtements, armures et accessoires.
- [x] Chapitre 12 — Objets, équipements et armes.
- [x] Chapitre 13 — Architecture, bâtiments et kits modulaires.
- [x] Chapitre 14 — Terrains, paysages et mondes ouverts.
- [x] Chapitre 15 — Végétation et biomes.
- [x] Chapitre 16 — Textures, matériaux et pipeline PBR.
- [x] Chapitre 17 — UV, retopologie et baking.
- [x] Chapitre 18 — LOD, imposteurs et optimisation géométrique.
- [x] Chapitre 19 — Rigging et skinning.
- [x] Chapitre 20 — Animation procédurale et animation par keyframes.
- [x] Préproduction et direction artistique — 5 chapitres sur 5.
- [ ] Êtres vivants, objets et environnements.
- [ ] Animation, audio, VFX, UI et UX.
- [ ] Automatisation et validation artistique.

**Statut M4 : en cours — 20 chapitres rédigés, repérés et audités sur 30.**

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

- [x] Produire, préflighter et inspecter le PDF complet de fin du Livre II.

- [ ] Définir la licence globale du projet.
- [ ] Produire les versions PDF, HTML et EPUB.
- [ ] Produire un PDF balisé pour les lecteurs d’écran.
- [ ] Publier les archives du Companion Pack.

## M9 — Version 1.0

- [ ] Stabiliser les cinq Livres et le Companion Pack.
- [ ] Exécuter les campagnes finales de QA.
- [ ] Publier la version 1.0 de la collection.
