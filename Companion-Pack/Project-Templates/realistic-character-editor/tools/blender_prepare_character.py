"""Prepare a selected Blender mesh for Asteria Character Studio.

Run from Blender's Scripting workspace with one body mesh selected.
The script creates the expected shape-key names as empty copies of Basis.
Artists must sculpt and validate every target before export.
"""

from __future__ import annotations

import json
from pathlib import Path

import bpy

SIGNED_TARGETS = {
    "stature": ("morph_stature_neg", "morph_stature_pos"),
    "head_scale": ("morph_head_small", "morph_head_large"),
    "shoulder_width": ("morph_shoulders_narrow", "morph_shoulders_wide"),
    "chest_volume": ("morph_chest_small", "morph_chest_large"),
    "waist_width": ("morph_waist_narrow", "morph_waist_wide"),
    "hip_width": ("morph_hips_narrow", "morph_hips_wide"),
    "torso_length": ("morph_torso_short", "morph_torso_long"),
    "arm_length": ("morph_arms_short", "morph_arms_long"),
    "leg_length": ("morph_legs_short", "morph_legs_long"),
    "muscle_mass": ("morph_muscle_low", "morph_muscle_high"),
    "adipose_mass": ("morph_adipose_low", "morph_adipose_high"),
    "hand_scale": ("morph_hands_small", "morph_hands_large"),
    "foot_scale": ("morph_feet_small", "morph_feet_large"),
    "jaw_width": ("morph_jaw_narrow", "morph_jaw_wide"),
    "nose_scale": ("morph_nose_small", "morph_nose_large"),
    "eye_spacing": ("morph_eyes_close", "morph_eyes_wide"),
}

AGE_TARGETS = (
    "age_infant",
    "age_early_childhood",
    "age_childhood",
    "age_adolescence",
    "age_young_adult",
    "age_mature_adult",
    "age_elder",
)


def require_active_mesh() -> bpy.types.Object:
    obj = bpy.context.active_object
    if obj is None or obj.type != "MESH":
        raise RuntimeError("Select one active body mesh before running the script.")
    if obj.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
    return obj


def ensure_shape_key(obj: bpy.types.Object, name: str) -> bool:
    keys = obj.data.shape_keys
    if keys and name in keys.key_blocks:
        return False
    obj.shape_key_add(name=name, from_mix=False)
    return True


def write_manifest(obj: bpy.types.Object, created: list[str]) -> Path:
    blend_path = Path(bpy.data.filepath) if bpy.data.filepath else Path.cwd() / "untitled.blend"
    output = blend_path.parent / "character_morph_manifest.json"
    payload = {
        "schema_version": 1,
        "object_name": obj.name,
        "mesh_name": obj.data.name,
        "vertex_count": len(obj.data.vertices),
        "polygon_count": len(obj.data.polygons),
        "signed_targets": SIGNED_TARGETS,
        "age_targets": AGE_TARGETS,
        "created_shape_keys": created,
        "warning": "Shape keys are empty scaffolds until sculpted and validated.",
    }
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return output


def main() -> None:
    obj = require_active_mesh()
    created: list[str] = []

    if obj.data.shape_keys is None:
        obj.shape_key_add(name="Basis", from_mix=False)
        created.append("Basis")

    for negative, positive in SIGNED_TARGETS.values():
        if ensure_shape_key(obj, negative):
            created.append(negative)
        if ensure_shape_key(obj, positive):
            created.append(positive)

    for target in AGE_TARGETS:
        if ensure_shape_key(obj, target):
            created.append(target)

    obj["asteria_character_contract"] = "CP-PT-REALISTIC-CHARACTER-EDITOR"
    obj["asteria_shape_key_count_expected"] = 39
    obj["asteria_minor_representation_policy"] = "non-explicit-and-covered"

    manifest_path = write_manifest(obj, created)
    print(
        "ASTERIA_CHARACTER_PREPARED",
        {
            "object": obj.name,
            "created": len(created),
            "manifest": str(manifest_path),
        },
    )


if __name__ == "__main__":
    main()
