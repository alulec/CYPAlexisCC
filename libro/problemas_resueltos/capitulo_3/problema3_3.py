# dado un numero entero, realiza la suma de la siguinte serie 1 - 1/2 + 1/3 - 1/4 + 1/5 +- 1/n
# ts (toatal suma), n (numero ingresado por el usuario), selec (selector de ruta)
ts = 1
i = 2
selec = "-"
n = int(input("Ingresa un numero: "))
while i <= n:
    if selec == "-":
        ts -= 1/i
        selec = "+"
    else:
        ts += 1/i
        selec = "-"
    i += 1
print("Total de la suma: ",ts)

