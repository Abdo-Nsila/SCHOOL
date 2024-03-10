class Pizza :
    def __init__(self , ingredient) :
        self.ingredient = ingredient

    @classmethod
    def normal_Pizza(cls) :
        return cls(['tomato' , 'onion' , 'frommage'])

    @classmethod
    def margarita_Pizza(cls) :
        return cls(['tomato' , 'onion' , 'motzarilla'])

    @classmethod
    def small_Pizza(cls) :
        return cls(['tomato' , 'onion'])

    def __str__(self) :
        return f"The Pizaa ingredients is : {self.ingredient}"

    
        


pizza1 = Pizza(['tomato' , 'olives'])
# Donner les valeurs aux attributs comme un constructeur , personaliser les valeurs comme tu veux  ==>  @classmethod
# ||il prend le classe(cls) comme paramétre||
pizza2 = Pizza.normal_Pizza()
pizza3 = Pizza.margarita_Pizza()
pizza4 = Pizza.small_Pizza()

print(pizza2 , "\n", pizza3 , "\n", pizza4)


