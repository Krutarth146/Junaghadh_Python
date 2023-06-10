# Prime Number

# 23 ---> 1, 23
# 29 ---> 1, 29
# 24 ---> 1,2,3,4,6,8,12,24
# 32 ---> 1,2,4,8,16,32
# 37 ---> 1, 37

num = 5
divisor = 0

for i in range(1,num+1):  # 1 to 5   # i = 2
    if num % i == 0:  # 5 % 5 == 0
        # print(i)     # 1 5
        divisor = divisor + 1  # 2

# print(divisor)  # 2

if divisor == 2:   # 2 == 2
    print(num,"is Prime")

#  ------------------------------------------

# Prime Numbers in Range (1 to 10000)

# for num in range(1,10001):   # 26
#     divisor = 0  

#     for j in range(1,num+1):  # 1 to 26
#         if num % j == 0:
#             divisor += 1

#     if divisor == 2:
#         print(num,end=' ')


# Perfect Numbers

# 28 ----> 1 to 27     # 1 + 2 + 4 + 7 + 14 ---> 28


i = 1
num = 6
sum = 0

while i < num:  # 1 to 27
    if num % i == 0:
        sum += i
    i+=1

if sum == num:
    print("Perfect")

# 1 to 10k Perfect Numbers

# -------------------------------------------------

# print Reverse Numbers

num = 7590     # ---> 376  # Ans. 3

# while num!=0:
while num > 0:
    rem = num % 10    # rem = 7
    print(rem,end='') # 957
    num = num // 10    # num = 0

print()
# ------------------------------------
num = 9521     # ---> 376  # Ans. 3
sum = 0
# while num!=0:
while num > 0:
    rem = num % 10    # rem = 
    sum = sum + rem   # sum = 9 + 5 + 7 = 21
    num = num // 10    # num = 0

print(sum)  # 17


# ------------------------------------
num = 95    # ---> 376  # Ans. 3
digit = 0
# while num!=0:
while num > 0:
    digit += 1   #
    num = num // 10    # num = 0

print(digit)  # 17




# ------------------------------------
num = 101     # ---> 376  # Ans. 3
rev = 0
safe = num

# while num!=0:
while num > 0:
    rem = num % 10         # rem = 3
    rev = rev * 10 + rem   # sum = 243
    num = num // 10        # num = 0

print(rev)  # 243

if rev == safe:  # 101 == 101
    print("Palindrome")
else:
    print("Fail")

# 1 to 10000  Palindrome numbers



# ------------------------------------
num = 153     # ---> 376  # Ans. 3
rev = 0
safe = num

# while num!=0:
while num > 0:
    rem = num % 10         # rem = 3
    rev = rev + rem ** len(str(safe))    # sum = 243
    num = num // 10        # num = 0

print(rev)  # 243

if rev == safe:  # 101 == 101
    print("Armstrong")
else:
    print("Fail")

# 1 to 10000  Armstrong numbers