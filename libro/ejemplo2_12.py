a = int(input("Dame un numero entero positivo: "))
b = int(input("Dame un numero entero positivo: "))
c = int(input("Dame un numero entero positivo: "))
if a > b:
    if a > c:
        if b > c:
            print(f"{a} > {b} > {c}")
        else:
            print(f"{a} > {c} > {b}")
    else:
        print(f"{c} > {a} > {b}")
else:
    if b > c:
        if a > c:
            print(f"{b} > {a} > {c}")
        else:
            print(f"{b} > {c} > {a}")
    else:
        print(f"{c} > {b} > {a}")
print("Fin del Programa.")
