# dict1 = {"Name" : "Manoj", 'Car' : 'Alto', 'Price' : 800}

# x = dict1.setdefault('Price', 800)
# x = dict1.setdefault('Price', 900)
# # x = dict1.setdefault('color', "Violet")
# print(x)

# print(dict1)

# dict1['Gender'] = "Male"

# dict1.update({'Gender1' : "Male1"})
# print(dict1)   # {'Name': 'Manoj', 'Car': 'Alto', 'Price': 900, 'color': 'Violet', 'Gender': 'Male', 'Gender1': 'Male1'}

# dict1['color'] = 'Red'
# print(dict1)

# dict1['Price'] = 7777

# print(dict1)


# print(dict1.popitem())
# print(dict1)


# for k in dict1.values():
#     print(k)

# # ---------------------------------------------------------------

# # 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# # Sample Dictionary ( n = 5) :
# # Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
 
# dict1 = {}
# n = 5

# for i in range(1,n+1):
#     dict1[i]  = i**2


# # dict1 = {1 : 1, 2 : 4 ......}


# # 4. Write a Python script to check whether a given key already exists in a dictionary.


# dict2 = {'Name': 'Manoj', 'Car': 'Alto', 'Price': 900, 'color': 'Violet', 'Gender': 'Male', 'Gender1': 'Male1'}

# key1 = input()


# if key1 in dict2:
#     print("Available")




# dict2 = {'list1' : [10,20,99,3,1,89], 'Mist2' : [64,32,21,90], 'Zist3' : [90,12,33,78,44]}


# for list1Name, val in dict2.items():
#     val.sort()
#     dict2[list1Name] = val

# print(dict2)




# Input : test_dict = {‘Gfg’ : 3, ‘is’ : 7, ‘best’ : 10, ‘for’ : 6, ‘geeks’ : ‘CS’}, K = 1 
# Output : {‘geeks’ : ‘CS’} 
# Explanation : Only Mixed value is retained.


# Python - Remove keys with Values Greater than K ( Including mixed values )
# Input : test_dict = {'Gfg' : 3, ‘is’ : 7, ‘best’ : 10, ‘for’ : 6, ‘geeks’ : ‘CS’}, K = 7 
# Output : {‘Gfg’ : 3, ‘for’ : 6, ‘geeks’ : ‘CS’} 
# Explanation : All values greater than K are removed. Mixed value is retained. 


test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10, 'for' : 6, 'geeks' : "CS" }
K = 7 

new_dict = {}

for key,val in test_dict.items():
    # print(i,j)
    if type(val) == int and val < K:
        new_dict.update({key : val})
    elif type(val) == str:
        new_dict[key] = val

print(new_dict)   # {'Gfg': 3, 'for': 6, 'geeks': 'CS'}



# num_freq = [[10,5], [5, 4], [3,2], [11,1]]


# for i in range(len(num_freq)) :   # 4  ---> 0 to 3   # i = 0
        
#             val = num_freq[i][1]
#             if val % 2 == 0 :
#                 no_of_painrs = no_of_painrs + 1



# # 10 --> Counter

# dict1 = {}


# if ele not in dict1:
#     dict1[ele] = 1
# else:
#      dict1[ele] += 1

dict1 =  {10 : 5, 20 : 4}

for i in dict1:
    print(dict1[i])


for k,v in dict1.items():
    print(v)

# ----------------------------------------------------------

dict2 = {'Name' : "Krutarth", 'gender' : "Male", 'School' : "HBK"}

keys_list = [i for i in dict2.keys()]
print(keys_list)
print(type(keys_list))


keys_list.sort()

print(keys_list,' ----')   # ['Name', 'School', 'gender']  ----

new_dict = {}

for i in keys_list:
    new_dict.update({i:dict2[i]})

print(new_dict)


for j in sorted(dict2.items()):
    print(j)

from collections import OrderedDict

dict2 = OrderedDict(dict2)
print(dict2)

x,y,z = [10,20,90]

print(x,y)


# Anagram

s = "state"
t = "taste"

dict1  = {}
dict2 = {}

for i in set(s):
    dict1[i] = s.count(i)

print(dict1)   # {'a': 1, 't': 2, 's': 1, 'e': 1}