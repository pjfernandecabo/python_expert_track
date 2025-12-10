import time
from sensors import Sensor, SensorManager
from analytics import AnalyticsEngine

def main():
    print("🤖 Iniciando Protocolo de Arranque del NeuroBot v1.0")

    # 1. Configuración de Sensores (I/O Bound -> Threading)
    sensor_mgr = SensorManager()
    sensor_mgr.add_sensor(Sensor("Lidar", 1.0))
    sensor_mgr.add_sensor(Sensor("Termico", 2.5))

    # 2. Arrancar hilos de sensores (no bloquean el main thread)
    sensor_mgr.start_all()

    # Dejamos que los sensores trabajen un poco mientras el robot "hace otras cosas"
    print("\n... El robot está 'pensando' mientras los sensores recogen datos ...")
    time.sleep(3)

    # 3. Ejecutar Tarea Pesada (CPU Bound -> Multiprocessing)
    # Imaginemos que hemos acumulado 10 lotes de datos para procesar
    data_payload = [100] * 8  # 8 tareas pesadas

    engine = AnalyticsEngine()

    # El procesamiento pesado ocurre en paralelo en otros núcleos
    # Nota: En una app real, esto podría ser async o en background,
    # pero aquí bloquearemos el main thread para ver el resultado,
    # ¡sin embargo, los sensores siguen reportando en sus hilos!
    results = engine.process_data_parallel(data_payload)

    print(f"📊 Resultado del análisis: {results[:2]}... (total {len(results)})")

    # Dejamos correr un poco más
    time.sleep(2)

    # 4. Apagar
    sensor_mgr.stop_all()
    print("🤖 NeuroBot apagado correctamente.")

if __name__ == "__main__":
    # Protección necesaria para multiprocessing en Windows/macOS,
    # buena práctica siempre en Python.
    main()
