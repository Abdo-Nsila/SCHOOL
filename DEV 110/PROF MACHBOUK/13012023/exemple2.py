# s = "zaher MEchbouk"
# lst = s.split(" ")
# for i in range(len(lst)):
#     for c in lst[i]:
#         if(c.isupper()):
#             print(c)
# mot = "test3"
# l = ['test1', 'test1', 'test2']
# if (mot not in l):
#     print(mot + ' not in list')
# else:
#     print(l.count(mot))


# -------------------------------  1  ------------------------------
# try :
#     num = int(input("Entrer un nombre : "))
# except :
#     print("L'entrer et n'est pas un entier !")


# -------------------------------  2  ------------------------------
try :
    # print(10 / 0)
    # print(x)
    # print(int("Hello"))
    print("hello"-2)
except ZeroDivisionError :
    print("Can't divide by Zero")
except NameError :
    print("Variable is not defined")
except ValueError :
    print("Value is not correct")
except :
    print("Erreur Happens")
else :
    print("Erreur")
finally :
    print('Programme Is End')










