class ResourceRegistry(type):
    registry = {}

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        ResourceRegistry.registry[name] = cls
        print(f"[REGISTRY] Clase registrada: {name}")
        return cls


class BaseResource(metaclass=ResourceRegistry):
    """Clase base para todos los recursos monitorizados"""
    pass
