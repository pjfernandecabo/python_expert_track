# Context Managers

## 🧠 Introducción

Los context managers (with ... as ...) permiten encapsular la lógica de inicialización y limpieza de recursos.
El patrón más común es el uso con archivos, pero también se usan para manejar:

- conexiones a bases de datos, APIs, sockets
- bloqueos de threads o procesos
- gestión de memoria GPU (PyTorch, TensorFlow)
- logging, profiling o manejo temporal de estado

## 🎯 Objetivos de la lección

- Comprender el protocolo del context manager (__enter__ / __exit__).
- Crear context managers personalizados con clases.
- Usar decoradores contextmanager de contextlib.
- Implementar contextos anidados y combinados.
- Desarrollar un mini framework de recursos que gestiona distintos tipos de contextos.

## 
```css
Context Manager Protocol
    ├── __enter__() → inicializa
    ├── __exit__() → limpia
    ├── with ... as ... → usa el recurso
    ├── contextlib.contextmanager → simplifica el patrón
    └── ExitStack → combina varios contextos

```