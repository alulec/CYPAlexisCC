# programa que dado el monto a pagar determina si hay descuento aplicable o no y efectua dicho descuento de existir.
monto = float(input("Monto a pagar: "))
if monto < 500:
    print("Su compra es de $",monto)
elif monto < 1000:
    print("Su compra es de $", monto * 0.95," usted ahorro $", monto * 0.05)
elif monto < 7000:
    print("Su compra es de $", monto * 0.89," usted ahorro $", monto * 0.11)
elif monto < 15000:
    print("Su compra es de $", monto * 0.82," usted ahorro $", monto * 0.18)
elif monto > 15000:
    print("Su compra es de $", monto * 0.75," usted ahorro $", monto * 0.25)
