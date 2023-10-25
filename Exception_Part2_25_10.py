# # raise keyword, User Defined Exception, nzec Error, logging


# list1 = ["10",20,"30",40,"str1",True]

# try:
#     for i in list1:
#         print(i)
#         b = int(i)

# except Exception as err:
# # except ArithmeticError as err:
#     print("str to int Not Possible")   # User Defined Msg
#     print("Computer Generated Error is:",err)

# finally:
#     print(len(list1))

# print("Outside Code")


# -----------------------------------------------

# User Defined Exception

# Step - 1
class ThreeDivisionError(Exception):
    def __init__(self, str):
        print("ThreeDivisionError Exception Called", str)


try:
    num = 67
    sum = 0
    

    while num >0:
        sum += (num % 10)
        num = num // 10

    if sum % 3 == 0:
        print("Possible")
    else:
        raise ThreeDivisionError("It's Error")    # Step - 2  (Forcefully)
        # raise    # Step - 2  (Forcefully)
    

except ThreeDivisionError as err: # Step - 3
    print("Not Divisible by 3",err)

# OutOfMoney, MinimumBalance
# s1 = Student("Manoj")

import logging
import datetime

logging.basicConfig(filename='Transaction_e.log', filemode="a", format='%(asctime)s  %(levelname)s %(message)s')


class OutOfMoney(Exception):
    pass

class MinimumBalance(Exception):
    pass


balance = 50000
def withdraw(amount):
    global balance
    try:
        if amount > balance:
            raise OutOfMoney("Your amount is too high than balance",amount-balance)
        else:
            if (balance - amount) <= 10000:
                raise MinimumBalance()
            
            else:
                balance -= amount
                print('Amount Withdrawed',balance)
    except OutOfMoney:
        logging.warning("Out of Money")
        print("Map ma Revanu")
    
    except MinimumBalance:
        logging.error("Uder the 10000")
        print("Pls Follow Rule")

# withdraw(300)
# withdraw(60000)
# withdraw(60000)
withdraw(45000)


# x = int(input())
# y = int(input())

# print(x+y)


# N-ZEC Error

x, y = input().strip().split()

print(x,y)



# importing module
# import logging
 
# Create and configure logger
logging.basicConfig(filename="newfile1.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
 
# Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")