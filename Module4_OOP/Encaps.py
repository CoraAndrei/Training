# class Student():
#     def __init__(self):
#        self._age =0
#
#     @property
#     def age(self):
#          return self._age
#     @age.setter
#     def age(self,age):
#         self._age=age
#
#
# s = Student()
# print(s.age)
#



# class example_of_encapsulation:
#     _protected = 'protected'
#     __private = 'privare'
#     public = 'public'
# # print(dir(example_of_encapsulation))
#
# print(example_of_encapsulation.public)
# print(example_of_encapsulation._protected)
# print(example_of_encapsulation.private)


# class Computer:
#     def __init__(self):
#         self.__max_price = 1000
#
#     def sell(self):
#         print(f"Selling Price:{self.__max_price}")
#
#     def setMaxPrice(self, price):
#         self.__max_price = price
#
#         # show sell price
#
#
# c = Computer()
# c.sell()
#
# # change the price
# c.setMaxPrice(999)
# c.sell()


#Class Masina, var =viteza maxima ,metoda ca sa definesc doua masini (audi, bmw), total = aduna vitezele masinilor

class Masina():
    def __init__(self,viteza_maxima):
        self.viteza_maxima=viteza_maxima

    def __add__(self, other):
        return self.viteza_maxima + other.viteza_maxima
audi = Masina(51)
bmw = Masina(49)
total_viteza = audi + bmw
print(f"Viteza combinata: {total_viteza}")




# alt exemplu
class Area:
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print("Rectangle: ",(a*b))
        elif a!=None:
            print("square:",(a*a))
        else:
            print("No input")
object1=Area()# 0 input
object1.find_area(10) #100
object1.find_area(10,20) # 10x20=200