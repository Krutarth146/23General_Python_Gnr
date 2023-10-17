class RBI():
    def repoRate(self, reposrate):
        self.repo = reposrate
        print('RBI reporate Unchanged',self.repo)

class Kotak(RBI):


    def repoRate(self,rs,name):
        super().repoRate(4)
        self.reporate = 9.0
        print('Kotak reporate Unchanged',self.reporate, rs, name)

    def InterestRate(self):
        print(4)

    def InterestRate(self, rate):
         print(rate)


mithil = Kotak()

mithil.repoRate(50000,"Aman")


# ---------------------------------------------------

print(len("Mithil"))   # 6
print(len([10,90,203,0]))  # 4
print(min([10,90,20,34]))
print(sum([10,90,20,34]))
print(all([10,90,20,0]))
print(any([10,90,20,0]))


# 0 '' [] False None

# 3 -10 [10,20] True

class Royal(): 
    def Techno(obj):
        obj.name = "Hiren"
        print("Hello")


class Aakash():
    def Techno(obj):
        obj.id = 90
        print('Ram')


for obj in [Royal(), Aakash()]:
    obj.Techno()



#  Join Tuples if similar initial element

que = [(10,20), (10,30), (5,7), (7,5), (5,9,5), (70,7), (7,10)]
ans = [(10,20,30), (5,7,9), (7,5,10), (70,7)]