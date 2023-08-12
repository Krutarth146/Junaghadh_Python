# Decorators

# Decorator is first class Object


# we can pass function as an Argument
def fun(f1):
    print("Fun1 Function")
    f1()

def ashok():
    print("This is Ashok Function")

f = ashok

fun(f)
fun(ashok)


def fun1(f4):

    def fun3():
        print("FUnction 3 Under FUn1")
        f4()

    return fun3()

# def Uday():
#     print("Uday Function")


# fun1(Uday)

print("=-----------------------=")
@fun1
def Uday():
    print("Uday Function")


@classmethod  # Decorator
def Parth(cls):
    print("Parth")

# @teacher_required
# def edit_marks():
#     print(True)