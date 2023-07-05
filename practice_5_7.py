list1 = ['C', 'o', 'm', 'p', 'u', 't', 'e', 'r']

# Reverse this list without using reverse Method

# Method - 1
# Slicing

print(list1[::-1])   # ['r', 'e', 't', 'u', 'p', 'm', 'o', 'C']


# Method - 2

for j in range(len(list1)-1, -1, -1):
    print(list1[j],end=' ')   # r e t u p m o C

# Method - 3

for i in reversed(list1):
    print(i)

# Method - 4

list1.reverse()
print(list1)

# Method - 5

my_list = ['c', 'o', 'm', 'p', 'u', 't', 'e', 'r']
reversed_list = []

while my_list:
    reversed_list.append(my_list.pop())

print(reversed_list)


# Method - 6

list1 = ['C', 'o', 'm', 'p', 'u', 't', 'e', 'r']

length = len(list1)
for k in range(length // 2):
    list1[k], list1[length-1-k] = list1[length-1-k], list1[k]
    # temp = list1[k]
    # list1[k] = list1[length-1-k]
    # list1[length-1-k] = temp

print(list1)  # ['r', 'e', 't', 'u', 'p', 'm', 'o', 'C']


# Program = 2

list2 = [1,0,1,1,1,0,1,1,0]


for i in list2:
    if i == 0:
        list2.remove(0)
        list2.append(0)

print(list2)   # [1, 1, 1, 1, 1, 1, 0, 0, 0]

# ---------------------

list1 = [10,20,30,10,80,90,32,10,10]


# --------------------------------

l4 = [1,1,1,1,1,1,1,1,0]

# l8 = [1,2,3,1,1,1]
sum = 0
flag = 0

for i in range(len(l4)):
    sum += l4[i]  # sum = sum + l4[i]

    if i+1 == sum:
        flag = 1
    else:
        flag = 0
        break

if flag:
    print(True)
# 

str1 = "Royal"

# Tqacn