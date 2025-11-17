from decorators import log_call, timer

def create_resource_class(name, *, monitored_fields=None):

    monitored_fields = monitored_fields or []

    namespace = {}

    # ------------------------------------------------------
    # __init__
    # ------------------------------------------------------
    def __init__(self, **kwargs):
        self._stats = {"calls": 0, "errors": 0}
        for field in monitored_fields:
            setattr(self, field, kwargs.get(field, None))

    namespace["__init__"] = __init__

    # ------------------------------------------------------
    # Método monitorizado
    # ------------------------------------------------------
    @log_call
    @timer
    def update(self, **kwargs):
        """Actualiza los valores del recurso."""
        self._stats["calls"] += 1
        for k, v in kwargs.items():
            setattr(self, k, v)
        return True

    namespace["update"] = update

    # ------------------------------------------------------
    # __repr__
    # ------------------------------------------------------
    def __repr__(self):
        data = {field: getattr(self, field) for field in monitored_fields}
        return f"<{name} data={data} stats={self._stats}>"

    namespace["__repr__"] = __repr__

    return type(name, (object,), namespace)
