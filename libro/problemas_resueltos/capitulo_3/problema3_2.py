# Realiza la suma e imprime los nmeros de la siguiente serie: 2, 5, 7, 10, 12, 15, 17...1800
# dot ( determina si se suma dos o tres), ts (total suma), i (inicio de la serie)
i = 2
ts = 0
dot = 2
while i <= 1800:
    ts += i
    print(i,end=" ")
    if dot == 2:
        dot = 3
        i +=3
    else:
        dot = 2
        i += 2
print(f"total de la suma: {ts}")
