
#              <<< La Partie de construire les Tableaux est les Déclarer >>>
print("")
print(" |||| La Partie de construire les Tableaux est les Déclarer : ||||")
print("")

matrice1=[]
ligne  = int(input("Entrer Le Nombre des lignes du matrice 1 : "))
colone1 = int(input("Entrer Le Nombre des colones du matrice 1 : "))
for i in range(0,ligne) :       #Former Les lignes du Matrice 1
    t=[]
    for j in range(0,colone1) :     #Former Les colones du Matrice 1
        t.append(0)
    matrice1.append(t)            #Ajouter Les lignes avec ses colones au Matrice 1
# print(matrice1)

print("")

matrice2=[]

print("||============================================================================================||")
print("||                                                                                            ||")
print("||               ! Attention: Ce programme est faite pour le produit du 2 Matrices,           ||")
print("||  Donc le nombre des colone du matrice 1, doit être égale au nombre des ligne du matrice 2. ||")
print("||                Alors d'aprés votre saisit des colone du matrice 1 ,                        ||")
print("||           Le programme va prit que Le Nombre des lignes du matrice 2 = ",colone1,"                 ||")
print("||                                                                                            ||")
print("||============================================================================================||")
colone2 = int(input("Entrer Le Nombre des colones du Matrice 2  : "))
for i in range(0,colone1) :        #Former Les lignes du Matrice 2
    t=[]
    for j in range(0,colone2) :    #Former Les colones du Matrice 2
        t.append(0)
    matrice2.append(t)             #Ajouter Les lignes avec ses colones au Matrice 2
# print(matrice2)

Tab=[]

for i in range(0,ligne) :      #Former Les lignes du Matrice de Produit
    t=[]
    for j in range(0,colone2) :    #Former les colones du Matrice de Produit  
        t.append(0)
    Tab.append(t)                #Ajouter Les lignes avec ses colones au Matrice de Produit
# print(Tab)


print("")
print("")

print("SAISIT DE LA Matrice 1 :")
for i in range(0, ligne):                  # Parcourir les lignes du Matrice 1
    print("    LIGNE : " + str(i+1))       
    for j in range(0, colone1):            # Parcourir les colonnes du Matrice 1
        num = int(input("Entrer le Nombre " + str(j+1) + " Dans la ligne " + str(i+1) + " : "))
        matrice1[i][j] = num
print(matrice1)
print("")

print("SAISIT DE LA Matrice 2 :")
for i in range(0, colone1):      # Parcourir les lignes du Matrice 2 ' avec colone1 = ligne '
    print("    LIGNE : " + str(i+1))
    for j in range(0, colone2):  # Parcourir les colonnes du Matrice 2
        num = int(input("Entrer le Nombre " + str(j+1) + " Dans la ligne " + str(i+1) + " : "))
        matrice2[i][j] = num
print(matrice2)
print("")



# L'étape du produit entre les 2 Matrices
for ligneM1 in range(0, ligne):            # Parcourir les lignes du Matrice 1
    for coloneM2 in range(0, colone2):     # Parcourir les colonnes du Matrice 2
        S = 0
        for coloneM1 in range(0, colone1): # Parcourir les colonnes du Matrice 1 et les lignes du Matrice 2 
            Tab[ligneM1][coloneM2] = S + matrice1[ligneM1][coloneM1] * matrice2[coloneM1][coloneM2]
            S = Tab[ligneM1][coloneM2]
            

print("Le Produit du 2 Matrices = ", Tab)
