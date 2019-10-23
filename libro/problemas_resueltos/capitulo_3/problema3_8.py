"""
Conjetura de ULAM
Se ingresa cualquier numero entero positivo.
Si es par se divide entre dos, de lo contrario se multiplica por tres y se le agrega uno.
Obtiene enteros repitiendo el preoceso.
Finaliza cuando el numero inicial se convierte en uno.
n = numero inicial
"""
n = int(input("Numero positivo: "))
print("Los numeros que componen la serie son: ",end="")
if n > 0:
    while n != 1:
        print(n,end=" ")
        if ((-1)**n) > 0:
            n = n / 2
        else:
            n = ((n*3) + 1)
    print("1")
else:
    print("Tiene que ser un numero entero positivo.")
