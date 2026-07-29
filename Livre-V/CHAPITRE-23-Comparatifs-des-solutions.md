---
title: "Livre V — Fiche 23 : Comparatifs des solutions"
id: "DOC-L5-CH23"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 23
last-verified: "2026-07-29T22:44:00+02:00"
audit-status: "complete"
audit-date: "2026-07-29T22:44:00+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-23.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "conditional-solution-comparisons-criteria-weighting-migration-and-reversibility"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-python:
  implementation: "CPython"
  version: "3.14.6"
  fallback-version: "3.13.14"
  qualification-status: "inherited-provisional"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Comparatifs des solutions

> **Type de document :** contrats de comparaison, matrices de critères, méthodes de pondération, scénarios et recommandations conditionnelles.
> **Lecture :** éliminer d’abord les options qui violent une contrainte, définir ensuite les critères et les preuves, comparer par scénario, puis tester la robustesse de la conclusion.
> **Principe :** une solution n’est pas « meilleure » en soi ; elle peut être préférable pour un besoin, un environnement, une période, une organisation et un niveau de preuve nommés.

## Index express

| Besoin | Ouvrir |
|---|---|
| définir un comparatif complet | [CMP-00](#cmp-00--contrat-minimal-dun-comparatif) |
| séparer fait, mesure, préférence et décision | [Matrice A](#matrice-a--couches-dinformation-et-autorités) |
| cadrer la décision et les candidats | [CMP-01](#cmp-01--question-périmètre-et-candidats) |
| appliquer les portes éliminatoires | [CMP-02](#cmp-02--éligibilité-portes-et-exclusions) |
| définir critères, échelles et directions | [CMP-03](#cmp-03--critères-échelles-et-directions) |
| trouver le propriétaire de chaque critère | [Matrice B](#matrice-b--familles-de-critères-et-sources-propriétaires) |
| pondérer sans masquer les contraintes | [CMP-04](#cmp-04--pondérations-scores-et-limites) |
| traiter données manquantes et normalisation | [CMP-05](#cmp-05--données-manquantes-normalisation-et-incertitude) |
| comparer par scénario ou profil | [CMP-06](#cmp-06--scénarios-profils-et-variantes) |
| qualifier les faits et les sources | [CMP-07](#cmp-07--faits-sources-et-traçabilité) |
| intégrer les mesures sans surinterpréter | [CMP-08](#cmp-08--mesures-distributions-et-effet-pratique) |
| encadrer avis, ergonomie et préférences | [CMP-09](#cmp-09--évaluation-qualitative-préférences-et-biais) |
| savoir quelle recommandation est permise | [Matrice C](#matrice-c--sorties-de-décision-et-déclarations-permises) |
| calculer coût total, migration et sortie | [CMP-10](#cmp-10--coût-total-migration-réversibilité-et-sortie) |
| vérifier sensibilité, égalités et robustesse | [CMP-11](#cmp-11--sensibilité-robustesse-égalités-et-indétermination) |
| publier, maintenir et retirer un comparatif | [CMP-12](#cmp-12--rapport-versionnage-maintenance-et-retrait) |

## Règles non négociables

- une porte obligatoire précède toute pondération ;
- une donnée absente reste absente et ne reçoit pas automatiquement une note moyenne ou nulle ;
- une mesure conserve son protocole, son environnement, sa date et son incertitude ;
- une préférence est attribuée à un profil ou à un évaluateur, jamais déguisée en fait ;
- un score agrégé ne remplace pas les valeurs brutes, les réserves et les coûts de sortie ;
- une recommandation reste conditionnelle et peut légitimement conclure `indéterminé`, `égalité` ou `pilote requis`.

---

<!-- l5:card -->
## CMP-00 — Contrat minimal d’un comparatif

| Champ | Règle |
|---|---|
| identité | identifiant stable, version, propriétaire, date et horizon de révision |
| décision | action concrète à prendre : adopter, conserver, migrer, tester, retirer ou différer |
| périmètre | besoin, population, plateforme, équipe, budget, contraintes et durée d’usage |
| candidats | versions exactes, éditions, configurations et variantes réellement comparables |
| portes | contraintes obligatoires de compatibilité, licence, sécurité, fonction et réversibilité |
| critères | définition, unité, direction favorable, source, méthode et échelle |
| scénarios | profils Solo, Studio, développement, CI, runtime, archive ou usage spécialisé |
| poids | valeurs fixées avant notation, justification et propriétaire du scénario |
| preuves | faits sourcés, mesures, tests, revues humaines, statuts et dates |
| données manquantes | traitement explicite, interdiction d’inventer ou de masquer l’absence |
| coûts | acquisition, matériel, installation, formation, exploitation, maintenance, migration et sortie |
| analyse | scores détaillés, dominances, sensibilité, égalités, incertitude et réserves |
| recommandation | choix conditionnel, alternatives, repli, déclencheurs de réévaluation et approbation |
| historique | changements de candidats, poids, sources, résultats, décisions et motifs |

**Réponse rapide :** la [méthode de décision](CHAPITRE-02-Arbres-de-decision.md#dec-00--lire-un-arbre-sans-transformer-une-préférence-en-fait) élimine les options non admissibles ; le [contrat de benchmark](CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md#bmk-00--contrat-minimal-dun-benchmark) possède les mesures ; la [cellule de compatibilité](CHAPITRE-22-Matrices-de-compatibilite.md#comp-00--contrat-dune-cellule-de-compatibilité) possède les relations versionnées. Cette fiche assemble ces preuves pour une décision sans les remplacer.

**Diagramme compact :** `besoin → portes → candidats admissibles → critères figés → preuves → scénarios → sensibilité → recommandation conditionnelle`.

**Niveau de preuve :** `static-review`. Aucun outil, modèle, backend, format ou service n’est classé par résultat exécuté dans cette fiche.

---

<!-- l5:matrix -->
## Matrice A — Couches d’information et autorités

| Couche | Question | Autorité | Exemple de sortie | Interdit |
|---|---|---|---|---|
| fait | que déclare ou contient l’objet ? | documentation officielle, manifeste, licence, version ou source propriétaire | plateforme annoncée, format accepté, fonctionnalité documentée | transformer une annonce en test local |
| compatibilité | cette combinaison et cette opération sont-elles qualifiées ? | [fiche 22](CHAPITRE-22-Matrices-de-compatibilite.md#matrice-a--légende-à-trois-axes) et test propriétaire | `official + workflow_pass + conditional` | fusionner les trois axes en un symbole |
| mesure | quelle grandeur a été observée ? | [fiche 21](CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md#bmk-08--statistiques-dispersion-et-incertitude) et données brutes | distribution, intervalle, taux d’échec, mémoire | retenir seulement la meilleure valeur |
| évaluation qualitative | comment un profil juge-t-il l’usage ? | protocole de revue, critères et évaluateurs identifiés | clarté, ergonomie, contrôlabilité, qualité perçue | présenter un avis comme universel |
| préférence | quelle importance un scénario donne-t-il à chaque critère ? | propriétaire du scénario et pondérations datées | priorité à la maintenance en Solo ou à l’automatisation en Studio | changer les poids après lecture des scores |
| coût | quelles ressources sont engagées pendant le cycle de vie ? | estimation sourcée, contrat, inventaire et historique | euros, heures, matériel, dépendances et coût de sortie | confondre prix d’achat et coût total |
| décision | quelle option est retenue sous quelles conditions ? | responsable nommé, portes et preuves consultables | référence, pilote, maintien, migration ou différé | recommander sans périmètre ni repli |

**Décision :** conserver les couches séparées dans le rapport. Une même cellule peut afficher un fait, une mesure et une préférence, mais leur provenance et leur niveau de preuve restent visibles.

---

<!-- l5:card -->
## CMP-01 — Question, périmètre et candidats

| Élément | Formulation utile | Formulation à éviter |
|---|---|---|
| décision | « quel moteur retenir pour servir un modèle local dans le profil Studio S pendant douze mois ? » | « quel est le meilleur moteur ? » |
| fonction essentielle | capacité sans laquelle le candidat est hors périmètre | liste de souhaits non hiérarchisée |
| population | utilisateur Solo, équipe, joueur, opérateur CI ou mainteneur | « tout le monde » |
| environnement | OS, matériel, réseau, build, versions et contraintes | « machine moderne » |
| candidats | solutions plausibles après revue initiale, versions et éditions nommées | noms de produits sans configuration |
| horizon | pilote, production courante, migration ou archive | comparaison sans durée d’usage |
| statu quo | option « conserver l’existant » avec coûts et risques | forcer un changement |
| option minimale | repli qui préserve la fonction essentielle | candidat ajouté uniquement pour faire nombre |
| décision différée | données requises et date de réexamen | absence de conclusion masquée par une moyenne |

**Réponse rapide :** les [arbres de décision](CHAPITRE-02-Arbres-de-decision.md) définissent les familles plausibles ; les [fiches des outils](CHAPITRE-03-Fiches-des-logiciels-et-outils.md) et des [moteurs/backends](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md) identifient les rôles. Les modèles, workflows et formats restent dans les [fiches 05 à 08](CHAPITRE-05-Fiches-des-modeles-de-langage.md) et la [fiche 13](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md).

**Diagramme compact :** `décision nommée → fonction essentielle → contraintes → horizon → candidats exacts + statu quo + repli`.

**Limite :** comparer un moteur, une interface et un modèle comme s’ils remplissaient le même rôle produit un classement sans sens.

---

<!-- l5:card -->
## CMP-02 — Éligibilité, portes et exclusions

| Porte | Preuve minimale | Sortie si non satisfaite |
|---|---|---|
| fonction essentielle | capacité démontrée ou déclarée dans la portée requise | exclu ou pilote ciblé |
| compatibilité | cellule directionnelle et versions nommées | non admissible pour ce scénario |
| licence et provenance | licence, droits, redistribution, attribution et source | blocage jusqu’à qualification |
| sécurité et confidentialité | surface, données, secrets, réseau et responsabilités | refus ou architecture de confinement |
| données et migration | sauvegarde, schéma, conversion, réversibilité et restauration | migration interdite ou pilote sur copie |
| plateforme et export | éditeur, build, package, installation et cible distincts | limitation au développement ou à une plateforme |
| maintenance | version épinglable, dépendances, propriétaire et voie de mise à jour | réserve forte ou retrait du parcours principal |
| budget dur | plafond financier, matériel, mémoire, délai ou capacité humaine | exclusion, réduction de périmètre ou repli |
| conformité organisationnelle | approbation, audit, hébergement ou support requis | décision suspendue |

**Réponse rapide :** la [matrice de pondération](CHAPITRE-02-Arbres-de-decision.md#matrice-a--pondérer-sans-masquer-les-portes-éliminatoires) interdit qu’un bon score compense une contrainte obligatoire. La [politique de compatibilité](../Volume-0/CHAPITRE-09-Politique-de-compatibilite.md#2-niveaux-de-compatibilité), la [sécurité de production/runtime](../Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md) et la [provenance des assets](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md) restent propriétaires des portes spécialisées.

**Porte :** une option exclue reste visible avec son motif, sa source et la condition qui permettrait de la réévaluer. Elle ne reçoit pas une note artificielle destinée à la maintenir dans le classement.

---

<!-- l5:card -->
## CMP-03 — Critères, échelles et directions

| Champ du critère | Règle |
|---|---|
| identifiant | stable, distinct du libellé affiché |
| définition | une seule notion, compréhensible sans interprétation implicite |
| famille | fonction, compatibilité, qualité, performance, coût, risque, maintenance ou préférence |
| direction | plus bas, plus haut, proche d’une cible, dans une plage ou booléen |
| unité | unité physique, euros, heures, taux, classe ordinale ou statut |
| méthode | source, test, calcul, revue ou questionnaire |
| échelle | bornes, significations et traitement de `non applicable` |
| seuil | porte, différence pratique ou niveau acceptable |
| qualité de preuve | documentation, test, répétition, revue indépendante ou décision |
| date | collecte, vérification, expiration et version associée |
| dépendances | critères corrélés, double comptage possible et préconditions |
| réserve | population, scénario et cas non couverts |

**Réponse rapide :** définir un critère avant de regarder les candidats. La [question mesurable](CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md#bmk-01--question-hypothèse-et-décision) impose métrique primaire, direction et seuil pratique ; la [granularité de compatibilité](CHAPITRE-22-Matrices-de-compatibilite.md#comp-01--axes-identité-et-granularité) impose objet, cible et opération exacts.

**Diagramme compact :** `critère → définition → direction → unité/échelle → méthode → seuil → preuve → réserve`.

**Limite :** « facilité », « qualité », « puissance » ou « moderne » ne sont pas des critères tant que leurs observations et leurs limites ne sont pas définies.

---

<!-- l5:matrix -->
## Matrice B — Familles de critères et sources propriétaires

| Famille | Critères possibles | Source propriétaire | Contrôle contre le double comptage |
|---|---|---|---|
| fonction et adéquation | capacités requises, limites, workflows, API | [outils](CHAPITRE-03-Fiches-des-logiciels-et-outils.md), [moteurs](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md), [patrons](CHAPITRE-16-Patrons-d-architecture.md) | une capacité n’est pas aussi notée comme ergonomie si l’observation est identique |
| compatibilité | OS, GPU, backend, version, format, import, export | [matrices de compatibilité](CHAPITRE-22-Matrices-de-compatibilite.md#matrice-b--routage-par-famille-de-compatibilité) | déclaration officielle et test local séparés |
| performance et ressources | latence, débit, mémoire, chargement, stabilité | [benchmarks](CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md#matrice-a--routage-par-famille-de-mesure), [profilage CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md#8-mesurer-plusieurs-distributions-pas-un-seul-nombre), [GPU](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md#7-distinguer-cpu-de-rendu-gpu-et-attente), [mémoire](../Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md#7-les-quatre-questions-dune-enquête-mémoire) | ne pas ajouter trois fois la même durée sous latence, vitesse et performance |
| qualité du résultat | exactitude fonctionnelle, rendu, audio, sortie IA, pertes | [tests](../Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md#6-contrat-dun-cas), [3D](CHAPITRE-18-Reference-graphique-et-3D.md), [audio](CHAPITRE-19-Reference-audio.md), [modèles](CHAPITRE-05-Fiches-des-modeles-de-langage.md) | séparer qualité objective, conformité et préférence humaine |
| données et formats | schéma, transaction, conversion, round-trip, migration | [formats](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#matrice-a--sélection-par-besoin), [SQLite](CHAPITRE-14-Schemas-SQLite-et-migrations.md), [sauvegardes](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#3-périmètre-et-frontières) | une réussite de parse n’est pas une réussite métier |
| sécurité et confidentialité | surface, permissions, secrets, données, exposition | [séparation IA](../Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md), [serveurs](../Livre-IV/CHAPITRE-13-Serveurs-dedies-et-securite-reseau.md) | une absence d’incident n’est pas une preuve de sécurité |
| exploitation | installation, diagnostic, automatisation, sauvegarde, reprise | [scripts](CHAPITRE-10-Bibliotheque-de-scripts-et-recettes-de-code.md), [observabilité](../Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md#8-distinguer-événements-métriques-et-traces), [DevOps](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#1-rôle-du-chapitre), [reprise](../Livre-IV/CHAPITRE-15-Sauvegardes-migrations-et-reprise-apres-incident.md) | ne pas confondre automatisable et déjà automatisé |
| publication et plateformes | export, packaging, distribution, correctifs | [exports](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md#4-prérequis-et-frontières), [publication](../Livre-IV/CHAPITRE-17-Publication-et-distribution.md), [mises à jour](../Livre-IV/CHAPITRE-20-Correctifs-mises-a-jour-et-retour-arriere.md) | distinguer build, package, publication et rollback |
| maintenance et pérennité | cadence, dépendances, support, archive, reconstruction | [maintenance](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md) | popularité actuelle et pérennité ne sont pas synonymes |
| licence et provenance | usage, redistribution, attribution, consentement | [provenance](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md) et future [fiche 25](#frontières-de-la-fiche) | une licence non qualifiée devient une porte, pas une note |
| coût total et migration | euros, temps, matériel, formation, dépendances, sortie | [CMP-10](#cmp-10--coût-total-migration-réversibilité-et-sortie) et inventaires propriétaires | prix affiché et coût de cycle de vie séparés |

**Décision :** chaque critère pointe vers une source propriétaire. Le comparatif ne devient pas une nouvelle autorité technique sur les outils, formats, modèles ou plateformes.

---

<!-- l5:card -->
## CMP-04 — Pondérations, scores et limites

| Règle | Application |
|---|---|
| poids préalables | fixer et dater les poids avant de noter les candidats |
| scénarios séparés | un profil Solo et un profil Studio possèdent des poids distincts |
| échelle courte | utiliser peu de niveaux, chacun défini par une preuve observable |
| score détaillé | conserver note, poids, valeur brute, source et justification |
| portes indépendantes | ne jamais compenser une incompatibilité, une licence bloquante ou un risque interdit |
| corrélations | réduire ou regrouper les critères qui mesurent le même phénomène |
| non-applicable | exclure du dénominateur selon une règle commune, sans avantager silencieusement |
| manque de preuve | signaler une incertitude ou demander un pilote, pas inventer une note |
| arrondis | calculer avec précision interne et afficher un arrondi non trompeur |
| score global | outil de synthèse, jamais preuve autonome ni verdict universel |

**Réponse rapide :** la [matrice de départ Solo/Studio](CHAPITRE-02-Arbres-de-decision.md#matrice-a--pondérer-sans-masquer-les-portes-éliminatoires) fournit des priorités candidates, pas des poids permanents. Une pondération peut utiliser une somme normalisée, une méthode ordinale ou une comparaison par paires, à condition que la règle soit fixée et lisible.

**Diagramme compact :** `portes satisfaites → poids figés → valeurs et preuves → scores détaillés → agrégat → sensibilité → décision humaine`.

**Limite :** multiplier des notes ordinales par des poids donne un indice de décision, pas une mesure physique. Deux écarts de note ne sont pas automatiquement équivalents.

---

<!-- l5:card -->
## CMP-05 — Données manquantes, normalisation et incertitude

| Situation | Traitement recommandé | Traitement interdit |
|---|---|---|
| valeur inconnue | `unknown`, source attendue et action de collecte | note moyenne par défaut |
| test bloqué | `blocked`, précondition et risque visibles | convertir en échec |
| donnée obsolète | `stale`, date et changement invalidant | conserver comme valeur actuelle |
| non applicable | exclure selon une règle annoncée | noter zéro ou maximum automatiquement |
| candidats mesurés sur unités différentes | convertir seulement avec relation valide et documentée | normalisation arbitraire |
| bornes ouvertes | afficher la limite et éviter le classement fin | inventer une valeur centrale |
| estimation | plage, hypothèses, source et confiance | valeur unique sans réserve |
| mesure incertaine | distribution, dispersion, intervalle ou statut | comparer seulement les moyennes |
| échelle qualitative | ancres observables et évaluateurs identifiés | nombres décoratifs sans définition |
| données incompatibles | suspendre le critère ou refaire la collecte | forcer une agrégation |

**Réponse rapide :** les statuts `not_assessed`, `blocked`, `stale` et `not_applicable` de la [fiche 22](CHAPITRE-22-Matrices-de-compatibilite.md#matrice-a--légende-à-trois-axes) restent distincts. Les exclusions, valeurs aberrantes et données manquantes mesurées suivent la [fiche 21](CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md#bmk-09--valeurs-aberrantes-données-manquantes-et-exclusions).

**Porte :** si une donnée manquante peut inverser la décision sur un critère important, la sortie correcte est `pilote requis` ou `indéterminé`, pas un classement provisoire présenté comme stable.

---

<!-- l5:card -->
## CMP-06 — Scénarios, profils et variantes

| Profil ou scénario | Questions dominantes |
|---|---|
| Solo local | installation, coût de maintenance, diagnostic, repli manuel, temps d’apprentissage |
| Studio | automatisation, rôles, audit, intégration, support, partage et continuité |
| développement | itération, visibilité des erreurs, outils, hot reload et compatibilité éditeur |
| CI | headless, reproductibilité, temps de job, cache, secrets et artefacts |
| runtime joueur | stabilité, mémoire, latence, accessibilité, offline et récupération |
| production d’assets | provenance, batch, qualité, formats, réimportation et validation humaine |
| service IA local | modèle, backend, API, mémoire, sécurité et repli déterministe |
| publication | plateformes, SDK, signature, package, installation et support |
| maintenance longue | dépendances, migration, archivage, reconstruction et succession |
| laboratoire | apprentissage ciblé, isolation, budget d’échec et absence de dépendance centrale |

**Réponse rapide :** un comparatif produit une vue par scénario, pas un classement unique. L’[architecture Solo/Studio](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md#3-un-produit-deux-enveloppes-opérationnelles), les [outils natifs, WSL ou Docker](CHAPITRE-02-Arbres-de-decision.md#dec-02--windows-natif-wsl-ou-docker) et les [profils de compatibilité](../Volume-0/CHAPITRE-09-Politique-de-compatibilite.md#3-environnement-matériel-de-référence) illustrent des contextes qui changent les poids sans changer les faits.

**Diagramme compact :** `mêmes candidats + mêmes faits → poids et portes par scénario → résultats distincts → recommandations conditionnelles distinctes`.

**Limite :** créer trop de scénarios peut masquer l’absence de décision. Regrouper ceux dont les contraintes, poids et preuves sont réellement identiques.

---

<!-- l5:card -->
## CMP-07 — Faits, sources et traçabilité

| Source | Usage permis | Réserve obligatoire |
|---|---|---|
| documentation officielle | fonction, plateforme, version, limite et politique publiées | portée et date |
| licence ou contrat | droits et obligations connus | qualification juridique non revendiquée hors compétence |
| notes de version | ajout, rupture, correction ou retrait | effets indirects possibles |
| dépôt, commit ou digest | identité technique et historique | branche, fork et build distincts |
| fiche du Livre V | synthèse et routage vers le propriétaire | niveau souvent `static-review` |
| chapitre des Livres I à IV | méthode, contexte, frontière et validation | ne prouve pas une exécution absente |
| test ou benchmark | résultat dans un environnement précis | protocole, données brutes et incertitude |
| issue ou forum | symptôme, piste ou cas communautaire | non autoritatif sans reproduction ou source |
| offre commerciale | prix, conditions et service annoncés | date, taxes, région, durée et évolution possibles |
| expertise humaine | contexte, risque et compromis | auteur, rôle, conflit d’intérêts et date |

**Réponse rapide :** la [traçabilité de compatibilité](CHAPITRE-22-Matrices-de-compatibilite.md#comp-02--sources-preuves-et-traçabilité) et le [catalogue diagnostique](CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md) interdisent de promouvoir une source isolée au-delà de ce qu’elle démontre. Les faits susceptibles d’évoluer portent version, date et URL ou référence locale.

**Intégrité :** chaque cellule du comparatif conserve `criterion_id`, `candidate_id`, valeur, unité, source, date, preuve, statut, auteur du jugement éventuel et réserve.

**Limite :** le nombre de sources n’est pas un score de vérité. La diversité sert à contrôler les angles morts, pas à voter entre documents.

---

<!-- l5:card -->
## CMP-08 — Mesures, distributions et effet pratique

| Élément | Règle de comparaison |
|---|---|
| protocole | identique ou différence explicitement justifiée entre candidats |
| métrique primaire | définie avant la campagne et liée à la décision |
| distribution | médiane, percentiles, dispersion et cas extrêmes selon le domaine |
| répétitions | runs indépendants et observations internes distingués |
| environnement | matériel, OS, pilote, versions, charge et instrumentation |
| qualité | oracle fonctionnel ou humain séparé de la performance |
| effet pratique | seuil qui change la décision, pas seulement différence numérique |
| incertitude | intervalle, plage, statut ou réserve adaptée |
| données brutes | conservées avec exclusions et transformations |
| invalidation | changement de version, protocole, scénario ou plateforme enregistré |

**Réponse rapide :** appliquer la [fiche 21](CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md), notamment la [comparaison baseline/candidate](CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md#bmk-10--comparaison-effet-et-signification-pratique). Les propriétaires spécialisés restent le [CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md#8-mesurer-plusieurs-distributions-pas-un-seul-nombre), le [GPU](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md#7-distinguer-cpu-de-rendu-gpu-et-attente), la [mémoire](../Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md#7-les-quatre-questions-dune-enquête-mémoire), les [chargements](../Livre-IV/CHAPITRE-09-Chargements-streaming-et-gestion-des-ressources.md#8-budgets-de-chargement) et les [systèmes de jeu](../Livre-IV/CHAPITRE-10-Optimisation-des-scenes-scripts-et-systemes-de-jeu.md#7-classer-le-coût-avant-de-modifier).

**Porte :** une option plus rapide mais incorrecte, instable, non autorisée ou non compatible ne gagne pas le comparatif. Les portes fonctionnelles et de qualité précèdent le score de performance.

**Limite :** une différence statistique ne devient pas automatiquement un avantage perceptible, économique ou opérationnel.

---

<!-- l5:card -->
## CMP-09 — Évaluation qualitative, préférences et biais

| Élément | Contrôle |
|---|---|
| question | une notion par item : clarté, contrôlabilité, charge cognitive ou qualité perçue |
| ancres | exemples observables pour chaque niveau de l’échelle |
| évaluateur | rôle, expérience, besoins d’accessibilité et exposition antérieure |
| ordre | randomiser ou contrebalancer lorsque l’ordre peut influencer |
| anonymisation | masquer la solution si possible et pertinent |
| répétition | revoir plusieurs tâches ou échantillons plutôt qu’une impression unique |
| désaccord | conserver distribution, commentaires et minorité pertinente |
| préférence | rattacher au scénario et au profil, pas à la vérité technique |
| conflit d’intérêts | déclarer relation commerciale, contribution ou préférence préalable |
| décision | ne pas convertir un vote en preuve de sécurité, licence ou compatibilité |

**Réponse rapide :** les revues humaines complètent les tests, notamment pour les [assets](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md#1-rôle-du-chapitre), l’[accessibilité](../Livre-IV/CHAPITRE-18-Accessibilite.md), la [localisation](../Livre-IV/CHAPITRE-19-Localisation-et-internationalisation.md), la [référence graphique](CHAPITRE-18-Reference-graphique-et-3D.md) et la [référence audio](CHAPITRE-19-Reference-audio.md). Elles ne remplacent ni licence, ni mesure, ni test fonctionnel.

**Porte :** une préférence majoritaire peut être refusée si elle exclut un besoin obligatoire d’accessibilité, de sécurité ou de conformité.

**Limite :** une note qualitative précise à deux décimales reste une synthèse ordinale si l’échelle ne possède pas de distance mesurable.

---

<!-- l5:matrix -->
## Matrice C — Sorties de décision et déclarations permises

| Sortie | Conditions minimales | Formulation permise | Formulation interdite |
|---|---|---|---|
| `reference_for_scenario` | portes satisfaites, preuves suffisantes, scénario et repli nommés | « référence pour le scénario S jusqu’à réévaluation » | « meilleure solution » |
| `conditional_choice` | avantages ciblés, limites et conditions visibles | « préférable si C1 et C2 sont vraies » | « recommandée pour tous » |
| `pilot_required` | donnée importante manquante ou risque réversible à tester | « exécuter le pilote P avant décision » | « probablement compatible » |
| `keep_current` | migration sans bénéfice pratique démontré ou risque supérieur | « conserver l’existant dans l’horizon H » | « l’existant est supérieur en soi » |
| `migrate` | bénéfice pratique, plan, sauvegarde, repli et coût acceptés | « migrer par étapes avec portes G » | « mettre à jour car plus récent » |
| `avoid_for_scope` | porte violée ou coût/risque non acceptable dans le périmètre | « éviter pour S, réévaluer si E change » | « inutilisable partout » |
| `tie` | candidats équivalents dans la précision et les critères retenus | « égalité ; choisir selon préférence secondaire documentée » | inventer un vainqueur par arrondi |
| `indeterminate` | preuves incompatibles, manquantes ou trop incertaines | « aucune conclusion défendable actuellement » | masquer l’incertitude par un score moyen |
| `retire` | support, sécurité, reproductibilité ou voie de migration insuffisants | « retirer du parcours actif, historique conservé » | supprimer sans successeur ni archive |

**Décision :** toute sortie nomme scénario, date, versions, preuves, approbateur, repli et déclencheurs de réévaluation. Une recommandation est un contrat révisable, pas une propriété éternelle du candidat.

---

<!-- l5:card -->
## CMP-10 — Coût total, migration, réversibilité et sortie

| Famille de coût | Questions à enregistrer |
|---|---|
| acquisition | licence, abonnement, hébergement, support et conditions tarifaires datées |
| matériel | CPU, GPU, RAM, stockage, périphériques, énergie et renouvellement |
| installation | préparation, dépendances, comptes, sécurité et environnement |
| apprentissage | documentation, formation, expérimentation et perte de productivité |
| intégration | adaptateurs, données, API, CI, exports, tests et observabilité |
| exploitation | temps humain, incidents, sauvegardes, monitoring et support |
| maintenance | mises à jour, dépendances, correctifs, conformité et documentation |
| migration | inventaire, conversion, double exploitation, validation et communication |
| interruption | indisponibilité, retour arrière, perte de capacité et risque de calendrier |
| sortie | export des données, formats ouverts, suppression, archive et remplacement |
| dette évitée | simplification réelle, dépendance supprimée ou risque réduit |
| horizon | pilote, un an, durée de projet ou conservation historique |

**Réponse rapide :** comparer le coût total sur un horizon commun, en euros et en temps lorsque ces unités sont pertinentes, sans additionner des grandeurs différentes sans convention. Les migrations suivent les [sauvegardes et reprises](../Livre-IV/CHAPITRE-15-Sauvegardes-migrations-et-reprise-apres-incident.md), les [correctifs et retours arrière](../Livre-IV/CHAPITRE-20-Correctifs-mises-a-jour-et-retour-arriere.md) et la [maintenance à long terme](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md).

**Diagramme compact :** `statu quo → préparation → coexistence → migration → validation → exploitation → sortie ou retour arrière`.

**Porte :** une migration irréversible ou sans sauvegarde testée ne peut pas être compensée par un score fonctionnel élevé.

**Limite :** un prix public, une licence gratuite ou un benchmark rapide ne mesure ni le temps humain, ni la dépendance fournisseur, ni le coût de sortie.

---

<!-- l5:card -->
## CMP-11 — Sensibilité, robustesse, égalités et indétermination

| Contrôle | Question |
|---|---|
| poids | de petites variations raisonnables changent-elles le vainqueur ? |
| données | une valeur manquante plausible inverse-t-elle la décision ? |
| échelle | une autre normalisation défendable change-t-elle l’ordre ? |
| scénarios | le candidat reste-t-il préférable dans les profils réellement importants ? |
| portes | une réserve proche du seuil doit-elle imposer un pilote ? |
| corrélations | deux critères surpondèrent-ils le même avantage ? |
| arrondi | l’écart affiché dépasse-t-il la précision des données ? |
| dominance | un candidat est-il au moins aussi bon partout et meilleur sur un critère pertinent ? |
| regret | quel est le coût d’une mauvaise décision et de son retour arrière ? |
| robustesse | la recommandation survit-elle aux hypothèses raisonnables ? |
| égalité | les différences sont-elles trop faibles pour justifier un classement ? |
| indétermination | quelles preuves précises manquent pour conclure ? |

**Réponse rapide :** publier au minimum le scénario nominal, une variation des poids importants, le traitement des données manquantes et les points de bascule. Une recommandation fragile devient `conditional_choice` ou `pilot_required`, pas `reference_for_scenario`.

**Diagramme compact :** `résultat nominal → variation poids/données/échelles → points de bascule → robustesse forte, conditionnelle, égalité ou indéterminée`.

**Limite :** une analyse de sensibilité ne répare pas des critères mal définis ou des sources insuffisantes ; elle révèle seulement la dépendance de la conclusion aux hypothèses retenues.

---

<!-- l5:card -->
## CMP-12 — Rapport, versionnage, maintenance et retrait

| Section du rapport | Contenu minimal |
|---|---|
| résumé | décision, scénario, versions, date, confiance et repli |
| question | besoin, horizon, contraintes et approbateur |
| candidats | identifiants exacts, configurations, statu quo et exclusions |
| portes | statut, preuve, motif et condition de réouverture |
| critères | définitions, unités, directions, échelles, poids et sources |
| données | faits, mesures, avis, valeurs manquantes et dates |
| résultats | valeurs brutes, notes, scores, dominances et réserves |
| sensibilité | variations, égalités, points de bascule et incertitude |
| coûts | hypothèses, euros, temps, migration, exploitation et sortie |
| recommandation | choix conditionnel, étapes, pilote, repli et déclencheurs de révision |
| historique | changements de versions, poids, sources, décision et propriétaire |
| retrait | successeur, migration, archive, identifiant et dernière preuve |

**Réponse rapide :** conserver un registre canonique de données et produire des vues dérivées par scénario. Le [registre de compatibilité](CHAPITRE-22-Matrices-de-compatibilite.md#comp-12--historique-responsabilités-et-retrait), la [maintenance des benchmarks](CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md#bmk-12--répétition-indépendante-maintenance-et-retrait) et les [artefacts de CI](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#1-rôle-du-chapitre) fournissent les preuves liées sans être copiés dans le comparatif.

**Diagramme compact :** `registre canonique → vues par scénario → décision approuvée → surveillance des déclencheurs → révision, migration ou retrait`.

**Déclencheurs de révision :** nouvelle version majeure, changement de licence ou prix, fin de support, nouvel OS/GPU/backend, incident de sécurité, changement de besoin, mesure invalidée, coût de migration modifié ou alternative devenue admissible.

**Niveau de preuve :** `static-review`. Aucun comparatif exécutable, tableur de scoring, campagne utilisateur, devis, prix courant, mesure ou décision d’achat n’est produit ici.

---

## Frontières de la fiche

Cette fiche possède le contrat de comparaison, les critères, la pondération, les scénarios, la sensibilité, les coûts de migration et la forme des recommandations conditionnelles. Elle ne possède pas :

- les arbres de décision initiaux, conservés dans la [fiche 02](CHAPITRE-02-Arbres-de-decision.md) ;
- l’identité et le rôle des outils, moteurs ou modèles, conservés dans les [fiches 03 à 07](CHAPITRE-03-Fiches-des-logiciels-et-outils.md) ;
- les protocoles et résultats de mesure, conservés dans la [fiche 21](CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md) et les chapitres spécialisés du Livre IV ;
- les statuts de compatibilité, conservés dans la [fiche 22](CHAPITRE-22-Matrices-de-compatibilite.md) ;
- les procédures d’installation, production, test, export, publication, migration ou maintenance, conservées dans les Livres I à IV ;
- les checklists de décision et de publication, réservées à la future fiche 24 ;
- la qualification globale des licences, de la provenance et de la conformité, réservée à la future fiche 25 ;
- les index transversaux, réservés à la future fiche 26 ;
- les tableurs, scripts, jeux de données, pilotes, rapports automatisés et comparatifs exécutables, réservés au Companion Pack.

**Règle finale :** lorsqu’aucune solution ne domine avec des preuves suffisantes, documenter l’égalité, l’indétermination ou le pilote requis. Forcer un vainqueur est une perte d’information, pas une décision plus claire.
