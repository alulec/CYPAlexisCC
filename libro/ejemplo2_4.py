# Programa que dado el sueldo de un trabajador imprima el nuevo sueldo con un aumento de 15% o 12% si es inferior o superior a $1000 respectivamente 
sue = float( input("Cual es el sueldo del empleado: "))
if sue < 1000:
    print("El nuevo sueldo del empleado es: ", sue * 1.15)
else:
    print("El nuevo sueldo del empleado es: ", sue * 1.12)
