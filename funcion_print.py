# print tiene cuatro formas de uso
"""
1. con comas
2. con signo '+'
3. con la funcion format()
4. es una variante de format()
"""
# con comas
edad = 10
nombre = "alexis"
estatura = 1.70
print(edad , estatura , nombre)

#  con '+' hace lo mismo pero
# no realiza es casting automatico
# no agrega espacio
print(str(edad ) + str(estatura ) + nombre)

# funcion format
print("Nombre: {1} Edad. {0}".format(nombre,edad)) 

# la forma cuatro es con una variante de format() simplificada
print(f"Nombre: \"{nombre}\" \Edad:\t {edad}")

#print y el argumento end
print("solo hay 10 tipoes de personas las que saben binario y las que no",end="\n")
print("otra linea")
