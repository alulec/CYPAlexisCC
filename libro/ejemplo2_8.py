# programa que calcula el aumento de un empleado dependiendo de su categoria y su sueldo
sue = float(input("sueldo: "))
cat = int(input("categoria: "))

nsue = 0
if cat == 1:
    print("nuevo sueldo: ", (sue * 1.15))
elif cat == 2:
    print("nuevo sueldo: ", (sue * 1.10))
elif cat == 3:
    print("nuevo sueldo: ", (sue * 1.8))
elif cat == 4:
    print("nuevo sueldo: ", (sue * 1.7))
else:
    print("Categoria invalida.")
