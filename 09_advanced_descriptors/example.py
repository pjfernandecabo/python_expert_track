class Demo:
    def __get__(self, instance, owner):
        print("GET called")

class A:
    x = Demo()

a = A()
a.x   # imprime: GET called



class Field:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        setattr(instance, self.private_name, value)


class Person:
    name = Field()
    age = Field()

p = Person()
p.name = "Pedro"
p.age = 38

print(p.name, p.age)


class IntegerField(Field):
    def __set__(self, instance, value):
        if not isinstance(value, int):
            #raise TypeError("Value must be integer")
            print("Value must be integer")
        super().__set__(instance, value)

class Product:
    stock = IntegerField()

p = Product()
p.stock = 10     # ok
p.stock = "aaa"  # error

class RangeField(IntegerField):
    def __init__(self, *, min=None, max=None):
        self.min = min
        self.max = max

    def __set__(self, instance, value):
        if (self.min is not None and value < self.min) or \
           (self.max is not None and value > self.max):
            #raise ValueError(f"Value {value} is out of range")
            print(f"Value {value} is out of range")
        super().__set__(instance, value)

class Sensor:
    temp = RangeField(min=-10, max=70)

s = Sensor()
s.temp = 25  # OK
s.temp = 200 # error

class ComputedProperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.func(instance)

class Circle:
    def __init__(self, r):
        self.r = r

    @ComputedProperty
    def area(self):
        return 3.1416 * self.r**2

c = Circle(10)
print(c.area)  # 314.16

class CachedProperty:
    def __init__(self, func):
        self.func = func
        self.private_name = "_cached_" + func.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if hasattr(instance, self.private_name):
            return getattr(instance, self.private_name)
        value = self.func(instance)
        setattr(instance, self.private_name, value)
        return value

import time

class Expensive:
    @CachedProperty
    def compute(self):
        time.sleep(2)
        return 42

e = Expensive()
print(e.compute) # tarda 2s
print(e.compute) # inmediato
