#                          <<<<    Exercice 1 :   >>>>
# Créer un fichier :
f = open("C:\\Users\\aa\\Desktop\\monfichier.txt","x",encoding="utf8")
f.close()


# Ecrire un text dans ce fichier
f = open("C:\\Users\\aa\\Desktop\\monfichier.txt","w",encoding="utf8")
f.write("Python est un langage deprogrammation orienté objet")
f.close()


f = open("C:\\Users\\aa\\Desktop\\monfichier.txt","r",encoding="utf8")
print(f.read())
f.close()
