
# 🧩 Lección 1 — Object Inspector

## 🎯 Objetivo

Aprender a **inspeccionar y explorar objetos en Python** utilizando el módulo estándar `inspect`, entendiendo la estructura interna de cualquier clase, módulo o función.


## 📚 Conceptos cubiertos

- Tipos básicos en Python como objetos
- El módulo `inspect`
- Atributos, métodos y miembros especiales (`__dunder__`)
- Representación de objetos y reflexión


## 🧰 Mini proyecto — *Object Inspector*

Implementamos una utilidad llamada `inspect_object(obj)` que imprime:
- Tipo y clase del objeto  
- Módulo al que pertenece  
- Atributos y métodos públicos  
- Documentación (docstring) disponible  

### 📄 Código principal
Archivo: `obj_inspector.py`

```python
import inspect

def inspect_object(obj):
    print(f"📘 Tipo: {type(obj)}")
    print(f"🏷️  Clase: {obj.__class__.__name__}")
    print(f"📦  Módulo: {obj.__class__.__module__}\n")

    print("🔹 Métodos y atributos:")
    for name, member in inspect.getmembers(obj):
        if not name.startswith("__"):
            print(f"  • {name}: {type(member)}")

if __name__ == "__main__":
    class Demo:
        def __init__(self, x): self.x = x
        def double(self): return self.x * 2

    d = Demo(5)
    inspect_object(d)
