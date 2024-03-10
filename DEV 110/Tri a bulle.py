T = [6,4,3,5]

while True :
    cond = True
    for i in range(1,len(T)) :
        if T[i] < T[i-1] :
            cond = False
            aide = T[i]
            T[i] = T[i-1]
            T[i-1] = aide
    if cond == True :
        break
print(T)


#                                 < Alghorithme >
#Var i,j,aide,n : entier
# T:Tableu:(n) : entier 
# cond : bolénne
# Debut
# T <-- [0,9,15,87,-95,2,3,1,-99999,1,2,25]
# Répeter jusqu'à:
# |  cond <-- True
# |  Pour i de 1 à n faire
# |  |    Si T[i] < T[i-1] alors
# |  |    |    cond <-- False
# |  |    |    aide <-- T[i]
# |  |    |    T[i] <-- T[i-1]
# |  |    |    T[i-1] <-- aide
# |  |    FinSi
# |  FinPour
# Jusqu'à:
#       cond = True
# Ecrire(T)
# Fin: