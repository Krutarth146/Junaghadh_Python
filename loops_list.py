# # 3 + 33 + 333 + 3333 + 33333 = (?)


# num = 4
# step = 3

# # 3 ---> 33  -----> 333
# # num = num * 10 + 3  # 3 * 10 + 3  ---> 33
# # num = num * 10 + 3  # 33 * 10 + 3 ----> 333
# # num = num * 10 + 3  # 33 * 10 + 3 ----> 3333
# # num = num * 10 + 3  # 33 * 10 + 3 ----> 33333
# vivek = num
# i = 1  # start
# sum = 0
# while i <= step:  # Condition
#     print(num)           # 3
#     sum += num
#     num = num * 10 + vivek   # 33
#     i+=1 # Flow          # i =2

# print(sum)  # 37035

# # ----------------------------------------

# # For loop

# for khushi in range(10):  # ENd - 10 (n-1), start - 0 (default - 0)
#     print(khushi,end=' ')  # 0 1 2 3 4 5 6 7 8 9
# print()

# for k in range(7, 26):   # start - 7, End - 26 (n-1) 25  [7 to 25]
#     print(k,end=' ')  # 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

# print()


# for w in range(26,7):
#     print(w)   # No O/p


# for q in range(3, 41, 2): # (start, end(n-1), step(n-1))
#     print(q,end=' ')  # 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39


# # for w in range(10,3):
# for w in range(10,3,1):
#     print(w)  # No o/p
# print()
# print()
# for q in range(10,3,-1):   # step -> Positive Side / Negative Side
#     print(q,end=' ')  # 10 9 8 7 6 5 4

# step -> Positive Side / Negative Side
# STep -> How Many Steps (SKip)
# print()
# for q in range(50,20,-2):   # step -> Positive Side / Negative Side
#     print(q,end=' ')  # 50 48 46 44 42 40 38 36 34 32 30 28 26 24 22

# print()


# for h in range(-2 , -10, 2):
#     print(h)  # No o/p

# print()

# for g in range(-1, -2 , -3):
#     print(g)
# print()

# for g in range(-10, -2 , 3):
#     print(g)  # -10 -7 -4

# print()

for a in range(5,-4,3):
    print(a)

# if bool(0) is False:
#     print("0 is False")
# else:
#     print("Fail")


print()

for f in range(-3,5,2):
    print(f)  # -3 -1 1 3


# While  / For 
# 
for j in range(1,101): 
    if j % 2 != 0:
        print(j,end=' ')  # 
print()
# print()
# for h in range(5,101,5):
#     print(h,end=' ')

for j in range(1,101):
    if j % 5 == 0 or j % 7 == 0:
        print(j,end=' ')  # 35 70
# 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99

x = 90  # Assignment (Low Priority)
x == 90  # Equality O/p (Comparison)

count = 0
ex_count = 0
for i in range(3): # (0 to 2)         # i = 2  # Total Loop freq - 3
    for j in range(3):  # (0 to 2)    # j = 0  # # Total Loop freq - 9
        print(i,j)     # (0 0) (0 1) (0 2) (1 0) (1 1) (1 2) (2 0) (2 1) (2 2)
        count+=1
    ex_count+=1

print(count)  # 9
print(ex_count)  # 3


list1 = [10,20,30,40,50,56,90]
# [(10,10), (10,20), (10,30), (10,40)....]


for k in list1:
    print(k)

# for k in range(7):
for k in range(len(list1)):  # 0 1 2 3 4 5 6
    print(list1[k]) # list1[0]

list1 = [10,20,30,40,50,56,90]
# [(10,10), (10,20), (10,30), (10,40)....]
ans = []
for aman in list1:
    for parth in list1:
        ans.append((aman,parth))

print(ans)  # [(10, 10), (10, 20), (10, 30), (10, 40), (10, 50), (10, 56), (10, 90), (20, 10), (20, 20), (20, 30), (20, 40), (20, 50), (20, 56), (20, 90), (30, 10), (30, 20), (30, 30), (30, 40), (30, 50), (30, 56), (30, 90), (40, 10), (40, 20), (40, 30), (40, 40), (40, 50), (40, 56), (40, 90), (50, 10), (50, 20), (50, 30), (50, 40), (50, 50), (50, 56), (50, 90), (56, 10), (56, 20), (56, 30), (56, 40), (56, 50), (56, 56), (56, 90), (90, 10), (90, 20), (90, 30), (90, 40), (90, 50), (90, 56), (90, 90)]
 
# Table -----