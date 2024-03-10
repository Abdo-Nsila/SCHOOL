 #                                       < Assurance AutoMobile >

age = float(input("Vote age :")) 
permit = float(input("Entré la durée du permit en année:"))
accident = float(input("Le nombre d'accident:"))
c = int(input("Vous avez terminer la contrat (si oui tapez:1) (si non tapez:0)  :"))
b = int(input("Vous avez une tarif bleu (si oui tapez:1) (si non tapez:0) : "))



b =(b == 1) 

age1 = (age < 25)
age2 = ( age >= 25)

p = (permit < 2)
p1 = (permit >= 2)

a = (accident == 0)
a1 = (accident == 1)
a2 = (accident == 2)
a3 = (accident > 2)
a4 = (accident == 3)
a5 = (accident > 3)
a6 = (accident > 1)
a7 = (accident == 4)
a8 = (accident > 4)

c1 = (c == 1)
c2 = (c == 0)


if (age1 and p and a and c2) or (age1 and p1 and a1 and c2 ) or (age2 and p and a1 and c2) or (age2 and p1 and a7 and c1 and b) or (age1 and p1 and a2 and c1) or (age2 and p and a2 and c1 ) or (age2 and p1 and a4 and c1) or (age1 and p and a1 and c1) or (age2 and p1 and a2 and c2 ) :
    print("Le tarif rouge")


elif (age1 and p1 and a and c2) or (age2 and p and a and c2) or (age2 and p1 and a1 and c2) or (age1 and p and a and c1) or (age2 and p1 and a4 and c1 and b) or (age1 and p1 and a1 and c1) or (age2 and p and a1 and c1) or (age2 and p1 and a2 and c1) or (age1 and p1 and a and c1) :
        print("Le tarif orange")


elif (age2 and p1 and a and c2) or (age2 and p1 and a2 and c1 and b) or (age2 and p1 and a1 and c1) or (age2 and p and a and c1) :
            print("Le tarif vert")


elif (age2 and p1 and a and c1) or (age2 and p1 and a1 and c1 and b) :
                print("Le tarif bleu")


elif (age1 and p and a6 and (c2 or c1)) or (age1 and p1 and a3 and (c2 or c1)) or (age2 and p and a6 and (c2 or c1)) or (age2 and p1 and a8 and c1 and b ) or (age1 and p1 and a3 and (c1 or c2)) or (age2 and p and a3 and (c1 or c2)) or (age2 and p1 and a8 and (c1 or c2)) or (age2 and p1 and a5 and (c1 or c2)) :
                    print("L'assurance est refusé")

