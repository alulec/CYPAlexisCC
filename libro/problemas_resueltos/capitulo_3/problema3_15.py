cl = 0
cuenta = 0
print("Tipos de llamada: internacional (i), nacional (n) y local (l).")
print("Para finalizar oprima: ´x´ y ´-1´") 
tipo = input("Tipo de llamada: ")
dur = int(input("Duracion de la llamada: "))
while (tipo != "x") and (dur != (-1)):
    if tipo == "i":
        if dur > 3:
            costo = 7.59 + (dur-3)*3.03
        else:
            costo = 7.59
    elif tipo == "l":
        cl += 1
        if cl > 50:
            costo = .60
        else:
            costo = 0
    elif tipo == "n":
        if dur > 3:
            costo = 1.20 + (dur-3)*.48
        else:
            costo = 1.20
    cuenta += costo
    tipo = input("Tipo de llamada: ")
    dur = int(input("Duracion de la llamada: "))
print("El costo de las llemadas es de $",cuenta)
