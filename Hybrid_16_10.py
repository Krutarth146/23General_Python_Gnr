class A:
    def mA(self):
        print('MA Method Under A Class')


class B(A):
    def mB(self):
        print('MB Method Under B Class')
        

class C(A):
    def mC(self):
        print('MC Method Under C Class')
        

class D(B, C):
    def mD(self):
        print('MD Method Under D Class')
        


d1 = D()
d1.mA()