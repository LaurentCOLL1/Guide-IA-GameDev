---
title: "Livre I — Chapitre 3 : Git, GitHub et Visual Studio Code"
id: "DOC-L1-ENV-GIT"
status: "draft-review"
version: "1.0.0"
lang: "fr-FR"
book: "Livre I"
chapter: 3
last-verified: "2026-07-18"
reference-platform:
  os: "Windows 11 64 bits"
  vcs: "Git for Windows"
  editor: "Visual Studio Code"
---

# Git, GitHub et Visual Studio Code

> **Identifiant stable :** `DOC-L1-ENV-GIT`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Résultat attendu :** disposer d’un dépôt local propre, synchronisé avec GitHub, ouvert dans VS Code et capable de restaurer une modification sans perdre les modèles, caches ou secrets exclus du versionnement.

## 1. Rôle de Git dans le projet

Git enregistre l’évolution des sources :

- documentation Markdown ;
- scripts ;
- code Godot et Python ;
- configurations ;
- schémas de données ;
- petits fichiers de test ;
- manifestes d’assets et de modèles.

Git n’est pas une sauvegarde universelle de la station de travail. Il ne doit pas contenir automatiquement :

- modèles IA volumineux ;
- caches ;
- environnements Python ;
- bases locales contenant des données privées ;
- sorties générées ;
- mots de passe, jetons ou clés ;
- fichiers binaires temporaires de Blender ou Godot.

La règle principale est :

> Un commit doit représenter un changement compréhensible, restaurable et suffisamment petit pour être relu.

## 2. Git, GitHub et VS Code

```text
Git
└── historique local distribué

GitHub
├── hébergement du dépôt distant
├── issues et pull requests
├── CI avec GitHub Actions
└── protections et collaboration

Visual Studio Code
├── édition des fichiers
├── terminal intégré
├── comparaison des changements
├── extensions
└── débogage selon les langages
```

Un dépôt Git fonctionne sans GitHub. GitHub ajoute la synchronisation distante et les outils collaboratifs.

## 3. Installer Git for Windows

### 3.1 Installation avec WinGet

```powershell
winget show --id Git.Git --exact --source winget
winget install --id Git.Git --exact --source winget
```

Fermer et rouvrir PowerShell :

```powershell
git --version
where.exe git
```

Le site officiel Git publiait Git for Windows 2.55.0 lors de la vérification du 18 juillet 2026. Le guide ne dépend pas de ce numéro exact : enregistrer la version réellement installée.

### 3.2 Choix d’installation recommandés

Pour un débutant :

- Git disponible depuis la ligne de commande et les logiciels tiers ;
- gestionnaire d’identifiants Git Credential Manager activé ;
- fins de ligne Windows gérées avec prudence ;
- branche initiale nommée `main` ;
- éditeur par défaut VS Code après son installation ;
- OpenSSH fourni avec Windows ou Git, mais une seule configuration clairement documentée.

Ne pas activer plusieurs gestionnaires d’identifiants concurrents.

## 4. Configurer l’identité Git

```powershell
git config --global user.name "Votre nom"
git config --global user.email "adresse-associee-au-compte@example.com"
git config --global init.defaultBranch main
```

Vérifier :

```powershell
git config --global --list --show-origin
```

Le nom et l’adresse figurent dans les commits. Pour un dépôt public, GitHub permet d’utiliser une adresse `noreply` associée au compte.

Ne pas confondre :

- identité de commit ;
- authentification GitHub ;
- autorisation d’accès à un dépôt.

## 5. Installer Visual Studio Code

### 5.1 Installation

Le programme d’installation utilisateur est le choix recommandé pour la majorité des postes individuels.

```powershell
winget show --id Microsoft.VisualStudioCode --exact --source winget
winget install --id Microsoft.VisualStudioCode --exact --source winget
```

Vérifier :

```powershell
code --version
```

Ouvrir le dossier courant :

```powershell
code .
```

### 5.2 Profil dédié

Créer un profil VS Code nommé `IA GameDev` afin d’isoler les réglages du projet.

Extensions de départ possibles :

- Markdown All in One ;
- YAML ;
- Python ;
- GitLens, optionnel ;
- EditorConfig ;
- extension Godot/GDScript retenue par le Livre II.

Installer uniquement les extensions nécessaires. Chaque extension exécute du code avec des droits importants dans l’éditeur.

### 5.3 Paramètres du workspace

Exemple `.vscode/settings.json` :

```json
{
  "files.encoding": "utf8",
  "files.eol": "\n",
  "editor.formatOnSave": false,
  "files.exclude": {
    "**/.venv": true,
    "**/__pycache__": true,
    "**/.godot": true
  }
}
```

Les réglages partagés doivent rester utiles à tous les contributeurs. Les préférences personnelles appartiennent au profil utilisateur.

## 6. Créer un dépôt local

