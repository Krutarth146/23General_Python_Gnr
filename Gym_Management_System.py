import mysql.connector

mydb = mysql.connector.connect(user="root", password = "mysql", host = "localhost", database = "gen")

# print(mydb)   # <mysql.connector.connection_cext.CMySQLConnection object at 0x000001FA5C61C6D0>

if mydb.is_connected():
    print("Database Connected....")
else:
    print("Error occured")

cur = mydb.cursor()

# GYM Mgmt  ----> cust_details, logs, Phy_details

cur.execute("create table IF NOT EXISTS cust_details (ID INT PRIMARY KEY, NAME VARCHAR(30) NOT NULL, AGE INT NOT NULL, GENDER CHAR NOT NULL, USER_ID VARCHAR(30) NOT NULL UNIQUE, PASSWORD VARCHAR(16) NOT NULL)")

cur.execute("create table if not EXISTS PHY_DETAILS1 (PID INT PRIMARY KEY, HEIGHT FLOAT, WEIGHT FLOAT, BMI FLOAT, FOREIGN KEY(PID) REFERENCES cust_details(ID))")

# cur.execute("alter table cust_details add (joining_date date, sub_end_date date)")


class wrongCred(Exception):
    pass

class UniqueUserID(Exception):
    pass

class SubExpired(Exception):
    pass

# cur.execute("alter table cust_details modify id int auto_increment")
#  ALTER TABLE CUST_DETAILS MODIFY JOINING_DATE DATETIME;
#  ALTER TABLE CUST_DETAILS MODIFY SUB_END_DATE DATETIME;
from datetime import datetime


# import datetime

# print(datetime.datetime.today())  # 2023-11-08 17:56:17.36812
try:
    print("1 ------ Signup")
    print("2 ------ Login")
    print("3 ------ Subs. Renewal")

    choice = int(input("Enter your Choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender M or F: ")
        while 50:
            user_id = input("Enter User ID: ")
            try:
                cur.execute("select USER_ID from cust_details")
                list1 = cur.fetchall()   # [('shr',), ('Manioj',) ]
                print(list1)
                f = 0
                for subtup in list1:
                    if subtup[0] == user_id:
                        f = 1
                        print("Matched")
                        raise UniqueUserID
                if f == 0:
                    password = input("Enter Password: ") 
            
                    cur.execute('SELECT DATE_FORMAT(SYSDATE(),"%Y-%m-%d %H:%i:%S") FROM DUAL')
                    joining = cur.fetchone()

                    cur.execute('select DATE_FORMAT(date_add(sysdate(), interval 1 year),"%Y-%m-%d %H:%i:%S")  from dual')
                    ending = cur.fetchone()

                    # ID INT PRIMARY KEY, NAME VARCHAR(30) NOT NULL, AGE INT NOT NULL, GENDER CHAR NOT NULL, USER_ID VARCHAR(30) NOT NULL UNIQUE, PASSWORD VARCHAR(16) NOT NULL
                    print(joining,ending)
                    query = "INSERT INTO CUST_DETAILS (NAME, AGE, GENDER, USER_ID, PASSWORD, joining_date, SUB_END_DATE) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    tup1 = (name, age, gender, user_id, password, joining[0], ending[0])
                    cur.execute(query, tup1)   
                    mydb.commit()
                    
                    query = "select id from cust_details where name = %s"
                    t1 = (name,)
                    cur.execute(query, t1)

                    id1 = cur.fetchone()  # id1[0]

                    height = float(input("Enter Height: "))
                    weight = float(input("Enter weight: "))
                    BMI = 5.5  # formula
                    query = "INSERT INTO phy_DETAILS1 (pid, HEIGHT, WEIGHT, BMI) VALUES (%s, %s, %s, %s)"
                    tup1 = (id1[0], height, weight, BMI)
                    cur.execute(query, tup1)
                    mydb.commit()
                    print("Signup Successfull.")
                    f = 1

                if f == 1:
                    break
                
                    # Phy Details Height, weight, BMI, target_BMI, target_weight
                    # logs Login time, entry weight, logout time, Exit Weight   cur.execute("select user_id, password from cust_details where user_id = %s".format(user_id))
            except UniqueUserID: 
                print("Please Enter Another User ID")


    elif choice == 2:
        username1 = input("Enter UserName: ")
        password1: input("Enter Password: ")
        print("-----------")
        cur.execute("SELECT USER_ID, password FROM CUST_DETAILS")
        list45 = cur.fetchall()

        if len(list45) != 0:
            for subtup in list45:
                print(subtup[1])
                print(subtup[0])
                if (username1 == subtup[0]) and (password1 == subtup[1]):
                    print(list45)
                    print("Login Successfull....")
                    break
                else:
                    print("Nope")
        else:
            raise wrongCred
        
except wrongCred:
    print("Invalid Cred.")
except:
    print("Error Occured")

