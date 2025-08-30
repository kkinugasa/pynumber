# Ensure src layout is importable when running tests without installation
import os
import sys

ROOT = os.path.dirname(os.path.dirname(__file__))
src_path = os.path.join(ROOT, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)
