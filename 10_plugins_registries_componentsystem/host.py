# host.py
from loader import discover_plugins_from_package, list_registered_plugins
from registry import get_registry
import traceback

def create_and_setup(plugin_meta, config=None):
    cls_or_obj = plugin_meta.obj
    # instantiate if it's a class
    if isinstance(cls_or_obj, type):
        inst = cls_or_obj()
    else:
        inst = cls_or_obj
    config = config or {}
    try:
        inst.setup(config)
    except Exception as e:
        print(f"[WARN] plugin {plugin_meta.name} setup failed: {e}")
        traceback.print_exc()
    return inst

def run_plugin(plugin_name: str, version: str = None, config: dict = None, **kwargs):
    reg = get_registry()
    meta = reg.get(plugin_name, version)
    if not meta:
        raise KeyError(f"No plugin found for {plugin_name} {version}")
    inst = create_and_setup(meta, config)
    try:
        return inst.run(**kwargs)
    except Exception as e:
        print(f"[ERROR] running plugin {plugin_name}: {e}")
        traceback.print_exc()
        return None

if __name__ == "__main__":
    # discover plugins in local package 'plugins'
    discover_plugins_from_package("plugins")

    print("Registered plugins:")
    for p in list_registered_plugins():
        print(f"- {p.name} v{p.version} (module={p.module})")

    # run examples
    res = run_plugin("hello", name="Pedrin", config={"prefix": "¡Hola"})
    print("hello ->", res)

    res2 = run_plugin("math", config={"factor": 10}, x=2, y=3)
    print("math ->", res2)
