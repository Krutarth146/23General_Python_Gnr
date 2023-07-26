# 60. Write a Python program to find a list of all numbers that are adjacent to a prime number in the list, sorted without duplicates.

list1 = []

# Input:
# [2, 17, 16, 0, 6, 4, 5]
# Output:
# [2, 4, 16, 17]

list1 = [2, 17, 16, 23, 6, 4, 5]
res = []
for ind in range(len(list1)):
    div = 0
    for k in range(1,list1[ind]+1):  # 1 to 3 
        if list1[ind] % k == 0:  # 2 % 1 == 0
            div += 1

    if div == 2:
        if ind == 0:
            res.append(list1[ind+1])
        elif ind == len(list1)-1:
            res.append(list1[ind-1])
        else:
            res.extend([list1[ind+1],list1[ind-1]])

res.sort()
print(res)


# ------------------------------------------------------------
# Calculate Sum of Digits and if Sum is > 0 then add it to Another Answer List.

list4 = [31, -6, -103, -200, -301, -555]   #   < 0
res = []

for num in list4:   # num = -103
    sum = 0
    copy = num  # copy = -103

    if num > 0:
        res.append(copy)
    
    elif num < 0:   # -103
        x = str(copy)  # x = '-103'   # string
        for j in range(1, len(str(copy))):  # 1 to 4 ---> 1,2,3
            if j == 1:
                sum = sum - int(x[j])   # Sum = -1
 
            else:
                sum += int(x[j])  # 3

        num = copy

        if sum > 0:  # sum = 2
            res.append(copy)

print(res)

# ----------------------------------------------------------------------------------
# 66. Write a Python program to find the indices of the closest pair from a list of numbers.

# Input: [1, 7, 9, 2, 10]
# Output:
# [0, 3]
# Input: [1.1, 4.25, 0.79, 1.0, 4.23]
# Output:
# [4, 1]
# Input: [0.21, 11.3, 2.01, 8.0, 10.0, 3.0, 15.2]
# Output:
# [2, 5]


# Input: [1, 7, 9, 2, 10]
# Output:
# [0, 3]


list1 = [1.1, 4.25, 0.79, 1.0, 4.23]
res = []
for i in range(len(list1)):
    
    for j in range(len(list1)):

        if i != j:
            x = list1[i] - list1[j]
            res.append([list1[i],list1[j],abs(x)])
    
    print("res = ",res)
    
res.sort(key=lambda x : x[-1])
ans = res[0][0:2]
print(ans)