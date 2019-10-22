arsu = 0
arno = 0
mersu = 50000
mes = 0
arce = 0
for i in range(1, 13, 1):
    print("Mes ",i)
    rno = int(input("Promdeio de lluvias del mes zona Norte: "))
    rce = int(input("Promdeio de lluvias del mes zona Centro: "))
    rsu = int(input("Promdeio de lluvias del mes zona Sur: "))
    arno += rno
    arce += rce
    arsu += rsu
    if rsu < mersu:
        mersu = rsu
        mes = 1
prorce = arce / 12
print(f"Promedio de lluvias de la zona centro: {prorce}")
print(f"Mes con menor lluvia en reg. sur: {mes}")
print(f"Registro del mes con menor lluvia es : {mersu}")
if arno > arce:
    if arno > arsu:
        print("La region con mayor lluvia es la reg. Norte")
    else:
        print("La region con mayor lluvia es la reg. Sur")
elif arce > arsu:
    print("La region con mayor lluvia es la reg. Centro")
else:
    print("La region con mayor lluvia es la reg. sur")
