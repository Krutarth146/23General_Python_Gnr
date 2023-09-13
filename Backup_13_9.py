# # Operators: 

# # 1. Arithmetic   + - * / // % **

# num1 = 25
# num2 = 2
# print(f'{num1} / {num2} = {num1 / num2}')   # 25 / 2 = 12.5
# print(f'{num1} // {num2} = {num1 // num2}')   # 25 // 2 = 12
# print(f'{num1} % {num2} = {num1 % num2}')   # 25 % 2 = 1


# # Assignment Operator  = += -= *= /= //= %= <<= >>+ ^= |= &= (Lowest Priority)

# x = 90

# x += 10   # x = x + 10  # 100
# x += 300   # 400
# x /= 3     # 133.3333333333
# x += 900   # 1033.333333
# x %= 5     # 3.3
# x -= 1     # 2.

# print(x + 50)   # 52.33333333333326
# print(x)       # 2.3333333333332575

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



# # Method - 2
# # list2 = list(map(str, input().split()))
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
        l1 = []
        for k in str3:
            if ord(k) >= 48 and ord(k) <= 57:
                l1.append(int(k))
        print('Tuple is: ',tuple(l1))
        new1.append(tuple(l1))
    

        # ----------------------------------------------------
    elif i[0] == '{' and i[-1] == '}':   
        i = i[1:-1]
        # print(str1)

        list1 = list(i)

      
        new = []
        for i in list1:
            if i != '"':
                new.append(i)

        temp = []
        dict1 = {}
        str1 = ''
        for i in range(len(new)):
            if new[i] == ',':
                for c in temp[2:]:
                    str1 += c
                dict1[temp[0]] = int(str1)
                temp = []
                str1 = ''
                
                pass
            elif i == len(new) - 1:
                temp.append(new[i])
                for c in temp[2:]:
                    str1 += c
                dict1[temp[0]] = int(str1)

            else:
                temp.append(new[i])

        D_key = [i for i in dict1]
        D_val = [i for i in dict1.values()]
        print('Dict Key', D_key)
        print('Dict Val', D_val)

    else:
        print('Set')
