# String -----> Immutable

str1 = 'A'
print(type(str1))

str2 = "Dhairya"
print(type(str2))

str3 = '''Bansi'''
print(type(str3))


str1 = "Aman is Good Boy123."

print(len(str1))   # 20  len starts from 1, Indexes starts from 0
print(id(str1))     # 1818602714528
print(max(str1))   # y  (121)
print(min(str1))   # space (32)

str1 = 'Dhairya'
str2 = ' Patel'

print(id(str1))
str1+=str2
print(id(str1))

print(str1)   # Dhairya Patel

print('Muskan ' * 3)  # Muskan Muskan Muskan
print('Muskan ' + '3')  # Muskan 3


# Indexing & Slicing

str1 = "Aman is Good Boy123."

print(str1[3])   # n
print(str1[-3])  # 2  # str

print(str1[4::1])   #  is Good Boy123.
print(str1[-5:-1:1])   # y123
print(str1[-5: :1])   # y123.
print(str1[: :1])   # Aman is Good Boy123.
print(str1[: :2])   # Aa sGo o13
print(str1[: :-1])   # .321yoB dooG si namA
print(str1[: :-2])   # .2yBdo inm
print(str1[8:11:-1])   # .


# String Methods --------------------------------


str1 = "Aman_is Good Boy123."

print(str1.capitalize())   # Aman_is good boy123.
print(str1.title())   # Aman_Is Good Boy123.
print(str1.istitle())   # False
print(str1.upper())   # AMAN_IS GOOD BOY123.
print(str1.lower())   # aman_is good boy123.
print(str1.swapcase())   # aMAN_IS gOOD bOY123.
print(str1.casefold())   # aman_is good boy123.


str1 = "Aman_is Good Boy123."

list1 = str1.split(' ')  # by default = ' '
list1 = str1.split('_')  # ['Aman', 'is Good Boy123.']
list1 = str1.split('A')  # ['', 'man_is Good Boy123.']
print(list1)   # ['', 'man_is Good Boy123.']

list1 = str1.partition('A')  # ('', 'A', 'man_is Good Boy123.')
print(list1)
list1 = str1.partition(' ')  # ('Aman_is', ' ', 'Good Boy123.')
list1 = str1.rpartition(' ')  # ('Aman_is Good', ' ', 'Boy123.')
print(list1)

  # ('Aman_is Good', ' ', 'Boy123.')


list1 = ['Dhairya', 'is', 'Good']
print(' '.join(list1))   # Dhairya is Good


str1 = 'Bansi is Also Good'
str2 = 'Aman'
print(''.join(str1))   # Bansi is Also Good


print(str1.replace('Bansi', 'Nupur'))   # Nupur is Also Good
print(str1.replace('is', 'are'))   # Bansi are Also Good
print(str1.replace('o', 'w'))   # Bansi is Alsw Gwwd
print(str1.replace('o', 'w',1))   # Bansi is Alsw Good
print(str1.replace('o', 'w',-1))   # Bansi is Alsw Good

str2 = 'Hello Sam1'

table = str2.maketrans('Samw', 'RAMW', '1')
print(table)  # {83: 82, 97: 65, 109: 77, 49: None}


print(str2.translate(table))   # Hello RAM


str1 = 'the lion is the King of the Jungle.'


str1 = str1.replace('the','a',1)
list1 = str1.split()

for k in range(len(list1)-1,-1,-1):
    if list1[k] == 'the':
        list1[k] = 'a'
        break

str1 = ' '.join(list1)

print(str1)   # a lion is the King of a Jungle.

ans = 'a lion is the king of a Jungle.'


str1 = 'Amana'
print(str1.ljust(10,'$'))   # Amana$$$$$
print(str1.rjust(10,'$'))   # $$$$$Amana


print(str1.center(10,'*'))   # **Amana***


str1 = '     Dhairya       '
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())   # same as trim in SQL

str1 = 'Manoj is goodi 45'
print(str1.count('z'))   # 0
print(str1.count('i', 7,8))   # 0
print(str1.find('z'))    # -1
# print(str1.index('z'))   # Error
print(str1.index('i'))   # 6
print(str1.rindex('i'))   # 13


str1 = 'Nayan'   # Palindrome or Not???



# pangram ----> A to Z and space
# anagram ----> act ---> cat, listen ---> silent