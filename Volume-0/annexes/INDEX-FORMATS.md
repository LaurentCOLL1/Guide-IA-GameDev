---
title: "Annexe — Index des formats"
id: "DOC-V0-ANN-INDEX-FORMATS"
status: "in-progress"
version: "0.1.0"
---

# Index des formats

Cet index définit les formats privilégiés pour les sources, les échanges, les livrables et l’archivage. Un format non répertorié peut être utilisé, mais son choix doit être justifié lorsqu’il devient une dépendance du projet.

## Classification

- **Source** : format modifiable faisant autorité.
- **Échange** : format intermédiaire entre outils.
- **Livrable** : format destiné à l’utilisateur, au moteur ou à la publication.
- **Archive** : format conservé pour la reproductibilité ou la migration.

## Documentation et données textuelles

| Format | Usage principal | Classe | Priorité | Notes |
|---|---|---|---|---|
| Markdown `.md` | Source documentaire | Source | Obligatoire | Source de vérité de la collection |
| YAML `.yaml` / `.yml` | Métadonnées et configuration lisible | Source | Recommandé | Éviter les structures excessivement complexes |
| JSON `.json` | Échange structuré et configurations d’outils | Source / échange | Recommandé | Valider avec un schéma lorsque le contrat est stable |
| CSV `.csv` | Tableaux simples et imports | Échange | Optionnel | Documenter séparateur, encodage et unités |
| TOML `.toml` | Configuration d’outils | Source | Optionnel | Utiliser lorsqu’il s’agit du format natif du projet |
| PDF `.pdf` | Publication figée | Livrable | Obligatoire | Ne doit pas remplacer les sources Markdown |
| HTML `.html` | Publication web | Livrable | Recommandé | Généré depuis les sources |
| DOCX `.docx` | Échange éditorial | Livrable / échange | Optionnel | Généré, non canonique |

## Code et scripts

| Format | Usage | Classe | Notes |
|---|---|---|---|
| GDScript `.gd` | Code Godot | Source | Respecter les conventions du projet |
| Python `.py` | Automatisation et outils | Source | Dépendances verrouillées |
| PowerShell `.ps1` | Scripts Windows | Source | Prévoir journalisation et mode simulation |
| Shell `.sh` | Scripts Linux et environnements compatibles | Source | Utiliser un shebang explicite |
| SQL `.sql` | Schémas et migrations | Source | Une migration publiée ne doit pas être réécrite |

## Images et textures

| Format | Usage | Classe | Priorité |
|---|---|---|---|
| PNG `.png` | Image sans perte, transparence, masques | Source / échange | Recommandé |
| JPEG `.jpg` | Image photographique compressée | Livrable / échange | Optionnel |
| WebP `.webp` | Publication web et compression | Livrable | Recommandé pour le web |
| EXR `.exr` | Données HDR, passes et compositing | Source / échange | Recommandé pour pipelines avancés |
| TIFF `.tif` | Échange haute qualité | Échange | Optionnel |
| SVG `.svg` | Icônes et graphiques vectoriels | Source / livrable | Recommandé |
| KTX2 `.ktx2` | Textures GPU compressées | Livrable runtime | Recommandé selon cible |

## Modèles, scènes et animation 3D

| Format | Usage | Classe | Priorité |
|---|---|---|---|
| Blender `.blend` | Source de création 3D | Source | Obligatoire pour assets Blender |
| glTF / GLB `.gltf` / `.glb` | Échange vers le moteur | Échange / livrable | Recommandé |
| FBX `.fbx` | Échange avec outils tiers | Échange | Optionnel, seulement si nécessaire |
| OBJ `.obj` | Géométrie statique simple | Échange | Optionnel |
| Alembic `.abc` | Caches d’animation ou simulation | Échange | Optionnel |

## Audio et vidéo

| Format | Usage | Classe | Priorité |
|---|---|---|---|
| WAV `.wav` | Master audio sans perte | Source / archive | Obligatoire pour les masters |
| FLAC `.flac` | Archive audio sans perte compressée | Archive | Recommandé |
| OGG Vorbis `.ogg` | Audio runtime ou diffusion | Livrable | Recommandé selon moteur |
| MP3 `.mp3` | Diffusion et prévisualisation | Livrable | Optionnel |
| Opus `.opus` | Voix et diffusion efficace | Livrable | Recommandé selon cible |
| MP4 `.mp4` | Vidéo de démonstration | Livrable | Recommandé |
| WebM `.webm` | Vidéo web ou runtime | Livrable | Optionnel |

## Modèles IA et workflows

| Format | Usage | Classe | Notes |
|---|---|---|---|
| SafeTensors `.safetensors` | Poids de modèles | Archive / runtime | Préféré lorsqu’il est supporté |
| GGUF `.gguf` | Modèles quantifiés pour moteurs compatibles | Runtime | Enregistrer quantification et empreinte |
| ONNX `.onnx` | Échange et exécution de modèles | Échange / runtime | Documenter opset et backend |
| JSON de workflow ComfyUI | Graphe reproductible | Source | Conserver versions des nœuds et modèles |
| Fichiers de prompt `.md`, `.yaml` ou `.json` | Prompts versionnés | Source | Associer un identifiant stable |

## Données persistantes et archives

| Format | Usage | Classe | Notes |
|---|---|---|---|
| SQLite `.sqlite` / `.db` | Base locale | Source runtime | Versionner le schéma, pas nécessairement la base générée |
| ZIP `.zip` | Distribution et archivage général | Archive / livrable | Fournir une empreinte pour les versions publiées |
| TAR `.tar` avec compression | Archivage technique | Archive | Recommandé dans les environnements Unix |
| Godot Resource `.tres` | Ressources textuelles Godot | Source | Préféré aux variantes binaires pour la collaboration |
| Godot Scene `.tscn` | Scènes textuelles Godot | Source | Facilite revue et versionnement |

## Règles de choix

- Préférer un format ouvert, documenté et largement supporté.
- Conserver les sources modifiables même lorsqu’un format optimisé est généré.
- Ne pas versionner les fichiers générés lourds sans justification.
- Documenter unités, espace colorimétrique, fréquence, résolution et compression lorsque ces paramètres influencent le résultat.
- Associer une empreinte aux modèles et archives publiés.
- Vérifier les licences des codecs et bibliothèques nécessaires à la distribution.

## Checklist

- [ ] Le format source est identifié.
- [ ] Le format d’échange est compatible avec les outils ciblés.
- [ ] Le livrable peut être régénéré depuis les sources.
- [ ] Les paramètres critiques sont documentés.
- [ ] Les fichiers lourds respectent la stratégie Git ou Git LFS retenue.
- [ ] Les archives publiées possèdent une empreinte et un numéro de version.
