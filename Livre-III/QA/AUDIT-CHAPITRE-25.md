---
title: "Audit post-création — Livre III, chapitre 25"
id: "DOC-L3-QA-AUDIT-CH25"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L3-CH25"
chapter-version: "1.0.0"
audit-date: "2026-07-24T21:47:46+02:00"
last-verified: "2026-07-24T21:47:46+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 25

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de matérialisation des profils, de mesure du contraste, d’exécution des parcours de focus, de sessions avec des personnes, de confidentialité opérationnelle, de mesures runtime et de PDF de fin de Livre.

Aucun profil d’accessibilité, variante de contraste, scène Godot, capture, session, participant, observation, enregistrement, benchmark ou PDF n’est revendiqué comme produit ou exécuté.

## 2. Périmètre comparé au plan maître

Le chapitre couvre hiérarchie de l’information, charge cognitive, contraste, tailles, densité, lisibilité, perception des couleurs, codages redondants, focus, ordre logique, réduction du mouvement, flashs, erreurs, confirmations, annulation, récupération et notifications.

Les protocoles de test couvrent tâches, recrutement, consentement, confidentialité, préparation de session, facilitation, observations, mesures, gravité, rapport, retest et limites de généralisation.

Les livrables prévus sont préparés comme contrats : checklist UX, profils d’accessibilité, variantes de contraste, scénarios de tests et rapport utilisateur. Leur matérialisation reste en réserve.

## 3. Frontières contrôlées

- le chapitre 24 conserve design system, thèmes, composants et dispositions ;
- le chapitre 25 conserve critères UX, profils d’accessibilité visuelle et tests avec des personnes ;
- le Livre II chapitre 6 conserve intentions d’entrée et remappage ;
- les chapitres métier du Livre II conservent états, commandes et transactions ;
- le Livre IV complétera accessibilité audio, commandes et plateforme ;
- les critères WCAG servent de références mesurables sans constituer une certification automatique du jeu ;
- aucune observation, animation, option ou interface n’applique directement une règle métier.

## 4. Contrôles pédagogiques

- procédure progressive depuis la hiérarchie de l’information jusqu’à la porte d’acceptation ;
- contraste, taille, couleur redondante, focus, cibles, mouvement et récupération expliqués ;
- profils composables, migrations, brouillon, aperçu et application séparés ;
- scénarios, consentement, facilitation, observations et analyse encadrés ;
- fonctions, paramètres, types, retours et effets de bord explicités dans les exemples GDScript ;
- chaque bloc significatif possède un repère d’utilisation et une explication structurée ;
- dix diagnostics suivent l’ordre symptôme, exemple fautif, raison, exemple corrigé, raison ;
- modes Solo et Studio documentés en Markdown ordinaire ;
- valeurs candidates, données personnelles absentes et preuves non exécutées explicitement signalées.

## 5. Contrôles documentaires

- lignes : 2158 ;
- titres : 71 ;
- blocs code ou données : 74 ;
- marqueurs d’explication : 74 ;
- explications structurées hors diagnostics : 54 ;
- diagnostics détaillés : 10 ;
- titres dupliqués : 0 ;
- blocs significatifs dupliqués : 0 ;
- paragraphes longs dupliqués : 0 ;
- synthèse opérationnelle `Project Asteria` présente ;
- références techniques officielles sous forme de liens Markdown cliquables ;
- absence de prochaine action et de recommandation GPT dans le texte lecteur ;
- PDF non produit.

## 6. Exactitude technique

La revue statique s’appuie sur la documentation officielle Godot 4.7 pour `Control`, les actions `ui_*`, le focus, les résolutions multiples et la pseudo-localisation.

Les critères W3C WCAG 2.2 sont présentés comme références de conception pour contraste, usage de la couleur, focus, taille des cibles, reflow, animation, flashs et erreurs. Le chapitre précise qu’ils concernent le contenu web et ne certifient pas automatiquement Project Asteria.

Les formulations distinguent observation et interprétation, préférence et barrière, mesure et décision, session qualitative et généralisation statistique, profil visuel et diagnostic médical, consentement d’observation et consentements d’enregistrement ou de citation.

## 7. Réserves ouvertes

- pilote `AST-UX-PILOT-CORE-SHELL-001` non matérialisé ;
- profils de contraste, texte, mouvement, focus et couleur non créés ;
- mesures de contraste et captures non produites ;
- parcours de focus et tailles de cibles non exécutés ;
- variantes de mouvement et revue des flashs non inspectées ;
- scénarios et fixtures non matérialisés ;
- aucun participant recruté et aucune session conduite ;
- consentements, stockage restreint, rétention et retrait non mis en œuvre ;
- observations, problèmes, rapport et retests non produits ;
- conformité WCAG du jeu non revendiquée ;
- CPU, GPU, mémoire, allocations et latence non mesurés ;
- Starter Kit non matérialisé ;
- licence globale de la collection non définie ;
- PDF du Livre III différé à la fin du Livre.

## 8. Conclusion

Le chapitre satisfait le plan maître et peut entrer dans la validation légère sans PDF. La preuve finale restera `pending` jusqu’à la réussite des workflows permanents sur la branche matérialisée.
