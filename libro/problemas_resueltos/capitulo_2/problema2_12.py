# calcula el sueldo a pagar por horas extras a un trabajador, dependiendo su categoria.
suel = float(input("Sueldo base del trabajador: "))
hor = int(input("Horas extra trabajadas: "))
cat = int(input("Categoria del trabajador: "))
if cat == 1:
    PEH =  30
elif cat == 2:
    PEH = 38
elif cat == 3:
    PEH = 50
elif cat == 4:
    PEH = 70
else:
    PEH = 0
if hor > 30:
    NSUE = suel + 30 * PEH
else:
    NSUE = suel + hor * PEH
print(f"El sueldo del trabajador es de ${NSUE}")
