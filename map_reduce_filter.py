
max1 = lambda num1, num2, num3 : (num1 if num1 > num3 else num3) if num1 > num2 else (num2 if num2 > num3 else num3)
print(max1(10,99,340))   # 99


# list1 = [10,20,30,94,56,43,32]

# def square(num):
#     return num ** 2

# print(square(5))   # 25

# # --------------------------------


# for i in list1:
#     print(square(i))


# x1 = map(lambda x : x * x, list1)
# print(x1)   # <map object at 0x000001A66807C610>

# x2 = list(map(lambda x : x * x, list1))
# x2 = list(map(square, list1))
# print(x2)   # [100, 400, 900, 8836, 3136, 1849, 1024]


# ---------------------------------------

# Filter

list1 = [10,20,30,94,56,43,32]

list7 = list(map(lambda x : x > 50 ,list1))

print(list7)   # [False, False, False, True, True, False, False]


list7 = list(filter(lambda x : x > 50 ,list1))
print(list7)   # [94, 56]

list7 = list(filter(lambda x : x % 2 != 0 ,list1))
print(list7)   # [43]


# Reduce ------------------------------


# import functools

# import numpy as np

# numpy.array
# np.array

# functools.reduce

# sum1 = 0

# for i in list1:
#     sum1 = sum1 + i

# print(sum1)  # 512

from functools import reduce

list1 = [10,90,35,89,221,67]

list8 = reduce(lambda n1 , n2 : n1 + n2 , list1)

print(list8)   # 512


from itertools import accumulate

list8 = list(accumulate(list1, lambda n1,n2 : n1 * n2))

print(list8)   # [10, 900, 31500, 2803500, 619573500, 41511424500]


# ---------------------------------------------------------------


# We can make function under function


def prachi(f8):
    def Arin():
        print("Arin FUnction")
        f8()

    def royal():
        print("Royal Techno")

    # Arin()
    royal()
    return Arin()


def mit():
    print("Mithil Function")

prachi(mit)



# ----------------------------------------------
def prachi(f8):
    def Arin():
        print("Arin FUnction")
        f8()

    return Arin()

@prachi   # Custom Decorator
def mit():
    print("Mithil Function")

# prachi(mit)

@prachi   # Custom Decorator
def Bansi():
    print("Bansi is Good")


# @classmethod  (Inbuilt)
# @staticmethod