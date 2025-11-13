from functools import wraps

print("=== DECORATOR EXPLORER ===\n")

# =====================================================
# 1️⃣ DECORADOR SIMPLE (sin parámetros)
# =====================================================
def simple_decorator(func):
    print(f"[simple_decorator] Recibí la función: {func.__name__}")

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[wrapper] Antes de ejecutar {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[wrapper] Después de ejecutar {func.__name__}")
        return result

    return wrapper


@simple_decorator
def saludo(nombre):
    """Función de saludo simple"""
    print(f"Hola, {nombre}!")
    return len(nombre)


print("\n--- Ejecutando saludo('Pedro') ---")
saludo("Pedro")
print(f"Nombre interno: {saludo.__name__}")
print(f"Docstring: {saludo.__doc__}")


# =====================================================
# 2️⃣ DECORADOR PARAMETRIZABLE (con argumentos)
# =====================================================
def repeat(times=2):
    print(f"[repeat] Configurando decorador con times={times}")

    def decorator(func):
        print(f"[repeat.decorator] Recibí la función: {func.__name__}")

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[repeat.wrapper] Ejecutando {func.__name__} {times} veces:")
            results = []
            for i in range(times):
                print(f"   → Iteración {i+1}")
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator


@repeat(times=3)
def di_hola(nombre):
    print(f"Hola, {nombre}!")
    return nombre.upper()


print("\n--- Ejecutando di_hola('Lucía') ---")
di_hola("Lucía")


# =====================================================
# 3️⃣ SIN @wraps: cómo se pierden los metadatos
# =====================================================
def no_wraps_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@no_wraps_decorator
def despedida():
    """Función con docstring"""
    print("Adiós!")


print("\n--- Ejecutando despedida() ---")
despedida()
print(f"Nombre interno: {despedida.__name__}")
print(f"Docstring: {despedida.__doc__}")
