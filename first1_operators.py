# Python is Dynamic Lang.

# int x = 90
x = 80
print(type(x))  # <class 'int'>

y = 90.89
print(type(y))  # <class 'float'>

_ = 'R'
print(type(_))  # <class 'str'>

d1 = True
print(type(d1))   # <class 'bool'>

k = 90 + 8j   # Complex
print(type(k))    # <class 'complex'>  # 90 is Real Part, 8j is Imaginary Part

s = 8  # int
print(k+s)  # (98+8j)

x = 90 # int
r = 89.78  # float

print(x+r)  # 179.78   # Implicit Typecasting

x = None
print(type(x))  # <class 'NoneType'>

# Typecasting  One datatype to Another Datatype  ---> 1, Implicit T.c  2. Explicit TYpeC

num1 = 90
num2 = 80

print(num1,"+",num2,"=",num1+num2)
print(f"{num1} + {num2} = {num1 + num2}")   # Fstring adv. Formatted String

str1 = "989"
str2 = "90"
print(str1 + str2)  # 98990

str1 = int(str1)
str2 = int(str2)   # Explicit Typecasting
print(str1 + str2)   # 1079


s = True   # 1
w = 23

print(s+w)  # 24   # Implicit

f = '90.78'
print(int(float(f)))  # 90   # Explicit TYpeconversion

print(round(90.78))

import math
print(math.floor(90.99))   # 90
print(math.ceil(90.0001))   # 91

print(18 // -4)  # -5

print("Hello",end=" ROyal ")
print("Vivek")  # Hello ROyal Vivek

d = 90
w = 80
e = 78

print(d,w,e,sep='\n')   # 90 80 78

list1 = [10,90,10,89.89,True,78+9,None,"string",[10,20,30,[10,20,30]], (21,13,4)]
print(list1)  # [10, 90, 10, 89.89, True, 87, None, 'string', [10, 20, 30, [10, 20, 30]], (21, 13, 4)]
print(type(list1))  # <class 'list'>  # Mutable (Changeble)
print(len(list1))  # 10 # Length starts from 1, Index starts from 0

tup1 = (10,20,30,90.89,True,(10,20,30,))
print(tup1)
print(type(tup1))  # Imutable (Not Changeble)
tup1 = list(tup1)
tup1.append(5000)
print(tuple(tup1))

dict1 = {12}
print(type(dict1))  # <class 'set'>

dict2 = {"Name" : "Krutarth", "Roll" : 900}
print(type(dict2))  # <class 'dict'>