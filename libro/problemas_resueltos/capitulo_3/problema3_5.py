# Dado N n'umeros enteros como datos; calcula cuantos numeros positivos fueron ingresados, el promedo de los numeros positivos y el promedio de todos los números ingresados.
# n (total de números a ingresar), num (numero), negativos (cantidad de numeros negativos) positivos (cantidad de numeros positivos), sumap (suma de positivos), promediop (promedio de los numeros positivos), promediog (promedio general)
n = int(input("Cantidad de numeros a ingresar: "))
sumap = 0
positivos = 0
negativos = 0
for i in range(0, n, 1):
    num = int(input("Numero: "))
    if num > 0:
        sumap += num
        positivos += 1
    else:
        negativos += num
promediop = sumap / positivos
promediog = (positivos + negativos)/n
print(f"Numeros mayores que cero: {positivos}, promedio de los numeros positivos {promediop} y promedio general {promediog}")
