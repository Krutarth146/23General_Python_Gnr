# Python is Interpreted (Line by Line Code Interpretation), Dynamic

print('''
      Multi
      Line
      string
''')

print("V")

try:
  printa("scsdcsdc")
except:
  print("Error Occured")
  
print("Manoj")


# int x, y= 89;

# x = 90;

name = "Manoj"

print(type(name))   # <class 'str'>

name = 56

print(type(name))   # int


surname = "Patel"   # Assignment

# address += "Ahm"  # Error

# Datatypes : int, float, str, bool, Complex, Nonetype
# Collections: list, Tuple, Dict, Set

print("Hello Aman",end='\n')
print('Gm')
print()

x, y , z = '10','20','Aman'

print(x,y,z,sep=' ',end=' ------ ')
print("Vaibhav")   # 10 20 Aman ------ Vaibhav


# scanf()
x = 67
print(type(x))  # int


# y = input()
# print(type(y))  # <class 'str'>

# TypeCast   1. Implicit   2. Explicit

print(True + 67)   # bool + int   # 68  (Implicit)

print(int(float('34.88')))  # 34   # Explicit T.C

print(round(34.88))   # 35

import math

print(math.ceil(34.20))   # 35
print(math.ceil(34.00))   # 34
print(math.floor(34.99))   # 34
print(math.floor(34.00))   # 34


x = 90 + 7j
print(type(x))   # <class 'complex'>

k = None
print(type(k))   # <class 'NoneType'>


list1 = [20, 10, 56, True, [45, 'Str1', (), (10,), set(), {}, {10}, {'Name' : 'Manoj'}]]

print(list1)   # [20, 10, 56, True, [45, 'Str1', (), (10,), set(), {}, {10}, {'Name': 'Manoj'}]]


print(list1[-2])   # True
print(type(list1[-2]))    # <class 'bool'>

print(list1[-2:-1])  # [True]   # Slicing
print(type(list1[-2:-1]))  # <class 'list'>

print(list1[3:2])  # []

# ---------------------------------
# print(list1[start : end (n-1) : step(n-1)])

# Step - Positive (left to right)
# Step - Negative (RIght to left)

list1 = [20, 10, 56, True, [45, 'Str1', (), (10,), set(), {}, {10}, {'Name' : 'Manoj'}]]
print(list1[1:4:1])  # [10, 56, True]
print(list1[1:4:2])  # [10, True]
print(list1[-1:-3:2])  # []
print(list1[-1:-3:-2])  # [[45, 'Str1', (), (10,), set(), {}, {10}, {'Name': 'Manoj'}]]

print(list1[1:2:-1])  # []
print(list1[-1][6:-3:1])  # []


# Truthy Values: 10, [10,20], "Aamna", -90
# Falsy: [], '', False, 0


if "":
    print(True)
elif 45 > 90:
    print("Ashok")
else:
    if 'Mithil' > 'nupur':
        print(ord('M'))
    else: 
        print(chr(90))   # Z


n1, n2,n3 = 67, 78, 90


max = n1 if n1>n3 else n3 if n1 > n2 else n2 if n2>n3 else n3
print(max)   # 90


# Loops

j = 67

while j<=71:
    print(j)
    j = j + 1  # j+=1  # (Low Priority)


f = 90

while True:
    f-=1
    if f == 45:
        break
    print(f)


# -----------------------
f = 90
flag = 0

while not(flag):  # and  or  not  (logical)
    f-=1
    if f == 45:
        flag = 1
        continue
    print(f)

# ------------------------


print()


g = 67
k = 70
while g<=70:   # True
    while k >= 67:  # True
        if g > k:  # 
            break
        print(k)   # 70  69  68  67
        k-=1  # 66
    print(g)   # 67  68 69 70
    g+=1  # 71

else:
    print("Run")


# ---------------------------------------------


# For Loop

# for x in range(start, end, step):
for x in range(10):  # (End (n-1))
    print(x,end=' ')    # 0 to 9


print()

for s in range(34,29,-1):
    print(s)



list1 = [10,20,30,40,50,60,70,80]

print(list1[4:-2])  # Direction

for i in range(-2,4,2):  # start = -2, end = 4(3), step = 1 (n-1) 0
    print(i)  # -2 0 2

print()
for i in range(-10,-3):  # start = -2, end = 4(3), step = 1 (n-1) 0
    print(i)  # -2 0 2


# ---------------------------------------------------------

list1 = [10,20,30,40,50,60]

for k in list1[2:]:   # in - Membership Operator
    print(k)

for k in list1[-1::-1]:   # in - Membership Operator
    print(k)

# for d in range(6):
    # print(d)  # 0 to 5

print()
print()
print()
for d in range(len(list1)):
    print(list1[d])  

list4 = [[10,20], [50,60], [90,33], [44,56]]

