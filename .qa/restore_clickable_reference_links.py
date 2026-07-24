#!/usr/bin/env python3
from pathlib import Path
import runpy
import traceback

try:
    runpy.run_path('.qa/restore_payload.py', run_name='__main__')
except Exception:
    Path('.qa/restore-error.log').write_text(traceback.format_exc(), encoding='utf-8')
