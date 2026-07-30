#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

if ! command -v python3 >/dev/null 2>&1; then
    echo "Erreur : Python 3 est introuvable." >&2
    exit 1
fi

python3 tools/build_publications.py --clean --formats pdf html epub
python3 tools/validate_publications.py --report dist/publications/validation.json

echo "Publications générées dans dist/publications/"
