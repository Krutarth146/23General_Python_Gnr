# num = 16

# for j in range(1,16):
#     if num % j == 0:
#         print(f"{j} * {num//j} = {num}")

# 2
# 22
# 222
# 2222
# 22222

# num = 3, step = 2

# 3 + 33 = 36




# List ----> Ordered (Indexed), Allow's Duplicates
list1 = [10,20, 10, True, 1, [(10,203), {10,20}], {'Name' : 'Krutarth', 'roll' : [10,20,30]}]
print(list1)
print(type(list1))
print(id(list1))   # 1859765133568


print(len(list1))   # 7   (Len starts from 1, Index starts from 0)
tup1 = ()
print(type(tup1))   # tuple
tup1 = (10)
print(type(tup1))   # int
tup1 = (10,)
print(type(tup1))  # tuple


list1 = [10,20,90,89]
print(min(list1))   # 10
print(max(list1))   # 90
print(sum(list1) / len(list1))   # 52.25


print(list(reversed(list1))) #  [89, 90, 20, 10]


# print(list1.reverse())   # None
print(list1)   # [89, 90, 20, 10]

list1.sort()
# list1.reverse()
print(list1)   # [90, 89, 20, 10]


list1.sort(reverse=True)
print(list1)   # [90, 89, 20, 10]


list1 = [10,20, 10, True, 1, [(10,203), {10,20}], {'Name' : 'Krutarth', 'roll' : [10,20,30]}]

# Indexing
print(list1[-1])   # {'Name': 'Krutarth', 'roll': [10, 20, 30]}
print(list1[-1]["roll"])   # [10, 20, 30]
print(list1[-1]["roll"][-1])   # 30
print(list1[-1]["roll"][2])   # 30


x1, x2, x3 = [10,20,30]

print(x2 + x3)   # 50


# Slicing
list1 = [10,20, 10, True, 1, [(10,203), {10,20}], {'Name' : 'Krutarth', 'roll' : [10,20,30]}]

# print(tup1[])
print(list1[-1:])   # [{'Name' : 'Krutarth', 'roll' : [10,20,30]}]
print(type(list1[-1:]))   # <class 'list'>
print(type(list1[-1]))   # <class 'dict'>
print(type(list1[-2]))   # <class 'list'>
print(type(list1[-2:]))   # <class 'list'>
print(list1[-2:])   # [[(10, 203), {10, 20}], {'Name': 'Krutarth', 'roll': [10, 20, 30]}]
print(list1[2:3])   # [10]
print(list1[2:2:1])   # []
# print(list1[start:End])   # [10]
# print(list1[start:End:step])   # [10]

list1 = [90,23,4566,6,77,53]
print(list1[3:-2])   # [6]
print(list1[3:-2:-1])   # []