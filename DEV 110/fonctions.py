# def max_min(a,b) :
#     if a > b :
#         max = a
#     else :
#         max = b
#         return(max)

# a = int(input("Entrer le 1 nombre :"))
# b = int(input("Entrer le 2 nombre :"))

# print("Le plus grand nombre est :" , max(a,b) )

year = int(input("year :"))
j1 = 3
m1 = "avril"
t=[1,2,3,4,5,6,7,8,9,10]
for y in range(2022,year) :
    
    
        for i in range(1,14) :
            if j1 != 0 :
                j1 = j1 - 1
                p = 13 - i
                print(j1)
            elif p != 0 :
                j1 = 30
                for i in range(1,p+1) :
                    j1 = j1 - 1
                    p = p - 1
                    print(p)
                    if p == 0 :
                        break

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

print(j1,str(m1),year)
