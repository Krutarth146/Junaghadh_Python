# l2 = [(10,20), (333,45), (21, 90), (2,67), (3,), (24,90)]

# # (10,20), (21, 90), (24,90)

# res = []


# for tup in l2:  # tup = (333,45)
#     flag = 0
#     for ele in tup:   # ele = 333, ele = 45
#         if len(str(ele)) != 2:
#             flag = 1
#             break
#     if flag == 0:
#         res.append(tup)

# print(res)   # [(10, 20), (21, 90), (24, 90)]

# res1 = [ele for tup in l2 for ele in tup if len(str(ele)) == 2]
# print(res1)

# Lambda  (Anounoumous Function)

def square(num):
    return num ** 2

print(square(5))   # 25



x = lambda num : num ** 2
# print(x)  # <function <lambda> at 0x00000235B5842200>
print(x(6))


y = lambda x,y = 78 : x*y

print(y(10,67))   # 670
print(y(10))   # 780



# Quadratic Function     # (a * x ** 2) + (b * x) + (c)

def quadratic(a1,b1,c1):
    return lambda x, uday = 30 : (a1 * x ** 2) + (b1 * x) + (c1) + uday

print(quadratic(3,4,2)(5))

# aman = quadratic(3,4,2)
# print(aman(5))  # (3 * 25) + (20) + 2  ---> 75 + 20 + 2  # 97


list1 = [10,320,40,590,88]

def square(list1):
    sq1 = []
    for i in list1:
        sq1.append(i*i)
    return sq1

print(square(list1))   # [100, 102400, 1600, 348100, 7744]

square_l = lambda x : x*x
print(square_l(5))   # 25

p1 = list(map(lambda x : x**3, list1))
# print(p1)   # <map object at 0x000002716D99B640>
print(p1)   # [1000, 32768000, 64000, 205379000, 681472]

list1 = [10,320,40,590,88]

p2 = list(filter(lambda x : x > 100, list1))
print(p2)   # [320, 590]

p2 = list(map(lambda x : x > 100, list1))
print(p2)   # [False, True, False, True, False]


from functools import reduce

list1 = [10,320,40,590,88]


p3 = reduce(lambda x,y : x+y, list1)
print(p3)   # 1048

from itertools import accumulate

p4 = list(accumulate(list1, lambda x,y : x+y))
print(p4)   # [10, 330, 370, 960, 1048]