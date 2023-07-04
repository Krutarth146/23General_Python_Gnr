list1 = [10,20,34,56,90,78,67]


# index1 = int(input())
# print(list1[index1])

l2 = [10,20,30,40,50,60,70,81,91]

for j in l2:
    print(j,end=' ')   # 10 20 30 40 50 60 70 81 91 

print()
for k in l2[::-1]:
    print(k,end=' ')   # 91 81 70 60 50 40 30 20 10

print()
for h in range(len(l2)):
    # print(h,end=' ')  # 0 1 2 3 4 5 6 7 8
    if h % 2 == 1:
        print(l2[h],end=' ')  # 20 40 60 81

print()
print()

for _ in l2:
    if _ % 2 == 1:
        print(_)

print()

counter = 0
for j in range(4):
    for h in range(3):
        for t in range(2):
            pass
            counter+=1

print(counter)  # 24

l2 = [26, 89, 56, 45, 32, 21]

# [(26,26), (26,89), (26,56) ....]
res= []
for j in l2:   # j = 26
    for k in l2:  # k = 26
        res.append((j,k))
print(res)


l3 = [10,20,31,40,67,506]


for j in range(len(l3)):
    if l3[j] % 2 != 0:
        print(j)

l4 = [10, 90, 78, 78, 67, 45]

for k in range(len(l4)):
    if l4.count(l4[k]) == 1:
        print(l4[k])


#  ------------------------------

for j in l4:
    if l4.count(j) == 1:
        print(j)

# ------------------------------------


l7 = [10,20,30,405,90]
l8 = [90,1,32,45,30]

# [(10,90), (20,1), (30,32), (405,45), (90,30)]


for k in range(len(l7)):
    for y in range(len(l8)):
        if k == y:
            print(l7[k],l8[y])


for f,k in zip(l7,l8):
    print((f,k))


