"""
archivo = open("numeros.txt","rt")
#print(dir(archivo))
numeros1 = archivo.read()
print(numeros1)
print()
print(numeros1.split())
lista_num=[]
print()
for linea in numeros1.split('\n'):
    for numero in linea.split(','):
        lista_num.append( int(numero))
print(lista_num)
print()
lista_num.sort()
print(f"\n Lista ordenada: {lista_num} \n")

print(f"El mayor es : {lista_num[-1]} y el menor es: {lista_num[0]}")
archivo.close()
"""

archivo = open("numeros.txt","rt")
numeros2 = archivo.readlines()
print(numeros2)
lista_num2 = str(numeros2)
#print(lista_num2.split('\n'))


#print("\n ", numeros2 , "\n")
#print(f"El mayor es : {lista_num[-1]} y el menor es: {lista_num[0]}")
archivo.close()

"""
archivo = open("numeros.txt","rt")
numeros3 = archivo.readline()
print(numeros3)
lista = numeros3.split(',')
lista_num3 = []
for numero in lista:
    lista_num3.append(int(numero))
lista_num3.sort()
print(lista_num3)
print(f"El numero mayor de la lista es {lista_num3[-1]} y el menor es {lista_num3[0]}")
archivo.close()
"""
