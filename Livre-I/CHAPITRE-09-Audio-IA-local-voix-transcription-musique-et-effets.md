---
title: "Livre I — Chapitre 9 : Audio IA local, voix, transcription, musique et effets"
id: "DOC-L1-CH06"
status: "reviewed"
version: "1.4.0"
lang: "fr-FR"
book: "Livre I"
chapter: 9
legacy-chapter: 6
canonical-order: 9
last-verified: "2026-07-18"
reference-platform:
  os: "Windows 11 64 bits"
  gpu: "AMD Radeon RX 6750 XT 12 Go"
  cpu: "AMD Ryzen 7 2700"
  ram: "32 Go"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audio IA local, voix, transcription, musique et effets

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L1-CH06`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **État technique vérifié le :** 18 juillet 2026  
> **Résultat attendu :** disposer d’une chaîne audio locale, traçable et juridiquement vérifiable pour créer des voix, transcrire des enregistrements, générer des maquettes musicales et produire des effets destinés au jeu.

## 1. Objet du chapitre

Ce chapitre construit la couche audio locale du projet.

Elle doit couvrir quatre besoins distincts :

1. **synthèse vocale** pour les dialogues, narrations et prototypes ;
2. **transcription** pour les réunions, prises de voix et sous-titres ;
3. **génération musicale** pour les maquettes et recherches d’ambiance ;
4. **génération ou transformation d’effets sonores** pour les prototypes et bibliothèques internes.

Ces quatre domaines ne doivent pas être confondus dans un seul environnement Python. Les dépendances, licences, formats et besoins matériels diffèrent fortement.

La stratégie du guide est :

> **[SORTIE] Résultat attendu - Ne pas saisir :** comparer avec la sortie obtenue.

```text
Texte / audio source
        │
        ├── TTS léger et reproductible
        │   ├── Kokoro
        │   └── Piper
        │
        ├── TTS expressif et clonage autorisé
        │   ├── Chatterbox
        │   └── Voicebox comme studio optionnel
        │
        ├── Transcription
        │   ├── faster-whisper CPU INT8
        │   ├── whisper.cpp CPU ou Vulkan
        │   └── OpenAI Whisper comme référence
        │
        ├── Génération expérimentale
        │   ├── MusicGen
        │   └── AudioGen
        │
        └── Postproduction
            ├── FFmpeg
            ├── Audacity
            └── Ardour
```

## 2. Principes obligatoires

### 2.1 Le CPU reste la référence

Sur la RX 6750 XT, aucune chaîne audio ne doit dépendre exclusivement d’un backend GPU expérimental.

Chaque outil retenu doit disposer :

- d’un mode CPU fonctionnel ;
- d’une commande de test minimale ;
- d’un fichier de versions ;
- d’un emplacement de cache connu ;
- d’une méthode de désinstallation ou de restauration.

Les accélérations DirectML, Vulkan, ROCm ou ZLUDA peuvent être testées dans des environnements isolés, mais elles ne remplacent pas le chemin CPU de référence.

### 2.2 Une voix n’est pas un simple fichier modèle

Toute voix doit posséder une fiche indiquant :

- son origine ;
- le titulaire des droits ou du consentement ;
- les usages autorisés ;
- la langue et l’accent ;
- la méthode d’enregistrement ;
- le moteur compatible ;
- la licence du modèle et de la voix ;
- la date de validation ;
- les restrictions de diffusion.

### 2.3 Aucun clonage sans consentement explicite

Le projet interdit :

- le clonage d’une personne sans autorisation documentée ;
- l’imitation trompeuse d’une personnalité réelle ;
- l’utilisation de prises obtenues dans un contexte privé sans accord ;
- la fabrication d’un consentement après la génération ;
- l’association d’une voix à des propos susceptibles de nuire à la personne enregistrée.

Pour les voix internes au projet, conserver une preuve de consentement et une description précise des usages autorisés.

### 2.4 Les sorties IA restent des sources intermédiaires

Une génération brute ne doit pas être intégrée directement dans le jeu.

Le pipeline officiel est :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Génération
    ↓
Écoute et sélection humaine
    ↓
Nettoyage
    ↓
Montage
    ↓
Normalisation
    ↓
Validation artistique et juridique
    ↓
Export jeu
```

