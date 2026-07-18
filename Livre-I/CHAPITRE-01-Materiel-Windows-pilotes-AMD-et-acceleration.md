---
title: "Livre I — Chapitre 1 : Matériel, Windows, pilotes AMD et accélération locale"
id: "DOC-L1-CH01"
status: "reviewed"
version: "1.4.0"
lang: "fr-FR"
book: "Livre I"
chapter: 1
last-verified: "2026-07-18"
reference-hardware:
  gpu: "AMD Radeon RX 6750 XT 12 Go"
  cpu: "AMD Ryzen 7 2700"
  ram: "32 Go"
  os: "Windows 11 64 bits"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Matériel, Windows, pilotes AMD et accélération locale

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L1-CH01`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **État technique vérifié le :** 18 juillet 2026  
> **Résultat attendu :** disposer d’un poste Windows stable, documenté et prêt à accueillir Docker, ComfyUI, les LLM locaux et la chaîne audio du guide.

## 1. Objet du chapitre

Ce chapitre prépare le socle matériel et logiciel sur lequel reposera toute la plateforme locale du guide.

Il ne cherche pas à obtenir immédiatement le meilleur score de génération. Il cherche d’abord à obtenir un poste :

- stable ;
- récupérable après une erreur ;
- mesurable ;
- suffisamment documenté pour reproduire une installation ;
- compatible avec la carte graphique AMD Radeon RX 6750 XT de référence ;
- capable de basculer vers le CPU lorsqu’un backend GPU échoue.

La règle principale est la suivante :

> Une accélération expérimentale ne doit jamais devenir l’unique moyen de démarrer, diagnostiquer ou restaurer la plateforme.

## 2. Configuration matérielle de référence

La collection utilise le profil suivant pour ses procédures et ses budgets :

| Composant | Référence du guide |
|---|---|
| GPU | AMD Radeon RX 6750 XT |
| Architecture GPU | RDNA 2 |
| Cible LLVM | `gfx1031` |
| VRAM | 12 Go |
| Unités de calcul | 40 |
| CPU | AMD Ryzen 7 2700, 8 cœurs / 16 threads |
| RAM | 32 Go |
| Système principal | Windows 11 64 bits |
| Stockage conseillé | SSD, avec espace séparé pour les modèles et caches |
| Réseau | connexion requise pour les installations et mises à jour |

Les caractéristiques GPU ci-dessus correspondent à la nomenclature AMD actuelle. Elles servent à identifier correctement la carte et à éviter d’appliquer des instructions destinées à une autre famille RDNA.

## 3. Ce que permet réellement la RX 6750 XT en 2026

### 3.1 Atouts

La RX 6750 XT dispose de 12 Go de VRAM, ce qui permet notamment :

- d’exécuter des workflows d’image locaux avec des compromis raisonnables ;
- de charger certains modèles de langage quantifiés sur le GPU ou en mode hybride ;
- de réaliser des traitements audio accélérés lorsque le logiciel fournit un backend compatible ;
- de travailler confortablement dans Blender et Godot ;
- de conserver une marge supérieure aux cartes 8 Go pour les textures, modèles et caches.

### 3.2 Limites structurantes

La carte appartient à la famille RDNA 2 et utilise la cible `gfx1031`. Cette distinction est importante : les matrices de compatibilité AMD ne traitent pas tous les GPU RDNA 2 de la même manière.

Au 18 juillet 2026 :

- le runtime HIP Windows est indiqué comme disponible pour la RX 6750 XT ;
- le HIP SDK Windows complet n’est pas officiellement pris en charge pour cette carte ;
- la matrice officielle PyTorch sur Windows ne liste pas la RX 6750 XT parmi les GPU pris en charge ;
- il ne faut donc pas présenter ROCm/PyTorch Windows comme la voie officielle principale de ce guide pour ce matériel.

Cette situation ne signifie pas que toute charge de calcul HIP est impossible. Elle signifie que le guide doit distinguer strictement :

1. ce qui est officiellement validé par AMD ;
2. ce qui fonctionne grâce à un runtime partiel ;
3. ce qui dépend d’un projet communautaire ;
4. ce qui n’a été testé que sur une configuration précise.

## 4. Stratégie d’accélération du guide

Le guide classe les voies d’exécution dans l’ordre suivant.

### 4.1 Voie A — Windows ML, ONNX Runtime et DirectML

**Statut : recommandé lorsque l’application ou le modèle le permet.**

DirectML fonctionne sur le matériel compatible DirectX 12. Microsoft maintient DirectML, mais oriente désormais les nouveaux déploiements ONNX Runtime sous Windows vers Windows ML, qui sélectionne dynamiquement le fournisseur d’exécution adapté au matériel.

Cette voie est privilégiée pour :

- les modèles disponibles au format ONNX ;
- l’inférence intégrée à une application Windows ;
- les outils explicitement compatibles DirectML ou Windows ML ;
- les scénarios où la portabilité entre AMD, Intel et NVIDIA est prioritaire.

Limites :

- tous les projets Python ou PyTorch ne prennent pas en charge DirectML ;
- certaines extensions CUDA n’ont pas d’équivalent ;
- les performances varient fortement selon les opérateurs et le modèle ;
- DirectML est en ingénierie soutenue, et non dans une phase d’expansion fonctionnelle rapide.

### 4.2 Voie B — Backend natif spécifique à l’application

**Statut : recommandé lorsqu’il est maintenu par le projet utilisé.**

Certains logiciels proposent leur propre backend AMD, Vulkan, DirectX 12, HIP ou ONNX. Cette voie doit être choisie avant d’ajouter une couche de compatibilité externe.

Ordre de décision :

1. backend officiellement documenté par l’application ;
2. version explicitement compatible avec la carte et le pilote ;
3. test minimal reproductible ;
4. mesure de la VRAM et du temps d’exécution ;
5. seulement ensuite, optimisation avancée.

### 4.3 Voie C — ZLUDA

**Statut : optionnel et expérimental.**

ZLUDA est un projet indépendant qui cherche à exécuter des applications CUDA non modifiées sur des GPU non NVIDIA. Le dépôt amont publiait la version 6 le 29 juin 2026.

Dans ce guide, ZLUDA n’est jamais traité comme :

- une fonctionnalité officielle AMD ;
- une fonctionnalité officielle Microsoft ;
- une garantie de compatibilité CUDA complète ;
- une solution universelle pour tous les nœuds ComfyUI ;
- un remplacement transparent et permanent d’un environnement NVIDIA.

ZLUDA doit être installé dans un environnement isolé, avec :

- une version épinglée ;
- une archive ou un hash conservé ;
- un environnement Python dédié ;
- un workflow de test minimal ;
- une procédure de retour au mode CPU ;
- des journaux distincts de ceux de l’installation stable.

La procédure détaillée sera traitée dans le chapitre ComfyUI. Le présent chapitre ne valide que la stratégie générale.

### 4.4 Voie D — CPU

**Statut : obligatoire comme solution de diagnostic et de secours.**

Le Ryzen 7 2700 ne fournit pas les performances d’un GPU moderne pour l’inférence lourde, mais le CPU reste indispensable pour :

- vérifier qu’un modèle ou un workflow est fonctionnel ;
- distinguer une erreur générale d’une erreur de backend GPU ;
- convertir des modèles ;
- exécuter de petites tâches ;
- restaurer une plateforme lorsque le pilote GPU est instable.

Le chemin CPU doit rester documenté même lorsque le GPU fonctionne.

## 5. Matrice de décision pour la RX 6750 XT

| Besoin | Voie prioritaire | Repli | Statut |
|---|---|---|---|
| Application ONNX sous Windows | Windows ML / ONNX Runtime | DirectML explicite, puis CPU | Recommandé |
| Outil avec backend AMD/Vulkan natif | Backend officiel de l’outil | CPU | Recommandé |
| PyTorch Windows générique | Backend documenté par le projet | `torch-directml`, puis CPU | À tester par projet |
| Application uniquement CUDA | ZLUDA isolé | CPU ou remplacement de l’outil | Expérimental |
| PyTorch ROCm Windows sur RX 6750 XT | Ne pas en faire le parcours principal | DirectML, ZLUDA ou CPU | Non officiellement pris en charge |
| Diagnostic d’un workflow | CPU minimal | aucun | Obligatoire |

## 6. Préparer le matériel physique

### 6.1 Vérifications avant toute installation

Éteindre le poste puis vérifier :

- que la carte graphique est correctement insérée ;
- que tous les connecteurs d’alimentation PCIe requis sont branchés ;
- que l’alimentation est adaptée à l’ensemble de la configuration ;
- que les ventilateurs et entrées d’air ne sont pas obstrués ;
- que le moniteur principal est branché sur la carte graphique et non sur une sortie de carte mère inutilisable ;
- que le SSD dispose d’une marge suffisante ;
- que la mémoire vive est détectée intégralement.

### 6.2 Refroidissement

Les charges IA peuvent maintenir le GPU à forte utilisation plus longtemps qu’un usage bureautique. Une température stable compte davantage qu’un benchmark très court.

Avant de conclure à un défaut logiciel, vérifier :

- la température GPU ;
- la température du point chaud lorsqu’elle est exposée ;
- la vitesse des ventilateurs ;
- l’absence de chute brutale de fréquence ;
- la stabilité après plusieurs minutes de charge.

Le guide ne recommande pas l’overclocking pour le parcours principal. Toute modification de fréquence ou de tension doit être annulée pendant le diagnostic.

### 6.3 Stockage

Séparer logiquement les catégories suivantes :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
C:\IA-GameDev\
├── apps\
├── models\
├── datasets\
├── caches\
├── workspaces\
├── logs\
└── backups\
```

