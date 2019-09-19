#aurio, su npeso en libras y su altura en pies, devuelva su nombre, su altura en toneladas y su altura en metros
nom= input("Nombre del dinosaurio: ")
alt= float(input("Peso del dinosaurio: "))
pes= float(input("Altura del dinosaurio: "))
altu= alt * .454392
peso= pes * 3.28084
print(f"{nom} pesa: {peso} toneladas y mide {altu} metros")
