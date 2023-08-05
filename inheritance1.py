# Inheritance  ---> Inherit

class RBI():
    _repo_rate = 7.0

    __total_ac = 900000000000000000000


    def __init__(self, colorName):
        self.color = colorName
    
    @classmethod
    def repoRate(cls):
        print("Repo rate is",cls._repo_rate)

    def Guideline(self):
        print("THis is Guideline Method")

    def printBColor(self):
        print(self.color)

# class ICICI : public RBI   in CPP

class ICICI(RBI):
    def __init__(self, colornameeeeee):
        super().__init__(colornameeeeee)
        print("ICICI B color:",self.color)

    def interest(self):
        self.interest = 4.2
        print("Interest Rate of ICICI is",self.interest)


parth = ICICI("RED")

# parth.interest()
# parth.Guideline()

# print(parth._repo_rate)   # 7.0
# print(parth._RBI__total_ac)   # 900000000000000000000

# parth.printBColor()