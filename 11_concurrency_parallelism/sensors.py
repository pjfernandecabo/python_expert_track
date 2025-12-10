import threading
import time
import random
from typing import List, Dict

class Sensor:
    def __init__(self, name: str, interval: float):
        self.name = name
        self.interval = interval
        self.running = False
        self.data: float = 0.0
        self._thread = threading.Thread(target=self._run_loop, name=f"Thread-{name}")

    def start(self):
        """Inicia la lectura del sensor en un hilo separado."""
        self.running = True
        print(f"🔌 Sensor {self.name} activado.")
        self._thread.start()

    def stop(self):
        """Detiene el sensor."""
        self.running = False
        self._thread.join()
        print(f"📴 Sensor {self.name} detenido.")

    def _run_loop(self):
        """Simula operación I/O bound (esperar datos)."""
        while self.running:
            # Simula tiempo de espera de I/O (lectura de hardware)
            time.sleep(self.interval)

            # Simula obtención de dato
            self.data = round(random.uniform(20.0, 30.0), 2)
            print(f"   [{self.name}] Dato leído: {self.data}")

class SensorManager:
    def __init__(self):
        self.sensors: List[Sensor] = []

    def add_sensor(self, sensor: Sensor):
        self.sensors.append(sensor)

    def start_all(self):
        print("\n--- Iniciando Sistema de Sensores (Threading) ---")
        for s in self.sensors:
            s.start()

    def stop_all(self):
        print("\n--- Deteniendo Sistema de Sensores ---")
        for s in self.sensors:
            s.stop()
