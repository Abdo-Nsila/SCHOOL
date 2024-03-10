def estPremier(y):
    for i in range(2, y):
        if (y % i == 0):
            return False
    return True

def prochaine(x) :
    while True :
        x = x + 1
        if estPremier(x) == True :
            return x 
            break

while (True):
    num = int(input("Number = "))
    if (num > 1):
        break

print("Le premier prochaine est ",prochaine(num))


