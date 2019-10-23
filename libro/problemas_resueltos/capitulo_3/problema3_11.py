"""
Cuenta los votos totales de una eleccion, cuenta los votos respectivos de cada cadidato y obtiene el porcentaje correspondiente de los votos obtenidos por cada candidato respecto del total de votos
can1 = almacena los votod del candidato 1
can2 = almacena los votos del candidato 2
can3 = almacena los votos del candidato 3
can4 = almacena los botos del candidato 4
sumv = suma de todos los votos
por1, por2, por3 y por4 expresan el porcentaje del total de votos obtenido por cada candidato
vot = voto
"""
can1 = 0
can2 = 0
can3 = 0
can4 = 0
print("El codigo para mostar el total de la cuenta es : 0")
print("Ingresa el numero del candidato al que corresponde el voto (1, 2, 3 o 4) ")
vot = int(input("Voto: "))
while vot !=0:
    if vot == 1:
        can1 += 1
    elif vot == 2:
        can2 += 1
    elif vot == 3:
        can3 += 1
    else:
        can4 += 1
    vot = int(input("Voto: "))
sumv = can1 + can2 + can3 + can4
por1 =(can1/sumv)*100
por2 =(can2/sumv)*100
por3 =(can3/sumv)*100
por4 =(can4/sumv)*100
print(f"Votos del candidato 1 : {can1}, porcentaje del electorado obtenido: {por1}")
print(f"Votos del candidato 2 : {can2}, porcentaje del electorado obtenido: {por2}")
print(f"Votos del candidato 3 : {can3}, porcentaje del electorado obtenido: {por3}")
print(f"Votos del candidato 4 : {can4}, porcentaje del electorado obtenido: {por4}")

