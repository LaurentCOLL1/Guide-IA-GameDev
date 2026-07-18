# Construire la documentation

## Prérequis

### Obligatoire

- Git.
- Pandoc.
- Une distribution LaTeX pour la sortie PDF : MiKTeX sous Windows ou TeX Live sous Linux.

### Recommandé

- Visual Studio Code.
- Extension Markdown All in One.
- Mermaid CLI pour pré-rendre certains diagrammes lorsque nécessaire.

## Vérifier Pandoc

```bash
pandoc --version
```

## Construire le document

### Windows PowerShell

```powershell
./build.ps1
```

### Linux ou macOS

```bash
chmod +x build.sh
./build.sh
```

Les fichiers générés sont placés dans `dist/`.

## Ordre des sources

Le fichier `contents.txt` définit l'ordre officiel de compilation. Une ligne vide ou commençant par `#` est ignorée.

## Construction manuelle

```bash
pandoc --metadata-file=metadata.yaml --toc --number-sections --from=markdown+yaml_metadata_block --pdf-engine=xelatex --output=dist/Guide-IA-GameDev.pdf $(grep -vE '^\s*(#|$)' contents.txt)
```

Sous PowerShell, utiliser le script fourni afin d'éviter les différences de substitution de commandes.

## Dépannage

- **`pandoc` introuvable** : vérifier le `PATH`.
- **`xelatex` introuvable** : installer MiKTeX ou TeX Live.
- **Police absente** : modifier `metadata.yaml` ou installer une police libre compatible.
- **Lien ou image manquante** : vérifier les chemins relatifs depuis la racine du dépôt.

## Règle de publication

Le Markdown est la source de vérité. Les PDF, pages HTML et autres exports sont des artefacts générés et ne doivent pas être modifiés manuellement.
