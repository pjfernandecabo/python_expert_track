# registry.py
from typing import Dict, Type, Any
from dataclasses import dataclass

@dataclass
class PluginMeta:
    name: str
    version: str
    module: str
    obj: Any

class PluginRegistry:
    def __init__(self):
        self._registry: Dict[str, PluginMeta] = {}

    def register(self, name: str, version: str, module: str, obj: Any):
        key = f"{name}:{version}"
        if key in self._registry:
            raise KeyError(f"Plugin {key} already registered")
        self._registry[key] = PluginMeta(name, version, module, obj)

    def get(self, name: str, version: str = None):
        if version:
            return self._registry.get(f"{name}:{version}")
        # fallback: return latest version for name
        candidates = [m for m in self._registry.values() if m.name == name]
        if not candidates:
            return None
        # simple version selection: lexicographic (recommend semantic versioning compare in prod)
        candidates.sort(key=lambda m: m.version, reverse=True)
        return candidates[0]

    def all(self):
        return list(self._registry.values())

# convenience decorator for plugins to register themselves
_registry = PluginRegistry()

def register_plugin(obj):
    """
    Decorator to register plugin classes/instances.
    Plugin must have .name and .version attributes.
    """
    name = getattr(obj, "name", None)
    version = getattr(obj, "version", None)
    module = getattr(obj, "__module__", "<unknown>")
    if not name or not version:
        raise ValueError("Plugin must declare 'name' and 'version' attributes")
    _registry.register(name, version, module, obj)
    return obj

def get_registry():
    return _registry
