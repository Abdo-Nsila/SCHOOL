class Date :

    def __init__(self , date) :
        self.__date = date

    def get_date(self) :
        return self.__date

    def set_date(self) :
        return Date.change_form(self.__date)

    @staticmethod
    def change_form(date) :
        return date.replace("/" , "-")


d = Date("30/05/2004")
a = d.set_date()
print(d.set_date())    #  ==  print(a)


myDate = "30/05/2004"
b = Date.change_form(myDate)
print(Date.change_form(myDate))   # ==  print(b)


if a == b :
    print("equal")
else :
    print("inequal")