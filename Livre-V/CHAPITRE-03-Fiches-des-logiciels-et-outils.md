---
title: "Livre V — Fiche 03 : Fiches des logiciels et outils"
id: "DOC-L5-CH03"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 3
last-verified: "2026-07-28T13:42:52+02:00"
audit-status: "complete"
audit-date: "2026-07-28T13:42:52+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-03.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "software-and-tools"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Fiches des logiciels et outils

> **Type de document :** cartes normalisées d’outils, matrices de compatibilité et commandes minimales de vérification.
> **Lecture :** ouvrir directement la carte de l’outil, vérifier la date et le niveau de preuve, puis rejoindre le tutoriel propriétaire.
> **Principe :** une version citée est une référence datée de la collection, pas une promesse de dernière version ni de compatibilité universelle.

## Index express

| Outil ou famille | Ouvrir |
|---|---|
| Windows Terminal et PowerShell 7 | [OUTIL-01](#outil-01--windows-terminal-et-powershell-7) |
| WinGet | [OUTIL-02](#outil-02--winget) |
| Git for Windows | [OUTIL-03](#outil-03--git-for-windows) |
| GitHub et GitHub Actions | [OUTIL-04](#outil-04--github-et-github-actions) |
| Visual Studio Code | [OUTIL-05](#outil-05--visual-studio-code) |
| Python, lanceur `py` et `uv` | [OUTIL-06](#outil-06--python-lanceur-py-et-uv) |
| Docker Desktop, WSL 2 et Compose | [OUTIL-07](#outil-07--docker-desktop-wsl-2-et-compose) |
| Godot Engine | [OUTIL-08](#outil-08--godot-engine) |
| Blender | [OUTIL-09](#outil-09--blender) |
| ComfyUI | [OUTIL-10](#outil-10--comfyui) |
| Open WebUI | [OUTIL-11](#outil-11--open-webui) |
| Open Terminal | [OUTIL-12](#outil-12--open-terminal) |
| compatibilité d’ensemble | [Matrice A](#matrice-a--compatibilité-et-positionnement) |
| formats et intégrations | [Matrice B](#matrice-b--formats-interfaces-et-autorités) |
| commandes de vérification | [Matrice C](#matrice-c--commandes-minimales-de-vérification) |

---

<!-- l5:card -->
## OUTIL-00 — Contrat commun d’une carte

| Champ | Règle de lecture |
|---|---|
| rôle | fonction principale dans la collection ; ce champ ne décrit pas toutes les capacités du logiciel |
| référence datée | version ou état observé dans le chapitre propriétaire, avec sa date de vérification |
| installation minimale | voie d’entrée retenue par la collection ; la procédure détaillée reste dans le tutoriel source |
| formats et interfaces | fichiers, protocoles ou points d’intégration réellement utilisés par le guide |
| alternative ou repli | solution permettant de continuer sans rendre l’outil irremplaçable |
| limites | incompatibilités, risques, licence, sécurité ou statut expérimental à ne pas masquer |
| preuve | `static-review` signifie relu contre les sources du dépôt, sans exécution revendiquée dans cette fiche |

**Règle de mise à jour :** lorsqu’une version, une licence ou une compatibilité change, modifier d’abord le chapitre propriétaire, puis la présente carte. La [politique de compatibilité](../Volume-0/CHAPITRE-09-Politique-de-compatibilite.md) reste normative.

---

<!-- l5:matrix -->
## Matrice A — Compatibilité et positionnement

| Outil | Hôte Windows | WSL ou conteneur | GPU AMD Windows | Parcours principal |
|---|---|---|---|---|
| Windows Terminal / PowerShell | natif | héberge aussi des sessions WSL | sans objet | administration et scripts sur l’hôte |
| WinGet | natif | non retenu dans le conteneur | sans objet | découverte et installation de paquets Windows |
| Git | natif | possible dans WSL avec dépôt séparé ou règles explicites | sans objet | historique local et synchronisation |
| GitHub | service distant | accessible depuis les deux environnements | sans objet | PR, issues, CI et hébergement distant |
| VS Code | natif | accès WSL possible | sans objet | édition, comparaison et terminal intégré |
| Python | natif par environnement | possible dans WSL ou conteneur | dépend du backend et du projet | un environnement isolé par outil |
| Docker Desktop | natif avec backend WSL 2 | moteur Linux intégré | accès GPU AMD non présumé | services web, bases et API auxiliaires |
| Godot | natif | headless possible selon la cible | rendu natif du moteur | développement et exécution du jeu |
| Blender | natif | ligne de commande possible, non principale | rendu et viewport selon pilotes | source 3D canonique et export glTF |
| ComfyUI | natif dans le parcours AMD du guide | laboratoire séparé | CPU obligatoire, ZLUDA expérimental | workflow nodal versionné |
| Open WebUI | navigateur sur l’hôte | service Docker | le moteur IA reste externe | interface centrale auto-hébergée |
| Open Terminal | navigateur ou API | conteneur interne recommandé | sans objet | exécution agentique confinée |

**Lecture :** « possible » ne signifie ni officiellement pris en charge ni validé sur la machine de référence. Les décisions conditionnelles restent dans la [fiche 02](CHAPITRE-02-Arbres-de-decision.md).

---

<!-- l5:card -->
## OUTIL-01 — Windows Terminal et PowerShell 7

| Champ | Référence |
|---|---|
| rôle | Windows Terminal affiche les sessions ; PowerShell 7 interprète les commandes et manipule des objets |
| référence datée | Windows 11, Windows Terminal et PowerShell 7 ; source vérifiée le `2026-07-18` |
| installation minimale | WinGet ou sources Microsoft, puis réouverture du terminal |
| formats et interfaces | scripts `.ps1`, variables d’environnement, pipelines d’objets, codes de sortie |
| intégrations | Git, Python, Docker, Godot headless, Blender CLI et outils de validation |
| alternative ou repli | `cmd.exe` pour quelques outils historiques ; WSL pour les commandes Linux explicitement marquées |
| limites | une commande PowerShell n’est pas automatiquement valide dans CMD ou Bash ; éviter l’élévation par défaut |
| tutoriel propriétaire | [Terminal, console et shell](../Livre-I/CHAPITRE-02-Terminal-PowerShell-et-outils-Windows.md#2-terminal-console-et-shell) et [installation des outils de base](../Livre-I/CHAPITRE-02-Terminal-PowerShell-et-outils-Windows.md#3-installer-les-outils-de-base) |
| liens officiels | [documentation PowerShell](https://learn.microsoft.com/powershell/), [documentation Windows Terminal](https://learn.microsoft.com/windows/terminal/) |
| preuve | `static-review` ; aucune installation exécutée dans cette fiche |

---

<!-- l5:card -->
## OUTIL-02 — WinGet

| Champ | Référence |
|---|---|
| rôle | rechercher, inspecter et installer des paquets Windows depuis une source nommée |
| référence datée | inclus dans Windows 11 via App Installer selon la source vérifiée le `2026-07-18` |
| installation minimale | mettre à jour App Installer si `winget` est absent |
| formats et interfaces | identifiant de paquet, source, version et options `--exact` |
| intégrations | installation de PowerShell, Windows Terminal, Git, VS Code et Python |
| alternative ou repli | installateur officiel téléchargé et archivé avec sa provenance |
| limites | vérifier l’éditeur, la source et la version avant installation ; une recherche non exacte peut sélectionner un mauvais paquet |
| tutoriel propriétaire | [Vérifier WinGet](../Livre-I/CHAPITRE-02-Terminal-PowerShell-et-outils-Windows.md#31-vérifier-winget) |
| lien officiel | [documentation WinGet](https://learn.microsoft.com/windows/package-manager/winget/) |
| preuve | `static-review` ; aucun paquet installé dans cette fiche |

---

<!-- l5:card -->
## OUTIL-03 — Git for Windows

| Champ | Référence |
|---|---|
| rôle | historique distribué des sources, configurations, manifestes et petits jeux de test |
| référence datée | Git for Windows `2.55.0` observé lors de la vérification du `2026-07-18` |
| installation minimale | paquet `Git.Git`, branche initiale `main`, identité de commit et gestionnaire d’identifiants unique |
| formats et interfaces | dépôt `.git`, index, commits, branches, tags, fichiers `.gitignore` et attributs |
| intégrations | GitHub, VS Code, Godot, Blender, documentation et CI |
| alternative ou repli | Git local fonctionne sans GitHub ; une archive complète reste nécessaire pour les données hors Git |
| limites | ne pas versionner secrets, caches, environnements Python, modèles volumineux ni sorties reconstruites |
| tutoriel propriétaire | [Rôle de Git](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md#1-rôle-de-git-dans-le-projet) et [installer Git for Windows](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md#3-installer-git-for-windows) |
| lien officiel | [documentation Git](https://git-scm.com/docs) |
| preuve | version datée issue du tutoriel ; aucune commande Git exécutée dans cette fiche |

---

<!-- l5:card -->
## OUTIL-04 — GitHub et GitHub Actions

| Champ | Référence |
|---|---|
| rôle | hébergement distant, pull requests, issues, protections, automatisation et artefacts de CI |
| référence datée | service sans version unique ; comportement qualifié par les workflows du dépôt au `2026-07-28` |
| installation minimale | aucun client obligatoire au-delà de Git ; authentification et dépôt distant configurés dans le tutoriel |
| formats et interfaces | Git, YAML de workflows, statuts de commit, artefacts et journaux |
| intégrations | VS Code, branches protégées, tests, construction documentaire et publication |
| alternative ou repli | le dépôt local reste utilisable hors ligne ; les contrôles critiques doivent pouvoir être relancés localement |
| limites | ne pas stocker de secret en clair ; une CI verte ne remplace pas les tests runtime non exécutés |
| tutoriel propriétaire | [Git, GitHub et VS Code](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md#2-git-github-et-vs-code) et [DevOps et intégration continue](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md) |
| lien officiel | [documentation GitHub](https://docs.github.com/) |
| preuve | les workflows du dépôt constituent une preuve documentaire datée, pas une qualification matérielle globale |

---

<!-- l5:card -->
## OUTIL-05 — Visual Studio Code

| Champ | Référence |
|---|---|
| rôle | édition des fichiers, terminal intégré, comparaison Git, extensions et débogage selon le langage |
| référence datée | Visual Studio Code sur Windows 11, source vérifiée le `2026-07-18` ; enregistrer la version réellement installée |
| installation minimale | installateur utilisateur ou paquet `Microsoft.VisualStudioCode`, puis profil dédié au projet |
| formats et interfaces | Markdown, YAML, JSON, Python, GDScript, paramètres `.vscode` et tâches |
| intégrations | Git, Python, Godot, Docker, WSL et outils documentaires |
| alternative ou repli | éditeur de scripts intégré de Godot ou autre éditeur qualifié par l’équipe |
| limites | chaque extension exécute du code ; limiter les extensions et distinguer réglages partagés et préférences personnelles |
| tutoriel propriétaire | [Installer Visual Studio Code](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md#5-installer-visual-studio-code) |
| lien officiel | [documentation Visual Studio Code](https://code.visualstudio.com/docs) |
| preuve | `static-review` ; aucun profil ni extension installé dans cette fiche |

---

<!-- l5:card -->
## OUTIL-06 — Python, lanceur `py` et `uv`

| Champ | Référence |
|---|---|
| rôle | automatisation, validation, conversion, outils IA et génération de données |
| référence datée | CPython `3.14.6` publié et `3.13.14` conservé comme repli de compatibilité au `2026-07-18` |
| installation minimale | installateur officiel ou gestionnaire documenté, puis environnement isolé par application |
| formats et interfaces | `pyproject.toml`, fichier de verrouillage, `requirements.txt`, environnement `.venv` |
| intégrations | ComfyUI, audio, scripts Blender, validation documentaire et automatisation du Livre II |
| alternative ou repli | `venv` et `pip` restent le chemin standard ; `uv` accélère la gestion sans supprimer l’obligation de verrouillage |
| limites | la version la plus récente n’est pas automatiquement compatible ; éviter le Python global partagé entre outils |
| tutoriel propriétaire | [Pourquoi isoler Python](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#1-pourquoi-isoler-python), [choisir une version](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#3-choisir-une-version-de-python) et [créer un environnement](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#5-créer-un-environnement-avec-venv) |
| liens officiels | [documentation Python](https://docs.python.org/3/), [documentation uv](https://docs.astral.sh/uv/) |
| preuve | versions issues du tutoriel daté ; aucun environnement créé dans cette fiche |

---

<!-- l5:card -->
## OUTIL-07 — Docker Desktop, WSL 2 et Compose

| Champ | Référence |
|---|---|
| rôle | isoler et orchestrer interfaces web, API, bases, outils documentaires et services auxiliaires |
| référence datée | Docker Desktop avec backend WSL 2 ; WSL `2.1.5` ou ultérieur indiqué par la source vérifiée le `2026-07-18` |
| installation minimale | Docker Desktop, moteur Linux WSL 2, virtualisation active et Compose intégré |
| formats et interfaces | image, conteneur, volume, réseau, `Dockerfile`, `compose.yaml`, registre et digest |
| intégrations | Open WebUI, Open Terminal, bases relationnelles ou vectorielles et services locaux |
| alternative ou repli | exécution native sur Windows lorsque l’accès matériel, le diagnostic ou la simplicité le justifie |
| limites | l’accès GPU AMD n’est pas présumé dans Docker Desktop Windows ; vérifier aussi les conditions de licence Docker Desktop |
| tutoriel propriétaire | [Objet de Docker](../Livre-I/CHAPITRE-05-Docker-et-Docker-Compose.md#1-objet-du-chapitre), [positionnement officiel](../Livre-I/CHAPITRE-05-Docker-et-Docker-Compose.md#3-positionnement-officiel-au-18-juillet-2026) et [installer Docker Desktop](../Livre-I/CHAPITRE-05-Docker-et-Docker-Compose.md#5-installer-docker-desktop) |
| liens officiels | [installation Docker Desktop sous Windows](https://docs.docker.com/desktop/setup/install/windows-install/), [documentation Compose](https://docs.docker.com/compose/) |
| preuve | `static-review` ; aucun moteur ni conteneur lancé dans cette fiche |

---

<!-- l5:card -->
## OUTIL-08 — Godot Engine

| Champ | Référence |
|---|---|
| rôle | moteur du jeu, éditeur de scènes, runtime GDScript, import des assets et export des livrables |
| référence datée | Godot `4.7.1-stable`, édition Standard, GDScript et Forward+ ; vérifié le `2026-07-18` |
| installation minimale | archive ou installateur officiel de la version stable, chemin enregistré et mise à jour réversible |
| formats et interfaces | `project.godot`, scènes `.tscn`, Resources `.tres`, GDScript `.gd`, glTF/GLB, commandes headless |
| intégrations | Git, VS Code, Blender, services IA derrière des contrats et pipeline d’export |
| alternative ou repli | édition .NET lorsque C# est une décision explicite ; mode headless pour import et smoke tests |
| limites | ne pas ouvrir l’unique copie du projet avec une version de développement ; Standard et .NET ne sont pas interchangeables sans décision |
| tutoriel propriétaire | [Version de Godot retenue](../Livre-II/CHAPITRE-01-Decouvrir-Godot-et-creer-le-projet-fil-rouge.md#3-version-de-godot-retenue), [scènes et nœuds](../Livre-II/CHAPITRE-03-Scenes-noeuds-Resources-et-signaux.md) et [exports](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md) |
| liens officiels | [documentation Godot 4.7](https://docs.godotengine.org/en/4.7/), [archive Godot](https://godotengine.org/download/archive/) |
| preuve | version documentaire ; aucun projet ouvert ou exporté dans cette fiche |

---

<!-- l5:card -->
## OUTIL-09 — Blender

| Champ | Référence |
|---|---|
| rôle | source canonique des assets 3D, édition, rigging, animation, baking et export |
| référence datée | Blender `5.2.0` Stable, qualifié par revue documentaire le `2026-07-22` |
| installation minimale | version Stable depuis `blender.org`, sans add-on tiers obligatoire pour le chemin glTF |
| formats et interfaces | source `.blend`, bibliothèques, caches, glTF 2.0, conteneur GLB et scripts Python |
| intégrations | Godot `4.7.1-stable`, Git ou Git LFS selon la politique, VS Code et automatisation Python |
| alternative ou repli | import direct `.blend` réservé à l’itération Solo ; GLB reste le conteneur d’échange principal |
| limites | un export n’est pas une source ; tout add-on futur doit être qualifié par version, licence, permissions et retrait |
| tutoriel propriétaire | [Niveau de preuve et réserves](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md#3-niveau-de-preuve-et-réserves), [qualifier la chaîne](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md#4-qualifier-la-chaîne-doutils) et [importation dans Godot](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#1-rôle-du-chapitre) |
| liens officiels | [téléchargement Blender](https://www.blender.org/download/), [manuel Blender 5.2](https://docs.blender.org/manual/en/5.2/) |
| preuve | `static-review` ; aucun fichier `.blend` ni export GLB exécuté dans cette fiche |

---

<!-- l5:card -->
## OUTIL-10 — ComfyUI

| Champ | Référence |
|---|---|
| rôle | graphe nodal de génération et traitement visuel, automatisable par API |
| référence datée | ComfyUI `v0.28.0`, tag stable observé et vérifié le `2026-07-18` |
| installation minimale | installation manuelle isolée, environnement CPU validé, code épinglé par tag et commit |
| formats et interfaces | workflow JSON, modèles et manifestes, nœuds, API locale, entrées et sorties médias |
| intégrations | Python, concept art, production en lots, Blender et pipelines documentés |
| alternative ou repli | CPU obligatoire ; ZLUDA en laboratoire isolé ; DirectML classé secours dégradé |
| limites | Desktop Windows non retenu pour la RX 6750 XT ; ne jamais utiliser `latest` comme preuve ; les nœuds tiers modifient la surface de confiance |
| tutoriel propriétaire | [État officiel](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#2-état-officiel-au-18-juillet-2026), [matrice de décision](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#3-matrice-de-décision) et [production en lots](../Livre-III/CHAPITRE-30-Automatisation-Blender-ComfyUI-et-production-en-lots.md) |
| liens officiels | [documentation ComfyUI](https://docs.comfy.org/), [dépôt ComfyUI](https://github.com/Comfy-Org/ComfyUI) |
| preuve | revue statique ; aucun workflow, modèle ou backend exécuté dans cette fiche |

---

<!-- l5:card -->
## OUTIL-11 — Open WebUI

| Champ | Référence |
|---|---|
| rôle | interface centrale pour conversations, connaissances, outils, agents et fournisseurs de modèles |
| référence datée | projet et architecture Docker vérifiés le `2026-07-18` ; image à épingler par version ou digest |
| installation minimale | conteneur officiel, volume persistant, authentification active, secret stable et liaison locale |
| formats et interfaces | navigateur, API de moteurs, Open Responses, connaissances, outils, MCP et volume de données |
| intégrations | Ollama ou serveur compatible sur l’hôte, Open Terminal sur réseau interne et sauvegarde Docker |
| alternative ou repli | autre interface qualifiée ou accès direct à l’API du moteur ; les données doivent rester exportables |
| limites | une interface n’est pas un moteur ; ne pas partager le volume stable avec une image de développement ; ne pas désactiver l’authentification par défaut |
| tutoriel propriétaire | [Objet du chapitre](../Livre-I/CHAPITRE-06-Open-WebUI-Open-Terminal-et-Vane.md#1-objet-du-chapitre), [état des projets](../Livre-I/CHAPITRE-06-Open-WebUI-Open-Terminal-et-Vane.md#3-état-des-projets-au-18-juillet-2026) et [décisions de sécurité](../Livre-I/CHAPITRE-06-Open-WebUI-Open-Terminal-et-Vane.md#4-décisions-de-sécurité) |
| lien officiel | [documentation Open WebUI](https://docs.openwebui.com/) |
| preuve | `static-review` ; aucune image téléchargée ni conversation créée dans cette fiche |

---

<!-- l5:card -->
## OUTIL-12 — Open Terminal

| Champ | Référence |
|---|---|
| rôle | API et serveur MCP permettant à un assistant d’exécuter des commandes et de manipuler un espace de travail |
| référence datée | intégration qualifiée dans le chapitre de plateforme vérifié le `2026-07-18` |
| installation minimale | conteneur sur réseau Docker interne, clé API, espace de travail dédié et aucun port publié vers l’hôte |
| formats et interfaces | API, MCP, commandes, fichiers, scripts et réseau interne |
| intégrations | Open WebUI et dépôt de travail explicitement monté |
| alternative ou repli | exécution humaine dans PowerShell ; mode natif uniquement lorsque l’accès Windows est indispensable et le risque accepté |
| limites | ne jamais monter le profil Windows, le socket Docker, les clés SSH ou les secrets ; validation humaine pour toute action destructive |
| tutoriel propriétaire | [Open Terminal](../Livre-I/CHAPITRE-06-Open-WebUI-Open-Terminal-et-Vane.md#32-open-terminal) et [décisions de sécurité](../Livre-I/CHAPITRE-06-Open-WebUI-Open-Terminal-et-Vane.md#42-open-terminal) |
| lien officiel | [dépôt Open Terminal](https://github.com/open-webui/open-terminal) |
| preuve | description statique d’une frontière de confiance ; aucun agent ni terminal exécuté dans cette fiche |

---

<!-- l5:matrix -->
## Matrice B — Formats, interfaces et autorités

| Outil | Entrées principales | Sorties ou autorité | Ne doit pas devenir |
|---|---|---|---|
| Git | fichiers versionnés | historique et commits | sauvegarde de tous les binaires et secrets |
| GitHub | commits et workflows | revue, statuts et artefacts | preuve d’un test runtime absent |
| VS Code | dossier de travail | fichiers modifiés et diagnostics d’éditeur | autorité métier du jeu |
| Python | code, dépendances et données | scripts, rapports et artefacts générés | environnement global partagé |
| Docker | images, Compose et secrets injectés | services et volumes persistants | accès GPU AMD supposé |
| Godot | scènes, Resources, scripts et imports | projet exécutable et exports | outil de production des sources 3D |
| Blender | sources `.blend` et bibliothèques | exports glTF/GLB | stockage autoritaire du runtime |
| ComfyUI | workflow, modèles et entrées | médias et métadonnées | preuve de provenance sans manifeste |
| Open WebUI | requêtes, connaissances et outils | conversations et orchestration d’interface | moteur ou source de vérité métier |
| Open Terminal | commandes et espace monté | effets sur les fichiers et processus | accès général au poste |

---

<!-- l5:matrix -->
## Matrice C — Commandes minimales de vérification

| Outil | Contexte et commande | Ce que la sortie doit prouver |
|---|---|---|
| PowerShell | **[PS]** `pwsh --version` | version du shell réellement lancé |
| Windows Terminal | **[PS]** `wt --version` | présence de l’application terminal |
| WinGet | **[PS]** `winget --version` | gestionnaire accessible dans la session |
| Git | **[PS]** `git --version` | version du binaire présent dans le `PATH` |
| VS Code | **[PS]** `code --version` | version et architecture de l’éditeur |
| Python | **[PS]** `py --list-paths` | versions installées et chemins des interpréteurs |
| Docker | **[PS]** `docker version` | client et moteur accessibles |
| Compose | **[PS]** `docker compose version` | plugin Compose intégré disponible |
| WSL | **[PS]** `wsl --status` | backend et version par défaut |
| Godot | **[PS]** `& $env:GODOT_EXE --version` | version de l’exécutable explicitement sélectionné |
| Blender | **[PS]** `blender --version` | version du binaire lorsque son dossier est déclaré |
| ComfyUI | **[PS]** `git -C <installation> describe --tags --always` | tag ou commit de l’installation ; remplacer `<installation>` |
| Open WebUI | **[PS]** `docker image inspect <image> --format "{{json .RepoDigests}}"` | digest de l’image ; remplacer `<image>` |
| Open Terminal | **[PS]** `docker image inspect <image> --format "{{json .RepoDigests}}"` | digest de l’image ; remplacer `<image>` |

**Limite :** ces commandes identifient une installation. Elles ne prouvent ni sa compatibilité fonctionnelle, ni ses performances, ni sa sécurité. Les procédures de correction restent dans les tutoriels propriétaires.

---

## Frontières de la fiche

Cette fiche possède l’identité, le rôle, les formats, les intégrations, les alternatives, les limites et les références officielles des outils. Elle ne possède pas :

- les installations complètes, qui restent dans les Livres I à III ;
- les décisions conditionnelles, qui restent dans la [fiche 02](CHAPITRE-02-Arbres-de-decision.md) ;
- les moteurs et backends IA, réservés au chapitre 4 ;
- les modèles de langage, visuels ou audio, réservés aux chapitres 5 à 7 ;
- les comparatifs détaillés et coûts de migration, réservés au chapitre 23 ;
- les matrices de compatibilité versionnées et preuves d’exécution, réservées au chapitre 22 et aux campagnes runtime.

**Niveau de preuve :** `static-review`. Aucun logiciel n’a été installé, lancé, mis à jour ou benchmarké pour produire cette fiche.
