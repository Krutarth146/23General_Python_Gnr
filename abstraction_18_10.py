# Abstarction 


# to Abstarct ----> To hide bussiness Logic

# Abstarction / Data Hiding ()  ----> Diffrent


# Data Abstarction
#     - Abstarct Class
#         - Abstarct Method

# Abstarct Method

from abc import ABC,abstractmethod

class RBI(ABC):

    @abstractmethod
    def After4():
        # Empty Code
        pass

    @abstractmethod
    def After5():
        # Empty Code
        pass

    def get_interstRates(self, interest):   # Concreate Methods
        self.int = interest
        print('Interest Rates are:',self.int)


class Kotak(RBI):
    def __init__(self, num1=None, num2 = None):
        self.num1 = num1
        self.num2 = num2

    def After4(self):
        print("Kotak Bank Nasta")

    def After5(self):
        print('Security Check')

    
    


class SBI(RBI):
    def After4(self):
        print('Software Updation')

    def After5(self):
        print('Passbook Printing')


# yash = RBI()

nupur = Kotak()
mithil = SBI()
nupur.After4()
mithil.After4()
mithil.After5()

mithil.get_interstRates(2.5)
nupur.get_interstRates(4)





# -------------------------------------------------------------------------------
#  Join Tuples if similar initial element

que = [(10,20), (10,30), (5,7), (7,5), (5,9,5), (70,7), (7,10)]
# ans = [(10,20,30), (5,7,9), (7,5,10), (70,7)]


# [ for i in range(len(que)) for j in range(i+1, len(que)) if que[i][0] == que[j][0]]

x = list(set([j[0] for j in que]))

main = []
for i in x:
    temp = []
    count = 0
    for j in range(len(que)):
        if i == que[j][0]:
            count+=1
            temp.extend(que[j])
        if count == 0:
            temp.extend(que[j])
    if len(temp) != 0:
        main.append(set(temp))

print(main)



dev = [list({v for subtup in list1 if subtup[0] == k for v in subtup}) for k in start]
print(dev)   # [[90, 5, 6, 7], [9, 5, 6]]


# ------------------------------------


tup1 = ((1,9,4), (8,3,2), (9,1,2))
k = 4

ans = ((5,13,8), (12,7,6), (13,5,6))


# --------------------------------------


# Encryption - Decryption

# Jalp Panchal ----> lXIM XXXXXX

# capital ---> +2 (Small)   C --> e
# small   ---> -3 (Capital)  # c ---> Z

print(ord('A'))   # 65

print(chr(ord('A') + 2))   # C