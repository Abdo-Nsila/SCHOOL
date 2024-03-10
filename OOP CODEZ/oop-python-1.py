from datetime import *

class Student :
    num_of_Students = 0
    def __init__(self , name , age , courses = ['None']) :
        self.__name = name
        self.__age = age
        self.__courses = courses
        Student.num_of_Students += 1

    def descripe(self) :
        print(f"My name is {self.__name} and my age is {self.__age}")
        # print("My name is {} and my age is {}".format(self.__name , self.__age))

    def is_old(self , num) :
        if self.__age <= num :
            print(f"{self.__name} is not old")
        else :
            print(f"{self.__name} is old")
    @property
    def get_name(self) :
        print(self.__name)
    
    def set_name(self , new_name) :
        self.__name = new_name

    def get_age(self) :
        print(self.__age)

    def set_age(self , new_age) :
        self.__age = new_age


    @classmethod
    def init_name_and_birthYear(cls ,name ,birthYear) :
        return cls(name ,date.today().year - birthYear)


#           self.name      ==>    Public Attribute
#           self.__name    ==>    Private Attribute






student_1 = Student('Abdellah' , 18 , ['algo' , 'oop'])
student_2 = Student('Omar' , 60 , ['web' , 'php'])



# print(id(student_1)) ==> id
# student_1.name = 'Nsila'   ==>    !! Not recommended !!
# --------------------------------------------------------
# print(student_1.name ,student_1.age ,student_1.courses )
# print(student_2.name ,student_2.age ,student_2.courses )
# --------------------------------------------------------
# print(Student.num_of_Students)
# --------------------------------------------------------
student_2 = Student.init_name_and_birthYear("Bachar" , 2000)
student_2.descripe()
# student_2.descripe()
# --------------------------------------------------------
# student_1.is_old(50)
# student_2.is_old(50)
# --------------------------------------------------------
# student_1.descripe()
# student_1.get_name()
# student_1.set_name("Nsila")
# student_1.get_name()
# student_1.get_age()
# student_1.set_age(20)
# student_1.get_age()
# student_1.descripe()
# print("---------------------------------------------------")
# student_2.descripe()
# student_2.get_name()
# student_2.set_name("Ali")
# student_2.get_name()
# student_2.get_age()
# student_2.set_age(40)
# student_2.get_age()
# student_2.descripe()
