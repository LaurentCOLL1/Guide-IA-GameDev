---
title: "Audit post-création — Livre IV, chapitre 18"
id: "DOC-L4-QA-AUDIT-CH18"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre IV"
chapter: 18
chapter-id: "DOC-L4-CH18"
chapter-version: "1.0.0"
last-verified: "2026-07-27T13:24:17+02:00"
audit-status: "complete"
audit-date: "2026-07-27T13:24:17+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 18 — Accessibilité

## 1. Décision

Décision : **accepté avec réserves runtime, plateformes, technologies d’assistance, sessions utilisateurs,
photosensibilité, publication et fin de Livre**.

Le chapitre satisfait le plan maître au niveau documentaire. Il traite les commandes, le visuel, l’audio, la cognition
et la motricité, prépare les options demandées, définit les parcours représentatifs, documente les limites et fournit
une déclaration publique candidate sans revendiquer de conformité ni de campagne exécutée.

## 2. Périmètre contrôlé

- frontière avec le chapitre 17 pour la publication initiale ;
- frontière avec le chapitre 25 du Livre III pour l’accessibilité visuelle des assets et de l’UX ;
- frontière avec le chapitre 19 pour localisation, polices, scripts et sens d’écriture ;
- frontière avec le chapitre 20 pour correctifs, mises à jour distribuées et rollback ;
- matrice de barrières fondée sur les tâches plutôt que sur des diagnostics ;
- architecture de profils composables, prévisualisables, annulables et persistables ;
- actions nommées, remapping, conflits, invites dynamiques, maintiens, répétitions et combinaisons ;
- zones mortes, sensibilités, inversion et alternatives numériques aux gestes analogiques ;
- rythme, difficulté décomposée, limites de temps, pause et récupération ;
- contraste, couleur redondante, taille du texte, reflow, focus, cibles, mouvement et photosensibilité ;
- sous-titres, captions, mixage, mono, dynamique, signaux visuels, description audio et TTS ;
- charge cognitive, objectifs, erreurs, aides motrices, haptique et sauvegardes ;
- profils Solo/Studio, parcours représentatifs, sessions utilisateurs et non-régression ;
- registre de limites, déclaration publique, support et corrélation au build ;
- dix diagnostics complets conformes à la règle sémantique.

## 3. Contrôle du plan maître

Les cinq objectifs du plan maître sont couverts : cinq familles de barrières, réglages clés, scénarios avec profils et
utilisateurs, limites connues et accès depuis les réglages. Les cinq livrables sont représentés par la matrice, les
options, les parcours, le rapport d’audit et la déclaration candidate.

La frontière supérieure est respectée : les fondations visuelles du Livre III sont consommées sans être réécrites. La
validation future repose sur des parcours représentatifs et non sur la seule présence de réglages.

## 4. Contrôle pédagogique

- les termes fondamentaux sont définis avant usage ;
- les exemples GDScript expliquent classe, héritage, types, paramètres, retours, mutations, effets et limites ;
- les formats YAML, JSON, Markdown, CSV et texte expliquent leurs champs et résultats attendus ;
- les nombres sont explicitement candidats lorsqu’ils ne proviennent pas d’une campagne ;
- les réserves de syntaxe ou de plateforme sont nommées lorsque l’API dépend de la matérialisation ;
- chaque bloc clôturé possède un repère d’utilisation immédiatement avant le fence ;
- les dix repères apparaissent dans le corps du chapitre ;
- les dix cas de diagnostic comportent symptôme, exemple fautif, justification, correction et justification.

## 5. Contrôle technique

- la séparation action/périphérique est compatible avec `InputMap` et `InputEvent` ;
- le remapping conserve des erreurs structurées et ne modifie pas le métier ;
- les exemples `Theme` utilisent les listes de types et de propriétés de tailles de police ;
- le TTS utilise `DisplayServer.tts_get_voices_for_language()`, `tts_speak()` et `tts_stop()` ;
- la limite entre TTS système et intégration riche de lecteur d’écran est explicitée ;
- WCAG 2.2 est qualifié comme norme web réutilisée pour des objectifs, sans déclaration automatique de conformité native ;
- les Xbox Accessibility Guidelines sont qualifiées comme bonnes pratiques, sans certification juridique ;
- la photosensibilité conserve une porte bloquée tant que l’analyse et la revue ne sont pas exécutées ;
- les informations accessibles restent des sorties de présentation sans autorité gameplay ;
- la déclaration publique est liée au build, aux preuves et aux limites.

