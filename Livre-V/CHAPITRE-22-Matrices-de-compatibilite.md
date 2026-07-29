---
title: "Livre V — Fiche 22 : Matrices de compatibilité"
id: "DOC-L5-CH22"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 22
last-verified: "2026-07-29T21:13:00+02:00"
audit-status: "complete"
audit-date: "2026-07-29T21:13:00+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-22.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "versioned-compatibility-matrices-evidence-and-lifecycle"
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

# Matrices de compatibilité

> **Type de document :** contrats de cellules, légendes de statuts, matrices versionnées, règles de preuve et historique de changements.
> **Lecture :** définir l’objet et les axes, lire séparément la déclaration du fournisseur et la preuve locale, puis rejoindre le test ou le chapitre propriétaire avant toute décision.
> **Principe :** une cellule vide, ancienne, bloquée ou non testée ne prouve pas une incompatibilité ; une déclaration officielle ne prouve pas non plus que la combinaison locale a été exécutée.

## Index express

| Besoin | Ouvrir |
|---|---|
| définir une cellule de compatibilité complète | [COMP-00](#comp-00--contrat-dune-cellule-de-compatibilité) |
| lire les statuts sans les confondre | [Matrice A](#matrice-a--légende-à-trois-axes) |
| choisir les axes et la granularité | [COMP-01](#comp-01--axes-identité-et-granularité) |
| qualifier une source ou un test | [COMP-02](#comp-02--sources-preuves-et-traçabilité) |
| traiter versions, plages et direction | [COMP-03](#comp-03--versions-plages-et-direction-de-compatibilité) |
| trouver la matrice propriétaire | [Matrice B](#matrice-b--routage-par-famille-de-compatibilité) |
| croiser OS, shell, conteneur et chemins | [COMP-04](#comp-04--systèmes-shells-conteneurs-et-fichiers) |
| croiser GPU, pilote et backend | [COMP-05](#comp-05--matériel-gpu-pilotes-et-backends) |
| croiser outils, runtimes et dépendances | [COMP-06](#comp-06--outils-runtimes-plugins-et-dépendances) |
| croiser formats, import et round-trip | [COMP-07](#comp-07--formats-import-export-et-round-trip) |
| croiser API, données, réseau et mods | [COMP-08](#comp-08--api-protocoles-données-réseau-et-modding) |
| enregistrer un test positif ou négatif | [COMP-09](#comp-09--tests-positifs-négatifs-bloqués-et-non-applicables) |
| promouvoir ou dégrader un statut | [Matrice C](#matrice-c--portes-de-promotion-dégradation-et-décision) |
| concevoir une matrice lisible | [COMP-10](#comp-10--forme-densité-et-vues-dérivées) |
| gérer migration, rupture et repli | [COMP-11](#comp-11--migration-rupture-repli-et-dépréciation) |
| maintenir l’historique et la gouvernance | [COMP-12](#comp-12--historique-responsabilités-et-retrait) |

---

<!-- l5:card -->
## COMP-00 — Contrat d’une cellule de compatibilité

| Champ | Règle |
|---|---|
| identité | identifiant stable de la relation, distinct du titre affiché |
| sujet | composant, fichier, workflow, build, service ou capacité évalué |
| cible | OS, architecture, GPU, backend, outil, version, format, API ou profil concerné |
| direction | lecture, écriture, import, export, migration, exécution, connexion ou reprise |
| versions | versions exactes, commits, digests, schémas ou plages réellement couvertes |
| déclaration amont | officiel, communautaire, expérimental, explicitement non supporté ou inconnu |
| preuve locale | non évalué, documentation relue, test réussi, échec reproduit, bloqué ou obsolète |
| résultat fonctionnel | capacité précise validée ou non, sans extrapoler aux autres opérations |
| environnement | matériel, OS, pilote, build, options et dépendances |
| source | lien officiel, chapitre propriétaire, rapport de test ou artefact |
| date | date de vérification et, si nécessaire, date d’expiration |
| limites | cas exclus, défauts connus, coûts, sécurité et qualité |
| repli | voie alternative, conversion, version précédente ou absence de repli |
| propriétaire | personne ou chapitre chargé de réévaluer la cellule |
| historique | changement de statut, motif, preuve et successeur éventuel |

**Réponse rapide :** la [politique de compatibilité](../Volume-0/CHAPITRE-09-Politique-de-compatibilite.md#6-matrice-de-compatibilité) impose version, OS, matériel, niveau, dernier test et remarques. La présente fiche ajoute la direction, les preuves séparées et le cycle de vie afin d’éviter qu’un mot unique masque plusieurs réalités.

**Diagramme compact :** `sujet + cible + direction → déclaration amont → preuve locale → décision bornée → date et réévaluation`.

**Niveau de preuve :** `static-review`. Aucune combinaison matérielle, logicielle, de format ou de plateforme n’est testée dans cette fiche.

---

<!-- l5:matrix -->
## Matrice A — Légende à trois axes

| Axe | Valeur | Signification | Ne signifie pas |
|---|---|---|---|
| déclaration amont | `official` | le fournisseur documente la combinaison dans une portée nommée | test local réussi |
| déclaration amont | `community` | une communauté ou intégration tierce la documente | engagement du fournisseur |
| déclaration amont | `experimental` | voie annoncée instable, en aperçu ou laboratoire | inutilisable |
| déclaration amont | `unsupported` | le fournisseur exclut explicitement la combinaison | impossibilité physique dans tous les forks |
| déclaration amont | `unknown` | aucune déclaration fiable n’est enregistrée | incompatibilité |
| preuve locale | `not_assessed` | aucun test local conforme n’est enregistré | échec |
| preuve locale | `docs_reviewed` | documentation, versions et limites ont été relues | exécution |
| preuve locale | `smoke_pass` | démarrage ou opération minimale réussie | workflow complet |
| preuve locale | `workflow_pass` | scénario propriétaire terminé avec oracle satisfait | performance ou sécurité globale |
| preuve locale | `regression_pass` | suite qualifiée réussie sur la combinaison | absence future de régression |
| preuve locale | `failed_reproduced` | échec reproductible avec attendu, environnement et artefacts | cause unique |
| preuve locale | `blocked` | précondition absente, risque ou outil indisponible | échec du composant |
| preuve locale | `stale` | preuve trop ancienne ou invalidée par un changement | échec actuel |
| décision collection | `reference` | voie principale dans le périmètre nommé | meilleure solution universelle |
| décision collection | `conditional` | autorisée sous conditions et repli visibles | support général |
| décision collection | `laboratory` | exploration isolée, sans dépendance centrale | voie de production |
| décision collection | `avoid` | ne pas sélectionner pour le périmètre courant | impossibilité hors périmètre |
| décision collection | `retired` | retirée du parcours actif, historique conservé | identifiant réutilisable |
| transversal | `not_applicable` | la relation n’a pas de sens pour cette cellule | non testé |

**Décision :** ne jamais fusionner les trois axes en un seul symbole. Une voie peut être officiellement supportée mais non testée localement, ou communautaire et validée sur un scénario précis.

---

<!-- l5:card -->
## COMP-01 — Axes, identité et granularité

| Question | Règle |
|---|---|
| quel sujet ? | nommer l’artefact exact : outil, build, plugin, modèle, fichier, API ou workflow |
| quelle cible ? | une dimension testable : OS, architecture, version, backend, format ou profil |
| quelle opération ? | lecture et écriture, import et export, éditeur et build sont des cellules distinctes |
| quel niveau ? | éviter les lignes « Windows » ou « GPU » sans version, architecture ou pilote pertinent |
| quelle variante ? | séparer CPU, Vulkan, DirectML, ZLUDA, ROCm/HIP ou backend propriétaire |
| quelle portée ? | préciser Solo, Studio, développement, CI, build test, runtime ou archive |
| quelle qualité ? | une sortie techniquement produite peut échouer visuellement, auditivement ou fonctionnellement |
| quelle sécurité ? | compatibilité technique et autorisation de déploiement restent deux décisions |
| quelle temporalité ? | la cellule décrit un état daté et peut expirer |
| quelle indépendance ? | séparer les axes qui peuvent changer sans entraîner les autres |

**Réponse rapide :** une matrice utile minimise chaque cellule à une relation vérifiable. La [politique des versions exactes](../Volume-0/CHAPITRE-09-Politique-de-compatibilite.md#51-versions-exactes-pour-les-dépendances-critiques) interdit de cacher un commit, un digest ou une version de schéma derrière « récent ».

**Diagramme compact :** `objet exact × cible exacte × opération exacte × environnement exact = une cellule réévaluable`.

**Limite :** multiplier les axes jusqu’à produire une matrice illisible est une autre erreur. Les vues dérivées de [COMP-10](#comp-10--forme-densité-et-vues-dérivées) filtrent un registre canonique plus détaillé.

---

<!-- l5:card -->
## COMP-02 — Sources, preuves et traçabilité

| Source | Capacité | Limite |
|---|---|---|
| documentation officielle | confirmer une déclaration, une version, une plateforme ou une limite publiée | ne prouve pas l’exécution locale |
| notes de version | dater ajout, rupture, retrait ou migration | peuvent omettre un effet indirect |
| dépôt ou issue amont | identifier commit, correctif, bug connu ou statut expérimental | commentaire isolé non autoritatif |
| chapitre propriétaire | conserver le contexte et la méthode retenue par la collection | niveau souvent `static-review` |
| manifeste d’environnement | identifier versions, matériel, options et dépendances | ne prouve aucun résultat |
| test documenté | prouver une opération et un oracle dans un environnement | ne couvre que le scénario testé |
| artefact CI | prouver l’exécution du job et ses sorties conservées | ne remplace pas un test de plateforme absent |
| import ou capture | montrer un résultat visuel, audio ou structurel | ne prouve pas le round-trip ni le runtime |
| journal ou trace | contextualiser une réussite ou un échec | ne prouve pas seul la cause |
| décision humaine | accepter une combinaison et ses risques | ne transforme pas une réserve en fait |

**Réponse rapide :** la hiérarchie de preuve du [catalogue diagnostique](CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md#matrice-c--niveaux-de-preuve-et-portes-de-promotion) et celle des [benchmarks](CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md#matrice-c--niveaux-de-preuve-et-déclarations-permises) s’appliquent également aux cellules de compatibilité.

**Intégrité :** chaque preuve locale conserve identifiant du test, commit ou build, environnement, statut, date, artefact et empreinte. Une URL sans date ni portée ne suffit pas.

**Limite :** une source officielle peut déclarer « supporté » alors que le projet utilise une extension, une option ou une conversion hors de cette portée.

---

<!-- l5:card -->
## COMP-03 — Versions, plages et direction de compatibilité

| Situation | Traitement |
|---|---|
| version exacte | cellule principale lorsque dépendance, modèle, format ou build est critique |
| commit ou digest | préféré pour image, dépôt, workflow, modèle ou artefact mutable |
| plage de versions | admise seulement si les bornes et cas intermédiaires sont testés ou documentés |
| version minimale | ne prouve pas automatiquement toutes les versions supérieures |
| compatibilité ascendante | un lecteur ancien accepte-t-il une donnée nouvelle ? tester explicitement |
| compatibilité descendante | un lecteur nouveau accepte-t-il une donnée ancienne ? tester explicitement |
| lecture seule | ne déduit ni écriture, ni conversion, ni sauvegarde |
| écriture | ne prouve pas la réouverture ou l’import ailleurs |
| migration | source, cible, sauvegarde, journal et retour arrière distincts |
| round-trip | exporter, importer, réexporter et comparer selon les pertes autorisées |
| API compatible | endpoints, champs, erreurs et streaming réellement utilisés seulement |
| éditeur versus build | deux environnements et deux cellules |
| runtime versus archive | exploitation immédiate et lisibilité future séparées |

**Réponse rapide :** la [politique des plages](../Volume-0/CHAPITRE-09-Politique-de-compatibilite.md#52-plages-de-versions) exige des tests ; « toutes les versions récentes » est refusé. Pour les formats, le [contrat d’un format](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#fmt-00--contrat-dun-format) sépare syntaxe, schéma, sémantique, évolution et conversion.

**Diagramme compact :** `source vA --opération--> cible vB --oracle--> statut ; sens inverse = nouvelle cellule`.

**Limite :** une réussite de lecture après migration destructive n’est pas une preuve de compatibilité bidirectionnelle.

---

<!-- l5:matrix -->
## Matrice B — Routage par famille de compatibilité

| Famille | Axes principaux | Propriétaire documentaire | Preuve locale attendue |
|---|---|---|---|
| outils de base | OS, shell, architecture, version, chemin | [fiches des logiciels](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#matrice-a--compatibilité-et-positionnement) | version, démarrage, commande minimale |
| moteurs et backends IA | modèle, moteur, backend, API, GPU, mémoire | [moteurs et backends](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#matrice-b--api-formats-accélération-et-mémoire) | chargement, appel réel, backend détecté |
| modèles IA | architecture, format, quantification, tokenizer, licence | [modèles de langage](CHAPITRE-05-Fiches-des-modeles-de-langage.md) | hash, prompt ou échantillon, résultat borné |
| workflows visuels | ComfyUI, nœuds, modèles, backend, VRAM | [modèles visuels](CHAPITRE-06-Fiches-des-modeles-visuels.md) | workflow figé, image et manifeste |
| audio IA | modèle, voix, langue, runtime, consentement | [modèles audio](CHAPITRE-07-Fiches-des-modeles-audio.md) | échantillon autorisé, format et mesure |
| formats structurés | modèle, encodage, schéma, conversion | [formats d’échange](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#matrice-b--couches-de-validation) | parse, schéma, sémantique et round-trip |
| bases et sauvegardes | schéma, migration, version d’application | [SQLite](CHAPITRE-14-Schemas-SQLite-et-migrations.md) et [sauvegardes](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#3-périmètre-et-frontières) | copie, migration, lecture et restauration |
| assets 3D | Blender, glTF/GLB, Godot, renderer, preset | [référence graphique](CHAPITRE-18-Reference-graphique-et-3D.md#matrice-b--formats-et-chemins-déchange) | export, import, scène et revue |
| audio runtime | source, codec, import Godot, dispositif | [référence audio](CHAPITRE-19-Reference-audio.md#matrice-b--formats-et-chemins-dusage) | import, lecture, boucle et écoute |
| réseau et API | protocole, version, transport, autorité | [communication IA](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md#51-port-applicatif) | handshake, requête, erreurs et reprise |
| exports | Godot, templates, SDK, OS, architecture | [exports et packaging](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md#4-prérequis-et-frontières) | export, installation et lancement propre |
| mods | API publique, manifeste, capacités, dépendances | [modding](../Livre-IV/CHAPITRE-21-Modding-et-contenu-communautaire.md#5-choisir-les-surfaces-dextension) | validation, activation, désactivation et sauvegarde |
| archivage | format, dépendances, outils, reconstruction | [maintenance et pérennité](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md#4-modèle-mental--conserver-un-système-pas-seulement-un-zip) | fixité, restauration ou reconstruction |

**Décision :** cette fiche centralise les statuts et leur lecture. Les procédures, oracles et corrections restent dans les sources propriétaires.

---

<!-- l5:card -->
## COMP-04 — Systèmes, shells, conteneurs et fichiers

| Axe | Questions obligatoires |
|---|---|
| OS | famille, version, édition, architecture et correctifs pertinents |
| shell | PowerShell, CMD, Bash ou autre ; syntaxe et encodage ne sont pas interchangeables |
| chemin | séparateur, casse, longueur, caractères, liens et emplacement du dépôt |
| permissions | utilisateur, groupe, ACL, élévation et fichiers exécutables |
| locale | langue, séparateur décimal, fuseau, encodage et tri |
| WSL | distribution, emplacement des fichiers, réseau, GPU et permissions |
| conteneur | OS de l’image, architecture, moteur, volumes, réseau et secrets |
| hôte/conteneur | client disponible ne prouve pas la capacité du moteur ou du runtime interne |
| système de fichiers | NTFS, ext4, partage, montage, sensibilité à la casse et performances |
| headless | démarrage sans interface, dépendances graphiques et sortie |
| CI | image du runner, shell par défaut, permissions et services |
| repli | procédure native, conteneur séparé ou opération manuelle |

**Réponse rapide :** la [politique des systèmes](../Volume-0/CHAPITRE-09-Politique-de-compatibilite.md#4-systèmes-dexploitation) traite Windows, Linux, macOS et WSL comme des profils différents. La [matrice des outils](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#matrice-a--compatibilité-et-positionnement) rappelle que « possible » n’est ni « officiellement supporté » ni « validé ».

**Porte :** une commande réussie dans WSL ou un conteneur ne qualifie pas automatiquement la même opération sur l’hôte, et inversement.

**Limite :** le déplacement d’un dépôt entre systèmes de fichiers peut modifier permissions, casse, performances et comportement de surveillance.

---

<!-- l5:card -->
## COMP-05 — Matériel, GPU, pilotes et backends

| Couche | Identité à enregistrer | Preuve distincte |
|---|---|---|
| CPU | modèle, architecture, cœurs et instructions requises | démarrage, calcul ou benchmark spécialisé |
| GPU | modèle, architecture, VRAM et identifiant du dispositif | détection et exécution réelle |
| pilote | version, fournisseur et paquet | journal du runtime et stabilité du scénario |
| API | Vulkan, DirectX, Metal, OpenGL ou autre | initialisation et capacité utilisée |
| backend | CPU, Vulkan, DirectML, ZLUDA, ROCm/HIP ou spécifique | log, mémoire et comparaison |
| précision | FP32, FP16, BF16, INT8 ou quantification | sortie correcte et qualité |
| offload | couches, opérations ou buffers déplacés | utilisation réelle de mémoire et temps |
| renderer | Forward+, Mobile, Compatibility ou autre | scène et build correspondants |
| profil mémoire | RAM, VRAM, batch, résolution, contexte | absence de saturation et résultat |
| thermique/énergie | secteur, profil, fréquence et température | stabilité dans la fenêtre |
| repli | CPU, résolution réduite, batch 1 ou modèle plus petit | test fonctionnel séparé |

**Réponse rapide :** la [politique GPU](../Volume-0/CHAPITRE-09-Politique-de-compatibilite.md#8-compatibilité-gpu) interdit de supposer CUDA. La [matrice moteurs/backends](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#matrice-b--api-formats-accélération-et-mémoire) distingue CPU, Vulkan, DirectML, ZLUDA et ROCm/HIP au lieu de les regrouper sous « GPU ».

**Diagramme compact :** `matériel → pilote → API → backend → modèle ou charge → résultat + mémoire + qualité`.

**Limite :** un GPU détecté, de la VRAM allouée ou un logo dans l’interface ne prouve pas que le calcul dominant utilise la voie attendue.

---

<!-- l5:card -->
## COMP-06 — Outils, runtimes, plugins et dépendances

| Élément | Compatibilité à séparer |
|---|---|
| outil principal | version, édition, OS, architecture et mode d’installation |
| runtime | version réellement lancée, non seulement installée |
| plugin ou extension | API hôte, version, permissions et provenance |
| dépendance native | ABI, architecture, bibliothèque, compilateur et redistribution |
| dépendance Python | interpréteur, environnement, verrou, roue et index |
| image de conteneur | tag, digest, architecture et base OS |
| service distant | version ou comportement, endpoint, authentification et quota |
| script | shell, runtime, encodage, chemins et privilèges |
| workflow CI | action, version, runner, permissions et artefacts |
| modèle ou asset | hash, licence, format et outil consommateur |
| configuration | schéma, valeur par défaut, variable et secret séparé |
| installation | méthode supportée, mise à jour, désinstallation et retour arrière |

**Réponse rapide :** la [matrice formats/interfaces/autorités](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#matrice-b--formats-interfaces-et-autorités) empêche de confondre rôle et compatibilité. Le [contrat moteur/backend](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#moteur-00--contrat-et-vocabulaire) exige d’identifier chaque couche avant d’attribuer un résultat.

**Porte :** une extension compatible avec l’éditeur peut échouer dans un export ; une roue Python installable peut ne pas posséder le backend ou l’architecture requis.

**Limite :** une dépendance transitive peut rompre une combinaison sans apparaître dans le titre de la cellule ; conserver le verrou ou l’inventaire correspondant.

---

<!-- l5:card -->
## COMP-07 — Formats, import, export et round-trip

| Opération | Oracle minimal | Réserve |
|---|---|---|
| détection | format et version identifiés sans se fier à l’extension seule | détection n’est pas parse |
| parse | syntaxe ou conteneur accepté | ne prouve pas le schéma |
| validation | schéma, types, bornes et invariants satisfaits | ne prouve pas la sémantique métier complète |
| lecture | informations requises accessibles | ne prouve pas l’écriture |
| écriture | document produit selon le profil | ne prouve pas sa réouverture |
| import | outil cible crée les objets attendus | paramètres par défaut peuvent perdre des données |
| export | livrable produit avec preset et journal | ne prouve pas l’import dans la cible |
| conversion | pertes autorisées et erreurs rapportées | « terminé » ne signifie pas sans perte |
| round-trip | source → cible → source comparée selon oracle | identité binaire rarement requise |
| migration | ancienne version → nouvelle avec sauvegarde | ne prouve pas le retour arrière |
| archive | format, dépendances et métadonnées conservés | présence ne prouve pas reconstruction |
| runtime | résultat exploité dans le build cible | distinct de l’éditeur |

**Réponse rapide :** la [sélection des formats](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#matrice-a--sélection-par-besoin) part du modèle et de l’autorité. Pour la 3D, la [matrice d’échange](CHAPITRE-18-Reference-graphique-et-3D.md#matrice-b--formats-et-chemins-déchange) sépare source, livraison et import ; pour l’audio, la [matrice des formats](CHAPITRE-19-Reference-audio.md#matrice-b--formats-et-chemins-dusage) sépare source, master et runtime.

**Diagramme compact :** `source → export → livraison → import → usage → réexport éventuel → comparaison des pertes`.

**Limite :** une image ressemblante ou un son audible ne prouve pas la conservation des métadonnées, unités, rig, boucles, canaux ou droits.

---

<!-- l5:card -->
## COMP-08 — API, protocoles, données, réseau et modding

| Domaine | Axes de compatibilité |
|---|---|
| API | version, endpoint, méthode, champs, erreurs, streaming et authentification |
| « compatible OpenAI » | sous-ensemble exact, modèles, outils, streaming et codes réellement utilisés |
| protocole réseau | version, framing, ordre, horloge, autorité et refus propre |
| client/serveur | versions dans les deux sens, topologie et capacité de migration |
| données persistantes | version de schéma, migration, sauvegarde, restauration et downgrade |
| SQLite | schéma, migrations, pragmas, extension et version du runtime |
| sauvegarde de jeu | build producteur, build lecteur, mods actifs et contenus requis |
| configuration | champs inconnus, valeurs par défaut, validation et secret |
| mod | API publique, manifeste, namespace, dépendances, capacités et ordre |
| asset communautaire | format, limites, validation, licence et isolation |
| localisation | locale, clés, placeholders, police et repli |
| reprise | retry, idempotence, timeout, annulation et état partiel |

**Réponse rapide :** la [politique réseau](../Volume-0/CHAPITRE-09-Politique-de-compatibilite.md#11-compatibilité-réseau-et-multijoueur) sépare compatibilité réseau et sauvegardes. Le [port applicatif](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md#51-port-applicatif) sépare domaine et transport, tandis que le [modding](../Livre-IV/CHAPITRE-21-Modding-et-contenu-communautaire.md#4-modèle-mental--une-extension-est-une-entrée-non-fiable) traite toute extension comme une entrée non fiable.

**Porte :** une réponse HTTP 200 ne prouve ni conformité de tous les champs, ni ordre des événements, ni compatibilité de reprise. Une sauvegarde chargée ne prouve pas que tous ses contenus restent disponibles.

**Limite :** l’absence d’erreur visible peut masquer une perte silencieuse ; l’oracle doit vérifier les invariants métier.

---

<!-- l5:card -->
## COMP-09 — Tests positifs, négatifs, bloqués et non applicables

| Statut de run | Conditions | Effet sur la cellule |
|---|---|---|
| `pass` | préconditions satisfaites, opération terminée, oracle réussi | preuve locale positive pour ce scénario |
| `fail_reproduced` | attendu défini, échec répété, artefacts conservés | preuve négative bornée |
| `fail_unconfirmed` | anomalie observée mais non reproduite ou contexte incomplet | enquête, pas incompatibilité |
| `blocked` | dépendance, matériel, droit, risque ou coût empêche le test | reste non évalué |
| `not_run` | test prévu mais non exécuté | aucune conclusion |
| `not_applicable` | relation sans sens pour les axes choisis | cellule explicitement neutralisée |
| `invalid_test` | protocole ou oracle défectueux | aucun effet, test à corriger |
| `stale` | preuve invalidée par versions, date ou environnement | retirer la promotion active |
| `partial` | certaines capacités réussissent et d’autres non | scinder la cellule |
| `waived` | risque accepté par autorité nommée | décision temporaire, pas preuve technique |

**Réponse rapide :** l’[échelle diagnostique](CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md#diag-01--vocabulaire-et-niveaux-de-certitude) interdit de transformer un symptôme ou un message en cause. La [fiche benchmark](CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md#bmk-07--format-des-données-brutes-et-nullabilité) conserve statuts et valeurs absentes au lieu de les remplacer par zéro.

**Diagramme compact :** `préconditions → opération → oracle → artefacts → statut du run → mise à jour bornée de la cellule`.

**Preuve négative :** « incompatible » exige au minimum un attendu, un environnement, une version, une reproduction, une source ou un test propriétaire et une vérification qu’un prérequis manquant n’explique pas l’échec.

**Limite :** un test positif ne prouve pas l’absence de défaut intermittent ; un test négatif ancien ne prouve pas l’échec d’une version corrigée.

---

<!-- l5:matrix -->
## Matrice C — Portes de promotion, dégradation et décision

| Transition | Preuve minimale | Décision autorisée | Motif de dégradation |
|---|---|---|---|
| `not_assessed → docs_reviewed` | source datée, versions et portée enregistrées | planifier le test | source retirée ou ambiguë |
| `docs_reviewed → smoke_pass` | installation ou démarrage minimal avec artefact | exploration contrôlée | changement de version ou environnement |
| `smoke_pass → workflow_pass` | scénario propriétaire et oracle satisfaits | usage conditionnel | régression fonctionnelle ou qualité |
| `workflow_pass → regression_pass` | suite répétable et cas d’erreur pertinents | voie supportée dans le périmètre | suite obsolète ou preuve perdue |
| `regression_pass → reference` | repli, maintenance, sécurité et propriétaire acceptés | parcours principal | dépendance non maintenue ou risque |
| `not_assessed → blocked` | précondition ou risque documenté | aucune conclusion technique | précondition résolue |
| `any → failed_reproduced` | échec reproductible et contexte complet | éviter la combinaison précise | correctif ou nouvelle version à retester |
| `any → stale` | version, date, pilote, protocole ou artefact invalidé | retirer la déclaration active | nouvelle preuve conforme |
| `conditional → laboratory` | variabilité, dette ou risque accru | isolation obligatoire | qualification réussie |
| `reference → retired` | fin de support, migration et historique | retrait du parcours | aucun retour sans nouvelle décision |

**Décision :** le niveau le plus faible entre déclaration amont, preuve locale, sécurité, qualité, maintenance et licence borne l’usage. La fiche 23 pourra comparer les solutions ; elle ne pourra pas améliorer un statut de compatibilité sans preuve.

---

<!-- l5:card -->
## COMP-10 — Forme, densité et vues dérivées

| Problème | Réponse de conception |
|---|---|
| trop d’axes | registre canonique en lignes, vues filtrées par décision |
| cellules longues | code de statut court plus lien vers la preuve |
| statuts combinés | colonnes séparées pour amont, local et décision |
| dates invisibles | `verified_at` et `expires_at` visibles |
| plages ambiguës | bornes exactes et note de couverture |
| matrices énormes | une vue par famille, plateforme ou version |
| cellules vides | `not_assessed`, `not_applicable` ou `unknown`, jamais blanc ambigu |
| doublons | identifiant relationnel stable et source unique |
| couleurs seules | symbole, texte et légende accessibles |
| historique écrasé | journal append-only ou commits corrélés |
| synthèse trompeuse | compteurs accompagnés du dénominateur et des statuts |
| export PDF/HTML | titres courts, tables scindables et liens visibles |

**Réponse rapide :** le registre canonique peut utiliser une ligne par relation ; les matrices humaines sont des projections. Un tableau « outil × OS » ne doit pas absorber versions, backends, opérations et preuves dans une note illisible.

**Diagramme compact :** `registre normalisé → filtres versionnés → matrice de lecture → cellule → preuve détaillée`.

**Profil Solo :** quelques outils et plateformes réellement utilisés, statuts explicites et revue manuelle datée.

**Profil Studio :** registre central, propriétaires, vues par équipe, automatisation, dérogations, dates d’expiration et rapports de couverture.

---

<!-- l5:card -->
## COMP-11 — Migration, rupture, repli et dépréciation

| Événement | Action |
|---|---|
| nouvelle version mineure | vérifier notes, installer isolément et exécuter la suite pertinente |
| nouvelle version majeure | créer de nouvelles cellules et une note de migration |
| format modifié | sauvegarder, convertir sur copie, valider et tester le round-trip |
| API retirée | marquer rupture, migrer le client et conserver l’ancien contrat si supporté |
| pilote ou backend changé | requalifier détection, qualité, mémoire et stabilité |
| plugin abandonné | geler la version, migrer ou retirer la dépendance |
| sécurité critique | bloquer ou dégrader même si le test fonctionnel passe |
| licence modifiée | suspendre redistribution ou usage selon la gouvernance |
| service distant modifié | versionner le comportement observé et le repli |
| régression | revenir à la combinaison qualifiée et ouvrir un diagnostic |
| fin de support | annoncer date, successeur, migration et archive |
| preuve perdue | passer à `stale` ou `not_assessed` selon le contexte |

**Réponse rapide :** la [politique de dépréciation](../Volume-0/CHAPITRE-09-Politique-de-compatibilite.md#14-dépréciation) conserve l’identifiant et la migration. Les données persistantes exigent sauvegarde, migration, test sur copie et restauration selon la [politique des données](../Volume-0/CHAPITRE-09-Politique-de-compatibilite.md#10-compatibilité-des-données-et-sauvegardes).

**Diagramme compact :** `changement détecté → impact sur les cellules → test/migration → décision → historique + repli`.

**Limite :** une solution de repli non testée est une intention, pas une garantie. Elle reçoit sa propre cellule et sa propre preuve.

---

<!-- l5:card -->
## COMP-12 — Historique, responsabilités et retrait

| Champ de gouvernance | Règle |
|---|---|
| propriétaire | responsable de la cellule, de la source et de la réévaluation |
| vérificateur | personne ou job distinct lorsque le risque le justifie |
| date de revue | dernière vérification documentaire |
| date de test | dernière exécution conforme |
| expiration | échéance ou événement invalidant |
| changement | ancien statut, nouveau statut, motif et preuve |
| dérogation | périmètre, risque, approbateur et fin |
| successeur | cellule, version ou voie de remplacement |
| archivage | preuve, manifestes et outils nécessaires à la reconstruction |
| retrait | date, raison, migration et conservation historique |
| couverture | axes intentionnellement testés et angles morts |
| communication | index, changelog, note de migration et équipes concernées |

**Réponse rapide :** une matrice est un produit maintenu, non une capture statique. La [maintenance](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md#6-établir-les-responsabilités) exige des propriétaires explicites ; la [politique de rupture](../Volume-0/CHAPITRE-09-Politique-de-compatibilite.md#15-politique-de-rupture) impose changelog, fiche, matrice et note de migration.

**Révision :** réévaluer lors d’un changement de version, pilote, OS, matériel, schéma, format, plugin, API, licence, test, sécurité ou propriétaire. Une cellule sans preuve consultable et sans propriétaire ne peut pas rester `reference`.

**Historique :** ne jamais réattribuer un identifiant retiré. Conserver le dernier périmètre autorisé, la raison du retrait et le lien vers le successeur.

**Limite :** la matrice centrale exécutable et ses rapports automatisés appartiennent au Companion Pack. Cette fiche définit leurs contrats sans les matérialiser.

---

## Sources propriétaires et limites

- [Volume 0 — Politique de compatibilité](../Volume-0/CHAPITRE-09-Politique-de-compatibilite.md)
- [Livre V, fiche 03 — Fiches des logiciels et outils](CHAPITRE-03-Fiches-des-logiciels-et-outils.md)
- [Livre V, fiche 04 — Fiches des moteurs et backends IA](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md)
- [Livre V, fiche 05 — Fiches des modèles de langage](CHAPITRE-05-Fiches-des-modeles-de-langage.md)
- [Livre V, fiche 06 — Fiches des modèles visuels](CHAPITRE-06-Fiches-des-modeles-visuels.md)
- [Livre V, fiche 07 — Fiches des modèles audio](CHAPITRE-07-Fiches-des-modeles-audio.md)
- [Livre V, fiche 13 — Structures JSON et formats d’échange](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md)
- [Livre V, fiche 14 — Schémas SQLite et migrations](CHAPITRE-14-Schemas-SQLite-et-migrations.md)
- [Livre V, fiche 18 — Référence graphique et 3D](CHAPITRE-18-Reference-graphique-et-3D.md)
- [Livre V, fiche 19 — Référence audio](CHAPITRE-19-Reference-audio.md)
- [Livre V, fiche 20 — Catalogue des erreurs et diagnostics](CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md)
- [Livre V, fiche 21 — Benchmarks et méthodes de mesure](CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md)
- [Livre IV, chapitre 16 — Exports Godot et packaging](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md)
- [Livre IV, chapitre 21 — Modding et contenu communautaire](../Livre-IV/CHAPITRE-21-Modding-et-contenu-communautaire.md)
- [Livre IV, chapitre 22 — Maintenance, archivage et pérennité](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md)

**Niveau de preuve de cette fiche :** `static-review`. Les contrats et liens sont relus contre les sources du dépôt. Aucun OS, GPU, pilote, backend, outil, plugin, runtime, format, import, export, API, sauvegarde, migration, réseau, mod, build, package ou archive n’a été testé ; aucune cellule runtime, matrice exécutable, preuve de compatibilité, incompatibilité, source externe qualifiée, donnée utilisateur ou PDF n’a été produit.

## Synthèse de consultation

Définir une relation précise et directionnelle ; conserver séparément déclaration amont, preuve locale et décision ; identifier versions, environnement, opération, source, date, limites et repli ; considérer les statuts `not_assessed`, `blocked`, `stale` et `not_applicable` comme des informations distinctes ; promouvoir uniquement avec une preuve propriétaire ; dégrader ou retirer dès qu’un changement invalide la portée ; enfin conserver l’historique afin que la matrice aide au choix et au diagnostic sans inventer de support.
