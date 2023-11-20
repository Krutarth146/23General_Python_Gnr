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

cur.execute("create table if not EXISTS PHY_DETAILS2 (PID INT PRIMARY KEY auto_increment, HEIGHT FLOAT, WEIGHT FLOAT, BMI FLOAT, ID int, FOREIGN KEY(ID) REFERENCES cust_details(ID))")

cur.execute("CREATE TABLE IF NOT EXISTS LOGS (LID INT PRIMARY KEY AUTO_INCREMENT, ENTRY_TIME DATETIME, EWEIGHT FLOAT, EXIT_TIME DATETIME, EXWEIGHT FLOAT, ID INT, FOREIGN KEY(ID) REFERENCES CUST_DETAILS(ID));")

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
                # print(list1)
                f = 0
                for subtup in list1:
                    if subtup[0] == user_id:
                        f = 1
                        print("Matched")
                        raise UniqueUserID
                if f == 0:
                    password = input("Enter Password: ") 
            
                    cur.execute('SELECT DATE_FORMAT(SYSDATE(),"%Y-%m-%d %H:%i:%S") FROM DUAL')
                    joining = cur.fetchone()  # ('11',)

                    cur.execute('select DATE_FORMAT(date_add(sysdate(), interval 1 year),"%Y-%m-%d %H:%i:%S")  from dual')
                    ending = cur.fetchone()

                    # ID INT PRIMARY KEY, NAME VARCHAR(30) NOT NULL, AGE INT NOT NULL, GENDER CHAR NOT NULL, USER_ID VARCHAR(30) NOT NULL UNIQUE, PASSWORD VARCHAR(16) NOT NULL
                    print(joining,ending)
                    query = "INSERT INTO CUST_DETAILS (NAME, AGE, GENDER, USER_ID, PASSWORD, joining_date, SUB_END_DATE) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    tup1 = (name, age, gender, user_id, password, joining[0], ending[0])
                    cur.execute(query, tup1)   
                    mydb.commit()
                    
                    query = "select id, USER_ID from cust_details"
                    cur.execute(query)
                    id3 = cur.fetchall()                      
                    
                    for subtup in id3:
                        if subtup[1] == user_id:
                            print(subtup[0])
                            break

                    height = float(input("Enter Height: "))
                    weight = float(input("Enter weight: "))
                    BMI = 5.5  # formula
                    query = "INSERT INTO phy_DETAILS2 (HEIGHT, WEIGHT, BMI, ID) VALUES (%s, %s, %s, %s)"
                    tup1 = (height, weight, BMI, subtup[0])
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
        password1 = input("Enter Password: ")
        cur.execute("SELECT USER_ID, password, id FROM CUST_DETAILS")
        list45 = cur.fetchall()

        d = 0
        for subtup in list45:
            if (username1 == subtup[0]) and (password1 == subtup[1]):
                print("Login Successfull....")
                cur.execute('SELECT DATE_FORMAT(SYSDATE(),"%Y-%m-%d %H:%i:%S") FROM DUAL')
                entry_time = cur.fetchone()  # ('11',)
                q1 = "insert into logs (ENTRY_TIME, id) values (%s, %s)"
                t6 = (entry_time[0], subtup[2])

                cur.execute(q1, t6)
                mydb.commit()
                ch = int(input("1 --- Logout"))
                if ch == 1:
                    pass
                    # cur.execute('select DATE_FORMAT(date_add(sysdate(), interval 1 year),"%Y-%m-%d %H:%i:%S")  from dual')
                    # ending = cur.fetchone()
                d = 1
                break
        if d == 0:
            raise wrongCred
        
except wrongCred:
    print("Invalid Cred.")
except:
    print("Error Occured")

finally:
    if mydb.is_connected():
        cur.close()
        mydb.close()