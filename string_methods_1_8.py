list1 = [10,20,30,40,50]


list1.append(300)
print(list1)

list1.extend([300])
list1.extend([[300]])
list1.extend(['100',300])
print(list1)   # [10, 20, 30, 40, 50, 300, 300, [300], '100', 300]

list1.insert(2,4500)
print(list1)   # [10, 20, 4500, 30, 40, 50, 300, 300, [300], '100', 300]


# -----------------------------------------------------

# str1 = "    "

# print(str1.isalnum())  # False
# print(str1.isalpha())  # False
# print(str1.isascii())  # True
# print(str1.isdecimal())  # True
# print(str1.isdigit())  # True
# print(str1.isnumeric())  # True
# print(str1.isidentifier())  # True
# print(str1.isprintable())  # True
# print(str1.istitle())  # False
# print(str1.isspace())  # True

str1 = "Mithil is Good Boy123."
print(' '.join(str1))   # M i t h i l   i s   G o o d   B o y 1 2 3 .

print(len(str1))   # 22
print(str1.ljust(30,'$'))   # Mithil is Good Boy123.
print(str1.rjust(30,'$'))   # $$$$$$$$Mithil is Good Boy123.

str1 = "       Mithil is Good Boy123.        "
print(str1.lstrip())   # Mithil is Good Boy123.
print(str1.rstrip())   #        Mithil is Good Boy123.


str2 = "Hello Sam1"  # ----> Hello Ram
table = str2.maketrans("S", "R", "S")
print(table)   # {83: None}


print(str2.translate(table))   # Hello Ram



# str3 = "Hello Alin"

# table = str3.maketrans(' ', '0')

# print(str3.translate(table))   # HeSSi ASin

str3 = "Hello Arin123 Mithil"

# print(str3.partition(' '))   # ('Hello', ' ', 'Arin123 Mithil')
# print(str3.rpartition(' '))   # ('Hello Arin123', ' ', 'Mithil')
print(str3.split(' '))   # ['Hello', 'Arin123', '', 'Mithil']
print(str3.split('  '))   # ['Hello Arin123 Mithil']
# print(str3.split('i'))   # ['Hello Ar', 'n123 M', 'th', 'l']

str4 = " Hello Manoj"

# print(str4.partition(' '))   # ('', ' ', 'Hello Manoj')
# print(str4.rpartition(' '))  # (' Hello', ' ', 'Manoj')

# print(str4.split(' '))   # ['', 'Hello', 'Manoj']

print(str4.replace("noj", "hesh"))  #  Hello Mahesh

str5 =  "the lion is the King of the Forest"
print(str5.replace('the', 'a'))  # a lion is a King of a Forest
print(str5.replace('the', 'a',1))  # a lion is the King of the Forest

# a lion is the King of a Forests  # Hw