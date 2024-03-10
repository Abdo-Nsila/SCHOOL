def estPremier(num):
    # estPremier(num:entier)
    # var i:entier
    # debut
    # pour i de 2 à num-1 faire
    for i in range(2, num):
        # si(num mod i=0 )alors
        if (num % i == 0):
            #Ecrire(num, " n'est pas premier")
            # print(num, " n'est pas premier")
            # retourner
            return False
    #Ecrire(num, " est  premier")
    # print(num, " est premier")
    return True


    # fin
'''
Cette procédure sert à extraire les nombres premiers à partir
d'un nombre entier passer en paramètre'''


def extraireNbrsPremier(x):
    for i in range(2, x+1):
        if (estPremier(i) == True):
            print(i, end="|")


while (True):
    x = int(input("x="))
    if (x > 1):
        break
if (estPremier(x) == True):
    print(x, " est premeir")
else:
    print(x, "n'est pas premeir")
extraireNbrsPremier(x)
