# Encapsulation

# class Alto:
#     wheels = 4   # Public Class Variable
#     _insurance_cmp = 'Acko'   # Protected class Variable
#     __price = 1000000   # Private

#     def __init__(self, name) -> None:
#         self.owner = name   # Instance Variable Public

#     def show_details(slf):
#         print(slf.owner)
#         print(f'Alto has Total {Alto.wheels} Wheels and Insurance is {Alto._insurance_cmp}')

#     def show_price(self):
#         print(self.__price)


# Arin = Alto('Arinbhai')
# Arin.show_details()

# Arin.show_price()   # 1000000
# # print(Arin.__price)  # Error
# print(Arin._Alto__price)  #  1000000
# # print(Alto.__price)  #  Error
# print(Alto._Alto__price)  #  1000000




class Alto:
    wheels = 4   # Public Class Variable
    _insurance_cmp = 'Acko'   # Protected class Variable
    __price = 1000000   # Private

    def __init__(self, name) -> None:
        self.owner = name   # Instance Variable Public
        print('Alto Constructor Called')

    def show_details(slf):
        print(slf.owner)
        print(f'Alto has Total {Alto.wheels} Wheels and Insurance is {Alto._insurance_cmp}, Owner is {slf.owner}')

    def show_price(self):
        print(self.__price)


# class Innova : public Alto
class Innova(Alto):

    def __init__(self, owner_name):
        # super().__init__("Bansi")
        print('Innova Constructor Called')
        super().__init__(owner_name)


    def Airbags(self, total_bags):
        self.airbags = total_bags
        # print('Total Airbags are',self.airbags)
        return self.airbags



# Inheritance ----> Inherits features from another class
# Nupur = Alto()


mithil = Innova("Harsh")
# print(mithil.__price)  # Error
# print(mithil._insurance_cmp)  # Acko
# print(mithil.Airbags(6))   # 6
mithil.show_details()