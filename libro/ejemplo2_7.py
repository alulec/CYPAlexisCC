num = int(input("Ingresa un numero entero positivo: "))
v = int(input("Ingresa otro numero entero positivo: "))
val = 0
if num == 1:
    val= 100 * v
elif num == 2:
    val= 100  ** v
elif num == 3:
    val= 100/ v
else:
    val= 0
print(val)
print("Fin del programa.")
