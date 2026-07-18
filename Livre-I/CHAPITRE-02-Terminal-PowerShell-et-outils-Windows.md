---
title: "Livre I — Chapitre 2 : Terminal, PowerShell et outils Windows"
id: "DOC-L1-ENV-TERMINAL"
status: "draft-review"
version: "1.2.0"
lang: "fr-FR"
book: "Livre I"
chapter: 2
last-verified: "2026-07-18"
reference-platform:
  os: "Windows 11 64 bits"
  shell: "PowerShell 7"
  terminal: "Windows Terminal"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Terminal, PowerShell et outils Windows

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L1-ENV-TERMINAL`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Résultat attendu :** savoir exécuter, comprendre, journaliser et annuler les commandes utilisées dans les chapitres suivants sans travailler systématiquement en administrateur.

## 1. Pourquoi ce chapitre existe

Le terminal est l’interface commune de Docker, Git, Python, ComfyUI, des LLM locaux, des outils audio et des scripts du Companion Pack.

Le guide ne suppose pas que le lecteur connaît déjà :

- la différence entre un terminal et un interpréteur de commandes ;
- la notion de dossier courant ;
- les chemins absolus et relatifs ;
- les variables d’environnement ;
- les droits administrateur ;
- les redirections et pipelines ;
- les codes de sortie ;
- les journaux d’exécution.

La règle principale est :

> Une commande ne doit pas être copiée aveuglément. Il faut identifier son programme, ses arguments, les fichiers qu’elle modifie et la méthode de retour arrière.

## 2. Terminal, console et shell

### 2.1 Windows Terminal

Windows Terminal est l’application qui affiche les onglets, panneaux et sessions. Il peut héberger plusieurs shells :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Windows Terminal
├── PowerShell 7              pwsh.exe
├── Windows PowerShell 5.1    powershell.exe
├── Invite de commandes       cmd.exe
└── distributions WSL         bash, zsh ou autre
```

### 2.2 PowerShell 7

PowerShell 7 est le shell principal du guide. Il est distinct de Windows PowerShell 5.1, encore présent pour la compatibilité avec certains composants historiques.

Vérifier la session :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
$PSVersionTable
$PSHOME
Get-Process -Id $PID | Select-Object Path
```

Une commande destinée à PowerShell n’est pas nécessairement valide dans `cmd.exe` ou Bash.

### 2.3 Syntaxe utilisée dans le guide

Les blocs sont identifiés explicitement :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Write-Output "Commande PowerShell"
```

> **[WSL] Terminal WSL/Bash - Exécuter :** utiliser la distribution Linux indiquée.

```bash
printf '%s\n' "Commande Bash ou WSL"
```

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Sortie attendue ou pseudo-arborescence
```

## 3. Installer les outils de base

### 3.1 Vérifier WinGet

WinGet est inclus dans Windows 11 via App Installer.

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
winget --version
winget source list
```

Si la commande est absente, mettre à jour **App Installer** depuis la source Microsoft officielle avant d’ajouter un gestionnaire de paquets tiers.

### 3.2 Installer Windows Terminal et PowerShell

Rechercher les paquets exacts :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
winget search --id Microsoft.WindowsTerminal --exact
winget search --id Microsoft.PowerShell --exact
```

Installer :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
winget install --id Microsoft.WindowsTerminal --exact --source winget
winget install --id Microsoft.PowerShell --exact --source winget
```

Fermer puis rouvrir le terminal, puis vérifier :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
wt --version
pwsh --version
```

Les versions Preview ne sont pas utilisées dans le parcours stable.

### 3.3 Installer les utilitaires communs

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
winget install --id 7zip.7zip --exact --source winget
winget install --id Microsoft.Sysinternals --exact --source winget
```

Chaque installation doit être précédée d’un `winget show --id ... --exact` afin de vérifier l’éditeur, la source et la version sélectionnée.

## 4. Travailler sans administrateur par défaut

Une session élevée modifie davantage de fichiers et masque parfois un problème de permissions.

Le parcours normal utilise une session utilisateur. L’élévation est réservée aux opérations qui l’exigent réellement :

- activation d’une fonctionnalité Windows ;
- installation système ;
- modification protégée du pare-feu ;
- maintenance d’un service ;
- réparation système documentée.

Vérifier si la session est élevée :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(
    [Security.Principal.WindowsBuiltInRole]::Administrator
)
$isAdmin
```

Ne pas désactiver UAC pour simplifier une procédure.

## 5. Comprendre les chemins

### 5.1 Dossier courant

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Get-Location
Set-Location C:\IA-GameDev
Get-ChildItem
```

Alias courants à reconnaître, sans les imposer dans les scripts documentés :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
pwd  → Get-Location
cd   → Set-Location
ls   → Get-ChildItem
cat  → Get-Content
```

Les scripts du guide utilisent de préférence les noms complets des commandes PowerShell.

### 5.2 Chemins absolus et relatifs

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
# Absolu
C:\IA-GameDev\models\modele.gguf

# Relatif au dossier courant
.\models\modele.gguf

# Dossier parent
..\archives
```

