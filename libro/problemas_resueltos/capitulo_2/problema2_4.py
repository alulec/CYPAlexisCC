# dada la matricula de un alumno y sus cinco calificaciones, imprime su matricula, su promedio y su estado (aprobado/ no aprobado)
mat = input("Matrícula del alumno: ")
cal1 = float(input("Primer calificación: "))
cal2 = float(input("Segunda calificación: "))
cal3 = float(input("Tercera calificación: "))
cal4 = float(input("Cuarta calificación: "))
cal5 = float(input("Quinta calificación: "))
pro = (cal1 + cal2 + cal3 + cal4 + cal5)/5
if  pro >= 6:
    print(f"El alumno {mat} aprobo el curso con {pro}")
else:
    print(f"El alumno {mat} reprobo el curso con {pro}")
