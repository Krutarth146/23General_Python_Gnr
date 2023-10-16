class Bank:
    def __init__(self, name1 = None, year = None):
        self.name = name1
        self.b_year = year
        self.balance = 6000
        print('Bank Con. Called')

    # setattr
    def setAccount(self, new_name, year):
        self.name = new_name
        self.b_year = year
        self.manoj = 0

    # getattr
    def printName(self):
        return self.name, self.b_year, self.balance
    
    def Cricket(self):
        print('Bank Cricket')
    
    @staticmethod
    def Example():
        # a1 = arr.array('i', [10,20,30,40,])
        # print(a1) 
        # list1 = [56,90,34,23]
        # a1.fromlist(list1)
        # print(a1) 
        # a1[0] = 900
        # print(a1)    # array('i', [900, 20, 30, 40, 56, 90, 34, 23])

        print(type(a1))   # <class 'array.array'>

        a1 = a1.tolist()
        print(type(a1))   # <class 'list'>
        # print( 
        # a1 = arr.array('u', ['b','x','z','w'])
        # print(a1) 


class Zerodha:
    def __init__(self) -> None:
        self.shares = 900
        print('Zerodha Con. Called')

    def Cricket(self):
        print('Zerodha Cricket')

    def printer(self):
        print('Zerodha Class Printer Method', self.shares)
    


class Person(Bank, Zerodha):   # MRO 
    def __init__(self) -> None:
        super().__init__()
        Zerodha.__init__(self)
        print('Person Class Con. Called')

    def CreatAccount(self):
        '''This is Person Class which is inherited from Bank & Zerodha'''
        self.name = None
        Zerodha().Cricket()

    def Deposit(self):
        print('Deposit Method Under Person Class')

    def Tr(self):
        sb = Zerodha()
        sb.Cricket()

    def Cricket(self):
        Zerodha().Cricket()
        Bank().Cricket()


harsh = Person()

harsh.Cricket()   # Bank Cricket

list1 = [Bank(), Zerodha()]

# Bank.Cricket()   # Class Method
# Bank().Cricket()

# print(list1)   # [<__main__.Bank object at 0x0000023D396D7CA0>, <__main__.Zerodha object at 0x0000023D396D7C40>]
# for k in list1:
#     k.Cricket()

harsh.Cricket()