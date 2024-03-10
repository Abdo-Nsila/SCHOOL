from abc import ABC, abstractmethod


class Parent(ABC) :

    @abstractmethod
    def area(self) :
        pass

    @abstractmethod
    def perimetre(self) :
        pass

    @abstractmethod
    def display(self) :
        pass



class Square(Parent) :

    def __init__(self,lenght) :
        self.__lenght = lenght

    def area(self) :
        areaOfSquare =  self.__lenght * self.__lenght
        return areaOfSquare

    def perimetre(self) :
        primetreOfSquare = self.__lenght * 4
        return primetreOfSquare

    def display(self) :
        return f"Area of square : {Square.area()}, and Perimetr of square : {Square.perimetre()} "


class Rectangle(Parent) :
    def __init__(self,lenght,width):
        self.__lenght = lenght
        self.__width = width

    def area(self) :
        areaOfRect = (self.__lenght + self.__width) * 2
        return areaOfRect

    def perimetre(self):
        perimetreOfRect = self.__lenght * self.__width
        return perimetreOfRect

    def display(self) :
        return f"Area of Rectangle : {Rectangle.area()}, and Perimetr of Rectangle : {Rectangle.perimetre()} "

    

# Object of Square :
sq = Square(8)
print(sq.display())

# Object of Rectangle :
rect = Rectangle(5, 20)
print(rect.display())
