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
while (n1 % n2 != 0):
    r = n1 % n2
    n1 = n2
    n2 = r
print(n2)
print("PGDC de (", x, " et ", y, " ) est ", n2)
