#!/usr/bin/env python3
"""CI debugging script to print environment and version information"""

import importlib
import json
import os
import platform
import sys
from pathlib import Path


def main():
    """Print comprehensive CI environment debugging information"""
    print("=" * 60)
    print("CI ENVIRONMENT DEBUG INFORMATION")
    print("=" * 60)

    # Python and system info
    print("PY:", sys.version)
    print("OS:", platform.platform())
    print("CWD:", Path.cwd())
    print("PYTHON_PATH:", sys.path[:3] + ["..."] if len(sys.path) > 3 else sys.path)

    # Environment variables
    env_vars = {
        k: v
        for k, v in os.environ.items()
        if k
        in [
            "PYTHONUTF8",
            "TZ",
            "PIP_INDEX_URL",
            "PYTHONDONTWRITEBYTECODE",
            "CI",
            "GITHUB_ACTIONS",
        ]
    }
    print("ENV:", json.dumps(env_vars, indent=2))

    # Package versions
    print("\nPACKAGE VERSIONS:")
    print("-" * 30)
    for mod in ("pip", "setuptools", "wheel", "pytest", "build", "twine"):
        try:
            m = importlib.import_module(mod)
            version = getattr(m, "__version__", "n/a")
            print(f"{mod}: {version}")
        except Exception as e:
            print(f"{mod}: MISSING ({e})")

    # Additional debugging info
    print(f"\nPython executable: {sys.executable}")
    print(f"Platform: {sys.platform}")
    print(f"Architecture: {platform.machine()}")
    print(f"Processor: {platform.processor()}")

    # Check if we can import our package
    print("\nPACKAGE IMPORT TEST:")
    print("-" * 30)
    try:
        import dinoscan

        print(f"dinoscan: {dinoscan.__version__}")
        print(f"dinoscan location: {dinoscan.__file__}")
    except Exception as e:
        print(f"dinoscan: IMPORT FAILED ({e})")

    print("=" * 60)


if __name__ == "__main__":
    main()
