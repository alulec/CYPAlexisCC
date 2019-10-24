n = int(input("Dame un numero: "))
i = 1
while i < n:
    suma = 0
    j = 1
    while j <= (i // 2):
        if (i % j) == 0:
            suma += j
        j += 1
    if suma == i:
        print(i," es un numero perfecto. ")
    i += 1
print("Fin del programa")
