## LISTS
print('LISTS')
list1 = [10, 20, 300, 400, 5000, 6000, 500, 30, 40]

#Exercise1: Add item 200 in the third position of list
list1.insert(2, 200)
print(list1)

#Exercise2:  Print number 6000 within the list
print(list1[6])

#Exercise3: Replace number 20 from the list with 900
list1[1]=900
print(list1)

#Exercise4: Add only the numbers from the following list to the end of list1. list2=[10, 40, 300, 6500]
list2 = [10, 40, 300, 6500]
list1.extend(list2)
print(list1)

#Exercise5: Create a new list, named list3, having only one occurences of any element in list1.
singleoccurences=set(list1)
list3=[]
list3.extend(singleoccurences)
print(list3)

#Exercise6: Sort the new list3, and print only the elements placed on even positions in the list"
list3.sort()
print(list3)
print(list3[0:11:2])

#Exercise7: Print message: 'Ana 5 are 67 mere' using list indexes. Hint: Be careful for concatenation of different data types.
list4 = ['Ana', 'are', 'mere']
list5 = [5, 6, 7, 8]
print(list4[0] + ' ' + str(list5[0]) + ' ' + list4[1] + ' ' + str(list5[1]) + str(list5[2]) + ' ' + list4[2])

#DICTIONARIES
print('DICTIONARIES')
dict={"name": "John", "country": "USA", "born": 1996, "job": "Engineer", "car": "Hyundai Tucson"}

#Exercise1: Print the year when John was born.
print(dict['born'])

#Exercise2:  Change the country were John is living from 'USA' to 'CAN'.
dict['country'] = 'CAN'
print(dict)

#Exercise3:Create a new key named 'child_names' and add dict_list as value
dict_list = ['Jack', 'Ana', 'Dan']
dict['child_names'] = dict_list
print(dict)

#Exercise4: Delete the job key and print just the keys from the dictionary
del dict['job']
print(f"Dict has the values: '{dict.keys()}")

#Exercise5:    Having the following dict:
#    - print value from 'Machine Learning' key.          Hint: dictionary inside another dictionary
#    - add a new key 'Test' with value 'Passed' inside 'datacamp' values
new_dict = {"datacamp": {"Deep Learning": "Python", "Machine Learning": "Pandas"}, "linkedin": "jobs", "nvidia": "hardware"}
print(new_dict['datacamp']['Machine Learning'])

new_dict['datacamp']['Test'] = 'Passed'
print(new_dict)

#Exercise6:     Having the following dict:
#    - Delete 'Java' value from inside the dictionary
#    - Add number 6 in  the first position of 'numbers' list
#    - Sort the 'numbers' list and then print the number of elements from the list
dict_list = {"datacamp":{"Deep Learning": ['Python', 'Java'], "Machine Learning": ["Pandas", "Keras"]},"linkedin":"jobs","nvidia":"hardware", "numbers": [5, 4, 3, 2, 1]}
dict_list['datacamp']['Deep Learning'].remove('Java')
print(dict_list)

dict_list['numbers'].insert(0, 6)
print(dict_list)

dict_list['numbers'].sort()
print(dict_list)
print(len(dict_list['numbers']))

# TUPLES | SETS
print('TUPLES | SETS')
tuple1 = (1, 2, 3, 4, 5)
#Exercise1:  Assign in one line all the elements from tuple1 to variables n1, n2, n3, n4, n5
n1, n2, n3, n4, n5 = tuple1
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)

#Exercise2: Based on tuple1, create a new tuple2 containing elements from index 2 and 3 using list slicing
tuple2 = tuple1[2:4]
print(f'tuple2 is: {tuple2}')

#Exercise3:     Is it possible to append a new element at the end of the tuple?
print('No, tuples are immutable and we cannot change, add or remove items after the tuple has been created.')

#Exercise4: Based on sets, create a new tuple named 'tuple4' without having any duplicated elements
tuple3 = (5, 4, 5, 3, 2, 1, 10)
tuple4 = tuple(set(tuple3))
print(f'tuple4 is: {tuple4}')
