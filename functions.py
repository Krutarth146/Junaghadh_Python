
# Functions ---> 
# 1. Pre Defined  ----> len(), max(), sum(), min(), print(), input()  
# 2. User Defined  ----> Uday(), Royal()

# 
#  Functions. Syntax

# 1. Func. Defination
# 2. Func. Calling

# void Uday();   # Func. Declaration

# void Uday()
# {
#     print(32+56)   # Func. Defination
# }

# void main()
# {
#     sortedvs
#     vsv
#     sdv
#     Uday();   # Func. Calling
#     vsdv
# }


# 1. Func. Defination

def Royal():   # FUnc. Defination
    print("ROyal is Best Institute Ever.")
    print("ROyal is Best Institute Ever1.")
    print("ROyal is Best Institute Ever2.")
    print("ROyal is Best Institute Ever3.")

Royal()   # Func. Calling
Royal()   # Func. Calling
Royal()   # Func. Calling
Royal()   # Func. Calling


# Func. Types

# 1. Without Return Type and Without Arguments
# 2. Without Return Type and With Arguments
# 3. With Return Type and Without Arguments
# 4. With Return Type and With Arguments    
# main()
# {

# }

# 1. Without Return Type and Without Arguments

def Parth():
    print("This is Parth Function")
    x,y,z = 90,80,67

    print(x+y+z) 

Parth()   # 237


# 2. Without Return Type and With Arguments

def subtraction(num1, num2, num3):
    print(num1 - num2 + int(num3))   # 79
    print(num1, num2, num3)  # 90 67 56
    pass

subtraction(90,67,"56")



# Ex.2

def Uday(list1):
    list1.insert(2,9000)

    list1.append(400000)

    print(list1)   # [10, 290, 9000, 80, 84, 3, 3, 27]


p1 = [10,290,80,84,3,3,27]
Uday(p1)
print(p1)   # [10, 290, 9000, 80, 84, 3, 3, 27, 400000]

# p1.append(1000)
# print(p1)
# Uday(p1)



# 3. With Return Type and Without Arguments

def Amit():
    x,y = 900,700
    list1 = [10,20,30]
    k = 80
    return x+y+800, list1


print(Amit())  # (2400, [10, 20, 30])

x = Amit()
print(x)

# print(k)


f = 90  # GLobal Variable

def Akshay():  
    global f 
    f+=10   # Local Variable
    print("Internal",f)   # 100



Akshay()

f+=30
print("External", f)  # 130


# 4. With Return Type and With Arguments 


def Khushi(n1, n2=0, n4=50):
    return n1+n2+n4


print(Khushi(900))   # 950


# ---------------------------------------------------


def Manoj(num20,*royal,num89=78):
    print(royal)   # (10, 20, 30, 'str1', [10, 20], (10, 20), {10}, {'Name': 'Kru'})

    print(sum(royal))   # 151.89

    for i in royal:
        print(i,end=' ')

    print(type(royal))  # <class 'tuple'>
    print("num20 = ",num20)   # num20 =  10

# Manoj(10,20,30,"str1",[10,20],(10,20),{10,10},{"Name" : "Kru"})
Manoj(10,20,30,90.89,True)


# --------------------------------------------------------


# kwargs -----> Dict

def Harsh(*badsha, **kwargs):
    print(kwargs)   # {'name': 'Uday', 'Roll': [10, 20, 30], 'Address': {'City': 'Ahm'}}

    for key,val in kwargs.items():
        print(val)

    print(kwargs["Address"]['City'])   # Ahm

    print(badsha)


Harsh(10,20,30,name = "Uday", Roll = [10,20,30], Address = {'City' : "Ahm"}) 