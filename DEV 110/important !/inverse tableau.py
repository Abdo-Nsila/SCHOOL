
def SaisirTableau(max):
    tab = []
    for add_élement in range(0, max):
        num = int(input("Entrer tab["+str(add_élement)+"] :"))
        tab.append(num)
    print(tab)
    



    print(" ")
    print("!---------------------------!")
    print(" ")




    print("AFFICHAGE DU TABLEAU INVERSE :")
    tr = []
    for inverse in range((len(tab))-1, -1, -1):
        tr.append(tab[inverse])
        print("tab["+str(inverse)+"] :",tab[inverse])
    print(tr)


max = int(input("Entrer le nombre de case :"))
print("SAISIT DU TABLEAU :")
SaisirTableau(max)




