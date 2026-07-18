#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DIST="$ROOT/dist"
CONTENTS_FILE="$ROOT/contents.txt"
METADATA_FILE="$ROOT/metadata.yaml"
OUTPUT_FILE="$DIST/Guide-IA-GameDev.pdf"

if ! command -v pandoc >/dev/null 2>&1; then
    echo "Erreur : Pandoc est introuvable. Installez Pandoc et ajoutez-le au PATH." >&2
    exit 1
fi

mkdir -p "$DIST"

mapfile -t SOURCES < <(
    sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' "$CONTENTS_FILE" |
    grep -vE '^(#|$)' |
    sed "s#^#$ROOT/#"
)

for source in "${SOURCES[@]}"; do
    if [[ ! -f "$source" ]]; then
        echo "Erreur : source absente : $source" >&2
        exit 1
    fi
done

echo "Construction de $OUTPUT_FILE"
pandoc \
    --metadata-file="$METADATA_FILE" \
    --from=markdown+yaml_metadata_block \
    --toc \
    --number-sections \
    --pdf-engine=xelatex \
    --resource-path="$ROOT" \
    --output="$OUTPUT_FILE" \
    "${SOURCES[@]}"

echo "PDF généré : $OUTPUT_FILE"
