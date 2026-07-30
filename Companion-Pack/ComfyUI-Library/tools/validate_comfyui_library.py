from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

FORBIDDEN_SUFFIXES = {".safetensors",".ckpt",".pt",".pth",".bin",".onnx",".gguf",".zip",".7z",".tar",".gz"}
FORBIDDEN_DIRS = {"__pycache__",".venv","venv","node_modules",".git"}
SECRET_PATTERNS = [r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY", r"ghp_[A-Za-z0-9]{20,}", r"sk-[A-Za-z0-9]{20,}"]

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    errors = []
    required = [
        "README.md","VERSION","CHANGELOG.md","LICENSE-STATUS.md","DEPENDENCIES.json","PROVENANCE.json",
        "manifest.json","catalog.json","checksums.json","manifests/comfyui.yaml",
        "manifests/models/MODELS.yaml","manifests/custom-nodes/CUSTOM-NODES.yaml",
        "manifests/workflows/WF-COMFY-0001.yaml","manifests/workflows/WF-COMFY-0100.yaml",
        "workflows/source/WF-COMFY-0001-validation-copy.json",
        "workflows/api/WF-COMFY-0001-validation-copy.json",
        "workflows/source/WF-COMFY-0100-concept-art-template.json",
        "presets/cpu.yaml","presets/amd.yaml","presets/quality.yaml",
        "docs/BOUNDARIES.md","docs/INTEGRATION.md","docs/MANIFESTS.md","docs/RUNTIME-QUALIFICATION.md","docs/SECURITY.md",
        "validation/reference/WF-COMFY-0001-preview.svg",
        "tools/png_utils.py","tools/make_validation_input.py","tools/run_validation_workflow.py",
        "tools/validate_comfyui_library.py","scripts/run_cpu.sh","scripts/run_cpu.ps1",
        "python/tests/test_pack.py","qa/AUDIT-COMFYUI-LIBRARY.md","qa/VALIDATION-COMFYUI-LIBRARY.yaml"
    ]
    for rel in required:
        if not (root/rel).is_file(): errors.append(f"missing:{rel}")
    version=(root/"VERSION").read_text(encoding="utf-8").strip()
    manifest=load_json(root/"manifest.json")
    catalog=load_json(root/"catalog.json")
    checksums=load_json(root/"checksums.json")
    if manifest.get("version") != version: errors.append("manifest-version-mismatch")
    if catalog.get("pack_version") != version: errors.append("catalog-version-mismatch")
    if catalog.get("workflows") != ["WF-COMFY-0001","WF-COMFY-0100"]: errors.append("catalog-workflow-order")
    wf1=load_json(root/"manifests/workflows/WF-COMFY-0001.yaml")
    wf2=load_json(root/"manifests/workflows/WF-COMFY-0100.yaml")
    if wf1.get("status") not in {"accepted","candidate"}: errors.append("wf1-status")
    if wf1.get("models") != [] or wf1.get("custom_nodes") != []: errors.append("wf1-must-be-model-free")
    if wf2.get("status") != "review": errors.append("wf2-must-remain-review")
    if wf2.get("backend",{}).get("executed") is not False: errors.append("wf2-execution-claim")
    api=load_json(root/wf1["api_workflow"])
    if {node.get("class_type") for node in api.values()} != {"LoadImage","SaveImage"}: errors.append("validation-node-set")
    ui=load_json(root/wf1["source_workflow"])
    if {node.get("type") for node in ui.get("nodes",[])} != {"LoadImage","SaveImage"}: errors.append("validation-ui-node-set")
    concept=load_json(root/wf2["source_workflow"])
    expected={"CheckpointLoaderSimple","CLIPTextEncode","EmptyLatentImage","KSampler","VAEDecode","SaveImage"}
    if not expected.issubset({node.get("type") for node in concept.get("nodes",[])}): errors.append("concept-template-node-set")
    models=load_json(root/"manifests/models/MODELS.yaml")
    for model in models.get("models",[]):
        if model.get("redistribution") != "excluded": errors.append("model-not-excluded")
        if model.get("status") == "accepted" and not model.get("sha256"): errors.append("accepted-model-without-hash")
    custom=load_json(root/"manifests/custom-nodes/CUSTOM-NODES.yaml")
    if custom.get("installation_policy",{}).get("automatic") is not False: errors.append("automatic-custom-node-install")
    actual_files=[]
    for path in sorted(root.rglob("*")):
        rel=path.relative_to(root)
        if any(part in FORBIDDEN_DIRS for part in rel.parts):
            errors.append(f"forbidden-directory:{rel}"); continue
        if not path.is_file(): continue
        actual_files.append(rel.as_posix())
        if path.suffix.lower() in FORBIDDEN_SUFFIXES: errors.append(f"forbidden-binary:{rel}")
        try: text=path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"non-utf8:{rel}"); continue
        for pattern in SECRET_PATTERNS:
            if re.search(pattern,text): errors.append(f"possible-secret:{rel}")
    for rel,digest in checksums.get("files",{}).items():
        path=root/rel
        if not path.is_file(): errors.append(f"checksum-missing-file:{rel}")
        elif hashlib.sha256(path.read_bytes()).hexdigest()!=digest: errors.append(f"checksum-mismatch:{rel}")
    report={"status":"success" if not errors else "failure","pack_version":version,"source_files":len(actual_files),"workflow_count":2,"runtime_workflows":1,"template_workflows":1,"profiles":3,"models_bundled":0,"custom_nodes_bundled":0,"errors":errors}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False))
    if not errors: print(f"COMFYUI_LIBRARY_STATIC: PASS ({len(actual_files)} files)")
    return 1 if errors else 0

if __name__=="__main__":
    raise SystemExit(main())
