# Error and Exception

# age = 22
# if age > 18:
# print('Major')

# num = int(input())

# try:
#     print(25 // num)
# except:
#     print("Division By Zero is Not Allowed")

# print('Outside of try-catch Block')

# ----------------------------------------------------------------


# Exception  ----> Base class

# num = 90
# str1 = "Mithil"

# try:
#     print(num + int(str1))
# except Exception as err:
#     print('Error! Not Possible',err)   # Error! Not Possible invalid literal for int() with base 10: 'Mithil'
    
# # Built In Exception classes


# -------------------------------------------


# list1 = [10,20,30,40,506,60]

# try:
#     for i in list1:
#         if i >= 100:
#             b = i + 50
#         else:
#             x = int(input("Enter ELement: "))
#             print(b)
#             print(x+b)


# except ZeroDivisionError:
#     print("Zero Division Error")

# except ArithmeticError:
#     print("Arithmetic Error Occured and Handled")

# except NameError:
#     print("Name Error Occured and Handled")

# except Exception as err:
#     print('Error! Not Possible',err)   # Error! Not Possible invalid literal for int() with base 10: 'Mithil'
    
# Built In Exception classes


try:
    f1 = open("String_Exercises1.txt",'r')
    print("File is Successfully Opened")

except FileNotFoundError:
    print("File Not Found at this Path")

else:   # If any Exception is Not occued then Else Block will be Executed
    f1.close() 
    print("File is Successfully closed")


# -------------------------------------------------------------



def print_series(num):
    for i in range(1,num+1):
        print("yielding",i)
        yield i


x = print_series(2)

try:
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
except AssertionError:
    print('Assertion Error Occured')
else:
    print("Generation Successfully")
finally:
    print("This is Finally block which is always Executed!")

print('Outside block')


# raise keyword, User Defined Exception, nzec Error, logging