from model import Model
from fields import StringField, IntegerField, EmailField

class User(Model):
    name = StringField(required=True, min_length=2)
    age = IntegerField(min=0, max=120)
    email = EmailField(required=True)

class Product(Model):
    name = StringField(min_length=3)
    price = IntegerField(min=0)
    stock = IntegerField(min=0, default=0)


user = User(name="Pedro", email="pedro@tech.com", age=38)
print(user)
print(user.to_dict())

product = Product(name="Laptop", price=1200)
print(product)
product.update(stock=15)
print(product)
