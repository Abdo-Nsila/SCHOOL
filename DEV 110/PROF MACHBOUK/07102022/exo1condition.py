x = float(input("x="))
y = float(input("y="))

if ((x > 0) and (y > 0)) or ((x < 0) and (y < 0)):
    print("le produit des deux nombres ", x, " et ", y, " est positif")
else:
    print("le produit des deux nombres ", x, " et ", y, " est négatif")
