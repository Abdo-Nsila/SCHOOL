def SaisirTableau(nbrelts):
    t = []
    for i in range(nbrelts):
        print("tab[", i, "]=", end="")
        t.append(int(input()))
    return t


def InverserTableau(t):
    tr = []
    # for i in range(len(t)):
    #     tr.append(t[(len(t)-1)-i])
    # for i in range(len(t)-1,-1,-1):
    #     tr.append(t[i])
    for i in range(len(t)):
        tr.insert(0, t[i])

    return tr


def AffichageTableau(tab):
    for i in range(len(tab)):
        print("tab[", i, "]=", tab[i])


# nrtab = int(input("Nombre le tableau souhaité:"))
max = int(input("taille du tableau : "))
print("SAISIT:")
tableau = SaisirTableau(max)
print("AFFICHAGE")
AffichageTableau(tableau)
tableauInverse = InverserTableau(tableau)
print("AFFICHAGE TABLEAU INVERSE")
AffichageTableau(tableauInverse)
