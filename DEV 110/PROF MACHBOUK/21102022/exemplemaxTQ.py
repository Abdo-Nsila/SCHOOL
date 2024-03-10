a=int(input("Entrer numéro 1 : "))
max=a
indicemax=1
i=1
while(a!=0):
    a=int(input("Entrer numéro "+str(i+1)+ " : "))
    if(a>max):
        max=a
        indicemax=i+1
    i+=1
print("Max : ",max,"  - indice Max : ",indicemax )