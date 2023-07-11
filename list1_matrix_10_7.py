# Write a Python program to test a list of one hundred integers between 0 and 999, which all differ by ten from one another. Return True otherwise False.

list1 = [10,20,30,40,50,60,70,80,90]


# Divide----------------
# flag = 1
# l2 = []

# for k in list1:
#     if k % 10 != 0:
#         flag = 0
#         l2.append(flag)
#         break
#     l2.append(flag)
# print(l2)
# print(all(l2))


# Differnce ----------------------
flag = 0
for i in range(len(list1)-1):
    if list1[i+1] - list1[i] == 10: 
        flag = 1
        print(flag,list1[i],list1[i+1],sep=' ')
    else:
        flag = 0
        break

if flag == 1:
    print(True)


# ------------------------------------------------


list1 = [[10,20,40],
         [90,50,60],
         [30,20,66]]

print(list1)
print(list1[1][2])  # 60

for sublist in list1:  # sublist = [10,20,40]
    for element in sublist:
        print(element,end=' ')  # 10 20 40 90 50 60 30 20 66

print()
for row in range(len(list1)):
    print(list1[row])


print()
for row in range(len(list1)):   # row = 0
    for col in range(len(list1[row])):   # col = 1
        print(list1[row][col])  # list1[0][1]

print()
for row in range(len(list1)):   # row = 0
    for col in range(len(list1[row])):   # col = 1
        print(list1[row][col],end=' ')  # list1[0][1]
    print()

print()

# Transpose
for row in range(len(list1)):   # row = 0
    for col in range(len(list1[row])):   # col = 0
        if list1[col][row] % 2 == 0:
            print(list1[col][row],end=' ')  # list1[1][0]
    print()



list1 = [[10,20,40],
         [90,50,60],
         [30,20,66]]


sum = 0
for row in range(len(list1)):   # row = 0
    for col in range(len(list1[row])):   # col = 0
        if row == col:
            sum += list1[row][col]
    print()

print(sum)  # 126

# HW

# 40 + 50 + 30  Diagonal Sum
# Spiral print
# Snake Print


list1 = [[10,20,40],
         [90,50,60],
         [30,20,66]]


for row in range(len(list1)):
    if row % 2 == 0:
        for col in range(len(list1[row])):
            print(list1[row][col])
    else:
        for col in range(len(list1[row])-1 , -1, -1):
            print(list1[row][col])


for row in range(len(list1)):
   for col in range(len(list1[row])):
       if list1[row][col] == 40:
           pass
        #    print(row,col)
            # print(list1[row].index(list1[row][col]))


