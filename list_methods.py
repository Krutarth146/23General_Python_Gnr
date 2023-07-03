list1 = ['Mithil', 'Geeks', 4, "geeks"]

print(list1[::-3])  # ['geeks', 'Mithil']
print(list1[:1:-2])  # ['geeks']
print(list1[:0:])  # []
print(list1[1:1:1])  # []



# List Methods

list1 = [10,20,30,40,50]

list1.append("Mithil")
list1.append(9000)
print(list1)  # [10, 20, 30, 40, 50, 'Mithil', 9000]


# list1.extend(900)  #  'int' object is not iterable
list1.extend('900')  #  
print(list1)  # [10, 20, 30, 40, 50, 'Mithil', 9000, '9', '0', '0']


l2 = [10,90,89,78]

list1.append(l2)
print(list1)  # [10, 20, 30, 40, 50, 'Mithil', 9000, '9', '0', '0', [10, 90, 89, 78]]

# list1.extend(l2)
# print(list1)  # [10, 20, 30, 40, 50, 'Mithil', 9000, '9', '0', '0', 10, 90, 89, 78]

# list1.extend("Mithil")
# print(list1)  # [10, 20, 30, 40, 50, 'Mithil', 9000, '9', '0', '0', [10, 90, 89, 78], 'M', 'i', 't', 'h', 'i', 'l']
list1.extend(["Mithil"])
list1.extend([990])
print(list1)  # [10, 20, 30, 40, 50, 'Mithil', 9000, '9', '0', '0', [10, 90, 89, 78], 'Mithil', 990]


del list1[5:]

print(list1)  # [10, 20, 30, 40, 50]


list1.insert(2,7000)
print(list1)   # [10, 20, 7000, 30, 40, 50]


list1.insert(-1,3000)
print(list1)   # [10, 20, 7000, 30, 40, 3000, 50]

list1[2] = 7800

print(list1)   # [10, 20, 7800, 30, 40, 3000, 50]   # Replace Value


x = list1.pop()
print(x)
print(list1)   # [10, 20, 7800, 30, 40, 3000]


list1.pop(-3)
print(list1)  # [10, 20, 7800, 40, 3000]

l1 = [10,20,30,40,20,20,90]
# list1.remove(20)
# print(list1)   # [10, 7800, 40, 3000]

# for i in l1:
#     if i == 20:
#         l1.remove(i)

# print(l1)


l2=  []

for i in l1:
    if i not in l2 and i != 20:
        l2.append(i)

print(l2)  # [10, 20, 30, 40, 90]


l1.sort() # Asc
# l1.sort(reverse=True)  # Decreasing

print(l1)   # [10, 20, 20, 20, 30, 40, 90]

l1.reverse()
print(l1)

# l1.clear()


l2 = l1.copy()   # Xerox
# print(l2)

l3 = l1   # Deep Copy  ----> Digilocker


l1.append(900)
print(l1)   # [90, 40, 30, 20, 20, 20, 10, 900]
print(l2)   # [90, 40, 30, 20, 20, 20, 10]
print(l3)   # [90, 40, 30, 20, 20, 20, 10, 900]

l3.append(3000)
print(l1)   # [90, 40, 30, 20, 20, 20, 10, 900, 3000]

print(l1.count(20))   # 3  # Occurance


l2 = [10,20,10,10,10,20]
print(l2.index(20,3))  # 5


# List Methods End ---------------------------