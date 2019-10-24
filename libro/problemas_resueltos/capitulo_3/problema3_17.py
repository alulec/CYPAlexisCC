i = 3
sp = 0
m = int(input("Ingresa un numero: "))
if m >= 1:
    sp += 1
    print("Numero primo: 1 ")
    if m >= 2:
        sp += 1
        print("Numero primo: 2")
while i <= m:
    band = "v"
    j = 3
    while (j <( i // 2)) and (band == "v"):
        if (i % j) == 0:
            band = "f"
        j += 2
    if band == "v":
        print("Numero primo : ",i)
        sp +=1
    i += 2
print(f"Entre 1 y {m} hay {sp} numeros primos")
