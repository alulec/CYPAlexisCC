maypro = 0
n = int(input("Numero de fabricas: "))
if n <= 100:
    for i in range(0, n, 1):
        fabrica = int(input("Clave de fabrica: "))
        totalnu = 0
        j = 1
        while j <= 12:
            mes = int(input("Produccion del mes: "))
            totalnu += mes
            if (j == 7) and ( mes >= 3000000):
                print(f"La produccion de la fabrica: {fabrica} es mayor a 3 000 000")
            j += 1
        if totalnu > maypro:
            maypro = totalnu
            clave = fabrica
        print(f"Produccion anual fabrica {fabrica} es de ${totalnu}")
    print(f"Fabrica que mas produjo en el año fue: {clave} con una produccion de: {maypro}.") 
else:
    print("Error en numero de fabricas")

