
#                        <<       Exercice Etoile     ___     Triangle      ____       Triangle de Pascale      >>


def etoile(n) :
    for i in range(1,n) :
        print("*"*i)

print(" ")
n = int(input("<<------Nombre de ligne------> : "))


print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("<------------Etoile------------->")
print(" ")

etoile(n)

# * 
# **
# ***
# ****






print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("<------------Tiangle_slach------------->")
print(" ")

def tiangle_slach(n) :
    x = n+1   
    c = 0
    for i in range(0,n) :
        x = x - 1                     
        if i < n-1 :
            print(" "*x+"/"+" "*(c)+"\\")
            c = c + 2
        elif i == n-1 :
            print(" "*x+"/"+"_"*(c)+"\\")

tiangle_slach(n)


#    /\
#   /  \
#  /    \
# /______\







print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("<------------Triangle_etoile------------>")
print(" ")

def triangle_etoile(n) :
    x = n+1   
    for i in range(0,n) :
        x = x - 1                     
        print(" "*x  +("* ")*(i))

triangle_etoile(n)


#     *
#    * *
#   * * *
#  * * * *





print(" ")
print(" ")
print(" ")
print(" ")
print("<----------Triangle De Pascale---------->")
print(" ")

def pascale(ligne) :
    ligne = ligne - 2
    T = [[1],[1,1]]
    for i in range (1,ligne+1) : 
        t = []
        for j in range ( (len(T[i]))-1 ) :
            if j == 0 :
                t.append(1)
            s = T[i][j] + T[i][j+1]
            t.append(s)
        t.append(1)
        T.append(t)

    for k in range(len(T)) :
        print(T[k])
    print(" ")

pascale(n)
