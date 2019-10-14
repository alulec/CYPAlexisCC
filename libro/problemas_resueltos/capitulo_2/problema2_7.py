# dados tres números detrmina si estos fueron dados en orden ascendente
a = float(input("Dame un numero: "))
b = float(input("Dame un numero: "))
c = float(input("Dame un numero: "))
if a > b:
    print("No estan en orden creciente.")
elif b > c:
    print("No estan en orden creciente.")
else:
    print("Si están en orden creciente.")
