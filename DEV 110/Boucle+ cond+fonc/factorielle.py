a = int(input(" a :"))
b = int(input(" b :"))
op = int(input(" Entrer l'operation [+ --> 1],[ - --> 2],[ x --> 3],[ / --> 4] :"))






def somme(a,b) :
    c = a+b
    print(a,"+",b,"=",c)


def soustraction(a,b) :
    c = a-b
    print(a,"-",b,"=",c)


def multiplication(a,b) :
    c = a*b
    print(a,"*",b,"=",c)
    return c


def division(a,b) :
    c = a/b
    print(a,"/",b,"=",c)
    return c


if op == 1 :
    somme(a,b)


if op == 2 :
    soustraction(a,b)


if op == 3 :
    multiplication(a,b)


if op == 4 :
    division(a,b)


# x = [3,45,20,10,10,25,36,14,10,95,47]
# print(len (x))