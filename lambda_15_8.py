# lambda ---> Anounoumous Function  (One Liner)

# Square

def square(num):
    return num ** 2

print(square(5))


square_l = lambda num : num ** 2

print(square_l(4))   # 16



# --------------

reverse = lambda str1 : str1[::-1]
print(reverse("Shubham"))   # mahbuhS


n = lambda *args : args[0] + 10
print(n(10,20,304))   # 20


p1 = lambda num1, num2, num3 = 3 : num1 ** num2 + num3

print(p1(10,2))   # 103



# (a*x**2) + (b*x) + (c)

# a,b,c,x
var1 = 90

def quadratic_fun(a1,b1,c1):
    return lambda var1=90: lambda x1, x2 : (a1*var1**2) + (b1*var1) + (c1) + x1


# arin = quadratic_fun(10,20,4)

# print(arin(5))   # 354
print(quadratic_fun(10,20,4)(45)(90,56))   # 444


var2 = 90

def N1():
    x = var2
    print("Nupur",x+10)


N1()


# Nested Lambda

harsh = lambda x,y : lambda x1,x2 : x+y+x1+x2


# print(harsh(10,20)(30,40))   # 100

mithil = harsh(10,20)

print(mithil(5,6))   # 41


# Lambda Examples


def square(num):
    return num ** 2


sq = lambda num : num ** 2
print(type(sq))   # <class 'function'>
print(sq(5))   # 25

list1 = [10,299,32,44,21,578,89]

# for i in list1:
#     print(sq(i))

arin1 = map(square, list1)

print(arin1)   # <map object at 0x00000212E6E37C70>
print(type(arin1))   # <class 'map'>

arin1 = list(map(square, list1))
arin1 = list(map(lambda num : num ** 2, list1))
print(arin1)   # [100, 89401, 1024, 1936, 441, 334084, 7921]
print(type(arin1))   # <class 'list'>