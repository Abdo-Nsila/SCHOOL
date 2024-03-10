max = 0
indicemax = 0
for i in range(1, 21):
    print("Ecrire numéro ", i, " : ", end="")
    a = int(input(""))
    if (a > max):
        max = a
        indicemax = i
print("Le plus grand de ces nombres est :", max)
print("C’était le nombre numéro ", indicemax)
