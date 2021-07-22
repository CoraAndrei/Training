# class Person():
#     def __init__(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
#     def isEmployee(self):  # check is emp or not
#
#         return False
#     # Inherit sau Subclass lui Person
#
#
# class Employee(Person):
#
#     def isEmployee(self):
#         return True
#
#
# emp = Person('Sergiu')
# print(emp.getName(), emp.isEmployee())
# print('$$$$$$$$')
#
# emp = Employee("Daniel")
# print(emp.getName(), emp.isEmployee())


# class Person(object):
#     def __init__(self,name,cnp):
#         self.name = name
#         self.cnp = cnp
#     def display(self):
#         print(self.name)
#         print(self.cnp)


class Base(object):
    # constructor
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class Child(Base):
    # cons
    def __init__(self, name, age):
        Base.__init__(self, name)  # invocare in interiorul partii de init
        self.age = age

    def getAge(self):
        return self.age


class GrandChild(Child):
    def __init__(self,name,age,address):
        Child.__init__(self,name,age) # imi aduce name si age din Child
        self.address=address
    def getAddress(self):
        return self.address

who_am_i = GrandChild('Gogo',32,'Sopor')
print(who_am_i.getName(),who_am_i.getAge(),who_am_i.getAddress())