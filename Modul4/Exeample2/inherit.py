# class Person(object):
#
#     def __init__(self, name):  # constructor
#         self.name = name
#
#     def getName(self):  # To Get Name
#         return self.name
#
#     def isEmployee(self):  # Check is emp or not
#         return False
#
#
# # Inherit sau Subclasa lui Person:
# class Employee(Person):
#
#     def isEmployee(self):
#         return True
#
#
# # Actual Code
#
# # CAZ 1
# emp = Person('Sergiu')
# print(emp.getName(), emp.isEmployee())  # Sergiu , False
# print("$$$$$$$$$ Person $$$$$$$$$")
#
# print("$$$$$$$$$ Employee $$$$$$$$$")
#
# #CAZ 2
# emp = Employee("Daniel")
# print(emp.getName(), emp.isEmployee())  # Daniel , True


# Parrent Class
# class Person(object):
#     def __init__(self, name, cnp):
#         self.name = name
#         self.cnp = cnp
#
#     def display(self):
#         print(self.name)
#         print(self.cnp)
#
#
# # Child
#
# class Employee(Person):
#     def __init__(self, name, cnp, pozitie, salariu):
#         self.pozitie = pozitie
#         self.salariu = salariu
#
#         # invok __init__ parent class
#
#         Person.__init__(self, name, cnp)
#
#
# angajat = Employee('Andreea', 123432, 'MANAGER PESTE QA', 666666)
#
# angajat.display()


class Base(object):
    # Constructor
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class Child(Base):
    # Con
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    def getAge(self):
        return self.age


class GrandChild(Child):
    #
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    def getAddress(self):
        return self.address


who_am_i = GrandChild('Gogo', 32, 'Sopor')
print(who_am_i.getName(), who_am_i.getAge(), who_am_i.getAddress())