## 3. Architecture des dossiers

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
audio-local/
├── environments/
│   ├── voicebox/
│   ├── chatterbox/
│   ├── kokoro/
│   ├── piper/
│   ├── faster-whisper/
│   ├── whisper-cpp/
│   └── audiocraft/
├── models/
│   ├── tts/
│   ├── stt/
│   ├── music/
│   └── sfx/
├── voices/
│   ├── references/
│   ├── manifests/
│   └── consent/
├── recordings/
│   ├── raw/
│   └── cleaned/
├── transcripts/
├── generations/
│   ├── speech/
│   ├── music/
│   └── sfx/
├── masters/
├── game-ready/
├── benchmarks/
├── logs/
└── scripts/
```

Ne pas mélanger :

- les enregistrements bruts ;
- les références de clonage ;
- les générations intermédiaires ;
- les masters validés ;
- les fichiers compressés destinés au moteur de jeu.

## 4. Formats audio du projet

### 4.1 Formats sources

| Usage | Format recommandé |
|---|---|
| Enregistrement de voix | WAV PCM 24 bits |
| Traitement intermédiaire | WAV PCM 32 bits flottant |
| Archive sans perte | FLAC |
| Échange avec outils IA | WAV PCM 16 ou 24 bits |
| Export final Godot | OGG Vorbis ou WAV selon usage |
| Prévisualisation légère | Opus ou OGG |

### 4.2 Fréquences d’échantillonnage

Conserver la fréquence native du moteur pendant la génération.

Pour les masters du projet :

- `48 kHz` pour les voix, ambiances et effets liés au jeu ;
- `44,1 kHz` uniquement lorsqu’un outil ou une bibliothèque l’impose ;
- `16 kHz mono` pour les entrées Whisper lorsque le moteur l’exige ou pour les tests reproductibles.

Ne pas effectuer plusieurs conversions successives entre 44,1 et 48 kHz.

### 4.3 Convention de nommage

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
<type>_<personnage-ou-source>_<intention>_<langue>_<version>.<extension>
```

Exemples :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
voice_mara_warning_fr_v003.wav
voice_narrator_codex_fr_v002.flac
sfx_door_metal_heavy_v005.wav
music_ruins_night_loop_v004.wav
```

## 5. Voicebox : studio vocal optionnel

### 5.1 Positionnement

Voicebox est un studio vocal open source combinant :

- plusieurs moteurs TTS ;
- Whisper pour la transcription ;
- des fonctions de dictée ;
- une API REST ;
- un serveur MCP ;
- des traitements audio ;
- une interface de bureau.

Le projet fournit actuellement un installeur Windows MSI et un déploiement Docker.

### 5.2 Parcours retenu

Pour la configuration de référence :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Voicebox Windows
├── CPU : référence universelle
├── DirectML : option de test
├── CUDA : non applicable à la RX 6750 XT
└── ROCm : parcours Linux, non retenu pour Windows
```

Voicebox doit donc être installé d’abord en mode CPU. DirectML peut être testé après validation fonctionnelle, sans modifier l’environnement de référence.

### 5.3 Installation prudente

1. télécharger l’installeur depuis la source officielle ;
2. vérifier le nom du projet et l’éditeur ;
3. enregistrer la version et l’empreinte du fichier ;
4. installer dans un dossier dédié ;
5. démarrer sans télécharger tous les moteurs ;
6. tester un seul moteur léger ;
7. vérifier les dossiers de modèles et de données ;
8. sauvegarder la configuration avant d’ajouter un moteur lourd.

### 5.4 Rôle dans le guide

Voicebox est recommandé lorsque le lecteur souhaite :

- comparer plusieurs moteurs dans une seule interface ;
- gérer des références vocales ;
- dicter localement ;
- exposer une API audio ;
- connecter un agent via MCP ;
- produire rapidement des prototypes de dialogues.

Il reste optionnel : les moteurs peuvent être utilisés directement par leurs interfaces Python ou en ligne de commande.

## 6. Kokoro : synthèse légère

### 6.1 Positionnement

