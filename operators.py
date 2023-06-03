# Operators

# print(2**3**2)  # 512

# print(89 + 26 / 4 % 2)  # 89.5
# print(89 / 22 % 2)  # 0.04545454545454586


# # Assignment  = += -= *= /= //= %= &= |= ^= (Low Priority)
# a = 20
# a += 1  # 21     # a = a+1   
# a += 40  # 61
# a /= 2   # 30.5
# a %= 2   # 0.5
# print(a)   # 0.5



# Bitwise O/p ---->   & | ^ << >> (Bit by Bit Conversion)

# Decimal to Binary

# 893, 9034, 3425, 211, 466

# Binary to Decimal

# 1010111  10001  101  10100111111


# print(45 & 89)  # 9
# print(213 | 67)  # 215
# print(34 | 82)   # 114
# print(711 ^ 25)  # 734  
# print(987 << 4)  # 15792
# print(345 >> 2)  # 86


# Logical O/p

# and or not

# Comparison O/p ---> == != < > <= >=

# IF ELSE
# name = input("Enter Name: ")
# age = int(input("Enter Age: "))

# if age >= 18:
#     print(f"{name} is Eligible for Voting.")
# elif age <= 0:
#     print("Pls Enter Valid Age.") 
# else:
#     print(f"{name} is not Eligible for Voting. You need {18-age} years.")


# ---------------------------
num = 740
if num % 5 == 0 or num % 7 == 0 and num % 10 == 0:
    print("Vivek")
else:
    print("ROyal Manopj")

# Vivek

x = 90
print(~x)  # -91 # Find  H.w

y = -23
print(~y)  # 22  # Find  H.w



# H.W.
# Total Days ------> Find -> Total Years, Months, Rem_days
# Total Seconds ---> Find -> Total Hours, Minutes, seconds

# 400 -> 1 Year, 1 Month, 5 rem_days
# Leap Year


# Linear Search

list1 = [10,90,78,67,45,32]

need = 46


for vivek in list1:
    if need == vivek:
        print(f"{need} is Found")
        break
else:
    print("Not Found")


# Membership O/p  in   not in
if need \
    in \
    list1:
    print(f"{need} is Found")
else:
    print("Not Found")  