$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$Dist = Join-Path $Root "dist"
$ContentsFile = Join-Path $Root "contents.txt"
$MetadataFile = Join-Path $Root "metadata.yaml"
$FilterFile = Join-Path $Root "filters/pdf-normalize.lua"
$OutputFile = Join-Path $Dist "Guide-IA-GameDev.pdf"

if (-not (Get-Command pandoc -ErrorAction SilentlyContinue)) {
    throw "Pandoc est introuvable. Installez Pandoc et ajoutez-le au PATH."
}

foreach ($Required in @($ContentsFile, $MetadataFile, $FilterFile)) {
    if (-not (Test-Path $Required)) {
        throw "Fichier de construction absent : $Required"
    }
}

if (-not (Test-Path $Dist)) {
    New-Item -ItemType Directory -Path $Dist | Out-Null
}

$Sources = Get-Content $ContentsFile |
    ForEach-Object { $_.Trim() } |
    Where-Object { $_ -and -not $_.StartsWith("#") } |
    ForEach-Object { Join-Path $Root $_ }

foreach ($Source in $Sources) {
    if (-not (Test-Path $Source)) {
        throw "Source absente : $Source"
    }
}

$Arguments = @(
    "--metadata-file=$MetadataFile",
    "--from=markdown+yaml_metadata_block",
    "--lua-filter=$FilterFile",
    "--toc",
    "--number-sections",
    "--pdf-engine=xelatex",
    "--resource-path=$Root",
    "--output=$OutputFile"
) + $Sources

Write-Host "Construction de $OutputFile"
& pandoc @Arguments

if ($LASTEXITCODE -ne 0) {
    throw "Pandoc a échoué avec le code $LASTEXITCODE."
}

Write-Host "PDF généré : $OutputFile"
