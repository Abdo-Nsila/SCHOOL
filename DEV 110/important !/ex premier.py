
# num = int(input("num : "))

# def prochainepremier(num) : 
#     for j in range(num+1,100) :   
#         for i in range(2,j-1) :
#             num = x
#             if (num % i == 0) :
#                 print("Le nombre",i,"n'est pas premier")
#                 break


# prochainepremier(num)

def somme(a,b):
    c = a + b
    return c

num = int(input('Enter num :'))

c = 0
for i in range(1,num+1) :
    c = somme(c, i)
    


print("L somme des entier de ",1," à ",num," est :  ",c)



# Exercice de prochaine entier