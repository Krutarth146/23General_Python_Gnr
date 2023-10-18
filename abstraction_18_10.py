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


#  Join Tuples if similar initial element

que = [(10,20), (10,30), (5,7), (7,5), (5,9,5), (70,7), (7,10)]
# ans = [(10,20,30), (5,7,9), (7,5,10), (70,7)]


[for i in range(len(que)) for j in range(i+1, len(que)) if que[i][0] == que[j][0] for x in que[]]

for i in range(len(que))