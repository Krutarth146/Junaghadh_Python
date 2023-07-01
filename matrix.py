list2 = [[10,20,30], 
         [40,51,60], 
         [71,80,90]]


print(len(list2))  # 3

for i in list2:  # i = [10,20,30]
    print(i)

# [10, 20, 30]
# [40, 50, 60]
# [70, 80, 90]

sum = 0
for sublist in list2:
    for element in sublist:
        if element % 2 == 1:
            print(element,end=' ')  # 51 71
        sum += element
print(sum)  # 452



list2 = [[10,20,30], 
         [40,51,60], 
         [71,80,90]]


for row in range(len(list2)):  # 3 ---> 0 1 2   row = 1
    if row % 2 == 0:
        for col in range(len(list2[row])): # 3 ---> 0 1 2  col = 0
            print(list2[row][col],end=' ')  # list2[2][2]
    else:
        for col in range(len(list2[row])-1,-1,-1):
            print(list2[row][col],end=' ')  # 10 20 30 60 51 40 71 80 90




list2 = [[10,20,30], 
         [40,51,60], 
         [71,80,90]]

# 10 51 90
sum = 0
for row in range(len(list2)):
    for col in range(len(list2[row])):
        if row == col:
            sum = sum + list2[row][col]
print()
print(sum)  # 151

print()
sum = 0
for row in range(len(list2)):
    for col in range(len(list2[row])):
        if row+col == len(list2)-1:
            sum = sum + list2[row][col]

print(sum)  # 152

print()
sum = 0
length = len(list2)
for row in range(len(list2)):
    sum = sum + list2[row][length - 1 - row]

print(sum)  # 152


# Transpose
list2 = [[10,20,30], 
         [40,51,60], 
         [71,80,90]]

for row in range(len(list2)):
    for col in range(len(list2[row])):
        print(list2[col][row],end=' ')  # list2[0][1]  # 10 40 71 20 .....
    print()

# HW
# 10 20 30 60 90 80 71 40 51  (Spiral)