Cette organisation limite les chemins trop longs, simplifie les sauvegardes et évite de remplir le disque système avec des caches de modèles difficiles à identifier.

## 7. Préparer Windows

### 7.1 Système recommandé

Le parcours principal utilise Windows 11 64 bits, maintenu à jour. Les documentations AMD récentes pour HIP SDK Windows et PyTorch ROCm Windows ciblent Windows 11.

Windows 10 peut rester utilisable pour certains outils DirectML, mais il ne constitue plus la cible principale de la collection.

### 7.2 Informations à relever

Ouvrir PowerShell et exécuter :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Get-ComputerInfo |
    Select-Object WindowsProductName, WindowsVersion, OsBuildNumber,
                  CsSystemType, CsTotalPhysicalMemory
```

Lister le processeur et les cartes graphiques détectées :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Get-CimInstance Win32_Processor |
    Select-Object Name, NumberOfCores, NumberOfLogicalProcessors

Get-CimInstance Win32_VideoController |
    Select-Object Name, DriverVersion, AdapterRAM, VideoProcessor
```

Créer un rapport DirectX :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
New-Item -ItemType Directory -Force -Path C:\IA-GameDev\logs | Out-Null
dxdiag /t C:\IA-GameDev\logs\dxdiag.txt
```

Afficher la version de Windows avec l’interface graphique :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
winver
```

