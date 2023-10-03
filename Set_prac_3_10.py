list1 = [10,20,30,40,50]
list2 = [10,20,30,50,10,20]
ans = 40

list3 = [2,9,4,5]
list4 = [2,10,9,4,5]
ans = 10


f2 = open('sbsir.txt', 'rt')
c = 0
for i in f2.read():
    if i.lower() == 'i':
        c+=1

print(c)
f2.close()


c = 0

# list1= ["a", 'e', 'i' ,'o' ,"u"]
# for i in str1:
#     if i in list1:
#         c+=1
# print(c)

str1 = 'Jatin Raaathod'   # ---> 6

str2 = 'aeiouAEIOU'
ans = sum(str1.count(i) for i in str2)
dict1  = {j : str1.count(j) for j in str2 if str1.count(j) > 0}  # {'a': 4, 'i': 1, 'o': 1}
# (4,0,1,1,0,0,0,0,0,0) 
print(ans)   # <generator object <genexpr> at 0x000001BA772A9A10>
print(dict1)