Kokoro est un modèle TTS léger de 82 millions de paramètres, accompagné d’une bibliothèque d’inférence installable avec Python.

Il est adapté à :

- la génération rapide sur CPU ;
- les voix temporaires de gameplay ;
- les tests de rythme et de durée ;
- les narrations simples ;
- les pipelines automatisés.

### 6.2 Environnement isolé

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
py -3.11 -m venv environments\kokoro\.venv
environments\kokoro\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install kokoro soundfile
```

Enregistrer ensuite :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
pip freeze > environments\kokoro\requirements-lock.txt
```

### 6.3 Test minimal

Créer `scripts/test-kokoro.py` avec une phrase française courte, générer un WAV puis vérifier :

- que la langue choisie correspond au modèle ;
- que le fichier n’est pas vide ;
- que la fréquence d’échantillonnage est enregistrée ;
- qu’aucune coupure n’apparaît en début ou fin ;
- que les nombres, sigles et noms propres sont prononcés correctement.

### 6.4 Usage recommandé

Kokoro est le premier moteur à tester pour :

- les prototypes ;
- les centaines de lignes temporaires ;
- les tests d’interface ;
- les voix système ;
- l’accessibilité ;
- les prévisualisations de localisation.

## 7. Piper : synthèse robuste et embarquable

### 7.1 Dépôt actuel

Le développement historique de `rhasspy/piper` a été déplacé vers `OHF-Voice/piper1-gpl`.

Le dépôt actuel :

- fournit le paquet `piper-tts` ;
- intègre `espeak-ng` pour la phonémisation ;
- expose une CLI, une API Python et un serveur web ;
- utilise la licence GPL-3.0 pour le code actuel.

Les voix téléchargées peuvent posséder des licences distinctes.

### 7.2 Installation

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
py -3.11 -m venv environments\piper\.venv
environments\piper\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install piper-tts
```

Lister et télécharger les voix :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python -m piper.download_voices
python -m piper.download_voices fr_FR-siwis-medium --data-dir models\tts\piper
```

La disponibilité et le nom exact des voix doivent être vérifiés lors de l’installation.

### 7.3 Génération

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python -m piper `
  --data-dir models\tts\piper `
  -m fr_FR-siwis-medium `
  -f generations\speech\piper-test.wav `
  -- "Ceci est un test de synthèse vocale locale."
```

### 7.4 Usage recommandé

Piper est adapté à :

- la synthèse rapide ;
- les machines sans GPU ;
- les systèmes embarqués ;
- les voix utilitaires ;
- les interfaces d’accessibilité ;
- les serveurs locaux à faible consommation.

## 8. Chatterbox : voix expressive et clonage contrôlé

### 8.1 Positionnement

Chatterbox est une famille de modèles TTS open source de Resemble AI.

La branche multilingue actuelle est destinée aux voix conversationnelles et au clonage vocal, tandis que les variantes Turbo privilégient la rapidité et certains marqueurs paralinguistiques.

Le projet est installé avec :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
pip install chatterbox-tts
```

Le dépôt indique que le développement et les tests de référence utilisent Python 3.11 sous Debian. Une installation Windows doit donc être traitée comme une adaptation à valider, pas comme une équivalence garantie.

### 8.2 Environnement séparé

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
py -3.11 -m venv environments\chatterbox\.venv
environments\chatterbox\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install chatterbox-tts
pip freeze > environments\chatterbox\requirements-lock.txt
```

### 8.3 Référence vocale

Une référence de clonage doit être :

- enregistrée avec consentement ;
- exempte de musique ;
- exempte de réverbération excessive ;
- limitée à une seule personne ;
- fournie dans une langue compatible ;
- conservée avec son manifeste ;
- retirée si le consentement est révoqué.

### 8.4 Manifest de voix

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
id: VOICE-MARA-FR-001
owner: "Interprète interne"
consent_status: approved
consent_document: "consent/VOICE-MARA-FR-001.pdf"
language: fr-FR
engine: chatterbox
reference_file: "references/mara-neutral-01.wav"
reference_sha256: "À_CALCULER"
allowed_uses:
  - prototype
  - game-dialogue
forbidden_uses:
  - advertising-without-new-approval
  - impersonation
review_date: "2026-07-18"
```

