# asyncdjangoorm/utils/settings_loader.py
import importlib.util
import os
import sys
from pathlib import Path

def load_settings_module():
    """
    Returns the imported settings module for the current project.
    Lookup order:
      1) ASYNCDJANGO_SETTINGS_MODULE env var (module path like "myproj.settings")
      2) find nearest settings.py in cwd or parent folders
    Raises RuntimeError if not found.
    """
    env = os.getenv("ASYNCDJANGO_SETTINGS_MODULE")
    if env:
        return __import__(env, fromlist=["*"])

    cwd = Path.cwd()
    for p in [cwd] + list(cwd.parents):
        settings_py = p / "settings.py"
        if settings_py.exists():
            name = f"_asyncdjango_settings_{p.name}"
            spec = importlib.util.spec_from_file_location(name, str(settings_py))
            module = importlib.util.module_from_spec(spec)
            sys.modules[name] = module
            spec.loader.exec_module(module)
            # attach path info used later
            module.__file__ = str(settings_py)
            return module

    raise RuntimeError("Could not find settings.py. Set ASYNCDJANGO_SETTINGS_MODULE or run from project root.")
