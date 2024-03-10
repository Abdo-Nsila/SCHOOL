

max = 0 
i = 1

while (False) :
        a = int(input("Tapez le nombre " +str(i) +":" ) )
        if a >= max :
                max = a
                imax = i
        if (a == 0) :
            break
        
        i += 1




print("Le grand nombre est :", max)
print("La position :",imax)
