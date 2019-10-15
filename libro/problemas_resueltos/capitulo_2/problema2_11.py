# calcula el costo de una llamada dependiendo de la duracion y la ubicacion del remitente.
lada = int(input("Clave: "))
dur = float(input("Tiempo de llamada: "))
if  lada == 12:
    costo = dur * 2
elif lada == 15:
    costo = dur * 2.2
elif lada == 18:
    costo = dur * 4.5
elif lada == 19:
    costo = dur * 3.5
elif (lada == 23) or (lada == 25):
    costo = dur * 6
elif lada == 29:
    costo = dur * 5
else:
    print("La clave que ingresaste no es correcta.")
print("El costo de llamada es de $",costo)
