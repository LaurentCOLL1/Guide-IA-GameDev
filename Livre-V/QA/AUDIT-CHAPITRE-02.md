---
title: "Audit post-création — Livre V, fiche 02"
id: "DOC-L5-AUDIT-CH02"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 2
audit-date: "2026-07-28T13:00:32+02:00"
last-verified: "2026-07-28T13:00:32+02:00"
audit-level: "static-review"
target-document: "Livre-V/CHAPITRE-02-Arbres-de-decision.md"
protocol: "Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md"
---

# Audit post-création — Fiche 02

## 1. Décision

La fiche 02 — **Arbres de décision** est acceptée au niveau `static-review` selon le protocole spécialisé du Livre V.

La décision couvre la structure non linéaire, les portes éliminatoires, les critères pondérés, les chemins AMD/CPU, les variantes Solo/Studio, les scénarios et les renvois vers les Livres I à IV. Elle ne qualifie aucun benchmark, aucune installation, aucune compatibilité matérielle exécutée et aucune décision produit réelle.

## 2. Couverture du plan maître

Les quatre objectifs sont couverts :

1. guider les choix d’outils, formats, moteurs et pipelines ;
2. expliciter critères, contraintes et conséquences ;
3. fournir des chemins AMD, CPU, Solo et Studio ;
4. signaler les situations où aucune solution unique n’existe.

Les quatre livrables sont présents :

- douze arbres ou cartes décisionnelles spécialisées ;
- trois matrices de critères, scénarios et conséquences ;
- quatre exemples de décisions conditionnelles ;
- des renvois fréquents vers les chapitres et sous-sections propriétaires.

La frontière est respectée : la fiche ne produit pas les fiches normalisées des outils du chapitre 3 et ne remplace pas les comparatifs détaillés du chapitre 23.

## 3. Structure de référence

La fiche place un index express en ouverture, puis organise les choix en unités indépendantes :

- méthode de lecture d’un arbre ;
- accélération AMD, CPU et voie expérimentale ;
- Windows natif, WSL et Docker ;
- environnements Python ;
- ComfyUI ;
- moteurs LLM et interfaces ;
- stockage et persistance ;
- transports IA ;
- production d’assets ;
- diagnostic de performance ;
- Solo et Studio ;
- publication et situations sans solution unique.

Les tables précèdent les explications courtes. Aucun long parcours narratif ou tutoriel complet n’est introduit.

## 4. Critères et conséquences

La matrice de pondération distingue les portes éliminatoires des préférences. Les critères de compatibilité, licence, fonction essentielle, reproductibilité et réversibilité peuvent invalider une option avant notation.

Chaque arbre indique, selon le sujet :

- la contrainte déterminante ;
- le choix initial ;
- la limite ou le compromis ;
- le repli ;
- la source propriétaire ;
- la mesure ou validation encore nécessaire.

Les notes et poids sont explicitement présentés comme des points de départ adaptables, pas comme des résultats objectifs.

## 5. Chemins AMD, CPU, Solo et Studio

Le chemin AMD conserve le CPU comme référence fonctionnelle et de diagnostic. Les voies DirectML, backend natif et ZLUDA sont séparées selon leur statut dans les sources du Livre I.

Le chemin Solo réduit le coût opérationnel sans modifier le cœur métier. Le chemin Studio ajoute revues, responsabilités, plateformes et portes CI sans créer une seconde architecture du jeu.

## 6. Navigation et liens

Métriques statiques :

- lignes : 344 ;
- titres : 19 ;
- fiches marquées : 14 ;
- matrices marquées : 3 ;
- liens internes : 80 ;
- renvois vers les Livres I à IV : 63 ;
- liens profonds vers des sous-sections : 32 ;
- blocs clôturés : 0 ;
- titres dupliqués : 0.

Les liens profonds visent notamment les voies d’accélération AMD, les parcours ComfyUI, les distinctions moteur/interface, les frontières de sauvegarde, l’importation Godot, le débogage et les enveloppes Solo/Studio.

## 7. Comparaison avec les chapitres voisins

La fiche 01 conserve la carte générale et les routes par besoin. La fiche 02 transforme ces routes en décisions conditionnelles.

Le chapitre 3 possédera les fiches normalisées des logiciels et outils, avec leurs rôles, versions, formats, intégrations et limites. La présente fiche choisit seulement une famille ou une voie selon un contexte.

Le chapitre 23 possédera les comparatifs détaillés, pondérations par solution et coûts de migration. La présente fiche définit la méthode de décision commune sans comparer exhaustivement tous les produits.

## 8. QA spécialisée

Le chapitre respecte `document-format: "reference-cards"` et utilise les marqueurs `l5:card` et `l5:matrix`.

Il ne contient :

- ni résultats d’apprentissage ;
- ni progression tutoriel linéaire ;
- ni série artificielle de dix diagnostics ;
- ni synthèse `Project Asteria` ;
- ni bloc de code ou commande sans valeur de consultation immédiate.

Les validateurs permanents contrôlent métadonnées, liens locaux, fragments profonds, doublons, repères éventuels et absence de PDF.

## 9. Réserves

- aucun scénario n’a été soumis à des lecteurs ou équipes réels ;
- aucune pondération n’a été calibrée par étude utilisateur ;
- aucune voie AMD, CPU, DirectML, ZLUDA, Docker ou LLM n’a été exécutée dans ce lot ;
- aucun benchmark matériel ou runtime n’est revendiqué ;
- aucun artefact du Companion Pack n’a été créé ;
- aucun PDF n’a été produit ;
- la licence globale et le balisage avancé restent ouverts.

## 10. Conclusion

La fiche 02 couvre le plan maître sous une forme consultable rapidement. Elle rend les contraintes, compromis, replis et preuves visibles, renvoie vers les tutoriels propriétaires et évite toute recommandation absolue.
