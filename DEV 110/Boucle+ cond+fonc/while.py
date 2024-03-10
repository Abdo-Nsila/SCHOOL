
imax = 1
a = int(input("Tapez le nombre 1 :"))
max = a 
i = 2

while (a != 0)  :
    a = int(input("Tapez le nombre :"))
    if a > max :
        max = a
        imax = i
    i = i+1




print("Le grand nombre est :", max)
print("La position :",imax)
