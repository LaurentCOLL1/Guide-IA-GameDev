$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

$Python = Get-Command python -ErrorAction SilentlyContinue
if (-not $Python) {
    $Python = Get-Command py -ErrorAction SilentlyContinue
}
if (-not $Python) {
    throw "Python 3 est introuvable."
}

if ($Python.Name -eq "py.exe" -or $Python.Name -eq "py") {
    & $Python.Source -3 tools/build_publications.py --clean --formats pdf html epub
    if ($LASTEXITCODE -ne 0) { throw "La construction multiformat a échoué." }
    & $Python.Source -3 tools/validate_publications.py --report dist/publications/validation.json
} else {
    & $Python.Source tools/build_publications.py --clean --formats pdf html epub
    if ($LASTEXITCODE -ne 0) { throw "La construction multiformat a échoué." }
    & $Python.Source tools/validate_publications.py --report dist/publications/validation.json
}

if ($LASTEXITCODE -ne 0) {
    throw "La validation des publications a échoué."
}

Write-Host "Publications générées dans dist/publications/"
