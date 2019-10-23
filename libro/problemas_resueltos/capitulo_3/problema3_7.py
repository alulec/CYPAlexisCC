"""
Dadas el numero de ventas y el monto de cada una refleja cuantas ventas se han realizao de $200 o menos, mayores de $200 pero menores a $400 y las mayores de $4oo
n = total de ventas realizadas
mon = monto de la venta 
chi = numero de ventas iguales o menores de $200
med = numero de ventas superiorees a $200 pero inferiores a $400
gra = numero de ventas iguales o superiores a $400
v = el monto de la venta
"""
chi = 0
med = 0
gra = 0
n = int(input("Total de ventas: "))
i = 1
while i <= n:
    v = float(input("Monto de venta: "))
    if v <= 200:
        chi += 1
    elif v < 400:
        med += 1
    else:
        gra += 1
    i += 1
print(f"Ventas iguales o inferiores a $200: {chi}, mayores a $200 e inferiores a $400: {med} y superiores a $400: {gra}")
