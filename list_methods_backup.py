list1 = []

print(type(list1))   # <class 'list'>

l2 = [10,20,90.89,True,'False',[(10,20,30), [10,20]], {10,20}, {"Name" : "Margi"}] # allow's Duplicates
print(l2)
print(id(l2))   # 2872641339264
print(len(l2))   # 8   # Length starts from 1, Index starts from 0


# List Characteristics:
# Ordered (Indexed), Allow's Duplicates, Mutable (Changeble)


# Indexing
print(l2[1])  # 20
print(l2[-7])  # 20
print(l2[-2])  # {10,20}
print(type(l2[-2]))  # <class 'set'>


l2 = [10,20,{'Name' : 'Margi', 'address' : {'state' : "Guj", 'city' : 'Ahm', 'pincode' : [10,20,30,(55,43),33]}}]
print(l2[-1]['address'])  # {'state': 'Guj', 'city': 'Ahm', 'pincode': [10, 20, 30, (55, 43), 33]}
print(l2[-1]['address']['pincode'])  # [10, 20, 30, (55, 43), 33]
print(l2[-1]['address']['pincode'][3])  # (55, 43)
print(l2[-1]['address']['pincode'][-2])  # (55, 43)
print(l2[-1]['address']['pincode'][-2][0])  # 55


l3 = [10,20,30,40,50,60,60,70,80,90]

# print(l3[start : end (n-1) : step (n-1)])
print(l3[0 : 6])  # [10,20,30,40,50,60]
print(l3[3 : 4])  # [40]
print(type(l3[3 : 4]))  # <class 'list'>
print(l3[5 : 2])  # []
print(l3[5 : 2 : -1])  # [60, 50, 40]
print(l3[ :  : 1])  # [10, 20, 30, 40, 50, 60, 60, 70, 80, 90]
print(l3[ :  : 2])  # [10, 30, 50, 60, 80]
print(l3[-10 : -5 : ])  # [10, 20, 30, 40, 50]
print(l3[-10 : -5 : -2])  # []
print(l3[-3 :  : ])  # [70, 80, 90]
print(l3[-3 :  : -1])  # [70, 60, 60, 50, 40, 30, 20, 10]
print(l3[-3 : 4 : 2])  # []
print(l3[::-1])  # [90, 80, 70, 60, 60, 50, 40, 30, 20, 10]

# List Methods


l3.append(5000)
# l3.append("Margi")
# print(l3)   # [10, 20, 30, 40, 50, 60, 60, 70, 80, 90, 5000, 'Margi']

# # l3.extend(500)   # TypeError: 'int' object is not iterable

# l3.extend("Ashok")
# print(l3)  # [10, 20, 30, 40, 50, 60, 60, 70, 80, 90, 5000, 'Margi', 'A', 's', 'h', 'o', 'k']


l4 = [10,20,30]

l3.append(l4)
print(l3)   # [10, 20, 30, 40, 50, 60, 60, 70, 80, 90, 5000, [10, 20, 30]]  # len = 12
 
# l3.extend(l4)
# print(l3)  # [10, 20, 30, 40, 50, 60, 60, 70, 80, 90, 5000, 10, 20, 30]  # len = 14


l3.insert(2,45)
print(l3)   # [10, 20, 45, 30, 40, 50, 60, 60, 70, 80, 90, 5000, [10, 20, 30]]

l3.insert(-1,8000)
print(l3)  #  [10, 20, 45, 30, 40, 50, 60, 60, 70, 80, 90, 5000, 8000, [10, 20, 30]]

l3.pop()
print(l3)   # [10, 20, 45, 30, 40, 50, 60, 60, 70, 80, 90, 5000, 8000]

x = l3.pop(2)
print(x)  # 45
print(l3)   # [10, 20, 30, 40, 50, 60, 60, 70, 80, 90, 5000, 8000]

l3.remove(5000)
print(l3)   # [10, 20, 30, 40, 50, 60, 60, 70, 80, 90, 8000]

del l3[5:]

print(l3)  # [10, 20, 30, 40, 50]

# l3.clear()
# print(l3)

l9 = l3.copy()  # xerox

l10 = l3   # Digilocker

l3.append(400) 
l10.append(401) 

print(l3,l9,l10)  # [10, 20, 30, 40, 50, 400, 401] [10, 20, 30, 40, 50] [10, 20, 30, 40, 50, 400, 401]


l3.reverse()

print(l3)  # [401, 400, 50, 40, 30, 20, 10]

l3.sort()

print(l3)   # [10, 20, 30, 40, 50, 400, 401]

l3.sort(reverse=True)

print(l3)   # [401, 400, 50, 40, 30, 20, 10]