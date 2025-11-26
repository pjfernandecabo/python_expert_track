# plugins/hello_plugin.py
from plugin_base import PluginSpec
from registry import register_plugin

class HelloPlugin:
    name = "hello"
    version = "1.0.0"

    def setup(self, config):
        self.prefix = config.get("prefix", "Hello")

    def run(self, name="world"):
        return f"{self.prefix}, {name}!"

# register class (decorator returns it)
register_plugin(HelloPlugin)
