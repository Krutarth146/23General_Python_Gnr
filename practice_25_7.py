# 38. Write a Python program to sort the numbers in a given list by the sum of their digits.
# Input: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Output:
# [10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19]
# Input: [23, 2, 9, 34, 8, 9, 10, 74]
# Output:
# [10, 2, 23, 34, 8, 9, 9, 74]



# 47. Write a Python program to filter for numbers in a given list whose sum of digits is > 0, where the first digit can be negative.
# Input:
# [11, -6, -103, -200]
# Output:
# [11, -103]
# Input:
# [1, 7, -4, 4, -9, 2]
# Output:
# [1, 7, 4, 2]
# Input:
# [10, -11, -71, -13, 14, -32]
# Output:
# [10, -13, 14]


list1 = [10,20,]
# print(str(list1))

# for i in list1:
#     print(len(str(i)))



# 47. Write a Python program to filter for numbers in a given list whose sum of digits is > 0, where the first digit can be negative.
# Input:
# [11, -6, -103, -200]
# Output:
# [11, -103]
# Input:
# [1, 7, -4, 4, -9, 2]
# Output:
# [1, 7, 4, 2]
# Input:
# [10, -11, -71, -13, 14, -32]
# Output:
# [10, -13, 14]


list4 = [11, -6, -103, -200]
res = []

for num in list4:
    sum = 0
    copy = num

    if num > 0:
        res.append(num)
    
    elif num < 0:
        x = str(copy)
        for j in range(1, len(str(copy))):   # -6
            if j == 1:
                sum = sum - int(x[j])  # x[1]

            else:
                sum += int(x[j])



    num = copy

    if sum > 0:
        res.append(copy)

print(res)

