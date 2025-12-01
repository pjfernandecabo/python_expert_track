# hot_reload.py
import time
import importlib
import sys
from pathlib import Path

class PluginReloader:
    def __init__(self, package_path: Path, interval: float = 1.0):
        self.package_path = package_path
        self.interval = interval
        self._mtimes = {}  # module -> last modification

    def track(self):
        plugin_files = list(self.package_path.glob("*.py"))
        for filepath in plugin_files:
            mod_name = f"plugins.{filepath.stem}"
            mtime = filepath.stat().st_mtime
            self._mtimes[mod_name] = mtime

    def watch(self, on_reload=None):
        """
        on_reload(module_name) se dispara cada vez que un módulo es recargado.
        """
        print("[HOT-RELOAD] Watching plugin folder...")
        self.track()

        while True:
            time.sleep(self.interval)
            plugin_files = list(self.package_path.glob("*.py"))

            for filepath in plugin_files:
                mod_name = f"plugins.{filepath.stem}"
                mtime = filepath.stat().st_mtime

                if mod_name not in self._mtimes:
                    self._mtimes[mod_name] = mtime
                    continue

                if mtime > self._mtimes[mod_name]:
                    self._mtimes[mod_name] = mtime
                    print(f"[HOT-RELOAD] Detected change in {mod_name}")
                    self.reload_module(mod_name)
                    if on_reload:
                        on_reload(mod_name)

    def reload_module(self, mod_name):
        if mod_name in sys.modules:
            importlib.reload(sys.modules[mod_name])
        else:
            importlib.import_module(mod_name)
