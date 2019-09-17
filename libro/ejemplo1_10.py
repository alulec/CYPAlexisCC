print("programa que calcula el area y perimetro de un cilindro")
rad = int(input("cual es el radio: "))
alt = int(input("cual es la altura: "))
vol = (3.141592)*(rad**2)*(alt)
are = 2*3.141592*rad*alt
print("el area del cilindro es {} y su volumen es {}".format (are,vol))

