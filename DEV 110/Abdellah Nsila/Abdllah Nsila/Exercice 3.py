#                          <<<<    Exercice 3 :   >>>>
# Créer un fichier :
f = open("C:\\Users\\aa\\Desktop\\myfile.txt","x",encoding="utf8")
f.close()


f = open("C:\\Users\\aa\\Desktop\\myfile.txt","w",encoding="utf8")
f.write( "Python est un langage de programmation souple et flexible.\n")
f.close()

f = open("C:\\Users\\aa\\Desktop\\myfile.txt","a",encoding="utf8")
f.write("Ce contenu a été ajouté via un code Python !\n")
f.close()

f = open("C:\\Users\\aa\\Desktop\\myfile.txt","r",encoding="utf8")
print(f.read())
f.close()