# # # Linear Search

# # list1 = [10,90,78,43,21,89,55,3,221,343,45,3]

# # num = int(input("Enter any Number: "))

# # # if num in list1:
# # #     print("Element is Found")

# # for i in range(len(list1)):
# #     if list1[i] == num:
# #         print(num,i)

# # --------------------------------------------


# # Binary Search

# list1 = [i for i in range(1,201)]   # 1 to 200
# # print(list1)

# num = int(input("Enter a Number: "))
# flag = 0

# count = 0

# min = 0
# max = len(list1)-1


# while min <= max:
#     count += 1
#     mid = ( min + max ) // 2  # 99 49 74 61 67 64 62 63
#     if list1[mid] == num:
#         flag = 1
#         print("ELement is Found",count)
#         break
#     elif list1[mid] < num:
#         min = mid + 1
#     elif list1[mid] > num:
#         max = mid-1


#     # if flag == 0:
#     #     print("Not Found",count)
# print(num,'---->',count,end='\t')


# def twoArrays(k, A, B):
#     flag = 0
#     for i in A:
#         for j in B:
#             if (i + j) == k:
#                 print(k)
#                 # B.remove(j)
#                 flag+=1
#                 break
#     if flag == len(A):
#         return "YES"
#     else:
#         return "NO"
        

# print(twoArrays(10,[18, 73, 55, 59, 37, 13, 1, 33],[81, 11, 77, 49, 65, 26, 29, 49]))


A = [84, 2, 50, 51, 19, 58, 12, 90, 81, 68, 54, 73, 81, 31, 79, 85, 39, 2]
B = [53, 102, 40, 17, 33, 92, 18, 79, 66, 23, 84, 25, 38, 43, 27, 55, 8, 19]
k = 94

def twoArrays(k, A, B): 
    list1 = [] 
    for i in A:
        flag = 0
        list1 = []
        for j in B:
            if (i+j) >= k:
                list1.append(j)

        if list1:
            ele = min(list1)
            print(ele,list1)
            B.remove(ele)
        else:
            flag = 1
            return "NO"
        print(i,j,B)
    if flag == 0:
        return "YES"
    

print(twoArrays(k,A,B))