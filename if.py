edad = int(input("Dame tu edad: "))
ine = bool(int(input("Tienes ine (0= no y 1= si): ")))
if (edad >= 18 and ine == True) or (ine == 1):
    print("Es mayor de edad")
    print("Puedes entrar al bar.")
print("Fin del programa")
