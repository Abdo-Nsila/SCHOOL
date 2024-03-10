T = [0,9,15,87,-95,2,3,1,-99999,1,2,25]

n = len(T)
for j in range(1,n) :
    select = T[j]
    i = j-1
    while (i >= 0) and (T[i] > select) :
        T[i+1] = T[i]
        i -= 1
    T[i+1] = select
print(T)

#                                 < Alghorithme >
# Var i,j,select : entier
#     T:Tableu:(n) : entier 
# Debut
# |T <-- [0,9,15,87,-95,2,3,1,-99999,1,2,25]
# |Pour i in range(1,n) faire
# ||   select <-- T[j]
# ||   i <-- j-1
# ||    TantQue (i >= 0) et (T[i] > select) faire
# ||    |    T[i+1] <-- T[i]
# ||    |    i <-- i - 1
# ||    FinTQ
# ||    T[i+1] <-- select
# |FinPour
# |print(T)
# Fin 