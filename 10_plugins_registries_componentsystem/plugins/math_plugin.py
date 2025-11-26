# plugins/math_plugin.py
from registry import register_plugin

class MathPlugin:
    name = "math"
    version = "0.1.0"

    def setup(self, config):
        self.factor = config.get("factor", 1)

    def run(self, x, y):
        return (x + y) * self.factor

register_plugin(MathPlugin)
