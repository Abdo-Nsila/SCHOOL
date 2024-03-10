def pgdc(x, y):
    while (x % y != 0):
        r = x % y
        x = y
        y = r
    return y


def estPremierEntreEux(x, y):
    '''
    Code de l'algo à écrire:

    retourner Vrai si x et y sont premiers entre eux
            Faux  sinon
   '''
    pass


while True:
    x = int(input("x : "))
    if (x > 0):
        break
while True:
    y = int(input("y : "))
    if (y > 0):
        break
if (x > y):
    n1 = x
    n2 = y
else:
    n2 = x
    n1 = y
p = pgdc(n1, n2)
print("PGDC de (", x, " et ", y, " ) est ", p)
