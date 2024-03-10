#                          <<<<    Exercice 5 :   >>>>
# Créer un fichier :
f = open("C:\\Users\\aa\\Desktop\\myfile.txt","x",encoding="utf8")
f.close()


f = open("C:\\Users\\aa\\Desktop\\myfile.txt","w",encoding="utf8")
f.write( "Python est le meilleur langage de programmation")
f.close()


f = open("C:\\Users\\aa\\Desktop\\myfile.txt","r",encoding="utf8")
l = f.read()
f.close()


l = l.split(" ")
l.pop(4)
l = " ".join(l)

f = open("C:\\Users\\aa\\Desktop\\myfile.txt","w",encoding="utf8")
f.write(l)
f.close()

f = open("C:\\Users\\aa\\Desktop\\myfile.txt","r",encoding="utf8")
print(f.read())
f.close()