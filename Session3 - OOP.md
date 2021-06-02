# Session 3
## OOP | Exceptions | Files in Python


# Classes

<details>

 - How to create a class
 - Constructors
 - Self parameter -> reference to the current instance of the class

 
 ```js
import socket


class Server:
    """ Holds all server related operations, regardless of the OS """
    def __init__(self, hostname, procs=2, mem=4):
        """ Constructor.
        Parameters:
            hostname <String> The server's hostname.
            procs: <Int> (optional) Number of processors.
            mem: <Int> (optional) GB of RAM.
        """
        self.hostname = hostname
        self.procs = procs
        self.total_mem = mem
 
        self._load = 0
 
        self._set_system_info()
 
    def print_server_information(self):
        """ Print all server information """
        print "\nServer info follows:"
        print "Hostname: %s" % self.hostname
        print "IP addr: %s" % self.ip
        print "Processor number: %s" % self.procs
        print "Mem: %s" % self.total_mem
        print "Server load: %s" % self._load
 
    def start_process(self, process_name):
        """ Start a new process on the server.
        Parameters:
            process_name: <String> The name of the process to start.
        Return:
            True/False
        """
        process_load = 10
        if process_name == "SA":
            process_load = 50
 
        server_load = self._load + process_load
        if server_load > 120:
            print "Server load is too high. Stop some processes first."
            return False
 
        self._load = server_load
 
        return True
 
    def _set_system_info(self):
        """ Retrieves additional information about this server."""
        self.ip = socket.gethostbyname(self.hostname)
 
 
if __name__ == "__main__":
    # Create object
    linux_server = Server("yahoo.com")
    linux_server.print_server_information()
 
    if linux_server.start_process("SA"):
        print "Started process successfully."
        linux_server.print_server_information()
    else:
        print "Unable to start this process."
    print dir(linux_server)

```

