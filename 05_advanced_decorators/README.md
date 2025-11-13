# 🧩 Lección 5 — Decoradores avanzados y patrones funcionales en Python

## 🎯 Objetivo

Objetivo: Dominar la creación, comprensión y composición de decoradores, tanto simples como parametrizables, y aplicar patrones funcionales de uso profesional.


## 📚 Conceptos cubiertos

Los decoradores permiten modificar o extender el comportamiento de funciones y clases sin alterar su código fuente.
Son ampliamente utilizados en:

- Frameworks web (FastAPI, Flask, Django),

- Librerías de IA (PyTorch, TensorFlow),

- y código de infraestructura (logging, validación, métricas).


Tipos de decoradores
| Tipo               | Ejemplo                                   | Características                                   |
| ------------------ | ----------------------------------------- | ------------------------------------------------- |
| **Simple**         | `@logger`, `@timer`                       | Reciben solo la función.                          |
| **Parametrizable** | `@repeat(times=3)`, `@validate_args(int)` | Reciben argumentos antes de la función.           |
| **Combinado**      | `@timer` + `@logger`                      | Se pueden apilar. El orden de evaluación importa. |

```css
05_decorator_lab/
├── decorators.py        # Implementaciones de decoradores
├── examples.py          # Ejemplos de uso real
├── run_lab.py           # Ejecutor principal del laboratorio
└── decorator_explorer.py # Script exploratorio visual y didáctico
```

## 🔍 Mini resumen visual — Mapa mental del flujo de un decorador parametrizable

```css
@repeat(times=3)
def saluda(): ...

        ▼
1️⃣ repeat(times=3)            ← función externa (configura el decorador)
        │
        ▼
2️⃣ devuelve decorator(func)   ← función intermedia que recibe la función original
        │
        ▼
3️⃣ devuelve wrapper()         ← función interna que envuelve la ejecución
        │
        ▼
4️⃣ saluda = wrapper           ← reemplaza la referencia original
        │
        ▼
5️⃣ Llamadas reales ejecutan wrapper() → que a su vez llama func()
```
## 🧠 decorator_explorer.py — Script de exploración paso a paso

Este archivo muestra, mediante prints, cómo Python evalúa un decorador desde dentro, tanto los simples como los parametrizables.
Permite observar:

- Cuándo se ejecuta la capa externa (def repeat(times)),

- Cuándo se aplica el decorador interno (def decorator(func)),

- Y cómo el wrapper final reemplaza la función original.

## 📈 Resumen de lo aprendido

- ✅ Entendiste cómo funcionan los decoradores simples y parametrizables.
- ✅ Usaste @wraps para preservar los metadatos de las funciones decoradas.
- ✅ Implementaste decoradores útiles: logger, timer, repeat, validate_args.
- ✅ Exploraste la composición y orden de ejecución de múltiples decoradores.
- ✅ Analizaste internamente cómo Python ejecuta cada capa de un decorador.


## 🧩 Recomendación profesional

Cuando desarrolles librerías o frameworks:

- Siempre utiliza @wraps (fundamental para introspección y documentación).

- No abuses de decoradores anidados complejos (dificultan depuración).

- Agrupa decoradores relacionados en un módulo propio (decorators.py).

- Documenta con claridad qué hace cada decorador y qué devuelve.
