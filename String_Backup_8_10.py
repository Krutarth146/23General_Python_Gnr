str1 = 'Rishita is Good Girl123.'

print(len(str1))  # 24   # Starts from 1, Index starts from 0

print(str1.center(30, '*'))   # ***Rishita is Good Girl123.***

str2 = 'Ståle'
print(str2.encode())   # b'St\xc3\xa5le'
print(str2.encode(encoding="ASCII",errors="replace"))   # b'St?le'
print(str2.encode(encoding="ASCII",errors="namereplace"))   # b'St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
print(str2.encode(encoding="ASCII",errors="ignore"))   # b'Stle'
print(str2.encode(encoding="ASCII",errors="xmlcharrefreplace"))   # b'St&#229;le'
print(str2.encode(encoding="ASCII",errors="backslashreplace"))   # b'St\\xe5le'

str1 = 'Rishita is Good Girl123.'
print(str1.endswith('3.'))  # True
print(str1.startswith('3.'))  # True
str1 = 'Rishita is\tGood Girl123.'
print(str1.expandtabs(32))  # Rishita is                      Good Girl123.

name = 'Manoj'
mode = 'Good'

str3 = f"{name} is {mode} Boy"   # fstring (Adv. FOrmatted str)
print(str3)

str3 = '{name} is {mode} Boy.'
# print(str3.format(name, mode))
print(str3.format(name = "Manoj", mode = 'Good'))


dict1 = {'name' : 'Ramesh', 'mode' : "Bad"}

print(str3.format_map(dict1))


# print(str1.i)


# pangram ----> A to Z and space
# anagram ----> act ---> cat, listen ---> silent

# Pangram Program

str4 = " The quick brown fox jumps over the lazy dog"

# if len(set(str4.lower())) == 27:
#     print('Pangram')

new = ''

for i in str4.lower():  
    if i not in new:
        new+=i.lower()

print(len(new))   # 27

# anagram ----> act ---> cat, listen ---> silent


# rishita  --  tishira

str1 = "actt"
str2 = 'cate'
list1 = []

if len(str1) == len(str2):
    temp = []
    dict1 = {}

    for i in set(str1):
        # temp.append((i,str1.count(i)))   # [('a', 1), ('c', 1), ('t', 2)]
        dict1[i] = str1.count(i)          #  {'t': 2, 'c': 1, 'a': 1}
else:   
    pass

print(dict1)


d1 = {'t': 2, 'c': 1, 'a': 1}
d2 = {'c': 1, 'a': 1, 't': 2}   # Ordered, No Indexing

if d1 == d2:
    print(True)

# print(d2['C'])   # Error
print(d2.get('C'))   # None


str4 = "MISISIPPI"

# list1 = [['M' , 1], ['I' , 4].....]
# dict1 = {'M' : 1, 'I' : 4...}


dict1 = {}

for i in str4:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i]+=1

print(dict1)   # {'M': 1, 'I': 4, 'S': 2, 'P': 2}


print(' '.join(str1))   # a c t t

str2 = 'Aman'

print(str2.join(str1))   # aAmancAmantAmant
print(str1.join(str2))   # Aacttmacttaacttn


print(str1.removeprefix('a'))   # ctt

str1 = 'Aman has two bets\n3 Balls'
# print(str1)
print(str1.splitlines())   # ['Aman has two bets', '3 Balls']

str2 = '5000'
print(str2.zfill(5))   # 05000