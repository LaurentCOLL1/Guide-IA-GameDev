---
title: "Companion Pack — ComfyUI Library"
id: "CP-PACK-06-COMFYUI-LIBRARY"
status: "candidate"
version: "1.0.0"
lang: "fr-FR"
validation-status: "candidate-runtime"
redistribution-status: "pending-global-license"
reference-software:
  comfyui: "v0.28.0"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# ComfyUI Library

Le Pack 6 distribue des workflows visuels reproductibles, leurs manifestes, profils matériels, règles de provenance, scripts de lancement, contrôles et preuves. Il sépare strictement les graphes, les modèles et les résultats.

> **Repères d’utilisation :** **[PS]** PowerShell, **[CMD]** Invite de commandes, **[WSL]** terminal Linux sous Windows, **[DCT]** terminal d’un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à comparer et **[LECTURE]** contenu à étudier.

## 1. État du lot

| Élément | État candidat |
|---|---|
| workflow de validation sans modèle | matérialisé |
| workflow de concept art | modèle non exécuté |
| profils CPU, AMD RDNA2 et qualité | matérialisés |
| manifeste ComfyUI | tag `v0.28.0`, commit à enregistrer pendant la qualification |
| modèles | aucun distribué |
| custom nodes | aucun code distribué |
| scripts Linux et PowerShell | matérialisés |
| provenance et checksums | matérialisés |
| image légère de référence | SVG original |
| qualification ComfyUI | à exécuter en CI |
| licence globale | non décidée |

## 2. Frontières

Le Pack matérialise exactement l’entrée **Pack 6 — ComfyUI Library** du plan maître. Il ne distribue aucun checkpoint, LoRA, VAE, upscaler, custom node tiers, image d’entrée externe, secret ou résultat artistique présenté comme accepté.

Le workflow `WF-COMFY-0001` utilise seulement `LoadImage` et `SaveImage`. Il sert à qualifier le chargement du graphe, l’API locale, la file, la sortie PNG et les métadonnées sans télécharger de modèle.

Le workflow `WF-COMFY-0100` reste au statut `review`. Il expose un patron text-to-image à nœuds natifs, mais exige un modèle fourni et qualifié par l’utilisateur. Aucun résultat, droit, performance ou qualité n’est revendiqué.

## 3. Arborescence

> **[LECTURE] Arbre du Pack — Ne pas saisir.**

```text
ComfyUI-Library/
├── workflows/
│   ├── source/
│   └── api/
├── manifests/
│   ├── workflows/
│   ├── models/
│   └── custom-nodes/
├── presets/
├── scripts/
├── tools/
├── validation/reference/
├── docs/
└── qa/
```

## 4. Profil CPU de validation

> **[PS] PowerShell 7 — Exécuter depuis la racine du dépôt :**

```powershell
$env:COMFYUI_ROOT = "D:\IA\ComfyUI\installations\comfyui-cpu"
& .\Companion-Pack\ComfyUI-Library\scripts\run_cpu.ps1
```

Le script lie explicitement le serveur à `127.0.0.1`. Il ne résout aucun modèle et n’installe aucun custom node.

## 5. Valider le Pack

> **[PS] PowerShell 7 — Exécuter depuis la racine du dépôt :**

```powershell
python .\Companion-Pack\ComfyUI-Library\tools\validate_comfyui_library.py

python -m unittest discover `
  -s .\Companion-Pack\ComfyUI-Library\python\tests `
  -v
```

Le validateur refuse les poids de modèle, archives, secrets, chemins incohérents, dépendances automatiques et claims d’exécution non prouvés.

## 6. Exécuter le workflow minimal

La CI crée une image d’entrée déterministe, démarre ComfyUI en CPU, vérifie la présence exacte des nœuds natifs, soumet le workflow API, attend le succès puis vérifie la sortie PNG.

> **[LECTURE] Chaîne de validation — Ne pas saisir.**

```text
PNG déterministe généré
        ↓
LoadImage
        ↓
SaveImage
        ↓
PNG avec métadonnées prompt + workflow
        ↓
SHA-256 et rapport d’exécution
```

Ce parcours valide l’infrastructure ComfyUI, pas la génération par modèle.

## 7. Profils

- `presets/cpu.yaml` : référence fonctionnelle obligatoire ;
- `presets/amd.yaml` : laboratoire isolé ZLUDA pour la RX 6750 XT, non qualifié ;
- `presets/quality.yaml` : paramètres de départ du workflow de concept, non exécutés.

Aucun profil ne contient de promesse de débit, VRAM, déterminisme bit à bit ou qualité.

## 8. Provenance et modèles

Chaque modèle doit recevoir une source officielle, une révision, une licence, une empreinte SHA-256 et une décision de redistribution avant usage. `MODEL-USER-SD15-001` reste volontairement non résolu.

Une sortie ComfyUI ne devient ni concept retenu ni asset final sans revue humaine, provenance et porte qualité propriétaire.

## 9. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 9.1 Installer automatiquement les custom nodes

**Exemple fautif**

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```text
Importer un workflow reçu puis accepter « installer tous les nœuds manquants ».
```

**Exemple corrigé**

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```text
Lister les classes manquantes, identifier chaque dépôt, lire le code,
épingler un commit, enregistrer la licence, puis installer dans un environnement isolé.
```

**Différence :** le flux corrigé traite les custom nodes comme du code exécutable et conserve une décision vérifiable plutôt qu’une installation implicite.

### 9.2 Versionner un checkpoint dans Git

**Exemple fautif**

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```text
models/checkpoints/model.safetensors
```

**Exemple corrigé**

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```text
manifeste : identifiant, source, révision, licence, taille et SHA-256 ;
fichier réel : stockage externe contrôlé.
```

**Différence :** le dépôt conserve la preuve et le contrat sans redistribuer un poids volumineux ou juridiquement non qualifié.

### 9.3 Présenter le profil AMD comme validé

**Exemple fautif**

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```text
RX 6750 XT : backend ComfyUI AMD officiellement supporté et rapide.
```

**Exemple corrigé**

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```text
RX 6750 XT : profil ZLUDA communautaire isolé, non exécuté dans ce lot ;
profil CPU conservé comme référence fonctionnelle.
```

**Différence :** la formulation corrigée sépare la possibilité expérimentale d’une compatibilité ou performance démontrée.

### 9.4 Confondre workflow exécuté et qualité artistique

**Exemple fautif**

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```text
La file a terminé : le concept est accepté.
```

**Exemple corrigé**

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```text
La file a terminé : la sortie rejoint la quarantaine ;
une personne applique ensuite la revue artistique et juridique.
```

**Différence :** le succès technique devient une entrée de revue, jamais une décision artistique automatique.

### 9.5 Oublier les métadonnées et le JSON source

**Exemple fautif**

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```text
Conserver uniquement une capture JPEG sans workflow.
```

**Exemple corrigé**

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```text
Conserver le JSON source, le manifeste, le PNG interne avec métadonnées
et l’empreinte de chaque fichier significatif.
```

**Différence :** la chaîne corrigée permet l’audit et la reprise même lorsque l’image seule ne conserve plus toutes les informations.

## 10. Réserves

Le candidat ne valide encore aucun modèle réel, aucune génération text-to-image, aucun custom node tiers, aucun profil AMD, aucune performance, aucune qualité artistique, aucun droit d’exploitation de sortie et aucune redistribution autonome.
