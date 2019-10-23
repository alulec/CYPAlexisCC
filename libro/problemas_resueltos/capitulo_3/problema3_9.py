"""
Dado un numero realiza la suma de 1^1 + 2^2 + 3^3 + ... n^n
n = numero ingresado por el usuario
suma = acumula los valores de cada sumando de la suma
i = variable de control del bucle
"""
suma = 0
i = 1
n = int(input("Ingresa un nnumero: "))
while i <= n:
    suma += i**i
    i += 1
print("El total de la sumatoria es : ",suma)
