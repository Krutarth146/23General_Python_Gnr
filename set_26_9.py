str1 = 'Apple is Very useful t us.'

str1 = str1.lower()

vowels = "aeiou"


dict1 = {}

for i in vowels:   # i = 'a'
    # dict1[i] = str1.count(i)
    if str1.count(i) != 0:
        dict1.update({i : str1.count(i)})

print(dict1)   # {'a': 1, 'e': 3, 'i': 1, 'o': 1, 'u': 3}

print(len(dict1))


str1 = "the big dwarf only jumps"


list1 = str1.split(' ')
print(list1)   # ['the', 'big', 'dwarf', 'only', 'jumps']



str1 = ''.join(list1)
print(str1)   # thebigdwarfonlyjumps


list1 = [i for i in str1 if ord(i) >= 97 and ord(i) <= 120]
print(list1)


# a=[1,2,3,4,5,(4,5),"u",{"w":45,"r":21},5]


# print([int(i) for i in input().strip().split()])

# print(list(map(str, input().strip().split())))


# Array

import array as arr

# a1 = arr.array('i', [10,20,30,40,])
a1 = arr.array('u', ['b','x','z','w'])
print(a1)    # array('i', [10, 20, 30, 40])