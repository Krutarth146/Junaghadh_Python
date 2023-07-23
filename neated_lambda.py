parth = lambda x = 5 : lambda p, y : x+y+p
# ans = parth(30)

# print(ans(15,55))   # 70

# print(parth(45,32))  # 87

ans = parth()
print(ans(30,40))  # 75

royal = lambda n1,n2 : lambda f : n1 ** f + n2

print(royal(10,20)(5))  # 100020


list3 = [10,20,44,22,11,33,45,2]

from functools import reduce

print(reduce( lambda x, y : x if x > y else y , list3))  # 44


from itertools import accumulate
list4 = list(accumulate(list3, lambda x, y : x if x < y else y))
print(list4)  # [10, 20, 44, 44, 44, 44, 45, 45]


# Recursion

# When Function calls itself then it is called as Recursion

def Harsh(num):
    if num == 0:
        return
    print(num)
    return Harsh(num-1)

Harsh(10)

# 25 to 35
num2 = 35
# x = 35

def Hiral(num1):
    if num1 == num2+1:
        return 
    print(num1,end=' ')
    return Hiral(num1+1)

# Hiral(25)

# print()
# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num-1)  # 5 * 4 * 3 * 2 * 1

# print(factorial(500))


# Fibonacci
print()
print()

from functools import lru_cache

@lru_cache(maxsize=1000)
def fibo(num):
    if num == 1 or num == 0:
        return num
    return fibo(num-1) + fibo(num - 2)

print(fibo(100))


# 0 1 1 2
for i in range(100):
    print(fibo(i),end=' ')