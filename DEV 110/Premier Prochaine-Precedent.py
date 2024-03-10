def premier(x) :
    cond = True
    for i in range(2,x) :
        if x % i == 0 :
            cond = False
            break
    return cond


def premierprochaine(y) :
    while True :
        y = y + 1
        if premier(y) == True :
            return y
            break


def premierprecedent(y) :
    while True :
        y = y - 1
        if premier(y) == True :
            return y
            break



while True :
    print("")
    print("----------------------------------------------------------------------")
    num = int(input("Enter a Number : "))

    print("Le nombre ", "|" ,premierprochaine(num) , "|" , " est le premier prochaine .")
    print("Le nombre ", "|" ,premierprecedent(num), "|" , " est le premier precedent .")



# if premier(num) == False :
#     a = premier(num)
#     print(a)
#     print("NoN premier")
# else :
#     a = premier(num)
#     print(a)
#     print("Oui premier")

