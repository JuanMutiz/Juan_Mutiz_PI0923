noms = []
para = True

while para:
    dec = input ("Quem continuar? S/N")
    if dec == "S" or dec == "s":
        para = False
        continue
    noms.append(input("Insira seu nome"))

for nom in noms:
    print(nom)
