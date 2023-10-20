import json

# record = {
#     '1001' : {'pName' : 'cadbury', 'qn' : 230, 'price':20},
#     '1002' : {'pName' : 'Kellogs', 'qn' : 450, 'price':50},
#     '1003' : {'pName' : 'parleg', 'qn' : 300, 'price':10},
#     '1004' : {'pName' : 'kitkat', 'qn' : 60, 'price':30}
# }

f1 = open('Inventory.txt','r')
raw_data = f1.read()

record = json.loads(raw_data)

# print(type(record))
f1.close()

# print(len(record))  # 4
# print(record['1002'])   # {'pName': 'Kellogs', 'qn': 450, 'price': 50}
# print(record['1002']['qn'])   # 450

print('Menu'.center(40,'-'))

print("Product ID     Product Name    Product Quantity    Product Price")

for i in record:
    print(i, record[i]['pName'], record[i]['qn'], record[i]['price'], sep='             ')



upid = input("Enter Product Id: ")
user_need = int(input("Enter Quantity: "))

total_bill = 0   # snake case
# totalBill = 0  # Camel case
if upid in record and user_need > 0:
    if user_need <= record[upid]['qn']:
        total_bill = user_need * record[upid]['price']
        record[upid]['qn'] -= user_need
        print("Total Bill Amount is",total_bill)
        print('Inventory Updated, Thank You!!')
    else:
        print(f"We have only {record[upid]['qn']} Quantity.")
        choice = input("If you need this then Press Y or y: ")
        if choice.lower() == 'y':
            total_bill = record[upid]['qn'] * record[upid]['price']
            record[upid]['qn'] = 0
            print("Total Bill Amount is",total_bill)
            print('Inventory Updated, Thank You!!')
        else:
            print('Thank You!')
            exit()
else:   
    print('Invalid')

# print(record)


# JSON -----> Javascript Object Notation

fp = open("Inventory.txt",'w')

data = json.dumps(record)
# print(data)
# print(type(data))

fp.write(data)
fp.close()


# Add_Product, Quantity
# Bill.txt  ----> Name, Date, Total Bill Amount import datetime, date