#!/usr/bin/env bash
set -euo pipefail
COMFYUI_ROOT="${COMFYUI_ROOT:?Set COMFYUI_ROOT to the pinned ComfyUI checkout}"
exec python "$COMFYUI_ROOT/main.py" --cpu --listen 127.0.0.1 --port 8188 --input-directory "${COMFYUI_INPUT:-$COMFYUI_ROOT/input}" --output-directory "${COMFYUI_OUTPUT:-$COMFYUI_ROOT/output}" --user-directory "${COMFYUI_USER:-$COMFYUI_ROOT/user}"
