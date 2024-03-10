#Passage par valeur ENTIER
def Modifier(a):
    a=a+1
    return a
X=int(input("X : "))
#X=Modifier(X)
Modifier(X)
print(X)