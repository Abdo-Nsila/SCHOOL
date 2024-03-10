t = [6,4,3,5,2,2,6,4,3,5,2,6,4,3,5,2]
n = len(t)
# remplissage
# n = int(input("Donner la taille du tableau :"))
# print("Donner", n, "Nombres")
# for i in range(n):
#     num = int(input("Nombre numéro " + str(i+1) + " : "))
#     t.append(num)
# print("le tableau avant le tri est", t)

# Tri
for i in range(0, n-1):
    min = t[i]
    pos = i
    for j in range(i+1, len(t)):
        if t[j] < min:
            min = t[j]
            pos = j
    if min != t[i]:
        aide = t[i]
        t[i] = min  # t[pos]
        t[pos] = aide

# affichage
print("Tableau final :")
print(t)
