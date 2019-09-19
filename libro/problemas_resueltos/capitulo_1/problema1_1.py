# Programa que calcula el cambio dentro de una transaccion comercial 
prepro= float(input("Precio del producto: "))
pago= float(input("Monto de pago: "))
devo= pago-prepro
print(f"Pagaste: ${pago} y el precio del producto es: ${prepro} y tu cambio es: ${devo}")
