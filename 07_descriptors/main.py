class Typed:
    def __init__(self, type_):
        self.type_ = type_
        self.private_name = None

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError(f"Se esperaba {self.type_.__name__}")
        setattr(instance, self.private_name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, None)

class Product:
    name = Typed(str)
    price = Typed(float)

p = Product()
p.name = "Manzana"
p.price = 2.99      # OK
#p.price = "hola"    # ERROR
print(f"Producto: {p.name}, Precio: {p.price}")
