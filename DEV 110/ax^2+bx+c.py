
#                                   <<<< Equation de second degré : ax^2+bx+c=0 >>>>

a = float((input("Tapez a :")))
b = float((input("Tapez b :")))
c = float((input("Tapez c :")))

from math import *


if a == 0 :
    X0 = -c / b
    print("L'équation admet une seule solution X0 =",X0)

elif c == 0 :
    X1 = 0
    X2 = -b / a
    print("L'équation admet 2 solutions:","X1 =",X1,"and","X2 =",X2)


elif (a != 0) and (c!=0) :
    d = (b*b)-4*a*c
    print("Delta =",d)



    if d < 0 :
        print("L'équation n'admet aucune solution")



    elif d == 0 :
        X0 = -b / 2*a
        print("L'équation admet une seule solution X0 =",X0)


    elif d > 0 :
        X1 = (-b + sqrt(d)) / (2*a)
        X2 = (-b - sqrt(d)) / (2*a)
        print("L'équation admet 2 solutions:","X1 =",X1,"and","X2 =",X2)
