num = 89321   # ----> 398

# while num != 0:
while num > 0:
    print(num % 10,end='')   # 8
    num = num // 10    # num = 0

# ---------------------------------------------

num = 8   # ----> 398
counter = 0
print()
# while num != 0:
while num > 0:
    num = num // 10    # num = 0
    counter += 1

print(counter)

# ---------------------------------------------

num = 6732   # ---->
print()
sum = 0

while num > 0:
    remainder = num % 10   # 6
    if remainder % 2 != 0:
        sum = sum + remainder   # 18
    num = num // 10        # 0

print(sum)  # 18

# ------------------------------------------------


print()


x1 = 1   # Start   

while x1 <= 10000:  # End POsition   # num = 56

    rev = 0


    num1 = x1
    xerox = num1

    while num1 > 0:
        remainder = num1 % 10   # 6
        rev = rev * 10 + remainder   # 65
        num1 = num1 // 10        # 0

    # print(rev)  # 18
    if rev == xerox:  # 65 == 56
        print(x1,end=' ')

    x1+=1


