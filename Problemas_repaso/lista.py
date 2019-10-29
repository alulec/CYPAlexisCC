lista = []
lista2 = list()
print(lista)
print(lista2)

numeros = [3,4,52,45,7,64,546,567,0]
print(numeros)
print(numeros[2])
print(numeros[-1])
#slicing
print(numeros[3:-1:1])
print(numeros[::-1])

cosas = ["Alexis",545,9,34,35,True,None,[3,4,5,6,7,8]]
print(cosas)
print(cosas[7])
print(cosas[7][2])
cosas[1] = 10001
cosas[5] = False
print(cosas)

#tupla
fecha = '12/05/2019'
lista_fecha = fecha.split('/')
print(lista_fecha)
