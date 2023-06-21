k = 1

while k<=10:
    print(k,end=' ')   # 1
    k+=1 
    if k == 5:
        break

p = 10
while p<=15:  
    if p == 12:
        p+=1
        continue
    print(p)   # 10 11 13 14 15
    p+=1


# ---------------------

# x = 25
# l = 25
# while x<=30:
#     while l<=30:
#         if x == l:
#             continue
#         print(l)
#         l+=1
#     print(x)
#     x+=1

# Infinite


k = 56
print()
while k<=60:         # k = 57 ,  l = 58
    l = 56
    while l<60:
        if k == l:
            l+=1
            continue
        print(l,end=' ')
        l+=1
    print(k,end=' ')
    k+=1
# 57 58 59 56 56 58 59 57 56 57 59 58 56 57 58 59 56 57 58 59 60


# ------------------------------

j = 13
p = 13
while j<=16:          # j = 16, p = 16
    while p <= 16:   
        if j <= p:  
            break
        print(p)
        p+=1
    print(j)
    j+=1

# 13 13 14 14 15 15 16