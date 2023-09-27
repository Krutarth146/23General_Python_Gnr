list1 = [10,90,20,30,40,50]

print(list1[4])   # 40
# print(list1[start : end (n-1) : step (n-1)])   # 40
print(list1[1:5:1])   # [90, 20, 30, 40]
print(list1[1:5:2])   # [90, 30]
print(list1[1:5:-1])   # []
print(list1[5:1:-1])   # [50, 40, 30, 20]
print(list1[5:1:1])   # []
print(list1[5::1])   # [50]
print(type(list1[5::1]))   # <class 'list'>
print(type(list1[5]))   # <class 'int'>
print(list1[-3::])   # [30, 40, 50]
print(list1[-3:])   # [30, 40, 50]
print(list1[:-3:])   # [10, 90, 20]
print(list1[-3:5:1])   # [30, 40]
print(list1[-5:2:-1])   # []
print(list1[-3:2:1])   # []

# for j in range(-5,2,-1):
    # print(j,end=' ')

for j in range(-3,2,1):
    print(j,end=' ')     # -3 -2 -1 0 1

list1 = [10,90,20,30,40,50]

print(list1[3:-2:-1])   # []

# List Methods   ---> Mutable (Changeble)

list2 = [90,89,78]

list1+=list2

print(list1)   # [10, 90, 20, 30, 40, 50, 90, 89, 78]

list1.append(900)
list1.append("Mnaoj")
list1.append(True)
list1.append([10,20,30])
list1.append(list2)

print(list1)   # [10, 90, 20, 30, 40, 50, 90, 89, 78, 900, 'Mnaoj', True, [10, 20, 30], [90, 89, 78]]
print(len(list1))   # 14

list1.extend('34')
print(list1)  # [10, 90, 20, 30, 40, 50, 90, 89, 78, 900, 'Mnaoj', True, [10, 20, 30], [90, 89, 78], '3', '4']

list1.extend('Arin')
print(list1)  # [10, 90, 20, 30, 40, 50, 90, 89, 78, 900, 'Mnaoj', True, [10, 20, 30], [90, 89, 78], '3', '4']

list1.extend(["Bansi"])
print(list1)  # [10, 90, 20, 30, 40, 50, 90, 89, 78, 900, 'Mnaoj', True, [10, 20, 30], [90, 89, 78], '3', '4', 'A', 'r', 'i', 'n', 'Bansi']

list1.extend([["Bansi"]])
print(list1)  # [10, 90, 20, 30, 40, 50, 90, 89, 78, 900, 'Mnaoj', True, [10, 20, 30], [90, 89, 78], '3', '4', 'A', 'r', 'i', 'n', 'Bansi', ['Bansi']]


list4 = [40, 200]
list5 = [10,90]

# list4.append(list5)
# print(list4)   # [40, 200, [10, 90]]   # len = 3

# list4.extend(list5)
# print(list4)   # [40, 200, 10, 90]   # len = 4

list4 = [40, 200, 900, 400, 100, 800]
list4.insert(2, 1600)
list4.insert(-1, 1200)
list4.insert(8, 1100)
list4.insert(12, 1300)
print(list4)   # [40, 200, 1600, 900, 400, 100, 1200, 800, 1100, 1300]


list4 += [90]
print(list4)   # [40, 200, 1600, 900, 400, 100, 1200, 800, 1100, 1300, 90]

# ----------------------------------------------

# Remove

# list1.clear()


# del list1
del list1[4:]

print(list1)   # [10, 90, 20, 30]


x = list1.pop() 
print(x)   # 30
print(list1)  # [10, 90, 20]
x = list1.pop(1)
print(list1)    # [10,20]


list1.remove(10)
print(list1)   # [20]


list1 = [10,10,90,40, 10,50]
print(list1.count(10))   # 3
print(list1.count(80))   # 0
print(list1.index(10,2))   # 2


print(list1)   # [10, 10, 90, 40, 10, 50]

# Method = 1

print(sorted(list(set(list1))))  # [10, 40, 50, 90]
print(list(reversed(list(set(list1)))))   # [90, 50, 10, 40]


# Method = 2

for k in list1:
    print(k)

for k in list1[::-1]:
    print(k)

# for j in range(6):  # 0 to 5

# for j in range(len(list1)):
#     if list1[j] == 10:
#         list1.remove(10)
# print(list1[j])


# Method = 3

list6 = list1.copy()   # Shallow Copy
 

for j in range(len(list1)):
    if list1[j] == 10:
        list6.remove(10)
print(list6)


# Method = 4

counter = list1.count(10)
for j in range(counter-1):
    list1.remove(10)

print(list1)   # [90, 40, 50]


# Method = 5

new = []

for k in list1:
    if k not in new:
        new.append(k)


print(new)

