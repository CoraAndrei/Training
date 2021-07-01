## LISTS
list1 = [10, 20, 300, 400, 5000, 6000, 500, 30, 40]

# Exercise1:
# Add item 200 in the third position of list
list1.insert(2, 200)

# Exercise2:
# Print number 6000 within the list
print(list1[6])

# Exercise3:
# Replace number 20 from the list with 900
list1[1] = 900

# Exercise4:
# Add only the numbers from the following list to the end of list1. list2=[10, 40, 300, 6500]
list2 = [10, 40, 300, 6500]
list1.extend(list2)

# Exercise5:
# Create a new list, named list3, having only one occurence of any element in list1.   Hint: use set() then list()
list3 = list(set(list1))

# Exercise6:
# Sort the new list3, and print only the elements placed on even positions in the list"   Hint: use list slicing
list3.sort()

# Exercise7:
# list4 = ['Ana', 'are', 'mere']
# list5 = [5, 6, 7, 8]
# Print message: 'Ana 5 are 67 mere' using list slicing. Hint: Be careful for concatenation of different data types
list4 = ['Ana', 'are', 'mere']
list5 = [5, 6, 7, 8]

print(list4[0:1], list5[0:1], list4[1:2], list5[1:3], list4[2:3])



## DICTIONARIES
dict = {"name": "John", "country": "USA", "born": 1996, "job": "Engineer", "car": "Hyundai Tucson"}

# Exercise1:
# Print the year when John was born.
print(dict["born"])

# Exercise2:
# Change the country were John is living from 'USA' to 'CAN'.
dict["country"] = "CAN"

# Exercise3:
# dict_list = ['Jack', 'Ana', 'Dan']
# Create a new key named 'child_names' and add dict_list as value
dict_list = ['Jack', 'Ana', 'Dan']
dict["child_names"] = dict_list

# Exercise4:
# Delete the job key and print just the keys from the dictionary
dict.pop('job')

# Exercise5:
# Having the following dict: new_dict = {"datacamp":{"Deep Learning": "Python", "Machine Learning": "Pandas"},"linkedin":"jobs","nvidia":"hardware"}
new_dict = {"datacamp":{"Deep Learning": "Python", "Machine Learning": "Pandas"},"linkedin":"jobs","nvidia":"hardware"}
# - print value from 'Machine Learning' key.          Hint: dictionary inside another dictionary
print(new_dict["datacamp"]["Machine Learning"])
# - add a new key 'Test' with value 'Passed' inside 'datacamp' values
new_dict["datacamp"] = {"Test":"Passed"}

# Exercise6:
# Having the following dict: dict_list = {"datacamp":{"Deep Learning": ['Python', 'Java'], "Machine Learning": ["Pandas", "Keras"]},"linkedin":"jobs","nvidia":"hardware", "numbers": [5, 4, 3, 2, 1]}
dict_list = {"datacamp":{"Deep Learning": ['Python', 'Java'], "Machine Learning": ["Pandas", "Keras"]},"linkedin":"jobs","nvidia":"hardware", "numbers": [5, 4, 3, 2, 1]}
# - Delete 'Java' value from inside the dictionary
del dict_list["datacamp"]["Deep Learning"][1]
# - Add number 6 in  the first position of 'numbers' list
dict_list["numbers"].insert(0, 6)
# - Sort the 'numbers' list and then print the number of elements from the list
dict_list["numbers"].sort()
print(len(dict_list["numbers"]))



## TUPLES | SETS
tuple1 = (1, 2, 3, 4, 5)

# Exercise1:
# Assign in one line all the elements from tuple1 to variables n1, n2, n3, n4, n5
n1, n2, n3, n4, n5 = tuple1

# Exercise2:
# Based on tuple1, create a new tuple2 containing elements from index 2 and 3 using list slicing
tuple2 = tuple1[2:4]

# Exercise3:
# Is it possible to append a new element at the end of the tuple?
# Answer: no

# Exercise4:
# tuple3 = (5, 4, 5, 3, 2, 1, 10)
# Based on sets, create a new tuple named 'tuple4' without having any duplicated elements
tuple3 = (5, 4, 5, 3, 2, 1, 10)
tuple4 = tuple(set(tuple3))
print(tuple4)