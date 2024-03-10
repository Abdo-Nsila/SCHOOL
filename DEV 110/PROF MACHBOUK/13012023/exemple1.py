#__________Gestion de quelques type d'erreurs Sémantique______#
# 1-erreur de valeur (conversion entre types incompatibles)
# try:  # ESSAYER DE TROUVER UNE ERREUR
#     x = int(input("x:"))
#     print(x)
# except Exception as e:  # INTERCEPTER L'ERREUR (CATCH)
#     print(type(e))
#     print(e)

# print("Merci pour la saisie")


# #2-division par zero
# try:  # ESSAYER DE TROUVER UNE ERREUR
#     x=9/0
#     print(x)
# except Exception as e:  # INTERCEPTER L'ERREUR (CATCH)
#     print(type(e))
#     print(e)

# print("Merci pour la saisie")

# # 3-indice hors limite d'une liste
# try:  # ESSAYER DE TROUVER UNE ERREUR
#     x = [12, -10, 0]
#     print(x[5])
# except Exception as e:  # INTERCEPTER L'ERREUR (CATCH)
#     print(type(e))
#     print(e)


# print("Merci pour la saisie")

# 4-erreur sur le fichier
try:  # ESSAYER DE TROUVER UNE ERREUR
    f = open("file1.txt", "w", encoding='utf8')
    f.write("Salut\n")
    f.write(2/0)
    f.write("test")
except Exception as e:  # INTERCEPTER L'ERREUR (CATCH)
    print(type(e))
    print(e)
finally:
    f.close()

print("Merci pour la saisie")
