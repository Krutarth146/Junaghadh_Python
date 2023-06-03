for j in range(-3, 5, 2):
    print(j,end=' ')   # -3 -1 1 3 

print()

for g in range(-8, -1, -2):
    print(g)

print()

for h in range(5, -2, -3):
    print(h,end=' ')  # 5 2 -1

# While loop

# start point, ENd point, FLow (Incre / Decre)

# 25 to 65
print()
vivek = 25   # Intialization

while vivek <= 65:   # Condition
    print(vivek,end=' ')   # statements
    if vivek == 35:
        print("Hello") 
        break

    vivek += 1     # Flow

print()
print(vivek)   # 35

# 25 26 27 28 29 30 31 32 33 34 35 Hello
# (10) , (3,10), (1,10,-2)  in for loop


num = 1
while num <= 15:
    num += 1 
    if num == 10:
        # print("Hello")
        continue
    print(num)

# --------------------------------

i = 2

while i <= 4:
    j = 1
    while j <= 4:
        if i == j:
            break
        print(j, end=' ')
        j+=1
    print(i,end=' ')
    i+=1

# -----------------------------


i = 4
while 10:
    if i == 7:
        break
    print(i)
    i+=1

# 4 5 6

# ----------------------

num = 1
kum = 1
while num <= 5:

    while kum <= 4:
        if num == kum:
            kum+=1
            continue
        print(kum)
        kum+=1
    print(num)
    num += 1






# internal_loop = 0
# outer_loop = 0

# num = 1

# while num <= 5:
    
#     kum = 25
#     while kum <= 30:
#         print(kum,end=' ')
#         internal_loop += 1
#         kum += 1
#     outer_loop+=1
#     num += 1
# print()
# print(internal_loop,outer_loop,sep='\t')


# base = int(input("ENter Base: "))
# power = int(input("ENter Power: "))


# i = 1
# akshay = 1

# while i <= power:
#     akshay = akshay * base
#     i+=1

# print(akshay)



# ---------------------------------

for i in range(5):
    for j in range(3):
        if i == j:
            print("Hello",end= ' ')
    print(i,end=' ')
else:
    print("Else Block Executed")

# Hello 0 Hello 1 Hello 2 3 4 Else Block Executed


# If loop is Naturally Executed then ELse block is Executed otherwise Not.