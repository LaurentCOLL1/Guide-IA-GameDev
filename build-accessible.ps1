$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

foreach ($command in @("python", "docker", "pdfinfo", "pdftotext", "qpdf")) {
    if (-not (Get-Command $command -ErrorAction SilentlyContinue)) {
        throw "Erreur : $command est introuvable."
    }
}

python tools/build_accessible_pdf.py --clean --pull
python tools/validate_accessible_pdf.py --report dist/publications/accessible-pdf-validation.json

Write-Host "PDF balisé candidat généré dans dist/publications/Guide-IA-GameDev-accessible.pdf"
