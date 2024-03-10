#Passage par référence ENTIER 
def Modifier(a):
    a[0]=a[0]+1
    
X=[int(input("X : "))]
 
Modifier(X)
print(X)