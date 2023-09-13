# Operators: 

# 1. Arithmetic   + - * / // % **

num1 = 25
num2 = 2
print(f'{num1} / {num2} = {num1 / num2}')   # 25 / 2 = 12.5
print(f'{num1} // {num2} = {num1 // num2}')   # 25 // 2 = 12
print(f'{num1} % {num2} = {num1 % num2}')   # 25 % 2 = 1


# Assignment Operator  = += -= *= /= //= %= <<= >>+ ^= |= &= (Lowest Priority)

x = 90

x += 10   # x = x + 10  # 100
x += 300   # 400
x /= 3     # 133.3333333333
x += 900   # 1033.333333
x %= 5     # 3.3
x -= 1     # 2.

print(x + 50)   # 52.33333333333326
print(x)       # 2.3333333333332575

# & - Bitwise
# and - Logical

# a=[1,2,3,4,5,(4,5),"u",{"w":45,"r":21},5]

# list1 = []
# total_inputs = int(input("Enter Total Inputs: "))


# Method - 1

# for i in range(7):  # 0 to 6
# for i in range(total_inputs):
#     x = input("Enter any Input: ")
#     list1.append(x)

# print(list1)


str1 = '{"w":45,"r":21}'
# Method - 2
# list2 = list(map(str, input().split()))
# print(list2)
list1 =['1','2','3','4','5','(4,5)',"u",'{"w":45,"r":21}','5']
new1= []

for i in list1:
    if len(i) == 1:
        if ord(i) >= 48 and ord(i) <= 57:
            new1.append(int(i))
            print(int(i))
        elif (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
            new1.append(i)
            print(i)
    elif i[0] == '(' and i[-1] == ')':
        print(i)
        str3 = i[1:-1]
        print("str3 = ",str3)
        l1 = []
        for k in str3:
            if ord(k) >= 48 and ord(k) <= 57:
                l1.append(int(k))
        print('Tuple is: ',tuple(l1))
        new1.append(tuple(l1))
    elif i[0] == '{' and i[-1] == '}':
        if ':' in i:
            print('Dict is')
            str3 = i[1:-1]
            print('str3',str3)   # "w":45,"r":21
            
            dict3 = {}
            val = ''
            for p in range(len(str3)-2):

                temp = ''
                if str3[p+2] == ':':
                    print('str3[p] = ',str3[p])
                    temp += str3[1:p+1]

                    for r in range(p+3,len(str3)-1):
                        if str3[r+1] == ',':
                            val+=str3[p+3 : r+1]
                            # print(str3[p+3])
                            break
                    dict3[temp] = int(val)   
                print('dict3',dict3)                 
                print(str3)
                if p == len(str3)-1:

                        break

            print('temp',temp)
            print('str3', str3)

            



        else:
            print('Set')
print(new1)