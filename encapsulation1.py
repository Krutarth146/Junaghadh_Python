# Encapsulation

class Royal:
    no_of_students = 800   # Public class Variable
    _wifipw = 87654321   # Protected Class Variable
    __bank_ac = 40000000000000000000   # Private Class Variable

    def __init__(self, name1, fee1):  # Parametrized Constructor
        self.name = name1    # name is Instance Varibale
        self.fee = fee1

    @staticmethod
    def printwifipw():   # Static Method
        print("Strong Pw")

    def printFees(self):   # Instance Method
        print("This is Printfees Method")
        # choice = int(input("Are u want to Change Name?"))
        choice = 0
        if choice:
            self.name = input("Enter New Name: ")
            print("S Changed")

    @classmethod
    def changePass(cls):   # Class Method
        cls._wifipw = "Aman123"
        print("Wifi Password Changed.")

    @classmethod
    def deposit(clssssss, amount):
        clssssss.__bank_ac += amount
        print("Your Updated Balance is",clssssss.__bank_ac)

uday = Royal('Uday', 25000)
akshay = Royal('Akshay', 30000)

print(Royal._wifipw)   # 87654321
print(uday.name)    # Uday

Royal.changePass()
print(Royal._wifipw)   # Aman123

uday.changePass()
print(Royal._wifipw)   # Aman123
print(uday._wifipw)   # Aman123
print(akshay._wifipw)   # Aman123

uday.printFees()

print(uday.name)
print(akshay.name)

Royal.printwifipw()

print(Royal._wifipw)

Royal.deposit(6000)

# print(Royal.__bank_ac)  # Generates an Error

print(Royal._Royal__bank_ac)   # 40000000000000006000