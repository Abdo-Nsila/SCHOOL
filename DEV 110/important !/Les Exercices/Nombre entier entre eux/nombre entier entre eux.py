def pgdc(x, y):
    while (x % y != 0):
        r = x % y
        x = y
        y = r
    return y


def estPremierEntreEux(x, y):
    if p == 1 :
        print("          Les nombres ",x,"et",y,"sont entier entre eux            ")
    else :
        print("      ):  Les nombres ",x,"et",y,"ne sont pas entier entre eux  ): ")


while True:
    x = int(input("Entrer le Nombre 1 : "))
    if (x > 0):
        break
while True:
    y = int(input("Entrer le Nombre 2  : "))
    if (y > 0):
        break
if (x > y):
    n1 = x
    n2 = y
else:
    n2 = x
    n1 = y

p = pgdc(n1, n2)

print("||------------------------------------------------------||")
print("||   PGDC de (", x, " et ", y, " ) est : ", p,"                  ||")
print("||------------------------------------------------------||")
estPremierEntreEux(x, y)

