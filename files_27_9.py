# # Files


# # File  1. Text File   2. Binary File

# # File Operating Modes

# # 'w' ----> Write Mode  (Overwrite)
# # 'a' ----> Append Mode
# # 'x' ----> 

# # f1 = open('aman.txt', 'wt')
# # f1 = open('aman1.txt', 'x')
# # f1.write("Hello Arin Bhai")

# # list1 = ['\nHello Harsh Bhai', '\nBansi is GOod', '\nSb sir is also Good']


# # f1.writelines(list1)

# # f1.close()


# f2 = open('aman.txt','r')

# # x = f2.read()
# # x = f2.readline()   # Hello Arin Bhai
# # x = f2.readline(5)  # Hello
# # print(x)

# print(f2.tell())   # 0
# print(f2.readline())   # Hello Arin Bhai
# print(f2.tell())   # 17
# print(f2.readline())   # Hello Harsh Bhai
# print(f2.readline())   
# print(f2.readline())   
# print(f2.readline())   
# print(f2.readline())   


# f2.seek(17)   # Reset the value
# # f2.seek(17,)   # hw
# print(f2.readline())      # Hello Harsh Bhai


# f2.seek(0)
# list1 = f2.readlines()
# print(list1)   # ['Hello Arin Bhai\n', 'Hello Harsh Bhai\n', 'Bansi is GOod\n', 'Sb sir is also Good']
# print(f2.tell())   # 69

# f2.seek(0)
# x = f2.readlines()

# print(x)   # ['Hello Arin Bhai\n', 'Hello Harsh Bhai\n', 'Bansi is GOod\n', 'Sb sir is also Good']
# print(type(x))   # list

# c = 0
# l1 = []
# for k in x:  
#     c+=1
#     x = k.split()
#     l1.extend(x)
#     # for j in k:
# print(l1)

# print(c)
# f2.close()

import fun_prac_import_17_10

# fun_prac_import_17_10.greet()