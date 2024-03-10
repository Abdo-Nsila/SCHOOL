m = str(input("Entrer le mois :"))
j = int(input("Entrer le jour :"))
p = int(input("Entrer nombre de jours que voulait vous ajouter :"))


# t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


r = 0

if j == 30:
    j = 0

    if m == str("décembre"):
            m = str("janvier")
    elif    m == str("janvier") :
                m = str("février")
    elif    m == str("février") :
                m = str("mars")
    elif    m == str("mars") :
                m = str("avril")
    elif    m == str("avril") :
                m = str("mai")
    elif    m == str("mai") :
                m = str("juin")
    elif    m == str("juin") :
                m = str("juillet")
    elif    m == str("juillet") :
                m = str("aout")
    elif    m == str("aout") :
                m = str("septembre")
    elif    m == str("septembre") :
                m = str("octobre")
    elif    m == str("octobre") :
                m = str("novembre")
    elif    m == str("novembre") :
                m = str("décembre")
    for i in range(1,p+1) :
        if j < 30 :
            j = j + 1
            r = p - i
# 30 ==> 1
        elif r != 0 :
            j = 0
            if      m == str("décembre") :
                m = str("janvier")
            elif    m == str("janvier") :
                m = str("février")
            elif    m == str("février") :
                m = str("mars")
            elif    m == str("mars") :
                m = str("avril")
            elif    m == str("avril") :
                m = str("mai")
            elif    m == str("mai") :
                m = str("juin")
            elif    m == str("juin") :
                m = str("juillet")
            elif    m == str("juillet") :
                m = str("aout")
            elif    m == str("aout") :
                m = str("septembre")
            elif    m == str("septembre") :
                m = str("octobre")
            elif    m == str("octobre") :
                m = str("novembre")
            elif    m == str("novembre") :
                m = str("décembre")

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
            j = 0
            if      m == str("décembre") :
                m = str("janvier")
            elif    m == str("janvier") :
                m = str("février")
            elif    m == str("février") :
                m = str("mars")
            elif    m == str("mars") :
                m = str("avril")
            elif    m == str("avril") :
                m = str("mai")
            elif    m == str("mai") :
                m = str("juin")
            elif    m == str("juin") :
                m = str("juillet")
            elif    m == str("juillet") :
                m = str("aout")
            elif    m == str("aout") :
                m = str("septembre")
            elif    m == str("septembre") :
                m = str("octobre")
            elif    m == str("octobre") :
                m = str("novembre")
            elif    m == str("novembre") :
                m = str("décembre")

            for x in range(1,p+1) :    
                j = j + 1
                if j >= 30 :     # Si j=30 en doit répeter au nouveau toute la boucle
                    continue
                break

            # if      m == str("décembre") :
            #     m = str("janvier")
            # elif    m == str("janvier") :
            #     m = str("février")
            # elif    m == str("février") :
            #     m = str("mars")
            # elif    m == str("mars") :
            #     m = str("avril")
            # elif    m == str("avril") :
            #     m = str("mai")
            # elif    m == str("mai") :
            #     m = str("juin")
            # elif    m == str("juin") :
            #     m = str("juillet")
            # elif    m == str("juillet") :
            #     m = str("aout")
            # elif    m == str("aout") :
            #     m = str("septembre")
            # elif    m == str("septembre") :
            #     m = str("octobre")
            # elif    m == str("octobre") :
            #     m = str("novembre")
            # elif    m == str("novembre") :
            #     m = str("décembre")




print(j ,"in " + str(m) )



