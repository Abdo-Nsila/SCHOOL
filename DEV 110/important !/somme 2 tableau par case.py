# t1=[2,8,60,98]   t1[0]²
# t2=[78,24,18,3]  t2[0]
# t3=[80,32,78,101]  t3 = t1[0] + t2[0]  =====>   t3 = 2 + 78  ===>   t3 = 80

def SaisirTableau_1_Et_2_SommeEnTableau_3(max):
    print("TABLEAU 1 :" )
    tab1 = []
    for add_élement in range(0, max):
        num = int(input("Entrer tab1["+str(add_élement)+"] :"))
        tab1.append(num)
    
    print(tab1)
    
    print(" ")
    print("!---------------------------!")
    print(" ")
    
    print("TABLEAU 2 :" )
    tab2 = []
    for add_élement in range(0, max):
        num = int(input("Entrer tab2["+str(add_élement)+"] :"))
        tab2.append(num)
    
    print(tab2)
    
    print(" ")
    print("!---------------------------!")
    print(" ")
    
    tab3=[]
    for index_table in range(0, max) :
        tab3.append(  tab1[index_table] + tab2[index_table]  )
    print("LA SOMME EST TABLEAU 3:" )
    print(tab3)



max = int(input("Entrer le nombre des Case de chaque Tableau :"))
print("!---------------------------!")
print("SAISIT DES TABLEAUS :")
SaisirTableau_1_Et_2_SommeEnTableau_3(max)