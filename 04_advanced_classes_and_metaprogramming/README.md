# 🧩 Lección 4 — Clases Avanzadas y Metaprogramación

## 🎯 Objetivo

Comprender cómo Python trata las clases como objetos de primera clase y cómo manipular su comportamiento dinámicamente.
Aprenderás a usar atributos mágicos, metaclases y decoradores de clase para crear estructuras potentes y adaptables.

---

## 📚 Conceptos cubiertos

- Revisión rápida de clases y objetos

- Atributos mágicos (__init__, __repr__, __getattr__, __setattr__, __call__, etc.)

- Decoradores de clase y funciones de registro dinámico

- Propiedades (@property) y control de acceso

- Metaclases (type): creación dinámica de clases

- Generación de clases “al vuelo” (Class Factories)

- Aplicaciones en frameworks (Django ORM, Pydantic, etc.)

---

## 🧰 Mini proyecto — *Logging y Resource Timer*

### 📌 Objetivo:
- Construir un “Class Factory” que genere clases dinámicamente con atributos y métodos definidos por el usuario.
Así podrás crear objetos personalizados en tiempo de ejecución sin definir explícitamente sus clases.

### 📁 Archivos
- ``class_factory``.py — código principal

- `example_usage.py` — demostración del uso del generador de clases
- `namespace_explorer.py` - ejercicio completo
---





## 🧪 Ejemplo de uso

```bash
python decorators_contexts.py
```

## 💡 Conceptos prácticos aplicados

- Diferencias entre clases e instancias

## 🧾 Resumen de la lección

| Tipo                  | Dónde vive   | Ejemplo              | Visible en `__dict__`                |
| --------------------- | ------------ | -------------------- | ------------------------------------ |
| Atributo de instancia | En el objeto | `self.age`           | ✅ Sí                                 |
| Atributo de clase     | En la clase  | `species`, `kingdom` | 🚫 No (a menos que se copie en init) |
| Método de clase       | En la clase  | `speak`, `__repr__`  | 🚫 No (pero accesible vía lookup)    |



