# Single Line Comment

'''
Multi
Line
Comment
'''

# printf("Hello ROyalites!");  in c

print("Hello Royalites!")  # Hello Royalites!
print('SB sir')   # SB sir

print('''
    Address: 
        Sarghasan - 302
        Gnr Chokdi - 380001
''')


print("Hello 'Divy'",end=' agni ')
print("Hello Shubham")   # Hello Divy agni Hello Shubham

# Python is Dynamic Lang., Interpreted

# int x = 90;

print("Nupur")
print("Nupur")

x = 90
y = 70
z = 56
c = 90
# print("%d%d%d",x,y,z);

print(x,y,z      ,c, sep=", ",end=' ')   # 90, 70, 56, 90
print("Hello")
# print(x y z)

# _name = 'Bansi'
_name = "Bansi"
money = 900.67

print(_name,"has",money,"ruppes only.")   # Bansi has 900.67 ruppes only.
print(_name+" has",money,"ruppes only.")  # Bansi has 900.67 ruppes only.

print(f"{_name} has {money} Rupees only.")  # fstring (Adv. Formatted String)


print(90 + 56)  # 146
print(45 / 2)  # 22.5
print(46 / 2)  # 23.0
print(46 / 2)  # 23.0   # FLoat Division
print(46 // 2)  # 23
print(45 // 2)  # 22   # Floor Division 
print(21 // -4)  # -6

print()

print(round(45.90))   # 46
print(round(45.40))   # 45
print(round(45.40,2))   # 45.4
print(round(45.49,1))   # 45.5
print(round(45.49,0))   # 45.0
print(round(45.49,-1))   # 45.0
print(round(45.49,-2))   # 0.0
print(round(55.49,-2))   # 100.0