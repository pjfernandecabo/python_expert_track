import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        print("⏱ Timer started.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end = time.time()
        print(f"⏱ Timer finished. Elapsed: {end - self.start:.4f}s")
        return False


class TemporaryVariable:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __enter__(self):
        globals()[self.name] = self.value
        print(f"Variable global '{self.name}' creada con valor {self.value}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        del globals()[self.name]
        print(f"Variable global '{self.name}' eliminada.")
