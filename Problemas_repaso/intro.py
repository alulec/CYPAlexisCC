nombre = "Alexis Jesus"
numero = 48
print(nombre)
print(nombre[11])
print(nombre[-1])
print("-",nombre[6],"-")
#slicing (caracteres selectos en una cadena)
print(nombre[1:11:1])
print(nombre[0:11:2])
print(nombre[7::1])
#valores por defecto [0:0:1]
print(nombre[::])

#slicing negativo
print(nombre[-1:-6:-1])
print(nombre[::-1])
print(nombre[-7::-1])
"""
ejercicio:
hacer un slicing para imprimir  la palabra "existen",
otro para "personas" de fonrma inversa
y otro para que imprima toda la frase de forma inversa.
"""
frase = "Solo existen dos tipos de personas, las que saben binario y las que no."
print(frase[5:12:1])
print(frase[-38:-46:-1])
print(frase[::-1])

"""
print(dir(nombre))
print("")
print(dir(numero))
"""
print(nombre.upper())
print(nombre.lower())
print(f"La frase 'binario' inicia en la posiscion {frase.find('binario')}")
