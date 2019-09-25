# Programa que aplica el aumento de 15% a un sueldo dado si este es inferior a $1000
sue = float( input("Sueldo: "))
if sue < 1000:
    print("El nuevo sueldo del trabajador es: ",sue * 1.15)
