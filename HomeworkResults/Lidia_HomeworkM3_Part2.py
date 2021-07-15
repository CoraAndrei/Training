# Exercise 1 : Print multiplication table of a given number
# Hint: You need to define a variable number = xxx, and use the range(function) range (1,11,1)
# multiply i with the given number and print the result
# For example, num = 2 so the output should be

print('***** Exercise1*****')
var = 3
my_range = range(1, 11)
for i in my_range:
    print(var, 'x', i, '=', var * i)

print('***** Exercise2*****')

# Exercise 2: Reverse the following list using for loop
list1 = [10, 20, 30, 40, 50]

for i in reversed(list1):
    print(i)

print('***** Exercise3*****')

# Exercise 3: Display numbers from -10 to -1 using for loop
list_neg = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
for i in list_neg:
    print(i)

print('***** Exercise4*****')

# Exercise 4: Display a message “Done” after successful execution of for loop
# For example, the following loop will execute without any error.
#
for i in range(5):
    print(i)
else:
    print('Done!')

print('***** Exercise5*****')

# Exercise 5: Display the cube of the number up to a given integer
# Given:
#
input_number = 1
while input_number <= 6:
    print((f'Curent number is :{input_number} and the cube is {input_number ** 3}'))
    input_number += 1
