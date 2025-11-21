# 🧠 LECCIÓN 9 — Descriptores, Propiedades Avanzadas y Campos Inteligentes

## 🎯 Objetivo de la lección

Al terminar esta lección podrás:

- Entender cómo funciona el protocolo descriptor (__get__, __set__, __delete__).
- Construir propiedades avanzadas sin usar @property.
- Implementar campos validados, tipo ORM:
    - IntegerField,
    - StringField,
    - RangeField,
    - CachedProperty.
- Crear descriptores computados, memoizados o con lógica de acceso.
- Comprender cómo dataclasses y pydantic inspiran su funcionamiento en descriptores.

## 📌 1. Concepto fundamental

Un descriptor es un objeto que implementa alguno de estos métodos:

```python
__get__(self, instance, owner)
__set__(self, instance, value)
__delete__(self, instance)
```
Cuando un atributo es un descriptor, Python NO accede directamente al diccionario de la instancia.
En vez de eso, redirige el acceso a estos métodos.

## 📌 2. Por qué existen los descriptores

Permiten:

- validación automática
- conversión automática
- lazy loading (solo se calcula al acceder)
- cacheo inteligente
- proteger acceso a recursos
- instrumentación
- lógica compartida entre muchas clases (como hacen ORMs)

Ejemplos del día a día que usan descriptores:

- @property
- staticmethod, classmethod
- funciones definidas dentro de una clase
- campos de Django ORM
- functools.cached_property

```markdown
Acceso atributo → ¿descriptor? → ejecuta __get__/__set__
                                        ↓
                         lógica central inteligente
```