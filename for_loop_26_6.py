# For Loop

for r in range(10):   # end = 10 (n-1) 9 , Default start = 0
    print(r,end=' ')  # 0 1 2 3 4 5 6 7 8 9 


print()

for j in range(2,11):
    print(j,end=' ')   # 2 3 4 5 6 7 8 9 10

print()

for k in range(25,101):
    print(k,end=' ')  # 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100

print()


for royal in range(25,41,1):  # (start, end(n-1), step(n-1))
    print(royal,end=' ')  # 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
print()


for royal in range(25,41,2):  # (start, end(n-1), step(n-1))
    print(royal,end=' ')  # 25 27 29 31 33 35 37 39

print()

for royal in range(25,41,3):  # (start, end(n-1), step(n-1))
    print(royal,end=' ')  # 25 28 31 34 37 40
print()

for royal in range(41,25,3):  # (start, end(n-1), step(n-1))
    print(royal,end=' ')  # No o/p
print()

for royal in range(41,25):  # (start, end(n-1), step(n-1))
    print(royal,end=' ')  # No o/p
print()

for royal in range(41,25,-1):  # (start, end(n-1), step(n-1))
    print(royal,end=' ')  # 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26
print()

for royal in range(41,25,-3):  # (start, end(n-1), step(n-1))
    print(royal,end=' ')  # 41 38 35 32 29 26
print()

for royal in range(-3,6,-2):  # (start, end(n-1), step(n-1))
    print(royal,end=' ')  # 
print()

for royal in range(4, 12, -2):  # (start, end(n-1), step(n-1))
    print(royal,end=' ')  # 
print()

for royal in range(4, 12, 2):  # (start, end(n-1), step(n-1))
    print(royal,end=' ')  # 4 6 8 10
print()

for royal in range(-9, -2, 3):  # (start, end(n-1), step(n-1))
    print(royal,end=' ')  # -9 -6 -3
print()

for royal in range(-9, 5, 3):  # (start, end(n-1), step(n-1))
    print(royal,end=' ')  # -9 -6 -3 0 3
print()

for royal in range(4, -4, -1):  # (start, end(n-1), step(n-1))
    print(royal,end=' ')  # 4 3 2 1 0 -1 -2 -3
print()

for royal in range(2,5):
    for j in range(royal):
        if royal == j:
            break
        print(j,end=' ')
    print(royal,end=' ')  
# 0 1 2 0 1 2 3 0 1 2 3 4



list1 = [10,20,30,40]

for i in list1:
    print(i)   # 10 20 30 40

# for j in range(0,len(list1),2):
for j in range(0,4,2):
    print(list1[j])

l1 = [10,20,30]
l2 = [10,20,30]

print(l1[0] * l2[0])  # 100


str1 = "Krupanshi"


for i in str1:
    print(i,end=' ')  # K r u p a n s h i

l3 = ['str1', "90", 800, [10,20,3], {"name" : "Tushar", 'tup1' : (10,20,30)}, (10,)]


for i in l3[3]:
    print(i)