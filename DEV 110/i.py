n = int(input("Tapez n :"))


a = 0
for i in range(1,n+1) :
    a =(1/i) + a
print("La somme est :",a)

b = 0
for i in range(1,n,-1 ) :
    b = (1/i) + b
print("La somme est :",b)
