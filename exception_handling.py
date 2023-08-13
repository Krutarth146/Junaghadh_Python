# Exception Handling

print("Hello")

# x = int(input())
# y = input()
# print(x+y)


try:
    num = int(input("Enter Number: "))
    print(56 // num)
    print(32 + 'str1')


except ZeroDivisionError:
    print('Zerodivision Error Occured')

except ArithmeticError:
    print('ArithmeticError Error Occured')


# except Exception as e: 
except: 
    print("Error Occured")

else:
    print("Else Block called")

finally:
    print("Finally Block is always Executed")

print("Aman")