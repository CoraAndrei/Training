# print('Start Foo Barr $$$$')
#
# # Example 1
# if 'foo' in ['bar', 'air', 'quiz']:
#     print('I am a part of the group')
#     print('or am i')
# print('Is this really who i am?')
#
# print('End Foo Barr $$$$')
#
# print('*****************************************')
# # Example 2
# print('Start does this line execute')
# if 'foo' in ('foo', 'air', 'tesla'):
#     print('Outer condition True')
#     if 10 > 20:
#         print('Inner Condition')
#
#     print('Between Inner Condition')
#
#     if 10 < 20:
#         print('Inner Condition')
#
#     print('End of outer condition')
# print('After Condition')
#
# print('End do lines execute')
#
# print('*****************************************')
# Example 2
#
# print('Start if statement / else Statement')
#
# x = 20
# if x < 50:
#     print('x is smaller then 50 first condition')
# else:
#     print('x is larger then life')
#
# print('End if Statement / else Statement')

# #Example 4
#
# name = 'Andrei P.'
# if name == 'Andreea':
#     print('Hello Andreea and be well :D')
# elif name == 'Lidia':
#     print('Hello Lidia and be well :D')
# elif name == 'Andrei P.':
#     print('Hello Andrei P. and be well :D')
# elif name == 'Daniel':
#     print('Hello Daniel. and be well :D')
# elif name == 'Srj :D':
#     print('Hello Srj :D. and be well :D')
# else:
#     print(f'I do not know who you are ### {name} ###')
#
# # Example 5
#
# names = {'Andreea': 'Hello Andreea',
#          'Andrei': 'Hello Andrei P',
#          'Lidia': 'Hello Lidia',
#          'Daniel': 'Hello Daniel',
#          'Srj': 'Hello Srj',
#          }
# print(names.get('Andrei'), 'Do I know or do I? who are you')
#
# new_name = 'Gogo'
# print(names.get(new_name, f'Dyou know who I am? I am not in this class {new_name}'))
#
# # Example 6
#
# class_presence = 0
#
# if class_presence == 1:
#     print('Andrei');print('Andreea');print('Srj')
# elif class_presence == 2:
#     print('Lidia');print('Daniel');print('Andrei P')
# elif class_presence == 3:
#     print('Gogo');print('All Alone')
# elif class_presence == 4:
#     print('Yeey');print('Everyone is in Class')
# else:
#     print('Really No one is in class X')
#
# print('###')
# if 'Gogo' in 'Gogo is present in this class': print('yes');print('No');print('Who knows')
#
# class_presence == 7
# print('Andrei C') if class_presence == 7 else print('Andrei C is not in class')
#
# # example 7
#
# monthly_income = 100  # $100
# monthly_expenses = 500  # $500
#
#
#
# print('You are in the green go ahead and spend it all !!!') \
#     if monthly_income > monthly_expenses else print('=') \
#     if monthly_income == monthly_expenses else print('Stop it !!! You will go broke.')

# Example 8
monthly_expenses = 200
fun_expenses = 33
monthly_income = 500
remaining_budget = monthly_income - monthly_expenses

if monthly_expenses > fun_expenses and monthly_income > monthly_expenses:
    print('You are in the green go ahead and spend it all !!!')
else:
    print('Stop it !!! You will go broke')

if monthly_expenses > fun_expenses or monthly_income > monthly_expenses:
    print(f'You are in the green go ahead and spend it all !!! You have all money in the world {remaining_budget}')
else:
    print('Stop it !!! You will go broke')