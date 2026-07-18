---
title: "Livre I — Chapitre 10 : Sécurité, sauvegarde et validation de la plateforme"
id: "DOC-L1-ENV-SECURITY"
status: "draft-review"
version: "1.2.0"
lang: "fr-FR"
book: "Livre I"
chapter: 10
last-verified: "2026-07-18"
reference-platform:
  os: "Windows 11 64 bits"
  scope: "plateforme locale IA et GameDev"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Sécurité, sauvegarde et validation de la plateforme

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L1-ENV-SECURITY`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Résultat attendu :** disposer d’une plateforme locale dont les secrets, sources, données, modèles et configurations sont inventoriés, sauvegardés, restaurables et validés avant le début du développement du jeu.

## 1. Objet du chapitre

Les chapitres précédents installent plusieurs couches :

> **[SORTIE] Résultat attendu - Ne pas saisir :** comparer avec la sortie obtenue.

```text
Windows et pilote AMD
├── terminal et PowerShell
├── Git, GitHub et VS Code
├── Python et environnements
├── Docker et volumes
├── Open WebUI et outils
├── ComfyUI, modèles et workflows
├── LLM locaux
└── audio IA local
```

Une plateforme qui démarre aujourd’hui mais ne peut pas être restaurée demain n’est pas considérée comme validée.

La règle principale est :

> Une sauvegarde n’existe réellement que lorsqu’une restauration a été testée et que ses dépendances sont connues.

## 2. Modèle de menace réaliste

Le parcours ne cherche pas à couvrir toutes les attaques possibles. Il traite en priorité :

- perte ou corruption d’un disque ;
- mise à jour incompatible ;
- suppression accidentelle ;
- fuite d’un jeton ou d’une clé ;
- exposition réseau involontaire ;
- extension VS Code, nœud ComfyUI ou paquet Python malveillant ;
- modèle ou fichier sérialisé non fiable ;
- conteneur trop privilégié ;
- synchronisation d’un fichier privé vers un dépôt public ;
- ransomware ou compte Windows compromis ;
- impossibilité de reconstruire une version ancienne.

## 3. Classer les données

### 3.1 Sources reproductibles

Exemples :

- Markdown ;
- code ;
- fichiers Compose ;
- scripts ;
- `pyproject.toml` ;
- fichiers de verrouillage ;
- workflows ComfyUI JSON ;
- manifestes ;
- schémas de base de données.

Ces fichiers doivent être versionnés dans Git lorsqu’ils ne contiennent pas de secret.

### 3.2 Données volumineuses remplaçables

Exemples :

- modèles téléchargés ;
- caches ;
- installateurs publics ;
- images Docker publiques ;
- dépendances reconstruisibles.

Conserver au minimum :

- source ;
- version ;
- licence ;
- empreinte ;
- procédure de téléchargement ou reconstruction.

Une copie locale ou hors ligne est recommandée lorsque la ressource peut disparaître.

### 3.3 Données uniques

Exemples :

- créations originales ;
- enregistrements vocaux autorisés ;
- projets Blender ;
- bases de connaissances annotées ;
- configurations affinées ;
- sauvegardes du jeu ;
- résultats de tests longs ;
- clés de signature.

Ces données exigent plusieurs copies et une restauration testée.

### 3.4 Secrets et données privées

Exemples :

- jetons GitHub ;
- clés API ;
- clés SSH privées ;
- mots de passe de bases ;
- certificats ;
- voix ou données personnelles ;
- conversations privées ;
- informations de participants aux tests.

Ces éléments ne doivent pas être placés dans un dépôt public, un log partagé ou une archive non chiffrée.

## 4. Inventaire de la plateforme

Créer :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
C:\IA-GameDev\platform-manifest\
├── hardware.yaml
├── windows.yaml
├── applications.yaml
├── python-environments.yaml
├── docker-services.yaml
├── models.yaml
├── volumes.yaml
├── secrets-register.yaml.example
├── backups.yaml
└── validation.md
```

Exemple `applications.yaml` :

> **[VSC] Visual Studio Code - Créer ou modifier :** `applications.yaml`.

```yaml
applications:
  - name: Git for Windows
    version: "version observée"
    source: "https://git-scm.com/"
    install_method: winget
    package_id: Git.Git
  - name: PowerShell
    version: "version observée"
    source: "Microsoft"
    install_method: winget
    package_id: Microsoft.PowerShell
```

Le registre de secrets ne contient jamais les valeurs secrètes. Il enregistre seulement :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
secrets:
  - id: SEC-GITHUB-AUTH
    purpose: "authentification GitHub"
    storage: "gestionnaire d’identifiants ou agent SSH"
    owner: "utilisateur ou rôle"
    rotation: "selon politique"
    recovery: "procédure séparée"
