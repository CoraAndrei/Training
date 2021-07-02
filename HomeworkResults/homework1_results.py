#Lists

list1 = [10, 20, 300, 400, 5000, 6000, 500, 30, 40]
# Exercise1:Add item 200 in the third position of list

list1[3] = 200
print("The third position of list is :")
print(list1)

# Exercise2: Print number 6000 within the list

print("The number within the list is:")
print(list1[5])

# Exercise3:Replace number 20 from the list with 900

list1[1]=900
list1.insert(3,200)
print("The list with the replaced number is :")
print(list1)

# Exercise4:Add only the numbers from the following list to the end of list1. list2=[10, 40, 300, 6500]

list2=[10, 40, 300, 6500]
list1.append(list2)
print("The list with added numbers at the end is:")
print(list1)

# Exercise5:Create a new list, named list3, having only one ocurences of any element in list1.   Hint: use set() then list()

list1 = [10, 900, 300, 200, 400, 5000, 6000, 500, 30, 40, 10, 40, 300, 6500]
print("The original list is:")
print(list1)
list3 = set(list1)
print("The list after removing duplicates:")
print(list3)

# Exercise6: Sort the new list3, and print only the elements placed on even positions in the list"   Hint: use list slicing
list3 = [900, 6500, 200, 5000, 10, 40, 300, 400, 6000, 500, 30]
print("The elements placed on even position:")
print(list3[1:10:2])

# Exercise7:
list4 = ['Ana', 'are', 'mere']
list5 = [5, 6, 7, 8]
#     Print message: 'Ana 5 are 67 mere' using list slicing. Hint: Be careful for concatenation of different data types.
message = list4[0] +" "+ str(list5[0]) +" " + list4[1] + " "+  str(list5[1]) + str(list5[2]) +" "+ list4[2]
print( message )


# Tuples/Sets

tuple1 = (1, 2, 3, 4, 5)
#Exercise1: Assign in one line all the elements from tuple1 to variables n1, n2, n3, n4, n5
n1,n2,n3,n4,n5= tuple1
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)

# Exercise2: Based on tuple1, create a new tuple2 containing elements from index 2 and 3 using list slicing
tuple2 = tuple1[2:3:1]
print ("The elements from index 2 and 3 are " )
print(tuple2)

# Exercise3: Is it possible to append a new element at the end of the tuple?
# R: Touples items are unchangeable

# Exercise4:
tuple3 = (5, 4, 5, 3, 2, 1, 10)
#Based on sets, create a new tuple named 'tuple4' without having any duplicated elements
tuple4 = set(tuple3)
print("The tuple after removing duplicates: ")
print(tuple4)


#Dictionaries

dict = {"name": "John", "country": "USA", "born": 1996, "job": "Engineer", "car": "Hyundai Tucson"}

# Exercise1:Print the year when John was born
print("The year when John was born is ")
print(dict["born"])

# Exercise2: Change the country were John is living from 'USA' to 'CAN'.

dict["country"]= 'CAN'
print("The dict with new country is ")
print(dict)

#Exercise3:
dict_list = ['Jack', 'Ana', 'Dan']
#Create a new key named 'child_names' and add dict_list as value


dict['child_names'] = dict_list
print("The dict with new key is: ")
print(dict)

# Exercise4:Delete the job key and print just the keys from the dictionary
del dict['job']
print(dict)
print(dict.keys())
#print(dict.values())
#print(dict.items())

#Exercise5:
#Having the following dict:
new_dict = {"datacamp":{"Deep Learning": "Python", "Machine Learning": "Pandas"},"linkedin":"jobs","nvidia":"hardware"}

#- print value from 'Machine Learning' key.          Hint: dictionary inside another dictionary

print("The value from 'Machine Learning' key is:-")
print(new_dict['datacamp']['Machine Learning'])

#- add a new key 'Test' with value 'Passed' inside 'datacamp' values
new_dict['datacamp']['Test']='Passed'
print("The dictionary with new key-value is:-")
print(new_dict)

#Exercise6:
#Having the following dict:

dict_list = {"datacamp":{"Deep Learning": ['Python', 'Java'], "Machine Learning": ["Pandas", "Keras"]},"linkedin":"jobs","nvidia":"hardware", "numbers": [5, 4, 3, 2, 1]}

# - Delete 'Java' value from inside the dictionary
del (dict_list['datacamp']['Deep Learning'][1])
print("The dictionaty with the deleted value is: ")
print(dict_list)
#- Add number 6 in  the first position of 'numbers' list
dict_list['numbers'].insert(0,6)
print("The 'numbers' list from the dictionary is: ")
print(dict_list)
#- Sort the 'numbers' list and then print the number of elements from the list
dict_list["numbers"].sort()
print("The sorted 'numbers' list is:-")
print(dict_list)

print("The number of elements from the list is:-")
print(len(dict_list["numbers"]))


