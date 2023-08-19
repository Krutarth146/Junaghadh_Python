# Operator Overloading ----> Polymorphism  (Magic Methods / Dunder Methods)

class Student:
    def __init__(self, name1, roll1,marks1):
        self.name = name1
        self.roll = roll1
        self.marks = marks1
        print(self.name, self.roll)

    def Girnar(sf, rupees):
        sf.rupees = rupees
        print("Happy Journey",sf.name, '---->', sf.rupees)

    def sum(sf,other):
        print(sf.marks + other.marks)

    def __gt__(sl, other):
        return sl.marks > other.marks
    
    def __le__(sl, other):
        return sl.marks <= other.marks


Uday = Student("Uday Rathod", 900,34)
Ajay = Student("Ajay Katara", 800,7)


Uday.Girnar(5000)
Uday.sum(Ajay)   # 101
# print(Uday + Ajay)   # 101
print(Uday > Ajay)   # 101
print(Uday <= Ajay)   # 101


# x = 89   # int
# y = 78.90  # Float

# print(x+y)
 
