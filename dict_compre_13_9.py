# dict1 = {"Name" : "Krutarth", 'Roll' : 900, 'Address' : "Ahmedabad"}

# print(dict1['Name'])   # Krutarth
# # print(dict1['city'])   # Error

# print(dict1.get('city'))   # None

from bidict import bidict

# dict2 = bidict(dict1)

# print(dict2)   # bidict({'Name': 'Krutarth', 'Roll': 900, 'Address': 'Ahmedabad'})
# print(type(dict2))   # <class 'bidict.bidict'>

# print(dict2['Roll'])  # 900

# dict3 = dict2.inverse

# print(dict3)   # bidict({'Krutarth': 'Name', 900: 'Roll', 'Ahmedabad': 'Address'})

# print(dict3['Krutarth'])  # Name
# print(dict3.keys())   # dict_keys(['Krutarth', 900, 'Ahmedabad'])


# for key,val in dict1.items():
#     if val == 900:
#        print(key)     # Roll


# new = []
# keys = []
# values = []

# for k in dict1.items():
#     new.append(k)
# for i,j in dict1.items():
#     new.append([i,j])
#     keys.append(i)
#     values.append(j)

# print(new)   # [('Name', 'Krutarth'), ('Roll', 900), ('Address', 'Ahmedabad')]
# print(new[0][1])
# print(keys)   # ['Name', 'Roll', 'Address']
# print(values)  # ['Krutarth', 900, 'Ahmedabad']

# for subtup in new:
#     if subtup[1] == 900:
#         print("Found")

# ----------------------------------------

dict1 = {'str1' : 900, 'str2' : 89 , 'str3' : 567}

# for i in dict1.values():
#     print(i)

val = [i for i in dict1.values()]
print(val)   # [900, 89, 567]

val.sort()  # [89,567, 900]
new = {}

from bidict import bidict
dict2 = bidict(dict1)
dict2 = dict2.inverse
print(dict2)

for i in val:   # [89, 567, 900]   #  i = 89
    for key, value in dict1.items():
        if i == value:   # 89 == 89
            # new[key] = i   # 
            new[key] = value   # 

print(new)


# -------------------------------------------------

dict3 = {}

list1 = [10,20,30,40,50,60,70]

# list1 = [(i,i**3) for i in list1]
# print(list1)   # [(10, 1000), (20, 8000), (30, 27000), (40, 64000), (50, 125000), (60, 216000), (70, 343000)]


# dict3 = {x : x*x for x in list1}
# print(dict3)   # {10: 100, 20: 400, 30: 900, 40: 1600, 50: 2500, 60: 3600, 70: 4900}

str1 = "Arin"

# {'A' : 'aaaaa', 'R' : 'rrrrr' ......}
str1 = "Arin"

dict3 = {x.upper() : x.lower()*5  for x in str1}
print(dict3)   # {'A': 'aaaaa', 'R': 'rrrrr', 'I': 'iiiii', 'N': 'nnnnn'}



str2 = 'Mithill'

# {'M' : 'l', 'i' : 'l', 't' : 'i', 'h' : 'h'}