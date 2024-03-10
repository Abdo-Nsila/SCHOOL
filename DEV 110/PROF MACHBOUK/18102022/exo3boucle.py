import math

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
if (a == 0):
    if (b != 0):
        print(b, "x+", c, "=0", sep="")
        print("la solution est ", -c/b)
    else:
        print("aucune solution")
else:
    print(a, "x^2+", b, "x+", c, "=0", sep="")

    delta = b**2-4*a*c
    if (delta < 0):
        print("pas de solution dans R")
        # z1 = complex(round(-b/2*a, 2), round(+math.sqrt(-delta)/(2*a), 2))
        # z2 = complex(round(-b/2*a, 2), round(-math.sqrt(-delta)/(2*a), 2))
        # print("l'équation admet deux racines : ",
        #       z1, " | ", z2, 2)

    elif (delta == 0):
        r = -b/(2*a)
        print("l'équation admet une racine double : ", round(r, 2))
    else:
        r1 = (-b+math.sqrt(delta))/(2*a)
        r2 = (-b-math.sqrt(delta))/(2*a)
        print("l'équation admet deux racines : ",
              round(r1, 2), " | ", round(r2, 2))
