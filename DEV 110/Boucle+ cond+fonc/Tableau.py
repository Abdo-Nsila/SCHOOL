
                                # <<<< 20 nombres :Le plus grand nombre__le plus petit nombre >>>>


t = []
max = 0                                                                           # La valeur initiale
min = 9999999999999999999999999999999999999999999999999999999999999999999999999   # La valeur initiale


for i in range(1,21) :

    a = int(input('number ' + str(i)+ ":" ) )    # Quand l'utilisateur entre un nombre :
    t.append(a)                                  # Il se stocke dans Le Tableau .

for x in range(0,len(t)) :                       # En fait un scane au élement du tableau :
    if  t[x] > max :
        max = t[x]                               # - Afin du récuperer le max

    if t[x] < min :
        min = t[x]                               # - est récuperer le min


# Ecrire :
print(t)             # Ecrire Les élement du tableau
print("max =",max)   # Ecrire le max
print("min =",min)   # Ecrire le min