### 7.3 Mises à jour système

Avant d’installer les outils IA :

1. installer les mises à jour de sécurité Windows ;
2. redémarrer ;
3. vérifier à nouveau Windows Update ;
4. créer un point de restauration lorsque la protection du système est disponible ;
5. sauvegarder les documents importants ;
6. noter le numéro de build Windows.

Ne pas installer simultanément un pilote GPU, une mise à jour majeure de Windows et plusieurs runtimes Python. Modifier une couche à la fois facilite le diagnostic.

## 8. Installer le pilote AMD

### 8.1 Source obligatoire

Télécharger le pilote depuis la page officielle de la RX 6750 XT ou utiliser l’outil officiel de détection AMD.

Au moment de la vérification de ce chapitre, la page AMD proposait un outil actualisé le 29 juin 2026. Cette date est informative : le lecteur doit toujours relever la version réellement proposée le jour de son installation.

### 8.2 Informations à enregistrer

Avant l’installation :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Date :
Version Windows :
Build Windows :
Version actuelle du pilote :
Version cible du pilote :
Source du paquet : AMD officiel
Type d’installation : mise à niveau / réinstallation
```

Après l’installation, conserver :

- le numéro de version Adrenalin ;
- la version du pilote affichée par Windows ;
- la date d’installation ;
- le nom du fichier téléchargé ;
- le hash du fichier lorsque l’environnement doit être reproductible ;
- une copie du rapport `dxdiag.txt`.

### 8.3 Installation normale

La procédure par défaut est :

1. fermer les logiciels 3D et IA ;
2. lancer l’installeur officiel AMD ;
3. conserver une installation standard ;
4. redémarrer lorsque demandé ;
5. vérifier le Gestionnaire de périphériques ;
6. générer un nouveau rapport DirectX ;
7. effectuer le test minimal du chapitre.

### 8.4 Nettoyage avancé

Une désinstallation complète ou un utilitaire de nettoyage n’est pas une première étape. Cette opération n’est justifiée qu’en présence de symptômes tels que :

- installation impossible ;
- périphérique désactivé ;
- version de pilote incohérente ;
- écran noir récurrent après mise à jour ;
- crash reproduit après retour aux paramètres par défaut.

Avant un nettoyage avancé :

- créer une sauvegarde ;
- télécharger à l’avance le pilote de remplacement ;
- connaître le mode sans échec ;
- conserver un moyen d’accès à Internet depuis un autre appareil ;
- documenter la version supprimée.

## 9. Vérifier DirectX 12 et le pilote

### 9.1 Contrôle graphique

Dans `dxdiag.txt`, vérifier :

- le nom de la carte ;
- la version du pilote ;
- l’absence de problème signalé ;
- les niveaux de fonctionnalités Direct3D exposés ;
- la version WDDM.

### 9.2 Contrôle PowerShell

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
$gpu = Get-CimInstance Win32_VideoController |
    Where-Object Name -Match "Radeon RX 6750 XT"

if (-not $gpu) {
    throw "RX 6750 XT non détectée par Windows."
}

$gpu | Format-List Name, DriverVersion, AdapterRAM, VideoProcessor
```