```

## 5. Politique 3-2-1 adaptée

Pour les données uniques :

- au moins trois copies ;
- sur au moins deux supports ou systèmes distincts ;
- dont une copie hors du poste principal.

Exemple Solo :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Copie 1 : SSD de travail
Copie 2 : disque externe déconnecté après sauvegarde
Copie 3 : stockage distant chiffré ou second lieu
```

Exemple Studio :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Copie 1 : stockage de production
Copie 2 : sauvegarde locale immuable ou versionnée
Copie 3 : site secondaire ou stockage objet avec rétention
```

GitHub est une copie distante des sources suivies, pas une sauvegarde des modèles, volumes Docker, bases locales et secrets.

## 6. Sauvegarder les sources Git

Vérifier l’état avant sauvegarde :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git status
git log --oneline --decorate -10
git remote -v
```

Synchroniser les commits voulus :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git push --all origin
git push --tags origin
```

Créer un bundle hors ligne :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git bundle create ..\backups\projet-$(Get-Date -Format yyyyMMdd).bundle --all
```

Vérifier :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git bundle verify ..\backups\projet-AAAAmmjj.bundle
```

Restaurer dans un dossier de test :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git clone ..\backups\projet-AAAAmmjj.bundle restauration-test
```

Les fichiers ignorés par Git doivent suivre une autre stratégie.

## 7. Sauvegarder Python

Ne pas sauvegarder `.venv` comme seule méthode de reprise.

Conserver :

- `pyproject.toml` ;
- `uv.lock` ou fichier équivalent ;
- `.python-version` ;
- sources Python ;
- contraintes spécifiques au backend ;
- versions des pilotes et bibliothèques externes ;
- roues ou archives nécessaires à une reconstruction hors ligne, si pertinent.

Test de restauration :

> **[VSC] Visual Studio Code - Créer ou modifier :** `.python-version`.

```powershell
Remove-Item .\.venv -Recurse -Force
uv sync --locked
uv run python -c "import sys; print(sys.executable)"
```

Une reconstruction doit réussir sans paquet installé manuellement et non déclaré.

## 8. Sauvegarder Docker

Conserver :

- `compose.yaml` et variantes ;
- `.env.example` ;
- configurations ;
- liste des images et digests ;
- exports logiques des bases ;
- archives des volumes importants ;
- procédures de restauration.

Inventaire :

> **[VSC] Visual Studio Code - Créer ou modifier :** `.env.example`.

```powershell
docker version > .\exports\docker-version.txt
docker image ls --digests > .\exports\docker-images.txt
docker volume ls > .\exports\docker-volumes.txt
docker compose config > .\exports\compose-resolved.yaml
```

Vérifier `compose-resolved.yaml` avant partage : l’interpolation peut y révéler une valeur sensible.

Sauvegarde générique d’un volume :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker run --rm `
  --mount source=nom_volume,target=/data,readonly `
  --mount type=bind,source="$PWD\backups",target=/backup `
  alpine:3.22 `
  tar -czf /backup/nom_volume.tar.gz -C /data .
```

Une base de données doit aussi utiliser son outil d’export logique.

## 9. Sauvegarder les modèles et workflows

Pour chaque modèle :

> **[VSC] Visual Studio Code - Créer ou modifier :** `tar -czf /backup/nom_volume.tar.gz -C /data .`.

```yaml
id: MODEL-EXAMPLE
name: "nom du modèle"
source: "URL officielle"
version: "version ou commit"
filename: "fichier"
sha256: "empreinte"
license: "licence"
usage: "LLM | image | audio"
required_by:
  - "workflow ou service"
