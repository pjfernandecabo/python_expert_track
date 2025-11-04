#!/usr/bin/env python3
import inspect
import sys
import types
import pprint
import gc
import sys

def inspect_object(obj):
    print("="*80)
    print(f"🔍 Object: {obj}")
    print(f"📦 Type: {type(obj)}")
    print(f"📏 Size (bytes): {sys.getsizeof(obj)}")
    print("-"*80)

    # Atributos públicos
    attrs = [a for a in dir(obj) if not a.startswith('__')]
    print(f"📜 Attributes ({len(attrs)}): {attrs}")
    print("-"*80)

    # Métodos
    methods = [name for name, val in inspect.getmembers(obj, inspect.ismethod) or inspect.isfunction]
    print(f"⚙️  Methods: {methods}")
    print("-"*80)

    # Herencia
    cls = type(obj)
    print("🏗️  MRO (Method Resolution Order):")
    pprint.pp([c.__name__ for c in inspect.getmro(cls)])
    print("-"*80)

    # Referencias (avanzado)
    refs = gc.get_referrers(obj)
    print(f"🔗 Referrers count: {len(refs)}")

def main():
    if len(sys.argv) != 2:
        print("Uso: python obj_inspector.py <modulo.objeto>")
        print("Ejemplo: python obj_inspector.py math.pi")
        sys.exit(1)

    target = sys.argv[1]
    module_name, _, attr = target.partition(".")
    module = __import__(module_name)
    obj = getattr(module, attr)
    inspect_object(obj)

if __name__ == "__main__":
    main()
