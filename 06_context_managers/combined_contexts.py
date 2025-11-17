from contextlib import ExitStack
from custom_resource import Timer
from file_context import FileManager

def combined_operations():
    with ExitStack() as stack:
        timer = stack.enter_context(Timer())
        file = stack.enter_context(FileManager("combined.txt", "w"))
        file.write("Operación dentro de múltiples contextos.\n")
        file.write(f"Tiempo inicial: {timer.start}\n")
