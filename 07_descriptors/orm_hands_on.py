class Column:
    def __init__(self, type_):
        self.type_ = type_

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError(f"{value} no es {self.type_.__name__}")
        setattr(instance, self.private_name, value)


class Model:
    def save(self):
        data = {
            name: getattr(self, "_" + name)
            for name, val in self.__class__.__dict__.items()
            if isinstance(val, Column)
        }
        print(f"Saving to DB: {data}")

class User(Model):
    id = Column(int)
    name = Column(str)
    age = Column(int)

u = User()
u.id = 1
u.name = "Pedro"
u.age = 38
u.save()
# u.age = "treinta y ocho"  # ERROR