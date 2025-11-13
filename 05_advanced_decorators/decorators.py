import time
from functools import wraps

def logger(func):
    """Log simple antes y después de una función."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Llamando a {func.__name__} con args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} retornó {result}")
        return result
    return wrapper


def timer(func):
    """Mide el tiempo de ejecución de una función."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"[TIMER] {func.__name__} tardó {elapsed:.2f} ms")
        return result
    return wrapper


def repeat(times=2):
    """Ejecuta una función varias veces."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                print(f"[REPEAT] Ejecución {i+1}/{times}")
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator


def validate_args(expected_type):
    """Valida que todos los args sean de un tipo concreto."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not all(isinstance(a, expected_type) for a in args):
                raise TypeError(f"Todos los argumentos deben ser {expected_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
