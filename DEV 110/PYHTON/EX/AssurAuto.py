age = int(input("Age:"))
p = int(input("Permit:"))
a = int(input("Accident:"))
c = int(input("Contrat:"))


if age<25 and p<2 :
    if c==0 :
        x="Tarif rouge"
    else :
        x="Refusée"



elif (age<25 and p>2) or (age>=25 and p<2) :
    if c==0 :
        x="Tarif orange"
    elif c==1 :
        x="Tarif rouge"
    elif c>1 :
        x="Refusée"



elif age>=25 and p>=2 :
        if c==0 :
            x="Tarif vert"
        elif c==1 :
            x="Tarif orange"
        elif c==2 :
            x="Tarif rouge"         
        elif c>2 :
            x="Refusée" 


if c>=1 :
    if x=="Tarif rouge" :
        x="Tarif orange" 

    elif x=="Tarif orange" :
        x="Tarif vert"

    elif x=="Tarif vert" :   
        x="Tarif bleu" 
    
print(x)