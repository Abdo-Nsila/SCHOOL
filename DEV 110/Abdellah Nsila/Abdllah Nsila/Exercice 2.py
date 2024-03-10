#                          <<<<    Exercice 2 :   >>>>
# Créer un fichier :
f = open("C:\\Users\\aa\\Desktop\\myfile.txt","x",encoding="utf8")
f.close()


f = open("C:\\Users\\aa\\Desktop\\myfile.txt","w",encoding="utf8")
f.writelines(['Ligne numéro 1\n','Ligne numéro 2\n','Ligne numéro 3\n','Ligne numéro 4\n','Ligne numéro 5\n'])
f.close()


# f = open("C:\\Users\\aa\\Desktop\\myfile.txt","w")
# f.writelines(['Ligne numéro 1\n','Ligne numéro 2\n', 'désolé ! Le contenu de cette ligne a été changé !\n','Ligne numéro 4\n','Ligne numéro 5\n'])
# f.close()

f = open("C:\\Users\\aa\\Desktop\\myfile.txt","r",encoding="utf8")
l = f.readlines()
f.close()


l[2] = 'désolé ! Le contenu de cette ligne a été changé !\n'


f = open("C:\\Users\\aa\\Desktop\\myfile.txt","w",encoding="utf8")
f.writelines(l)
f.close()

f = open("C:\\Users\\aa\\Desktop\\myfile.txt","r",encoding="utf8")
print(f.read())
f.close()