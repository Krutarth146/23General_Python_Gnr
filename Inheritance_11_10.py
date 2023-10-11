# Multilevel Inheritance

class Swift:
    wheels = 4 

    def __init__(self) -> None:
        self.owner_name = input()

    def show_features(self):
        print('Swift has Good Features')


class Innova(Swift):

    def __init__(self):
        self.price = 1000000

    def Extra_features(self):
        print('Many Features')


class BMW(Innova):

    @classmethod
    def Safety(cls):
        # print('6 Airbags',Swift.wheels)   # 6 Airbags 4
        # print('6 Airbags',BMW.wheels)   # 6 Airbags 4
        print('6 Airbags',cls.wheels)   # 6 Airbags 4

    def Solve_it(self):
        list1 = [10,20,30,40]

        # [(1,2,5,10) , (1,2,4,5,10,20), .....]
        # main = []
        # temp = []
        # for ele in list1:
        #     # temp = []
        #     temp.clear()
        #     for k in range(1,ele+1):
        #         if ele % k == 0:
        #             temp.append(k)
        #     main.append(temp)

        # main = [[k for k in range(1,ele+1) if ele % k == 0] for ele in list1]
        main = {ele : [k for k in range(1,ele+1) if ele % k == 0] for ele in list1}

        # temp.clear()
        return main


mithil = BMW()

mithil.Safety()
mithil.Extra_features()
print(mithil.Solve_it())  # [[1, 2, 5, 10], [1, 2, 4, 5, 10, 20], [1, 2, 3, 5, 6, 10, 15, 30], [1, 2, 4, 5, 8, 10, 20, 40]]
# {10: [1, 2, 5, 10], 20: [1, 2, 4, 5, 10, 20], 30: [1, 2, 3, 5, 6, 10, 15, 30], 40: [1, 2, 4, 5, 8, 10, 20, 40]}