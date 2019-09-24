# Programa que calcula el orden ascendente de tres numeros dados por el usuario
a = float( input("Dame el primer numero: "))
b = float( input("Dame el segundo numero: "))
c = float( input("Dame el tercer numero: "))
if a > b and a > c:
    if b > c: 
        print(a, b , c)
    else: 
        print(a, c , b)
if b > a and b > c:
    if a > c:
        print(b, a , c)
    else:
        print(b, c , a)
if c > b and c > a:
    if b > a:
        print(c, b , a)
    else:
        print(c, a , b)

