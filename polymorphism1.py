# Polymorphism

# Poly ---> Many
# Morph ----> Forms

# right ---> Letf - right, right - wrong
# len() ---> str, tuple, list, dict, set  # PolyMorphism's Ex
# Royal ---> Institute, Shahi


# set1 = {10,20,10}
# print(len(set1))  # 2
# print(len("Ashok"))  # 5
# print(len([10,20,30]))  # 5


class Royal():
    def __init__(sf):   
        sf.temp = 0
        print("This is Royal class Constructor")

    def Girnar(ml):
        ml.people = 120
        print("Happy Journey",ml.people)


class Infosys(Royal):
    def __init__(ff):
        ff.pleassure = 900

    def Girnar(dl):   # Method Overriding
        # Royal.Girnar(dl)
        dl.people = 200
        print("Shubh Yatra",dl.people)


    def Girnar(d1, pleassure):
        print("Mir6ami Dukkadam!!",pleassure)


    def Dubai(self):
        print("This is DUbai Method Under Infosys class")

    def Dubai(self, money):    # Method Overloading  ---> Parameter Different
        self.budjet = money
        print("Dubai with Money",self.budjet)


akshay = Infosys()
# akshay.Girnar(55000)
akshay.Girnar(500)

# res = [Royal(), Infosys()]
# print(res)

# for i in res:
#     i.Girnar()

akshay.Dubai(500000)


def jk():
    print("JK")

def jk(n1, n2):
    print(n1+n2)

jk(10,20)   # 30