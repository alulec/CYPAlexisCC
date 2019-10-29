#arreglos
#lectura
#escritura / asignacion
#ordenamiento
#busqueda

#escritura
frutas = ["Zapote", "Manzana", "Pera", "Aguacate", "Durazno", "Uva", "Sandia"]

#lectura, el selector [ indice ]
print(frutas[2])

#lectura con for
#for opcion 1
for indice in range(0, 7, 1):
    print(frutas[indice])
print("---------------")

# for opcion 2 -- por un iterador for each
for fr in frutas:
    print(fr)
#asignacion
frutas[2] = "Melon"
print(frutas)

#insercion al final
frutas.append("Naranja")
print(frutas)
print(len(frutas))
#insercion de un elemento en donde sea
frutas.insert(2,"Limon")
print(frutas)
print(len(frutas))

frutas.insert(0, "Mamey")
print(frutas)

#eliminacion con pop
print(frutas.pop())


frutas.append("Limon")
frutas.append("Limon")
print(frutas)
frutas.remove("Limon")
print(frutas)
print(frutas.pop(1))
print(frutas)

#ordenamiento
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)

#BUSQUEDA
print(f"El limon esta en la pos. {frutas.index('Limon')}")
print(f"El limon esta {frutas.count('Limon')} en la lista")

#concatenar
print(frutas)
otras_frutas = ["Rambutan", "Pitahaya", "Nispero", "Liche"]
frutas.extend(otras_frutas)
print(frutas)

#copia
copia = frutas
copia.append("NARANJA")
print(frutas)
print(copia)

otra_copia = frutas.copy()
otra_copia.append("FRESA")
otra_copia.append("FRESA")
print("-----------")
print(frutas)
print(otra_copia)
