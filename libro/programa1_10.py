# programa que calcula la base y superficie de un rectangulo
bas= int(input("cuanto mide la base: "))
alt= int(input("cuanto mide la altura: "))
sup= alt * bas
per= (2* alt) + (2* bas)
print("la superficies es de {}  y su perimetro es de {}".format(sup,per))
