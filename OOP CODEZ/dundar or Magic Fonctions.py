# class Man :

#     def __init__(self,name,age) :
#         self.__name = name
#         self.__age = age

#     def display() :
#         pass

#     def __add__(self,other) :
#         names = self.__name + " and " + other.__name
#         ages = self.__age + other.__age
#         return f"Names combined are {names}, and sum of ages is {ages}"

#     def __lt__(self,other) :
#         return self.__age < other.__age

    

# man1 = Man('Abdellah' , 18)
# man2 = Man('Mehdi' , 60)

#         __add__
# # print(man1 + man2)
#         __lt__
# print(man1 < man2)



#       <<   Mini example for magic functions  >>
# a = ['Abdellah' , 'Nsila' , 'Python']
# print(a.__len__())
# print(a.__getitem__())




class Order :

    def __init__(self,cart,custmore) :
        self.__cart = cart
        self.__custmore = custmore 

    def get_custmore(self) :
        return self.__custmore

    def get_cart(self) :
        return self.__cart

    def __len__(self) -> int :
        return len(self.__cart)

    def __call__(self) :
        print(self.__custmore)

    def __str__(self) -> str :
        return f"{self.__custmore} bought {self.__cart}"

    def __repr__(self) -> str:
        return f"Order(List of items ,  Cusumor name)"

    def __bool__(self) :
        return len(self.__cart) > 0

    def __iadd__(self,other) :
        self.__cart.append(other)
        return self
    def __radd__(self,other) :
        self.__cart.insert(0,other)
        return self

    def __isub__(self,other) :
        self.__cart.remove(other)
        return self

    def __imul__(self,other) :
        self.__cart *= other
        return self

    def __getitem__(self,key) :
        return self.__cart[key]

    def __setitem__(self,key,value) :
        self.__cart[key] = value
        return self 
    

    
order = Order(['Mother_Board intel B660' , 'intel core i5 12400' , 'RTX 3060 Ti' , '32 GB DDR4' , '2 TO SSD_NVME ' , 'PSU 800w' ,\
 'Case and Cooler' , 'Moniteur 2K 240hz 1ms' , 'Mouse_Keyboard ==> Logitec RGB'] , 'Abdellah Nsila')
# order = Order([],'Nsila')

# __len__
# print(len(order))

# __call__
# order()+
# __str__
# print(order)

# __repr__
# print(repr(order))

# __bool__
# print(bool(order))
# if order :
#     print(f"{order.get_custmore()} order is processing ...")
# else :
#     print("Shopping cart is empty ):")

# __________________Operators_________________
# __iadd__
# order += 'casque'
# __radd__
# order = 'microphone' + order

# __isub__
# order -= 'Mouse_Keyboard ==> Logitec RGB'

# __imul__
# order *= 2

# Result after operator :
# print(order.get_cart())

# __getitem__
print(order[2])

# __setitem__
order[2] = 'RTX 4080'
print(order.get_cart())
