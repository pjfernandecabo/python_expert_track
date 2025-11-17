# 🛰️ Mini-Proyecto: ResourceMonitor

## 🎯 Objetivo

Mini-framework diseñado para practicar:

- Metaclases
- Decoradores avanzados
- Factories de clases
- Manipulación del namespace
- Dunder methods (__init__, __repr__)
- Registro automático de clases
- Lógica dinámica en tiempo de ejecución

El proyecto define un sistema que permite crear recursos monitorizados (CPU, RAM, GPU, sensores, etc.) dinámicamente, añadirles decoradores automáticos y centralizarlos mediante una metaclase registradora.

## 📁 Estructura del proyecto

```css
ResourceMonitor/
│
├── decorators.py        # Decoradores: log, timer, repeat, validate_args
├── factory.py           # Factoría para crear clases dinámicas de recursos
├── resource_monitor.py  # Metaclase que registra recursos
├── example_usage.py     # Demostración completa del proyecto
└── README.md            # Este documento
```

## 🧠 Conceptos que practica este mini-proyecto
✔ Metaclases

- ResourceRegistry registra cualquier clase que herede de BaseResource.

✔ Decoradores

- log_call registra la ejecución.
- timer mide duración.
- repeat(n) ejecuta varias veces.
- validate_args(types) valida los tipos en runtime.

✔ Class Factory

- create_resource_class() genera clases completas con métodos monitorizables.

✔ Namespaces

- Los métodos se añaden al namespace antes de crear la clase.

✔ Dunder Methods

- `__repr__` imprime el estado del recurso.