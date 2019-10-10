# problema que dice que numero es el mayor de tres
a = float(input("primer numero (positivo): "))
b = float(input("segundo numero (positivo): "))
c = float(input("tercer numero (positivo): "))
if a > b:
    if  a > c:
        print(f"a es el mayor con valor de {a}")
    elif a == c:
        print(f"a y c son iguales con el valor de {a}")
    else:
        print(f"c es el mayor que vale {c}")
elif a == b:
    if a > c:
        print(f"a y b son los mayores, que tienen el valor de {a}")
    elif a == c:
        print(f"a, b y c son iguales, que tienen el valor de {a}")
    else:
        print(f"c es el mayor con valor de {c}")
elif b > c:
    print(f" b es el mayor con valor de {b}")
elif b == c: 
    print(f"b y c son iguales, que tienen el valor de {b}")
else:
    print(f"c es el mayor, que tiene valor de {c}")
print("Fin del programa.")