### 8.5 Validation

Tester au minimum :

- phrase neutre ;
- question ;
- avertissement ;
- nombres ;
- nom propre ;
- phrase longue ;
- émotion modérée ;
- prononciation de termes fictifs.

Un clonage ressemblant mais instable n’est pas considéré comme validé.

## 9. Transcription avec faster-whisper

### 9.1 Parcours principal

`faster-whisper` est la voie Python recommandée pour la transcription locale sur CPU.

Il utilise CTranslate2 et prend en charge :

- le calcul CPU INT8 ;
- les timestamps ;
- la détection de langue ;
- le VAD ;
- le traitement par lots ;
- des modèles Whisper convertis.

### 9.2 Installation

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
py -3.11 -m venv environments\faster-whisper\.venv
environments\faster-whisper\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install faster-whisper
pip freeze > environments\faster-whisper\requirements-lock.txt
```

### 9.3 Script minimal

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```python
from pathlib import Path
from faster_whisper import WhisperModel

source = Path("recordings/cleaned/test.wav")
model = WhisperModel("small", device="cpu", compute_type="int8")
segments, info = model.transcribe(
    str(source),
    beam_size=5,
    vad_filter=True,
    language="fr",
)

output = Path("transcripts/test.txt")
output.parent.mkdir(parents=True, exist_ok=True)
with output.open("w", encoding="utf-8") as handle:
    for segment in segments:
        handle.write(
            f"[{segment.start:08.2f} --> {segment.end:08.2f}] "
            f"{segment.text.strip()}\n"
        )

print(f"Langue : {info.language}")
```

### 9.4 Modèle de départ

Pour le Ryzen 7 2700 :

| Besoin | Modèle de départ |
|---|---|
| test rapide | `base` |
| français courant | `small` |
| meilleure précision hors temps réel | `medium` |
| validation maximale | comparaison avec `large-v3` ou `turbo` |

Le modèle `turbo` est optimisé pour la transcription, mais ne doit pas être utilisé comme modèle de traduction vers l’anglais.

### 9.5 Validation humaine

Toute transcription destinée à :

- un sous-titre publié ;
- un dialogue de jeu ;
- un contrat ;
- une décision de production ;
- une citation ;
- une fiche de personnage ;

doit être relue à partir de l’audio original.

Les modèles Whisper peuvent omettre, fusionner ou inventer des segments, notamment lorsque l’audio est silencieux, bruité ou ambigu.

## 10. Transcription avec whisper.cpp

### 10.1 Positionnement

`whisper.cpp` fournit une implémentation C/C++ autonome avec :

- exécution CPU ;
- quantification ;
- support Vulkan ;
- support ROCm ;
- VAD ;
- serveur local ;
- binaires Windows ;
- faible dépendance d’exécution.

Pour la RX 6750 XT, le parcours Vulkan est un laboratoire intéressant, car il évite de dépendre de CUDA.

### 10.2 Référence CPU

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
whisper-cli.exe `
  -m models\stt\ggml-small.bin `
  -f recordings\cleaned\test-16k-mono.wav `
  -l fr `
  -otxt `
  -osrt
```

### 10.3 Préparation FFmpeg

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
ffmpeg -i recordings\raw\test.wav `
  -ar 16000 `
  -ac 1 `
  -c:a pcm_s16le `
  recordings\cleaned\test-16k-mono.wav
```

### 10.4 Benchmark CPU contre Vulkan

Utiliser le même :

- fichier audio ;
- modèle ;
- nombre de threads ;
- options de segmentation ;
- langue ;
- VAD ;
- format de sortie.

Enregistrer :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
engine: whisper.cpp
commit: "À_RENSEIGNER"
backend: vulkan
model: ggml-small.bin
model_sha256: "À_CALCULER"
audio_duration_seconds: 600
processing_seconds: 0
real_time_factor: 0
word_errors_reviewed: 0
hardware: "RX 6750 XT / Ryzen 7 2700 / 32 Go"
```

Si Vulkan produit des erreurs, des gels ou une précision différente, revenir au CPU sans modifier les données source.

## 11. OpenAI Whisper comme référence

Le paquet officiel `openai-whisper` reste utile pour :

- comparer les résultats ;
- vérifier une régression ;
- valider un modèle ou un fichier ;
- reproduire le comportement de référence.

Installation :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
py -3.11 -m venv environments\openai-whisper\.venv
environments\openai-whisper\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install openai-whisper
```

