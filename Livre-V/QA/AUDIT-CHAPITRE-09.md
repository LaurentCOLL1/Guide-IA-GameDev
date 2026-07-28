---
title: "Audit — Livre V, fiche 09 : Bibliothèque de prompts"
id: "DOC-L5-QA-AUDIT-CH09"
status: "complete"
version: "1.0.0"
last-verified: "2026-07-28T19:12:00+02:00"
lang: "fr-FR"
book: "Livre V"
chapter: 9
audit-date: "2026-07-28T19:12:00+02:00"
audit-level: "static-review"
validation-authority: "livre-v-reference-profile"
---

# Audit — Fiche 09 : Bibliothèque de prompts

## 1. Décision

La fiche est conforme au profil spécialisé du Livre V sous réserve des exécutions explicitement laissées ouvertes. Elle catalogue des contrats de prompts textuels, structurés, RAG, code, visuels, audio et narratifs sans recopier les tutoriels propriétaires ni présenter des exemples comme des sorties réellement obtenues.

## 2. Périmètre contrôlé

- chemin canonique : `Livre-V/CHAPITRE-09-Bibliotheque-de-prompts.md` ;
- identifiant : `DOC-L5-CH09` ;
- version : `1.0.0` ;
- format : `reference-cards` ;
- niveau de preuve : `static-review` ;
- sources officielles évolutives revues le 28 juillet 2026 ;
- aucune compilation PDF intermédiaire.

## 3. Métriques statiques

| Mesure | Valeur |
|---|---:|
| lignes | 402 |
| titres | 18 |
| cartes `l5:card` | 13 |
| matrices `l5:matrix` | 3 |
| liens Markdown | 51 |
| renvois vers les Livres I à IV et Volume 0 | 27 |
| liens profonds vers les sources propriétaires | 27 |
| liens officiels | 7 |
| blocs clôturés | 0 |

## 4. Couverture du plan maître

| Exigence | Couverture |
|---|---|
| prompts par tâche et modèle | matrice de sélection et carte de cible exacte |
| variables et contraintes | types, bornes, confiance, délimiteurs et absence explicite |
| résultats attendus | formats, critères et états d’incertitude sans sortie inventée |
| limites, biais et sécurité | cartes par modalité et défense contre les injections |
| éviter les prompts magiques | template, instance, run, paramètres et évaluation séparés |
| templates paramétrés | treize contrats directement consultables |
| jeux de tests | douze fixtures de qualification sans résultat prérempli |
| exemples de sorties | formes attendues marquées illustratives, aucun résultat attribué à un modèle |
| critères d’évaluation | automatisation, revue humaine, variance et seuils distingués |
| modèle et version | fournisseur, snapshot, template de chat, moteur et date obligatoires |
| reproductibilité ou variance | cycle de qualification et comparaison contrôlée |

## 5. Frontières

La fiche conserve les responsabilités suivantes :

- les modèles restent aux fiches 05 à 07 ;
- les workflows et leur orchestration restent à la fiche 08 ;
- les scripts et runners restent au chapitre 10 ;
- les tutoriels détaillés restent dans les Livres I à IV ;
- les résultats de campagnes restent au chapitre 21 ;
- les compatibilités historiques restent au chapitre 22 ;
- les checklists transversales restent au chapitre 24 ;
- licences, provenance et conformité restent au chapitre 25 ;
- les paquets exécutables réels restent au Companion Pack.

## 6. Séparation définition et exécution

Chaque carte distingue template, variante, instance, requête, réponse brute, résultat interprété et décision. Aucune carte n’annonce :

- un modèle ou moteur réellement appelé ;
- une sortie JSON parsée ;
- une réponse RAG ou citation vérifiée ;
- un code généré, compilé ou testé ;
- une image, voix, transcription, musique ou effet produit ;
- une campagne d’injection, de migration ou de variance exécutée ;
- une performance, qualité ou reproductibilité mesurée.

## 7. Sécurité et gouvernance

Les contrôles couvrent les injections directes et indirectes, la séparation instruction/données, les outils autorisés, les secrets, les données personnelles, les sorties actives, les limites de ressources et les décisions critiques. Le prompt reste une couche consultative ; l’application et le workflow gardent authentification, autorisation, validation et effets.

## 8. Liens et sources

Les 27 renvois propriétaires empêchent les duplications. Les 27 fragments visent les standards de prompts, les jeux de tests LLM, le RAG, la sécurité, la narration, les prompts visuels et la chaîne audio.

Les liens externes pointent vers les documentations officielles d’OpenAI, Google, Anthropic, Ollama et OWASP revues le 28 juillet 2026. Leur présence ne constitue ni appel API, ni test de modèle, ni approbation d’une plateforme distante.

## 9. Réserves ouvertes

1. aucun modèle de langage, visuel ou audio appelé ;
2. aucun template ou dataset du Companion Pack créé ;
3. aucune instance résolue ni requête envoyée ;
4. aucune réponse brute, sortie structurée ou appel d’outil produit ;
5. aucun parse, test de code, RAG, génération visuelle ou audio exécuté ;
6. aucune campagne de variance, migration ou régression réalisée ;
7. aucun test d’injection ou de sécurité runtime réalisé ;
8. aucune donnée personnelle, secrète ou tierce manipulée ;
9. aucune mesure de tokens, latence, coût, mémoire ou qualité produite ;
10. aucune note humaine, approbation juridique ou décision de production enregistrée ;
11. aucun artefact permanent du Companion Pack matérialisé ;
12. aucun PDF produit ; licence globale et balisage avancé ouverts.

## 10. Critère d’acceptation

La fiche est acceptée au niveau `static-review` lorsque les validateurs permanents confirment structure, métadonnées, liens locaux, marqueurs Livre V, liens profonds, repères et absence de PDF. Les prompts eux-mêmes restent `defined` jusqu’à leur exécution sur un modèle exact et un jeu de tests représentatif.
