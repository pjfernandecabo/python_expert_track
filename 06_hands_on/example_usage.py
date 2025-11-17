from factory import create_resource_class
from decorators import repeat, validate_args
from resource_monitor import BaseResource

# ------------------------------------------------------
# Creamos dos clases dinámicas que heredan del BaseResource
# ------------------------------------------------------

CPUResource = create_resource_class(
    "CPUResource",
    monitored_fields=["usage", "temperature"]
)

MemoryResource = create_resource_class(
    "MemoryResource",
    monitored_fields=["used", "capacity"]
)

# Heredamos explícitamente para activar el registro por metaclase
class CPU(CPUResource, BaseResource):
    pass

class Memory(MemoryResource, BaseResource):
    pass


# ------------------------------------------------------
# Decoramos un método de usuario
# ------------------------------------------------------
class Operations:
    
    @repeat(3)
    @validate_args((int, int))
    def add(self, a, b):
        return a + b


# ------------------------------------------------------
# DEMOSTRACIÓN
# ------------------------------------------------------
if __name__ == "__main__":

    cpu = CPU(usage=20, temperature=40)
    mem = Memory(used=4096, capacity=8192)

    print("\n--- ESTADO INICIAL ---")
    print(cpu)
    print(mem)

    print("\n--- ACTUALIZANDO CPU ---")
    cpu.update(usage=45, temperature=55)
    cpu.update(usage=60)

    print("\n--- ACTUALIZANDO MEM ---")
    mem.update(used=5000)

    print("\n--- ESTADO FINAL ---")
    print(cpu)
    print(mem)

    print("\n--- OPERACIONES DECORADAS ---")
    ops = Operations()
    result = ops.add(10, 20)
    print(f"Resultado final (repeat=3): {result}")
