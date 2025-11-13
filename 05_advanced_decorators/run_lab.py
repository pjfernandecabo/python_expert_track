from examples import saluda, suma, grita, multiplica

def main():
    print("=== Decorator Lab ===\n")

    print("1️⃣  Probando logger:")
    saluda("Pedrin")

    print("\n2️⃣  Probando timer:")
    suma(100, 200)

    print("\n3️⃣  Probando repeat:")
    print(grita())

    print("\n4️⃣  Probando validate_args:")
    try:
        print(multiplica(2, 3, 4))
        print(multiplica(2, "x", 4))  # Error
    except TypeError as e:
        print(f"[ERROR] {e}")


    print(f"""\n✅ mini ejemplo.""")
    def doble(func):
        def wrapper(x):
            return func(x) * 2
        return wrapper

    def triple(n=3):
        def decorator(func):
            def wrapper(x):
                return func(x) * n
            return wrapper
        return decorator


    @doble
    def f(x): return x + 1

    @triple(n=5)
    def g(x): return x + 1

    print(f"f(2) = {f(2)}")  # (2+1)*2 = 6
    print(f"g(2) = {g(2)}")  # (2+1)*5 = 15


if __name__ == "__main__":
    main()
