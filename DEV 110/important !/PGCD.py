a = int(input("Entrer a :"))
b = int(input("Entrer b :"))


if a > b :
    max = a
    min = b

else :
    max = b
    min = a

a = max
b = min


r = b
while True:
    b = r
    r = a % b
    a = b
    if r == 0 :
        break

print("Le pgcd de ",max," et ",min,"est :", b)