FFmpeg doit être installé et accessible dans le `PATH`.

Exemple :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
whisper recordings\cleaned\test.wav `
  --model small `
  --language French `
  --output_dir transcripts\openai-whisper
```

Ce moteur n’est pas le parcours quotidien du guide sur la configuration de référence, mais il constitue un témoin utile.

## 12. Nettoyage et préparation avec FFmpeg

### 12.1 Normaliser le format

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
ffmpeg -i input.wav -ar 48000 -ac 1 -c:a pcm_s24le output.wav
```

### 12.2 Mesurer le niveau sonore

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
ffmpeg -i input.wav -af loudnorm=print_format=json -f null NUL
```

### 12.3 Normalisation en deux passes

Pour un master important :

1. lancer une première mesure `loudnorm` ;
2. relever les valeurs mesurées ;
3. exécuter la seconde passe avec ces valeurs ;
4. vérifier le fichier dans un éditeur audio.

Ne pas normaliser aveuglément toutes les voix au même niveau si leur rôle sonore diffère.

### 12.4 Supprimer les silences excessifs

Utiliser `silenceremove` uniquement sur une copie et vérifier les respirations, attaques de mots et consonnes finales.

## 13. Audacity et Ardour

### 13.1 Audacity

Audacity est recommandé pour :

- nettoyer une prise ;
- couper les silences ;
- corriger un clic ;
- comparer plusieurs générations ;
- exporter rapidement ;
- appliquer une normalisation simple.

### 13.2 Ardour

Ardour est recommandé pour :

- les projets multipistes ;
- les dialogues avec ambiance ;
- les bus et effets ;
- les automations ;
- les stems musicaux ;
- le mixage final ;
- les sessions longues et versionnées.

### 13.3 Règle de non-destruction

Toujours conserver :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
source brute
édition de travail
master sans perte
export jeu
```

## 14. Génération musicale avec AudioCraft et MusicGen

### 14.1 Statut

AudioCraft fournit le code de MusicGen et AudioGen.

La distinction de licence est essentielle :

- le **code** du dépôt est sous licence MIT ;
- les **poids de modèles fournis** sont sous CC-BY-NC 4.0.

Ces poids ne doivent donc pas être intégrés dans un pipeline commercial sans analyse juridique et solution de remplacement compatible.

### 14.2 Usage autorisé dans le guide

MusicGen est utilisé pour :

- recherche d’ambiance ;
- maquettes non commerciales ;
- tests de rythme ;
- références temporaires ;
- exploration de structures ;
- démonstrations techniques.

Il ne constitue pas la source musicale commerciale par défaut du projet.

### 14.3 Environnement séparé

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
py -3.11 -m venv environments\audiocraft\.venv
environments\audiocraft\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install git+https://github.com/facebookresearch/audiocraft.git
```

Cette installation peut être lourde et dépendre fortement de PyTorch. Sur la RX 6750 XT sous Windows, le CPU est la référence fonctionnelle, avec des temps de génération potentiellement élevés.

### 14.4 Prompt musical

Un prompt doit décrire :

- style ;
- instrumentation ;
- tempo ;
- énergie ;
- structure ;
- ambiance ;
- durée ;
- éléments à éviter.

Exemple :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Dark ambient exploration cue, sparse bowed metal, low cello drones,
slow pulse around 60 BPM, no vocals, no heroic melody, seamless loop,
ruined underground laboratory, restrained tension.
```

### 14.5 Manifest de génération

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
id: MUSIC-RUINS-NIGHT-004
engine: audiocraft-musicgen
model: facebook/musicgen-small
model_license: CC-BY-NC-4.0
commercial_status: forbidden-until-replaced-or-cleared
prompt: "Dark ambient exploration cue..."
seed: 184231
duration_seconds: 20
source_file: generations/music/music_ruins_night_v004.wav
status: prototype
```