```powershell
New-Item -ItemType Directory -Force C:\IA-GameDev\workspaces\mon-projet | Out-Null
Set-Location C:\IA-GameDev\workspaces\mon-projet
git init
```

Créer un fichier :

```powershell
"# Mon projet" | Out-File README.md -Encoding utf8
git status
```

Ajouter et committer :

```powershell
git add README.md
git commit -m "docs: initialize project"
```

Vérifier :

```powershell
git log --oneline --decorate --graph --all
```

## 7. Comprendre la zone de travail

Git distingue :

```text
fichiers de travail
       ↓ git add
index ou staging area
       ↓ git commit
historique local
       ↓ git push
dépôt distant
```

Commandes essentielles :

```powershell
git status
git diff
git diff --staged
git log --oneline
```

Avant chaque commit :

1. lire `git status` ;
2. lire `git diff` ;
3. ajouter seulement les fichiers voulus ;
4. relire `git diff --staged` ;
5. écrire un message explicite.

## 8. `.gitignore`

Exemple de base :

```gitignore
# Secrets
.env
.env.*
!.env.example
secrets/

# Python
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
.ruff_cache/

# Godot
.godot/

# Modèles et caches IA
models/
modeles/
cache/
caches/
outputs/

# Docker et données locales
data/
backups/
*.log

# Système et éditeur
Thumbs.db
.DS_Store
```

Tester l’exclusion :

```powershell
git check-ignore -v .env
git status --ignored
```

Un `.gitignore` n’efface pas un fichier déjà suivi. Pour arrêter de le suivre sans le supprimer localement :

```powershell
git rm --cached .env
```

Si un secret a déjà été committé, le retirer du dernier commit ne suffit pas : il faut le révoquer immédiatement et traiter l’historique.

## 9. `.gitattributes` et fins de ligne

Exemple :

```gitattributes
* text=auto eol=lf
*.ps1 text eol=crlf
*.bat text eol=crlf
*.png binary
*.jpg binary
*.glb binary
*.blend binary
```

Cette politique doit être décidée avant que le dépôt contienne de nombreux fichiers afin d’éviter des diffs entièrement réécrits.

Vérifier :

```powershell
git check-attr -a -- README.md
git diff --check
```

## 10. Git LFS

Git LFS peut suivre certains gros binaires versionnés :

- `.blend` ;
- `.glb` ;
- grosses textures sources ;
- fichiers audio maîtres ;
- archives indispensables et raisonnablement dimensionnées.

Il ne transforme pas GitHub en stockage illimité de modèles IA.

Installation :

```powershell
winget install --id GitHub.GitLFS --exact --source winget
git lfs install
```

Exemple :

```powershell
git lfs track "*.blend"
git lfs track "*.glb"
git add .gitattributes
```

Vérifier avant le commit :

```powershell
git lfs status
git lfs ls-files
```

Les quotas, coûts et conditions du service distant doivent être vérifiés avant un usage Studio.

## 11. Créer le dépôt GitHub

Créer un dépôt vide depuis GitHub, sans réinitialiser les fichiers si le dépôt local existe déjà.

Ajouter le remote :

```powershell
git remote add origin https://github.com/UTILISATEUR/DEPOT.git
git remote -v
git push -u origin main
```

Ne jamais inclure un jeton dans l’URL du remote.

## 12. Authentification GitHub

### 12.1 HTTPS avec Git Credential Manager

GitHub n’accepte pas le mot de passe du compte pour les opérations Git HTTPS. Utiliser :

- l’authentification navigateur proposée par Git Credential Manager ;
- GitHub CLI ;
- un jeton d’accès personnel à portée limitée lorsque nécessaire.

Les jetons doivent être traités comme des mots de passe.

### 12.2 GitHub CLI

Installation :

```powershell
winget install --id GitHub.cli --exact --source winget
gh --version
gh auth login
```

Vérifier :

```powershell
gh auth status
```

### 12.3 SSH

Générer une clé Ed25519 :

```powershell
ssh-keygen -t ed25519 -C "adresse-associee-au-compte@example.com"
```

La clé privée ne quitte pas le poste. Seule la clé publique est ajoutée au compte GitHub.

Tester :

```powershell
ssh -T git@github.com
```

Modifier le remote :

```powershell
git remote set-url origin git@github.com:UTILISATEUR/DEPOT.git
```

Protéger la clé privée avec une phrase secrète et une sauvegarde chiffrée adaptée.

## 13. Branches et changements isolés

Créer une branche :

```powershell
git switch -c docs/ajouter-chapitre
git status
```

Après les modifications :

```powershell
git add .
git commit -m "docs: add chapter"
git push -u origin docs/ajouter-chapitre
```

Une branche doit traiter un objectif cohérent.

Convention recommandée :

```text
feat/...
fix/...
docs/...
refactor/...
test/...
chore/...
```

## 14. Mettre à jour sans écraser son travail

Avant de récupérer :

```powershell
git status
```

Récupérer les références distantes :

