# 13

# Length

# num = 5621

# length = len(str(num))
# print(length)  # 4
# counter = 0

# while num > 0:
#     num = num // 10
#     counter+=1

# print(counter)

# print(25 / 2)   # 12.5  # float
# print(25 // 2)  # 12  # int



# -------------------------------

# Perfect Number

# 6 ---> 1+2+3  == 6

num= 1

while num <= 10000: 

    sum = 0
    i = 1


    while i<num:   # 28 ---> 1 2 4 7 14
        if num % i == 0: 
            sum = sum + i
        i+=1

    # print(sum)

    if sum == num:
        print(num)

    num+=1


# Twin Number
 
# 22

num = 1

while num <= 10000:
    mul = 1
    sum = 0

    xerox = num

    while xerox > 0:
        rem = xerox % 10
        sum = sum + rem
        mul = mul * rem
        xerox = xerox // 10

    if sum == mul:
        print(num)
    num += 1

# 100 to 400   ---> 3 Number Even


num = 100
counter = 0
while num <= 400:
    # num = 123
    xerox = num
    flag = 0
    while xerox != 0:
        counter += 1
        rem = xerox % 10 
        if rem % 2 == 0:
            flag = 1
        else:
            flag = 0
            break
        xerox = xerox // 10

    if flag == 1:
        print(num)

    num += 1

print("Counter = ",counter)  # 528


# Task


# 4. We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.
# Input: 2
# Output:
# [2, 4]
# Input: 10
# Output:
# [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# Input: 3
# Output:
# [3, 5, 7]
# Input: 17
# Output:
# [17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]