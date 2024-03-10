m = int(input("Mois : "))

if ((m == 12) or (m == 1) or (m == 2)):
    print("Hiver")
else:
    if ((m == 3) or (m == 4) or (m == 5)):
        print("Printemps")
    else:
        if ((m == 6) or (m == 7) or (m == 8)):
            print("Eté")
        else:
            if((m == 9) or (m == 10) or (m == 11)):
                print("Automne")
            else:
                print("mois incorrecte")
