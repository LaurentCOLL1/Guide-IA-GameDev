from __future__ import annotations
import argparse
import hashlib
import json
import time
import urllib.error
import urllib.request
from pathlib import Path
from png_utils import assert_comfy_metadata

def request_json(url: str, payload: dict | None = None) -> dict:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=data, headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(request, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))

def wait_ready(base_url: str, timeout: float) -> dict:
    deadline = time.monotonic() + timeout
    last = None
    while time.monotonic() < deadline:
        try:
            return request_json(base_url + "/system_stats")
        except (OSError, urllib.error.URLError, json.JSONDecodeError) as exc:
            last = exc
            time.sleep(1)
    raise TimeoutError(f"ComfyUI did not become ready: {last}")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://127.0.0.1:8188")
    parser.add_argument("--api-workflow", type=Path, required=True)
    parser.add_argument("--ui-workflow", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--timeout", type=float, default=180.0)
    args = parser.parse_args()

    system_stats = wait_ready(args.base_url, args.timeout)
    object_info = request_json(args.base_url + "/object_info")
    required = {"LoadImage", "SaveImage"}
    missing = sorted(required - set(object_info))
    if missing:
        raise RuntimeError("missing built-in nodes: " + ", ".join(missing))

    prompt = json.loads(args.api_workflow.read_text(encoding="utf-8"))
    workflow = json.loads(args.ui_workflow.read_text(encoding="utf-8"))
    payload = {
        "prompt": prompt,
        "client_id": "guide-ia-gamedev-pack-06",
        "extra_data": {"extra_pnginfo": {"workflow": workflow}},
    }
    queued = request_json(args.base_url + "/prompt", payload)
    prompt_id = queued["prompt_id"]
    deadline = time.monotonic() + args.timeout
    history = {}
    while time.monotonic() < deadline:
        history = request_json(args.base_url + f"/history/{prompt_id}")
        if prompt_id in history:
            break
        time.sleep(1)
    else:
        raise TimeoutError("workflow execution timeout")

    entry = history[prompt_id]
    if entry.get("status", {}).get("status_str") != "success":
        raise RuntimeError(json.dumps(entry.get("status", {}), ensure_ascii=False))
    images = []
    for node_output in entry.get("outputs", {}).values():
        images.extend(node_output.get("images", []))
    if len(images) != 1:
        raise RuntimeError(f"expected exactly one image, received {len(images)}")
    item = images[0]
    output_path = (args.output_root / item.get("subfolder", "") / item["filename"]).resolve()
    output_path.relative_to(args.output_root.resolve())
    if not output_path.is_file():
        raise FileNotFoundError(output_path)
    metadata = assert_comfy_metadata(output_path)
    digest = hashlib.sha256(output_path.read_bytes()).hexdigest()
    report = {
        "status":"success",
        "prompt_id":prompt_id,
        "required_nodes":sorted(required),
        "output":str(output_path),
        "sha256":digest,
        "size_bytes":output_path.stat().st_size,
        "metadata_keys":sorted(metadata),
        "system_stats_recorded":bool(system_stats),
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
