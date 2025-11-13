"""
Dynamic Class Factory
---------------------
Crea clases en tiempo de ejecución con atributos y métodos personalizados.
"""

def class_factory(name, attributes=None, methods=None):
    """
    Crea una clase dinámica con los atributos y métodos proporcionados.
    """
    attributes = attributes or {}
    methods = methods or {}

    # carga todos los atributos dinamicamente
    def auto_init(self, **kwargs):
        # Copiar atributos de clase
        for key, val in attributes.items():
            setattr(self, key, val)
        # Asignar los pasados por kwargs
        for key, val in kwargs.items():
            setattr(self, key, val)

    # Si no se define un __init__, añadimos el automático
    if "__init__" not in methods:
        methods["__init__"] = auto_init

    # Combinar atributos y métodos en un solo diccionario
    namespace = {**attributes, **methods}

    # Crear la clase usando type()
    return type(name, (object,), namespace)


# Ejemplo de clase con __repr__ personalizado
def pretty_repr(self):
    return f"Class Name :<{self.__class__.__name__}> and __dict__: <{self.__dict__}>"
