# # 2. With arguments and without Return Type

# def Mithil(num1, num2, num3="str1"):
#     print(num1 * num2, num3)

# Mithil(10,30)   # 9600


# def Harsh(*args):
#     print(args)   # ([10, 90.99, [10, 20, 30], {10, 20}],)
#     print(type(args))   # <class 'tuple'>

#     for i in args:
#         print(i)

#     print(args[-1][-3])   # 90.99   float


# list1 = [10,90.990, [10,20,30], {10,20}]
# Harsh(list1)


# def sbsir(n1,n2,*args,n5=91):
#     print(args)

# sbsir(10,20,30,40,50,90)


# # **kwargs

# dict1 = {"name" : "Nupur", 'name' : 'Mithil'}

# print(dict1)


# # ----------------------------------------------

# def Nupur(*args, **kwargs):
#     print(kwargs)   # {'name': 'Nupur', 'roll': 500, 'address': 'Gnr'}
#     kwargs['age'] = 10
#     kwargs.update({'Institute' : "Royal"})
#     print(kwargs)


# Nupur(10,20,30,40,50,name = "Nupur", roll = 500, address = "Gnr")   # {'name': 'Nupur', 'roll': 500, 'address': 'Gnr', 'age': 10, 'Institute': 'Royal'}



# 3. With return Type and without Args.

def Bansi():
    return 90,80,32,89.423,[10,20]

# 1.
x = Bansi() 
print(x)         # (90, 80, 32, 89.423, [10, 20])

# 2.
print(Bansi())   # (90, 80, 32, 89.423, [10, 20])


def series():
    num = 10
    list1 = []
    for i in range(1,num + 1):
        # print(i,end=' ')
        list1.append(i)
    return list1


print(series())   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# -------------------------------------------------

# def series():
#     num = 10

#     for i in range(1,num + 1):   # i = 1
#         return i   # 1

# print(series())   # 1

# --------------------------------------------

def series():
    num = 10

    for i in range(1,num + 1):   # i = 1
        yield i   # 1   # Generator
 
# print(series())   # <generator object series at 0x00000297C9EA9A10>

# for i in series():
#     print(i)   # 1 to 10

# print(series().__next__())
x = series()

print(type(x))  # Generator
print(x.__next__())
print(x.__next__())
print(x.__next__())
# print(x.__next__())

# x = series
# x = series()




# num1, num2, num3


# We can pass function as an argument


def fun2(f4):
    print("This is fun2 FUnction")
    f4()

def akshat():
    print("Akshat Function")


fun2(akshat)



# We can make function under function


def prachi(f8):
    def Arin():
        print("Arin FUnction")
        f8()

    return Arin()


def mithil():
    print("Mithil Function")

prachi(mithil)