def pgdc(x, y):
    while (x % y != 0):
        r = x % y
        x = y
        y = r
    print("PGDC de (", x, " et ", y, " ) est ", y)


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
pgdc(n1, n2)
