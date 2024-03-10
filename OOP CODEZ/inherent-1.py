# class Person :

#     def ___init__(self,name,age) :
#         self.name = name
#         self.age = age

#     def describe(self) :
#         return f"Your name is {self.name} and your age {self.age}"


# class Man(Person) :

#     # gender = "Male"
#     # num_of_men = 0

#     def __init__(self,name,age) :
#         super().__init__(name,age)
#         # self.voice = voice
#         # Man.num_of_men += 1

#     def describeToi(self):
#         print(super().describe())
#         # return string + f" and your voice is {self.voice} and your gender is {self.gender}"


# m = Man("Abdellah",18,"Medium")

# m.describeToi()


from datetime import *

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  @classmethod
  def initInformation(cls,name,birthday,extra=None) :
    return cls(name, date.today().year - birthday, extra)

  def printname(self):
    return (f"Your name is {self.name}, and you have {self.age}")




class Student(Person):

  gender = 'Male' 
  nbr_of_student = 0

  def __init__(self,name,age,mark) :
      super().__init__(name,age)
      self.mark = mark
      Student.nbr_of_student += 1

  def descripe(self):
      string = super().printname()
      return (string + f", you are a {self.gender}, and your mark is {self.mark}/20.")
        
#                      <<   Whith normal method   >>



student_1 = Student("Abdellah", 18, 20)
print(student_1.descripe())

print("--------------------------------------------------------------")

#                      <<    Whith classmethod    >>
student_1 = Student.initInformation('Abdellah' , 2004 , 20)
print(student_1.descripe())


#            Test about object is from a class (True or False)
# class Math :
#   def PI() :
#     return 3.14

# print(isinstance(student_1 , Math) )