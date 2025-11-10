# 🧩 Lección 2 — Iteradores y Generadores

## 🎯 Objetivo

Aprender a manejar **iteración avanzada en Python**, entendiendo cómo funcionan los **iteradores personalizados** y **generadores** para procesar datos grandes de forma eficiente y profesional.

Esta lección te prepara para escribir código más **Pythonic**, optimizado en memoria y altamente reutilizable.

---
## 🧾 RESUMEN 
 | Concepto             | Descripción                            | Ejemplo clave                            |
| -------------------- | -------------------------------------- | ---------------------------------------- |
| Iterador             | Objeto con `__iter__()` y `__next__()` | `CountDown`                              |
| Generador            | Función con `yield`                    | `countdown()`                            |
| Expresión generadora | `(x**2 for x in range(...))`           | Iteración lazy                           |
| `yield from`         | Delegar a otro generador               | `chain()`                                |
| Mini-proyecto        | *File Line Analyzer*                   | Lectura y filtrado eficiente de archivos |


## 📚 Conceptos cubiertos

- **Iteradores**: cómo implementar `__iter__()` y `__next__()`  
- **Generadores**: uso de `yield` para crear iteradores eficientes  
- **`yield from`**: delegación entre generadores  
- **Expresiones generadoras**: lazy evaluation  
- **Itertools**: herramientas avanzadas de iteración  
- Manejo de flujo de datos grandes sin cargar todo en memoria

---

## 🧰 Mini proyecto — *File Line Analyzer*

### 📌 Objetivo:
Crear un sistema que analice archivos de texto grandes línea por línea, filtrando información y calculando estadísticas **sin cargar todo el archivo en memoria**.

### 📁 Archivos
- `line_analyzer.py` — código principal del proyecto  
- `test_files/sample.txt` — archivo de prueba para el análisis

### 🔧 Funcionalidades
- Lectura de líneas con generador (`read_lines`)  
- Filtrado por palabra clave (`filter_lines`)  
- Cálculo de métricas sobre cada línea (`line_stats`)  
- Flujo completo orquestado en `analyze_file()`

---

## 🧪 Ejemplo de uso

```bash
python line_analyzer.py
```

## Salida esperada
```bash
Python es un lenguaje poderoso. (32 chars, avg=32.00)
Me gusta programar en Python. (30 chars, avg=31.00)
```

## 🎯 Al finalizar esta lección

- Entiendes cómo Python gestiona la iteración interna.

- Sabes crear tus propios iteradores con estado.

- Dominas generadores y expresiones generadoras para flujos grandes.

- Has construido un pipeline de datos eficiente y elegante.