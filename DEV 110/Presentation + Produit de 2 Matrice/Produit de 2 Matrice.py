
#              <<< La Partie de construire les Tableaux est les Déclarer >>>
print("")
print(" |||| La Partie de construire les Tableaux est les Déclarer : ||||")
print("")


ligne  = int(input("Entrer Le Nombre des lignes du matrice 1 : "))
colone1 = int(input("Entrer Le Nombre des colones du matrice 1 : "))
print("||============================================================================================||")
print("||                                                                                            ||")
print("||               ! Attention: Ce programme est faite pour le produit du 2 Matrices,           ||")
print("||  Donc le nombre des colone du matrice 1, doit être égale au nombre des ligne du matrice 2. ||")
print("||                Alors d'aprés votre saisit des colone du matrice 1 ,                        ||")
print("||           Le programme va prit que Le Nombre des lignes du matrice 2 = ",colone1,"                 ||")
print("||                                                                                            ||")
print("||============================================================================================||")
colone2 = int(input("Entrer Le Nombre des colones du Matrice 2  : "))
print("")
print("")


matrice1 = []
print("SAISIT DE LA Matrice 1 :")
for i in range(ligne) :
    t = []
    print("    LIGNE : " + str(i+1))
    for j in range(colone1) :
        print("matrice1[" ,i+1,"][",j+1,"]=",end=" ")
        t.append(int(input()))
    matrice1.append(t)
print(matrice1)
print("")
print("")


matrice2 = []       
print("SAISIT DE LA Matrice 2 :")
for i in range(colone1) :
    t = []
    print("    LIGNE : " + str(i+1))
    for j in range(colone2) :
        print("matrice2[" ,i+1,"][",j+1,"]=",end=" ")
        t.append(int(input()))
    matrice2.append(t)
print(matrice2)

Tab = []
for i in range(ligne) :      
    t=[]
    for j in range(colone2) :     
        t.append(0)
    Tab.append(t) 



for i in range(ligne):            
    for j in range(colone2):     
        S = 0
        for k in range(colone1): 
            Tab[i][j] = S + matrice1[i][k] * matrice2[k][j]
            S = Tab[i][j]
print("")

print("Le Produit du 2 Matrices = ", Tab)


