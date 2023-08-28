# # Linear Search

# list1 = [10,90,78,43,21,89,55,3,221,343,45,3]

# num = int(input("Enter any Number: "))

# # if num in list1:
# #     print("Element is Found")

# for i in range(len(list1)):
#     if list1[i] == num:
#         print(num,i)

# --------------------------------------------


# Binary Search

list1 = [i for i in range(1,201)]
# print(list1)

num = int(input("Enter any Number: "))  # 64
flag = 0

count = 0

min = 0
max = len(list1)-1

print()
while min <= max:
    count += 1
    mid = ( min + max ) // 2
    print(mid,'---')
    if list1[mid] == num:
        print("Element is Found",count)
        flag = 1
        break
    elif list1[mid] < num:
        print("Modified Min",min)
        min = mid + 1
    elif list1[mid] > num:
        print("Modified Max",max)
        max = mid-1


if flag == 0:
    print("Not Found",count)