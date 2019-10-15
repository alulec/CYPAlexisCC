n0 = 0
n = int(input("Dame unh numero entero positivo: "))
for i in range(0, n, 1):
    num = int(input("ingresa un entero: "))
    if num == 0:
        n0 += 1
print("Numeros de ceros capturados fue:",n0)
