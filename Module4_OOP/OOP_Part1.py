# class HUMAN:
#     human_behaviour = "Walk"
#     def __init__(self,age,name):
#         self.age = age
#         self.name=name
#     def print_age(self):
#         print(f'Age is {self.age}')
#     def print_name(self):
#         print(f'Age is {self.name}')
#
#     def print_behaviour(self,sound):
#         print(f'Name is {self.name} and age is {sound}')
#
#
# Person1 =HUMAN(12,"Mike") # a fost creat obiectul Person1
# # print(Person1.name)
# # print(Person1.age)
# # print(Person1.print_age())
# # print(Person1.print_name()) # printare metoda din interiorul clasei
# # print(Person1.human_behaviour)
# Person1.print_behaviour("Talk")
#
# # class SUMA:
#
# #     def suma(self, a, b):
# #         print(f'Sum of a+b is:  {a+b}')
# # a=3
# # b=5
# # s=SUMA()
# # s.suma(a,b)
#
#


# class Car:
#     def __init__(self,color,mileage):
#         self.color = color
#         self.mileage=mileage
#     def print_color_and_mileage(self):
#         print(f"Car color is {self.color} and mileage is{self.mileage}")
# Dacia = Car('red', 22000)
# Hyndai = Car('Black',5000)
#
# for car in (Dacia,Hyndai):
#     print(f"Car color is {car.color} and mileage is{car.mileage}")
# Dacia.print_color_and_mileage()


# clasa noua cu liste si dictionare

class Exercises:
    def __init__(self,list1,dict1):
        self.list1= list1
        self.dict1 =dict1

    def sort_list(self):
        self.list1.sort()
        return self.list1
        #print(f"The new list is {self.list1.sort()}")
    def print_dictionaries_keys(self):
        print(f'The dictionary is : {self.dict1.keys()}')
Variables = Exercises([5,4,3,2,1], {'a':1, 'b':2})
list2 = Variables.sort_list()
print(f'New sorted list is: {list2}')
Variables.print_dictionaries_keys()