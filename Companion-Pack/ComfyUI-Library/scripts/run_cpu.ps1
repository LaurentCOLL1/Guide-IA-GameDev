$ErrorActionPreference = "Stop"
if (-not $env:COMFYUI_ROOT) {
    throw "Définir COMFYUI_ROOT vers le checkout ComfyUI épinglé."
}
$inputDir = if ($env:COMFYUI_INPUT) { $env:COMFYUI_INPUT } else { Join-Path $env:COMFYUI_ROOT "input" }
$outputDir = if ($env:COMFYUI_OUTPUT) { $env:COMFYUI_OUTPUT } else { Join-Path $env:COMFYUI_ROOT "output" }
$userDir = if ($env:COMFYUI_USER) { $env:COMFYUI_USER } else { Join-Path $env:COMFYUI_ROOT "user" }
python (Join-Path $env:COMFYUI_ROOT "main.py") `
  --cpu `
  --listen 127.0.0.1 `
  --port 8188 `
  --input-directory $inputDir `
  --output-directory $outputDir `
  --user-directory $userDir
