def mi_decorador(func):
    def envoltura(*args, **kwargs):
        print("Antes de ejecutar la función")
        resultado = func(*args, **kwargs)
        print("Después de ejecutar la función")
        return resultado
    return envoltura

@mi_decorador
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Pedro")


##################
def repetir_veces(n):
    def decorador(func):
        def envoltura(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return envoltura
    return decorador

@repetir_veces(3)
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Pedro")

##################
def mayusculas(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

def exclamacion(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!!!"
    return wrapper

@exclamacion
@mayusculas
def saludo(nombre):
    return f"Hola {nombre}"

print(saludo("Pedro"))

#####################
class Recurso:
    def __enter__(self):
        print("Entrando al recurso")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saliendo del recurso")
        if exc_type:
            print(f"Ocurrió un error: {exc_val}")
        return True  # suprime la excepción

with Recurso() as r:
    print("Usando el recurso")
    raise ValueError("Prueba")

#######################
from contextlib import contextmanager

@contextmanager
def mi_recurso():
    print("Entrando")
    yield "valor"
    print("Saliendo")

with mi_recurso() as v:
    print(f"Usando {v}")
