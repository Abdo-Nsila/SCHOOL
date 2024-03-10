

monnaie = int(input("Entrer La valeur d'argent :"))



s = 4000+2000+800+2000+1000+700+300+400+2000+1000+1000+1000+(1000*4)+(100*30)+(200*4)+(1000*4)

# <<< Sayer MaMa >>>

# 4000 = Wi-Fi
# 2000 = eau/Electricité
# 800 = BotaGaz
# 2000 = Farine
# 1000 = Hile d'olive
# 700 =sucre
# 300 = café
# 400 = Tawabile
# 2000 = 9atani/7rira/Chofane
# 1000 = Tide/Javile
# 1000 = Hamame
# 1000 = Bus
# (1000*+) = légumes/Souk
# (100*30) = Gouter/Youssfe-Younnnes
# (200*4) = Viande
# (1000*4) = 7anoute




a = 0
s1 = 0
i = 1



while True  :
    a = int(input("Le prix du produit Numéro"+str(i)+":"))

    if a != 0 :
        s1 = int(input("Par jours(1) ou Par semaine(7) ou Mois(30) :"))


    if s1 == 1 :
        s1 = a * 30
    elif s1 == 7 :
        s1 = a * 4

    s = s + s1
    i = i + 1

    if a == 0 :
        break
print("Le resultas :",s,"Rial")




if monnaie >= s :
    r = monnaie - s
    print("Votre argent est sufusant Le reste est :",r)

else :
    print("!!!!!!! Votre argent est insufisant !!!!!!!")



# <<< Sayer BaBa >>>

#sucre = 360
#1l hile d'olive = 460
#1/4 kg thé = 500
#Gazwal = 150
#Hile de moto = 500
#Lait = 20 * 30
#Chofane = 20 * 30
#Oeufs =24 * 30
#Frommage = 40 * 30
#Pain = 100 * 30
#Legumes = 100 *30
#BotaGaz = 400 * 30
#Eau/Electricité 1000 
#Tide 260




