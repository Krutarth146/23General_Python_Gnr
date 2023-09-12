# # Python is Interpreted (Line by Line), High Levele (Human Redabale), Dynamic Lang.  (Run time)

# #include<stdio.h>
# # import pillow

# print('Hello')
# print("Shubham")

# try:
#     printa('''Arin
#             is 
#             Good
#         Boy''')
# except:
#     print("Error Occured")

# print("""Dhairya""")
# print("""Dhairya""")


# # int x = 90     # Compile Time Memory Allocation


# x = 90  # int

# kl = True
# print(kl)
# print(type(kl))   # <class 'bool'>

# kl = 67 + 90j
# kl = 'Shubham'

# # Single Line Comment


# '''
# sdcsc
# sd
# cs
# scsd
# '''


# # -----------------------------------------------------------

# # Print Function

# name = 'Arin'
# rupees = 900

# print("Arin has 500 Rupees only.")
# # print("%s has %d Rupees only.",name,rupees)
# print(name,"has",rupees,"Rupees only.",end=' $$$$$$$ ')    # Arin has 900 Rupees only.
# print(name,"has",rupees,"Rupees only.",sep='\t')    # Arin    has     900     Rupees only.
# print(name+" has",rupees,"Rupees only.")   # Arin has 900 Rupees only.



# x,y = [10,20]
# print(x,end=' ',sep=' ')   
# print(90)
# print("Manoj","Krutarth",sep = ' ',end='%')
# print("Aman")

# # 10 90
# # Manoj Krutarth%Aman

# print(f'{name + "Arin"} has {rupees + 1500} only.')  # ArinArin has 2400 only.

# # Datatypes

# # int, float, bool, complex, str, NoneType, list, Tuple, Set, Dictionary

# x = None

# print(type(x))


# str1 = '90.90'
# print(type(str1))   # str


# str3 = "True"
# str3 = True
# print(type(str3))   # <class 'bool'>

# # Typecasting   ---> One Datatype to Another Datatype 

# v1 = 90.89   # Float
# j = 89    # int
# print(v1 + j)   # 179.89   # Implicit T.C

# jk = True
# print(True + False)   # Implicit


# op = 'Aman'
# we = 'Arin'
# print(op + we * 2 + ' D3k911')  # 908989


# x = '4590'
# x = '45.90'
# print(int(float(x)))   # 45   # Explicit T.C
# print(round(45.90))   # 46

# import math

# print(math.floor(45.99999))   # 45
# print(math.ceil(45.00001))   # 46
# print(math.ceil(45.00000))   # 45


# print(-25 // 3)   # -9


# # print(int('a'))   # Error

# print(ord('a'))   # 97
# print(chr(33))   # !


# print(chr(ord('a')+1))   # b

# str1 = 'M'   # 77
# ans = 'z'    # 122

# print(chr(ord(str1) + 45))





str1 =     "KrutazY"
# Capital ---> +2
# Small -----> -3

# Z ---> B
# a ---> x

ans = ""


# && ---> and  (Logical and)




for i in str1:
    if i == 'M':
        ans += chr(ord(str1[0]) + 41)
    elif i == 'i':
        ans += chr(ord(str1[1]) - 23)

print(ans) 


# str1 = "Mithil"

# x = 90

# # for var_name in range(x):
# # for(i=0;i<=90;i++)  # STart = 0, End = 90, Flow - ++

# for var_name in range(90):   # STart = 0, End = 90 (n-1) 89
#     print(var_name)   # 0 to 89

# for shubham in range(11, 91):   # STart = 11, End = 91 (n-1) 90
#     print(shubham,end=' ')   # 0 to 89


# for mithil in [10,20,90,45,23]:
#     print(mithil)

str1 =     "KrutazY"
new = ''


for i in str1:
    if i == 'Y' or i == 'Z':
        new += chr(ord(i) - 24)
    elif i == 'a' or i == 'b' or i == 'c':
        new += chr(ord(i) +23 )
    elif ord(i) >= 65 and ord(i) <= 88:
        new += chr(ord(i) + 2)
    elif ord(i) >= 100 and ord(i) <= 122:
        new += chr(ord(i) - 3)

print(new)   # MorqxwA


# -----------------------------------


# Operators

# Membership Operator   ---> in, not in



# printf("ENter any Number: ");
# scanf("%d",&num1);
# num1 = int(input("Enter Number: "))  # str
# num2 = int(input("Enter Number: "))   # str


# x = 90   # int

# print(num1 * num2)  # 180


list1 = [10,90,89,45,67]
find_num = int(input())   # 45

# Linear Searching

for k in list1:
    # print(k)
    if k == find_num:
        print("Element is Found")
        break
else:
    print('Not Found')


# -------------------------------

if find_num in list1:
    print('Element is Found')
else:
    print('Not Found')


# ---------------------------------------------

# Identity Operator   is, is not

x = 90
y = 90

if x == y:
    print('x == y')

if x is y:
    print('x is y')

x = [90]
y = [90]

if x == y:   # Match Elements 
    print('x == y')

if x is y:   # Match References
    print('x is y')

dict1 = {'Name' : "Krutarth", 'Roll' : 90, 'list1' : [10,20]}
dict2 = {'Name' : "Krutarth", 'list1' : [10,20], 'Roll' : 90}


list1 = [10,20,30]
list2 = [10,30,20]

list1.sort()
list2.sort()
if list1 == list2:
    print("same")

print(id(list1),id(list2))
list1 = list2
print(id(list1),id(list2))

if list1 is list2:
    print("Same by ref")