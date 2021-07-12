# Exercises_part1
# 1. Write the syntax of simple if, elif, else statement and print whatever you like
weather = 'sunny'
print('Exercise part 1 #1 *****************')
if weather == 'sunny':
    print('Get some sunscreen on!')
elif weather == 'cloudy':
    print('Take an umbrella')
elif weather == 'windy':
    print('Take a jacket')
else:
    print('Stay inside!')

# 2. Write if statement to check if a person is over the age of 18 or not. print out the the age and a message.
age = 1
print('Exercise part 1 #2 *****************')
if age > 18:
    print('The person is over 18')
else:
    print('The person is not over 18')

# 3 Compare what number is greater between a , b and c (Hint: this exercise will need if ,
# elif, else, and , < , > )
a = 10
b = 15
c = 30
print('Exercise part 1 #3 *****************')
if a > b and a > c:
    print('a is greater than b and c')
elif b > a and b > c:
    print('b is greater than a and c')
else:
    print('c is greater than a and b')

# 4. Define a dictionary with at least 6 key value pairs and print the first the 1 the 2 and the 6 values from the dict.
qa_team = {'Andreea': 'Hello Andreea',
           'Andrei': 'Hello Andrei',
           'Lidia': 'Hello Lidia',
           'Sergiu': 'Hello Sergiu',
           'Daniel': 'Hello Daniel',
           'Gogo': 'Hello Gogo',
           'Cora': 'Hello Cora'
           }  # dictionary

print('Exercise part 1 #4 *****************')
# version 1
print(qa_team['Andreea'] + ' ' + qa_team['Andrei'] + ' ' + qa_team['Gogo'])
# version 2
print(qa_team.get('Andreea', 'You are not Andreea'))
print(qa_team.get('Andrei', 'You are not Andrei'))
print(qa_team.get('Gogo', 'You are not Gogo'))

# 5. Check if a number is odd or even and print if the number is even or odd.( Hint %2==0)
case_1_num = 65443
case_2_num = 6542

print('Exercise part 1 #5 *****************')
if case_1_num % 2 == 0:
    print(f'{case_1_num} is even')
else:
    print(f'{case_1_num} is odd')

if case_2_num % 2 == 0:
    print(f'{case_2_num} is even')
else:
    print(f'{case_2_num} is odd')

# Exercises_part2
# Exercise 1 : Print multiplication table of a given number
# Hint: You need to define a variable number = xxx, and use the range(function) range (1,11,1)
# multiply i with the given number and print the result
# For example, num = 2 so the output should be
# Expected output:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
print('Exercise part 2 #1 *****************')
num_range = range(1, 11)
num = 2

for i in num_range:
    print(i * num)

# Exercise 2: Reverse the following list using for loop
list1 = [10, 20, 30, 40, 50]
# Expected output:
#
# 50
# 40
# 30
# 20
# 10

print('Exercise part 2 #2 *****************')
for i in range(len(list1) - 1, -1, -1):
    print(list1[i])

# Exercise 3: Display numbers from -10 to -1 using for loop
# Expected output:
#
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1

print('Exercise part 2 #3 *****************')
for i in list(range(-10, 0)):
    print(i)
# Exercise 4: Display a message “Done” after successful execution of for loop
# For example, the following loop will execute without any error.
#
# Expected output should be:
# 0
# 1
# 2
# 3
# 4
# Done!

print('Exercise part 2 #4 *****************')
for i in range(5):
    print(i)
else:
    print('Done!')

# Exercise 5: Display the cube of the number up to a given integer
# Given:
#

#
# Expected output:
#
# Current Number is : 1  and the cube is 1
# Current Number is : 2  and the cube is 8
# Current Number is : 3  and the cube is 27
# Current Number is : 4  and the cube is 64
# Current Number is : 5  and the cube is 125
# Current Number is : 6  and the cube is 216

print('Exercise part 2 #5 *****************')
input_number = 6
for i in range(1, input_number + 1):
    print(f'Current Number is : {i} and the cube is {i * i * i}')

# Exercises_part3
# # Exercise 1 :
# # Write a while loop that adds all the numbers up to 10
# # Hint:
#
# counter = 0
# total = 0

print('Exercise part 3 #1 *****************')
counter = 0
total = 0
while counter <= 10:
    total += counter
    counter += 1
print(total)

# # Exercise 2 :
# # Using while loop, if statement and str() function; iterate through the list and if there is a 100,
# # print it with its index number. i.e.:
# # "There is a 100 at index no: 5"
#
# lst = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]

print('Exercise part 3 #2 *****************')
lst = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
i = 0
while i < len(lst):
    if lst[i] == 100:
        print(f'There is a {str(lst[i])} at index no: {i}')
    i += 1

#
# # Exercise 3 :
# # Display the numbers from 1 to 10 except 6.
# # Expected Output: 1 2 3 4 5 7 8 9 10

print('Exercise part 3 #3 *****************')
i = 0
while i < 10:
    i += 1
    if i == 6:
        continue
    print(i)

# # Exercise 4 :
# # Use .pop to print the given list backwards

klass = ['Oana', 'Andreea', 'Lidia', 'Daniel', 'SRJ', 'Andrei P.', 'Andrei C.', 'Gogo']

print('Exercise part 3 #4 *****************')
while len(klass):
    print(klass.pop(-1))

# # Exercise 4.1:
# # Use .pop to the same list given at Ex5 and create a while loop to see how is paying attention in Class or not
print('Exercise part 3 #4.1 *****************')
klass = ['Oana', 'Andreea', 'Lidia', 'Daniel', 'SRJ', 'Andrei P.', 'Andrei C.', 'Gogo']
pays_attention_in_class = 'SRJ'
i = 0
while i < len(klass):
    if klass[i] == pays_attention_in_class:
        print(f'{klass.pop(i)} is paying attention in class')
    i += 1
else:
    print('No one is in class')


# # Exercise 5:
# #  Using the same list as the list from the ex5 check if a certain person is 'in_class_or_not'
# # Hint: Use 'in' in order to check
print('Exercise part 3 #5 *****************')
klass = ['Oana', 'Andreea', 'Lidia', 'Daniel', 'SRJ', 'Andrei P.', 'Andrei C.', 'Gogo']
in_class_or_not = ['Oana', 'Gogo']
i = 0
while i < len(klass):
    if klass[i] in in_class_or_not:
        print(f'{klass[i]} is in class')
    i += 1
