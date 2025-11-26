# loader.py
import importlib
import pkgutil
import sys
from pathlib import Path
from typing import List
from registry import get_registry, register_plugin

def discover_plugins_from_package(package_name: str):
    """
    Import all submodules in the package and rely on them to register.
    Example: package_name='plugins' (a local package)
    """
    package = importlib.import_module(package_name)
    pkgpath = package.__path__  # type: ignore
    for _, modname, ispkg in pkgutil.iter_modules(pkgpath):
        fullname = f"{package_name}.{modname}"
        if fullname in sys.modules:
            importlib.reload(sys.modules[fullname])
        else:
            importlib.import_module(fullname)

def discover_plugins_from_path(path: Path, package_prefix: str = "plugins"):
    """
    Add path to sys.path and import modules under package_prefix.
    Useful for dynamic plugin directories.
    """
    path = str(path.resolve())
    if path not in sys.path:
        sys.path.insert(0, path)
    discover_plugins_from_package(package_prefix)

def list_registered_plugins():
    reg = get_registry()
    return reg.all()
