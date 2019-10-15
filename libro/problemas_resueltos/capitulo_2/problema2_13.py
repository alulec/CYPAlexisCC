# Dados como datos el número de matricula, carrera, semestre y promedio de un alumno, determina si dicho alumno es aceptado o no como miembro de la facultad menor.
mat = int(input("Matrícula del alumno: "))
car = input("Carrera: ")
sem = int(input("Semestre: "))
pro = float(input("Promedio: "))
if car == "economia":
    if (sem >= 6) and (pro >= 8.8):
        print(f"La matricula {mat} de la carrera {car} fue aceptada.")
    else:
        print(f"La matricula {mat} de la carrera {car} fue rechazada.")
elif car == "computacion":
    if (sem > 6) and (pro > 8.5):
        print(f"La matricula {mat} de la carrera {car} fue aceptada.")
    else:
        print(f"La matricula {mat} de la carrera {car} fue rechazada.")
elif (car == "administracion") or (car == "contabilidad"):
    if (sem > 5) and (pro > 8.5):
        print(f"La matricula {mat} de la carrera {car} fue aceptada.")
    else:
        print(f"La matricula {mat} de la carrera {car} fue rechazada.")
else:
    print("La carrera no esta contemplada")
