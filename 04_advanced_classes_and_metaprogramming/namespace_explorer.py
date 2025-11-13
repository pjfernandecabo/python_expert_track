

def class_factory(name, base_classes=(), attributes=None):
    """
    Crea una clase dinámica mostrando el proceso de construcción paso a paso.
    """
    attributes = attributes or {}

    print(f"\n🧩 Creando clase dinámica '{name}'...")
    print(f"Bases: {base_classes}")
    print("Atributos iniciales:")
    for k, v in attributes.items():
        print(f"  {k}: {v}")

    # Crear la clase usando type()
    new_class = type(name, base_classes, attributes)

    print(f"\n✅ Clase '{name}' creada con éxito:")
    print("Namespace (__dict__) de la clase:")
    for k, v in new_class.__dict__.items():
        print(f"  {k}: {v}")

    print("\n--- Fin de creación ---\n")
    return new_class


# Ejemplo de uso exploratorio
if __name__ == "__main__":
    # Definimos algunos atributos y métodos
    attrs = {
        "species": "Human",
        "__repr__": lambda self: f"<{self.__class__.__name__} {self.__dict__}>",
        "speak": lambda self: "Hola desde speak()!"
    }

    # Crear una clase Person
    Person = class_factory("Person", (), attrs)

    # Instanciamos un objeto
    p = Person()
    p.name = "Pedro"
    p.age = 38

    print("Objeto instanciado:", p)
    print("Namespace del objeto (__dict__):", p.__dict__)
    print("Namespace de la clase (__dict__):", Person.__dict__)

    print("\n🔍 Comprobando acceso a los métodos:")
    print("¿Tiene 'speak'? ->", hasattr(p, "speak"))
    print("Resultado de p.speak():\n", p.speak())
    
    # Añadir un método dinámicamente
    def custom_method(self):
        return f"{self.name} está corriendo!"

    p.run = custom_method.__get__(p)  # Enlaza la función como método bound
    print(p.run())  # "Pedro está corriendo!"