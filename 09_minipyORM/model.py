from exceptions import FieldError
from fields import Field


class ModelMeta(type):
    def __new__(mcls, name, bases, namespace):
        fields = {}

        for base in bases:
            if hasattr(base, "_fields"):
                fields.update(base._fields)

        for attr_name, attr_val in namespace.items():
            if isinstance(attr_val, Field):
                fields[attr_name] = attr_val

        namespace["_fields"] = fields

        return super().__new__(mcls, name, bases, namespace)

class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for field_name, field_obj in self._fields.items():

            if field_name in kwargs:
                setattr(self, field_name, kwargs[field_name])
            else:
                if field_obj.required and field_obj.default is None:
                    raise FieldError(f"Missing required field: {field_name}")

                setattr(self, field_name, field_obj.default)

    def to_dict(self):
        return {f: getattr(self, f) for f in self._fields}

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key not in self._fields:
                raise FieldError(f"Unknown field: {key}")
            setattr(self, key, value)

    def __repr__(self):
        fields = ", ".join(f"{k}={repr(getattr(self, k))}" for k in self._fields)
        return f"{self.__class__.__name__}({fields})"