```

Pour ComfyUI, conserver :

- workflows JSON ;
- manifestes ;
- liste des nœuds personnalisés ;
- versions ou commits ;
- snapshots du gestionnaire ;
- modèles et empreintes ;
- images de test avec métadonnées ;
- paramètres de lancement.

Pour les LLM, conserver :

- Modelfile ou configuration ;
- nom et hash du GGUF ;
- quantification ;
- contexte ;
- paramètres de génération ;
- benchmark de référence.

## 10. Secrets

### 10.1 Interdictions

Ne jamais stocker un secret dans :

- un fichier committé ;
- l’historique Git ;
- une capture d’écran publique ;
- un log de CI ;
- une URL ;
- un prompt envoyé à un service externe ;
- un fichier `compose-resolved.yaml` partagé sans inspection ;
- un workflow ComfyUI exporté publiquement.

### 10.2 Stockage

Selon le besoin :

- Git Credential Manager ;
- agent SSH ;
- gestionnaire de mots de passe ;
- coffre de secrets d’organisation ;
- secrets GitHub Actions ;
- secrets Docker ou fichiers montés hors dépôt.

Un fichier `.env` n’est pas sécurisé parce qu’il est caché. Il est seulement séparé de la configuration versionnée.

### 10.3 Fuite d’un secret

Procédure :

1. révoquer ou faire tourner le secret ;
2. arrêter l’usage concerné ;
3. identifier la portée et la durée d’exposition ;
4. rechercher les copies dans logs, archives et forks ;
5. nettoyer l’historique si nécessaire ;
6. documenter l’incident ;
7. corriger le mécanisme qui a permis la fuite.

La suppression du fichier dans un nouveau commit ne révoque pas un secret déjà exposé.

## 11. Protection GitHub

Pour un dépôt public :

- activer l’authentification multifacteur ;
- activer la protection de l’utilisateur lors du push ;
- activer les protections disponibles pour le dépôt ;
- examiner les alertes de dépendances ;
- limiter les permissions des workflows ;
- utiliser des environnements protégés pour les secrets de publication ;
- éviter les actions tierces non examinées.

La protection lors du push peut bloquer certaines informations d’identification avant leur arrivée dans le dépôt. Elle ne détecte pas tous les secrets possibles.

## 12. Réseau local

Par défaut :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Interface locale uniquement : 127.0.0.1
Réseau Docker interne : non publié
Accès LAN : désactivé sauf besoin documenté
Accès Internet entrant : interdit sans architecture dédiée
```

Vérifier les ports :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Get-NetTCPConnection -State Listen |
    Sort-Object LocalPort |
    Select-Object LocalAddress, LocalPort, OwningProcess
```

Identifier un processus :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Get-Process -Id IDENTIFIANT
```

Un service accessible sur `0.0.0.0` ou `::` doit être considéré comme potentiellement accessible depuis plusieurs interfaces.

## 13. Pare-feu et exposition

Ne pas désactiver globalement le pare-feu pour résoudre un problème de connexion.

Créer une règle uniquement lorsque :

- le service doit réellement être joint ;
- le protocole et le port sont connus ;
- la portée réseau est limitée ;
- l’authentification est adaptée ;
- la règle possède un propriétaire et une date de revue.

Après un test, supprimer les règles temporaires.

## 14. Logiciels et dépendances non fiables

### 14.1 Nœuds ComfyUI

Un nœud personnalisé est du code Python. Avant installation :

- vérifier le dépôt ;
- examiner la licence ;
- lire les dépendances ;
- rechercher les commandes système et accès réseau ;
- épingler une version ;
- tester dans un environnement séparé.

### 14.2 Extensions VS Code

Limiter les extensions et examiner :

- éditeur ;
- permissions ;
- dépôt source ;
- fréquence de maintenance ;
- changements de propriétaire ;
- nécessité réelle.

### 14.3 Modèles et données

Préférer les formats non exécutables lorsque possible. Un fichier `pickle`, certains checkpoints ou scripts intégrés peuvent exécuter du code lors du chargement.

Les modèles provenant d’une source inconnue doivent être isolés et analysés avant usage.

## 15. Chiffrement et accès au poste

Pour un poste contenant des secrets ou données privées :

- utiliser un compte Windows protégé ;
- activer un chiffrement de disque adapté lorsque disponible ;
- conserver la clé de récupération hors du poste ;
- verrouiller la session ;
- séparer les comptes administrateur et usage courant lorsque le contexte le justifie ;
- protéger les sauvegardes externes ;
- tester la récupération avant de dépendre du chiffrement.

Le chiffrement protège principalement les données au repos. Il ne protège pas un poste déjà déverrouillé et compromis.

## 16. Points de restauration et images système

Avant une modification majeure :

- créer un point de restauration lorsque la fonctionnalité est disponible ;
- sauvegarder les données uniques ;
- exporter les configurations ;
- télécharger la version précédente nécessaire au retour arrière ;
- noter les étapes de restauration.

Un point de restauration Windows ne remplace pas une sauvegarde indépendante des données.

## 17. Plan de reprise

Exemple :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
recovery_plan:
  target: "station IA GameDev"
  maximum_data_loss: "24 heures pour les données de travail"
  target_recovery_time: "une journée pour la plateforme de base"
  priorities:
    - "documents et code"
    - "clés et accès"
    - "bases et données uniques"
    - "configurations"
    - "modèles et caches"
  required_backups:
    - "bundle Git"
    - "exports Docker"
    - "manifestes des modèles"
    - "copie chiffrée des données uniques"
