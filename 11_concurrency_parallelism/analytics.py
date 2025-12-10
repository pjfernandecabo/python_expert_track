import multiprocessing
import time
import math

def cpu_heavy_task(data_chunk: int) -> int:
    """
    Simula una tarea intensiva de CPU (ej. análisis de imagen, cálculo matricial).
    Calcula la suma de factoriales (intencionalmente ineficiente para estresar la CPU).
    """
    result = 0
    # Aumentamos la complejidad para que se note el esfuerzo
    for i in range(1, 2000):
        result += math.factorial(i % 50)
    return result

class AnalyticsEngine:
    def __init__(self):
        pass

    def process_data_parallel(self, data_chunks: list[int]) -> list[int]:
        """
        Procesa una lista de datos utilizando múltiples procesos.
        Cada proceso tiene su propio intérprete de Python y GIL.
        """
        print(f"\n🧠 Iniciando Análisis Pesado con {multiprocessing.cpu_count()} núcleos...")
        start_time = time.time()

        # Pool de procesos: Python gestiona los workers automáticamente
        with multiprocessing.Pool() as pool:
            results = pool.map(cpu_heavy_task, data_chunks)

        duration = time.time() - start_time
        print(f"✅ Análisis completado en {duration:.4f} segundos.")
        return results

    def process_data_serial(self, data_chunks: list[int]) -> list[int]:
        """
        Procesa los datos secuencialmente (para comparar).
        """
        print("\n🐌 Iniciando Análisis Secuencial (un solo núcleo)...")
        start_time = time.time()
        results = [cpu_heavy_task(d) for d in data_chunks]
        duration = time.time() - start_time
        print(f"✅ Análisis completado en {duration:.4f} segundos.")
        return results
