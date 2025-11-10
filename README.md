# 🐍 Python Expert Track — Curso Avanzado de Python

Bienvenido al **Python Expert Track**, un programa completo diseñado para dominar Python desde la base sólida hasta un nivel profesional y experto.

---

# WARNING PEDRO
Before begin coding pls: 

1. activate uv env and deactivate conda base env:
```bash
source /home/pedro/Projects/python_expert_track/.venv_3_13/bin/activate &&
conda deactivate
```

2. Create a new branch in every lesson


```bash
git checkout -b feature/lesson-01
```

3. Make new lesson dir

```bash
mkdir 04_metaprogramming
```

4. Make Readme.md in every lesson

5. Finally, then, go to Github chapter to manage GIT commands

---

## 🚀 Objetivo del curso

El objetivo es aprender **Python en profundidad** mediante **proyectos reales (hands-on)**, construyendo herramientas y sistemas avanzados que consolidan cada concepto.

Cada lección tiene:
- 🧠 Introducción teórica breve  
- 🧰 Mini proyecto práctico  
- 🧾 Resumen final  
- 📂 Código estructurado y comentado  

---

## 🧭 Estructura de carpetas

```css
python_expert_track/
│
├── .gitignore
├── README.md
│
├── 01_object_inspector/
│   ├── obj_inspector.py
│   ├── README.md
│   └── __init__.py
│
├── 02_iterators_generators/
│   ├── README.md
│   └── __init__.py
│
├── 03_decorators_contexts/
│   ├── README.md
│   └── __init__.py
│
├── assets/
│   ├── images/
│   │   └── .gitkeep
│   ├── notebooks/
│   │   └── .gitkeep
│   └── data/
│       └── .gitkeep
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
└── docs/
    ├── roadmap.md
    ├── git_workflow.md
    └── changelog.md

```



## 🔄 Flujo de trabajo con Git

Este repositorio usa una estructura profesional basada en GitFlow:

- **`main`** → rama estable (solo versiones completas y testeadas)
- **`dev`** → rama activa de desarrollo
- **`feature/leccion-XX`** → rama temporal por cada lección

### 1️⃣ Creas la rama de desarrollo (una vez)

```bash
git checkout -b dev
git push -u origin dev
```

### 2️⃣ Creas una rama por lección

Por ejemplo, para la Lección 1:

```bash
git checkout -b feature/leccion-01
```

### 3️⃣ Trabajas y haces commits en esa rama

```bash
git add 01_object_inspector/
git commit -m "Lección 1: finalizada — Object Inspector"

```

### 4️⃣ Fusionas con dev cuando termines

```bash
git checkout dev
git merge feature/leccion-01
git push

```

### 5️⃣ Fusionas dev → main al finalizar un módulo completo

```bash
git checkout main
git merge dev
git push

```

**Ejemplo de flujo:**
```bash
git checkout -b feature/leccion-01
# trabajo y commits
git checkout dev
git merge feature/leccion-01
git push

```
---
## 📘 Progreso del curso

| Nº | Lección                        | Tema                                  | Estado |
| -- | ------------------------------ | ------------------------------------- | ------ |
| 1  | Object Inspector               | Introspección y reflexión en Python   | ✅      |
| 2  | Iteradores y Generadores       | Iteración eficiente y lazy evaluation | ⏳      |
| 3  | Decoradores y Context Managers | Patrón funcional avanzado             | ⏳      |

## 🧑‍💻 Autor

Pedro

PhD en IA, ingeniero de software experto en ML y Python

Actualmente desarrollando aplicaciones inteligentes y herramientas de productividad avanzada.

## ⚙️ Licencia

MIT License © 2025 — libre para aprender, usar y compartir.

