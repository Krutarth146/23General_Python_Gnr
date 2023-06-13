x = 90
y = 90

# Identity O/p (Ref. Comparison)  is , is not

print(id(x))  # 1648476883984
print(id(y))  # 1648476883984

# y += 10
# print(id(x))   # 1691815513104
# print(id(y))   # 1691815513424

if x == y:
    print("x == y")   # x == y

if x is y:
    print("x is y")   # x is y


l1 = [10,20,30,40,50,50]  # List
l2 = [10,20,30,40,50,50]  # List

if l1 == l2:
    print("l1 == l2")

print(id(l1))  # 1904495941824
print(id(l2))  # 1904496096256

l2 = l1  # Deep Copy


print(id(l1))  # 1626681694400
print(id(l2))  # 1626681694400

if l1 is l2:
    print("l1 is l2")


# ---------------------------

# Memebership o/p    in  ,  not in

l2 = [10, 90, 89, 67, 45, 34]


# Linear Search
user_need = int(input("Enter any Number: "))

for _ in l2:
    if user_need == _:
        print(f"{user_need} is Found")
        break
else:   # Else block executed if for loop is Naturally Executed.
    print("Not Found")

# 

if user_need in l2:
    print(f"{user_need} is Found")
else:
    print("Not Found")


fruits = ["lichi",'Mango', 'apple', 'banana']

user_need = input()

if user_need not in fruits:
    pass
else:
    print(f"{user_need} is Available")
    