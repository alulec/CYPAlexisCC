"""
dado el total de empleados, los numeros de mepleados y el sueldo de los mismos, determina 
el empleado con mayor sueldo
n = numero de empleados
num = numero de empleado
sue = sueldo del empleado
may = guarda el suledo del empleado mayor
emp = guarda el numero de empleado con mayor sueldo
"""
may = 0
emp = 0
n = int(input("Numero de empleados: "))
for i in range(0, n, 1):
    num = int(input("No° empleado: "))
    sue = float(input("Sueldo: "))
    if sue > may:
        may = sue
        emp = num
print(f"El empleado {emp} tiene el sueldo mayor que es de ${may}")
