year = int(input("Entrer L'année :"))
m1 = str(input("Entrer le mois :"))
j = int(input("Entrer le jour :"))
p = int(input("Entrer nombre de jours que voulait vous ajouter :"))

r = 0

if j == 30 :
    j = 1
    for i in range(1,p+1) :
        if j < 30 :
            j = j + 1
            r = p - i
# 30 ==> 1
        elif r != 0 :
            j = 1
            for x in range(1,p+1) :    
                j = j + 1
                if j >= 30 :
                    continue
                break





elif j != 30 :              
    for i in range(1,p+1) :
        if j < 30 : 
            j = j + 1                  
            r = p - i
# 30 ==> 1
        elif r != 0 :
            j = 1
            for x in range(1,p) :    
                j = j + 1
                if j >= 30 :     # Si j=30 en doit répeter au nouveau toute la boucle
                    continue
                break



print(j)