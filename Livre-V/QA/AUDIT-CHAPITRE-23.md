---
title: "Audit — Livre V, fiche 23 : Comparatifs des solutions"
id: "DOC-L5-QA-AUDIT-CH23"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 23
last-verified: "2026-07-29T22:44:00+02:00"
audit-date: "2026-07-29T22:44:00+02:00"
audit-level: "static-review"
validated-document: "Livre-V/CHAPITRE-23-Comparatifs-des-solutions.md"
validation-profile: "Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md"
---

# Audit de la fiche 23 — Comparatifs des solutions

## 1. Décision

**Décision : accepté au niveau `static-review`, avec réserves explicites sur toute comparaison exécutée, mesure, prix, contrat, campagne utilisateur et décision d’achat.**

La fiche respecte le profil spécialisé du Livre V : consultation non linéaire, cartes et matrices, renvois vers les propriétaires, séparation des preuves et absence de tutoriel complet recopié.

## 2. Périmètre audité

L’audit couvre :

- le contrat minimal d’un comparatif ;
- la séparation entre faits, compatibilité, mesures, évaluations qualitatives, préférences, coûts et décisions ;
- le cadrage de la question, des candidats, du statu quo et du repli ;
- les portes éliminatoires ;
- les critères, unités, échelles, directions, seuils et niveaux de preuve ;
- la pondération et les limites d’un score agrégé ;
- les données manquantes, bloquées, obsolètes et non applicables ;
- les scénarios Solo, Studio, développement, CI, runtime, production, publication et maintenance ;
- les sources, mesures et évaluations humaines ;
- le coût total, la migration, la réversibilité et la sortie ;
- l’analyse de sensibilité, les égalités et l’indétermination ;
- le rapport, le versionnage, la maintenance et le retrait.

L’audit ne qualifie aucun candidat réel et n’exécute aucune comparaison.

## 3. Métriques statiques

| Mesure | Valeur finale |
|---|---:|
| lignes du chapitre | 460 |
| titres Markdown | 20 |
| cartes `l5:card` | 13 |
| matrices `l5:matrix` | 3 |
| liens Markdown | 90 |
| renvois vers les Livres I à IV | 30 |
| liens avec fragment | 55 |
| diagrammes compacts | 8 |
| blocs clôturés | 0 |
| titres dupliqués | 0 |

## 4. Conformité au profil Livre V

| Exigence | Résultat | Observation |
|---|---|---|
| chemin canonique et identifiant stable | conforme | `DOC-L5-CH23` et chemin officiel du plan maître |
| front matter, version, date et audit | conforme | version `1.0.0`, preuve `static-review` |
| format `reference-cards` | conforme | cartes et matrices marquées |
| consultation non linéaire | conforme | index express et identifiants `CMP-*` |
| réponse rapide et limites | conforme | chaque carte substantive contient décision, porte ou limite |
| liens vers les propriétaires | conforme | fiches 02 à 22 et Livres I à IV reliés sans duplication longue |
| séparation statique/runtime | conforme | aucune comparaison exécutée revendiquée |
| absence de PDF intermédiaire | conforme | aucune chaîne PDF appelée |
| lot permanent de huit fichiers | à vérifier par CI | contrôle automatisé avant commit final |

## 5. Couverture du plan maître

| Objectif du plan | Couverture |
|---|---|
| comparer selon des critères explicites | `CMP-03`, matrice B et contrat `CMP-00` |
| séparer faits, mesures et préférence | matrice A, `CMP-07`, `CMP-08` et `CMP-09` |
| proposer des choix par scénario | `CMP-06` et matrice C |
| documenter les coûts de migration | `CMP-10` |
| fournir des tableaux comparatifs | matrices A à C |
| fournir des scénarios | `CMP-06` |
| fournir des pondérations | `CMP-04` |
| fournir des recommandations conditionnelles | matrice C et `CMP-12` |
| éviter toute recommandation absolue | principe, règles non négociables et frontière finale |
| validation reproductible et sources diverses | `CMP-03`, `CMP-07`, `CMP-08` et `CMP-11` |

## 6. Contrats structurants vérifiés

### 6.1 Portes avant score

La fiche interdit qu’un score agrégé compense :

- une incompatibilité obligatoire ;
- une licence ou provenance non qualifiée ;
- un risque de sécurité refusé ;
- une fonction essentielle absente ;
- une migration irréversible sans sauvegarde et repli.

