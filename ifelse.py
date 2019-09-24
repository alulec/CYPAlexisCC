edad = int( input("Dame tu edad: "))
ine = bool( int( input("Tienes inde (0= no 1= si): ")))
if edad >= 18 and ine == True:
    print("Eres mayor de edad")
    print("Puedes entrar al bar")
else: 
    print("Eres menor de edad")
    print("Puedes ir a jugar lol")
print("Fin del programa")
