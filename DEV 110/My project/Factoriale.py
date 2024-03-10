num = int(input("Entrer un nombre :"))



f = 1
fm =  str(1) + "X"
for i in range(1,num+1) :
    f = f*i
    if i==1 :
        continue

    if i < num :
        fm = fm + str(i) + "X" 
    elif i == num :
        fm = fm + str(i) 






print(fm,"=",f)