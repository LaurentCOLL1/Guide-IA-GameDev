---
title: "Livre V — Fiche 08 : Bibliothèque de workflows"
id: "DOC-L5-CH08"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 8
last-verified: "2026-07-28T18:20:01+02:00"
audit-status: "complete"
audit-date: "2026-07-28T18:20:01+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-08.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "cross-domain-workflow-library"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Bibliothèque de workflows

> **Type de document :** cartes de workflows, matrices de sélection, cycle de preuve et portes d’acceptation.
> **Lecture :** partir du résultat attendu, identifier le propriétaire du processus, puis vérifier entrées, dépendances, effets, preuves et repli.
> **Principe :** un workflow décrit une transformation ; il ne prouve ni son exécution, ni la qualité de sa sortie, ni l’autorisation de la publier.

## Index express

| Besoin | Ouvrir |
|---|---|
| enregistrer un workflow exact | [WORKFLOW-00](#workflow-00--contrat-dun-workflow) |
| choisir par domaine | [Matrice A](#matrice-a--sélection-par-domaine) |
| valider et importer du contenu Godot | [WORKFLOW-01](#workflow-01--contenu-godot) |
| tester et préparer un export Godot | [WORKFLOW-02](#workflow-02--qa-et-export-godot) |
| exporter un asset Blender | [WORKFLOW-03](#workflow-03--blender-vers-godot) |
| exécuter un graphe ComfyUI | [WORKFLOW-04](#workflow-04--comfyui-et-médias) |
| traiter une tâche audio | [WORKFLOW-05](#workflow-05--audio) |
| qualifier un chapitre ou une publication | [WORKFLOW-06](#workflow-06--documentation) |
| lire le cycle commun | [Matrice B](#matrice-b--cycle-dun-workflow) |
| utiliser une variante Solo | [WORKFLOW-07](#workflow-07--profil-solo) |
| utiliser une variante Studio | [WORKFLOW-08](#workflow-08--profil-studio) |
| protéger secrets et fichiers | [WORKFLOW-09](#workflow-09--sécurité-et-frontières) |
| reprendre sans masquer un échec | [WORKFLOW-10](#workflow-10--idempotence-retry-et-reprise) |
| conserver la provenance | [WORKFLOW-11](#workflow-11--manifestes-et-artefacts) |
| tester sans inventer une preuve | [Matrice C](#matrice-c--qualification-minimale) |
| publier un template réutilisable | [WORKFLOW-12](#workflow-12--paquet-et-acceptation) |

---

<!-- l5:card -->
## WORKFLOW-00 — Contrat d’un workflow

| Champ | Règle |
|---|---|
| identité | identifiant stable, version, propriétaire, dépôt, chemin canonique et empreinte |
| résultat | effet attendu formulé comme état vérifiable, jamais comme promesse vague de qualité |
| entrées | fichiers, données, paramètres, droits, versions et limites de taille |
| dépendances | outils, modèles, plugins, nœuds, bibliothèques, services et permissions |
| étapes | ordre logique, préconditions, points d’arrêt et autorité de chaque outil |
| sorties | artefacts, rapports, journaux, caches et éléments destinés au staging |
| effets de bord | écritures, suppressions, réseau, processus, consommation matérielle et données sensibles |
| codes d’échec | succès, entrée invalide, dépendance absente, exécution échouée, intégrité ou revue requise |
| reproductibilité | environnement, versions, configuration, seed éventuelle et niveau d’équivalence revendiqué |
| sécurité | frontière d’écriture, secrets, code tiers, fichiers non fiables et moindre privilège |
| preuve | définition relue, exécution minimale, artefacts, mesures, revue humaine et décision |
| retrait | dépendances affectées, remplaçant, conservation des preuves et date de fin d’usage |

**Réponse rapide :** la bibliothèque enregistre des **contrats de transformation**. Les primitives génériques restent dans les [définitions opérationnelles de l’automatisation](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#3-définitions-opérationnelles) ; l’orchestration artistique reste dans le [rôle du chapitre de production en lots](../Livre-III/CHAPITRE-30-Automatisation-Blender-ComfyUI-et-production-en-lots.md#1-rôle-du-chapitre).

---

<!-- l5:matrix -->
## Matrice A — Sélection par domaine

| Besoin | Workflow de départ | Source propriétaire | Preuve minimale | Repli |
|---|---|---|---|---|
| compiler et importer des données Godot | WORKFLOW-01 | [pipelines de contenu](../Livre-II/CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md#1-rôle-du-chapitre) | validation, staging, import terminé et rapport | validation locale sans promotion |
| vérifier un projet et préparer un candidat | WORKFLOW-02 | [portes de CI](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#8-définir-les-portes-de-pull-request) | import, tests du projet, export et empreintes | exécution locale identique |
| transformer une source Blender en échange Godot | WORKFLOW-03 | [pipeline Blender](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md#1-rôle-du-chapitre) | export de staging et contrôle d’import | export manuel avec même profil |
| produire des propositions visuelles | WORKFLOW-04 | [workflow JSON canonique](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#14-enregistrer-le-workflow-json-comme-source-canonique) | run identifié, sorties en quarantaine et revue | graphe manuel Core |
| synthétiser, transcrire ou préparer un audio | WORKFLOW-05 | [chaîne audio locale](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#1-objet-du-chapitre) | sortie témoin, journal, droits et écoute | outil CPU ou traitement manuel |
| valider un chapitre sans produire de PDF | WORKFLOW-06 | [cycle officiel de production](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#1-le-cycle-de-vie-officiel) | validateurs légers, rapport et diff ciblé | contrôles locaux documentés |
| coordonner plusieurs domaines | WORKFLOW-10 et WORKFLOW-11 | [modèle mental d’un lot](../Livre-III/CHAPITRE-30-Automatisation-Blender-ComfyUI-et-production-en-lots.md#6-modèle-mental-dun-lot) | plan figé, DAG, checkpoints et manifestes | lots indépendants plus petits |

Une ligne choisit un point d’entrée, pas un pipeline universel. Les outils restent propriétaires de leurs opérations, conformément aux [frontières de la fiche des logiciels](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#frontières-de-la-fiche) et aux [frontières des moteurs](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#frontières-avec-les-fiches-voisines).

---

<!-- l5:card -->
## WORKFLOW-01 — Contenu Godot

| Champ | Référence |
|---|---|
| besoin | transformer des sources auteur en définitions validées et importables sans donner d’autorité aux caches |
| entrées | révision Git, sources JSON ou Resources, schémas, identifiants, versions de l’outil et configuration |
| étapes | découvrir dans un ordre stable, valider, écrire en staging, produire un manifeste, lancer l’import puis contrôler les diagnostics |
| sorties | artefacts canoniques, manifeste, rapport et caches `.godot` reconstruisibles |
| refus | schéma invalide, identité dupliquée, sortie hors workspace, import incomplet ou diagnostic bloquant |
| reprise | reprendre depuis les sources et le plan ; supprimer les caches plutôt que les promouvoir |
| Solo | commande locale unique, aperçu du diff et validation avant copie vers les chemins canoniques |
| Studio | PR de contenu, artefacts de validation, revue du propriétaire et promotion séparée |
| sécurité | l’outil d’éditeur ne modifie aucun état runtime et n’écrit que dans le workspace déclaré |
| preuve | import réellement terminé, rapport archivé, empreintes et comparaison du diff |
| sources internes | [sources, artefacts et caches](../Livre-II/CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md#3-sources-artefacts-et-caches), [limiter le rayon d’impact](../Livre-II/CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md#7-limiter-le-rayon-dimpact), [sorties bornées](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#17-interdire-les-sorties-hors-du-workspace) |
| source officielle | [ligne de commande Godot](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html) |
| preuve actuelle | contrat relu ; aucun projet, importeur ou cache exécuté |

**Point critique :** `--import` attend la fin de l’import des ressources puis quitte, mais son succès ne prouve pas la validité métier des données. Le rapport propriétaire doit rester une porte distincte.

---

<!-- l5:card -->
## WORKFLOW-02 — QA et export Godot

| Champ | Référence |
|---|---|
| besoin | reproduire les contrôles rapides d’une révision puis préparer un candidat exportable |
| entrées | commit, `project.godot`, dépendances, profil de test, `export_presets.cfg` et templates qualifiés |
| étapes | démarrer l’éditeur headless, achever l’import, exécuter les tests du projet, collecter les rapports, exporter en staging et calculer les empreintes |
| sorties | rapports, journaux, manifeste de build, candidat et checksums |
| séparation | un test moteur lancé par `--test` n’est pas automatiquement la suite GDScript du projet |
| permissions | aucun secret sur une PR de faible confiance ; permissions du jeton explicitement minimales |
| cache | dépendances ou imports accélèrent un run mais ne deviennent ni preuve ni artefact publiable |
| artefact | le candidat conservé doit être celui qui traverse les portes ; ne pas le reconstruire après approbation |
| Solo | même script local et CI, une plateforme obligatoire et revue personnelle explicite |
| Studio | matrice de plateformes, approbateur indépendant et environnement protégé |
| sources internes | [niveau de preuve CI](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#3-niveau-de-preuve-et-réserves), [vocabulaire CI](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#5-vocabulaire-opérationnel), [deux enveloppes opérationnelles](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md#3-un-produit-deux-enveloppes-opérationnelles) |
| sources officielles | [ligne de commande Godot](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html), [artefacts GitHub Actions](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts) |
| preuve actuelle | aucun test, import, export ou candidat produit dans cette fiche |

---

<!-- l5:card -->
## WORKFLOW-03 — Blender vers Godot

| Champ | Référence |
|---|---|
| besoin | transformer une source `.blend` en fichier d’échange identifié sans écraser la source |
| entrées | source canonique, collection d’export, version Blender, profil glTF, unités, axes et dépendances |
| étapes | ouvrir une copie, vérifier les dépendances, valider la collection, exporter en arrière-plan, hacher le GLB puis contrôler l’import Godot |
| sorties | GLB ou glTF de staging, journal Blender, manifeste et rapport d’aller-retour |
| autorité | le `.blend` reste source ; l’export est dérivé ; seule une livraison approuvée rejoint le dépôt de destination |
| code | un script Python Blender possède les mêmes pouvoirs que l’utilisateur ; l’auto-exécution reste désactivée sauf source qualifiée |
| échec | scène absente, collection ambiguë, dépendance manquante, exception Python, export vide ou import Godot incohérent |
| reprise | nouvelle sortie temporaire ; aucune modification destructive de la source pendant une relance |
| Solo | profil d’export versionné et vérification manuelle du premier asset de chaque famille |
| Studio | ferme de jobs bornée, rapports centralisés et échantillonnage humain représentatif |
| sources internes | [responsabilités des fichiers](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md#5-responsabilités-des-fichiers), [qualifier la chaîne d’outils](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md#4-qualifier-la-chaîne-doutils), [tâches automatisables](../Livre-III/CHAPITRE-30-Automatisation-Blender-ComfyUI-et-production-en-lots.md#7-choisir-les-tâches-réellement-automatisables) |
| sources officielles | [arguments de ligne de commande Blender](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html), [sécurité des scripts Blender](https://docs.blender.org/manual/en/latest/advanced/scripting/security.html) |
| preuve actuelle | aucun Blender lancé, aucun GLB exporté et aucun import Godot contrôlé |

---

<!-- l5:card -->
## WORKFLOW-04 — ComfyUI et médias

| Champ | Référence |
|---|---|
| besoin | exécuter un graphe visuel versionné et relier ses sorties au paquet exact de modèles |
| entrées | workflow éditable JSON, format API, modèles, nœuds, entrées autorisées, paramètres, seed et limites |
| formes | le JSON de graphe sert à l’édition ; le format API décrit les nœuds et connexions soumis au serveur |
| étapes | vérifier versions et custom nodes, résoudre les modèles, figer les paramètres, soumettre, suivre le `prompt_id`, collecter puis mettre en quarantaine |
| sorties | manifeste de run, fichiers médias, métadonnées, journal, aperçus et décision humaine |
| métadonnées | une image peut embarquer un workflow, mais le JSON versionné et le manifeste restent les autorités documentaires |
| extensions | un custom node est du code tiers ; registre, commit, licence, permissions et retrait sont obligatoires |
| secrets | une clé de service ou de cloud ne figure jamais dans le workflow, les métadonnées ou le dépôt |
| reprise | resoumettre uniquement si le run précédent est absent ou classé échoué ; ne pas confondre timeout client et échec serveur |
| revue | une génération terminée reste en quarantaine jusqu’à validation artistique, technique et juridique |
| sources internes | [workflow JSON canonique](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#14-enregistrer-le-workflow-json-comme-source-canonique), [manifester les modèles](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#15-manifester-les-modèles-et-leurs-droits), [seeds et reproductibilité](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#17-gérer-les-seeds-et-la-reproductibilité-réelle) |
| sources officielles | [concept de workflow ComfyUI](https://docs.comfy.org/development/core-concepts/workflow), [spécification Workflow JSON](https://docs.comfy.org/specs/workflow_json), [templates de workflows](https://docs.comfy.org/custom-nodes/workflow_templates) |
| preuve actuelle | aucun graphe soumis, aucun modèle chargé et aucun média généré |

---

<!-- l5:card -->
## WORKFLOW-05 — Audio

| Champ | Référence |
|---|---|
| besoin | exécuter une transcription, une synthèse, une génération exploratoire ou une postproduction sans mélanger leurs environnements |
| entrées | texte ou audio autorisé, modèle, moteur, voix, consentement, format, langue et paramètres |
| étapes | valider les droits, préparer une copie, exécuter le moteur, conserver la sortie brute, écouter ou relire, nettoyer non destructivement puis exporter un dérivé |
| sorties | WAV ou transcription témoin, journal, manifeste, grille d’écoute, master candidat et export runtime séparé |
| TTS | voix, locuteur et consentement restent indépendants du modèle et du moteur |
| STT | l’audio original reste la référence ; silences, noms propres, langue et timestamps sont relus |
| musique et SFX | les sorties de poids non commerciaux restent des maquettes jusqu’à remplacement ou clarification |
| postproduction | FFmpeg, Audacity ou Ardour transforment un brouillon ; ils ne résolvent pas les droits du modèle ou de l’entrée |
| données | prises, références vocales et transcriptions sensibles restent hors dépôt public |
| repli | moteur CPU, transcription humaine, enregistrement ou création manuelle selon la tâche |
| sources internes | [formats audio du projet](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#4-formats-audio-du-projet), [gestion des modèles et licences](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#18-gestion-des-modèles-et-licences), [source, master et export](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#7-séparer-source-travail-master-et-export-runtime) |
| sources officielles | [documentation FFmpeg](https://ffmpeg.org/documentation.html), [filtres FFmpeg](https://ffmpeg.org/ffmpeg-filters.html) |
| preuve actuelle | aucun audio reçu, généré, transcrit, écouté, nettoyé ou exporté |

---

<!-- l5:card -->
## WORKFLOW-06 — Documentation

| Champ | Référence |
|---|---|
| besoin | transformer un lot documentaire ciblé en contenu relu, validé et traçable |
| entrées | branche dédiée, sources Markdown, front matter, liens, scripts de validation, plan et documents de gouvernance |
| étapes | rédiger, contrôler métadonnées et liens, auditer le profil, générer les rapports légers, mettre à jour la gouvernance, ouvrir la PR puis fusionner la tête validée |
| sorties | diff permanent, audit, preuve QA, rapports CI, artefacts et commit de fusion |
| règle PDF | aucune compilation PDF par chapitre ; la chaîne de publication complète reste différée à la fin du Livre ou de la collection |
| source d’ordre | `contents.txt` reste l’ordre lecteur ; un workflow ne réordonne pas silencieusement les chapitres |
| échec | lien local cassé, identifiant dupliqué, preuve incohérente, fichier temporaire restant ou validateur non vert |
| artefact | rapport de CI conservé avec run, digest, révision et rétention |
| repli | exécuter localement les mêmes validateurs, joindre les sorties et conserver la PR en brouillon |
| sécurité | les contrôles de PR n’exposent aucun secret à du code non fusionné |
| sources internes | [définition de terminé](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#2-définition-de-terminé), [production des exemples techniques](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#5-production-des-exemples-techniques), [chaîne de confiance CI](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#6-cartographier-la-chaîne-de-confiance) |
| sources officielles | [manuel Pandoc](https://pandoc.org/MANUAL.html), [workflows réutilisables GitHub Actions](https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations) |
| preuve actuelle | la présente fiche suit ce contrat documentaire ; aucun PDF n’est produit pour sa validation |

---

<!-- l5:matrix -->
## Matrice B — Cycle d’un workflow

| État | Question | Artefact autorisé | Passage interdit |
|---|---|---|---|
| `defined` | le contrat est-il complet et propriétaire identifié ? | fiche, schéma, template et exemples non exécutés | annoncer une compatibilité ou une performance |
| `qualified_inputs` | les entrées, dépendances, droits et versions sont-ils acceptables ? | plan figé et manifeste d’entrée | télécharger ou exécuter une dépendance inconnue |
| `ready` | workspace, permissions, capacité et repli sont-ils prêts ? | plan d’exécution et réservation de ressources | écrire dans les sources canoniques |
| `running` | le job respecte-t-il délais, concurrence et frontières ? | journaux temporaires et sorties de staging | promouvoir une sortie partielle |
| `failed` | l’échec est-il classé et les effets bornés ? | diagnostic, logs et checkpoint vérifié | relancer indéfiniment ou masquer le code de sortie |
| `produced` | les sorties sont-elles complètes et hachées ? | artefacts et manifeste de run | confondre fin technique et acceptation |
| `reviewed` | les contrôles automatiques et humains sont-ils satisfaits ? | rapport de revue et décision | reconstruire silencieusement le candidat |
| `accepted` | le même artefact peut-il être promu dans son périmètre ? | paquet immuable et preuve | étendre l’usage au-delà des droits et tests |
| `withdrawn` | quelles dépendances et sorties doivent être remplacées ? | décision de retrait et historique | supprimer les preuves nécessaires |

Le cycle reprend la distinction entre cache, artefact, preuve et promotion du [vocabulaire DevOps](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#5-vocabulaire-opérationnel). Un workflow peut être `defined` dans cette fiche tout en restant entièrement non exécuté.

---

<!-- l5:card -->
## WORKFLOW-07 — Profil Solo

| Champ | Référence |
|---|---|
| besoin | obtenir une chaîne lisible et reproductible sur une machine principale sans infrastructure permanente |
| propriétaire | une personne identifiée peut cumuler exécution et approbation, mais enregistre explicitement son auto-revue |
| déclenchement | commande locale ou action manuelle ; aucune tâche cachée au démarrage du poste |
| configuration | un fichier versionné par workflow, valeurs locales séparées et chemins relatifs au dépôt |
| dépendances | nombre réduit, versions épinglées et repli manuel connu |
| preuve | journal, code de sortie, manifeste, empreintes et courte checklist |
| reprise | workspace par run, checkpoint borné et possibilité de repartir depuis les sources |
| sécurité | pas de secret dans Git ; répertoire d’écriture limité ; confirmation avant destruction |
| coût cognitif | une commande d’entrée, un rapport principal et une procédure de retrait |
| évolution | la même identité de workflow peut acquérir une variante Studio sans changer sa finalité |
| sources internes | [un produit, deux enveloppes](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md#3-un-produit-deux-enveloppes-opérationnelles), [architecture cible Python](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#4-architecture-cible) |
| preuve actuelle | variante documentaire ; aucune machine Solo qualifiée par cette fiche |

**Porte Solo :** le workflow doit pouvoir être compris, lancé, arrêté, nettoyé et repris par son propriétaire sans dépendre d’un service distant obligatoire.

---

<!-- l5:card -->
## WORKFLOW-08 — Profil Studio

| Champ | Référence |
|---|---|
| besoin | exécuter le même contrat avec responsabilités séparées, plusieurs profils et preuves centralisées |
| propriétaires | mainteneur du template, propriétaire métier, opérateur, réviseur et approbateur de promotion |
| déclenchement | PR, tag, planification ou demande manuelle selon le niveau de confiance |
| réutilisation | workflow appelé, action composite ou template central selon jobs, runners, secrets et visibilité des logs |
| matrices | plateformes, versions, variantes et capacités ; un échec n’est jamais converti en succès global |
| secrets | environnements protégés, accès minimal et absence sur les déclencheurs non fiables |
| artefacts | identité de run, commit, matrice, digests, rétention et attestation éventuelle |
| concurrence | groupes explicites, annulation sûre et limites par ressource rare |
| approbation | promotion indépendante, même artefact et motif des dérogations |
| retrait | désactiver les appelants, conserver les preuves et migrer vers une version qualifiée |
| sources internes | [responsabilités Studio](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md#3-un-produit-deux-enveloppes-opérationnelles), [portes de pull request](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#8-définir-les-portes-de-pull-request) |
| source officielle | [réutilisation des workflows GitHub Actions](https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations) |
| preuve actuelle | variante documentaire ; aucun runner, secret ou environnement Studio configuré |

---

<!-- l5:card -->
## WORKFLOW-09 — Sécurité et frontières

| Risque | Contrôle minimal | Preuve |
|---|---|---|
| écriture hors dépôt ou workspace | chemins relatifs résolus sous une racine autorisée | journal des chemins et refus des remontées |
| fichier externe non fiable | quarantaine, type réel, taille bornée, analyse et copie de travail | manifeste d’entrée et empreinte |
| script Blender ou custom node | source, commit, licence, permissions et auto-exécution contrôlée | registre de dépendance et revue du code |
| secret dans configuration | injection au runtime, masquage des logs et portée par job | scan, environnement protégé et rotation |
| service exposé | liaison locale, authentification, quotas et pare-feu | adresse d’écoute et test d’accès |
| données personnelles | minimisation, accès, rétention, retrait et stockage séparé | registre de traitement et propriétaire |
| sortie générative | staging ou quarantaine avant toute intégration | statut, revue humaine et provenance |
| commande destructive | simulation, aperçu, confirmation et sauvegarde adaptée | diff ou plan de suppression |
| dépendance distante | version ou SHA épinglé, intégrité et repli local | verrou, digest et source officielle |
| workflow de PR | aucun secret et permissions minimales | configuration du déclencheur et du jeton |

Les [sorties hors workspace](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#17-interdire-les-sorties-hors-du-workspace), la [quarantaine des fichiers externes](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#8-recevoir-et-mettre-en-quarantaine-les-fichiers-externes) et la [chaîne de confiance CI](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#6-cartographier-la-chaîne-de-confiance) s’appliquent ensemble.

**Niveau de preuve :** règles de sécurité relues ; aucun secret, fichier tiers ou service n’a été manipulé.

---

<!-- l5:card -->
## WORKFLOW-10 — Idempotence, retry et reprise

| Champ | Règle |
|---|---|
| idempotence | répéter une tâche avec les mêmes entrées ne crée pas de promotion supplémentaire ni de corruption |
| retry | autorisé seulement pour une cause transitoire classée, avec limite, délai et journal |
| non-retry | entrée invalide, licence bloquée, intégrité échouée, schéma incompatible ou décision humaine requise |
| checkpoint | plan, versions, entrées terminées, sorties hachées et état des effets de bord |
| reprise | accepter le checkpoint uniquement si l’empreinte du plan et des dépendances correspond |
| staging | chaque tentative écrit dans un espace distinct avant remplacement contrôlé |
| timeout | expiration du client, du processus et du service distinguées |
| concurrence | tâches indépendantes uniquement ; ressources exclusives et quotas déclarés |
| ordre | dérivé du graphe de dépendances, jamais de l’ordre du système de fichiers |
| nettoyage | conserver rapports et preuves ; supprimer uniquement les temporaires identifiés |
| sources internes | [reprise sur erreur](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#34-reprise-sur-erreur), [modèle mental d’un lot](../Livre-III/CHAPITRE-30-Automatisation-Blender-ComfyUI-et-production-en-lots.md#6-modèle-mental-dun-lot) |
| preuve actuelle | politique définie ; aucun échec réel ni checkpoint démontré |

**Réponse rapide :** une relance n’est pas une stratégie de diagnostic. Après la limite prévue, le workflow s’arrête avec un état explicite et conserve les éléments nécessaires à l’analyse.

---

<!-- l5:card -->
## WORKFLOW-11 — Manifestes et artefacts

| Objet | Champs minimaux |
|---|---|
| définition | workflow, version, propriétaire, but, schéma, chemin et SHA-256 |
| révision source | dépôt, commit, branche ou tag, état du workspace et sous-modules éventuels |
| environnement | OS, architecture, versions des outils, dépendances, backend et capacités |
| entrées | identifiant, chemin relatif, taille, empreinte, licence, consentement et statut |
| paramètres | configuration résolue, variables non secrètes, seed, limites et profils |
| exécution | run, tentative, début, fin, opérateur, runner, codes et diagnostics |
| sorties | rôle, chemin, type média, taille, empreinte et statut de staging |
| cache | clé, contenu reconstructible, durée et règle d’invalidation |
| revue | contrôles automatiques, réviseur, décision, réserves et périmètre |
| promotion | artefact source, canal, approbateur, date et preuve du même digest |
| retrait | raison, dépendants, remplacement, conservation et date d’effet |

Le modèle reprend le [manifeste d’artefact](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#21-définir-un-manifeste-dartefact) et la séparation entre [source, travail, master et export audio](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#7-séparer-source-travail-master-et-export-runtime).

**Règles :**

- un cache n’est pas téléversé comme preuve par défaut ;
- un artefact sans empreinte n’est pas promu ;
- un manifeste sans sortie ne prouve pas qu’un workflow a réussi ;
- les secrets sont référencés par identifiant, jamais copiés ;
- les chemins absolus propres au runner restent hors du format portable.

**Niveau de preuve :** schéma de référence ; aucun manifeste de production ni artefact du Companion Pack n’a été créé.

---

<!-- l5:matrix -->
## Matrice C — Qualification minimale

| Test | Entrée fixe | Observation | Preuve attendue | État dans cette fiche |
|---|---|---|---|---|
| Q1 — lecture | définition et version | champs, liens et propriétaire | revue sans ambiguïté | relu |
| Q2 — validation statique | template et schéma | format, chemins et valeurs fermées | rapport sans erreur | non exécuté pour un template |
| Q3 — environnement propre | verrou et instructions | installation ou résolution des dépendances | journal et versions | non exécuté |
| Q4 — cas nominal | entrée témoin autorisée | sortie et code de succès | artefact, manifeste et empreinte | non exécuté |
| Q5 — entrée invalide | cas volontairement fautif | refus avant effet dangereux | code stable et diagnostic | non exécuté |
| Q6 — interruption | job arrêté au point défini | nettoyage et checkpoint | reprise ou refus contrôlé | non exécuté |
| Q7 — retry | panne transitoire simulée | limite et délai | nombre de tentatives enregistré | non exécuté |
| Q8 — reproductibilité | même plan et environnement | octets ou équivalence annoncée | comparaison et définition du niveau | non exécuté |
| Q9 — repli | dépendance ou accélération absente | chemin alternatif | résultat fonctionnel ou report explicite | non exécuté |
| Q10 — sécurité | entrée non fiable ou déclencheur PR | moindre privilège et quarantaine | aucune fuite ni écriture hors frontière | non exécuté |
| Q11 — Solo/Studio | même contrat | différences de gouvernance seulement | deux manifestes comparables | non exécuté |
| Q12 — retrait | version bloquée | dépendants et remplacement | plan de migration et historique | non exécuté |

Le chapitre 21 possédera les résultats mesurés. Le chapitre 22 possédera les matrices historiques par versions. Cette matrice décrit uniquement la campagne nécessaire pour faire évoluer un workflow de `defined` vers `accepted`.

---

<!-- l5:card -->
## WORKFLOW-12 — Paquet et acceptation

| Élément du paquet | Exigence |
|---|---|
| fiche | identité, but, propriétaire, entrées, sorties, limites et liens vers les tutoriels |
| définition | fichier canonique lisible, schéma ou format déclaré et version sémantique |
| variantes | Solo et Studio séparées sans dupliquer la logique propriétaire |
| configuration | exemple sans secret, valeurs obligatoires, limites et ordre de résolution |
| dépendances | versions ou commits, licences, capacités, retrait et alternatives |
| fixtures | entrées minimales autorisées, petites et indépendantes des données personnelles |
| vérification | commande ou procédure minimale, codes de sortie et résultats attendus |
| sécurité | frontière d’écriture, réseau, secrets, fichiers tiers et opérations destructives |
| preuve | rapports, run, artefacts, digests, revue humaine et réserves |
| documentation | source propriétaire dans les Livres I à IV et date de vérification |
| Companion Pack | emplacement prévu et statut `not-materialized` tant que les fichiers n’existent pas |
| décision | `defined`, `qualified`, `accepted_limited`, `accepted`, `blocked`, `withdrawn` ou `superseded` |

**Porte minimale :** un template devient `accepted` seulement après validation statique, exécution nominale, échec contrôlé, repli, reprise, revue de sécurité et conservation de ses preuves. Une définition relue sans run reste `defined`.

**Frontières :**

- les tutoriels détaillés restent dans les Livres I à IV ;
- la fiche 03 possède les logiciels et leurs installations minimales ;
- la fiche 04 possède les moteurs, API et backends ;
- les fiches 05 à 07 possèdent les modèles et composants ;
- la fiche 08 possède les contrats et l’index des workflows réutilisables ;
- la fiche 09 possédera les prompts et variables ;
- le chapitre 10 possédera les scripts et recettes de code ;
- le chapitre 21 possédera les benchmarks exécutés ;
- le chapitre 22 possédera les compatibilités historiques ;
- le chapitre 24 possédera les checklists transversales ;
- le chapitre 25 possédera licences, provenance et conformité ;
- les fichiers réutilisables réels appartiendront au Companion Pack après matérialisation.

**Niveau de preuve :** `static-review`. Aucun workflow Godot, Blender, ComfyUI, audio ou documentation n’a été matérialisé dans le Companion Pack ; aucun script, modèle, import, export, média, build, mesure, secret, approbation juridique ou PDF n’a été produit.