## 15. Génération d’effets avec AudioGen

AudioGen produit des sons à partir de descriptions textuelles.

Usages adaptés :

- idées d’impact ;
- textures mécaniques ;
- ambiances temporaires ;
- sons de créatures en phase de recherche ;
- variations destinées au montage.

Exemple de prompt :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Heavy corroded steel door closing in an underground bunker,
short mechanical groan, deep impact, small debris falling,
no music, no voice, dry recording.
```

Toute sortie doit être :

- écoutée ;
- découpée ;
- nettoyée ;
- comparée à des références ;
- documentée ;
- remplacée si sa licence n’est pas compatible avec la destination.

Les poids AudioGen fournis par AudioCraft relèvent également de la licence CC-BY-NC 4.0.

## 16. Production de dialogues de jeu

### 16.1 Pipeline recommandé

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Texte validé
    ↓
Dictionnaire de prononciation
    ↓
Génération de trois variantes
    ↓
Sélection humaine
    ↓
Nettoyage
    ↓
Montage respirations et silences
    ↓
Normalisation
    ↓
Sous-titre synchronisé
    ↓
Intégration Godot
```

### 16.2 Générer plusieurs variantes

Pour chaque ligne importante :

- variation neutre ;
- variation plus retenue ;
- variation plus intense.

Ne pas tenter de corriger uniquement par prompt une ligne dont le texte est mal écrit.

### 16.3 Dictionnaire de prononciation

Créer un fichier :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
audio-local/voices/pronunciation/fr-FR.yaml
```

Exemple :

> **[VSC] Visual Studio Code - Créer ou modifier :** `text audio-local/voices/pronunciation/fr-FR.yaml`.

```yaml
Aeryn: "É-rine"
Kael: "Ka-elle"
Nhar: "Nar"
ZLUDA: "Zé-lou-da"
ComfyUI: "Comfy U I"
```

Le dictionnaire doit être versionné avec les dialogues.

## 17. Sous-titres et accessibilité

La transcription peut produire une première version des sous-titres, mais elle ne remplace pas :

- la ponctuation éditoriale ;
- les noms des locuteurs ;
- les descriptions de sons ;
- les indications hors champ ;
- les choix de lisibilité ;
- la synchronisation finale.

Format source recommandé :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
WebVTT ou SRT
```

Format d’intégration : structure de données Godot dérivée du fichier source, jamais une copie non traçable.

## 18. Gestion des modèles et licences

Chaque modèle audio doit posséder un manifeste :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
id: MODEL-AUDIO-001
name: "Nom du modèle"
engine: "kokoro | piper | chatterbox | whisper | audiocraft"
source: "URL officielle"
version_or_commit: "À_RENSEIGNER"
model_file: "models/..."
sha256: "À_CALCULER"
code_license: "À_VÉRIFIER"
weights_license: "À_VÉRIFIER"
voice_or_dataset_license: "À_VÉRIFIER"
commercial_use: "allowed | restricted | forbidden | unknown"
verified_on: "2026-07-18"
```

Une licence de code permissive ne rend pas automatiquement les poids, les voix ou les jeux de données exploitables commercialement.

## 19. Sécurité et confidentialité

### 19.1 Données sensibles

Les dossiers suivants peuvent contenir des données biométriques ou personnelles :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
voices/references/
voices/consent/
recordings/raw/
transcripts/
```

Ils doivent être :

- exclus des dépôts publics ;
- chiffrés lorsque nécessaire ;
- sauvegardés séparément ;
- accessibles uniquement aux personnes autorisées ;
- supprimables à la demande du titulaire.

### 19.2 APIs locales

