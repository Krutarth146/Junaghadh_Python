# File Handling

# File Types
# 1. Text File  ---> 't'
# 2. Binary File ---> 'b'

# Modes:

# 'w' --> Write Mode (If file does not Exist then It will Create a New File, Overwrite)
# 'r' --> Read Mode (If file Does NOt Exist then It will Generate an Error)
# 'a' --> Append Mode (Append The data to last line of file)
# '+' --> Read + Write Mode


# fp = open("manoj.txt", 'w')

# # print(fp)   # <_io.TextIOWrapper name='manoj.txt' mode='w' encoding='cp1252'>

# fp.write("Hello Uday Patel!")
# fp.write("\nParth\tPatel")

# list1 = ['\nRoyal Technosoft ', 'Pvt LTD ', 'Dhiraj Sir ']


# fp.writelines(list1)

# print(type(fp))   # <class '_io.TextIOWrapper'>
# # fp.close()

# print(fp)


# fp = open("manoj.txt", 'r')  

# # x = fp.read()

# print(fp.tell())  # 0
# print(fp.readline())
# print(fp.tell())  # 19

# print(fp.readline())
# print(fp.tell())  # 32

# print(fp.readline())
# print(fp.readline())
# print(fp.readline())
# print(fp.readline())
# print(fp.tell())  # 94


# fp.seek(32)  # HW ---------------------

# print(fp.readline())
# # print(x)

# fp.seek(0)

# print(fp.readlines())

# # Royal Akshay is Good Student

# fp.close()



fp = open("manoj.txt",'w')

fp.write("Hello Tathya Patel\nsdvcsdcds")

fp.close()

# ------------------------------------


fr = open("dict_ss.png",'rb')

x1 = fr.read()

print(x1)

fr.close()

new = open("d_copy.png", "wb")

new.write(x1)

new.close()


# --------------------------------------

akshay  = open("Ak.txt", 'w+')

akshay.write("Hello This is AkshAy Solanki\nI am a Good Student\nI am also very Intelligent Guy.")

print(akshay.tell())  # 82

akshay.seek(0)

print(akshay.tell())   # 0

data = akshay.readlines()
print(data)

words = []
for i in data:
    words.extend(i.split())


print(len(words))   # 16
print(words)

c = 0
for wo in words:
    for ch in wo:
        c+=1

for j in words:
    if j.startswith("S"):
        print(j)

for i in range(len(words)):
    if words[i][0] == 'G':
        print(words[i])

print(c)  # 65
akshay.close()