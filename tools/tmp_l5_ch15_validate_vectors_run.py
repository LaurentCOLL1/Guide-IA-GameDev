#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("tmp_l5_ch15_validate_vectors.py")
SPEC = importlib.util.spec_from_file_location("l5_ch15_vector_fixtures", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Impossible de charger les fixtures vectorielles.")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)
module.EXPECTED_CASES = 43

if __name__ == "__main__":
    raise SystemExit(module.main())
