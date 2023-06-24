list1 = []

# List Characteristics : Ordered (Indexed), Mutable (Changeble), Allow's Duplicates

print(type(list1))   # <class 'list'>

l1 = [10,10,20.90,True,"False", 67+9j, [10,20,30], [[10,90],[89,43],[32,11]]]
print(l1)  # [10, 10, 20.9, True, 'False', (67+9j), [10, 20, 30], [[10, 90], [89, 43], [32, 11]]]

print(l1.__sizeof__())  # 104
print(len(l1))  # 8   # Length starts from 1, Index starts from 0
print(id(l1))  # 1530120617088

l1 = [10,10,20.90,True,"False", 67+9j, [10,20,30], [[10,90],[89,43],[32,11]]]





# Indexing
print(l1[5])   # (67+9j)
print(l1[-3])  # (67+9j)
print(l1[-1])  # [[10,90],[89,43],[32,11]]
print(l1[-1])  # [[10,90],[89,43],[32,11]]
print(l1[-1][2])  # [32, 11]
print(l1[-1][-1])  # [32, 11]
print(l1[-1][2][1])  # 11
print(l1[-1][2][-1])  # 11


tup1 = (10, 90, [([100,90], [23,68]), ([43,67], (2,2,2,5,3))])

print(tup1[2])  # [([100, 90], [23, 68]), ([43, 67], (2, 2, 2, 5, 3))]
print(tup1[2][1])  # ([43,67], (2,2,2,5,3))
print(tup1[2][1][0])  # [43,67]
print(tup1[2][1][0][-1])  # 67
print(type(tup1[2][1][0][-1]))  # <class 'int'>


# Slicing

l2 = [10,20,30,40,50,60,90,89,78,22,11,44,90]

# print(l2[start : end(n-1) : step(n-1)])

print(l2[0:6])  # [10, 20, 30, 40, 50, 60]
print(l2[3:4])  # [40]
print(type(l2[3:4]))  # <class 'list'>
print(l2[8:2])  # []
print(l2[-1 : -6])  # []
print(l2[-1 : 6])  # []
print(l2[-6 : 6])  # []
print(l2[4::1])  # [50, 60, 90, 89, 78, 22, 11, 44, 90]
print(l2[4::2])  # [50, 90, 78, 11, 90]
print(l2[4:10:-1])  # []
print(l2[10:4:-3])  # [11, 89]
print(l2[9::-3])  # [22, 90, 40, 10]
print(l2[9:0:-3])  # [22, 90, 40]
print(l2[-4:5:2])  # []


# List Methods

l1 = [10,20,30,40,50]

l2 = [90,89,78]

l1+=l2
print(l1)  # [10, 20, 30, 40, 50, 90, 89, 78]

# l1.append(900)
# l1.append("str1")

# print(l1)   # [10, 20, 30, 40, 50, 90, 89, 78, 900, 'str1']

# l1.extend('400')
# print(l1)  # [10, 20, 30, 40, 50, 90, 89, 78, 900, 'str1', '4', '0', '0']


l1 = [10,20,30,40,50]
l2 = [90,89]

l1.append(l2)
print(l1)   # [10, 20, 30, 40, 50, [90, 89]]

# l1.extend(l2)
# print(l1)   # [10, 20, 30, 40, 50, 90, 89]

l1.insert(2,5000)

print(l1)  # [10, 20, 5000, 30, 40, 50, [90, 89]]

l1[2] = 900
print(l1)  # [10, 20, 900, 30, 40, 50, [90, 89]]

l1.insert(100,900)
print(l1)

# l1[100] = 900  # Error

l1.remove(900)
print(l1)  # [10, 20, 30, 40, 50, [90, 89], 900]


for i in l1:
    if i == 900:
        l1.remove(i)

print(l1)  # [10, 20, 30, 40, 50, [90, 89]]


l1.pop()
l1.pop()
print(l1)  # [10, 20, 30, 40]

print(l1.pop(1))  # 20
print(l1)   # [10, 30, 40]


l6 = [10, 20, 30, 40, 50, [90, 89]]

# del l6
del l6[5:]
print(l6)   # [10, 20, 30, 40, 50]

print(l6.index(50))  # 4
# print(l6.index(500))  # Error
print(l6.count(50))  # 1


l7 = [90,32,89,12,89.89,34,56]
l7.sort()
print(l7)  # [12, 32, 34, 56, 89, 89.89, 90]

# l7.reverse()
# print(l7)   # [90, 89.89, 89, 56, 34, 32, 12]

l7.sort(reverse=True)
print(l7)   # [90, 89.89, 89, 56, 34, 32, 12]

xerox = l7.copy()

digilocker = l7

l7.append(7000)

print(l7)     # [90, 89.89, 89, 56, 34, 32, 12, 7000]
print(xerox)   # [90, 89.89, 89, 56, 34, 32, 12]
print(digilocker)  # [90, 89.89, 89, 56, 34, 32, 12, 7000]


digilocker.append('str1')

print(l7)   # [90, 89.89, 89, 56, 34, 32, 12, 7000, 'str1']

l1 = [10,20,30,40,50,90, 77,43]

for i in l1:
    print(i,end=' ')  # 10 20 30 40 50 90

print()
print()

# for j in range(len(l1)):
#     if l1[j] % 2 != 0:
#         print(l1[j])  # 77 , 43


# l4 = []
# for i in range(25,36):
#     l4.append(i)

# print(l4)
    

# num1 = int(input())
# num2 = int(input())
# b1 = []

# for j in range(num1, num2+1):
#     b1.append(j)
# print(b1)



# ----------------------

# 10 90 89 78 67

# ele = int(input())
# b2 = []


# i = 1
# while i<=ele:
#     num = int(input())
#     b2.append(num)
#     i+=1

# print(b2)




# 10 90 89
# [10,90,89]


# 90 89 78 67 56
# [90,89,78,67,56]

l3 = [int(i) for i in input().split()]   # List Comprehension
print(l3)


l3 = [10,90,89,78,67]

[(10,10), (10,90), (10,89) ....]