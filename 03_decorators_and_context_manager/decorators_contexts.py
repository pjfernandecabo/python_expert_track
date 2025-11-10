# Objetivo:

# Crear un decorador @log_time que mida el tiempo de ejecución de cualquier función.
# Crear un context manager que mida el tiempo de un bloque de código.
# Aplicar ambos para analizar funciones de ejemplo.

import time
from contextlib import contextmanager


# Decorador que mide tiempo
def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[{func.__name__}] Tiempo de ejecución: {end - start:.4f}s")
        return result
    return wrapper

# Context manager que mide tiempo
@contextmanager
def time_block(label="Bloque"):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"[{label}] Tiempo total: {end - start:.4f}s")

# Funciones de prueba
@log_time
def calcular_suma(n):
    return sum(range(n))

def main():
    print("Ejemplo con decorador:")
    calcular_suma(10_000_000)

    print("\nEjemplo con context manager:")
    with time_block("Suma de 1 a 10M"):
        sum(range(10_000_000))

if __name__ == "__main__":
    main()
