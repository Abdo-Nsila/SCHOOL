imax = -1
max = 0
i = 1

while i <= 20  :
    a = int(input("Tapez le nombre " + str(i) ))
    if a > max :
          max = a
          imax = i
    i = i+1




print("Le grand nombre est :", max)
print("La position :",imax)

