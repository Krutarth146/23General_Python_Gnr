set1 = {10,20,30,90}
print(set1)   # {10, 20, 90, 30} 


# Set ---> Unchangeble (We can add or Remove ELements)

# Frozen set

# frozenset(iterable)

list1 = [10,20,30,40]
list2 = [99, 30,40]
s2 = frozenset(list1)
s3 = frozenset(list2)

print(s2)   # frozenset({40, 10, 20, 30})
print(type(s2))   # <class 'frozenset'>


print(s2.intersection(s3))   # frozenset({40, 30})
print(s2.union(s3))   # frozenset({99, 20, 40, 10, 30})


dict1 = {'Name' : 'Mithil', 'Roll' : 900}

d1 = frozenset(dict1)
print(d1)   # frozenset({'Name', 'Roll'})


# d1.add(10)

# d1[0] = 'Manoj'   # 'frozenset' object does not support item assignment

s1 = set()

d1 = [90]
print(d1)

s1.add(10)
print(s1)  # {10}

# def Arin(n1):
#     return 10

# Using Fun Type - 4 with return Type and with Args

str1 =  "Apple is very useful to us."

# step - 1
ans = {'a' : 3, 'u' : 2}

# step - 2
# len(ans) == 5:
#     return True


def Problem(str1):
    pass