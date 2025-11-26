# plugin_base.py
from typing import Protocol, Dict, Any

class PluginSpec(Protocol):
    """
    Protocol (interface) that plugins must implement.
    Using Protocol allows structural typing (duck-typing).
    """
    name: str
    version: str

    def setup(self, config: Dict[str, Any]) -> None:
        """Called once when plugin is loaded."""
        ...

    def run(self, **kwargs) -> Any:
        """Execute plugin work. Should be idempotent if possible."""
        ...
