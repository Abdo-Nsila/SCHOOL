num = int(input("Entrer le nombre :"))


if (num > 0):
    t=[]
else :
        num = int(input("Entrer le nombre :"))



for i in range(1,999) :
        
            r = num % i
            num = i
            i = r
            if r == 0 :
                t.append(i)
            
print(t)
                
