max = 0
indicemax = 0
a = int(input("Ecrire numéro 1:"))
i = 2
while (a != 0):
    print("Ecrire numéro ", i, " : ", end="")
    a = int(input(""))
    if (a > max):
        max = a
        indicemax = i
    i += 1
print("Le plus grand de ces nombres est :", max)
print("C’était le nombre numéro ", indicemax)
