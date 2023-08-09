# Functions   --> Code Reusability, 

# 1. Predefined Function ---> len(), min(), max(), print(), input()
# 2. User-defined Functions

# Func. Declaration

# void sum();  // Func. Declaration

# main()
# {
#     sum() # Func. Calling
# }


# void sum()  # Func. Defination
# {
#     print("Hello")
# }

# 1. Func. Defination
# 2. Func. Calling

# FUnction Types

# 1. Without args and without Return Type
# 2. With args and without Return Type
# 3. Without args and with Return Type
# 4. With args and with Return Type


# 1. Without args and without Return Type

def dhairya():
    print("Hello World")
    for i in range(5):
        print(i)

dhairya()


x = 10   # GLobal Variable
def royal():
    x = 50   # local variable
    x+=10   # 60
    print(x)  # 60
    print("Harsh Vyas")

royal()   # 60
x+=20   # 30   # GLobal variable
print(x)  # 30


x = 10   # Global Variable
def royal():
    global x  # GLobal Variable
    x+=10   # 20
    print(x)  # 20
    print("Harsh Vyas")

royal()   # 20
x+=20   # 40   # GLobal variable
print(x)  # 40



# 2. With args and without Return Type

def patel(num1 = 90,num2 = 90, num3 = 2):  # Default FUnction
    x = int(input())
    print(2, num2 * num3, x)

# patel(10,"Mithil ",4)   # 10 Mithil Mithil Mithil
# patel()   # 10 Mithil Mithil Mithil


def techno(n1,n2, *kru):
    print(kru)
    print(type(kru))   # <class 'tuple'>

    for i in kru:
        print(i)

techno(10,20,"str1", [10,20])   # (10, 20, 'str1', [10, 20])