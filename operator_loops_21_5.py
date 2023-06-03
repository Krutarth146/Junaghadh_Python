days = 2340

year = days // 365
months = (days % 365) // 30
rem_days = (days % 365) % 30


print(f"Total Years: {year}, months: {months}, Remaining Days are {rem_days}")



# # Leap Year  ---> 4 

# for year in range(1800,3301):

#     if year % 400 == 0:
#         print(year,end=' ')
#     elif year % 4 == 0 and year % 100 != 0:
#         print(year,end=' ')


# Identity O/p

x = 90
y = 90

if x == y:
    print("Same")

if x is y:
    print("Same")

list1 = [10,20,30]
list2 = [10,20,30]

if list1 == list2:
    print("Same List")
print(id(list1))  # 2448633113152
print(id(list2))  # 2448633046656
if list1 is list2:
    print("list1 is list2")

list3 = list1

print(id(list1))  # 2189471656512
print(id(list3))  # 2189471656512


if list1 is list3:
    print("list1 is list3")


# Loops --> 1. Entry Control loops   ---> 1. while   2. for


# Intialization (start)
# Condition (Stop)
# Flow (Incre / Decre)

harsh = 79
while harsh >= 20:
    if harsh % 2 != 0:
        print("odd Number: ",harsh,end=' ')
    harsh-=1  # harsh = harsh - 2   

akshay = 90

while(3):
    if akshay == 98:
        break
    print(akshay,end=' ')
    akshay+=2
else:
    print("while Loop not Broken by any condition")
# 90 92 94 96

num = 1
i = 1
while num<=3:    # num = 3
    while i<=3:   # i = 3
        if num == i:  # 3 == 3
            break
        print(num)
        i+=1
    num+=1



# Nested If else


num1 = 9000
num2 = 670
num3 = 7800

# if num1 > num2:
#     print(num1)
# else:
#     print(num2)

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)

x = (num1 if num1 > num3 else num3) if num1 > num2 else (num2 if num2 > num3 else num3)
print(x)


# Ex. 

# num = 3
# step = 5


# 3 + 33 + 333 + 3333 + 33333 = (?)