def SaisirTableau(nbrelts):
    t = []
    for i in range(nbrelts):
        print("tab[", i, "]=", end="")
        t.append(int(input()))
    return t

def InverserTableau(t):
    tr=[]
    for inverse in range((len(t))-1, -1, -1):
        tr.append(t[inverse])
        print("tr["+str(inverse)+"] :",t[inverse])
    print(tr)

    return tr
def AffichageTableau(tab):
    for i in range(len(tab)):
        print("tab[", i, "]=", tab[i])
    print(tab)


nrtab = int(input("Nombre de tableau souhaité:"))
max = int(input("taille du tableau : "))
print("SAISIT:")
tableau = SaisirTableau(max)
print("AFFICHAGE")
AffichageTableau(tableau)
print("InverserTableau")
InverserTableau(tableau)
