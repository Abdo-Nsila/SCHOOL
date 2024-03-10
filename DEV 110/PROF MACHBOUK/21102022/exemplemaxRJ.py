i=1
max=0
while(True):
    a=int(input("Entrer numéro "+str(i)+" : "))
    if(a>=max):
        max=a
        indicemax=i
    i+=1
    if(a==0):
        break

print("Max : ",max,"  - indice Max : ",indicemax )