

class Bag:
    pen = "Fiat"
    notebook = "500"
    mouse = "white"

school = Bag()

# print(school.pen)


# class Person:
#     def __init__(self, a, b):
#         self.nemo = a
#         self.demo = b
        

# aytac = Person("John", 21)
# print("My name is",aytac.nemo,". I am",aytac.demo,"years old.")



class Person:
    def __init__(self, a, b, c):
        self.nemo = a
        self.sport = b
        self.car = c

    def __str__(self):
        return f"{self.nemo} {self.sport} {self.car}"

student = Person("Murad", "14", "BMW")
# print(student)





class Student:
    def __init__(self, a):
        self.teacher = a

    def __str__(self):
        return f"{self.teacher}"
    
    def myfunc(self):
        return "Hello my name is " + self.teacher

    def myFuncWithPrint(self):
        print("Hello my name is " + self.teacher) 

country = Student("Aytac")
print(country)

print(country.myfunc())   # return ile gelen
country.myFuncWithPrint() # print ile gelen







