lignes = [['Nom', 'Prénom', 'Age'], ['Benhanouch', 'hatim', 58], ['Ait abdellah', 'ismail', 13]]

ptrWrite = open("file.csv", 'w', encoding='utf')
for i in range(len(lignes)):
    lignes[i][2] = str(lignes[i][2])+'\n'
    colone = lignes[i]
    l = ";".join(colone)
    ptrWrite.writelines(l)
ptrWrite.close()