```powershell
git fetch --prune
```

Mettre à jour la branche principale lorsqu’elle est propre :

```powershell
git switch main
git pull --ff-only
```

`--ff-only` empêche Git de créer automatiquement un commit de fusion inattendu.

## 15. Restaurer une erreur

### 15.1 Annuler une modification non ajoutée

```powershell
git diff -- chemin\fichier.md
git restore chemin\fichier.md
```

### 15.2 Retirer de l’index sans perdre le fichier

```powershell
git restore --staged chemin\fichier.md
```

### 15.3 Créer un commit inverse

Pour un commit déjà partagé :

```powershell
git revert IDENTIFIANT_DU_COMMIT
```

### 15.4 Retrouver une référence

```powershell
git reflog
```

Ne pas utiliser `git reset --hard`, `git clean -fdx` ou une réécriture d’historique sans comprendre précisément ce qui sera perdu.

## 16. Pull requests et revues

Une pull request doit fournir :

- le problème traité ;
- les changements principaux ;
- les fichiers ou systèmes affectés ;
- la méthode de test ;
- les limites connues ;
- les captures ou journaux utiles ;
- la stratégie de retour arrière.

Pour le Mode Solo, une pull request personnelle reste utile pour déclencher la CI et relire le diff avant fusion.

## 17. Sécurité du dépôt

### Règles obligatoires

- activer l’authentification multifacteur du compte ;
- ne jamais versionner de secret ;
- utiliser des jetons à portée minimale ;
- supprimer les accès devenus inutiles ;
- vérifier les actions GitHub tierces avant usage ;
- épingler les actions critiques à une version ou un commit approuvé ;
- examiner les fichiers binaires et scripts ajoutés par une dépendance.

GitHub propose une protection lors du push capable de bloquer certains secrets avant leur arrivée dans le dépôt. Elle complète les contrôles locaux, sans les remplacer.

## 18. Mode Solo

Le parcours Solo utilise :

- `main` protégée par discipline personnelle ;
- une branche par changement significatif ;
- des commits petits ;
- GitHub comme copie distante des sources ;
- Git LFS uniquement pour les binaires justifiés ;
- une sauvegarde séparée pour les modèles et données locales.

## 19. Mode Studio

Le parcours Studio ajoute :

- branches protégées ;
- pull requests obligatoires ;
- approbations ;
- propriétaires de code ;
- CI obligatoire ;
- règles Git LFS ;
- politique de signature des commits ;
- gestion des accès et révocation ;
- modèles d’issues et de pull requests ;
- sauvegarde du dépôt et des artefacts externes.

## 20. Test de validation

```powershell
$root = Join-Path $HOME "ia-gamedev-git-check"
New-Item -ItemType Directory -Force $root | Out-Null
Set-Location $root

git init
"# Test Git" | Out-File README.md -Encoding utf8
@"
.env
.venv/
models/
"@ | Out-File .gitignore -Encoding utf8

git add README.md .gitignore
git commit -m "test: validate Git installation"
git log --oneline
```

Critères :

- [ ] `git --version` fonctionne.
- [ ] `code --version` fonctionne.
- [ ] L’identité Git est configurée.
- [ ] Le dépôt utilise `main`.
- [ ] `.gitignore` exclut `.env`, `.venv` et les modèles.
- [ ] Le lecteur distingue modification, index et commit.
- [ ] Un commit peut être restauré ou inversé.
- [ ] GitHub est accessible par HTTPS ou SSH.
- [ ] Aucun secret n’est présent dans le dépôt.
- [ ] Les gros binaires ont une politique explicite.

## 21. Sources officielles vérifiées

- [Installation de Git pour Windows](https://git-scm.com/install/windows)
- [Livre Pro Git](https://git-scm.com/book/fr/v2)
- [Documentation Git](https://git-scm.com/docs)
- [Installation de Visual Studio Code sous Windows](https://code.visualstudio.com/docs/setup/windows)
- [Profils Visual Studio Code](https://code.visualstudio.com/docs/configure/profiles)
- [Authentification GitHub](https://docs.github.com/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)
- [Connexion à GitHub avec SSH](https://docs.github.com/authentication/connecting-to-github-with-ssh/about-ssh)
- [GitHub CLI](https://cli.github.com/manual/)
- [Git Large File Storage](https://git-lfs.com/)
- [Protection des secrets lors du push](https://docs.github.com/code-security/concepts/secret-security/push-protection)

## 22. Résumé

Git protège l’historique des sources, GitHub ajoute la collaboration et la CI, et VS Code réunit l’édition, les diffs et le terminal.

Le lecteur doit pouvoir :

- créer un dépôt ;
- sélectionner les fichiers suivis ;
- exclure les secrets et caches ;
- produire un commit lisible ;
- synchroniser avec GitHub ;
- isoler un changement dans une branche ;
- restaurer une erreur sans effacer le travail valide.

Le chapitre suivant prépare Python et les environnements isolés.