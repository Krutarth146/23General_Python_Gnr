num = 21

if num % 3 == 0 or num % 7 == 0 and num % 5 == 0:
    print('Num is Div by 5 and 7 or 3')

# Logical Operators  and or not

# Truthy Values : 90, -80, True, [10,20,30], "Arin", 89.90
# Falsy Values : False, 0 , [], ''

if not []:
    print(True)   # True


num1 = 90
num2 = 78

# if num1 > num2: print(num1) 
# else: print(num2)


print(num1) if num1 > num2 else print(num2)   # 90


n1,n2,n3 = [10,95,230]

if n1 > n2:
    if n1 > n3:
        print(n1)
    else:
        print(n3)
else:
    if n2 > n3:
        print(n2)
    else:
        print(n3)


(print(n1) if n1 > n3 else print(n3)) if n1 > n2 else (print(n2) if n2 > n3 else print(n3))

# Bitwise Operator   &  |  ^  <<   >>

print(bin(902))   # 0b1110000110

print(0b1110000110)   # 902


print(bin(893))   # 1101111101
print(bin(56))    # 0000111000
# ---------------------------------
                #   0000111000   # AND
                #   1101000101   # XOR
print(0b1101000101)   # 837
print(893 & 56)   # 56 
print(893 | 56)   # 893
print(893 ^ 56)   # 837
print(893 << 3)   # 837   # 1101111101000  # 7144
print(893 >> 3)   # 837   # 1101111  # 111

print(0b1101111101000)   # 7144
print(0b1101111)   # 111


# -----------------------------------------------------

# while Loop (Entry Control Loop)

# Start, End, Step (Incre / Decre)

k = 1

while k<=100:
    if k % 3 == 0 or k % 7 == 0 and k % 5 == 0:
        print(k,end=' ')    # 3 6 9 12 15 18 21 24 27 30 33 35 36 39 42 45 48 51 54 57 60 63 66 69 70 72 75 78 81 84 87 90 93 96 99
    k+=1


jk = 900

while jk > 800:
    print(jk,end=' ')   # 900 899 898 897 896 895 894 893 892 891 890 889 888 887 886 885 884 883 882 881 880 879 878 877 876 875 874 873 872 871 870 869 868 867 866 865 864 863 862 861 860 859 858 857 856 855 854 853 852 851 850
    if jk == 850:
        break
    jk-=1


# ----------------------------------
print()
num = 89
while num <= 95:
    if num == 92:
        num+=1
        continue
    print(num,end=' ')   # 89 90 91 93 94 95
    num+=1


# ------------------------

num = 25
print()
print()
print()
while num <= 30:
    jk = 25

    while jk <= 30:
        if num == jk:
            break
        print(jk,end=' ')
        jk+=1
    print(num,end=' ')
    num+=1

# 25 25 26 25 26 27 25 26 27 28 25 26 27 28 29 25 26 27 28 29 30
print()
print()
while num <= 30:
    jk = 25

    while jk <= 30:
        if num == jk:
            jk+=1
            continue
        print(jk,end=' ')
        jk+=1
    print(num,end=' ')
    num+=1

# 25 25 26 25 26 27 25 26 27 28 25 26 27 28 29 25 26 27 28 29 30


# d1 = {'1':['a','b'],'2':['c','d']}

# l1 = d1['1']
# l2 = d1['2']

# for i in l1:
#     for j in l2:
#         print(i+j)

# value = {'1': ['a', 'b'], '2': ['c', 'd']}
# com = []

# for l1 in value['1']:
#     for l2 in value['2']:
#         com.append(l1 + l2)

# for com in com:
#     print(com)


# -----------------------

# %

num=int(input('\n enter the num:- '))
if num & 1:
    print('this is the odd')
else:
    print('this is the even')



def fun1(num):
    if num == 100:
        return num
    print(num,end=' ')
    return fun1(num+1)

print(fun1(1))


# i = 1
# fun(i)


