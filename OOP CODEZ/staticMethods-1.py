class Math :

    @staticmethod
    def add(a , b) :
        c = a + b
        return c

    @staticmethod
    def add5(a) :
        b = a + 5
        return b

    @staticmethod
    def add10(a) :
        b = a + 10
        return b

    @staticmethod
    def PI() :
        return 3.14

# x = Math.add(5 , 10)
# y = Math.add5(x)
# z = Math.add10(y)

# print(x ,y , z)


class Pizza :
    def __init__(self , raidus ,  ingredient) :
        self.raidus = raidus
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

    def pizaa_area(self) :
        return Pizza.circle_area(self.raidus)

    @staticmethod
    def circle_area(r) :
        result = r ** 2 * Math.PI()
        return result

p = Pizza(6 , ['tomato' , 'onion'])
print(p.pizaa_area())
print(Pizza.circle_area(4))   # Pour prendre des resultas afin de l'utiliser (il sont des general methods) ==> @staticmethod



