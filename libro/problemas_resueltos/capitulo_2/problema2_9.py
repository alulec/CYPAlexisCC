# calcula el precio de un articulo con impuesto agregado a partir de su precio base.
pre = float(input("Precio del producto: "))
if pre <= 20:
    print(f"El articulo cuasta ${pre}, no paga impuesto.")
elif (pre <= 40) and (pre > 20):
    print(f"El articulo con el precio inicial de ${pre} cuasta ${pre * 1.3}.")
elif (pre > 40) and (pre <= 500):
    print(f"El articulo con el precio inicial de ${pre} cuasta ${pre * 1.4}.")
elif pre > 500:
    print(f"El articulo con el precio inicial de ${pre} cuasta ${pre * 1.5}.")
