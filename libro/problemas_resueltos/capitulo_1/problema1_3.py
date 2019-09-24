#aurio, su npeso en libras y su altura en pies, devuelva su nombre, su altura en toneladas y su altura en metros
nom= input("Nombre del dinosaurio: ")
pes= float(input("Peso del dinosaurio: "))
alt= float(input("Altura del dinosaurio: "))
altu= alt * .3047
peso= pes * 1000
print(f"{nom} pesa: {peso} toneladas y mide {altu} metros")
