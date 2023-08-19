# # Exception Handling

# print("Hello")

# # x = int(input())
# # y = input()
# # print(x+y)


# try:
#     num = int(input("Enter Number: "))
#     print(56 // num)
#     print(32 + 'str1')


# except ZeroDivisionError:
#     print('Zerodivision Error Occured')

# except ArithmeticError:
#     print('ArithmeticError Error Occured')


# # except Exception as e: 
# except: 
#     print("Error Occured")

# else:
#     print("Else Block called")

# finally:
#     print("Finally Block is always Executed")

# print("Aman")


# ------------------------------------------------------------
list1 = []

# def signup():
#     username = input("Enter Username: ")
#     password = input("Enter Password: ")
#     al,num,valid,valid_1 = False, False, False, False


#     for i in username:
#         if (ord(i) >= 65 and ord(i)<= 90) or (ord(i)>=97 and ord(i)<=122):
#             al = True

#         if i >= '0' and i<='9':
#             num = True

#         if al == True and num == True:
#             valid = True
#             break

#     alpha,num1,sp = 0,0,0

#     for i in password:
#         if (i >= "A" and i<="Z") or (i >= 'a' and i<= 'z'):
#             alpha+=1
#         elif (i >= '0' and i<='9'):
#             num1 += 1
#         else:
#             sp+=1

#     if alpha >= 1 and num1 >= 1 and sp >= 1:
#         valid_1 = True
        


#     if valid == True and valid_1:
#         list1.append({username : password})
#         return list1
#     else:
#         raise Exception("Pls Enter Valid Username with Letters and Numbers.")


list1 = [{"Manoj12" : "Manoj@123"}, {"Ashok12" : "Ashok@123"}]

def login(list1):
    username1 = input("Pls Enter Username: ")
    pass1 = input("Pls Enter Password: ")

    for i in list1:
        print(i.keys())
        if i.get(username1) == pass1:
            print("Valid Credentials")
            break
    else:
        print("Invalid or wrong Credentials")

# signup()
# signup()

login(list1)

