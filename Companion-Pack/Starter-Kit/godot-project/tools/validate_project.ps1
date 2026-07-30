[CmdletBinding()]
param(
    [string]$Report = ""
)

$ErrorActionPreference = "Stop"
$ScriptPath = Join-Path $PSScriptRoot "validate_project.py"

$Python = Get-Command python -ErrorAction SilentlyContinue
if ($null -eq $Python) {
    $Python = Get-Command py -ErrorAction SilentlyContinue
}
if ($null -eq $Python) {
    throw "Python 3.10 ou plus récent est requis pour la validation statique."
}

$Arguments = @($ScriptPath)
if ($Report) {
    $Arguments += @("--report", $Report)
}

& $Python.Source @Arguments
exit $LASTEXITCODE
