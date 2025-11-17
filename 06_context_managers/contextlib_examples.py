from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"[{name}] Inicializando recurso...")
    try:
        yield f"Recurso-{name}"
    finally:
        print(f"[{name}] Liberando recurso...")

@contextmanager
def suppress_errors(*exceptions):
    try:
        yield
    except exceptions as e:
        print(f"Suprimida excepción: {e}")
