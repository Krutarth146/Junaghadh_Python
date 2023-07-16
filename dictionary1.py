# Dictionary:
# key-value Pair

dict1 = {}
print(type(dict1))  # <class 'dict'>


set1 = {10}
print(type(set1))   # <class 'set'>


dict2 = {'Name' : "Khushi", 'list1' : [10,20,30,40], 45 : 3}
print(dict2)   # {'Name': 'Khushi', 'list1': [10, 20, 30, 40], 45: 3}

print(len(dict2))  # 3
print(id(dict2))  # 2363150548224

print(dict2.__sizeof__())   # 216

print(dict2['list1'])   # [10, 20, 30, 40]

# Dictionary Characteristics: Ordered, Mutable (Changeble), Unique Keys (Don't Allowed Duplicates), values aloows Duplicates


dict1 = {"name" : "Parth", 'roll' : 900, 'name' : "Manoj"}
print(dict1)   # {'name': 'Manoj', 'roll': 900}


dict1 = {'Name' : "Krutarth", 'address' : {'Area' : 'Shahpur', 'pincode' : [10,20,30,30,40,50]}}

print(dict1)   # {'Name': 'Krutarth', 'address': {'Area': 'Shahpur', 'pincode': [10, 20, 30, 30, 40, 50]}}
print(dict1)   # {'Name': 'Krutarth', 'address': {'Area': 'Shahpur', 'pincode': [10, 20, 30, 30, 40, 50]}}

print(dict1['address']['pincode'][2])   # 30
print(dict1.keys())   # dict_keys(['Name', 'address'])
print(dict1.values())   # dict_values(['Krutarth', {'Area': 'Shahpur', 'pincode': [10, 20, 30, 30, 40, 50]}])

print(dict1.items())  # dict_items([('Name', 'Krutarth'), ('address', {'Area': 'Shahpur', 'pincode': [10, 20, 30, 30, 40, 50]})])

print(dict1['address'].keys())  # dict_keys(['Area', 'pincode'])
print(dict1['address'].values())  # dict_values(['Shahpur', [10, 20, 30, 30, 40, 50]])


for k in dict1:
    print(k)  # Name, address

dict1 = {'Name' : "Krutarth", 'address' : {'Area' : 'Shahpur', 'pincode' : [10,20,30,30,40,50]}}
for j in dict1.values():
    print(j)  # 
    print(type(j))  # str, dict


for k in dict1.items():
    print(k)   
    # ('Name', 'Krutarth')
    # ('address', {'Area': 'Shahpur', 'pincode': [10, 20, 30, 30, 40, 50]})


print(dict1['address']['Area'])   # Shahpur

# for key, val in dict1.items():
#     if val == 'Krutarth':
#         print(key)  # Name
print()
print()

for key, val in dict1.items():
    if type(val) == type({}):
        print("-------")
        if 'cgroad' in val.values():
            print(key)  # Name


dict1['Name'] = "Uday"
print(dict1)  # {'Name': 'Uday', 'address': {'Area': 'Shahpur', 'pincode': [10, 20, 30, 30, 40, 50]}}

# print(dict1['Name1'])  # Uday
# print(dict1.get('Name1'))   # Uday   # If key is not Found then it will not give any Error

dict1['age'] = 900
print(dict1)   # {'Name': 'Uday', 'address': {'Area': 'Shahpur', 'pincode': [10, 20, 30, 30, 40, 50]}, 'age': 900}

dict1.update({'Education' : 'MSC'})   # Mutable
print(dict1)   # {'Name': 'Uday', 'address': {'Area': 'Shahpur', 'pincode': [10, 20, 30, 30, 40, 50]}, 'age': 900, 'Education': 'MSC'} 

dict2 = dict1.copy()   # Shallow Copy
dict3 = dict1   # Deep Copy


dict3['roll'] = 700


print(dict3)
print(dict1)

# {'Name': 'Uday', 'address': {'Area': 'Shahpur', 'pincode': [10, 20, 30, 30, 40, 50]}, 'age': 900, 'Education': 'MSC', 'roll': 700}    
# {'Name': 'Uday', 'address': {'Area': 'Shahpur', 'pincode': [10, 20, 30, 30, 40, 50]}, 'age': 900, 'Education': 'MSC', 'roll': 700}
print(dict2)   # {'Name': 'Uday', 'address': {'Area': 'Shahpur', 'pincode': [10, 20, 30, 30, 40, 50]}, 'age': 900, 'Education': 'MSC'}

print(id(dict3))
print(id(dict1))


dict1.pop('Name')
print(dict1)   # {'address': {'Area': 'Shahpur', 'pincode': [10, 20, 30, 30, 40, 50]}, 'age': 900, 'Education': 'MSC', 'roll': 700}

x = dict1.popitem()
print(dict1)   # {'address': {'Area': 'Shahpur', 'pincode': [10, 20, 30, 30, 40, 50]}, 'age': 900, 'Education': 'MSC'}
print(x)   # ('roll', 700)



list1 = ('str1', 'str2', 'str3')
dict2 = dict.fromkeys({list1 : 0})
print(dict2)   # {('str1', 'str2', 'str3'): None}
  

list1 = [10,20,78,342,11]
 # Cube

# {10 : 1000, 20 : 8000, 78 : 474552, 342 : ...}

dict1 = {}


for x in list1:
    dict1[x] = x**3

print(dict1)

dict3 = [{x : x**3} for x in list1]
print(dict3)   # [{10: 1000}, {20: 8000}, {78: 474552}, {342: 40001688}, {11: 1331}]

print()
print()

l2 = [2,2,2,1,2,3,3,4,5,2,2]
l5 = list(set(l2))

dict5 = {}
print(l5)  # [1,2,3,4,5]

for i in l5:
    temp = []
    for j in range(len(l2)):
        if i == l2[j]:
            temp.append(j)
            print(temp)
    dict5[i] = temp

print(dict5)

print()
print()

l2 = [2,2,2,1,2,3,3,4,5,2,2]
l5 = list(set(l2))

dict5 = {}
print(l5)  # [1,2,3,4,5]

for i in l5:
    temp = []
    for j in range(len(l2)):
        if i == l2[j]:
            temp.append(j)
            # print(temp)
    dict5[i] = temp

print(dict5)

print([{i:[j for j in range(len(l2)) if i == l2[j]] for i in l5}])

l9 = [{i: [j for j in range(len(l2)) if i == l2[j]]} for i in l5 ]
print(l9)

dict_new = {}

for i in l9:
    dict_new.update(i)
print(dict_new)  # {1: [3], 2: [0, 1, 2, 4, 9, 10], 3: [5, 6], 4: [7], 5: [8]}


l4 = [k for k in range(1,11) if k % 2 != 0]
print(l4)   # [1, 3, 5, 7, 9]

# 32732737235

# l4 = [(10,3), (1,2,7), (2,1,3), (4,0)]


# def last_digit(ele):
#     return ele[-1]

# l4.sort(key=last_digit)
# print(l4)

l4 = [(10,3), (1,2,2), (2,1,3), (4,0)]

for i in range(len(l4)):
    for j in range(i+1, len(l4)):
        if l4[i][-1] > l4[j][-1]:
            l4[i],l4[j] = l4[j],l4[i]

print(l4)

# -------------------
str1 = ["Palindrome", "eye", 'Uday']

blank = []
for i in str1:
    if i.lower()[::-1] == i.lower():
        blank.append(True)
    else:
        blank.append(False)
print(blank)

palindrome = [i for i in str1 if i.lower()[::-1] == i.lower()]
print(palindrome)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.