# Dado el sueldo de cada empleado dentro de una nomina empresarial, calucula el aumento del sueldo por trabajador y el total de la nueva nomina.
# nom (total de la nomina empresarial), sue (sueldo de un empleado), nsu (nuevo sueldo), 
nom = 0
nsu = 0
print("El programa realiza el corte de nomina con el codigo: -1")
sue =  float(input("Sueldo: "))
while sue != (-1):
    if sue < 1000:
        nsu = sue*1.15
    else:
        nsu = sue*1.12
    nom += nsu
    print("N. Sueldo $", nsu)
    sue =  float(input("Sueldo: "))
print("La nomina total es de $", nom)
