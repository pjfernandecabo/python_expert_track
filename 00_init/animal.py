class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        return f"{self.nombre} hace un sonido."

a = Animal("Perro")
print(a.__class__)
print(type(a))
print(isinstance(a, Animal))
print(dir(a))
print(id(a))


# Así se crea una clase dinámicamente
MyClass = type("MyClass", (object,), {"x": 42, "saludar": lambda self: "Hola"})
obj = MyClass()

'''
# Equivalente a:
class MyClass(object):
    x = 42
    def saludar(self):
        return "Hola"
'''

print(obj.x, obj.saludar())


# vemos el bytecode generado
import dis
def suma(a, b): return a + b
dis.dis(suma)

# y el AST (Abstract Syntax Tree)
import ast, inspect
tree = ast.parse(inspect.getsource(suma))
print(ast.dump(tree, indent=4))
