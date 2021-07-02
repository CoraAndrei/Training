
"""
## LISTS
```js
    list1 = [10, 20, 300, 400, 5000, 6000, 500, 30, 40]

Exercise1:
    Add item 200 in the third position of list

Exercise2:
    Print number 6000 within the list

Exercise3:
    Replace number 20 from the list with 900

Exercise4:
    Add only the numbers from the following list to the end of list1. list2=[10, 40, 300, 6500]

Exercise5:
    Create a new list, named list3, having only one occurences of any element in list1.   Hint: use set() then list()

Exercise6:
    Sort the new list3, and print only the elements placed on even positions in the list"   Hint: use list slicing

Exercise7:
    list4 = ['Ana', 'are', 'mere']
    list5 = [5, 6, 7, 8]
    Print message: 'Ana 5 are 67 mere' using list slicing. Hint: Be careful for concatenation of different data types.

```

## DICTIONARIES
```js
    dict={"name": "John", "country": "USA", "born": 1996, "job": "Engineer", "car": "Hyundai Tucson"}


Exercise1:
    Print the year when John was born.

Exercise2:
    Change the country were John is living from 'USA' to 'CAN'.

Exercise3:
    dict_list = ['Jack', 'Ana', 'Dan']
    Create a new key named 'child_names' and add dict_list as value

Exercise4:
    Delete the job key and print just the keys from the dictionary

Exercise5:
    Having the following dict: new_dict = {"datacamp":{"Deep Learning": "Python", "Machine Learning": "Pandas"},"linkedin":"jobs","nvidia":"hardware"}
    - print value from 'Machine Learning' key.          Hint: dictionary inside another dictionary
    - add a new key 'Test' with value 'Passed' inside 'datacamp' values

Exercise6:
    Having the following dict: dict_list = {"datacamp":{"Deep Learning": ['Python', 'Java'], "Machine Learning": ["Pandas", "Keras"]},"linkedin":"jobs","nvidia":"hardware", "numbers": [5, 4, 3, 2, 1]}
    - Delete 'Java' value from inside the dictionary
    - Add number 6 in  the first position of 'numbers' list
    - Sort the 'numbers' list and then print the number of elements from the list

```

## TUPLES | SETS
```js
    tuple1 = (1, 2, 3, 4, 5)


Exercise1:
    Assign in one line all the elements from tuple1 to variables n1, n2, n3, n4, n5

Exercise2:
    Based on tuple1, create a new tuple2 containing elements from index 2 and 3 using list slicing

Exercise3:
    Is it possible to append a new element at the end of the tuple?

Exercise4:
    tuple3 = (5, 4, 5, 3, 2, 1, 10)
    Based on sets, create a new tuple named 'tuple4' without having any duplicated elements

 ```
"""
print('*****************************************************')
list1 = [10, 20, 300, 400, 5000, 6000, 500, 30, 40]
print(list1)

## LISTS
#Exercise 1
print('*****************************************************')
print('Exercise 1')
list1.insert(2, 200)
print(list1)

#Exercise 2
print('*****************************************************')
print('Exercise 2')
print(list1[6])

#Exercise 3
print('*****************************************************')
print('Exercise 3')
list1[1] = 900
print(list1)

#Exercise 4
print('*****************************************************')
print('Exercise 4')
list2=[10, 40, 300, 6500]
list1.extend(list2)
print(list1)

#Exercise 5
print('*****************************************************')
print('Exercise 5')
list3_set = set(list1)
print(list3_set)

list3 = list(list3_set)
print(list3)

#Exercise 6
print('*****************************************************')
print('Exercise 6')
list3.sort()
print(list3)
print(list1)
print(list1[1:14:2])

#Exercise 7
print('*****************************************************')
print('Exercise 7')
list4 = ['Ana', 'are', 'mere']
list5 = [5, 6, 7, 8]
print(list4[0] +" "+ str(list5[0]) + " " + list4[1] + " " + str(list5[1]) + str(list5[2]) + " " + list4[2])

## DICTIONARIES
dict={"name": "John", "country": "USA", "born": 1996, "job": "Engineer", "car": "Hyundai Tucson"}

#Exercise 1
print('*****************************************************')
print('Exercise 1')
print(dict["born"])


#Exercise 2
print('*****************************************************')
print('Exercise 2')
dict["country"] = "CAN"
print(dict["country"])

#Exercise 3
print('*****************************************************')
print('Exercise 3')
dict_list = ['Jack', 'Ana', 'Dan']
dict['child_names'] = dict_list
print(dict)

#Exercise 4
print('*****************************************************')
print('Exercise 4')
del dict['job']
print(dict)

#Exercise 5
print('*****************************************************')
print('Exercise 5')
new_dict = {"datacamp":{"Deep Learning": "Python", "Machine Learning": "Pandas"},"linkedin":"jobs","nvidia":"hardware"}
print(new_dict['datacamp']['Machine Learning'])
new_dict['datacamp']['Test'] = 'Passed'
print(new_dict)

#Exercise 6
print('*****************************************************')
print('Exercise 6')
dict_list = {"datacamp":{"Deep Learning": ['Python', 'Java'], "Machine Learning": ["Pandas", "Keras"]},"linkedin":"jobs","nvidia":"hardware", "numbers": [5, 4, 3, 2, 1]}
del dict_list['datacamp']['Deep Learning'][1]
print(dict_list)

## TUPLES | SETS
#Exercise 1
print('*****************************************************')
print('Exercise 1')
tuple1 = (1, 2, 3, 4, 5)
n1, n2, n3, n4, n5 = tuple1
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)

#Exercise 2
print('*****************************************************')
print('Exercise 2')
tuple2 = tuple1[2:4:1]
print(tuple2)

#Exercise 3
print('*****************************************************')
print('Exercise 3')
print('Is it possible to append a new element at the end of the tuple?')
print('No tuples cannot be changed.')

#Exercise 4
print('*****************************************************')
print('Exercise 4')
tuple3 = (5, 4, 5, 3, 2, 1, 10)
tuple3_set = set(tuple3)
print(tuple3_set)
tuple4 = tuple(tuple3_set)
print(tuple4)

