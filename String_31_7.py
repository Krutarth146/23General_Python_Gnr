# str1 = "Royal is Best Institute Ever123."

# print(str1[2::-2])  # [start : End (n-1) : step(n-1)]
# print(str1[2::5])  # ystter
# print(str1[2:8:5])  # ys
# print(str1[-6::2])  # e13
# print(str1[4:5:-1])  # blank
# print(str1[:-5:])  # Royal is Best Institute Eve
# print(str1[-10:14:1])  # Royal is Best Institute Eve


# for i in range(-10,14,2):   # (start, end(n-1),step(n-1))
#     print(i)


# ----------------------------------------------------

# str1 = "Arin is Good Boy."

# print(str1.count('o'))  # 3
# print(str1.count('o',11))  # 1
# print(str1.count('o',11,13))  # 0

# str1 = "Arin_is Good B@oy."
# print(str1.capitalize())  # Arin_is good boy.
# print(str1.casefold())  # arin_is good boy.
# print(str1.lower())  # arin_is good boy.
# print(str1.upper())  # ARIN_IS GOOD BOY.
# print(str1.title(),"----")  # Arin_Is Good B@Oy. ----
# print(str1.swapcase())  # aRIN_IS gOOD bOY.
# print(str1.isupper())  # False
# print(str1.islower())  # False
# print(str1.istitle())  # False

# str1 = "Arin_is Good B@oy."

# print(len(str1))   # 18
# print(str1.center(25))
# print(str1.center(25,'*'))   # ****Arin_is Good B@oy.***


# str2 = "Ståle"
# print(str2.encode())   # b'St\xc3\xa5le'
# print(str2.encode(encoding="ASCII", errors="namereplace"))   # b'St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
# print(str2.encode(encoding="ASCII", errors="replace"))   # b'St?le'
# print(str2.encode(encoding="ASCII", errors="backslashreplace"))   # b'St\\xe5le'
# print(str2.encode(encoding="ASCII", errors="ignore"))   # b'Stle'
# print(str2.encode(encoding="ASCII", errors="xmlcharrefreplace"))   # b'St&#229;le'

# str1 = "Arin_is Good B@oy."

# print(str1.endswith('y.'))   # True

# str1 = "Arin_is Good\tB@oy."
# print(str1.expandtabs())  # Arin_is Good    B@oy.
# print(str1.expandtabs(12))  # Arin_is Good            B@oy.
# print(str1.expandtabs(-4))  # Arin_is GoodB@oy.


# str3 = "{} is Good {}".format("Dhirya", "Boy")
str3 = "{1} is Good {0}".format("Dhairya", "Boy")
str3 = "{name} is Good {gender}".format(name = "Dhairya", gender =  "Boy")
print(str3)   # Dhairya is Good Boy


dict1 = {'Name' : "Arin", "Gender" : "Male"}

# str3 = 

print("{Name} is Good {Gender}".format_map(dict1))   # Arin is Good Male


name = "Arin"
gender = "Boy"
print(f"{name} is Good {gender}")   # Fstring   Arin is Good Boy

str3 = "Arin_is Good B@oy."
print(str3.find('o'))   # 9
print(str3.find('o',10))   # 10
print(str3.rfind('o'))   # 15
print(str3.index('o'))   # 9
print(str3.rindex('o'))   # 15
# print(str3.find('z'))   # -1
# print(str3.index('z'))   # Error  