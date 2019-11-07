def sumar( x , y ):
    z = x + y
    return z
def resta( x , y):
    return x - y

def mi_print( texto ):
    print(f"Estes es mi print: {texto}")

def multiplica(valor,veces):
    if veces == None:
        print("Debes enviar el segundo argumento de la funcion.")
    else:
        print(valor * veces)
def comanda(mesa, comensal, entrada, medio, fuerte, postre="Gelatina de limon"):
    print(f"Mesa: {mesa}  comensal: {comensal}")
    print(f"\t Entrada: {entrada}")
    print(f"\t Segundo tiempo: {medio}")
    print(f"\t Plato fuerte: {fuerte}")
    print(f"\t Postre: {postre}")
def comanda_2( **comida ):
    llaves=comida.keys()
    for elem in llaves:
        print(elem,'->',comida[elem])
def imprime_argumentos(*argumentos):
    for index in range(len(argumentos)):
        print(argumentos[index])









a = 10
b = 5
c = sumar(a,b)
print(f"la suma de {a} y {b} es {c}")
c = resta(a,b)
print(f"La resta de {a} y {b} es {c}")
mi_print("Hola !!!!")
multiplica(10,3)
multiplica(10,None)
multiplica('hola ',3)
comanda(2, 1, "Ensalada", "Sopa de rana", "Filete de pompi de sirena")
comanda("Ensalada", "Sopa de rana", "Filete de pompi de sirena", "Flan", 2, 1)
comanda(entrada="Ensalada", medio="Sopa de rana", fuerte="Filete de pompi de sirena", postre="Flan", mesa= 2, comensal=1)
comanda(entrada="Ensalada", medio="Sopa de rana", fuerte="Filete de pompi de sirena", mesa= 2, comensal=1)
imprime_argumentos('Hola', True, 3.141516, 1000, {'id':'sc01', 'nombre':'Alexis'})
imprime_argumentos()
comanda_2(entrada="Ensalada", medio="Sopa de rana", fuerte="Filete de pompi de sirena", mesa= 2, comensal=1, postre="Strudel de manzana", bebida="coca light")