Ce test confirme la détection par Windows. Il ne prouve pas encore qu’un backend IA particulier fonctionne.

## 10. Installer les prérequis généraux

Les chapitres suivants préciseront leurs propres versions. Le socle commun comprend généralement :

- Git ;
- Python dans des environnements isolés ;
- Visual C++ Redistributable lorsque requis ;
- Windows Terminal ;
- PowerShell récent ;
- 7-Zip ou un outil d’archive équivalent ;
- Docker Desktop dans le chapitre suivant.

Vérifier `winget` :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
winget --version
```

Vérifier Git après installation :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git --version
```

Vérifier Python sans supposer qu’une seule version globale sera utilisée :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
py --list
```

Le guide privilégie un environnement virtuel par application. Il déconseille d’installer toutes les bibliothèques IA dans le Python système.

## 11. Budgets pour 12 Go de VRAM

Les valeurs suivantes sont des budgets de planification, pas des garanties universelles.

| Usage | Règle de départ |
|---|---|
| Bureau, affichage et services GPU | conserver une marge avant de charger un modèle |
| ComfyUI | commencer avec un seul workflow et une résolution modérée |
| LLM | privilégier les quantifications adaptées et surveiller l’offload |
| Blender | fermer les charges IA inutiles pendant les rendus lourds |
| Exécution simultanée | éviter de charger plusieurs gros modèles sans mesure |
| Diagnostic | réduire la résolution, la taille de lot et le nombre de modèles |

La mesure réelle doit utiliser les outils fournis par l’application, les journaux et les compteurs Windows. Une erreur de mémoire peut provenir :

- de la VRAM réellement saturée ;
- d’une fragmentation ;
- d’un nœud conservant des tenseurs ;
- d’un modèle dupliqué en mémoire ;
- d’une incompatibilité de backend ;
- d’un dépassement de RAM système suivi d’une pagination excessive.

## 12. Test minimal de stabilité

### 12.1 Objectif

Avant Docker, ComfyUI ou les LLM, le poste doit réussir un test de base :

- Windows démarre normalement ;
- la RX 6750 XT est détectée ;
- le pilote ne signale pas d’erreur ;
- un logiciel 3D simple peut utiliser la carte ;
- plusieurs redémarrages successifs ne provoquent pas de panne ;
- le disque dispose d’un espace libre suffisant ;
- les rapports système sont archivés.

### 12.2 Dossier de preuve

Créer :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
C:\IA-GameDev\logs\platform-baseline\
```

