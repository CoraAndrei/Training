# Session 2
## Conditionals | Loops | Modules in Python


##
## Python Conditions and IF stataments
 - Python supports the usual logical conditions from mathematics:
 
 ```js
 Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
```

##
- Python if Statement Syntax:
- Python relies on indentation


```js
if expression
 Statement
```

```js
t = 3
if t < 4:
   print ('That's True!')
```
##
```js
if expression
 Statement
else 
 Statement
```

```js
t = 3
if t < 4:
   print ('That's True!')
else:
   print ('Not True!')
```

- 'elif' expression

```js
x = 5
if x < 0:
   x = 0
   print('Negative changed to zero')
elif x == 0:
   print('Zero')
elif x == 1:
   print('Single')
else:
   print('More')
```

##
## Range function

- used when iterating over a sequence of numbers: range()
```js
for i in range(5):
    print(i)
```

```js
range(start, stop, step)
range(5, 10) -> 5, 6, 7, 8, 9
range(0, 10, 3) -> 0, 3, 6, 9
```

##
## For statements

- used for iterating over items of any sequence

```js
for val in sequence:
    instructions in for block
```

```js
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

```js
# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    if val % 2 == 0:
       sum = sum + val

print("The sum is ", sum)
```

