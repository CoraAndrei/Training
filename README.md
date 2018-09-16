# Session 1

## Data Types in Python


Data Type | Data value
------------ | -------------
Integers | 5, 8, 400
Float | 4.3, 5.7, 12.3
String | words, characters
Boolean | True or False
List | [1, 2, 3, 4]  
Dictionaries | {1:'first', 2:'second'}
Tuples | (1,2,3)
Sets | [1, 2, 3]

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

#argv file

print "Name: %s, Age: %d" % ('John', 22)
  
```
</details>


##
### Working with basic arithmetic operators
<details>
 <summary>Click to expand </summary>

```js
import math

#from math import sqrt

a = 5 
b = 4
s = 'string'

print a+b
print type(a+b)
print '\n'

print a/b 
print type(a/b)

print a*b
print type(a/b)

print a%b
print type(a/b)

print '\n'

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

Tuples continued
# more on tuples
print '*' * 60
c = [9999, 333]
a = 1, 2, 3, 4, 5, c
print a
print type(a)
print a[5][0]
 
print '*' * 60
a, b = 1, 2
print a
print b
 
# print '*' * 60
# a, b = 1, 2, 3
 
print '*' * 60
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
#a.add(5, 6)
#len(a)
#a.add((5,6))
#a.add([7,8])
#a.update([7,8])
#a.update()

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

# converting to and from lists
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
#basics
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

#add operation
a['third'] =  4
print a

#update operation
a['third'] = 5
print a

print 'Dictionary keys:', a.keys()
print 'Dictionary values:', a.values()
print 'Dictionary items:', a.items()

```

</details>
