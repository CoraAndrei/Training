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
else 
 Statement
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