Cette séparation prolonge la fiche 02 sans la recopier.

### 6.2 Couches de preuve séparées

La matrice A distingue :

- fait sourcé ;
- statut de compatibilité ;
- mesure ;
- évaluation qualitative ;
- préférence de scénario ;
- coût ;
- décision.

Aucune couche n’est autorisée à prouver automatiquement une autre couche.

### 6.3 Critères auditables

Chaque critère doit définir :

- identité ;
- notion mesurée ou évaluée ;
- direction favorable ;
- unité ou échelle ;
- méthode ;
- seuil ;
- preuve ;
- date ;
- limites et dépendances.

Les mots vagues tels que « meilleur », « puissant », « facile » ou « moderne » ne deviennent pas des critères sans définition observable.

### 6.4 Données manquantes visibles

La fiche conserve séparément :

- inconnu ;
- bloqué ;
- obsolète ;
- non applicable ;
- estimation ;
- mesure incertaine.

Elle interdit l’imputation silencieuse d’une note moyenne ou nulle.

### 6.5 Recommandations conditionnelles

La matrice C permet :

- référence pour un scénario ;
- choix conditionnel ;
- pilote requis ;
- maintien de l’existant ;
- migration ;
- évitement borné au périmètre ;
- égalité ;
- indétermination ;
- retrait.

Chaque sortie conserve scénario, date, versions, preuves, repli et déclencheurs de réévaluation.

## 7. Frontières avec les fiches voisines

| Source | Responsabilité conservée |
|---|---|
| fiche 02 | arbres initiaux, contraintes et méthode de décision générale |
| fiches 03 à 07 | identité, rôle, alternatives et limites des outils, moteurs et modèles |
| fiches 13 à 19 | formats, données, architecture, gameplay, graphique et audio |
| fiche 20 | diagnostic et niveaux de certitude |
| fiche 21 | protocoles, données brutes, statistiques et effet pratique |
| fiche 22 | cellules et statuts de compatibilité versionnés |
| future fiche 24 | checklists et signatures de portes |
| future fiche 25 | licences, provenance et conformité globales |
| future fiche 26 | index transversaux |
| Companion Pack | tableurs, scripts, datasets, pilotes et rapports exécutables |

## 8. Qualité éditoriale

### Points forts

- méthode immédiatement utilisable sans imposer un produit ;
- portes éliminatoires clairement séparées des pondérations ;
- statu quo et repli traités comme candidats légitimes ;
- coûts exprimés sur le cycle de vie et non réduits au prix affiché ;
- égalité et indétermination reconnues comme résultats valides ;
- analyse de sensibilité obligatoire avant promotion d’une référence ;
- frontières nettes avec benchmark et compatibilité ;
- nombreuses sources locales vers les chapitres propriétaires.

### Risques résiduels

- une organisation peut encore choisir des poids biaisés ; la justification et la sensibilité limitent ce risque sans l’annuler ;
- des données qualitatives peuvent être sur-précisées ; les ancres et distributions doivent rester visibles ;
- le coût total dépend d’hypothèses susceptibles d’évoluer ; date et horizon sont obligatoires ;
- les futurs comparatifs exécutables devront ajouter validation des formules, fixtures et contrôles d’intégrité ;
- les prix, licences, versions et offres commerciales devront être revérifiés au moment de chaque campagne réelle.

## 9. Réserves de preuve

Aucun élément suivant n’a été produit ou exécuté pour cet audit :

- installation ou lancement d’un candidat ;
- comparaison fonctionnelle ;
- benchmark CPU, GPU, mémoire, chargement, réseau ou IA ;
- calcul de score ou normalisation sur des données réelles ;
- analyse de sensibilité exécutée ;
- devis, prix courant, contrat ou coût total réel ;
- campagne utilisateur, questionnaire, entretien ou test d’ergonomie ;
- décision d’achat, de migration, de retrait ou de référence ;
- tableur, script, dataset ou rapport du Companion Pack ;
- traitement de données personnelles ou confidentielles ;
- construction PDF.

## 10. Conclusion

La fiche 23 couvre le plan maître au niveau documentaire attendu. Elle fournit une méthode de comparaison révisable, traçable et conditionnelle sans classer artificiellement les solutions du guide.

**Statut final : accepté avec zéro erreur bloquante après validation légère, sous réserve des campagnes, sources actuelles, prix, licences et décisions réelles qui restent à exécuter et à approuver.**
