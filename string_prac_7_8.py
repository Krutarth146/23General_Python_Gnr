str1 = "Nupur"

# ans = ['N', 'Nu', 'Nup', 'Nupu', 'Nupur' ....]

for ch in range(len(str1)):   # ch = 1
    for k in range(ch+1):   # k = 0,1
        print(str1[k],end='')   # N
    print()
 
# res = ['NN', 'Nu', 'Np', 'Nu', 'Nr', 'uN' ...]

# -----------------------------------
# 41. Write a Python program to strip a set of characters from a string.

str1='the lion is the king of the junglee'

list1 = str1.split()
print(list1)


for i in list1:
    print(i)

for k in range(len(list1)):
    print(list1[k])



#  Write a Python program to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.


# PYtHon  # PYTHON
# PythON  # PythON