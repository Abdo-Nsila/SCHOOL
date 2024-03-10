
t =[]
# remplissage
n= int(input("Donner la taille du tableau :"))
print("Donner",n,"Nombres")
for i in range(n) :
    t.append(int(input("Nombre numéro " + str(i+1) + " : " ) ) )

# Tri
for i in range(n-1) :
    min = t[i]
    pos=i
    for j in range(i+1,n) :
        if t[j] < min :
            min = t[j]
            pos = j
        if min != t[i] :
            aide = t[i]
            t[i] = min
            t[pos] = aide
        print("t aprés une itération :",t)

# affichage
print("Tableau final :")
print(t)