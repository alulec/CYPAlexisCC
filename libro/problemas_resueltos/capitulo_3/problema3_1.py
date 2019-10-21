"""
Programa que recibe 270 numeros enteros. Realiza la suma de los numeros pares y luego obtiene el promedio. Tambien suma los valores de los impares (por separado).
sni (suma numeros impares)
snp (suma numeros pares)
cnp (cantidad numero par)
i   (contador de repeticiones)
pro (promedio de los numeros par)
num (numero entero)
"""
sni = 0
snp = 0
cnp = 0
for i in range(1 , 271, 1):
    num = int(input("Igresa un numero: "))
    if num != 0:
        if (-1)**num > 0:
            snp += num
            cnp += 1
        else:
            sni += num
pro = snp / cnp
print(f"Promedio de los numero par: {pro}, suma de los numero inpar: {sni}")
