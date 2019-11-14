# diccionarios {'llave':'valor'}
alumno = {'Num_ctu':'31606374',
          'Nombre':('Alexis','Cordova', 'De LA Cruz'),
          'Semestre' : 1,
          'Promedio': 0.0,
          'materias': ['CyP', 'Algebra', 'Calculo', 'Geometria', 'IntroICO'],
          'regular':bool(1),
          'lagrimas_por_examen':5,
          'direccion': {
                    'Calle': 'Rancho seco',
                    'Colonia':'Santa teresa',
                    'Numero': 1000,
                    'Cp': 54680,
                    'del num': 'Huehuetoca',
                    'Estado': {
                            'id':15,
                            'nombre':'Estado de Mexico',
                            'corto':'EdoMex'
                            }
                    }
          }
"""
print(alumno['materias'][1].upper())
print(alumno['Nombre'])
print(alumno)
print(alumno['Nombre'][1])
print(alumno['direccion']['Cp'])
print(alumno['direccion']['Estado']['corto'])
print(alumno['materias'][3::1])

#diccionario con []
mi_lista= [['a','b'],['c',10],['c',True]]
diccionario = dict(mi_lista)
print(diccionario)
"""
print(alumno['direccion']['Estado']['nombre'][10::].upper())


# son mutables
"""
alumno['lagrimas_por_examen']=10
alumno['cursa_inglès']=True
print(alumno)
"""
# funcion keys()
llaves = alumno.keys()
print(llaves)
for llave in llaves:
    print("+++++++")
    print(llave)
    print("-------")
    print(alumno[llave])
 # funcion values
for val in alumno.values():
     print(".............")
     print(val)
     print("+++++++")
#funcion items
for elem in alumno.items():
    print("343453465")
    print(elem)
    print("-----------")
