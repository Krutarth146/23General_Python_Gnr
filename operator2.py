# Bitwise Operator  & | ^ << >> ~

print(57 & 32)   # 32


# 111001
# 100000
# -------
# 100000  ---> 32

print(34 | 89)   # 123
 

# 0100010
# 1011001
# -------
# 1111011

print(34 ^ 31)  # 61
# xor 
# 0 0 0
# 1 1 0
# 1 0 1
# 0 1 1

print(34 << 2)   # 136

# 10001000.00

print(401 >> 3)   # 50

print(891 << 1) 

print(~32)     # -33   # H.W.
print(~(-58))  # 57


# Logical Operators   ---> and  or  not

print(90 and 56)  # 56
print(90 or 56)  # 90


# If Else

# age = int(input())
age = -10
name = "Vivek"

if age >= 18: 
    print(f"{name} is Eligible for voting")  # fstring
elif age <= 0:
    print("Enter Valid Age.") 
    if age == -3:
        print("Not Born")
else:
    print(f"{name} is Not Eligible. You need {18 - age} years more.")
    

# H.w ---> Maths + sci + Eng --> TOtal, Avg, Grades

num1 = 10
num2 = 3000
num3 = 390

print(num1 if num1 > num2 else num2)

# H.W   # 3 Variables  num1 , num2  ()

print((num1 if num1 > num3 else num3) if num1 > num2 else (num2 if num2 > num3 else num3))

# print(eval("3+2+1"))  # Explore

# print(exec('print("Hello")')) # Explore

num = 7

if num % 5 == 0 or num % 7 == 0 and num % 10 == 0:
    print("Divisible by 5 and 7")   # Divisible by 5 and 7