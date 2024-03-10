N = int(input("Entrer le nmobre de fois :"))

n = 1
max = 0
min = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999






while n <= N :
        
        for q in range(1,5) :
            
            a = int(input("Entrer le nmobre :" + str(q) + " dans N " + str(n) + ":") )
            
            if a > max  :
                max = a


            if a < min  :
                min = a

        print( "Le grand nombre",max )
        print( "Le petit nombre",min )

        n += 1

        if n < N :
            max = 0
            min = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999


if a > max :
    max = a

if a < min :
    min = a


print( "Le plus grand nombre",max )
print( "Le Plus petit nombre",min )