Y conserver :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
windows-info.txt
dxdiag.txt
gpu-driver.txt
disk-space.txt
validation-notes.md
```

Exemple de collecte :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
$dest = "C:\IA-GameDev\logs\platform-baseline"
New-Item -ItemType Directory -Force -Path $dest | Out-Null

Get-ComputerInfo |
    Out-File "$dest\windows-info.txt" -Encoding utf8

Get-CimInstance Win32_VideoController |
    Format-List * |
    Out-File "$dest\gpu-driver.txt" -Encoding utf8

Get-PSDrive -PSProvider FileSystem |
    Format-Table Name, Used, Free, Root -AutoSize |
    Out-File "$dest\disk-space.txt" -Encoding utf8

dxdiag /t "$dest\dxdiag.txt"
```

## 13. Procédure de diagnostic en couches

Lorsqu’un outil IA échoue, suivre cet ordre.

### Couche 1 — Matériel et Windows

- la carte est-elle détectée ?
- le pilote est-il chargé ?
- le système est-il stable ?
- l’espace disque est-il suffisant ?

### Couche 2 — Application sans accélération

- l’application démarre-t-elle en mode CPU ?
- le modèle se charge-t-il avec une configuration minimale ?
- les fichiers sont-ils intacts ?

### Couche 3 — Backend officiel

- le backend est-il documenté par la version installée ?
- la carte figure-t-elle dans la matrice de support ?
- les versions Python et bibliothèque sont-elles compatibles ?

### Couche 4 — Couche expérimentale

- la version ZLUDA est-elle épinglée ?
- les DLL ou bibliothèques correspondent-elles au guide utilisé ?
- un test minimal fonctionne-t-il ?
- l’échec disparaît-il en revenant au CPU ?

### Couche 5 — Optimisation

N’optimiser qu’après avoir obtenu une exécution correcte et reproductible.

## 14. Politique ZLUDA du projet

Toute procédure ZLUDA doit fournir les éléments suivants :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
backend: zluda
status: experimental
zluda_version: "version exacte"
zluda_source: "dépôt amont ou distribution documentée"
application: "nom et version"
python: "version exacte"
torch: "version exacte"
windows_build: "numéro"
amd_driver: "version"
gpu: "Radeon RX 6750 XT"
result: "success | partial | failed"
fallback: "cpu | directml | autre"
```

Une procédure ZLUDA ne peut être marquée « recommandée » que si :

- elle est reproductible sur la configuration de référence ;
- les fichiers installés sont traçables ;
- le chemin de désinstallation est connu ;
- le mode CPU reste disponible ;
- au moins un workflow réel du guide est validé ;
- les limites sont décrites.

## 15. Parcours Mode Solo

Le parcours Solo privilégie :

- une seule installation stable de pilote ;
- des environnements Python séparés mais peu nombreux ;
- un seul backend principal par application ;
- des scripts de collecte automatiques ;
- des sauvegardes locales simples ;
- ZLUDA uniquement dans un dossier expérimental distinct.

Arborescence conseillée :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
C:\IA-GameDev\
├── stable\
├── experimental\
├── models\
├── logs\
└── backups\
```