## 6. Métriques statiques

| Mesure | Valeur |
|---|---:|
| Lignes | 2090 |
| Titres | 61 |
| Blocs de code ou données | 64 |
| Blocs significatifs | 59 |
| Marqueurs d’explication | 64 |
| Explications structurées hors diagnostics | 44 |
| Cas fautifs expliqués | 10 |
| Corrections expliquées | 10 |
| Titres dupliqués | 0 |
| Blocs significatifs dupliqués | 0 |
| Paragraphes longs dupliqués | 0 |

## 7. Contrôle des références

- W3C WCAG 2.2 et documents Understanding ;
- Xbox Accessibility Guidelines et directives thématiques sur texte, canaux, captions, audio, entrée, difficulté, navigation, temps, mouvement, photosensibilité et documentation ;
- Godot Engine 4.7 pour InputMap, DisplayServer et text-to-speech ;
- liens Markdown nommés, sans URL brute dans la section de références ;
- portée normative ou informative explicitée.

## 8. Contrôle des doublons et frontières

Aucun titre dupliqué, aucun bloc significatif dupliqué et aucun paragraphe long dupliqué n’est détecté par le contrôle
local reproduisant la logique du validateur permanent.

Le chapitre ne recrée ni le pipeline de localisation, ni les pages boutique, ni les correctifs distribués, ni la
production visuelle des assets. Les références croisées sont formulées comme frontières de responsabilité.

## 9. Contrôle des revendications

- aucune fonction d’accessibilité de `Project Asteria` n’est déclarée comme implémentée ;
- aucun build, périphérique, lecteur d’écran, voix système ou API de plateforme n’est qualifié ;
- aucun parcours représentatif n’est exécuté ;
- aucune session avec utilisateur n’est planifiée ou réalisée ;
- aucune analyse de photosensibilité n’est exécutée ;
- aucune conformité WCAG, XAG, légale ou plateforme n’est revendiquée ;
- aucune déclaration publique n’est publiée ;
- aucun PDF du Livre IV n’est produit.

## 10. Réserves

- les valeurs de réglage doivent être qualifiées sur les plateformes et périphériques réels ;
- les extraits GDScript doivent être intégrés au Starter Kit puis testés avec Godot 4.7.1 ;
- les fonctions d’accessibilité de `DisplayServer` et le TTS doivent être vérifiés par système d’exploitation ;
- l’intégration avec les lecteurs d’écran doit être évaluée séparément du TTS intégré ;
- les écrans doivent être testés avec texte agrandi, contenus longs, ratios variés et futures localisations ;
- les captions, descriptions audio et mixages doivent être produits et revus sur les médias finaux ;
- les flashs, motifs et mouvements doivent passer une campagne et une revue spécialisées ;
- les aides motrices et de difficulté doivent être qualifiées avec le gameplay et le multijoueur concernés ;
- les sessions utilisateurs exigent recrutement, consentement, accessibilité, compensation, confidentialité et retrait ;
- la déclaration publique doit être générée depuis le build et les preuves réellement qualifiés ;
- la licence globale de la collection reste indéfinie ;
- le balisage final d’accessibilité du PDF de collection reste ouvert.

## 11. Preuves d’intégrité

- empreinte SHA-256 du chapitre : `e5451442ca0f82a7211523c0116867d56270eda0a3ef3fc8fa9d25bc6106b352` ;
- empreinte SHA-256 de l’audit : calculée après fermeture de ce rapport et enregistrée dans la preuve YAML ;
- validation permanente légère : en attente du commit final de la branche ;
- niveau d’audit : `static-review`.

## 12. Conclusion

Le chapitre 18 est accepté au niveau documentaire avec zéro erreur bloquante dans les contrôles locaux. La seule alerte
globale attendue reste la licence de collection non définie. Toutes les preuves runtime, humaines, matérielles, de
plateforme et de publication demeurent réservées.
