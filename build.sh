#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"

if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
    echo "Erreur : Python 3 est introuvable." >&2
    exit 1
fi

exec "$PYTHON_BIN" "$ROOT/tools/build_publications.py" --root "$ROOT" "$@"
