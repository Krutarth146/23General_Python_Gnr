list1 = [[10, 90], [43,56], [22, 88], [45,67]]

# c = 0
# for i in range(len(list1)-1):  
#     for j in range(i+1,len(list1)):
#         if list1[i][1] > list1[j][1]:
#             list1[i], list1[j] = list1[j], list1[i]
#         c+=1


# print(c)  # 6

# print(list1)


# ------------------------
list1 = [[10, 90, 88, 32], [43,56,21,32], [22, 88], [45,67, 43, 21]]

def Dev(mithil):
    return mithil[-2]


# print(Dev("Mayank"))
# print(Dev([10, 90, 78, 93]))

list1.sort(key=Dev)
print(list1)


list4 = ['M','i','s','s','i','s','s','i','p','p','i']

# M --- > 1
# i --- > 4

list5 = list(set(list4))  # Uniqueness
print(list5)


for i in list5:
    print(i,list4.count(i))

dict1 = {}

for x in list4:
    if x not in dict1:
        dict1[x] = 1
    else:
        dict1[x] += 1

print(dict1)   # {'M': 1, 'i': 4, 's': 4, 'p': 2}



# 38. Write a Python program to sort the numbers in a given list by the sum of their digits.
# Input: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Output:
# [10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19]
# Input: [23, 2, 9, 34, 8, 9, 10, 74]--> 5,2,9,7,8,9,1,11
# Output:
# [10, 2, 23, 34, 8, 9, 9, 74]

