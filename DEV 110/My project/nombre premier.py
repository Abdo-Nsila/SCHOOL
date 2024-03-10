# num = int(input("Entrer un nombre :"))

# for x in range(1,num+1,2) :
#     if num == x :
#         print("Le nombre :" + str(num) + " est premier.")

# if num != x :
#     print("Le nombre :" + str(num) + " n'est pas premier.")



t1 = []
t2 = []
for i in range(1, 11):
    
        num = int(input("Entrer le nombre numéro "+str(i)+":"))
        t1.append(num)
        for x in range(0, len(t1)):
            d = num % 2
        if d != 0:
            t2.append(num)

print("Les nombres :", t2 , " sont premiers.")
