a = int(input("Entrer un nombre :"))
n = int(input("Entrer un intervalle maximale :"))

s = 0

if a > 0 :
    for x in range(1,n+1) :
        s = a % x
        if s == 0 :
            print("Le nombre ",x," est un diviseur de ",a) 