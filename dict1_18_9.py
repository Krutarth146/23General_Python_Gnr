# # 22. Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

# dict1 = {'k1' : 90, 'k4' : 9, 'k2' : 88, 'k3' : 56}

# vals = [i for i in dict1.values()]

# vals.sort()
# vals = vals[-3:]

# new = {}
# for i in vals: # i = 56
#     for key,v1 in dict1.items():
#         if i == v1:
#             new[key] = v1

# print(new)    


# m = 1000
# sum = 90011
# str1 = ''

# while sum > 0:
#     if sum >= 1000:
#         str1 += 'm'
#         sum -= 1000
#         continue


# 23. Write a Python program to combine values in a list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

list1 = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

l2 = []
for dict22 in list1:
    l2.append([g for g in dict22.values()])

print(l2)

#  unique

for sublist in range(len(l2)):
    for sub2 in range(sublist+1,len(l2)):
        if l2[sublist][0] == l2[sub2][0]:
            l2[sublist][1] += l2[sub2][1]


# Recursion  ----> Func

# def Mithil(num):
#     print(num,end=' ')  # 1
#     if num == 100:
#         return
    
    
    
#     Mithil(num + 1)  # Mithil(2)


# Mithil(1)


def factorial(num):
    if num == 1:
        return 1

    return num * factorial(num-1)   # 5 * 4 * 3 * 2 

print(factorial(5))   # 120