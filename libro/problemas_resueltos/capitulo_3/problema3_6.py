"""
Dados N cantidad de numeros calcula el menor y mayor de estos.
n = Total de numeros a ingresar
num = Numero que se ingresa
may = numero utilizado par realizar una comparacion
men = numero utilizado para realizar una comparacion
"""
may = -100000
men = 100000
n = int(input("Ingresa el total de numeros: "))
for i in range(0, n, 1):
    num = int(input("Ingresa un numero: "))
    if num > may:
        may = num
    if num < men:
        men = num
print("El numero mayor es {} y el menor es {} ".format(may,men)) 
