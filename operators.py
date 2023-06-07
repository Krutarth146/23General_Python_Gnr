x = '90'
print(float(x))   # 90.0

# g = 'xyz'
# print(int(g))

print('%c' % 65)  # A
print('%c' % 32)  # 
print('%d' % 32)  # 32
print('%d' % 80)  # 32
print('%c' % 'A')  # A
print('%x' % 15)  # f
print('%X' % 15)  # F
print('%o' % 15)  # 17
# print('%O' % 15)  # Error

# print('%e' % ('NaN'))  # nan
# print('%E' % 'NaN')  # NAN
# print('%f' % 'NaN')  # nan
# print('%F' % 'NaN')  # NAN
print('%.2f' % 3.14)  # 3.140000

# %c - Char
# %d - int
# %f - FLoat
# %o - octal
# %x - Hexadecimal
# %s - string


print("Hello S.B %s %s %d Sir " %('Very','Good',900)+"Good Evening")  # Hello S.B Good Sir Good Evening

print("{} is Very {} Guru.".format("Manoj sir", 700))
print("{0} is Very {1} Guru.".format("Manoj sir", 700))

x = "Manish"
print("{1} is Very {0} Guru.".format(x,700))   # 700 is Very Manish Guru.

print(f"{0} is Very {float(90)} Guru.")   # 700 is Very Manish Guru.

# name = 'Dhairya'
# mode = 'Good'

print("{name} is {mode} Boy. {x} is also good. ".format(mode = 'Good', x = "Yash", name= 'Shubham'))

# Shubham is Good Boy. Yash is also good.

# -------------------------------------------------------

# Operators

# 1. Arithmetic O/p  
#   
# **    (Right to left)
# * / // %    
# + -

# + -  ---> Unary O/p

c = 333

print(c.__sizeof__())  # 28

# Assignment O/p   = += -= *= /= //= %= <<= >>= &= |= ^= (Low Priority)

x = 90

x += 10   # x = x + 10   # 100
x %= 2  # 0
x /= 3  # 0.0
x += 100  # 100.0
x *= 2   # 200.0

print(x)   # 200.0
y = 90
x += y
print(x)  # 290.0