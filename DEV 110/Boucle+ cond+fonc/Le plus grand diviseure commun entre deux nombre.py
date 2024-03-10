                                            #<<<< Le plus grand diviseure commun entre deux nombre >>>>

# Les entrée :
num1 = int(input('number 1:'))
num2 = int(input('number 2:'))





# Déclaration du tableu 1 pour le remplireavec les diviseurs de num 1 :
#tableau 1
tab1 = []

# Trouver les divs de num1 en utilisent (Mod) :
for i in range(1 , num1+1) :
    num1d = num1 % i
    if num1d == 0 :        # Si le Mod de num2 sur i égale 0 Alors :
        tab1.append(i)     # Ajouter dans le Tableau






#declaration du tableu 2 pour le remplire les diviseurs de num 2 :        
#tableau 2
tab2 = []                

# Trouver les divs de num2 en utilisent (Mod) :
for i in range(1,num2+1) :
    num2d = num2 % i

    if num2d == 0 :       # Si le Mod de num2 sur i égale 0 Alors :
        tab2.append(i)    # Ajouter dans le Tableau





#Trouver le plus grand div commun : L'étape de comparaison

for i in range(0,len(tab1)):       # Recupérer les valeurs du tab 1 Pour faire une boucle sue eux afin de les comparer avec les valeurs du tab 2 
    for j in range(0,len(tab2)):   # Recupérer les valeurs du tab 2 Pour faire une boucle sue eux afin de les comparer avec les valeurs du tab 1 

        if tab1[i] == tab2[j]:      # Trouver les div communs
            divc = tab1[i]          # Recupérer les div communs

# Enfin La boucle termine il va recupérer seulement le plus grand div commun entre num1 et num 2




# Est voisi le résultat finale

#Ecrire    
print('diviseurs du tableau 1: ',tab1,' diviseurs du tableau 2: ',tab2,'\nPlus grand diviseur commun: ',divc)
