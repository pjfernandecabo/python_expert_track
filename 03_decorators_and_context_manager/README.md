# 🧩 Lección 3 — Decoradores y Context Managers

## 🎯 Objetivo

Aprender a usar **decoradores y context managers** para escribir código **limpio, reusable y seguro** en Python.  
Esta lección te permite controlar la ejecución de funciones y recursos de manera profesional y elegante.

---

## 📚 Conceptos cubiertos

- **Decoradores**: extender funciones y clases sin modificar su código.  
- **Decoradores con argumentos**: parametrizar su comportamiento.  
- **Encadenamiento de decoradores**: aplicar varias transformaciones de manera ordenada.  
- **Context managers**: gestionar recursos (archivos, conexiones, locks) con `with`.  
- **`contextlib`**: crear context managers de forma sencilla y reusable.  
- Integración de **decoradores y context managers** para medir tiempos y controlar ejecución.

---

## 🧰 Mini proyecto — *Logging y Resource Timer*

### 📌 Objetivo:
- Crear un **decorador `@log_time`** que mida tiempo de ejecución de funciones.  
- Crear un **context manager** que mida el tiempo de un bloque de código.  
- Aplicar ambos en funciones de prueba para analizar su desempeño.

### 📁 Archivos
- `decorators_contexts.py` — código principal del proyecto

---

## 🧪 Ejemplo de uso

```bash
python decorators_contexts.py
```

## 💡 Conceptos prácticos aplicados

- Decoradores para extender funcionalidad sin tocar la función original.

- Decoradores con argumentos para flexibilidad y parametrización.

- Encadenamiento de decoradores para aplicar múltiples transformaciones.

- Context managers para control seguro de recursos.

- Uso de contextlib para simplificar creación de context managers.

- Integración práctica en mini proyectos de medición de desempeño.

## 🧾 Resumen de la lección
| Concepto                      | Qué aprendiste                                                   |
| ----------------------------- | ---------------------------------------------------------------- |
| Decoradores                   | Modificación y extensión de funciones/clases                     |
| Decoradores con argumentos    | Parametrización de decoradores                                   |
| Encadenamiento de decoradores | Aplicación secuencial de transformaciones                        |
| Context Managers              | Gestión segura de recursos con `with`                            |
| `contextlib`                  | Creación simple y reusable de context managers                   |
| Mini proyecto                 | Medición de tiempos de ejecución con decorador y context manager |
