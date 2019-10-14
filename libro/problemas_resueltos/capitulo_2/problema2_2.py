# dados dos números enteros (p y Q) determina si satisfacen la siguiente expresión p^3 + q^4 - 2*p^2 < 680
p = int(input("Dame p: "))
q = int(input("Dame q: "))
if (p**3 + q**4 -(2 * p**2)) < 680:
    print(f"Los valores {q} y {p} cumplen la expresión. ")
