

# In 2022 [ 3 avril -  2 mai ]
# -13 jours
# 1 moi ==> 30
#
#
#
#
year = int(input("Enter the year :"))


# t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


r = 0
j1 = 3
m1 = "avril"
year0 = year


for p in range(2022, year0):
    if j1 != 0:

        for p in range(1, 14):
            if j1 > 0:
                j1 = j1 - 1
                r = 14 - p
            # 30 ==> 1
            elif r != 0:
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

            for x in range(1, r+1):
                    m = m1
                    j1 = j1 - 1
                    break



year1 = year0

for p in range(2022, year0):


    
    r = 0

    if m1 == str("décembre"):
                m1 = str("janvier")
                year1 = year0 + 1
    elif    m1 == str("janvier") :
                m1 = str("février")
    elif    m1 == str("février") :
                m1 = str("mars")
    elif    m1 == str("mars") :
                m1 = str("avril")
    elif    m1 == str("avril") :
                m1 = str("mai")
    elif    m1 == str("mai") :
                m1 = str("juin")
    elif    m1 == str("juin") :
                m1 = str("juillet")
    elif    m1 == str("juillet") :
                m1 = str("aout")
    elif    m1 == str("aout") :
                m1 = str("septembre")
    elif    m1 == str("septembre") :
                m1 = str("octobre")
    elif    m1 == str("octobre") :
                m1 = str("novembre")
    elif    m1 == str("novembre") :
                m1 = str("décembre")



    if j1 == 30:
        j2 = 0
    
        # if      m1 == str("décembre"):
        #         m1 = str("janvier")
        #         year2 = year + 1
        # elif    m1 == str("janvier") :
        #         m1 = str("février")
        # elif    m1 == str("février") :
        #         m1 = str("mars")
        # elif    m1 == str("mars") :
        #         m1 = str("avril")
        # elif    m1 == str("avril") :
        #         m1 = str("mai")
        # elif    m1 == str("mai") :
        #         m1 = str("juin")
        # elif    m1 == str("juin") :
        #         m1 = str("juillet")
        # elif    m1 == str("juillet") :
        #         m1 = str("aout")
        # elif    m1 == str("aout") :
        #         m1 = str("septembre")
        # elif    m1 == str("septembre") :
        #         m1 = str("octobre")
        # elif    m1 == str("octobre") :
        #         m1 = str("novembre")
        # elif    m1 == str("novembre") :
        #         m1 = str("décembre")
        for i in range(1,30) :
            if j2 < 30 :
                j2 = j2 + 1
                r = p - i
            # 30 ==> 1
            elif r != 0 :
                j2 = 0
                for x in range(1,r) :    
                    j2 = j + 1
                    if j2 >= 30 :
                        continue
                    break




    elif j1 != 30 :  
        j2 = j1            
        for i in range(1,30) :
            if j2 < 30 : 
                j2 = j1 + 1                  
                r = p - i
            # 30 ==> 1
            elif r != 0 :
                j2 = 0
                
                for x in range(1,r) :    
                    j2 = j2 + 1
                    if j2 >= 30 :     # Si j=30 en doit répeter au nouveau toute la boucle
                        continue
                    break












j3 = j2 -1
# "Ramadan a ",year,"va être a :" 
# +"en",year2

print( j1 , str(m), year )
print(j3,"-",j2 , str(m1), year1 )




