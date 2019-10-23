"""

ap1, ap2, ap3, ap4, y ap5: acumulan el numero de boletos vendidos de cada localidad
clave: tipo de voletos vendidos
cant: cantidad de voletos vendidos
p1, p2, p3, p4, y p5:son los precios de cada localidad
pre: monto de la venta
recau = suma de lo obtenido en todas las ventas

"""
ap1 = 0
ap2 = 0
ap3 = 0
ap4 = 0
ap5 = 0
p1 = float(input("Precio de la localidad 1: "))
p2 = float(input("Precio de la localidad 2: "))
p3 = float(input("Precio de la localidad 3: "))
p4 = float(input("Precio de la localidad 4: "))
p5 = float(input("Precio de la localidad 5: "))
print("El corte de ventas se realiza con el codigo : -1")
clave = int(input("Tipo de localidad: "))
cant = int(input("Boletos vendidos: "))
recau = 0
while (clave != (-1)) and (cant != (-1)):
    if clave == 1:
        pre = p1*cant
        ap1 += cant
    elif clave == 2:
        pre = p2*cant
        ap2 += cant
    elif clave == 3:
        pre = p3*cant
        ap3 += cant
    elif clave == 4:
        pre = p4*cant
        ap4 += cant
    elif clave == 5:
        pre = p5*cant
        ap5 += cant
    print(f"Tipo de localidad: {clave}, cantidad de boletos: {cant} y monto a pagar ${pre}")
    recau = recau + pre
    clave = int(input("Tipo de localidad: "))
    cant = int(input("Boletos vendidos: "))
print(f"Cantidad de volestos vendidos de tipo 1: {ap1}")
print(f"Cantidad de volestos vendidos de tipo 2: {ap2}")
print(f"Cantidad de volestos vendidos de tipo 3: {ap3}")
print(f"Cantidad de volestos vendidos de tipo 4: {ap4}")
print(f"Cantidad de volestos vendidos de tipo 5: {ap5}")
print(f"Total reacudado ${recau}")
