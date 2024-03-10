
year = int(input("year :"))



r = 0
j1 = 3
m1 = "avril"

p = 0
years = year

for y in range(2022,year) :
    if j1 != 1 :
        for i in range(1,14) :
            if j1 != 1 :
                j1 = j1 - 1
                p = 13 - i 

            elif p != 0 :
                j1 = 30
                if m1 == str("décembre"):
                    m1 = str("novembre")
                elif m1 == str("novembre"):
                    m1 = str("octobre")
                elif m1 == str("octobre"):
                    m1 = str("septembre")
                elif m1 == str("septembre"):
                    m1 = str("aout")
                elif m1 == str("aout"):
                    m1 = str("juillet")
                elif m1 == str("juillet"):
                    m1 = str("juin")
                elif m1 == str("juin"):
                    m1 = str("mai")
                elif m1 == str("mai"):
                    m1 = str("avril")
                elif m1 == str("avril"):
                    m1 = str("mars")
                elif m1 == str("mars"):
                    m1 = str("février")
                elif m1 == str("février"):
                    m1 = str("janvier")
                elif m1 == str("janvier"):
                    m1 = str("décembre")
                    year = year - 1 


    if j1 == 1 :
        j1 = 30
        if m1 == str("décembre"):
                    m1 = str("novembre")
        elif m1 == str("novembre"):
                    m1 = str("octobre")
        elif m1 == str("octobre"):
                    m1 = str("septembre")
        elif m1 == str("septembre"):
                    m1 = str("aout")
        elif m1 == str("aout"):
                    m1 = str("juillet")
        elif m1 == str("juillet"):
                    m1 = str("juin")
        elif m1 == str("juin"):
                    m1 = str("mai")
        elif m1 == str("mai"):
                    m1 = str("avril")
        elif m1 == str("avril"):
                    m1 = str("mars")
        elif m1 == str("mars"):
                    m1 = str("février")
        elif m1 == str("février"):
                    m1 = str("janvier")
        elif m1 == str("janvier"):
                    m1 = str("décembre")
                    year = year - 1  
        for i in range(1,13) :
            if j1 != 1 :
                j1 = j1 - 1





































r = 0
m = m1
j = j1


if j == 30:
    j = 1

    if m == str("décembre"):
            m = str("janvier")
            years = year + 1
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
    for i in range(1,30) :
        if j < 30 :
            j = j + 1
            r = p - i
# 30 ==> 1
        elif r != 0 :
            j = 1
            if      m == str("décembre") :
                m = str("janvier")
                years = year + 1
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
    for i in range(1,30) :
        if j < 30 : 
            j = j + 1                  
            r = p - i
# 30 ==> 1
        elif r != 0 :
            j = 1
            if      m == str("décembre") :
                m = str("janvier")
                years = year + 1
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

if years > year :
    years = year + 1

print(j1,str(m1),year)
print(j,str(m),years)