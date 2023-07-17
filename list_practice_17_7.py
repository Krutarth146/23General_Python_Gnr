list2 = [[100,21,30], 
         [40,90,89], 
         [55,3,2]]

d1 = []
for row in range(len(list2)):   # list2[0] = [100, 21, 30]
    for col in range(len(list2[row])):   # 
        d1.append(list2[row][col])

d1.sort()

print(d1)  
print(len(d1))   # 9

# new = [[],[],[]]
# i = 0
# for row in range(len(list2)):   # list2[0] = [100, 21, 30]
#     for col in range(len(list2[row])):
#         list2[row][col] = d1[i]
#         i+=1

# print(list2)
new = []
i=0
for row in range(len(list2)):   # list2[0] = [100, 21, 30]
    temp = []
    for col in range(len(list2[row])):
        temp.append(d1[i])
        i+=1
    new.append(temp)

print(new)

import random

print(random.choice(new))


l1 = [10,20,30,90,78,54,32]

ne1 = []
for i in l1:
    temp = []
    temp.append(i)
    # ne1.append(temp)
    print(temp)

# print(ne1)


list1 = [2,2,4,5,6,2,3,4,9,9,1,4,2,3,2]


# Index display 
# 2 ---> 0,1,5,...
# 4 ---> 2 ...
# 5 ---> 3
# 6 ---> 4

# {2:[0,1,5...], 4 : [2...], }

# l4 = []
# l1 = [1,2,3,4,5]
# tup1 = (3,1)
# c = 0
# for j in l1:
#     for i in tup1:
#         l4.append(i)
#         c+=1
# print(c)
# print(l4)


