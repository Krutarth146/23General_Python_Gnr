# list1 = [10,20,30,40,50,56]

# print(len("Aman"))
# print(len([10,203,40,88]))
# # print(len(5632))   # Error
# print(len('5632'))    # 4

# l2 = iter(list1)  #  __iter__, __next__

# print(l2)   # <list_iterator object at 0x0000020C0C5FC6D0>

# print(next(l2))
# print(next(l2))
# print(next(l2))


# Expense Management : 

class Customer():
    def __init__(self):
        self.name = ""
        self.email = ""
        self.password = ""
        self.grocerry = 0
        self.personal = 0
        self.utility = 0

    def sign_up(self):
        self.name = input("Enter Name: ")
        self.email = input("Enter Email: ")
        self.password = input("Enter Password: ")

        if self.email.count('@') == 1 and self.email.count('.') == 1 and self.email.endswith('.') == False:
            return 1
        else:
            return 0
        

    def login(self, userid, paswd):
        return self.email == userid and self.password == paswd
    
    def personal_exp(self, amount):
        self.personal += amount

    def grocerry_exp(self, amount):
        self.grocerry += amount

    def utility_exp(self, amount):
        self.utility += amount


list1 = []
while True: 
    print("1 ---- Signup")
    print("2 ---- Login")
    print("3 ---- Show Customers")
    print("4 ---- Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        c = Customer()
        if c.sign_up():
            list1.append(c)

    elif choice == 2:
        userid = input("Enter User ID: ")
        passwordd = input("Enter Password: ")
        flag = 0
        for x in list1:
            if x.login(userid, passwordd):
                flag = 1
                while True:
                    print(f"Welcome {x.name}")
                    print("1 ---- Grocerry Exp.")
                    print("2 ---- Personal Exp.")
                    print("3 ---- Utility Exp.")
                    print("4 ---- Show Expences")
                    print("5 ---- Back to Dashboard")

                    ex_choice = int(input("Enter Expense Choice: "))

                    if ex_choice == 1:
                        amt = int(input("Enter Expense Value: "))
                        x.grocerry_exp(amt)

                    elif ex_choice == 2:
                        amt = int(input("Enter Expense Value: "))
                        x.personal_exp(amt)

                    elif ex_choice == 3:
                        amt = int(input("Enter Expense Value: "))
                        x.utility_exp(amt)

                    elif ex_choice == 4:
                        print(f"{x.grocerry}\n{x.personal}\n{x.utility}\nTotal = {x.grocerry + x.personal + x.utility}")
                    
                    elif ex_choice == 5:
                        break


        if flag == 0:
            print("Cred. Invalid")

    elif choice == 3:   # [obj1, obj2, obj3]
        for d in list1:
            print(d.name)

    elif choice == 4:
        exit()


# Email Duplicatation remove, Password Validation (regex - Regular Expression), Expense Name with Price and total, file (using Json)