# Multilevel Inheritance

class Alto():
    star = 4
    def Brake(self):
        print("This is Brake Method.")

    def Wheels(self):
        self.wheelss = 4   # Instance Variable
        print("This is wheels Method")

# class Innova : public Alto  in CPP

class Innova(Alto):
    def Airbag(self):
        print("There are 6 Airbags in this")
        # print(Alto.wheelss)
        print(Alto.star)
        i1 = Innova()
        i1.Wheels()
        print(i1.wheelss)

class Ferrari(Innova):
    def Safety_f(self):
        print("Safety Features")

# uday = Innova()   # uday is Object of Innova class

# uday.Airbag()
# uday.Wheels()

manoj = Ferrari()
manoj.Safety_f()
manoj.Brake()

# Safety Features
# This is Brake Method.

# --------------------------------------

# Heirarchical Inheritance
class RBI:
    def PrintNotes(self):
        print("Lot of Notes")

class Kotak(RBI):
    pass

class ICICI(RBI):
    def InterestRate(self):
        print("5% Interest")

class HDFC(RBI):
    pass


akshat = HDFC()
akshat.PrintNotes()
# akshat.InterestRate()  # Gives Error



# ------------------------------------


# Multiple Inheritance


class Father:
    def __init__(self):
        self.car = 2
    
    def CAR(self):
        print("Father has",self.car,"Cars")


class Mother:
    def __init__(self):
        # super().__init__()
        self.gold = 3

    def GOLD(self):
        print("Mother Has much Gold.",self.gold)


class Parth(Father, Mother):   # Method Resolution Order
    def __init__(self):
        # super().__init__()
        Mother.__init__(self)
        Father.__init__(self)
        print("Parth Class Constructor")
        self.mobile = "Samsung"

    def Mobile(self):
        print("Parth has Samsung Mobile.",self.mobile)


p1 = Parth()
# p1.Mobile()
p1.GOLD()
p1.CAR()