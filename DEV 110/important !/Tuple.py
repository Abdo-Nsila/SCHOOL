tup1 = ('Omar',70,'Nature',99,'Omar')
print(tup1)
print("[0]",tup1[1])
print("[1]",tup1[1:])

tup2 = ('Ali',5,'Kamal',20)   # En peux pas le modifier

# Built-in list Methods/Fonctions :
tup = (20,550,150,800,30,10)
print("[2]",max(tup))
print("[3]",min(tup))

list1 = list(tup1)     # Convertire une tiple au list
# list1.append('abdo')
print("[4]",list1)

f = tuple(list1)        # Convertire unr list au tuple
print("[5]",f)

list1 = [12,52,48,7,3]
print("[6]",max(list1))
print("[7]",min(list1))

a = {1,2,'X',4}
b = {1,2, 15,'X'}

print(a.symmetric_difference(b))
