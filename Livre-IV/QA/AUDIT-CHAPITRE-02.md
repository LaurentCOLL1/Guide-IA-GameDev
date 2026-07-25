---
title: "Audit post-création — Livre IV, chapitre 2"
id: "DOC-L4-QA-AUDIT-CH02"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L4-CH02"
chapter-version: "1.0.0"
audit-date: "2026-07-25T21:32:27+02:00"
last-verified: "2026-07-25T21:32:27+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 2

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de matérialisation de la charte QA, du registre des risques, de la matrice risques/contrôles, des portes qualité, des campagnes, des revues spécialisées et des exercices de récupération.

Aucune campagne fonctionnelle, artistique, sécurité, accessibilité, compatibilité, restauration ou publication de `Project Asteria` n’est revendiquée comme exécutée. Les commandes, schémas et scripts restent des modèles pédagogiques relus statiquement.

## 2. Périmètre comparé au plan maître

Le chapitre couvre les objectifs du plan maître :

- niveaux de test, responsabilités et portes qualité ;
- distinction entre prévention, détection et correction ;
- risques, priorités et calendrier ;
- critères d’entrée et de sortie ;
- articulation des axes documentaire, technique, artistique et produit.

Les livrables sont préparés comme contrats : charte QA, modèle de qualité, registre des risques, matrice risques/contrôles, calendrier, rôles Solo/Studio, modèles de rapports et validateur structurel. Leur matérialisation dans le projet fil rouge reste en réserve.

## 3. Frontières contrôlées

- le chapitre 1 conserve le catalogue de métriques, les simulations d’équilibrage et les rapports de décision associés ;
- le chapitre 3 conservera les cas de test, fixtures, scènes, suites manuelles et automatisées et matrices de couverture détaillées ;
- le chapitre 4 conservera la reproduction et le diagnostic des anomalies ;
- le chapitre 5 conservera la politique d’observabilité produit ;
- les chapitres 6 à 10 conserveront les campagnes de profilage et d’optimisation ;
- les chapitres 13 à 17 conserveront sécurité réseau, DevOps, packaging et publication spécialisés ;
- aucune porte qualité ne modifie directement un système de gameplay ;
- aucun pipeline ou score unique ne reçoit l’autorité de publication.

## 4. Contrôles pédagogiques

- objectifs, résultats d’apprentissage, prérequis et frontières explicités ;
- vocabulaire qualité, QA, contrôle, test, risque, porte, preuve, réserve, dérogation, sévérité et priorité défini ;
- modèles de qualité, niveaux et familles de contrôle documentés ;
- prévention, détection et correction séparées ;
- registre des risques et politique de classement expliqués ;
- couverture explicite des risques critiques par matrice ;
- six portes et leurs critères d’entrée/sortie définis ;
- statuts `PASS`, `PASS_WITH_RESERVATIONS`, `HOLD` et `REJECT` distingués ;
- rôles Solo et Studio, RACI et indépendance documentés ;
- calendrier, environnements, baselines, triage, stop-ship et dérogations couverts ;
- QA documentaire, technique, artistique et produit reliées ;
- accessibilité, sécurité, données assistées et récupérabilité intégrées ;
- indicateurs avec dénominateurs et modèles de rapports fournis ;
- validateur Python structurel et commande PowerShell expliqués ;
- cinquante-huit blocs possèdent un repère et une explication ;
- dix diagnostics suivent la séquence sémantique complète ;
- sources officielles fournies sous forme de liens Markdown cliquables.

## 5. Contrôles documentaires

- lignes : 2204 ;
- titres : 61 ;
- blocs code ou données : 58 ;
- blocs significatifs : 58 ;
- marqueurs d’explication : 58 ;
- explications structurées hors diagnostics : 38 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- exemples corrigés expliqués : 10 ;
- titres dupliqués : 0 ;
- blocs significatifs dupliqués : 0 ;
- paragraphes longs dupliqués : 0 ;
- synthèse opérationnelle `Project Asteria` présente ;
- références techniques sous forme de liens Markdown cliquables ;
- absence de recommandation GPT, de prochaine action et de chaîne d’export du guide dans le texte lecteur.

## 6. Exactitude technique

Le script Python utilise `dataclasses`, `datetime`, `typing`, listes et ensembles de la bibliothèque standard. La date est injectée dans `expired_waiver_ids()` au lieu d’être lue implicitement, ce qui maintient le déterminisme du contrôle.

Les valeurs de probabilité, impact et détectabilité sont déclarées ordinales. Le chapitre refuse de présenter leur multiplication comme une mesure scientifique. Les portes consomment plusieurs domaines et la décision finale reste humaine.

Les termes `RACI`, `stop-ship`, baseline, dérogation et risque résiduel sont définis dans leur usage opérationnel. Les exemples ne prétendent pas constituer une certification ou un conseil juridique personnalisé.

## 7. Contrôle des doublons et des frontières

Aucun titre, bloc significatif ou paragraphe long n’est dupliqué.

Les sujets voisins restent distincts :

- métriques et équilibrage : chapitre 1 ;
- cas fonctionnels et régression : chapitre 3 ;
- reproduction des anomalies : chapitre 4 ;
- observabilité : chapitre 5 ;
- profilage : chapitres 6 à 10 ;
- sécurité réseau et exploitation : chapitres 13 à 17.

## 8. Réserves ouvertes

- charte `AST-QA-CHARTER-001` non matérialisée ;
- profil de qualité non approuvé ;
- registre des risques non créé ;
- matrice risques/contrôles non créée ;
- calendrier et politiques de portes non créés ;
- aucune campagne fonctionnelle ou de non-régression exécutée ;
- aucune revue artistique, accessibilité ou sécurité exécutée ;
- aucun exercice de restauration ou retour arrière exécuté ;
- aucun environnement ou build candidat qualifié ;
- aucune décision de porte ou de publication approuvée ;
- aucune mesure runtime produite ;
- licence globale de collection non définie ;
- balisage d’accessibilité de l’export final toujours ouvert.

## 9. Conclusion

Le chapitre satisfait le périmètre du plan maître. Les validations documentaires et statiques ont réussi ; il est accepté au niveau `static-review` avec les réserves d’exécution et de matérialisation listées ci-dessus.
