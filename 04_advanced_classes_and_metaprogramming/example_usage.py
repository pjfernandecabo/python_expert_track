from class_factory import class_factory, pretty_repr

#def init_person(self, name, age):
#    self.info = {"name": name, "age": age}
    #self.species = self.__class__.species

# Crear clase dinámica
Person = class_factory(
    name="Person",
    attributes={"species": "Homo sapiens"},
    methods={
        "__repr__": pretty_repr,
        "greet": lambda self: print(f"Hola, soy {self.name} y tengo {self.age} años."),
    }
)

p = Person(name="Pedro", age=38)
p.greet()
print(p)


# --- Ejemplo 2: Clase Vehicle con métodos personalizados ---
def describe(self):
    print(f"🚗 {self.brand} {self.model} ({self.year}) - {self.type}")

Vehicle = class_factory(
    name="Vehicle",
    attributes={"type": "transporte terrestre"},
    methods={
        "__repr__": pretty_repr,
        "describe": describe
    }
)

v1 = Vehicle(brand="Tesla", model="Model Y", year=2024)
v1.describe()
print(v1)


# --- Ejemplo 3: Clase Animal con comportamiento dinámico ---
def speak(self):
    sounds = {"dog": "guau", "cat": "miau", "cow": "muuu"}
    print(f"El {self.species} dice '{sounds.get(self.species, '???')}'")

Animal = class_factory(
    name="Animal",
    attributes={"kingdom": "Animalia"},
    methods={
        "__repr__": pretty_repr,
        "speak": speak
    }
)

a1 = Animal(species="dog", age=3)
a2 = Animal(species="cow", age=7)
a3 = Animal(species="unicorn", age=100)

for a in [a1, a2, a3]:
    a.speak()
    print(f"\nAtributos del objeto: {a.__dict__}")
    print(f"\nClaves de la clase: {a.__class__.__dict__.keys()}")
    print(f"\nClaves de la clase Animal: {Animal.__dict__.keys()}")
    print(f"\nClaves de la clase Animal: {Animal.__dict__}")