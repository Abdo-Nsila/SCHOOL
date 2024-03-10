f = float(input ("Tapez le nombre des feuilles:"))

if f <= 10 :
    p  = f*20
    print("le prix est :",p,"Rial")

else:
    if (f>10) and (f<=20) :

        p1 = 10*20
        p2 = (f -10)*15

        p = p1 + p2
        print("le prix est :",p,"Rial")

    else:
        if f>20 :

            p1 = 10*20
            p2 = 10*10
            p3 = (f-20) * 10

            p = p1+p2+p3  
            print("le prix est :",p,"Rial")
