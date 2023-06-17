# 1 to 10000 Armstrong

# 1232 ---> 2*2*2*2 + 3*3*3*3 + 2*2*2*2 + 1*1*1*1 = 33 + 81 = 114


num = 1  # Intialization
while num <= 10000:
    xerox = num
    sum = 0

    while num != 0:
        remainder = num % 10   # Remainder = 9
        sum = sum + remainder ** len(str(xerox))  # sum = 8 + 729 = 737
        num = num // 10    # num = 0


    if sum == xerox:  # 737 == 0
        print(xerox)
    num = xerox
    num+=1


# Twin Number

# 22 ---> 2+2 == 2*2
# 231 --> 1+3+2 == 1*3*2

sum = 0
mul = 1
num = 321

while num > 0:
    rem = num % 10
    sum = sum + rem
    mul = mul * rem
    num = num // 10

if sum == mul:
    print("Twin Number")


# ------------------------------------------------


# String ----> String Is Immutable (Not Changeble)

str1 = 'J'
print(type(str1))

str2 = "Jakskasfa"
print(str2)

str3 = '90'
print(type(str3))


str4 = """677dscsdc"""
print(str4)

print(id(str3))   # 2668971416688
str3 += str4
print(str3)
print(id(str3))   # 2668971417072


# String Indexing And Slicing

str1 = "Royal_is Best Institute Ever123."

print(str1[-1])  # .
print(str1[3])  # a
print(str1[-10])  # e


# Slicing 
str1 = "Royal_is Best Institute Ever123."
print(str1[0 : 5])   # Royal
print(str1[10 : 5])   # blank
print(str1[-6 : -1])   # er123
print(str1[-3 : 3])   # 
print(str1[-3 : -3])   # 
print(str1[-3 : -1])   # 23
print(str1[-3 : ])   # 23.
print(str1[ -3: 0 : ])   # 
print(str1[ 3 :  : 2])   # a_sBs nttt vr2.
print(str1[ -4 : 5 : 2])   # blank
print(str1[ -4 : 5 : -1])   # 1revE etutitsnI tseB si
print(str1[ -1 : -9 : -1])   # .321revE



# String Methods


str1 = "Royal_is Best Institute Ever123."


list1 = str1.split()
print(list1)  # ['Royal_is', 'Best', 'Institute', 'Ever123.']

list2 = str1.split(" ")
print(list2)  # ['Royal_is', 'Best', 'Institute', 'Ever123.']

list2 = str1.split("_")
print(list2)  # ['Royal', 'is Best Institute Ever123.']

list2 = str1.split("t")
print(list2)  # ['Royal_is Bes', ' Ins', 'i', 'u', 'e Ever123.']

print(str1.partition('t'))  # ('Royal_is Bes', 't', ' Institute Ever123.')
print(str1.rpartition('t'))  # ('Royal_is Best Institu', 't', 'e Ever123.')



# l1 = ['Uday', 'Badshah']

str3 = ' '.join(str1)
print(str3)

print(len(str1))  # 32
print(str1.center(40, '*'))  # ****Royal_is Best Institute Ever123.****

str1 = "Royal_is Best Institute Ever123."
print(str1.find("t"))   # 12
print(str1.rfind("t"))   # 21
print(str1.rfind("t",13,20))   # 19
print(str1.index('t'))   # 12 
print(str1.count('z'))   # 0
 
# str1 = str1.replace('Institute', 'College')
str1 = str1.replace('e', 'o', 1)   # Royal_is Bost Institute Ever123.
print(str1)

str5 = "Nayan"

# print(str5[::-1])

str5 = str5.lower()

if str5 == str5[::-1]:
    print("Plaindrome")  # Plaindrome

str4 = "Ståle" 
print(str4.encode())   # b'St\xc3\xa5le'
print(str4.encode(encoding="ascii", errors="namereplace"))   # b'St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
print(str4.encode(encoding="ascii", errors="replace"))   # b'St?le'

str4 = "{1} is {0} Boy.".format("Uday", "Good")

print("%s" %"Uday")
print("%d" %500)
print("%.2f" % 900.789)
print("%2.2f" % 900.789)
print("%c" % 97)  # a
print(str4)


dict1 = {'Name' : "Kruatarth", 'Inst' : "Royal"}

print("{Name} , {Inst}".format_map(dict1))


str4 = "Hello"
print(str4.ljust(10,'*'))   # Hello*****

str4 = '     Uday         '
print(str4.strip())  # Uday


print(str4.swapcase())

str4 = '100000'
print(str4.zfill(12))   # 0100000


str8 = "Hello Sam Udev"

table = str8.maketrans('Sam','Ram',' U')
print(table)

str8 = str8.translate(table)
print(str8)