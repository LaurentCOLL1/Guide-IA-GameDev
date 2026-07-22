---
title: "Audit du Livre II — Chapitre 28"
id: "DOC-L2-QA-AUDIT-CH28"
status: "complete"
version: "1.0.0"
chapter-id: "DOC-L2-CH28"
chapter-version: "1.0.0"
audit-level: "static-review"
audit-date: "2026-07-22T03:02:36+02:00"
last-verified: "2026-07-22T03:02:36+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 28 — Journalisation, diagnostic et reproductibilité

## 1. Porte de création

Le chapitre a été créé sur la branche dédiée `docs/livre-ii-ch28-journalisation-diagnostic` et dans la pull request en brouillon #82, depuis le commit `2c62e1f6de55dfc8ebcbb4325363de178388ed3c`. La continuité, la roadmap, `contents.txt`, l’index du Livre II, le protocole QA et le chapitre 27 ont été relus avant rédaction. Aucun fichier, branche ou pull request concurrente portant le chapitre 28 n’était présent.

## 2. Résultats

- lignes finales : **2091** ;
- titres Markdown contrôlés : **74** ;
- blocs de code ou de données : **67** ;
- marqueurs d’explication : **67** ;
- explications structurées hors sections d’erreurs : **47** ;
- cas d’erreurs détaillés : **10** ;
- contre-exemples expliqués : **10** ;
- corrections expliquées : **10** ;
- doublons de titres : **0** ;
- blocs significatifs dupliqués : **0** ;
- paragraphes longs dupliqués : **0** ;
- blocs sans explication identifiable : **0** ;
- sections Solo/Studio placées dans un bloc de code : **0** ;
- commandes de procédure QA dans le chapitre lecteur : **0** ;
- instruction de pilotage du chapitre suivant : **0** ;
- métadonnée ou en-tête de niveau de raisonnement : **0** ;
- synthèse finale `Project Asteria` : **présente**.

## 3. Complétude et périmètre

Le chapitre distingue journaux, métriques, traces et artefacts de diagnostic. Il documente les sorties natives de Godot, la rotation des fichiers, les niveaux de sévérité, un catalogue d’événements stables, un schéma JSONL, les temps UTC et monotones, les identifiants opaques, la corrélation, la causalité, les spans, les métriques de faible cardinalité, les files bornées, l’échantillonnage, les marqueurs de session, les manifestes, les empreintes SHA-256, les archives ZIP, le consentement, la rétention et le support hors ligne.

Le chapitre 27 reste l’autorité des suites, fixtures, scénarios et résultats de tests. Le chapitre 28 consomme leurs artefacts sans les recréer ni modifier les golden files. L’automatisation Python, la génération de données et l’orchestration de campagnes restent réservées au chapitre 29. L’organisation globale Solo/Studio reste au chapitre 30.

## 4. Revue statique des références

La journalisation native, les paramètres de rotation, le flush de stdout, les catégories de sortie, les loggers personnalisés, les callbacks multithread, les piles d’appels, `Time`, `FileAccess`, `Crypto`, `Engine`, `ScriptBacktrace`, `HashingContext` et `ZIPPacker` ont été relus contre la documentation officielle Godot 4.7.

Le schéma de journaux, les sévérités, `TraceId` et `SpanId` ont été comparés au modèle stable des journaux OpenTelemetry. La propagation distribuée a été bornée par la recommandation W3C Trace Context. Les exclusions, la rédaction, la rétention et les risques de saturation ont été relus contre l’OWASP Logging Cheat Sheet.

Cette revue ne constitue ni une exécution du parseur GDScript, ni une création d’archive réelle, ni une collecte de crash avec symboles, ni une intégration à un collecteur distant.

## 5. Explications pédagogiques

Les **67** blocs possèdent **67** marqueurs. Les **47** blocs hors sections d’erreurs sont expliqués par des points spécifiques : organisation, responsabilités, paramètres, retours, déroulement, effets de bord, sécurité, invariants, résultat attendu et limites selon le besoin réel du bloc.

Les dix cas pédagogiques suivent directement la séquence obligatoire : symptôme, exemple fautif, `Pourquoi cet exemple est fautif`, exemple corrigé, puis `Pourquoi la correction fonctionne`. Aucun wrapper `Explication structurée du bloc` ne s’intercale dans ces séquences.

Les parcours Solo et Studio sont rédigés en Markdown ordinaire. Les blocs de texte sont réservés aux schémas, politiques, formats et listes littérales.

## 6. Contrôles particuliers

- les journaux n’acquièrent aucune autorité métier ;
- le tick logique reste distinct de l’horloge système ;
- les durées utilisent `Time.get_ticks_usec()` ;
- les noms d’événements sont stables et versionnés ;
- les identifiants de corrélation sont opaques ;
- les attributs sont admis par liste autorisée ;
- mots de passe, jetons, clés, chaînes de connexion, prompts et réponses brutes sont exclus ;
- les chaînes, files, journaux, traces, métriques et archives sont bornés ;
- les callbacks de `Logger` n’écrivent pas directement et évitent toute récursion ;
- les métriques interdisent les identifiants d’instances comme labels ;
- les événements graves ne sont pas échantillonnés ;
- un marqueur persistant signale seulement un arrêt non propre ;
- les paquets utilisent une liste fermée, des chemins relatifs et des empreintes SHA-256 ;
- le ZIP n’est pas présenté comme chiffré ou signé ;
- le consentement précède tout export ;
- le support hors ligne reste fonctionnel ;
- aucun des calques terminologiques interdits par le validateur n’est présent.

## 7. Réserves

- parseur Godot `4.7.1-stable` non exécuté ;
- scripts d’observabilité non matérialisés dans le Starter Kit ;
- `Logger` personnalisé non enregistré dans un processus Godot réel ;
- synchronisation multithread non exercée ;
- rotation et rétention non mesurées ;
- persistance JSONL et flush non testés sur les plateformes cibles ;
- métriques et traces non exportées ;
- arrêt brutal réel non provoqué ;
- crash natif et symbolisation non testés ;
- archives ZIP non créées ni relues ;
- consentement et interface d’aperçu non matérialisés ;
- collecteur OpenTelemetry non installé ;
- aucune donnée envoyée à un service distant ;
- aucun PDF construit.

## 8. Décision

Le chapitre 28 est **accepté au niveau `static-review`**. Il définit un contrat local, borné, minimisé et reproductible pour `Project Asteria`, sous réserve de sa matérialisation et de campagnes runtime ultérieures dans le Starter Kit.
