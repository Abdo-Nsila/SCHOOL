


matrice1=[]
t=[]
ligne  = int(input("Entrer Le Nombre des lignes du matrice 1 : "))
colone1 = int(input("Entrer Le Nombre des colones du matrice 1 : "))
for i in range(0,colone1) :
    t.append(0)
for j in range(0,ligne) :
    matrice1.append(t)

matrice2=[]
t=[]
print("||============================================================================================||")
print("||                                                                                            ||")
print("||               ! Attention: Ce programme est faite pour le produit du 2 Matrices,           ||")
print("||  Donc le nombre des colone du matrice 1, doit être égale au nombre des ligne du matrice 2. ||")
print("||                Alors d'aprés votre saisit des colone du matrice 1 ,                        ||")
print("||           Le programme va prit que Le Nombre des lignes du matrice 2 = ",colone1,"                 ||")
print("||                                                                                            ||")
print("||============================================================================================||")
colone2 = int(input("Entrer Le Nombre des colones du matrice 2  : "))
for i in range(0,colone2) :
    t.append(0)
for j in range(0,ligne) :
    matrice2.append(t)

Tab=[]
t=[]
for i in range(0,colone2) :
    t.append(0)
for j in range(0,ligne) :
    Tab.append(t)
print(Tab)