## 16. Parcours Mode Studio

Le parcours Studio ajoute :

- un registre matériel par poste ;
- une version de pilote approuvée ;
- une fenêtre de mise à jour ;
- un poste pilote avant déploiement général ;
- des fichiers de configuration versionnés ;
- une matrice de compatibilité par application ;
- un rapport d’incident commun ;
- l’interdiction d’imposer ZLUDA sans solution de repli documentée.

Exemple de registre :

| Poste | GPU | Windows | Pilote | Backend validé | Date |
|---|---|---|---|---|---|
| `DEV-01` | RX 6750 XT | Windows 11 | à renseigner | DirectML / CPU | à renseigner |

## 17. Critères de validation du chapitre

Le chapitre est validé pour un poste lorsque :

- [ ] Windows 11 64 bits est à jour ;
- [ ] la RX 6750 XT est détectée sans erreur ;
- [ ] le pilote provient d’AMD ;
- [ ] la version du pilote est enregistrée ;
- [ ] `dxdiag.txt` est archivé ;
- [ ] les informations CPU, RAM et disque sont enregistrées ;
- [ ] un point de restauration ou une sauvegarde existe ;
- [ ] les dossiers de travail sont créés ;
- [ ] le chemin CPU de secours est accepté comme exigence ;
- [ ] ROCm/PyTorch Windows n’est pas présenté comme officiellement pris en charge sur cette carte ;
- [ ] toute expérimentation ZLUDA est séparée de l’installation stable ;
- [ ] le poste peut passer au chapitre Docker.

## 18. Résultat attendu

À la fin de ce chapitre, le lecteur dispose :

- d’un inventaire matériel ;
- d’un Windows documenté ;
- d’un pilote AMD officiel installé ;
- d’un rapport DirectX ;
- d’une arborescence de travail ;
- d’une stratégie claire pour DirectML, Windows ML, ZLUDA et le CPU ;
- d’un dossier de preuves permettant de diagnostiquer les prochains chapitres.

## 19. Sources officielles et primaires

État vérifié le 18 juillet 2026.

- [AMD — Pilotes et téléchargements Radeon RX 6750 XT](https://www.amd.com/fr/support/downloads/drivers.html/graphics/radeon-rx/radeon-rx-6000-series/amd-radeon-rx-6750-xt.html)
- [AMD ROCm — Caractéristiques matérielles des GPU](https://rocm.docs.amd.com/en/latest/reference/gpu-arch-specs.html)
- [AMD ROCm — Configuration requise HIP SDK pour Windows](https://rocm.docs.amd.com/projects/install-on-windows/en/develop/reference/system-requirements.html)
- [AMD ROCm — Matrice de compatibilité Radeon sous Windows](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/compatibility/compatibilityrad/windows/windows_compatibility.html)
- [Microsoft — Windows AI](https://learn.microsoft.com/en-us/windows/ai/)
- [Microsoft — DirectML](https://learn.microsoft.com/fr-fr/windows/ai/directml/dml)
- [Microsoft — Démarrer avec DirectML](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)
- [Microsoft — PyTorch avec DirectML sous Windows](https://learn.microsoft.com/en-us/windows/ai/directml/pytorch-windows)
- [ZLUDA — dépôt amont](https://github.com/vosen/ZLUDA)

## 20. Prochaine étape

Le prochain chapitre installe et valide Docker Desktop ainsi que Docker Compose, sans supposer que les conteneurs auront un accès direct au GPU AMD pour toutes les charges IA.
