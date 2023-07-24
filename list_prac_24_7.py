# l1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# l2 = []


# for num in l1:
#     sum = 0
#     for i in range(len(str(num))): 
#         sum += num % 10
#         num //= 10
#     l2.append(sum)


# res = []

# for i in zip(l1,l2):
#     res.append(i)

# print(res)   # [(10, 1), (11, 2), (12, 3), (13, 4), (14, 5), (15, 6), (16, 7), (17, 8), (18, 9), (19, 10), (20, 2)]

# def ele(subtup):
#     return subtup[-1]

# res.sort(key = lambda x : x[-1])

# print(res)  # [(10, 1), (11, 2), (20, 2), (12, 3), (13, 4), (14, 5), (15, 6), (16, 7), (17, 8), (18, 9), (19, 10)]

# final_ans = []
# for i in res:
#     final_ans.append(i[0])

# print(final_ans)   # [10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19]


# --------------------------


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

# 56. Write a Python program to find an integer exponent x such that a^x = n.
# Input:
# a = 2 : n = 1024
# Output:
# 10
# Input:
# a = 3 : n = 81
# Output:
# 4
# Input:
# a = 3 : n = 1290070078170102666248196035845070394933441741644993085810116441344597492642263849
# Output:
# 170



# 61. Write a Python program to find the number which when appended to the list makes the total 0.
# Input:
# [1, 2, 3, 4, 5]
# Output:
# -15
# Input:
# [-1, -2, -3, -4, 5]
# Output:
# 5
# Input:
# [10, 42, 17, 9, 1315182, 184, 102, 29, 15, 39, 755]
# Output:
# -1316384

# 60. Write a Python program to find a list of all numbers that are adjacent to a prime number in the list, sorted without duplicates.
# Input:
# [2, 17, 16, 0, 6, 4, 5]
# Output:
# [2, 4, 16, 17]
# Input:
# [1, 2, 19, 16, 6, 4, 10]
# Output:
# [1, 2, 16, 19]
# Input:
# [1, 2, 3, 5, 1, 16, 7, 11, 4]
# Output:
# [1, 2, 3, 4, 5, 7, 11, 16]