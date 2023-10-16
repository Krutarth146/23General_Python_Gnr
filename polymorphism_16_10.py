# Poly ---> Many
# Morph ---> Forms

# right ----> right - wrong , left - right

# class RBI():
#     def repoRate(self):
#         self.reporate = 9.0
#         print('reporate Unchanged',self.repoRate)

# class Kotak():
#     pass
#     # def repoRate(self):
#     #     self.reporate = 9.0
#     #     print('reporate Unchanged',self.repoRate)

def repoRate(reporate):
        
        print('reporate Unchanged upper',reporate)

def repoRate():
    reporate = 98
    print('reporate Unchanged lower',reporate)


repoRate()
# repoRate(45)   # Error


class RBI():
    def repoRate(self, reposrate):
        self.repo = reposrate
        print('RBI reporate Unchanged',self.repo)

class Kotak(RBI):


    def repoRate(self,rs,name):
        self.reporate = 9.0
        print('Kotak reporate Unchanged',self.reporate, rs, name)

    def InterestRate(self):
        print(4)

    def InterestRate(self, rate):
         print(rate)



arin = Kotak()
mayur = Kotak()
arin.repoRate(10, 'Manoj')   # Method Overriding
# arin.repoRate(10)

# arin.InterestRate()
arin.InterestRate(10)   # Method Overloading


num1 = 90
num2 = 80
num3 = int(input())

print(num1 + num2 + num3) 

# print(arin + mayur)



# Operator Overloading
class Student():
    def __init__(self, a,b):
          self.a = a
          self.b = b

    def __add__(self, manoj):   # Magic Methods
        return self.a + manoj.a
    

    def __lt__(self, manoj):   # Magic Methods
        return self.a < manoj.a

    def __ge__(self, manoj):   # Magic Methods
        return self.a >= manoj.a


mithil = Student(10,20)
keshav = Student(30,40)

# print(mithil.sum1(keshav))
print(mithil + keshav)
print(mithil < keshav)
print(mithil >= keshav)


#['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', 
#'__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', 
#'__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', 
#'__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', 
#'__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__',
#'__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', 
#'__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', 
#'__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__',
#'__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 
#'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']