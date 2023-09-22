# set ---> Unordered (UnIndexed), Don't Allow Duplicates, Unchangeble* (We can add or Remove Elements)

set1 = {}
print(type(set1))   # <class 'dict'>

set2 = {10}
print(type(set2))   # <class 'set'>

set1 = set()  # Constructor Name
print(type(set1))


s1 = {10,20,30, 90, 89, 10, 20, 90.89, "Str1", True, None, 1, (10,90)}
print(s1)   # {True, 90, 'Str1', 10, (10, 90), 20, 89, 90.89, 30, None}  # 1 == True in set
print(len(s1))   # 10
print(id(s1))



set11 = {10,20,30}  # Iterable Values
set2 = [90,89,67]

for j in set2:
    set11.add(j)
set11.add((10,20))
print(set11)   # {67, 10, (10, 20), 20, 89, 90, 30}


# set5.update(dict1)   # In Dict
# set5.update({10:30})

set5 = {90,45}
set6 = {99,66}
set3 = [101,201,(10.20,)]


set5.update(set3)   # list
set5.update(set6)   # set
print(set5)   # {66, 99, 101, 201, 45, (10.2,), 90}


# Remove Elements

# del set5   # delete the set

# set5.clear()   # blank set
print(set5)   # {66, 99, 101, 201, 45, (10.2,), 90}


set5.remove(90)  
print(set5)   # {66, 99, 101, 201, 45, (10.2,)}

# set5.remove(34)
# print(set5)

set5.discard(90)   # If ele. is not found then it will not generate an Error


x = set5.pop()  
print(x)   # 66
x = set5.pop()  
print(x)   # 99

print(set5)   # {101, 201, 45, (10.2,)}


# Loop

for k in set5:
    print(k,end='\n')

set3 = {10,90,20}
set4 = {88,55,20,30}

# print(set3.difference(set4))   # {10, 90}
# print(set4.difference(set3))   # {88, 30, 55}


# set3.difference_update(set4)
# print(set3)   # {10,90}


# print(set3.symmetric_difference(set4))   # {10, 55, 88, 90, 30}

# print(set3.intersection(set4))  # {20}
print(set3.union(set4))   # {20, 90, 55, 88, 10, 30}
print(set3)   # {10, 20, 90}

# set4 = set3.copy()


set3 = {10,90,20}
set4 = {88,55,30,10,90,20}

print(set3.isdisjoint(set4))     # False
print(set3.issubset(set4))       # True
print(set3.issuperset(set4))     # False
print(set4.issuperset(set3))     # True

set1 = {10,203,50}
set2 = {10}

print(set1 - set2)   # {50, 203}