tipo1 = 0
tipo2 = 0
tipo3 = 0
tipo4 = 0
tipo5 = 0
mctipo2 = 0
n = int(input("Cantidad de años: "))
for i in range(0, n, 1):
    j = 1
    totvin = 0
    for j in range(1, 6, 1):
        v = float(input(f"Cuantos litros de vino del tipo {j} se produjeron: "))
        totvin += v
        if j == 1:
            tipo1 += v
        elif j == 2:
            tipo2 += v
            if v > mctipo2:
                mctipo2 = v
                año = n
        elif j == 3:
            tipo3 += v
            if v == 0:
                print(f"El año {n} no se produjo vino tiepo 3")
        elif j== 4:
            tipo4 += v
        elif j == 5:
            tipo5 += v
    print(f"Total litros producidos por año {totvin}")
print(f"Total tipo 1 {tipo1} litros ")
print(f"Total tipo 2 {tipo2} litros ")
print(f"Total tipo 3 {tipo3} litros ")
print(f"Total tipo 4 {tipo4} litros ")
print(f"Total tipo 5 {tipo5} litros ")
print(f"Año en que se produjo mayor cantidad de vino tipo 2 fue en el año {año} con {mctipo2} litros")

