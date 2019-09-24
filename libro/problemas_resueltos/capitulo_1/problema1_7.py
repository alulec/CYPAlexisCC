# Programa que calcula el area de un triangulo a partir de sus lados
l1= float(input("Dame el primer lado del triangulo: "))
l2=float(input("Dame el segundo lado del triangulo: "))
l3= float(input("Dame el tercer lado del triangulo: "))
s= (l1 + l2 + l3)/ 2
area= ( s * (s-l1) * (s-l2) * (s-l3)) ** .5
print(f"El area del triangulo de lados {l1}, {l2} y {l3} es {area}")
