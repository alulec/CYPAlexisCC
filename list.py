# lista
lluvias_norte = [80,60,120,100,70,150,100,47,95,70,100,130]

for indice in range(0, 12, 1):
    print(f"mes {indice+1} en region norte = {lluvias_norte[indice]} ")
print(lluvias_norte[4])
print(lluvias_norte[2:12:3])

sueldo = []
suma = 0
for indice in range(7):
    sueldo.append(int(input("sueldo: ")))
print(sueldo)

for indice in range (7):
    suma += sueldo [indice]

promedio = suma / 7
print(f"El promedio de sueldo es: {promedio}")
cont = 0
for indice in range (7):
    if sueldo [indice] > promedio:
        cont += 1
        print(f"Arriba: {sueldo[indice]}")
