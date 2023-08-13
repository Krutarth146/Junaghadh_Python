# Abstraction  ---> To Hide Bussiness Logic

from abc import ABC, abstractmethod

class Person(ABC):

    def m1(self):
        print("M1 Method Under Person class")

    @abstractmethod
    def amethod():
        pass

    def manoj(self):
        print("Peon of Royal")

class student(Person):
    def amethod(self):   # Method Overwrite
        self.role = 'Student'
        print("This is amethod Under Student Class",self.role)

class Teacher(Person):
    def amethod(self):   # Method Overwrite
        self.role = 'Teacher'
        print(f"This is amethod Under {self.role} Class")


# p1 = Person()   # Gives an Error

s1 = student()
t1 = Teacher()

s1.amethod()
t1.amethod()
t1.manoj()