
def  EstEntier(num) :
    t=[0]
    for y in range(1,num+1) :
        x = num
        while (x % y != 0):
            r = x % y
            x = y
            y = r
        if y == 1 :
            t[0]=1
        elif y == num :
            t.insert(1,num)
        else :
            t.append(y)


    if len(t) == 2 :
        print("Le nombre ",num,"est Premier")
    else :
        print("!! Le nombre ",num,"n'est pas Premier !!")


while True:
    x = int(input("Entrer le nombre : "))
    if (x > 1):
        num = x
        break

EstEntier(num)
# print("PGDC de (", x, " et ", y, " ) est ", n2)
