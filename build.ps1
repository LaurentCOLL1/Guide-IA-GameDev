$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$Python = Get-Command python -ErrorAction SilentlyContinue

if (-not $Python) {
    throw "Python 3 est introuvable. Installez Python et ajoutez-le au PATH."
}

& $Python.Source (Join-Path $Root "tools/build_publications.py") --root $Root @args

if ($LASTEXITCODE -ne 0) {
    throw "La construction multiformat a échoué avec le code $LASTEXITCODE."
}
