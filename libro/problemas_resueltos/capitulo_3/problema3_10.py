"""
Calcula el termino 180 de la secuencia de FIBONACCI
pri = primer numero de la secuencia
seg = segundo numero de la secuencia
sig = almacena la suma de la secuencia
i = variable de control
"""
pri = 0
seg = 1

for i in range(3, 181, 1):
    sig = pri + seg
    pri = seg
    seg = sig
print("El termino 180 de la serie es: ",sig)
