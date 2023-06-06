# print("Hello", file = open("first.txt", 'wt'))

# print("Hello",flush=True)

# scanf("%d",&num1);

# num1 = input("num1: ")   # Str
# num2 = input("Enter Second No: ")   # str

# print(num1 + num2)  # str + str (Concat) 5030

# Typecasting ---> One datatype to another Datatype

# (int) a in C

# Datatypes

x = -90333333333333333333333333
print(x)  # -90333333333333333333333333
print(type(x))  # <class 'int'>

_ = 89.78
print(type(_))  # <class 'float'>

o = 'k'
print(type(o))  # <class 'str'>

f = "str12232sdcsdcsdc"
print(type(f))  # <class 'str'>

g = '34'
print(type(g))  # <class 'str'>

f = True
print(type(f))  # <class 'bool'>

x = 90 + 8j     # 90 is Real part, 8j is Imaginary Part
print(type(x))  # <class 'complex'>

k = 8  # int
print(x+k)   # complex + int  # 98 + 8j

e = None
print(type(e))  # <class 'NoneType'>


# Collections
l1 = []
l1 = [10,20,30,90.89,True,'dcs',[(10,20,30)], {456, 90}, {'Name' : "Jainil", 'address' : {'Area' : "Sarghasan", 'City' : 'Gnr'}} ]
print(l1)
print(type(l1))  # <class 'list'>

jw = ()
print(type(jw))  # <class 'tuple'>

jw = (10)
print(type(jw))  # <class 'int'>

jw = (10,90,((20,30),[10,20]))
print(type(jw))  # <class 'tuple'>

s1 = {}
print(type(s1))  # <class 'dict'>
s3 = {"Name" : "Amaan", 'roll' : [10,20,30,40]}
print(type(s3))  # <class 'dict'>

dict =set()
print(type(dict))  # <class 'set'>

s8 = {10, 20,30, 30, 30, (10,20,), 90, 89, 78}   # Don't Alllow Duplicates, Unordered
print(s8)  # {20, 90, 30, 89, 10, 78, (10, 20)}
print(type(s8))  # <class 'set'>  


# ----------------------------------

# Typecasting  1. Implicit Typecasting   2. Explicit Typecasting

x = 90      # int
y = 67.89   # float
print(x + y)  # 157.89   # Implicit Typecasting

g = 890
w = '32'

# print(g+w)  # Error
w = int(w)
print(g+w)  # 922

h = True   # Bool
w = 67     # int

print(h+w)  # 68

h = False
w = 89
print(h+w)   # 89  # Implicit


str1 = "Thank"
str2 = "You"
print(str1 + str2)

s = '45.90'
# print(int(s))  # Error
print(int(float(s)))  # 45

import math

print(math.floor(45.99999))  # 45
print(math.ceil(45.0001))  # 46

 
print(2**3)  # 8      # 2*2*2  (Power)  # 8
print(2 ** 3 ** 2)  # 2 ** 9 --> 512


x = 'A'
# print(int(x))   # Error

print(ord(x))  # 65
print(chr(97))  # a
print(chr(48))  # 0

tup1 = (10,20,30)
print(list(tup1))   # [10, 20, 30]
print(type(tup1))   # <class 'tuple'>
 
num1 = int(input("Num1: "))
num2 = int(input("Num2: "))

print(num1 + int(num2))
print(f"sub is {num1} - {num2} = {num1 - num2}")
print(f"{num1} - {num2} = {num1 * num2}")
print(f"{num1} - {num2} = {num1 / num2}")
print(f"{num1} - {num2} = {num1 // num2}")
print(f"{num1} - {num2} = {num1 % num2}")
print(f"{num1} - {num2} = {num1 ** num2}")

# HW - Calc, 5 Area Program, Days, Seconds


