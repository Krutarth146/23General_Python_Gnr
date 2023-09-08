dict1 = {'Name' : "Mithil", 'Roll' : 900, 'Address' : [10,20,30,405,0]}

print(dict1)

print(dict1.get('Name'))   # Mithil

print(dict1['Name'])   # Mithil

dict1.update({'School' : "Royal"})
print(dict1)

# dict1.clear()
# print(dict1)   # {}
 
# del dict1 
# del dict1['Roll']
# print(dict1)   # {'Name': 'Mithil', 'Address': [10, 20, 30, 405, 0], 'School': 'Royal'}

# print(id(dict1))

# dict1 = {'School' : 'Girnar'}

# print(id(dict1))
# print(dict1)

# x = 90
# x = 80


# -------------------------------------------------------

dict2 = dict1.copy()    # Shallow Copy   # Xerox

print(dict2)


dict3 = dict1   # Deep Copy  # Digilocker


x = 90

dict4 = dict(dict1)   # Shallow Copy

dict1["Bansi"] = "Kadiya"

print(dict3)   # {'Name': 'Mithil', 'Roll': 900, 'Address': [10, 20, 30, 405, 0], 'School': 'Royal', 'Bansi': 'Kadiya'}


print(dict2)


print(dict4)   # {'Name': 'Mithil', 'Roll': 900, 'Address': [10, 20, 30, 405, 0], 'School': 'Royal'}


dict1.pop('Name')
print(dict1)   # {'Roll': 900, 'Address': [10, 20, 30, 405, 0], 'School': 'Royal', 'Bansi': 'Kadiya'}


x = ('Name', 'roll', 'school')
y = 0
dict6 = dict.fromkeys(x,y)

print(dict6)  # {'Name': 0, 'roll': 0, 'school': 0}

# dict1 = {'Name': 'Mithil', 'Roll': 802, 78: 89.9, 'address': {'City': 'Ahm', 'State': 'Guj', 'Pincode': {"standard" : [10, 90, 34, 56, 22]}}, 'Institute': 'Royal', 'School': 'HBK', 'Manoj': 'Tripathi'}

# print(dict1.keys())   # dict_keys(['Name', 'Roll', 78, 'address', 'Institute', 'School', 'Manoj'])
# print(dict1.values())   # dict_values(['Mithil', 802, 89.9, {'City': 'Ahm', 'State': 'Guj', 'Pincode': {'standard': [10, 90, 34, 56, 22]}}, 'Royal', 'HBK', 'Tripathi'])
# print(dict1['address'].keys())   # dict_keys(['City', 'State', 'Pincode'])
# print(dict1['address'].values())   # dict_values(['Ahm', 'Guj', {'standard': [10, 90, 34, 56, 22]}])


# print(dict1.items())   # dict_items([('Name', 'Mithil'), ('Roll', 802), (78, 89.9), ('address', {'City': 'Ahm', 'State': 'Guj', 'Pincode': {'standard': [10, 90, 34, 56, 22]}}), ('Institute', 'Royal'), ('School', 'HBK'), ('Manoj', 'Tripathi')])


# for i in dict1:   # Default Keys
#     print(i, dict1[i])   # dict1['Roll']


# for h in dict1.values():
#     print(h)

# for h in dict1.items():
#     print(h,end=' ')   # ('Name', 'Mithil') ('Roll', 802) (78, 89.9) ('address', {'City': 'Ahm', 'State': 'Guj', 'Pincode': {'standard': [10, 90, 34, 56, 22]}}) ('Institute', 'Royal') ('School', 'HBK') ('Manoj', 'Tripathi')


# for key, val in dict1.items():
#     print(key,'----> ', val)
#     if key == 'Name':
#         dict1[key] = 'SB Sir'

# print(dict1)


# str1 = "MISSISSIPPI"

# # dict1 = {'M' : 1, 'I' : 4, 'P' : 2, 'S' : 4}

# dict2 = {}

# # for ch in str1:
# #     if ch not in dict2:
# #         dict2[ch] = 1
# #     else:
# #         dict2[ch] += 1   # dict2[i] = dict2[i] + 1


# # # {'M' :  1, 'I' : 1, 'S' : 2}

# # print(dict2['M'])


# set1 = set(str1)
# print(set1)   # {'P', 'M', 'S', 'I'}


# dict2 = {}

# for i in set1:
#     count = 0
#     for j in str1:
#         if i == j:
#             count+=1

#     dict2.update({i : count})


# print(dict2)