```

Ordre de restauration conseillé :

1. Windows et mises à jour validées ;
2. pilote AMD ;
3. terminal, Git, VS Code et Python ;
4. dépôt et configurations ;
5. Docker ;
6. modèles et applications IA ;
7. volumes et bases ;
8. tests d’acceptation.

## 18. Validation globale de la plateforme

### 18.1 Contrôles système

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
pwsh --version
git --version
code --version
py --list
uv --version
wsl --version
docker version
docker compose version
```

### 18.2 Contrôles de services

- Docker `hello-world` ;
- projet Compose de validation ;
- Open WebUI accessible localement ;
- Open Terminal isolé ;
- workflow ComfyUI minimal ;
- requête LLM locale ;
- synthèse ou transcription audio minimale.

### 18.3 Contrôles de reprise

- cloner un bundle Git dans un dossier vide ;
- reconstruire un environnement Python ;
- restaurer un petit volume Docker de test ;
- vérifier un modèle par SHA-256 ;
- restaurer un workflow ComfyUI ;
- vérifier qu’aucun secret n’est présent dans le dépôt ;
- redémarrer la machine et retester les services.

## 19. Rapport de validation

Créer :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
C:\IA-GameDev\platform-manifest\validation.md
```

Modèle :

> **[VSC] Visual Studio Code - Créer ou modifier :** `text C:\IA-GameDev\platform-manifest\validation.md`.

```markdown
# Validation de la plateforme

- Date :
- Utilisateur ou rôle :
- Windows :
- Pilote AMD :
- Git :
- Python / uv :
- Docker :
- ComfyUI :
- LLM :
- Audio :

## Tests réussis

- [ ] Terminal
- [ ] Git
- [ ] Python
- [ ] Docker
- [ ] Open WebUI
- [ ] ComfyUI
- [ ] LLM
- [ ] Audio
- [ ] Sauvegarde
- [ ] Restauration

## Réserves

## Prochaine date de revue
```

## 20. Mode Solo

Le Mode Solo doit au minimum posséder :

- dépôt distant des sources ;
- disque externe déconnecté après sauvegarde ;
- copie hors poste des données uniques ;
- gestionnaire de mots de passe ;
- manifestes des modèles ;
- sauvegarde mensuelle complète et sauvegardes incrémentales régulières ;
- test trimestriel de restauration ;
- liste courte des services exposés.

## 21. Mode Studio

Le Mode Studio ajoute :

- responsables de sauvegarde et sécurité ;
- objectifs de perte de données et de reprise ;
- stockage central avec rétention ;
- sauvegardes immuables ;
- rotation des secrets ;
- registre des accès ;
- revue des dépendances ;
- restauration testée sur une infrastructure distincte ;
- plan de réponse aux incidents ;
- preuves de validation et journal des exercices.

## 22. Checklist de clôture du Livre I

- [ ] Les dix chapitres sont présents dans `contents.txt`.
- [ ] Le poste de référence est inventorié.
- [ ] Les versions installées sont enregistrées.
- [ ] Les sources sont versionnées et synchronisées.
- [ ] Les secrets sont absents du dépôt.
- [ ] Les environnements Python sont reconstructibles.
- [ ] Les volumes Docker importants sont sauvegardés.
- [ ] Les modèles possèdent source, licence et empreinte.
- [ ] Les interfaces locales ne sont pas publiées inutilement.
- [ ] Une sauvegarde hors poste existe.
- [ ] Un bundle Git a été restauré.
- [ ] Un environnement Python a été recréé.
- [ ] Un volume Docker de test a été restauré.
- [ ] Les services principaux réussissent leurs tests minimaux.
- [ ] Le rapport de validation est rempli.

## 23. Sources officielles vérifiées

- [Sécurité Windows](https://learn.microsoft.com/windows/security/)
- [Restauration Windows à un instant antérieur](https://learn.microsoft.com/windows/configuration/point-in-time-restore)
- [Authentification GitHub](https://docs.github.com/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)
- [Protection des secrets lors du push](https://docs.github.com/code-security/concepts/secret-security/push-protection)
- [Sauvegarde et restauration Docker Desktop](https://docs.docker.com/desktop/settings-and-maintenance/backup-and-restore/)
- [Volumes Docker](https://docs.docker.com/engine/storage/volumes/)
- [Verrouillage et synchronisation `uv`](https://docs.astral.sh/uv/concepts/projects/sync/)
- [Sécurité PowerShell](https://learn.microsoft.com/powershell/scripting/security/security-features)

## 24. Résumé

Le Livre I ne se termine pas lorsque les interfaces s’ouvrent. Il se termine lorsque la plateforme est :

- comprise ;
- inventoriée ;
- versionnée ;
- isolée ;
- protégée ;
- sauvegardée ;
- restaurable ;
- testée.

Une fois ces critères satisfaits, le Livre II peut commencer sur un socle dont les erreurs et pertes restent maîtrisables.