Toujours entourer un chemin contenant des espaces de guillemets :

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell # Absolu C:\IA-GameDev\models\modele.gguf # Relatif au dossier courant .\models\modele.gguf # Dossier parent ..\archives`.

```powershell
Set-Location "C:\IA GameDev\Mon Projet"
```

### 5.3 Chemins utilisateur portables

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell Set-Location "C:\IA GameDev\Mon Projet"`.

```powershell
$HOME
$env:USERPROFILE
$env:LOCALAPPDATA
$env:APPDATA
$env:TEMP
```

Préférer ces variables aux chemins contenant un nom d’utilisateur codé en dur.

## 6. Créer et manipuler des fichiers

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
New-Item -ItemType Directory -Force C:\IA-GameDev\workspaces
New-Item -ItemType File .\validation-notes.md
Copy-Item .\source.txt .\backup\source.txt
Move-Item .\ancien.txt .\nouveau.txt
Remove-Item .\fichier-temporaire.txt
```

Avant une suppression récursive :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Get-ChildItem .\dossier -Recurse
Remove-Item .\dossier -Recurse -WhatIf
```

Retirer `-WhatIf` uniquement après vérification.

Les commandes suivantes sont considérées comme destructives :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Remove-Item -Recurse -Force
docker compose down --volumes
git clean -fdx
```

Elles doivent être précédées d’un inventaire et d’une sauvegarde adaptée.

## 7. Variables d’environnement

### 7.1 Lire une variable

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
$env:PATH
$env:TEMP
```

### 7.2 Variable temporaire de session

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
$env:MON_MODELE = "C:\IA-GameDev\models\exemple.gguf"
```

Elle disparaît à la fermeture de la session.

### 7.3 Variable persistante utilisateur

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell $env:MON_MODELE = "C:\IA-GameDev\models\exemple.gguf"`.

```powershell
[Environment]::SetEnvironmentVariable(
    "IA_GAMEDEV_HOME",
    "C:\IA-GameDev",
    "User"
)
```

Ouvrir une nouvelle session avant de tester.

Ne jamais stocker durablement une clé privée dans une variable inscrite dans un script versionné.

## 8. Exécution des scripts

### 8.1 Identifier la politique active

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Get-ExecutionPolicy -List
```

Le guide n’impose pas `Unrestricted` et ne désactive pas globalement les protections.

Pour un script local contrôlé, préférer une portée limitée et documentée :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Dans une organisation, la stratégie de groupe prime et ne doit pas être contournée.

### 8.2 Inspecter avant d’exécuter

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Get-Content .\script.ps1
Get-FileHash .\script.ps1 -Algorithm SHA256
```

Pour un script téléchargé :

1. vérifier la source ;
2. lire son contenu ;
3. relever son hash ;
4. exécuter dans un dossier de test ;
5. vérifier les fichiers et processus créés.

Éviter les pipelines directs du type « téléchargement puis exécution » lorsque le script peut être téléchargé et inspecté séparément.

## 9. Redirections, pipelines et journaux

### 9.1 Pipeline d’objets

PowerShell transmet des objets, pas seulement du texte :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Get-Process |
    Sort-Object CPU -Descending |
    Select-Object -First 10 Name, CPU, WorkingSet
```

### 9.2 Enregistrer une sortie

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Get-ComputerInfo | Out-File .\windows-info.txt -Encoding utf8
```

Sortie standard et erreurs :

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell Get-ComputerInfo | Out-File .\windows-info.txt -Encoding utf8`.

```powershell
& .\outil.exe --version *> .\outil-version.log
```

Afficher et enregistrer simultanément :

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell & .\outil.exe --version *> .\outil-version.log`.

```powershell
& .\outil.exe --check 2>&1 | Tee-Object .\validation.log
```

### 9.3 Code de sortie

Après un programme natif :

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell & .\outil.exe --check 2>&1 | Tee-Object .\validation.log`.

```powershell
& git --version
$LASTEXITCODE
```

Dans un script :

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell & .\outil.exe --check 2>&1 | Tee-Object .\validation.log`.

```powershell
if ($LASTEXITCODE -ne 0) {
    throw "La commande a échoué avec le code $LASTEXITCODE."
}
```

## 10. Archives et empreintes

### 10.1 Créer une archive

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Compress-Archive -Path .\config\* -DestinationPath .\backups\config.zip
```

Pour les formats non pris en charge ou les archives volumineuses, utiliser 7-Zip :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
7z a .\backups\projet.7z .\projet\
```

### 10.2 Calculer une empreinte

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell 7z a .\backups\projet.7z .\projet\`.

```powershell
Get-FileHash .\archive.zip -Algorithm SHA256
```

Enregistrer le résultat :

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell Get-FileHash .\archive.zip -Algorithm SHA256`.

```powershell
Get-FileHash .\archive.zip -Algorithm SHA256 |
    Format-List |
    Out-File .\archive.zip.sha256.txt -Encoding utf8
```

