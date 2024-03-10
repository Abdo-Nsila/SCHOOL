pointeur1 = open("../dossier1/dossier2/file.txt", "r", encoding='utf-8')
for i in range(6):
    print(pointeur1.read(10))
    pointeur1.seek(pointeur1.tell()+2)

# for ligne in pointeur1:
#     print(ligne, end='')
# while (True):
#     str = pointeur1.readline()
#     if (not str):
#         break
#     print(str, end='')
# tab = pointeur1.readlines()
# for i in range(len(tab)):
#     print(tab[i])
# pointeur1.seek(10)

# print(pointeur1.read(2))
# print(pointeur1.read(2))
# pointeur1.seek(pointeur1.tell()+2)
# print(pointeur1.read(2))
# print(pointeur1.read(2))
# for i in range(2000):
#     pointeur1.write("{}".format(i))
#     if (i % 20 == 0):
#         pointeur1.write("\n")
# pointeur1.write("salut\nça va?")
# print("___________________________", file=pointeur1)
pointeur1.close()
