ligne = int(input("Entrée le nombre des édudiants : "))
colone = int(input("Entrée le nombre des Matiers : "))

M =[]
tab=[]

for i in range(0,ligne) :
    s = 0
    for j in range(0,colone) :
        note = float(input("Entrer la note du Matiere " + str(j+1) + " d'étudiant Numéro " + str(i+1) + " : " ))
        tab.append(note)
        s = s + note
    print("La Moyenne d'étudiant Numéro " + str(i) + " est : " , s / colone )


print(tab)