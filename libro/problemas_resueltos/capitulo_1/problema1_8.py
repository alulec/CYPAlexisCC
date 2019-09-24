# Programa que calcula la distancia entre dos puntos a partir de sus corrdenadas 
print("Primer punto")
x1= float(input("Dame x: "))
y1= float(input("Dmae y: "))
print("Segundo punto")
x2= float(input("Dame x: "))
y2= float(input("Dmae y: "))
dist= ((x1-x2) **2 + (y1-y2) **2) ** .5
print(f" La distancia entre el punto ({x1},{y1}) y el punto ({x2},{y2}) es {dist}")