Les serveurs TTS ou STT doivent écouter par défaut sur :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
127.0.0.1
```

Ne pas exposer une API de clonage vocal sur le réseau local ou Internet sans authentification, journalisation, quotas et politique d’accès.

### 19.3 Fichiers non fiables

Un fichier audio téléchargé doit être considéré comme non fiable.

Avant traitement :

- vérifier son extension réelle ;
- analyser le fichier ;
- convertir vers WAV avec FFmpeg ;
- limiter la durée ;
- refuser les fichiers anormalement volumineux ;
- ne pas exécuter de script inclus dans une archive.

## 20. Benchmarks

### 20.1 Mesures TTS

Enregistrer :

- durée du texte ;
- durée générée ;
- temps de génération ;
- facteur temps réel ;
- RAM maximale ;
- VRAM maximale ;
- erreurs de prononciation ;
- stabilité du locuteur ;
- bruit ou hallucination audio.

### 20.2 Mesures STT

Enregistrer :

- durée de l’audio ;
- temps de transcription ;
- facteur temps réel ;
- langue détectée ;
- taux d’erreurs sur un échantillon relu ;
- erreurs sur noms propres ;
- qualité des timestamps ;
- impact du VAD.

### 20.3 Cas de référence

Créer au minimum :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
benchmarks/audio/
├── fr-clean-60s.wav
├── fr-noisy-60s.wav
├── fr-two-speakers-60s.wav
├── names-and-numbers-30s.wav
└── silence-and-pauses-30s.wav
```

Les fichiers de benchmark doivent avoir une origine et une autorisation claires.

## 21. Mode Solo

Le Mode Solo privilégie :

- Voicebox uniquement si une interface unifiée est utile ;
- Kokoro ou Piper pour les prototypes ;
- faster-whisper `small` en CPU INT8 ;
- whisper.cpp comme alternative autonome ;
- Chatterbox pour les lignes importantes et consenties ;
- MusicGen et AudioGen uniquement pour les maquettes ;
- Audacity pour le nettoyage rapide ;
- FFmpeg pour les conversions automatisées ;
- un seul environnement actif à la fois.

## 22. Mode Studio

Le Mode Studio ajoute :

- registre central des voix ;
- documents de consentement ;
- rôles d’accès aux références vocales ;
- serveur de génération interne authentifié ;
- file de tâches ;
- journal des modèles et versions ;
- validation artistique à plusieurs niveaux ;
- comparaison automatique des sorties ;
- contrôle juridique avant intégration ;
- stockage séparé des enregistrements biométriques ;
- politique de révocation d’une voix ;
- dictionnaires de prononciation par langue ;
- tests de sous-titres et d’accessibilité.

## 23. Diagnostic

### Une génération TTS est vide

Vérifier :

- le modèle téléchargé ;
- le chemin de sortie ;
- la langue ;
- la voix ;
- la fréquence d’échantillonnage ;
- les journaux Python ;
- l’espace disque ;
- la longueur du texte.

### La voix change au milieu d’une phrase

- raccourcir le segment ;
- nettoyer la référence ;
- réduire les variations extrêmes ;
- tester une autre graine ;
- vérifier que la référence ne contient qu’une seule personne ;
- générer phrase par phrase.

### La transcription invente du texte

- activer ou ajuster le VAD ;
- découper les longs silences ;
- indiquer la langue ;
- utiliser un modèle plus grand ;
- comparer faster-whisper et whisper.cpp ;
- relire l’audio ;
- ne jamais valider automatiquement un passage silencieux.

### Les performances GPU sont inférieures au CPU

- confirmer le backend réellement utilisé ;
- comparer avec les mêmes paramètres ;
- vérifier les transferts CPU/GPU ;
- réduire le modèle ;
- mettre à jour le pilote ;
- revenir au CPU si la voie GPU n’est pas stable.

### La musique générée ne boucle pas

- générer une durée supérieure à la boucle cible ;
- découper une zone stable ;
- créer un fondu croisé ;
- ajuster la mesure dans Ardour ;
- éviter les attaques ou fins trop marquées ;
- tester la boucle dans Godot.

## 24. Checklist de validation

