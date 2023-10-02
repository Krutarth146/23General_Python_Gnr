f1 = open("sbsir.txt", 'wt+')


f1.write("Hello My Name is Dhairya My Prajapati")

list1 = ['\nHello Aman\n', 'Hello Krupanshi\n']
f1.writelines(list1)


f1.seek(0)  # Reset

# aman = f1.read()
aman = f1.readlines()
print(aman)
print(len(aman))   # 3

main = []
for line in aman:
    # print(line)
    main.extend(line.split(' '))

    # for k in line:
    #     print(k)
print(main)
f1.close()


for j in range(len(main)):
    # if main[j][0] == 'M':
    if main[j].startswith("My"):
        print(main[j]) # My
        print(j)   # 1, 5


f1 = open("Dict_Exercises_s.png",'rb')

x = f1.read()

# print(x)

f1.close()

f2 = open("Dict_Exer_copy.jpg","wb")

f2.write(x)

f2.close()

print(f2)