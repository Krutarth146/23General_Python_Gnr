# Loops

# Entry Control Loop  ---> 1. while   2. For

# Intialization (start), Condition (End), Flow (Incre / Decre)


x = 25   # start
while x <= 35:  # condition

    print(x,"Hello",end='   ')
    # x = x + 1
    x+=1   # Flow


# --------------------------

i = 1

while i<=100:
    print(i,end=' ')
    i+=2
# 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99

print()
# ---------------
print()
print()
print()
j = 1

while j <= 100:
    if j % 3 == 0 and j % 5 == 0 and j % 7 == 0:
        print(j,end=' ')   # 15 30 45 60 75 90
    j+=1


# -------------------
print()
print()

k = 1
while k<= 100:
    if k % 5 == 0 or k % 7 == 0 and k % 10 == 0:
        print(k)
    k+=1

# 25 to 1 in reverse print which is divisible by 3

g = 25

while g >= 1:
    if g % 3 == 0:
        print(g,end=' ')   # 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
    g-=1

# User Defined Table   7 * 1 = 7

# 1 to 10

# num = int(input())
# i = 1

# while i < 11:
#     # print(f"{num} * {i}  = {num * i}")
#     # print(num, "*", i ,'=', num * i)
#     # print("{} * {} = {}".format(num,i,num*i))
#     print("{0} * {1} = {2}".format(num,i,num*i))
#     i+=1



# -------------------------------------------

# Prime Numbers

# 24 ---> 1, 2, 3, 4, 6, 8, 12, 24
# 23 ---> 1, 23
# 45 ---> 1, 3, 5, 9, 15, 45
# 29 ---> 1, 29
# 37 ---> 1, 37

print()
num = int(input())
factors = 0

i = 1

while i<=num:
    if num % i == 0:
        print(i)
        factors += 1
    i += 1

print("Factors =",factors)

if factors == 2:
    print("Prime NUmber")

# 1 to 10000 Prime Numbers
# Ans. 2 3 5 7 11 13 ........

