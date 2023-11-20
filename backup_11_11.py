# # List is a collection which is ordered and changeable. Allows duplicate members.
# # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# # Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# # Dictionary is a collection which is ordered** (No Indexing) and changeable. No duplicate members.


# # Dict

# dict1 = {"name" : "Krutarth", 90 : 78, "name" : "Vaibhav", 'address' : [{'City' : ['Ahm', {'Area' : {'Shahpur' : {'Pcode' : 2, 'lmark' : 'Cama'}}}, 'Gnr']}]}

# print(dict1)

# print(dict1["name"])  # Vaibhav
# print(dict1[90])  # 78

# dict1["name"] = "Manoj"

# print(dict1)  # {'name': 'Manoj', 90: 78, 'address': [{'City': ['Ahm', {'Area': {'Shahpur': {'Pcode': 2, 'lmark': 'Cama'}}}, 'Gnr']}]}

# print()

# dict1["Roll"] = 90
# print(dict1)

# dict1.update({'Age' : 90})
# print(dict1)


# print(dict1.get('Age11'))   # None
# # print(dict1['Age11'])   # Error

# print(dict1['name'])   # Manoj
# # print(dict1["Manoj"])

# for i in dict1.keys():
#     print(i)

# for i in dict1.values():
#     print(i)

# for i in dict1.items():
#     print(i)

# for key,val  in dict1.items():
#     print(key,'----->',val)
#     if val == 90:
#         print(key)


# from bidict import bidict


# dict2 = {"name" : "Krutarth", 90 : 78, "name" : "Vaibhav", 'address' : "Shahpur"}
# d2 = bidict(dict2)

# print(d2)   # bidict({'name': 'Vaibhav', 90: 78, 'address': 'Shahpur'})

# d3 = d2.inverse
# print(d3)  # bidict({'Vaibhav': 'name', 78: 90, 'Shahpur': 'address'})


# print(d3['Vaibhav'])   # name


# dict2.setdefault('age', 89)
# dict2.setdefault('name', "Dp Pujara")

# print(dict2)   # {'name': 'Vaibhav', 90: 78, 'address': 'Shahpur', 'age': 89}


# list1 = [10,20,30]
# d9 = dict.fromkeys(list1,0)
# print(d9)    # {10: 0, 20: 0, 30: 0}


# e1 = dict2.pop('address')

# print(dict2, e1)   # {'name': 'Vaibhav', 90: 78, 'age': 89} Shahpur


# e2 = dict2.popitem()
# print(e2, dict2)   # ('age', 89) {'name': 'Vaibhav', 90: 78}


# str1 = "MISSISSIPPI"

# ans = {'M' : 1, "I" : 4, 'S' : 4, "P" : 2}


# res = {}

# for ele in set(str1):
#     ans[ele] = str1.count(ele)
#     # if ele not in res:
#     #     res[ele] = 1
#     # else:
#     #     res[ele] += 1

# # print(res)
# print(ans)   # {'M': 1, 'I': 4, 'S': 4, 'P': 2}


# list1 = [10,90,34,23,78,10,20,10,10]

# new = []

# # for k in list1:
# #     if k not in new:
# #         new.append(k)

# # print(new)   # [10, 90, 34, 23, 78, 20]


# for k in list1:
#     if list1.count(k) == 1:
#         new.append(k)

# print(new)   # [90, 34, 23, 78, 20]


# # list1 = [10,120,30,10,20,30,10]
# list1 = [10,120,30,10,10,20,30,40]


# # for j in list1:
# #     if j == 10:
# #         list1.remove(j)

# # print(list1)   # [120, 30, 10, 20, 30, 40]


# import json # (Javascript Object Notation)

# fp = open("record.txt","r")

# x = fp.read()

# dict1 = json.loads(x)


# fp.close()
# # dict1 = {'1001' : {'pName' : 'Parleg', 'price' : 900, 'qn' : 67},
# #          '1002' : {'pName' : 'Oats', 'price' : 600, 'qn' : 32},
# #          '1003' : {'pName' : 'kellogs', 'price' : 67, 'qn' : 7},
# #          '1004' : {'pName' : 'Perks', 'price' : 20, 'qn' : 700}
# #         }

# print(dict1)
# print(len(dict1))   # 4

# user_need = input("Enter Product Number: ")
# quantity = int(input("Enter quantity: "))


# if quantity <= dict1[user_need]['qn']:
#     print("Your total Bill Amount is",quantity * dict1[user_need]['price'])
#     dict1[user_need]['qn'] -= quantity
#     print('Record Updated')
# else:
#     print(f"We have only {dict1[user_need]['qn']} Quantity...")   # fstring
#     choice = input("Pls Prees Y for Acceptance or Press any Other Key")

#     if choice.lower() == 'y':
#         print("Your total Bill Amount is",dict1[user_need]['qn'] * dict1[user_need]['price'])
#         dict1[user_need]['qn'] = 0
#         print("Record Updated")

#     else:
#         print("Thanks")



# fp = open("record.txt","w")

# dict1 = json.dumps(dict1)

# fp.write(dict1)

# fp.close()  


# # ----------------------------------


# Functions

# Inbuilt
print(len([10,20,30]))  # 3

print(len("Amana"))   # 5

# UDF
# x = 89   # Global Varibale

# def Vaibhav(n1,n2 = 0):   # Default Function
#     # n3 = "jk"
#     # print(n1 + n2 + n3)
#     # return n1, n2, n3
#     global x
#     b = n1 + x   # 10 + 89

#     print(b)

#     x = x + 10
#     return x   # 99

# # Vaibhav("Vaibhav ", 2)   # Vaibhav Vaibhav
# # print(Vaibhav("Amna")[:4])   # Amna Ashokjk

# y, n2 = 40,50
# print(Vaibhav(n2, y))  # 139
# print(x)   # 99


# def Series(num):
#     list1 = []
#     for i in range(num):
#         list1.append(i)

#     return list1


# print(Series(10))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generator
def Series(num):
    for i in range(num):
        yield i


print(Series(10))   # <generator object Series at 0x0000021C6B499A10>

x = Series(10)

# print(x.__next__())   # 0
# print(x.__next__())   # 1
# print(x.__next__())   # 2


for j in Series(10):
    print(j)



def Vaibhav(m1):
    def kru(x2):
        print("Kru Function")
        x2()
    print("Vaibhav Function")
    return kru(m1)

@Vaibhav   # Custom Decorator
def royal():
    print("This is Royal FUnction")


# Vaibhav(royal)   # Kru Function


# OOP
# @classmethod
# @staticmethod
# @abstractmethod



def Square(num):
    return num ** 2


print(Square(52))   # 2704


# lambda  (Anounomous Function)

x = lambda num : num ** 2

print(x(23))   # 529


max_num = lambda n1, n2, n3 = 0  : n1 if n1 > n2 else n2

print(max_num(10,20))   # 20



# Quadratic FUnction


def Quadratic_Fun(a,b,c):
    return lambda x : (a * x ** 2) + (b*x) + c

fun = Quadratic_Fun(10,20,30)

print(fun(5))   # 380

# Nested lambda

val = lambda x, y : lambda p, q = 4: x + y + p + q

# k = val(10,20)

# print(k(3,4))  # 37

print(val(10,20)(3))   # 37