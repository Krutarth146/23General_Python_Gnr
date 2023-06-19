
# Print Reverse Number
num = 872  # ----> 278


# while num!=0:
while num > 0:
    remainder = num % 10  # 8
    print(remainder,end='')   # 278
    num = num // 10  # 0

# Sum of Odd Digits
num = 9631
sum = 0
print()
# while num!=0:
while num > 0:
    remainder = num % 10  # 6
    if remainder % 2 != 0:
        sum = sum + remainder  # 13
    num = num // 10  # 0

print(sum)


# Palindrome Numbers
num = 101  #  ---> 167
sum = 0
xerox = num
print()
# while num!=0:
while num > 0:
    remainder = num % 10  # 7
    sum = sum * 10 + remainder   # 167
    num = num // 10  # 0

print(sum)


if xerox == sum:  # 0 == 101
    print("Palindrome")


# Armstrong Number
num = 8208  #  ---> 167
sum = 0
xerox = num
print()
# while num!=0:
while num > 0:
    remainder = num % 10  # 1
    sum = sum + remainder ** len(str(xerox))   # sum =  153
    num = num // 10  # 0

print(sum)


if xerox == sum:  # 153 == 153
    print("Armstrong")


# 1 to 10000 Palindrome, Armstrong, Prime, Perfect, Twin, Find Total Digits

# num = 99999
# while(num > 0)

# for( ; num > 0 ; )

# Perfect Numbers

# 6 ---> 1 + 2 + 3 == 6
# 28 --> 1 + 2 + 4 + 7 + 14  == 28   


# Twin NUmbers

# 22 ---> 2 + 2 = 4 == 2*2 = 4
# 321 ---> 1+2+3 == 1*2*3


# 3. Write a Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
 

import random

x = random.randint(1,9)
print(x)

y = int(input())

if x == y:
    print("True Guess!!")
else:
    print("Wrong")

print(bin(56))
print(hex(56))

print(0b0101011)