- [ ] FFmpeg est installé et accessible.
- [ ] Les dossiers audio sont séparés par rôle.
- [ ] Un moteur TTS léger fonctionne sur CPU.
- [ ] Piper ou Kokoro produit un WAV valide.
- [ ] Chatterbox fonctionne dans un environnement séparé ou est explicitement reporté.
- [ ] Toute voix clonée possède un consentement vérifiable.
- [ ] faster-whisper CPU INT8 transcrit un fichier français.
- [ ] whisper.cpp CPU fonctionne comme deuxième moteur.
- [ ] Le test Vulkan de whisper.cpp est documenté ou marqué incompatible.
- [ ] Les modèles possèdent un manifeste et une empreinte.
- [ ] Les licences du code, des poids et des voix sont distinguées.
- [ ] Les poids AudioCraft sont identifiés comme non commerciaux.
- [ ] Les enregistrements bruts ne sont pas versionnés publiquement.
- [ ] Les APIs audio écoutent uniquement en local.
- [ ] Une chaîne de postproduction est validée.
- [ ] Les exports Godot sont produits depuis des masters sans perte.
- [ ] Les sous-titres générés sont relus humainement.
- [ ] Une sauvegarde et une procédure de restauration existent.

## 25. Critère d’acceptation

Le chapitre est validé lorsque le poste peut exécuter ce scénario :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Texte français
    → voix légère Kokoro ou Piper
    → WAV valide

Référence vocale autorisée
    → génération Chatterbox ou Voicebox
    → validation humaine

Enregistrement WAV
    → faster-whisper CPU INT8
    → transcription horodatée
    → comparaison whisper.cpp

Prompt musical ou effet
    → maquette AudioCraft non commerciale
    → nettoyage FFmpeg/Audacity/Ardour
    → master documenté
```

## 26. Décisions retenues

| Décision | Statut |
|---|---|
| CPU comme référence universelle | retenu |
| Voicebox comme studio obligatoire | écarté |
| Voicebox comme studio optionnel | retenu |
| Kokoro pour les prototypes rapides | retenu |
| Piper actuel `OHF-Voice/piper1-gpl` | retenu |
| Ancien dépôt Piper comme source principale | écarté |
| Chatterbox pour le clonage consenti et l’expression | retenu |
| faster-whisper CPU INT8 comme STT principal | retenu |
| whisper.cpp CPU/Vulkan comme référence autonome | retenu |
| OpenAI Whisper comme moteur de comparaison | retenu |
| AudioCraft pour une production commerciale directe | interdit sans nouvelle validation |
| AudioCraft pour les maquettes non commerciales | autorisé |
| Validation humaine des voix et transcriptions | obligatoire |
| Exposition réseau publique des APIs vocales | interdite par défaut |

## 27. Sources officielles vérifiées

- [Voicebox — dépôt officiel](https://github.com/jamiepine/voicebox)
- [Voicebox — documentation](https://docs.voicebox.sh/overview/introduction)
- [Chatterbox TTS](https://github.com/resemble-ai/chatterbox)
- [Kokoro](https://github.com/hexgrad/kokoro)
- [Piper actuel](https://github.com/OHF-Voice/piper1-gpl)
- [Piper CLI](https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/CLI.md)
- [OpenAI Whisper](https://github.com/openai/whisper)
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp)
- [AudioCraft](https://github.com/facebookresearch/audiocraft)
- [MusicGen](https://facebookresearch.github.io/audiocraft/docs/MUSICGEN.html)
- [AudioGen](https://facebookresearch.github.io/audiocraft/docs/AUDIOGEN.html)
- [FFmpeg](https://ffmpeg.org/documentation.html)
- [Audacity](https://www.audacityteam.org/)
- [Ardour](https://ardour.org/)

## 28. Résumé

La chaîne audio locale du guide repose sur une séparation claire des responsabilités :

- Kokoro et Piper pour la synthèse légère ;
- Chatterbox et Voicebox pour la voix expressive et le clonage autorisé ;
- faster-whisper et whisper.cpp pour la transcription ;
- OpenAI Whisper comme référence ;
- MusicGen et AudioGen pour les maquettes expérimentales ;
- FFmpeg, Audacity et Ardour pour transformer les générations en assets utilisables.

La qualité finale dépend moins du nombre de modèles installés que de la qualité des prises, du consentement, de la traçabilité, de la postproduction et de la validation humaine.

Ce chapitre termine le socle technique du Livre I. La prochaine étape est la validation complète de M2 et la préparation du Livre II consacré au développement du jeu et à son architecture.
