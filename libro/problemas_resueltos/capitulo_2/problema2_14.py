# programa que calcula el costo de internamiento de una persona segun su enfermedad
enf = int(input("No° de enfermedad: "))
dia = int(input("Dias internado: "))
eda = int(input("Edad: "))
cos = 0
if enf == 1:
    cos = dia * 25
elif enf == 2:
    cos = dia * 16
elif enf == 3:
    cos = dia * 20
elif enf == 4:
    cos = dia * 32
else:
    print("Dame un numero de enfermadad correcto (1,2,3 o 4")
if (eda >= 14) and (eda <= 22):
    print("El costo de la atencion es de $", cos * 1.10)
else: 
    print("El costo de la atencion es de $", cos )
