dict1 = {}

print(dict1)   # {}
print(type(dict1))   # <class 'dict'>

set2 = {10,20}
print(type(set2))   # <class 'set'>

set1 = set()
print(type(set1))   # <class 'set'>


dict1 = {'Name' : "Krutarth", 'Roll' : 900, 78 : 89.90, 'Name' : 'Mithil', "address" : {'City' : "Ahm", 'State' : 'Guj', 'Pincode' : [10,90,34,56,22]}}

print(dict1)   # {'Name': 'Mithil', 'Roll': 900, 78: 89.9, 'address': {'City': 'Ahm', 'State': 'Guj', 'Pincode': [10, 90, 34, 56, 22]}}

print(type(dict1))   # <class 'dict'>

print(len(dict1))   # 4

print(id(dict1))   # 2640828235840

# Destructuring

# print(dict1[0])  # Gives Error 

print(dict1["Name"])
print(dict1["Roll"])
# print(dict1["Royal"])   # Gives Error if key is not Present

print(dict1.get("Royal"))  # None    # Returns None if key is not Present
print(dict1.get("Roll"))   # 900


# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

dict1 = {'Name' : "Krutarth", 'Roll' : 900, 78 : 89.90, 'Name' : 'Mithil', "address" : {'City' : "Ahm", 'State' : 'Guj', 'Pincode' : [10,90,34,56,22]}}


dict1['Roll'] = 802

print(dict1)   # {'Name': 'Mithil', 'Roll': 802, 78: 89.9, 'address': {'City': 'Ahm', 'State': 'Guj', 'Pincode': [10, 90, 34, 56, 22]}}

dict1['Institute'] = 'Royal'

print(dict1)

dict1.update({"School" : "HBK", 'Manoj' : 'Tripathi'})

print(dict1)   

dict1 = {'Name': 'Mithil', 'Roll': 802, 78: 89.9, 'address': [{'City': 'Ahm', 'State': 'Guj', 'Pincode': {"standard" : [10, 90, 34, 56, 22]}}], 'Institute': 'Royal', 'School': 'HBK', 'Manoj': 'Tripathi'}

# print(dict1)   

print(dict1['address'])   # [{'City': 'Ahm', 'State': 'Guj', 'Pincode': {'standard': [10, 90, 34, 56, 22]}}]
print(dict1['address'][0])   # {'City': 'Ahm', 'State': 'Guj', 'Pincode': {'standard': [10, 90, 34, 56, 22]}}
print(dict1['address'][0]['Pincode'])   # {'standard': [10, 90, 34, 56, 22]}
print(dict1['address'][0]['Pincode']['standard'])   # [10, 90, 34, 56, 22]
print(dict1['address'][0]['Pincode']['standard'][-2])   # 56
print(type(dict1['address'][0]['Pincode']['standard'][-2]))   # <class 'int'>
print(type(dict1['address'][0]['Pincode']['standard']))   # <class 'list'>
