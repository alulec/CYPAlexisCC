# dado un numero determina si es positivo, negativo o nulo.
n = int(input("Dame un numero: "))
if n > 0:
    print(f"El numero {n} es positivo.")
elif n < 0:
    print(f"El numero {n} es negativo.")
else:
    print(f"El numero {n} es nulo.")
