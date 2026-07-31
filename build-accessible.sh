#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

command -v python3 >/dev/null 2>&1 || { echo "Erreur : Python 3 est introuvable." >&2; exit 1; }
command -v docker >/dev/null 2>&1 || { echo "Erreur : Docker est introuvable." >&2; exit 1; }
command -v pdfinfo >/dev/null 2>&1 || { echo "Erreur : pdfinfo est introuvable." >&2; exit 1; }
command -v pdftotext >/dev/null 2>&1 || { echo "Erreur : pdftotext est introuvable." >&2; exit 1; }
command -v qpdf >/dev/null 2>&1 || { echo "Erreur : qpdf est introuvable." >&2; exit 1; }

python3 tools/build_accessible_pdf.py --clean --pull
python3 tools/validate_accessible_pdf.py --report dist/publications/accessible-pdf-validation.json

echo "PDF balisé candidat généré dans dist/publications/Guide-IA-GameDev-accessible.pdf"
