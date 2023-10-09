str4 = " The quic brown fox jumps over the lazy dog"

# alpha = 'qwertyuiopasdfghjklzxcvbnm '

# for i in alpha:
#     if i not in str4.lower():
#         break
# else:
#     print('Pangram')

# if len(set(str4.lower())) == 27:
#     print('Pangram')

str1 = "Ståle"

print(str1.encode())   # b'St\xc3\xa5le'
print(str1.encode(encoding='ASCII', errors='replace'))  # b'St?le'
print(str1.encode(encoding='ASCII', errors='namereplace'))  
print(str1.encode(encoding='ASCII', errors='ignore'))  
print(str1.encode(encoding='ASCII', errors='backslashreplace'))    # b'St\\xe5le'
print(str1.encode(encoding='ASCII', errors='xmlcharrefreplace'))    # b'St&#229;le'

print(str1.endswith('e'))
print(str1.startswith('st'))   # False


str2 = 'Aman has\t2 legs'
print(str2)                  # Aman has        2 legs
print(str2.expandtabs())     # Aman has        2 legs
print(str2.expandtabs(32))   # Aman has                        2 legs

str1 = 'Ram'
str2 = 'Good'

str3 = '{} is {}'
print(str3.format(str1,str2))

str3 = '{1} is {0}'
print(str3.format(str1,str2))

str3 = '{str1} is {str2}'
print(str3.format(str1=  'Vishnu', str2 = 90))


dict1 = {"Name" : "Manoj", 'Roll' : 90, 'Address' : {'Ahm' : [10,20,30], 'gnr' : [20,0,390,30]}}

# Ordered (Not Index)

print(dict1['Address'])   # {'Ahm': [10, 20, 30], 'gnr': [20, 0, 390, 30]}
print(dict1['Address']['gnr'])   # [20, 0, 390, 30]
print(dict1['Address']['gnr'][1])   # [20, 0, 390, 30]
dict1 = [{"Name" : "Manoj", 'Roll' : 90, 'Address' : {'Ahm' : [10,20,30], 'gnr' : [20,0,390,30]}}]
print()