Une empreinte confirme l’intégrité d’un fichier connu. Elle ne prouve pas à elle seule que sa source est digne de confiance.

## 11. UTF-8, fins de ligne et encodage

Le dépôt utilise UTF-8.

Créer un fichier explicitement :

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell Get-FileHash .\archive.zip -Algorithm SHA256 | Format-List | Out-File .\archive.zip.sha256.txt -Encoding utf8`.

```powershell
"Texte en français" | Out-File .\exemple.txt -Encoding utf8
```

Vérifier les caractères accentués après une conversion ou une génération automatique.

Les scripts ne doivent pas dépendre d’un encodage implicite différent entre Windows PowerShell 5.1, PowerShell 7, Python et Git.

## 12. Séparer Windows et WSL

Une commande lancée dans WSL agit dans un environnement Linux, avec ses propres :

- chemins ;
- permissions ;
- exécutables ;
- environnements Python ;
- clés SSH ;
- fichiers de configuration.

Correspondance typique :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Windows : C:\IA-GameDev\projet
WSL     : /mnt/c/IA-GameDev/projet
```

Pour les projets Linux à forte activité disque, préférer le système de fichiers de la distribution WSL. Pour les applications natives Windows, conserver les fichiers attendus sur un volume Windows.

Ne pas mélanger silencieusement les exécutables `python`, `git` ou `docker` de Windows et de WSL dans une même procédure.

## 13. Profil PowerShell

Afficher le chemin du profil :

> **[VSC] Visual Studio Code - Créer ou modifier :** `text Windows : C:\IA-GameDev\projet WSL     : /mnt/c/IA-GameDev/projet`.

```powershell
$PROFILE
```

Créer le fichier :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
New-Item -ItemType File -Force $PROFILE
```

Le profil doit rester léger. Ne pas y placer :

- de secret ;
- de commande réseau automatique ;
- d’activation forcée d’un environnement Python ;
- de changement permanent de dossier ;
- de script non versionné indispensable au projet.

## 14. Mode Solo

Le parcours Solo conserve :

- un profil Windows Terminal principal ;
- PowerShell 7 stable ;
- une arborescence `C:\IA-GameDev` ;
- des scripts courts, lisibles et versionnés ;
- un dossier de journaux ;
- une archive avant toute modification risquée.

## 15. Mode Studio

Le parcours Studio ajoute :

- des scripts signés lorsque la politique l’exige ;
- une liste de versions approuvées ;
- des commandes reproductibles dans la CI ;
- des journaux horodatés ;
- des droits minimaux par rôle ;
- une procédure de revue avant exécution des scripts d’administration.

## 16. Test de validation

Créer un dossier de test :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
$root = Join-Path $HOME "ia-gamedev-terminal-check"
New-Item -ItemType Directory -Force $root | Out-Null
Set-Location $root
```

Exécuter :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
$report = [ordered]@{
    Date = Get-Date -Format "o"
    PowerShell = $PSVersionTable.PSVersion.ToString()
    Dossier = (Get-Location).Path
    Winget = (winget --version)
}

$report | ConvertTo-Json |
    Out-File .\terminal-check.json -Encoding utf8

Get-FileHash .\terminal-check.json -Algorithm SHA256 |
    Out-File .\terminal-check.sha256.txt -Encoding utf8
```

Critères :

- [ ] Windows Terminal démarre.
- [ ] `pwsh --version` fonctionne.
- [ ] `winget --version` fonctionne.
- [ ] Le lecteur sait identifier son dossier courant.
- [ ] Un chemin avec espaces est correctement cité.
- [ ] Un fichier UTF-8 est créé et relu.
- [ ] Une sortie et une erreur peuvent être journalisées.
- [ ] Une empreinte SHA-256 est calculée.
- [ ] Une suppression risquée est testée avec `-WhatIf`.
- [ ] Le lecteur distingue PowerShell, `cmd.exe` et WSL.

## 17. Sources officielles vérifiées

- [Installation de Windows Terminal](https://learn.microsoft.com/windows/terminal/install)
- [Installation de PowerShell sous Windows](https://learn.microsoft.com/powershell/scripting/install/install-powershell-on-windows)
- [Documentation WinGet](https://learn.microsoft.com/windows/package-manager/winget/)
- [Commande `winget install`](https://learn.microsoft.com/windows/package-manager/winget/install)
- [Documentation PowerShell](https://learn.microsoft.com/powershell/)
- [À propos des politiques d’exécution](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_execution_policies)

## 18. Résumé

Le terminal n’est pas une étape accessoire. Il constitue l’interface opérationnelle de toute la plateforme.

Avant de poursuivre, le lecteur doit savoir :

- où une commande s’exécute ;
- avec quels droits ;
- quels fichiers elle modifie ;
- comment enregistrer sa sortie ;
- comment vérifier son résultat ;
- comment revenir à l’état précédent.

Le chapitre suivant installe Git, configure GitHub et prépare VS Code.
