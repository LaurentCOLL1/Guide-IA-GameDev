---
title: "Audit post-création — Livre IV, chapitre 19"
id: "DOC-L4-QA-AUDIT-CH19"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre IV"
chapter: 19
chapter-id: "DOC-L4-CH19"
chapter-version: "1.0.0"
last-verified: "2026-07-27T18:41:51+02:00"
audit-status: "complete"
audit-date: "2026-07-27T18:41:51+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 19 — Localisation et internationalisation

## 1. Décision

Décision : **accepté avec réserves runtime, linguistiques, typographiques, culturelles, fournisseurs, plateformes,
publication et fin de Livre**.

Le chapitre satisfait le plan maître au niveau documentaire. Il prépare l’internationalisation de l’architecture, les
catalogues, formats culturels, écritures, polices, pseudo-locales, traductions, relectures et portes de publication sans
revendiquer de locale réellement intégrée ou supportée.

## 2. Périmètre contrôlé

- frontière avec le chapitre 17 pour pages boutique et publication initiale ;
- frontière avec le chapitre 18 pour accessibilité du produit complet ;
- frontière avec le chapitre 20 pour correctifs, mises à jour distribuées et rollback ;
- frontière avec le Livre III pour création des voix, audio et synchronisation labiale ;
- locales source, candidates, formats régionaux, écritures et politique de repli ;
- clés stables, chaînes externalisées, paramètres nommés, balisage et contenus non fiables ;
- pluriels, genres grammaticaux, dates, heures, nombres, montants en euros et unités ;
- texte bidirectionnel, shaping, segmentation, saisie, glyphes et piles de polices ;
- mise en page flexible, pseudo-localisation longue et bidirectionnelle ;
- catalogues, formats CSV/PO/Godot, extraction, statuts, glossaire et mémoire de traduction ;
- sous-titres, captions, voix localisées, images avec texte et contenus réglementaires ;
- contrôles automatisés, captures, écritures non latines, persistance et changement de langue ;
- confidentialité, sécurité des fournisseurs, procédures Solo/Studio et portes go/no-go ;
- dix diagnostics complets conformes à la règle sémantique.

## 3. Contrôle du plan maître

Les cinq objectifs sont couverts : externalisation, règles linguistiques et culturelles, polices/UI/voix/sous-titres,
organisation de traduction et contrôles automatisés. Les cinq livrables sont représentés par le catalogue candidat, les
conventions, la pseudo-localisation, les scénarios de débordement et le présent rapport linguistique.

La validation future est correctement réservée à une pseudo-langue exécutée, des langues longues, des écritures non
latines, des polices qualifiées et une revue linguistique en contexte sur un build corrélé.

## 4. Contrôle pédagogique

- les termes i18n, l10n, locale, écriture, repli, transcréation et adaptation culturelle sont définis avant usage ;
- les exemples GDScript expliquent types, paramètres, retours, effets et limites ;
- les formats YAML, JSON, texte, PowerShell, Bash et Batch expliquent leurs champs et résultats ;
- les montants restent structurés et utilisent `EUR`, avec `19,99 €` comme présentation française illustrative ;
- chaque bloc clôturé possède un repère d’utilisation et un marqueur d’explication ;
- les dix repères d’utilisation apparaissent dans le corps ;
- les dix diagnostics comportent symptôme, contre-exemple, justification, correction et justification.

## 5. Contrôle technique

- `TranslationServer.translate()` est utilisé depuis la méthode statique plutôt qu’un appel d’instance implicite à `tr()` ;
- `TranslationServer.standardize_locale()` est documenté à la frontière entre BCP 47 et la forme reconnue par Godot ;
- les placeholders nommés restent réordonnables et séparés des données métier ;
- les pluriels restent des règles de locale et la quantité demeure numérique ;
- dates, nombres, devises et unités restent structurés jusqu’au rendu ;
- les écritures RTL utilisent la direction de mise en page et le traitement bidirectionnel, pas un miroir géométrique ;
- la pseudo-localisation PowerShell protège variables et balises avant transformation ;
- les contrôles structurels ne sont pas présentés comme validation linguistique ou culturelle ;
- les traductions et sorties de fournisseurs n’acquièrent aucune autorité gameplay ;
- la publication d’une locale reste liée au même build, aux polices, aux preuves et aux réserves.

## 6. Métriques statiques

| Mesure | Valeur |
|---|---:|
| Lignes | 1325 |
| Titres | 60 |
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

- documentation officielle Godot sur internationalisation, locales, gettext, tableurs et `TranslationServer` ;
- Unicode Bidirectional Algorithm, LDML et CLDR ;
- BCP 47 pour l’identification des langues ;
- liens Markdown nommés, sans URL brute dans la section de références ;
- Godot `4.7.1-stable` conservé comme moteur de référence du dépôt.

## 8. Contrôle des doublons et frontières

Aucun titre, bloc significatif ou paragraphe long dupliqué n’est détecté par le contrôle local. Le chapitre ne recrée ni
l’accessibilité produit, ni les pages boutique, ni la production des voix, ni les mécanismes de patch et rollback.

## 9. Contrôle des revendications

- aucune locale cible n’est déclarée comme supportée ;
- aucune traduction, transcréation ou adaptation culturelle n’est déclarée comme approuvée ;
- aucun catalogue Godot, PO, CSV final ou mémoire de traduction n’est matérialisé ;
- aucune police, pile de fallback, écriture non latine ou saisie n’est qualifiée ;
- aucune pseudo-localisation ni capture de débordement n’est exécutée ;
- aucune voix localisée, caption ou synchronisation labiale n’est produite ;
- aucune relecture native, validation en contexte ou recherche utilisateur n’est exécutée ;
- aucun service distant ou fournisseur n’est qualifié ;
- aucun build multilingue ou publication réelle n’est produit ;
- aucun PDF du Livre IV n’est produit.

## 10. Réserves

- intégrer les catalogues au Starter Kit puis vérifier extraction, import et changement de locale dans Godot ;
- qualifier les locales avec des relecteurs compétents et des guides de style approuvés ;
- vérifier pluriels, genres, dates, nombres, montants, unités et calendriers par locale ;
- qualifier les piles de polices, licences, glyphes, shaping, segmentation et saisie ;
- exécuter pseudo-localisation longue, RTL et campagnes d’écritures non latines ;
- tester tailles de texte accessibles, focus, débordements, captures et ratios d’écran ;
- produire et revoir sous-titres, captions, voix et variantes de médias finales ;
- gouverner fournisseurs, corpus, données personnelles, secrets, rétention et retraits ;
- corréler toute déclaration de support linguistique à un build et à ses preuves ;
- définir la licence globale de la collection ;
- traiter le balisage final d’accessibilité du PDF de collection.

## 11. Preuves d’intégrité

- empreinte SHA-256 du chapitre : `6fa44239ff9d9992b36608627ebf3f4fe1c374debd35991346d07a4ccb562c68` ;
- empreinte SHA-256 de l’audit : calculée après fermeture de ce rapport et enregistrée dans la preuve YAML ;
- validation permanente légère : en attente du commit final de la branche ;
- niveau d’audit : `static-review`.

## 12. Conclusion

Le chapitre 19 est accepté au niveau documentaire avec zéro erreur bloquante dans les contrôles locaux. La seule alerte
globale attendue reste la licence de collection non définie. Toutes les preuves runtime, linguistiques, typographiques,
humaines, culturelles, de plateforme et de publication demeurent réservées.