flat_list1 = [10,20,50,60,90,33,44,56]

flat = []
# for sublist in list4:
#     # print(sublist)
#     for i in sublist:
#         flat.append(i)

# print(flat) 

# ----------------------------------


# for sublist in list4:
#     flat.extend(sublist)

# print(flat)


list1 = [10,20,30]   # Ordered (Indexed), Allow's Duplicates, Mutable (Changeble)

# list1.append(78)
list1.extend(str("Mithil"))
list1.extend([10,20,[10,20]])
print(list1)


list4 = [[10,20], [50,], [9,33], [44,564]]

ans = []
# [10,20]

for sublist in list4:  # [10,20]
    flag = False
    for x in sublist:  # 10
        if len(str(x)) != 2:
            flag = True
            break
    if flag == False:
        # print(sublist)
        ans.append(sublist)

print(ans)

# List Comprehension

list1 = [45,90,23,78]
res = []

for k in list1:
    # print(k**2) # k*k (Power)
    res.append(k*k)

 
print(res)   # [2025, 8100, 529, 6084]

res1 = [k*k for k in list1]
res1 = [k**3 for k in list1]
print(res1)


# 10 to 100
# [(10, 100, 1000), (20,400,8000)]
res1 = [(k,k**2,k**3) for k in range(1,101) if k % 10 == 0]
print(res1)


# ------------------------------------------------------

list1 = [10,89,45,34,23]

list1.insert(1,3400)
print(list1)   # [10, 3400, 89, 45, 34, 23]

list1[1] = 900

print(list1)   # [10, 900, 89, 45, 34, 23]

list1.insert(-1,7899)
print(list1)   # [10, 900, 89, 45, 34, 7899, 23]


list1.insert(7,7899)
print(list1)   # [10, 900, 89, 45, 34, 7899, 23, 7899]

# += 
# append
# insert
# extend


ele = list1.pop()
print(list1,ele)


ele = list1.pop(2)
print(list1,ele)


list1.remove(7899)
print(list1)


# ------

list3 = list1.copy()   # Xerox  (Shallow Copy)
list4 = list1  # Deep Copy   # Digilocker
list5 = list(list1)  # Xerox (Shallow Copy)


list1.append(89)
list4.append(45)


print(id(list1))
print(id(list4))
print(id(list3))
print(list3)   # [10, 900, 45, 34, 23]
print(list4)   # [10, 900, 45, 34, 23, 89, 45]
print(list5)   # [10, 900, 45, 34, 23]
print(list1)   # [10, 900, 45, 34, 23, 89, 45]


list1.append(10)
list1.append(10)
print(list1.count(10))  # 3

list1.reverse()
print(list1)
print(list1[::-1])   # [10, 900, 45, 34, 23, 89, 45, 10, 10]


str1 = "Hello Aman Gupta"
print(str1.count('a',9,12))   # 0


# list1.sort()

list3 = ["aman", "Manish", 'Vaibhav', 'Royallllll']
# list3.sort(reverse = False, key = lambda x:len(str(x)))
list3.sort()
print(list3)   # ['Aman', 'Royal', 'Manish', 'Vaibhav']

# del list1
del list1[3:]
print(list1)   # [10, 10, 45]

print(all(list1))   # True
print(any(list1))   # True

print(min(list1))   # 10
print(sum(list1))   # 65
print(sum(list1) / len(list1))   # 21.666666666666668
# print(max(list3))


# _____________-------------------------------------


# Tuple : Immutable (Not Changeble), Ordered, Allow's Duplicates


tup1 = ()
print(type(tup1))   # tuple

tup1 = (10)
print(type(tup1))   # int

tup1 = (10,)
print(type(tup1))   # tuple

print(tup1.index(10))   # 0


tup2 = (10,90)


print(id(tup1))
tup1 += tup2 
print(tup1)   # (10, 10, 90)
print(id(tup1))


# del tup1

tup1 = list(tup1)
tup1.append(906)
print(tuple(tup1))   # (10, 10, 90, 906)

print(type(tup1))  # list

tup1 = ((10,20), (45,32), (21,88), (11,22))
tup1 = list(tup1)
for subtup_ind in range(len(tup1)-1):   # 3 ---> 0,1,2
    for j in range(subtup_ind+1, len(tup1)):  # 3
        if tup1[subtup_ind][1] > tup1[j][1]:   # tup1[2][1] > tup1[3][1]   # 88 > 22
            print(subtup_ind, j)
            tup1[subtup_ind], tup1[j] = tup1[j], tup1[subtup_ind]

print(tup1)   # [(10, 20), (11, 22), (45, 32), (21, 88)]

# Tuple Comprehension


tup1.sort(key=lambda x:x[1])   # x = (10,20) : 20
print(tup1)