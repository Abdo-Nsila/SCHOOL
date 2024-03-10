T = [4,8,3,6,99,60,20,7,4,80,30]

for i in range(len(T)-1) :
    cond = False
    min = T[i]
    pos0 = i
    for j in range(i+1,len(T)) :
        if T[j] < min :
            min = T[j]
            pos1 = j
            cond = True
    if cond == True :
        aide = T[pos0]
        T[pos0] = min
        T[pos1] = aide
print(T)

#                                 < Alghorithme >

# Var min,pos0,pos1,aide,n,i,j  : Entier
#     T:Tableau(n):entier
#     cond : bolénne
# Debut
# |T <-- [0,9,15,87,-95,2,3,1,-99999,1,2,25]
# |  Pour i de 0 à n-1 faire
# |  |    cond <-- False
# |  |    min <-- T[i]
# |  |    pos0 <-- i
# |  |    Pour j de i+1 à n faire
# |  |    |    Si T[j] < min alors
# |  |    |    |    min <-- T[j]
# |  |    |    |    pos1 <-- j
# |  |    |    |    cond <-- True
# |  |    |    FinSi
# |  |    FinPour
# |  |Si cond = True alors
# |  ||    aide <-- T[pos0]
# |  ||    T[pos0] <-- min
# |  ||    T[pos1] <-- aide
# |  |FinSi
# |  FinPour
# |Ecrire(T)
# Fin: