# dados los coeficientes a, b y c de una ecuación, calcular las raices.
print("Dame unicamente los coeficientes de la ecuación, en orden (ax^2+bv+c).")
a = float(input("Dame a: "))
b = float(input("Dame b: "))
c = float(input("Dame c: "))
dis = b**2 - 4*a*c
if dis >= 0:
    x1 = (-(b) + (dis**0.5)) / (2*a)
    x2 = (-(b) - (dis**0.5)) / (2*a) 
    print(f"Las soluciones de la ecuación son {x1} y {x2}")
