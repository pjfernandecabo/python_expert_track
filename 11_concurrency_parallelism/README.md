# Lección 11: Concurrencia y Paralelismo — El Motor de la Robótica 🤖

¡Bienvenido al Nivel Pro!

En esta lección entramos en el mundo de la **ejecución simultánea**. Si quieres construir robots, procesar Big Data o manejar miles de conexiones web, no puedes vivir en un mundo "single-threaded".

## 🧠 Teoría: ¿Por qué mi código es lento?

### 1. El mito de la multitarea
Python tiene un "guardián" llamado **GIL (Global Interpreter Lock)**. Este cerrojo asegura que solo un hilo (thread) ejecute código Python a la vez dentro de un mismo proceso.

*   **¿Entonces los Threads no sirven?** ¡Sí sirven! Pero solo para tareas **I/O Bound** (esperar red, esperar disco, esperar input de usuario). Mientras un hilo espera, suelta el GIL y otro puede trabajar.
*   **¿Y si quiero usar todos los núcleos de mi CPU?** Necesitas **Multiprocessing**. Al crear nuevos procesos, cada uno tiene su propia instancia de Python y su propio GIL. ¡Libertad real!

### 2. Threading vs Multiprocessing (Regla de Oro)

| Herramienta | Tipo de Tarea | Ejemplo Robótica/Data | Coste de Memoria |
| :--- | :--- | :--- | :--- |
| **Threading** | **I/O Bound** (Esperar) | Leer sensores, peticiones HTTP, DB queries | Bajo (comparten memoria) |
| **Multiprocessing** | **CPU Bound** (Calcular) | Procesar visión por computador, ML training | Alto (memoria separada) |

---

## 🧰 Hands-On: Simulador de Robot "NeuroBot"

Vamos a construir el núcleo de un robot que necesita hacer dos cosas a la vez:
1.  **Leer Sensores (I/O Bound):** Simulado con `time.sleep()`. Usaremos **Threads** para no bloquear el sistema.
2.  **Analizar Datos (CPU Bound):** Cálculos matemáticos pesados. Usaremos **Multiprocessing** para no congelar los sensores.

### Estructura del Proyecto

*   `sensors.py`: Módulo de lectura de sensores (Threading).
*   `analytics.py`: Módulo de procesamiento pesado (Multiprocessing).
*   `robot.py`: El cerebro que coordina todo.
*   `benchmark_gil.py`: **Test Ninja** para demostrar la supremacía de los Procesos en CPU bound.

---

## 🧪 Test Ninja (Benchmark)

Ejecuta `python benchmark_gil.py` para ver con tus propios ojos cómo el GIL afecta el rendimiento.

## 🚀 Ejecución del Robot

Ejecuta `python robot.py` para ver el sistema en acción.
