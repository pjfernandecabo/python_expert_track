import time
from functools import wraps

# ------------------------------------------------------
# LOG DECORATOR
# ------------------------------------------------------
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Llamando a {func.__name__} con args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Resultado: {result}")
        return result
    return wrapper


# ------------------------------------------------------
# TIMER DECORATOR
# ------------------------------------------------------
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} tardó {end - start:.6f}s")
        return result
    return wrapper


# ------------------------------------------------------
# REPEAT DECORATOR FACTORY
# ------------------------------------------------------
def repeat(n_times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


# ------------------------------------------------------
# VALIDATE ARGS DECORATOR FACTORY
# ------------------------------------------------------
def validate_args(types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg, expected in zip(args[1:], types):  
                if not isinstance(arg, expected):
                    raise TypeError(f"Argumento {arg!r} debe ser {expected}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
