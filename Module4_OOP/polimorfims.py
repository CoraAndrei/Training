## 1 clasa papagal, clasa pinguin , la fiecare clasa metode de fly, swim
# class Parrot:
#     def fly(self):
#         print("Parrot can FLy")
#     def swim(self):
#         print("Parrot can't swim")
#
#
# class Penguin:
#     def fly(self):
#         print("Penguin can FLy")
#
#     def swim(self):
#         print("Penguin can't swim")
#
# def flying_test(bird):
#     bird.fly()
# #creare obiecte
# Reggy =Parrot()
# Sasha = Penguin()
#
# #passing object
# flying_test(Reggy)
# flying_test(Sasha)
#
# def swim_test(bird):
#     bird.swim()
# swim_test(Reggy)
# swim_test(Sasha)
#
#
# # poli cu class methods
#
# class Austria():
#     def capital(self):
#         print("Vienna is the capital of Aus")
#     def language(self):
#         print("Austrian is the most spoken L")
#     def status(self):
#         print("Austria is always in a continuu development phase")
# class Germany():
#     def capital(self):
#      print("Berlin is the capital of Aus")
#
#
#     def language(self):
#      print("German is the most spoken L")
#
#
#     def status(self):
#       print("German is not always so pleasent")
#
# obj_Austria = Austria()
# obj_Germany = Germany()
#
# for country in (obj_Austria,obj_Germany):
#     country.capital()
#     country.language()
#     country.status()



#### polimorfims cu functia de len()


print(len("My_Name_IS_Gogo"))
print(len([10,20,30]))

def add(x,y,z = 1):
    return x+y+z
print(add(2,3))
print(add(2,3,4))