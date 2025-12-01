import importlib
import pkgutil
from typing import Protocol, List


# Interfaz que todo plugin debe implementar
class Plugin(Protocol):
    name: str
    def process(self, text: str) -> str: ...


# Cargar plugins dinámicamente
def load_plugins() -> List[Plugin]:
    plugins = []
    package = "plugins"
    print(f"Cargando plugins desde el paquete '{package}'")

    for _, module_name, _ in pkgutil.iter_modules([package]):
        module = importlib.import_module(f"{package}.{module_name}")

        # Cada módulo debe definir la variable 'plugin'
        if hasattr(module, "plugin"):
            plugins.append(module.plugin)
            
    print(f"Total plugins cargados: {len(plugins)}")        
    return plugins


if __name__ == "__main__":
    plugins = load_plugins()

    for p in plugins:
        print(f"Plugin cargado → {p.name}")
        print("Resultado:", p.process("hola pedro"))
