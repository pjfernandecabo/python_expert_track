from decorators import logger, timer, repeat, validate_args

@logger
def saluda(nombre):
    return f"Hola, {nombre}!"

@timer
def suma(a, b):
    return a + b

@repeat(times=3)
def grita():
    return "¡¡Python!!"

@validate_args(int)
def multiplica(a, b, c):
    return a * b * c
