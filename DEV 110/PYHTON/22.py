
#                         <<<<Determiner est ce que le nombre des jours dans une annnée , 364 ou 365>>>>

year = int(input("Enter the year :"))


# 150 ==> 5*30
# 186 ==> 6*31
# 28-29    +3years_28 ==>kabisa   //    +1year_29 ==>basita     364-365
# 2000 ==> 29 février
day = 0
bas = []
kab = []


# Tableau for kabissa :
for y in range(0, year+1, 4):
    kab.append(y)
    
# Tableau for bassita :
for y in range(0, year+1):
    bas.append(y)
    


for y in range(0, len(kab)):
    for s in range(0, len(bas)):

            if year == kab[y]:
                day = 364
                nature = str("kabissa.")
                
            elif year == bas[s]:
                day = 365
                nature = str("bassita.")



print("Number of day in ",year,"is ",day,"day",nature)
