#!/usr/bin/env python3
import inspect
import sys
import pprint
import gc

def inspect_object(obj):
    print("=" * 80)
    print(f"🔍 Object: {obj!r}")
    print(f"📦 Type: {type(obj)}")
    print(f"📏 Size (bytes): {sys.getsizeof(obj)}")
    print("-" * 80)

    # Atributos públicos
    attrs = [a for a in dir(obj) if not a.startswith('__')]
    print(f"📜 Attributes ({len(attrs)}):")
    pprint.pp(attrs)
    print("-" * 80)

    # Métodos (functions o methods)
    methods = [
        name for name, val in inspect.getmembers(obj)
        if inspect.isfunction(val) or inspect.ismethod(val)
    ]
    print(f"⚙️  Methods ({len(methods)}):")
    pprint.pp(methods)
    print("-" * 80)

    # Herencia
    cls = type(obj)
    if inspect.isclass(cls):
        mro = [c.__name__ for c in inspect.getmro(cls)]
        print("🏗️  MRO (Method Resolution Order):")
        pprint.pp(mro)
        print("-" * 80)

    # Referencias (avanzado)
    try:
        refs = gc.get_referrers(obj)
        print(f"🔗 Referrers count: {len(refs)}")
    except Exception as e:
        print(f"⚠️  Could not get referrers: {e}")
    print("=" * 80)

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

