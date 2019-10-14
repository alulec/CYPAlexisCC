# dado un numero determina si es par, impar o nulo
n = int(input("Dame un número: "))
if n == 0:
    print("El numero es cero")
elif -1**n > 0:
    print(f"El número {n} es par.")
else:
    print(f"El número {n} es impar.")
