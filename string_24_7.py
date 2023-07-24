str1 = 'Mit hil is Good Boy.'
str2 = "SBsir"
str3 = '''Arin'''

print(str2)  # SBsir

# String is Immutable (Not Changeble)

# # char arr1[] = "Arin";
# arr1[2] = 'M'

print(str2[2])  # s
# str2[2] = 'M'   # 'str' object does not support item assignment
str2 = "Manojooo"
print(id(str2))  

# str2 = str2[:4] + str2[4:6].replace('o', 'k') + str2[5:]
# print(id(str2))

# print(str2)   #  Manojkooo

print(str2[:4],str2[4:6].replace('o','k') + str2[6:], sep='')


# --------------------------------------------------
str2 = "Royal is Best Institute Ever123."

print(str2[-1])  # . 
print(type(str2[-1]))  # <class 'str'>
print(str2[-32])  # R


print(len(str2))   # 32

# Slicing

print(str2[::])   # Royal is Best Institute Ever123.
print(str2[-1:])  # .
print(str2[:-1:])  # Royal is Best Institute Ever123
print(str2[::-1])  # .321revE etutitsnI tseB si layoR
print(str2[:-1])  # Royal is Best Institute Ever123

for i in range(-3,3,2):
    print(i)  # -3 -1 1

str2 = "Royal is Best Institute Ever123."
print(str2[-3:3:2])  # blank