"""
1. Create a class:
    PersonalData:
        + name
        + age
        + print_info()
 
2. Add several PersonalData objects to a list.
     - Find the oldest person
     - Sort the list alphabetically

 ```js
import random
 
 
 class PersonalData:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def print_info(self):
        print "Name: %s" % self.name
        print "age: %s" % self.age
 
if __name__ == "__main__":
    data_list = []
    for i in range(0, 10):
        data_list.append(PersonalData("Name%s" % random.randint(0, 100),
                                      random.randint(18, 65)))
    for p in data_list:
        p.print_info()
 
    print "Find oldest person"
    oldest = data_list[0]
    for data in data_list:
        if oldest.age < data.age:
            oldest = data
 
    oldest.print_info()
 
    data_list = sorted(data_list, key=lambda a: a.name)
    for data in data_list:
        data.print_info()
 ```

</details>

# Inheritance

 ```js
from example2 import Server
 
# class Server:
#    def __init__(self, hostname, procs=2, mem=4):
#        self.hostname = hostname
#        self.procs = procs
#        self.total_mem = mem
#        ...
 
 
class CoreServer(Server):
    def __init__(self, hostname):
        self.sa_release = "Isaac"
 
        Server.__init__(self, hostname)
 
    def start_process(self, process_name):
        print "CoreServer:start_process"
        return Server.start_process(self, process_name)
 
    def start_services(self):
        if self.start_process("SA"):
            print "Starting services on %s" % self.hostname
        else:
            print "Unable to start SA due to high server load."
 
 
core = CoreServer("hp.com")
print dir(core)
core.print_server_information()
 
core.start_services()
core.print_server_information()
 ```

 ```js
 
## Special methods
# Overwrite default/built in methods
 
class PersonalData:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def __str__(self):
        return "name: %s " % self.name + "age: %s" % self.age
 
    def __cmp__(self, other):
        if self.name == other.name:
            return 0
        else:
            return 1
 
 
data1 = PersonalData("Titus", "25")
print data1
 
data2 = PersonalData("Titus", "25")
 
print data1 == data2
```

```js
Static variables and methods
# decorators, static, static methods
 
 
class PersonalData:
    employee_id = 0
 
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
        PersonalData.employee_id += 1
 
    def print_info(self):
        print "name: %s" % self.name
        print "age: %s" % self.age
 
    @staticmethod
    def get_free_id():
        return PersonalData.employee_id + 1
 
 
print PersonalData.employee_id
data1 = PersonalData("Titus", "25")
print PersonalData.employee_id
print PersonalData.get_free_id()
```

# Encapsulation

 - restricted acces to methods and variables
 
 ```js
 class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
 ```
 
 
# Polymorphism

 - abbility to use common methods for different classes

```js
class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
```



# Homework

1. Create a class to represent complex numbers. Implement methods to add,
subtract and multiply two complex numbers

2. a) Create a class Floor that represent the floor in a building:
Floor:
+ size: square meters inside the floor
+ floor_nr: the number this floor has

b) Create a class Building that represents a building a city:
Building:
+ name: the name of the building
+ base_size: squere meters of the ground floor
+ max_floor: the maximum number of floors
+ floors: a list of all the floors (list of Floor objects) inside
the building
+ add_floor(objFloor): adds a floor in the building you cannot add
a floor with a larger size over a floor with
a smaller size this method should also give the
floor it's floor_nr

c) Create a class City that represents a city with buildings and floors
City:
+ name: name of the city
+ size: the square meters of the city
+ buildings: a list of Building objects inside the city
+ add_building: adds a building inside the buildings list
make sure the total buildings base size is not
greater than 50% of size.

d) Create an algorithm that creates a city and populates it with buildings
until it reaches the maximum size, and populates the buildings with floors.

3. 21. Implement a simple 21 card game. Classes:
Deck
+ constructor: population, calls shuffle
+ shuffle()
+ draw_card()

Hand:
+ cards
+ sum

Player
+ draw()

AI Player
+ draw()

Card
+ color
+ value
_str_

Known facts:

there is no special rule when adding cards
the card values are from 1 to 11: A=1, J=Q=K=10
the AI stop when sum is higher than 18
you are asked to draw cards until you decide to stop.

  
 
 
## PyObject
Atribute | Values
------------ | -------------
Type | integer
Refcount | 2
Value | 300
```js
x = 300
y = 300
print id(x)
print id(y)
print x is y
 > 28501818
 > 28501818
 > True
```
## Garbage collector
- Object refCount = 0    -> Object is deleted and the memory is deallocated
##
### Using **print** function to display the type of a variable:
<details>
 <summary>Click to expand</summary>
 
 ```js
- print "True is of type:", type(True)
  - True is of type: <type 'bool'>
- print "'ion' is of type:", type('ion')
  - ion is of type: <type 'str'>
- print "100 is of type:", type(100)
  - 100 is of type: <type 'int'>
- print "3.14 is of type:", type(3.14)
  - 100 is of type: <type 'float'>
- print "[1, 2, 3] is of type:", type([1, 2, 3])
  - [1, 2, 3] is of type: <type 'list'>
- print "(1, 2, 3) is of type:", type((1, 2, 3))
  - (1, 2, 3) is of type: <type 'tuple'>
  
- print "{1, 2, 3} is of type:", type({1, 2, 3})
  - {1, 2, 3} is of type: <type 'set'>
- print "{1: 2}) is of type:", type({1: 2})
  - {1: 2}) is of type: <type 'dict'>
  
- print type(True)
  - <type 'bool'>
- print type(1)
  - <type 'int'>
  
- print type(True) == type(1)
  - False
- print True == 1
  - True
  
 ```
 
</details>

##
### Reading keyboard input
<details>
 <summary> Click to expand </summary>
 
```js
name = raw_input("Give me a name: ")
print "Your name is: %s" % name

value1= raw_input("Give me a value: ")
value2= raw_input("Give me anoter name: ")
print 'The sum is: %s' % value1 + value2

value1= int(raw_input("Give me a value: "))
value2= int(raw_input("Give me anoter name: "))
sum = int(value1) + int(value2)
print 'The sum is: %d' % sum

ch = raw_input("Enter a character: ")[0]
print ch

ch = raw_input("Enter a character: ")[0:6]
print ch

result = eval(raw_input("Give me an expression: "))
print result

//argv file

print "Name: %s, Age: %d" % ('John', 22)  
```

</details>

##
### Working with basic arithmetic operators
<details>
 <summary> Click to expand </summary>
 
```js
import math
#from math import sqrt

a = 5 
b = 4
s = 'string'

print a+b
print type(a+b)

print a/b 
print type(a/b)
//print a//b

print a*b
print a%b
print type(a/b)

c = 2.5
print type(c*a)
print math.sqrt(b)

print str(a) + s
print s * 5

> Operations with Strings
s = 'hi'
c = 5

print s[1]
print len(s)
print s + 'there'

print 'Value of c is:' + c
print 'Value of c is:' + str(c)
print 'value of c is: %d ' % c
```

</details>

##
### Working with lists
<details>
 <summary> Click to expand </summary>
 
```js
>Functions 'append, extend and insert'
a = [1, 2, 3, 4, 5]
b = a

print a
print type(a)

a.append(6)
print a
a.append(['ana', 'are', 'mere']) #use also extend to see the list length difference
print a
print len(a)

a.insert(1, 'new')
print a

#time_difference_file

>Functions 'pop and remove'
a = [1, 2, 3, 4, 5, 1]
a.pop(1) #use also remove to see the difference
print a

>Function index
print a.index(2)

>Function reverse
a.reverse()
print a

>Function sort
a.sort()
print a

>Slicing
a = [1, 2, 3, 4, 5]
print a[2:4]
print a[:2]
print a[2:]

b = a 
b[1] = 'elem'
print b
print a
b= a[:]
b[1] = 2
print '\n', b
print a
```

</details>

##
### Working with tuples
<details>
 <summary> Click to expand </summary>
 
```js
a = (1)
print type(a)
a = (1,)
print type(a)
a = (1, 2, 2, 2, 3, 4, 2)
print 'a =', a
print '2 apare de %s ori in tupla' % a.count(2)
print '4 apare in tupla pe pozitia %d' % a.index(4)
 
my_list = [1, 2, 3]
my_set = {4, 5, 6}
print tuple(my_list)
print tuple(my_set)
 
print '*' * 60
a = [1, 2, 3, 4]
b = (5, 6, 7, a)
print b

a.append(9)
print b
c = [9999, 333]
a = 1, 2, 3, 4, 5, c
print a
print type(a)

print a[5][0]
a, b = 1, 2
print a
print b
 
// a, b = 1, 2, 3
 
a = (11, 22, 33)
a1, a2, a3 = a
print a1
print a2
print a3
# a[0] = 1
```

</details>

##
### Working with sets
<details>
 <summary> Click to expand </summary>
 
```js
a = {1, 2, 3}
b = set([1,2,3])
print type(a), type(b)

a.add(4)
print 'a =', a

//a.add(5, 6)
//len(a)
//a.add((5,6))
//a.add([7,8])
//a.update([7,8])
//a.update()

b = a
b.add(9)
print a,b

b = a.copy()
b.add(10)
print a,b
a.remove(1)
a.pop

#Operation between two sets
diff = b.difference(a)
print 'b-a: ', diff

uni = a.union(b)
print 'a+b: ', uni

inter = a.intersection(b)
print 'a intersected with b: ', inter

// converting to and from lists
my_list = [1, 2, 3]
my_set = set(my_list)
print my_set

my_new_list = list(my_set)
print my_new_list
```

</details>

##
### Working with dictionaries
<details>
 <summary> Click to expand </summary>
 
```js
//basics
a  = {'key': 'value'}
print a
print type(a)

a[1] = 10
print a

a['list'] = [1, 2, 3]
a[1, 2] = (1,2)   #tuple as a key
print a

a[[1, 2]] = [1, 2, 3]   #list as a key
print a
a  = {'first': 'element', 1: 4, 'third': 5, (1, 2): None, 'testing': 'another one'}
print a

> Operations with dictionaries
#delete operation
del a['third']
print a

//add operation
a['third'] =  4
print a

//update operation
a['third'] = 5
print a

print 'Dictionary keys:', a.keys()
print 'Dictionary values:', a.values()
print 'Dictionary items:', a.items()
```

</details>

##
### Working with datetime
<details>
 <summary> Click to expand </summary>
 
```js
# datetime features
import datetime
import time
 
current_date = datetime.datetime.now()
 
print type(current_date)
print current_date

tday = datetime.date.today()
print(tday.weekday())
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)
print tday + tdelta

my_custom_date = datetime.datetime(2000, 12, 12, 14, 59, 59)
print type(current_date)
print my_custom_date

t1 = datetime.datetime.now()
print t1
time.sleep(5)
t2 = datetime.datetime.now()
print t2
dif = t2 - t1
print dif
print type(dif)

from datetime import datetime as dt
 
now = dt.now()
print now
 
# printing date in a custom format
my_now = now.strftime('%A, %d %B %Y')
print my_now
 
# constructing a datetime object from a string
str_date = "22/03/2012 - 09:57"
new_date = dt.strptime(str_date, "%d/%m/%Y - %H:%M")
print new_date
print type(new_date)
```

</details>
