# Tuple ---> 


list1 = []
print(type(list1))  # list

tuple1 = ()
print(type(tuple1))  # tuple

tuple1 = (10)
print(type(tuple1))  # int

tuple1 = (10,)
print(type(tuple1))  # <class 'tuple'>

tup3 = (10,90.89,"str1",90+6j,True,[(10,10)], (10,10,), {10,10,'10'}, {"Name" : "Divy"})
print(tup3)  # (10, 90.89, 'str1', (90+6j), True, [(10, 10)], (10, 10), {10}, {'Name': 'Divy'})

print(len(tup3))  # 9

# Difference

# list ---> Ordered (Indexed), Allow's Duplicates, Mutable
# tuple ---> Ordered (Indexed),  Allow's Duplicates, Immutable

# list1[2] = 900

tup1 = (10,20,30,40,50,60,10,20,32,22)

# tup1[2] = 900  # 'tuple' object does not support item assignment

print(tup1.count(200))  # 0
# print(tup1.index(200))  # Error

print(min(tup1))
print(max(tup1))
print(sum(tup1))  # 294


# for i in sorted(tup1):
#     print(i)


for i in sorted(tup1):
    print(i)

tup1 = tuple(sorted(tup1))

print(tup1[::-1])   # (60, 50, 40, 32, 30, 22, 20, 20, 10, 10)

tup1 = (190,30,40,50)
tup2 = (33,290,11)


print(id(tup1))   # 8672
tup1+=tup2    
print(id(tup1))   # 8512
 
print(tup1)   # (190, 30, 40, 50, 33, 290, 11)


tup1 = (10,20,10,10,10)

print(tup1.index(10,1))


for i in range(len(tup1)):
    if tup1[i] == 10:
        print(i,tup1[i])

tup1 = list(tup1)
tup1.append(500)
print(tuple(tup1))   # (10, 20, 10, 10, 10, 500)

print(type(tup1))  # <class 'list'>

tup1 = (10,20,30,40,50,60,10,20,32,22)

print(tup1[4:8:-1])   # ()
print(tup1[5:-2:1])   # (60, 10, 20)

for j in range(5,-2,1):
    print(j)  # blank

for j in range(5,-2,-3):
    print(j)  # 5 2 -1

print(tup1[-3])   # 20
print(tup1[-3:])   # (20, 32, 22)

tup1 = (10,20,30,40,50,60,10,20,32,22)
print(tup1[-3::-1])   # (20, 10, 60, 50, 40, 30, 20, 10)
print(tup1[6:-3:-1])   # ()


tup1 = (10,20,30,40,50,60,10,20,32,22)

# ele = ?   # 3

# min --> 10,20,22
# max --> 40,50,60