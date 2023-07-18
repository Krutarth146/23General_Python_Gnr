list1 = [2,2,3,3,3,4,5,6,6,6,1,12,1,2,3,22]

# Index display 
# 2 ---> 0,1,5,...
# 4 ---> 2 ...
# 5 ---> 3
# 6 ---> 4

# {2:[0,1,5...], 4 : [2...], }

# 2 ----> [0, 1, .....]
# 3 ----> [2,3,4,...]

list1 = [2,2,3,3,3,4,5,6,6,6,1,12,1,2,3,22]
unique = []


for i in list1:
    if i not in unique:
        unique.append(i)

print(unique)   # [2, 3, 4, 5, 6, 1, 12, 22]
# print(list(set(list1)))  # [1, 2, 3, 4, 5, 6, 12, 22]

for ele in unique:
    temp = []
    for ind in range(len(list1)):
        if ele == list1[ind]:
            temp.append(ind)
    print(ele,'---->',temp)

# List Compre.


# [[10,90], [32,54], [12,78], [23,11], [64,89], [21,1]]