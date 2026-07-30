[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("solo", "studio")]
    [string]$Profile,

    [Parameter(Mandatory = $true)]
    [string]$ProjectName,

    [Parameter(Mandatory = $true)]
    [string]$ProjectId,

    [Parameter(Mandatory = $true)]
    [string]$OwnerHandle,

    [Parameter(Mandatory = $true)]
    [string]$Output,

    [switch]$Force
)

$ErrorActionPreference = "Stop"
$script = Join-Path $PSScriptRoot "instantiate_project.py"
$arguments = @(
    $script,
    "--profile", $Profile,
    "--project-name", $ProjectName,
    "--project-id", $ProjectId,
    "--owner-handle", $OwnerHandle,
    "--output", $Output
)
if ($Force) {
    $arguments += "--force"
}

python @arguments
if ($LASTEXITCODE -ne 0) {
    throw "Project template instantiation failed with exit code $LASTEXITCODE."
}
