# Prime

num = 24
# Divisors ---> 1,23


# for i in range(2,num):   # 2 to 23
#     if num % i == 0:
#         break

num = 23
k = 2
flag = 0

while k<(num//2):
    if num % k == 0: # 23 % 22 == 0
        flag = 1
        break
    k+=1

if flag == 0:
    print("Prime")

# Twin Number  22 , 321, 123, 231 (sum == mul)

# Fibonnacci using function

# 0, 1, 1, 2, 3, 5 .....

# def fibonacci(step):
#     n1,n2 = 0,1

#     # print(n1,n2,sep=' ',end=' ')
#     list1 = []
#     list1.append(n1)
#     list1.append(n2)

#     for i in range(step-2):
#         n3 = n1 + n2
#         list1.append(n3)
#         n1 = n2
#         n2 = n3
#     return list1

# print(fibonacci(int(input())))


# ------------------

def fibo(step):

    list1 = [0,1]

    for i in range(step-2):
        list1.append(list1[-1] + list1[-2])

    for k in list1:
        yield k   # Generator

import time
old_time = time.time()

for h in fibo(5):
    print(h)

print(time.time() - old_time)

# lambda, Recursion, Map, reduce, filter Remaining -------------------------

# ------------------------------------------

# Tuple

tup1 = (10,20,90.89,{10,10}, ({"Name" : 'Krutarth', 'roll' : [(10,20,30)]}))

print(tup1)   # (10, 20, 90.89, {10}, {'Name': 'Krutarth', 'roll': [(10, 20, 30)]})

tup2 = (10)
print(type(tup2))  # <class 'int'>
tup2 = (10,)
print(type(tup2))  # <class 'tuple'>

# Tuple Characteristics: Ordered (Indexed), Allow's Duplicates, Immutable (Not changeble)


print(tup1[-1]['roll'][-1][2])  # 30   # Indexing
print(tup1[-1:-4:-1])   # ({'Name': 'Krutarth', 'roll': [(10, 20, 30)]}, {10}, 90.89)

for k in range(-10,-5,2):
    print(k)
# -----------------------------------

tup1 = (10,20,30,40,50,60,70,80,90,20)
for k in range(3,-3,-1):
    print(k)  # 3,2,1,0,-1,-2

print(tup1[3:-3:-1])  # ()
print(tup1[2:3:-1])   # ()


print(tup1.index(20,2))   # 9
print(tup1.count(20))   # 2
print(tup1.count(1000))   # 0


for k in reversed(tup1):
    print(k)


for j in tup1[::-1]:
    print(j)

for k in enumerate(tup1,100):
    print(k,end=' ')   # (100, 10) (101, 20) (102, 30) (103, 40) (104, 50) (105, 60) (106, 70) (107, 80) (108, 90) (109, 20)

for position,ele in enumerate(tup1,1):
    if position % 2 != 0:
        print(ele)


tup2 = (10,20,390,78,54)
tup3 = (101,201,3901,781,541)

for l in zip(tup2,[i for i in range(len(tup3))]):
    print(l)

for g,h in zip(tup2,tup3):
    print(g,h)


tup3 = (10,20,10,10,10,20,90,80)

print(set(tup3))   # {80, 10, 20, 90}   # Don't Allow Duplicates, Unordered

# ----

l1 = []

for i in tup3:
    if i not in l1:
        l1.append(i)

print(l1)

# -------------

tup3 = list(tup3)

for i in tup3:
    if tup3.count(i) == 1:
        print(i)

# ----------------------

list1 = [10,20,30,10,20,10,30,10]

dict1 = {}

for k in set(list1):
    dict1[k] = list1.count(k)

print(dict1)


str1 = "Mississippi"
l2 = []

for k in str1:
    l2.append(k)

print(l2)  # ['M', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']

dict1 = {}

# for k in set(l2):
#     dict1[k] = l2.count(k)

# print(dict1)

#  ['M', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']

for m in l2:
    if m not in dict1:
        dict1[m] = 1
    else:
        dict1[m] += 1

print(dict1)


# Comprehension

l4 = [i for i in range(5)]
print(l4)  # [0, 1, 2, 3, 4]

list1 = [10, 81, 21, 34, 67]

# for j in list1:
#     if j % 2 == 1:
#         print(j)

l5 = [j for j in list1 if j % 2 == 1]
print(l5)   # [81, 21, 67]



p1 = [10,20,30,40,50,60,70]

# [(10,10), (10,20), (10,30) ...]

for k in p1:   # 10
    for l in p1:  # l = 20
        print((k,l))  # 10 20

l1 = [(k,l) for k in p1 for l in p1]
print(l1)