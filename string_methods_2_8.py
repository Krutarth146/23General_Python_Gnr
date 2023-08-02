str5 =  "the lion is the King of the Forest"

print(str5.replace('the', 'a', 1))

# print(str5[::-1])

# print(str5.replace('the','a').replace('a','the',2).replace('the','a',1))

list1 = str5.split()
print(list1)

for ind in range(len(list1)):
    if list1[ind] == 'the':
        list1[ind] = 'a'
        break

list1 = list1[::-1]
for ind in range(len(list1)):
    if list1[ind] == 'the':
        list1[ind] = 'a'
        break

list1 = list1[::-1]

str1 = ' '.join(list1)
print(str1)   # a lion is the King of a Forest

# -----------------------------------------------

str5 =  "the lion is the King of the Forest"

print(str5.removeprefix("t"))   # he lion is the King of the Forest
print(str5.removesuffix("st"))  # the lion is the King of the Fore


str5 =  "the lion is the\nKing of\nthe Forest"
print(str5.splitlines())   # ['the lion is the', 'King of', 'the Forest']

['the lion is the', 'King of', 'the Forest']
# Forest

str1 = 'royal trch'
print(str1.removeprefix('ro'))

list1 = ['the lion is the' , 'King of' , 'the forest']


print(list1[2][4:])  # forest
print(type(list1[2][4:]))  # str
# print(list1[2:3])
# print()

str5 =  "the lion is the King of the Forest"
print(str5.startswith('t'))  # True


str7 = '500'
print(str7.zfill(7))