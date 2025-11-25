from exceptions import ValidationError


class Field:
    """
    Base descriptor for all fields.
    Implements: __set_name__, __get__, __set__
    """
    def __init__(self, *, required=False, default=None):
        self.required = required
        self.default = default
        self.name = None  # set via __set_name__

    def __set_name__(self, owner, name):
        self.name = name
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, self.default)

    def validate(self, value):
        """Override in subclasses"""
        return value

    def __set__(self, instance, value):
        value = self.validate(value)
        setattr(instance, self.private_name, value)

class StringField(Field):
    def __init__(self, *, min_length=0, max_length=None, **kwargs):
        super().__init__(**kwargs)
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, value):
        if not isinstance(value, str):
            raise ValidationError(f"'{self.name}' must be a string")

        if len(value) < self.min_length:
            raise ValidationError(
                f"'{self.name}' must have at least {self.min_length} characters"
            )

        if self.max_length is not None and len(value) > self.max_length:
            raise ValidationError(
                f"'{self.name}' must have at most {self.max_length} characters"
            )

        return value

class IntegerField(Field):
    def __init__(self, *, min=None, max=None, **kwargs):
        super().__init__(**kwargs)
        self.min = min
        self.max = max

    def validate(self, value):
        if not isinstance(value, int):
            raise ValidationError(f"'{self.name}' must be an integer")

        if self.min is not None and value < self.min:
            raise ValidationError(f"'{self.name}' must be >= {self.min}")

        if self.max is not None and value > self.max:
            raise ValidationError(f"'{self.name}' must be <= {self.max}")

        return value

import re

class EmailField(StringField):
    email_regex = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

    def validate(self, value):
        value = super().validate(value)
        if not EmailField.email_regex.match(value):
            raise ValidationError(f"'{self.name}' must be a valid email")
        return value

