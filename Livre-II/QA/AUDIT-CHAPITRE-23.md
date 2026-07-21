---
title: "Audit du Livre II — Chapitre 23"
id: "DOC-L2-QA-AUDIT-CH23"
status: "complete"
version: "1.0.2"
chapter-id: "DOC-L2-CH23"
chapter-version: "1.0.2"
audit-level: "static-review"
audit-date: "2026-07-21T19:59:30+02:00"
last-verified: "2026-07-21T19:59:30+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 23 — Politique, factions et justice

## 1. Porte de brouillon

Le chapitre a été matérialisé sur la branche dédiée `docs/livre-ii-ch23-politique-factions-justice` et dans la pull request en brouillon #54. La seconde lecture a précédé le passage de la version `0.9.0` à `1.0.0`.

## 2. Résultats

- lignes finales : **4334** ;
- titres Markdown : **75** ;
- blocs de code ou de données : **71** ;
- marqueurs d’explication : **71** ;
- cas d’erreurs détaillés : **10** ;
- contre-exemples expliqués : **10** ;
- corrections expliquées : **10** ;
- doublons de titres : **0** ;
- blocs significatifs sans explication : **0** ;
- commandes de validation QA dans le chapitre lecteur : **0** ;
- instruction `Prochaine étape` dans le chapitre : **0** ;
- synthèse finale `Project Asteria` : **présente**.
- unités d’explication antérieures conservées : **279** ;
- segments d’explication antérieurs perdus : **0** ;
- points pédagogiques complémentaires ajoutés : **0** ;
- sections Solo/Studio rendues en Markdown ordinaire : **oui**.

## 3. Complétude et périmètre

Le chapitre couvre institutions, factions, rangs, fonctions, adhésions, mandats, lois versionnées, juridictions, droits, autorisations explicables, infractions rapportées, événements causaux, preuves, chaîne de garde, dossiers, enquêtes, verdicts, sanctions coordonnées et persistance.

Les frontières sont respectées :

- les personnages conservent les identités et états individuels ;
- les relations et familles ne créent aucun droit politique implicite ;
- l’inventaire conserve propriété, garde et transferts d’objets ;
- l’économie conserve portefeuilles, écritures et amendes préparées ;
- l’écologie conserve régions, populations et ressources ;
- les domaines et bâtiments restent réservés au chapitre 24 ;
- les quêtes et conséquences narratives restent réservées au chapitre 25.

## 4. Corrections issues de la seconde lecture

La seconde lecture a notamment :

1. exigé un titulaire valide pour tout mandat actif ;
2. exigé un titulaire vide pour tout siège vacant ;
3. recoupé les rangs des adhésions avec la définition de faction ;
4. recoupé institution et fonction des mandats avec la faction ;
5. aligné le retour du décodeur de sections sur la sentinelle `null` documentée ;
6. supprimé vingt en-têtes génériques redondants dans les exemples fautifs et corrigés ;
7. conservé les résultats idempotents, révisions et événements après commit ;
8. confirmé qu’une accusation ne produit ni verdict ni sanction ;
9. confirmé que les sanctions externes sont préparées par leurs autorités ;
10. confirmé la restauration globale avant remplacement.

## 5. Revue statique du code

Les extraits ont été relus pour les signatures, types, paramètres, retours, sentinelles, codes `Error`, copies détachées, bornes, intervalles, révisions, idempotence, juridictions, priorités, chaîne de garde et émissions après commit.

Cette revue ne constitue pas une exécution du parseur GDScript.

## 6. Explications pédagogiques



Les **71** blocs possèdent **71** marqueurs. Les explications antérieures ont été décomposées en **283** segments techniques conservés mot pour mot, puis regroupées sous des rubriques uniques et adaptées. Les libellés génériques sont interdits ; chaque point cite un champ, une fonction, une garde, un retour, un effet, un chemin ou une relation réellement visible dans le bloc.

## 7. Règle sémantique des erreurs

La section `Erreurs fréquentes et corrections` porte le marqueur `<!-- qa:error-correction-section -->`. Chacun des dix cas contient un symptôme, un exemple fautif expliqué et un exemple corrigé expliqué.

## 8. Contextes d’utilisation

Les fichiers à créer utilisent `[VSC]`. Les contrats, flux, structures et contre-exemples utilisent `[LECTURE]`. Aucune procédure éditoriale ou commande de workflow n’est placée dans le texte lecteur.

## 9. Sources et exactitude technique

Les références moteur visent les pages officielles Godot 4.7 pour `Resource`, `RefCounted`, `Array`, `Dictionary`, `StringName`, `Time` et GDScript. Les dépendances internes renvoient aux chapitres 9, 14 à 17 et 20 à 22.

## 10. Clôture éditoriale

La dernière section synthétise les décisions retenues pour `Project Asteria`. Elle ne contient ni chemin du chapitre suivant, ni niveau GPT futur, ni instruction de production.

## 11. Réserves

- le parseur Godot 4.7.1 n’a pas été exécuté ;
- les collections typées n’ont pas été vérifiées au runtime ;
- le commit multi-autorités n’a pas été exécuté ;
- les performances aux bornes n’ont pas été mesurées ;
- les adaptateurs de juridiction et de sanctions n’ont pas été matérialisés ;
- la scène pédagogique n’a pas été instanciée ;
- le codec et la restauration n’ont pas été exécutés ;
- la reproductibilité interplateforme n’a pas été vérifiée ;
- aucun PDF n’a été construit.


Les sections pédagogiques d’erreurs conservent leur séquence sémantique directe : symptôme, exemple fautif, explication du défaut, exemple corrigé et explication de la correction. Les rubriques générales de restructuration ne sont pas appliquées à ces deux explications, afin d’éviter répétitions, sous-titres intermédiaires et commentaires génériques.

## 12. Décision

Le chapitre 23 est **accepté au niveau `static-review`**, sous les réserves runtime et PDF de fin de Livre indiquées ci-dessus.
