colone = int(input("Entrée le Nombre des Colones : "))

M =[]
tab1=[]
tab2=[]
print("")
print("SAISIT DU TABLEAU 1 :")
for i in range(0,2) :
    if i > 0 :
        print("")
        print("SAISIT DU TABLEAU 2 :")
    for j in range(0,colone) :
            num = int(input("Entrer tab" + str(i+1) + " ["+str(j)+"] :"))
            if i == 0 :
                tab1.append(num)
            elif i > 0 :
                tab2.append(num)

M.append(tab1)
M.append(tab2)

print("")
print("La Matrices M = ", M )

tab=[]
for i in range(0,colone) :
    tab.append(M[0][i] + M[1][i])
print("")
print("La Somme des 2 Tableaux :")
print(tab)
print("")
