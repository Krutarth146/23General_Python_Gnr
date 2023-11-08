import mysql.connector

mydb = mysql.connector.connect(user = "root", password = "mysql", database = "gen", host = "localhost")

# print(mydb)   # <mysql.connector.connection_cext.CMySQLConnection object at 0x00000238EE8CC6D0>

if mydb.is_connected():
    print("Database Connected...")
else:
    print("Unable to Connect")

cur = mydb.cursor()

# cur.execute("create table demo1 (id int, Name varchar(20), address varchar(30))")
# print("Table Created")

# cur.execute("Insert into demo1 (Name, address) values (10, 'Aman', 'Ahmedabad')")
# cur.execute("Insert into demo1 values (10, 'Aman', 'Ahmedabad')")

# Primary Key ---> Not Null & Unique
# cur.execute("Insert into demo values (20, 'Aman', 17)")


id = 30
name = 'Yash'
age = 20    

query = "Insert into demo values (%s, %s, %s)"
tup1 = (id, name, age)

cur.execute(query, tup1)


mydb.commit()


# Create a New Table Primary Key, Not Null