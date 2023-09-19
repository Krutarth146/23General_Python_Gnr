for num in range(1,10001):
    x1 = num
    x2 = num

    count = 0
    # FInd TOtal Digits
    while num > 0:
        num = num // 10
        count+=1

    # print(count)
    sum = 0

    while x1 > 0:
        rem = x1 % 10
        k = 1
        mul = 1
        while k<=count:
            mul = mul * rem
            k+=1
        sum = sum + mul
        x1 = x1 // 10


    if x2 == sum:
        print(x2)


# Power Logic
# # 2 ** 3  ---> 2*2*2
# num = 2
# k = 1
# mul = 1

# while k<=3:
#     mul = mul * num   # 8 = 4 * 2
#     k+=1

# print(mul)   # 8