import time
import threading
import multiprocessing
import math

def heavy_computation():
    """Calcula suma de potencias, tarea puramente de CPU."""
    count = 0
    for i in range(10**6):
        count += math.pow(i, 2)
    return count

def run_threads(n_tasks):
    print(f"🧵 Ejecutando {n_tasks} tareas con THREADS...")
    start = time.time()
    threads = []
    for _ in range(n_tasks):
        t = threading.Thread(target=heavy_computation)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    return time.time() - start

def run_processes(n_tasks):
    print(f"🏭 Ejecutando {n_tasks} tareas con PROCESOS...")
    start = time.time()
    processes = []
    for _ in range(n_tasks):
        p = multiprocessing.Process(target=heavy_computation)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    return time.time() - start

if __name__ == "__main__":
    TASKS = 4 # Número de tareas concurrentes
    print("--- ⚔️  BENCHMARK: GIL vs MULTIPROCESSING ⚔️  ---")
    print(f"Tareas: {TASKS} cálculos pesados.")

    # 1. Test secuencial (Línea base)
    print(f"🐌 Ejecutando secuencialmente (Línea Base)...")
    start = time.time()
    for _ in range(TASKS):
        heavy_computation()
    time_seq = time.time() - start
    print(f"⏱️  Tiempo Secuencial: {time_seq:.4f}s\n")

    # 2. Test Threading
    time_threads = run_threads(TASKS)
    print(f"⏱️  Tiempo Threads: {time_threads:.4f}s")
    print("   (Nota: Si es similar o peor que secuencial, es culpa del GIL)\n")

    # 3. Test Multiprocessing
    time_processes = run_processes(TASKS)
    print(f"⏱️  Tiempo Procesos: {time_processes:.4f}s")

    # Conclusión
    improvement = time_threads / time_processes
    print("-" * 40)
    print(f"🏆 GANADOR: {'PROCESOS' if time_processes < time_threads else 'THREADS'}")
    print(f"🚀 Factor de aceleración: {improvement:.2f}x más rápido")
    print("-" * 40)
