---
title: "Audit rétroactif — exemples d’erreurs et corrections, chapitres 1 à 6"
id: "DOC-L2-QA-ERROR-EXAMPLES-CH01-CH06"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
audit-date: "2026-07-19"
audit-level: "static-review"
pdf-built: false
---

# Audit rétroactif — exemples d’erreurs et corrections, chapitres 1 à 6

## 1. Décision

Les sections pédagogiques consacrées aux erreurs, anti-patterns et diagnostics des chapitres 1 à 6 ont été révisées selon une règle sémantique indépendante de leur titre.

**Décision : accepté au niveau `static-review`, sous réserve de la validation automatique légère.**

## 2. Sections contrôlées

| Chapitre | Section | Cas détaillés |
|---:|---|---:|
| 1 | `Erreurs fréquentes` | 8 |
| 2 | `Erreurs fréquentes` | 9 |
| 3 | `Erreurs fréquentes et diagnostics` | 8 |
| 4 | `Éviter les anti-patterns` | 6 |
| 4 | `Erreurs fréquentes et diagnostics` | 6 |
| 5 | `Anti-patterns et corrections` | 7 |
| 6 | `Anti-patterns et corrections` | 8 |

Total : **52 cas détaillés**.

Le tableau `Symptômes fréquents` du chapitre 6 est conservé comme index rapide et renvoie explicitement vers la section détaillée.

## 3. Critères appliqués

Chaque cas détaillé contient maintenant :

1. un symptôme ou risque ;
2. un bloc marqué `Exemple fautif` ;
3. une correction formulée ;
4. un bloc marqué `Exemple corrigé` ;
5. un paragraphe `Différence` expliquant le changement de comportement ou d’architecture.

Les exemples utilisent les repères `[LECTURE]`, `[VSC]`, `[PS]`, `[APP]` ou `[SORTIE]` adaptés à leur nature.

## 4. Règle de titre

Aucun renommage artificiel n’est imposé. Les formulations suivantes sont équivalentes lorsqu’elles enseignent des fautes et leurs remèdes :

- erreurs fréquentes ;
- erreurs et diagnostics ;
- anti-patterns ;
- pièges ;
- mauvaises pratiques ;
- symptômes accompagnés de corrections.

Le marqueur `<!-- qa:error-correction-section -->` qualifie une section détaillée. Le marqueur `<!-- qa:error-correction-index -->` qualifie un index compact renvoyant vers les exemples.

## 5. Automatisation

`tools/validate_chapters.py` vérifie désormais :

- qu’une section reconnue possède un marqueur sémantique ;
- qu’une section détaillée possède des sous-cas ;
- que chaque sous-cas contient les deux exemples et l’explication de différence ;
- qu’un index compact renvoie vers des exemples détaillés.

## 6. Réserves

- les exemples restent audités statiquement ;
- les fichiers du Starter Kit ne sont pas encore matérialisés ;
- aucun PDF intermédiaire n’est construit ;
- les comportements seront qualifiés `runtime-tested` après exécution réelle.
