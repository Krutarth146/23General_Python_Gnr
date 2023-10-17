
b = 10

def greet():
    global b
    a = 20
    print(a+b)  # 30

    c = 20
    b = a+c   # 40
    return b
    # print(msg1, msg2)
    

# greet(msg2 = "Hello", msg1 = ("Ram","Ashok"))
# print(greet())   # 40
# print(b)  # 40
print('Hello Motto')
