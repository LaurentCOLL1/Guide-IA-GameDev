---
title: "Companion Pack — ComfyUI Library"
id: "CP-PACK-06-COMFYUI-LIBRARY"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-07-30T11:20:49+02:00"
validation-status: "runtime-tested-linux"
redistribution-status: "pending-global-license"
reference-software:
  comfyui: "v0.28.0"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# ComfyUI Library

Le Pack 6 distribue des workflows visuels reproductibles, leurs manifestes, profils matériels, règles de provenance, scripts de lancement, contrôles et preuves. Il sépare strictement les graphes, les modèles et les résultats.

> **Repères d’utilisation :** **[PS]** PowerShell, **[CMD]** Invite de commandes, **[WSL]** terminal Linux sous Windows, **[DCT]** terminal d’un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à comparer et **[LECTURE]** contenu à étudier.

## 1. État du lot

| Élément | État qualifié |
|---|---|
| workflow de validation sans modèle | exécuté sur CPU par le run `30529642016` |
| workflow de concept art | modèle non exécuté |
| profils CPU, AMD RDNA2 et qualité | matérialisés |
| manifeste ComfyUI | tag `v0.28.0`, commit `700821e1364eaab0e8f21c538a2131719fec57bf` |
| modèles | aucun distribué |
| custom nodes | aucun code distribué |
| scripts Linux et PowerShell | matérialisés |
| provenance et checksums | matérialisés |
| image légère de référence | SVG original |
| qualification ComfyUI | validée sur Linux x86_64 par le run `30529642016` |
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

## 10. Qualification obtenue

Le run `30529642016` a validé 37 fichiers du Pack et 12 tests Python, puis a cloné ComfyUI `v0.28.0` au commit `700821e1364eaab0e8f21c538a2131719fec57bf`. L’environnement utilisait CPython `3.12.13` et Torch `2.13.0+cu130` sur Ubuntu 24.04.

Le workflow `WF-COMFY-0001` a réellement exécuté `LoadImage → SaveImage` sans modèle ni custom node tiers. La sortie PNG contient les métadonnées `prompt` et `workflow`, mesure `1565` octets et possède l’empreinte `868bc37be44cf32ae8cac9e55106bd2d16dc9161f6bea4e391e9c146e7603388`.

Artefact `8754176422`, digest `sha256:19be52a44ab295a747cb4ed7655268058d27494572e83709455004bf5be145af`. L’arbre Git est resté propre et aucun PDF n’a été produit.

## 11. Réserves

La qualification ne valide aucun modèle réel, aucune génération text-to-image, aucun custom node tiers, aucun profil AMD, aucune performance, aucune qualité artistique, aucun droit d’exploitation de sortie et aucune redistribution autonome.
