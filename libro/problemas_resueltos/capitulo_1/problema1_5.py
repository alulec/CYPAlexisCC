# programa que a partir del radio de la base de un cilindro y su altura calcula el area y su volumen.
rad= float(input("Cuanto mide el radio: "))
alt= float(input("Cuanto mide su altura: "))
are= 2 * 3.141592 * rad * alt
vol= 3.141592 * (rad **2) * alt
print(f"El area del cilincdro es {are} y su volumen es de {vol}")
