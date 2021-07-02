print('Start Foo Bar $$$')

## Ex 1
# if 'foo' in ['bar', 'air', 'quiz']:
#     print('I am a part of the group')
#     print('or am I?')
# print('Is this really who i am ')

## Ex 2
# print('Start Does this line execute')
# if 'foo' in ['foo', 'air', 'tesla']:
#     print('Outer')
#     if 10 < 20:
#         print('')
#         # ...

## Ex 3 If Else

# print('Start if Statement / else Statement')
#
# x = 20
# if x < 50:
#     print('x is smaller than 50 first condition')
# else:
#     print('x is larger than life')
#
# print('End if Statement / else Statement')

## Ex 4
# name = 'Sergiu'
#
# if name == 'Andreea':
#     print('Hello Andreea and be well :D')
# elif name == 'Lidia':
#     print('Hello Lidia and be well :D')
# elif name == 'Andrei':
#     print('Hello Lidia and be well :D')
# else:
#     print(f"I do not know who you are {name}")

## Ex 5
# names = {'Andreea': 'Hello Andreea',
#          'Lidia': 'Hello Lidia',
#          'Daniel': 'Hello Daniel',
#          'Srj': 'Hello Srj',
#          }
# print(names.get('Lidia'), 'Do i know or do i ? who are you')
#
# new_name = 'Gogo'
# print(names.get(new_name, f'Do you know who i am? i am not in this class {new_name}'))

## Ex 6
# class_pres = 0
#
# if class_pres == 1:
#     print('Andrei');print('Andreea');print('Andrei P')
# elif class_pres == 2:
#     print('Lidia');print('Daniel');print('Srj')
# elif class_pres == 3:
#     print('Gogo');print('All alone')
# elif class_pres == 4:
#     print('Yeey');print('Everyone is in class')
# else:
#     print('Really no one is in class')

# if 'Gogo' in 'Gogo is present in this class': print('yes');print('no');print('who knows')

##Ex 7
monthly_income = 100
monthly_expenses = 500

print('you are in the green go an spend') if monthly_income > monthly_expenses else print("=") \
    if monthly_income == monthly_expenses else print('Stop it')


# monthly_expenses = 200
# fun_expenses = 33
# monthly_income = 500